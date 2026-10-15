<!--
---
type: Guide
---
-->

# 💻 Tasleemat Technical & Developer Guide

Welcome to the technical engineering reference manual for **Tasleemat (تسليمات)**. This document contains developer-focused instructions for the Python SDK, CLI project scaffolder, JSON Schema architecture, OKF Data Packages, automated test suites, and CI/CD documentation workflows.

> 👔 **Looking for Project Management Templates & Guides?** Return to the main **[README.md](../README.md)** or **[README_AR.md](../README_AR.md)**.

---

## 🛠️ 1. Tasleemat CLI Scaffolder & Terminal User Interface (TUI)

Tasleemat is published on PyPI as an enterprise CLI, interactive TUI workstation, and Python library.

### Installation
```bash
# Standard CLI & SDK installation
pip install tasleemat

# Full Interactive TUI Workstation (includes Textual & Arabic BiDi Shaping)
pip install "tasleemat[tui]"
```

### 🖥️ Interactive Bilingual TUI Workstation (`tasleemat tui`)
The full-screen interactive workstation turns Tasleemat into a standalone offline PMO terminal workbench:
```bash
# Launch interactive TUI (English Default)
tasleemat tui

# Launch directly in Arabic with BiDi shaping
tasleemat tui --lang ar
```

#### TUI Features:
- **7 Integrated Workspaces**:
  1. `🚀 Scaffolder`: 5-step visual wizard with live deliverable counts and agent setup.
  2. `📋 Deliverables`: 114 deliverable split-pane explorer with live Markdown and JSON schema preview.
  3. `🚪 Stage-Gates`: Gates 0 to 5 entry/exit criteria and checklist inspector.
  4. `📖 Lexicon`: Instant bilingual search across 114 PMI & Saudi DGA standardized terms.
  5. `🤖 AI Studio`: Prompt playground for drafting deliverables with live LLM generation and markdown export.
  6. `🔑 LLM API`: Unrestricted model configuration for OpenRouter, Google Gemini, OpenAI, Claude, Ollama, and custom OpenAI-compatible endpoints (Groq, DeepSeek, Together, etc.).
  7. `🔌 Agents Hub`: 1-click workspace configuration for **Cursor, Antigravity (AGY), Claude Desktop, VS Code, OpenCode, Cline, Windsurf, and OpenAI CLI replicas**.
  8. `🛡️ Auditor & KPIs`: Interactive governance verification with live progress bars, KPI metric cards, Stage-Gate readiness matrix, and deliverable findings.
- **Real-Time Keybindings**:
  - `F2`: Instant toggle between English and Arabic UI modes with native Arabic cursive shaping (`arabic-reshaper`) and bidirectional algorithm (`python-bidi`).
  - `F1`: Help and keyboard navigation guide.
  - `F10` / `Ctrl+Q`: Safe quit.

### Headless CLI Commands
```bash
# Scaffold a new project (interactive wizard or flags)
tasleemat init --tier 2 --pack agile --lang ar --name "منصة التحول الرقمي" --code "PRJ-2026-01"

# Audit and verify an existing project workspace against PMO governance tiers
tasleemat audit ./projects/PRJ-2026-01 --tier 2 --pack agile

# Run strict audit with JSON export for CI/CD gates
tasleemat audit ./my_project --strict --json --out audit_report.json

# Search deliverable templates by keyword in English or Arabic
tasleemat search "Risk" --lang en
tasleemat search "ميثاق" --lang ar

# List all supported lifecycle phases and form codes
tasleemat list --lang en
```

---

## 🤖 2. Programmatic Python SDK (`tasleemat.ai`)

The `tasleemat.ai` module provides a unified interface for LLM-assisted document generation (supporting OpenRouter, Google Gemini, OpenAI, Anthropic Claude, custom endpoints, or local engines).

### Configuration Setup
```bash
# Configure default LLM API key & provider via CLI (OpenRouter, Gemini, OpenAI, etc.)
tasleemat config set --provider openrouter --model anthropic/claude-3.5-sonnet --key "YOUR_KEY"
tasleemat config set --provider gemini --model gemini-2.5-flash --key "YOUR_GEMINI_API_KEY"
tasleemat config set --provider gemini --model gemini-2.5-flash --key "YOUR_GEMINI_API_KEY"

# Or configure OpenAI
tasleemat config set --provider openai --model gpt-4o --key "YOUR_OPENAI_KEY"
```

