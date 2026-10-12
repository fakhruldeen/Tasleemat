<!--
---
type: Guide
---
-->

# 💻 Tasleemat Technical & Developer Guide

Welcome to the technical engineering reference manual for **Tasleemat (تسليمات)**. This document contains developer-focused instructions for the Python SDK, CLI project scaffolder, JSON Schema architecture, OKF Data Packages, automated test suites, and CI/CD documentation workflows.

> 👔 **Looking for Project Management Templates & Guides?** Return to the main **[README.md](../README.md)** or **[README_AR.md](../README_AR.md)**.

---

## 🛠️ 1. Tasleemat CLI Scaffolder & Search Tool

Tasleemat is published on PyPI as an enterprise CLI and Python library.

### Installation
```bash
pip install tasleemat
```

### CLI Commands
```bash
# Scaffold a new project (interactive wizard or flags)
tasleemat init --tier 2 --pack agile --lang ar --name "منصة التحول الرقمي" --code "PRJ-2026-01"

# Search deliverable templates by keyword in English or Arabic
tasleemat search "Risk" --lang en
tasleemat search "ميثاق" --lang ar

# List all supported lifecycle phases and form codes
tasleemat list --lang en
```

---

## 🤖 2. Programmatic Python SDK (`tasleemat.ai`)

The `tasleemat.ai` module provides a unified interface for LLM-assisted document generation (supporting Google Gemini, OpenAI GPT-4, Anthropic Claude, or local mock engines).

### Configuration Setup
```bash
# Configure default LLM API key & provider via CLI
tasleemat config set --provider gemini --model gemini-2.5-flash --key "YOUR_GEMINI_API_KEY"

# Or configure OpenAI
tasleemat config set --provider openai --model gpt-4o --key "YOUR_OPENAI_KEY"
```

### SDK Code Example
```python
from tasleemat.ai import AIClient

# Initialize AI client (automatically reads configured API key or env variables)
client = AIClient(provider="gemini", model="gemini-2.5-flash")

# Generate a publication-ready PMO deliverable (e.g. Project Charter PMO-03.01)
deliverable_md = client.generate(
    prompt="Generate Project Charter for $2M E-Commerce Platform Modernization",
    system_instruction="You are an enterprise PMO Director. Adhere strictly to PMI PMBOK standards."
)

print(deliverable_md)
```

---

## 📦 3. Data Architecture & Synchronized 5-File Bundles

Every single deliverable artifact in `forms/` is organized as a synchronized 5-file bundle:

| File Type | Naming Pattern | Purpose |
| :--- | :--- | :--- |
| **Printable Markdown** | `*_Template.md` / `*_قالب.md` | Human-facing template with metadata headers and sign-off tables |
| **Practitioner Guide** | `*_Guide.md` / `*_دليل.md` | Detailed writing guide and upstream/downstream dependency rules |
| **LLM Prompt** | `*.md` | Machine-readable prompt instruction set for automated LLM drafting |
| **JSON Data Schema** | `*.json` | Machine-readable JSON schema defining section keys and constraints |
| **Data Dictionary** | `*.csv` | Structured 4-column dictionary (`Section,Field,Guidance,LLM_Value`) |

### Ingesting Metadata in Python & PowerBI
```python
import json
import pandas as pd

# Load master bilingual lexicon & form registry
with open("docs/LEXICON.json", "r", encoding="utf-8") as f:
    lexicon = json.load(f)

# Load OKF Data Package metadata
df_resources = pd.read_json("datapackage.json")
```

### Completed-Data Schemas (JSON Schema Draft 2020-12)
In addition to the 114 template schema definitions, Tasleemat provides additive companion completed-data schemas for core lifecycle deliverables:
- `PMO-01.01` (Business Case — Strategic Justification)
- `PMO-03.01` (Project Charter — Project Authorization)
- `PMO-04.01.01` (Project Management Plan — Master Integration Plan)
- `PMO-04.02.05` (Project Scope Statement — Scope Definition & Acceptance)
- `PMO-04.03.01` (Schedule Management Plan — CPM, Cadence & Thresholds)
- `PMO-04.04.01` (Cost Management Plan — Budget, EVM & Thresholds)
- `PMO-04.08.02` (Risk Register — Risk Assessment & Response Strategy)
- `PMO-04.10.01` (Stakeholder Engagement Plan — Matrix & Engagement Actions)
- `PMO-05.01` (Issue Log — Operational Impediments & Corrective Resolutions)
- `PMO-06.01` (Project Status Report — Operational Monitoring)
- `PMO-07.03` (Project or Phase Closeout — Archival & Benefits Handover)

