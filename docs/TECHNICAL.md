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

### 🗂️ The Four Distinct Data & Schema Layers

To prevent architectural ambiguity between form layouts and structured payload validation, Tasleemat defines four distinct data and contract layers:

| Layer | Component | Location / API | Standard / Dialect | Primary Purpose |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Form-Definition Section Schemas** | `forms/{en,ar}/**/*.json` | Custom Section Schema | Defines human-facing form section layouts, field prompts, and Markdown scaffolding rules. |
| **2** | **OKF Data Package Registry** | `datapackage.json` | Frictionless Table Schema | Indexes all 228 bilingual form resources as an Open Knowledge Data Package with FAIR-compliant metadata. |
| **3** | **Companion Completed-Data Schemas** | `tasleemat/schemas/completed/*.json` | JSON Schema Draft 2020-12 | Machine-readable JSON Schemas enforcing types, required fields, formats, and bounds for completed records. |
| **4** | **Runtime Project Payloads** | Client data passed to `validate_artifact_data` | JSON Object / Dict | The actual completed project data payloads created by practitioners or AI agents, validated in strict or draft mode. |

### Completed-Data Schemas (JSON Schema Draft 2020-12)
In addition to the 114 template schema definitions, Tasleemat provides additive companion completed-data schemas for **all 114 lifecycle deliverables** across all 8 phases (100% deliverable coverage). Each deliverable possesses:
- A Draft 2020-12 companion JSON schema in `tasleemat/schemas/completed/{ARTIFACT_ID}.schema.json`.
- Complete valid, invalid, and draft test fixture sets in `tests/fixtures/{valid,invalid,draft}/`.
- Full preflight inspection and runtime support in `validate_artifact_data` and MCP `tasleemat_validate_data`.
- Registered SHA-256 schema fingerprints in canonical `tasleemat/data/catalog.json`.

#### Structural Validation Engine Architecture & Contracts
Completed-data payload validation is executed through `validate_artifact_data` or MCP `tasleemat_validate_data`. The engine operates under strict deterministic contracts:
1. **Zero Mandatory External Dependencies:** Built on a pure-Python validation engine guaranteeing no third-party runtime package requirements.
2. **Schema Preflighting:** Every subschema, optional branch, and array item schema is statically preflighted before payload evaluation to reject unsupported keywords (`UNSUPPORTED_SCHEMA_ASSERTION`), invalid types (`UNSUPPORTED_TYPE_DECLARATION`), or broken patterns (`INVALID_PATTERN_SYNTAX`).
3. **Supported Keywords & Contexts:**
   - **Types:** `object`, `array`, `string`, `integer`, `number`, `boolean`, `null`. Python boolean subclass trap (`isinstance(True, int)`) is strictly guarded. Non-finite numbers (`NaN`, `Infinity`, `-Infinity`) are strictly rejected across untyped, typed, and nested payload values per RFC 8259.
   - **Bounds:** `minimum`, `maximum`, `minLength`, `maxLength`, `minItems`, `maxItems`. Preflight verifies all numeric bounds are finite numbers without float conversion overflow on arbitrary-precision large integers.
   - **Universal Equality:** `enum` and `const` enforced across all data types under strict JSON equality semantics (booleans and numbers never cross-match).
   - **Dialect Alignment & Preflight Enforcement:** Every schema structure accepted by preflight is guaranteed to be executable by runtime validation. In JSON Schema Draft 2020-12, type unions (`type: ["string", "null"]`) and legacy tuple item lists (`items: [...]`) are rejected during preflight (`UNSUPPORTED_TYPE_DECLARATION`, `UNSUPPORTED_SCHEMA_ASSERTION`) to prevent silent runtime skips.
   - **Format Assertion Policy & Registry:** Format keywords operate under explicit assertion mode managed by the centralized registry (`tasleemat.formats`). Preflight independently verifies format validity before payload traversal (`UNSUPPORTED_FORMAT_ASSERTION`, `MALFORMED_SCHEMA_KEYWORD`). Supported formats include:
     - `date`: RFC 3339 `YYYY-MM-DD` with strict leap year and calendar validity.
     - `date-time`: RFC 3339 timezone-aware timestamps (`Z` or `+/-HH:MM`), fractional seconds, and leap seconds.
     - `time`: RFC 3339 partial or offset time (`HH:MM:SS`).
     - `uuid`: RFC 4122 plain hex UUIDs (`8-4-4-4-12`).
     - `uri`: RFC 3986 absolute URIs with valid schemes.
     - `uri-reference`: RFC 3986 absolute or relative URI references without unescaped whitespace.
     - `email`: RFC 5322 standard address subset (`local-part@domain`).
     - `duration`: ISO 8601 duration representations (e.g. `P3Y6M4DT12H30M5S`, `PT15M`).