### SDK Code Example
```python
import tasleemat

# 1. List and filter canonical artifacts
artifacts = tasleemat.list_artifacts(phase="03", tier="2")
for a in artifacts:
    print(a.artifact_id, a.name_en, a.name_ar)

# 2. Retrieve artifact definition and specific asset by role
defn = tasleemat.get_artifact_definition("PMO-03.01")
template_text = tasleemat.get_artifact_asset("PMO-03.01", role="template", lang="en")
prompt_text   = tasleemat.get_artifact_asset("PMO-03.01", role="prompt",   lang="ar")

# 3. Retrieve standardized bilingual PMO terminology
pmo_terms = tasleemat.get_lexicon(category="Governance")

# 4. Validate completed artifact payload (strict or draft mode)
report = tasleemat.validate_artifact_data("PMO-03.01", {"artifact_id": "PMO-03.01", ...}, mode="strict")
print("Valid:", report.valid, "Errors:", report.errors)

# 5. Render offline styled HTML document
html_doc = tasleemat.render_artifact("PMO-03.01", lang="ar")
```

### AI Generation Client (`tasleemat.ai`)
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
| **`test_consumer_interface.py`** | Programmatic catalog discovery, bilingual asset loading, completed data validation, rendering |
| **`test_maharat_integration_contract.py`** | Simulated downstream integration verifying stable ID lookup, role asset access, draft mode, and error behavior |
| **`test_wheel_clean_install.py`** | Isolated wheel build, clean venv installation, and repository-free execution |
| **`test_parity.py`** | 1:1 English/Arabic structural symmetry across all 8 phases and 114 form folders |
| **`test_schemas.py`** | JSON schema parsing, top-level keys, field definitions, and JSON-CSV alignment |
| **`test_okf_datapackage.py`** | Frictionless JSON Schema standard compliance for all 228 package resources |
| **`test_governance_templates.py`** | Executive Document Control tables and relative link integrity |
| **`test_fictional_compliance.py`** | Sample data integrity, non-empty content checks, zero unresolved placeholders |
| **`test_cli_and_exporters.py`** | Multi-tier project scaffolding, parameter substitution, and catalog search |
| **`test_documentation.py`** | 24 operational manuals, LEXICON integrity, and repository Markdown link integrity |

---

## 🛠️ 5. Documentation Architecture

Tasleemat follows a hybrid **Repository-First & Static Portal** documentation architecture. All substantive project management manuals, stage-gate checklists, RACI matrices, and deliverable guides reside directly within the [`docs/`](README.md) and [`forms/`](forms/en/index.md) directories as native GitHub-flavored Markdown.

Additionally, an interactive static HTML documentation portal is automatically generated from these markdown sources via `tools/generate_documentation_portal.py` and deployed to GitHub Pages via continuous integration (`.github/workflows/deploy-docs.yml`).

---

## 🤝 6. Downstream Consumer Integration (e.g., Maharat)

Tasleemat serves as an upstream, read-only foundation for downstream skill runners and methodology agents (such as **Maharat**).

### Responsibility Boundaries
- **Tasleemat owns**: Stable artifact identities (`PMO-03.01`), read-only templates, practitioner guides, prompt specifications, tabular data dictionaries, companion structural JSON schemas, and offline HTML rendering.
- **Maharat owns**: Workflow orchestration, PMBOK methodological guidance, evidence sufficiency assessments, cross-artifact alignment checks, and human sign-off state.

### Explicit Non-Claims
Structural validity verified by Tasleemat does **NOT** establish:
1. PMI standard compliance or formal institutional certification.
2. Business or technical evidence sufficiency.
3. Methodological suitability for a specific project context.
4. Human executive authorization or stage-gate approval.

### Two-Tier Validation Architecture
1. **Tier 1 — Tasleemat Structural Checks**: Required JSON fields, primitive data types, enum bounds, string formats, array minItems constraints.
2. **Tier 2 — Maharat Suitability Checks**: Evaluation of whether project facts are current, sources are non-conflicting, assumptions are justified, and deliverables are complete.


---

<div align="center">
  <sub>Maintained by <a href="https://github.com/fakhruldeen">Fakhruldeen</a> • Open Source under MIT License</sub>
</div>
