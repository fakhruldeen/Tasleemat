# 💻 Tasleemat Technical & Developer Guide

Welcome to the technical engineering reference manual for **Tasleemat (تسليمات)**. This document contains developer-focused instructions for the Python SDK, CLI project scaffolder, JSON Schema architecture, OKF Data Packages, automated test suites, and CI/CD documentation workflows.

> 👔 **Looking for Project Management Templates & Guides?** Return to the main **[README.md](README.md)** or **[README_AR.md](README_AR.md)**.

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

---

## 🧪 4. Automated Testing Suite

Tasleemat features an extensive automated unit and integration test suite (`tests/`) covering 100% of all 102 forms, 204 reference examples, JSON schemas, OKF data packages, and CLI commands.

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
| **`test_parity.py`** | 1:1 English/Arabic structural symmetry across all 8 phases and 102 form folders |
| **`test_schemas.py`** | JSON schema parsing, top-level keys, field definitions, and JSON-CSV alignment |
| **`test_okf_datapackage.py`** | Frictionless JSON Schema standard compliance for all 204 package resources |
| **`test_governance_templates.py`** | Executive Document Control tables and relative link integrity |
| **`test_fictional_compliance.py`** | Sample data integrity, non-empty content checks, zero unresolved placeholders |
| **`test_cli_and_exporters.py`** | Multi-tier project scaffolding, parameter substitution, and catalog search |
| **`test_documentation.py`** | 24 operational manuals, LEXICON integrity, and MkDocs navigation |

---

## 🛠️ 5. Documentation Portal Generator

The static documentation site ([fakhr.me/Tasleemat/](https://fakhr.me/Tasleemat/)) is generated using MkDocs Material and custom Python tooling.

```bash
# Regenerate documentation assets and Navigation structure
python3 tools/generate_documentation_portal.py

# Build static HTML site
mkdocs build --clean

# Serve site locally for development
mkdocs serve
```

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/fakhruldeen">Fakhruldeen</a> • Open Source under MIT License</sub>
</div>