4. **Availability & Error Outcomes:**
   - `status="unknown_artifact"`: Deliverable ID not found in canonical catalog (`UNKNOWN_ARTIFACT`).
   - `status="unavailable"`: Deliverable registered in catalog but companion schema not yet published (`SCHEMA_UNAVAILABLE`).
   - `status="invalid_schema"`: Companion schema fails preflight inspection.
   - `status="supported"`: Schema preflighted and executed. Returns `valid=True` or `valid=False` with line-item `errors`.
5. **Deterministic Definition Reference Contract:** The `definition_version` parameter strictly accepts:
   - The installed deliverable definition SHA-256 fingerprint (`defn["fingerprint"]`).
   - The companion schema SHA-256 fingerprint (`defn["completed_data_validation"]["schema_fingerprint"]`).
   - The companion schema canonical `$id` URI (documented alias for current installed schema).
   - The authoritative installed release version tag (e.g. `"2.5.0"`, `"v2.5.0"`).
   Unmapped older package versions, arbitrary artifact ID suffixes, and dialect URIs (`https://json-schema.org/draft/2020-12/schema`) are strictly rejected (`UNSUPPORTED_VERSION`).
6. **Traceability Metadata:** `ValidationReport` clearly distinguishes:
   - `package_version`: Authoritative release version (`tasleemat.__version__`).
   - `artifact_id`: Canonical PMO identifier.
   - `schema_version`: Revision/fingerprint of the schema.
   - `schema_id`: Canonical Draft 2020-12 `$id` URI.
   - `schema_dialect`: Canonical Draft 2020-12 `$schema` URI.
   - `schema_fingerprint`: 64-character SHA-256 digest of the companion schema file.
   - `definition_fingerprint`: 64-character SHA-256 digest of the catalog definition.
   - `mode`: `"strict"` or `"draft"`.
   - `status`: Execution capability status.
7. **Immutability Guarantee:** Validation never mutates input dictionaries or catalog cache structures.
8. **MCP Server Protocol Conformance:** The Model Context Protocol (MCP) server strictly conforms to JSON-RPC 2.0:
   - Requires `jsonrpc: "2.0"` envelope.
   - Strictly validates request IDs (`string`, integer `number`, or `null`; integral float IDs like `1.0` are handled cleanly, while rejecting booleans, non-finite floats, fractional floats like `1.5`, and containers with `-32600`).
   - Requires object-shaped named parameters (`dict` or omitted); rejects positional parameter arrays with standard code `-32602` (`Invalid params`).
   - Silently drops unhandled JSON-RPC notifications while returning standard errors for unhandled requests.

### 🤖 Safe AI Drafting & Bounded Re-Validation Loop

Autonomous agents and LLM toolchains generating PMO deliverables should implement a bounded self-correction loop:

```
┌─────────────────┐       ┌────────────────────┐       ┌──────────────────────┐
│ 1. Fetch Schema │ ────> │ 2. LLM Drafts JSON │ ────> │ 3. Preflight Validate│
│    (Layer 3)    │       │    Structured Data │       │    (mode="draft")    │
└─────────────────┘       └────────────────────┘       └──────────┬───────────┘
                                                                  │
                                            ┌─────────────────────┴─────────────────────┐
                                            ▼                                           ▼
                                    [Validation Errors]                          [Valid Payload]
                                            │                                           │
                                            ▼                                           ▼
                                 ┌───────────────────────┐                  ┌───────────────────────┐
                                 │ 4. Targeted Repair    │                  │ 5. Strict Gate Audit  │
                                 │    (Max 2 iterations) │                  │    (mode="strict")    │
                                 └──────────┬────────────┘                  └───────────┬───────────┘
                                            │                                           │
                                            └───────────── Re-validate ────────────────>▼
                                                                                ┌───────────────────────┐
                                                                                │ 6. Render & Human PMO │
                                                                                │    Stage-Gate Signoff │
                                                                                └───────────────────────┘
```

