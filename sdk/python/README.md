# 🚀 Tasleemat (تسليمات) — Enterprise Bilingual PMO Toolkit & AI Automation Library

[![PyPI version](https://badge.fury.io/py/tasleemat.svg)](https://pypi.org/project/tasleemat/)
[![Live Documentation Portal](https://img.shields.io/badge/Live_Portal-fakhr.me%2FTasleemat-2563eb?logo=google-chrome&logoColor=white)](https://fakhr.me/Tasleemat/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23193523.svg)](https://doi.org/10.5281/zenodo.23193523)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PMI Standard](https://img.shields.io/badge/Standard-PMI%20PMBOK®%206th%2C%207th%20%26%208th%20Edition-0052cc)](https://fakhr.me/Tasleemat/)
[![Templates](https://img.shields.io/badge/Templates-102%20Bilingual%20Pairs%20(204%20Total)-059669)](https://fakhr.me/Tasleemat/)

**Tasleemat (تسليمات)** is a production-grade, open-source Project Management Office (PMO) operating system and Python library designed for **Project Managers, PMO Directors, Business Leaders, Data Engineers, and AI Engineers**.

It provides **102 standardized, bilingual (English & Arabic) project management deliverables** (204 synchronized form bundles total) covering the complete project lifecycle—from strategic portfolio roadmaps and business cases to scope baselines, risk registers, stage-gate reviews, Earned Value Analysis (EVA), and project closeouts.

---

## 🌟 Core Highlights

- **📚 102 Full-Lifecycle Artifacts (204 Form Bundles):** Complete 1-to-1 English and Arabic coverage across 8 lifecycle phases and 12 planning domains.
- **⚡ PMI PMBOK® Guide Aligned (6th, 7th & 8th Edition Ready):** Fully compliant with PMI standards, ISO 21500/21502 governance, Agile/Lean practice guides, ESG sustainability tracking, and NIST AI RMF.
- **🤖 Built-in AI Generation Engine (`tasleemat.ai`):** Instantly auto-fill publication-ready project documents using Google Gemini, OpenAI GPT-4, Anthropic Claude, or local Ollama LLMs.
- **📂 5-File Synchronized Artifact Bundles:** Every deliverable includes a printable Markdown template, practitioner writing guide, LLM prompt instruction, machine-readable JSON schema, and tabular CSV dictionary.
- **🚀 Global CLI Project Scaffolder (`tasleemat`):** Interactively or programmatically scaffold complete project workspaces tailored to your project size (Enterprise, Standard, Lean, Agile/AI).
- **🇸🇦 100% Arabic (RTL) Parity:** Native Arabic translations mapped directly to official PMI Lexicon terms.

---

## 💻 CLI Installation & Complete Usage Reference

Install the official package globally via `pip`:

```bash
pip install tasleemat
```

### 1. Help & Parameter Reference (`--help` / `-h` / `help`)
View detailed documentation for all CLI commands, arguments, choices, and practical examples:

```bash
# Complete CLI manual for all commands & arguments
tasleemat --help
tasleemat -h
tasleemat help

# Specific subcommand help
tasleemat help init
tasleemat generate --help
```

### 2. Project Workspace Scaffolding (`tasleemat init`)
Scaffold a complete project workspace with pre-populated bilingual templates matching your project tier:

```bash
# Interactive scaffolding wizard
tasleemat init

# Fast-track command with flags (Tier 2, Agile Pack, Arabic templates)
tasleemat init --tier 2 --pack agile --lang ar --name "منصة التحول الرقمي" --code "PRJ-2026-01" --out ./My_Project
```

#### Supported Scaffolding Tiers:
- **Tier 1 (Enterprise):** 52+ full governance baselines for complex corporate programs.
- **Tier 2 (Standard Core):** 14+ essential baselines for medium-sized projects.
- **Tier 3 (Lean / Fast-Track):** 6 core deliverables for quick execution.

#### Supported Methodology Packs:
- `general`: Standard PMBOK alignment.
- `agile`: Scrum, Kanban, Sprint Planning & Retrospectives.
- `ai`: AI Governance, Ethics, Model Cards & Readiness Assessments.
- `predictive`: Waterfall & Earned Value Management (EVM).
- `hybrid`: Blended Agile/Predictive controls.

---

### 3. Catalog Search & Listing (`tasleemat search` / `tasleemat list`)
Browse and search forms by keyword or PMO form code:

```bash
# Search deliverable forms by keyword
tasleemat search "Risk" --lang en
tasleemat search "ميثاق" --lang ar

# List all 102 forms in catalog
tasleemat list --lang en
```

---

### 4. LLM AI Configuration (`tasleemat config`)
Configure your default LLM AI provider and API credentials (stored securely at `~/.tasleemat/config.json`):

```bash
# Configure Google Gemini
tasleemat config set --provider gemini --model gemini-2.5-flash --key "YOUR_GEMINI_API_KEY"

# Or configure OpenAI
tasleemat config set --provider openai --model gpt-4o --key "YOUR_OPENAI_KEY"

# View current configuration
tasleemat config show
```

---

### 5. Automated AI Document Generation (`tasleemat generate`)
Auto-fill publication-ready project deliverables directly from meeting notes:

```bash
# Auto-fill Project Charter (PMO-03.01) from meeting notes
tasleemat generate --form PMO-03.01 --notes ./meeting_notes.txt --out ./03_01_Project_Charter.md

# Test offline with mock engine (no API tokens consumed)
tasleemat generate --form PMO-03.01 --notes "Enterprise Cloud Migration" --mock
```

---

### 6. Automated Test Suite (`tasleemat test`)
Execute the built-in repository verification suite:

```bash
tasleemat test -v
```

---

## 🤖 Programmatic Python SDK (`tasleemat.ai`)

You can also import `tasleemat.ai` directly into custom Python pipelines, internal dashboards, or automated AI workflows:

```python
from tasleemat.ai import AIClient

# Initialize client (resolves API credentials automatically)
client = AIClient(provider="gemini", model="gemini-2.5-flash")

# Auto-fill a PMO deliverable
charter_markdown = client.generate(
    prompt="Generate Project Charter for $2M E-Commerce Platform Modernization",
    system_instruction="You are an enterprise PMO Director. Adhere strictly to PMI PMBOK standards."
)

print(charter_markdown)
```

### Data Engineering & Metadata Ingestion
Ingest the master bilingual lexicon or individual form schemas into `pandas` or PowerBI:

```python
import json
import pkg_resources

# Access bundled LEXICON registry
lexicon_path = pkg_resources.resource_filename("tasleemat", "docs/LEXICON.json")
with open(lexicon_path, "r", encoding="utf-8") as f:
    lexicon_data = json.load(f)

print(f"Loaded {len(lexicon_data)} registered deliverable forms.")
```

---

## 📦 5-File Synchronized Artifact Architecture

Inside every form folder (e.g., `forms/en/03_Initiating/01_Project_Charter/`), Tasleemat provides 5 synchronized files:

| File Type | Pattern | Purpose |
| :--- | :--- | :--- |
| **Printable Template** | `*_Template.md` / `*_قالب.md` | Human-facing document structure with sign-off headers |
| **Practitioner Guide** | `*_Guide.md` / `*_دليل.md` | In-depth operational guide & dependency rules |
| **LLM Generation Prompt** | `*.md` | Engineered system prompt for automated LLM drafting |
| **JSON Data Schema** | `*.json` | Machine-readable schema for API integrations & validation |
| **Tabular Dictionary** | `*.csv` | 4-column structured dictionary for Excel/PowerBI ingestion |

---

## 🗺️ Project Lifecycle Overview (102 Forms)

| Phase Code | Phase Name | Deliverables Count | Focus Area |
| :---: | :--- | :---: | :--- |
| **00** | **Program & Portfolio Management** | **6 Forms** | Portfolio roadmaps, OKR alignment, capacity planning, PMO maturity |
| **01** | **Business & Value Delivery** | **4 Forms** | Business cases, benefits realization plans, value registers |
| **02** | **Project Approach & Tailoring** | **6 Forms** | Tailoring strategy, AI governance, AI ethics baselines, model cards |
| **03** | **Initiating** | **5 Forms** | Project charter, product vision, assumption log, stakeholder register |
| **04** | **Planning** | **52 Forms** | 12 Domains: Scope, Schedule, Cost, Quality, Resource & Psychological Safety, Communications, Risk, Procurement, Stakeholder, OCM, Sustainability/ESG |
| **05** | **Executing** | **12 Forms** | Issue log, change requests, retrospectives, team performance |
| **06** | **Monitoring & Controlling** | **12 Forms** | Status reports, Earned Value (EVA), UAT signoff, flow metrics |
| **07** | **Closing** | **5 Forms** | Lessons learned, contract closeouts, operational handover |

---

## 📜 Standards & Compliance Alignment

- **PMI PMBOK® Guide** (6th, 7th & 8th Edition Ready)
- **ISO 21500:2021 & ISO 21502:2020** (Project & Portfolio Governance)
- **Agile & Lean Practice Guides** (Scrum, Kanban, Value Streams)
- **NIST AI Risk Management Framework & EU AI Act** (AI Artifacts)
- **UN Sustainable Development Goals & ESG Frameworks**

---

## 🔗 Useful Links & Citation

- **🌐 Live Web Documentation Portal:** [fakhr.me/Tasleemat/](https://fakhr.me/Tasleemat/)
- **🐙 GitHub Repository:** [github.com/fakhruldeen/Tasleemat](https://github.com/fakhruldeen/Tasleemat)
- **📚 Citation (Zenodo DOI):** [10.5281/zenodo.23193523](https://doi.org/10.5281/zenodo.23193523)

> Mohamed (Fouad) Fakhruldeen. (2026). fakhruldeen/Tasleemat: v2.2.0 [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23193523

---

<div align="center">
  <sub>Open Source under <a href="https://opensource.org/licenses/MIT">MIT License</a>. Maintained by <a href="https://github.com/fakhruldeen">Fakhruldeen</a>.</sub>
</div>