#### Structural Validation Engine Architecture & Contracts
Completed-data payload validation is executed through `validate_artifact_data` or MCP `tasleemat_validate_data`. The engine operates under strict deterministic contracts:
1. **Zero Mandatory External Dependencies:** Built on a pure-Python validation engine guaranteeing no third-party runtime package requirements.
2. **Schema Preflighting:** Every subschema, optional branch, and array item schema is statically preflighted before payload evaluation to reject unsupported keywords (`UNSUPPORTED_SCHEMA_ASSERTION`), invalid types (`UNSUPPORTED_TYPE_DECLARATION`), or broken patterns (`INVALID_PATTERN_SYNTAX`).
3. **Supported Keywords & Contexts:**
   - **Types:** `object`, `array`, `string`, `integer`, `number`, `boolean`, `null`. Python boolean subclass trap (`isinstance(True, int)`) is strictly guarded.
   - **Bounds:** `minimum`, `maximum`, `minLength`, `maxLength`, `minItems`, `maxItems`.
   - **Universal Equality:** `enum` and `const` enforced across all data types.
   - **Format Validation:** `format="date"` strictly enforces ISO 8601 `YYYY-MM-DD` and calendar validity.
4. **Availability & Error Outcomes:**
   - `status="unknown_artifact"`: Deliverable ID not found in canonical catalog (`UNKNOWN_ARTIFACT`).
   - `status="unavailable"`: Deliverable registered in catalog but companion schema not yet published (`SCHEMA_UNAVAILABLE`).
   - `status="invalid_schema"`: Companion schema fails preflight inspection.
   - `status="supported"`: Schema preflighted and executed. Returns `valid=True` or `valid=False` with line-item `errors`.
5. **Definition Reference Contract:** The `definition_version` argument accepts the installed definition SHA-256 fingerprint, schema `$id`, schema fingerprint, or authoritative release version tag. Unknown tags or schema dialect URIs are rejected (`UNSUPPORTED_VERSION`).
6. **Immutability Guarantee:** Validation never mutates input dictionaries or catalog cache structures.

### Mock Generation Notice
The built-in offline mock provider (`AIClient(provider="mock")`) emits structural placeholders labeled prominently with:
`<!-- UNVALIDATED TEST OUTPUT: NOT SUITABLE FOR PRODUCTION USE -->`
Mock deliverables are strictly intended for offline structural pipeline testing and require human PMO review and validation before use.

---

## 🧪 4. Automated Testing Suite

Tasleemat features an extensive automated unit and integration test suite (`tests/`) covering 100% of all 114 forms, 228 reference examples, JSON schemas, OKF data packages, and CLI commands.

### Running Unit Tests
```bash
# Run complete test suite (28 comprehensive unit & integration tests)
python3 -m unittest discover -s tests -v

# Or run directly via CLI
tasleemat test -v
```

### Test Suite Modules
| Test Module | Coverage & Verification Scope |
| :--- | :--- |
| **`test_parity.py`** | 1:1 English/Arabic structural symmetry across all 8 phases and 114 form folders |
| **`test_schemas.py`** | JSON schema parsing, top-level keys, field definitions, and JSON-CSV alignment |
| **`test_okf_datapackage.py`** | Frictionless JSON Schema standard compliance for all 228 package resources |
| **`test_governance_templates.py`** | Executive Document Control tables and relative link integrity |
| **`test_fictional_compliance.py`** | Sample data integrity, non-empty content checks, zero unresolved placeholders |
| **`test_cli_and_exporters.py`** | Multi-tier project scaffolding, parameter substitution, and catalog search |
| **`test_documentation.py`** | 24 operational manuals, LEXICON integrity, and repository Markdown link integrity |

---

## 🛠️ 5. Documentation Architecture

Tasleemat follows a pure **Repository-First** documentation architecture. All substantive project management manuals, stage-gate checklists, RACI matrices, and deliverable guides reside directly within the [`docs/`](README.md) and [`forms/`](forms/en/index.md) directories as native GitHub-flavored Markdown.

The previous GitHub Pages deployment portal has been retired. Documentation is directly accessible, searchable, and navigable within the repository.

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/fakhruldeen">Fakhruldeen</a> • Open Source under MIT License</sub>
</div>