1. **Preflight Draft Validation:** Validate agent drafts using `mode="draft"` to surface missing fields and formatting violations early.
2. **Targeted Repair (Bounded Loop):** Pass specific field validation errors back to the model for surgical correction. Enforce a hard ceiling of 2–3 repair iterations to avoid infinite API loops.
3. **Strict Gate Validation:** Before submitting deliverables for executive stage-gate review, execute validation with `mode="strict"` to guarantee mandatory sections and baseline completeness.
4. **Mandatory Human Sign-off:** AI-generated artifacts serve as accelerator drafts. Official project authorization requires formal sign-off by designated authorities in the Document Control table.

### Mock Generation Notice
The built-in offline mock provider (`AIClient(provider="mock")`) emits structural placeholders labeled prominently with:
`<!-- UNVALIDATED TEST OUTPUT: NOT SUITABLE FOR PRODUCTION USE -->`
Mock deliverables are strictly intended for offline structural pipeline testing and require human PMO review and validation before use.

---

## 🧪 4. Automated Testing Suite

Tasleemat features an extensive automated test suite (`tests/`) covering 100% of all 114 forms, 228 reference examples, JSON schemas, OKF data packages, CLI commands, and MCP protocol integration.

### Running Unit Tests
```bash
# Run complete test suite (130 comprehensive unit & integration tests)
pytest tests/ -v

# Or run via unittest
python3 -m unittest discover -s tests -v

# Or run directly via CLI
tasleemat test -v
```

### Complete Test Suite Modules (15 Modules / 130 Tests)
| Test Module | Coverage & Verification Scope | Tests |
| :--- | :--- | :---: |
| **`test_parity.py`** | 1:1 English/Arabic structural symmetry across all 8 phases and 114 form folders | 3 |
| **`test_schemas.py`** | JSON schema parsing, top-level keys, field definitions, and JSON-CSV alignment | 3 |
| **`test_okf_datapackage.py`** | Frictionless JSON Schema standard compliance for all 228 package resources | 3 |
| **`test_governance_templates.py`** | Executive Document Control tables and relative link integrity | 3 |
| **`test_fictional_compliance.py`** | Sample data integrity, non-empty content checks, zero unresolved placeholders | 3 |
| **`test_cli_and_exporters.py`** | Multi-tier project scaffolding, parameter substitution, and catalog search | 6 |
| **`test_documentation.py`** | 24 operational manuals, LEXICON integrity, and repository Markdown link integrity | 5 |
| **`test_ai_client.py`** | AI client initialization, retry heuristics, prompt formatting, error taxonomy | 5 |
| **`test_consumer_interface.py`** | Public consumer API contract (`tasleemat.list_artifacts`, `get_artifact`, `get_template`, etc.) | 8 |
| **`test_eva.py`** | Earned Value Analysis mathematics (CPI, SPI, CV, SV, EAC, TCPI) and edge cases | 7 |
| **`test_format_handlers.py`** | Markdown, JSON, and CSV export handlers, parameter substitution | 6 |
| **`test_maharat_integration_contract.py`** | Integration contracts for downstream agents and structured tooling | 4 |
| **`test_mcp_server.py`** | MCP JSON-RPC 2.0 stdio server, tool dispatch, error codes, float ID handling | 35 |
| **`test_validation_engine_hardening.py`** | Draft 2020-12 validator hardening, recursive non-finite checks, large integer bounds | 38 |
| **`test_wheel_clean_install.py`** | Clean-environment wheel packaging and CLI installation verification | 1 |
| **Total Test Suite** | **Comprehensive Automated Verification Across All Functional Capabilities** | **130** |

---

## 🛠️ 5. Documentation Architecture

Tasleemat follows a pure **Repository-First** documentation architecture. All substantive project management manuals, stage-gate checklists, RACI matrices, and deliverable guides reside directly within the [`docs/`](README.md) and [`forms/`](forms/en/index.md) directories as native GitHub-flavored Markdown.

For online interactive browsing, an accessible, searchable static HTML portal is generated via `tools/generate_documentation_portal.py` and published at **[https://fakhr.me/Tasleemat/](https://fakhr.me/Tasleemat/)**.

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/fakhruldeen">Fakhruldeen</a> • Open Source under MIT License</sub>
</div>
