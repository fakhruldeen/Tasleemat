# 🚀 Tasleemat (تسليمات) — Enterprise Bilingual PMO Operating System & Python SDK

[![PyPI version](https://badge.fury.io/py/tasleemat.svg)](https://pypi.org/project/tasleemat/)
[![Python Versions](https://img.shields.io/pypi/pyversions/tasleemat.svg)](https://pypi.org/project/tasleemat/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PMI Standard](https://img.shields.io/badge/Standard-PMI%20PMBOK®%206th%2C%207th%20%26%208th%20Edition-0052cc)](https://github.com/fakhruldeen/Tasleemat)
[![Deliverables](https://img.shields.io/badge/Deliverables-114%20Bilingual%20Pairs%20(228%20Total)-059669)](https://github.com/fakhruldeen/Tasleemat)
[![Data Package](https://img.shields.io/badge/Data%20Package-OKF%20Frictionless-orange)](https://github.com/fakhruldeen/Tasleemat/blob/main/datapackage.json)
[![MCP Server](https://img.shields.io/badge/MCP%20Server-Standard%20Protocol-7c3aed)](https://github.com/fakhruldeen/Tasleemat/blob/main/docs/MCP_INTEGRATION.md)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23193523.svg)](https://doi.org/10.5281/zenodo.23193523)

**Tasleemat (تسليمات)** is a production-grade, open-source Project Management Office (PMO) operating system and programmatic Python library designed for **Project Managers, PMO Directors, Business Leaders, Data Engineers, and AI Agents**.

It provides **114 standardized, bilingual (English & Arabic) project management deliverables** (228 synchronized form bundles total) covering the complete project lifecycle—from strategic portfolio roadmaps and business cases to scope baselines, risk registers, stage-gate reviews, Earned Value Analysis (EVA), and project closeouts.

With **Version 2.4.1**, Tasleemat delivers a **complete programmatic Python API**, standard **Model Context Protocol (MCP)** server, standalone offline rendering, structural JSON schema data contracts with strict and draft validation modes, and machine-readable downstream integration contracts for AI agent orchestrators (such as **Maharat**).

---

## 🌟 What's New in v2.4.1

- ⚡ **Native Model Context Protocol (MCP) Server:** Plug Tasleemat directly into Claude Desktop, Cursor, and OpenCode via `tasleemat-mcp` or `python -m tasleemat.mcp`.
- 🧩 **First-Class Programmatic Python API:** Access all 114 artifact definitions, bundles, templates, guides, prompts, and schemas directly via `import tasleemat`.
- 🔍 **Structural Data Validation Engine:** Validate artifact data payloads against formal Draft 2020-12 companion JSON schemas with field-level error reporting (`validate_artifact_data`).
- 📝 **Strict & Draft Validation Modes:** Support production sign-offs with strict validation while enabling in-progress agent workflows with non-blocking draft warnings.
- 🎨 **Standalone Document Rendering:** Render artifacts to styled, print-ready HTML with zero external services and strict immutability protection for source templates (`render_artifact`).
- 🤖 **Agent Orchestrator Integration (Maharat Ready):** Machine-readable catalog, stable artifact IDs (`PMO-XX.YY`), cryptographic SHA-256 content fingerprints, and standardized bilingual terminology getters (`get_lexicon`).
- 🔒 **Absolute Immutability & Traceability:** Guaranteed immutability of the source `forms/` catalog with runtime guards against unintended overwrites.

---

## 💻 Installation

Install the official package from PyPI:

```bash
pip install tasleemat
```

Verify your installation:

```bash
tasleemat --help
```

---

## 🚀 Python SDK Quickstart

### 1. Catalog Discovery & Metadata Retrieval

Discover registered PMO deliverables and inspect their phase, tailoring profile, and cryptographic fingerprints:

```python
import tasleemat

# List all 114 registered artifacts
artifacts = tasleemat.list_artifacts()
print(f"Discovered {len(artifacts)} standardized deliverables.")

# Filter by project lifecycle phase
planning_artifacts = tasleemat.list_artifacts(phase="Planning")

# Retrieve detailed metadata for a specific deliverable
charter = tasleemat.get_artifact_definition("PMO-03.01")
print(charter["name_en"])      # "PROJECT CHARTER"
print(charter["name_ar"])      # "ميثاق المشروع"
print(charter["phase"])        # "Initiating"
print(charter["tier"])         # "Tier 3 (Lean)"
print(charter["fingerprint"])   # SHA-256 content fingerprint
```

### 2. Bilingual Asset Retrieval

Retrieve templates, guides, AI prompts, data schemas, and dictionaries without parsing directory structures:

```python
from tasleemat import get_artifact_asset, get_artifact_assets

# Retrieve specific asset directly (by role and language)
# Roles: "template", "guide", "prompt", "schema", "dictionary", "example"
en_template = get_artifact_asset("PMO-03.01", role="template", lang="en")
ar_template = get_artifact_asset("PMO-03.01", role="template", lang="ar")

# Or fetch the entire asset bundle
bundle_ar = get_artifact_assets("PMO-03.01", lang="ar")
print(bundle_ar.get_guide_content())
schema_dict = bundle_ar.get_schema_data()
```

### 3. Structural Data Validation (`strict` vs `draft`)

Validate structured project data against formal companion schemas:

```python
from tasleemat import validate_artifact_data

project_charter_data = {
    "artifact_id": "PMO-03.01",
    "project_name": "Digital Transformation Initiative",
    "project_code": "PRJ-2026-001",
    "project_manager": "Sarah Jenkins, PMP",
    "sponsor": "Executive Committee",
    "business_need": "Modernize legacy transaction platforms to reduce latency by 40%.",
    "project_purpose": "Deploy enterprise microservices architecture.",
    "objectives": [
        {"objective": "Migrate 10 core services", "target_date": "2026-12-31"}
    ],
    "high_level_requirements": ["99.99% SLA availability", "Zero data loss during cutover"],
    "summary_budget": {"total_budget": 1500000.0, "currency": "SAR"}
}

# Strict Mode: For formal stage-gate approvals and final baselines
report = validate_artifact_data("PMO-03.01", project_charter_data, mode="strict")
if report.valid:
    print("✅ Document structure is strictly valid for stage-gate submission!")
else:
    for err in report.errors:
        print(f"❌ Error at {err.field_path}: {err.message} (Code: {err.code})")

# Draft Mode: For intermediate agent loops or draft authoring (produces warnings, does not fail)
draft_report = validate_artifact_data("PMO-03.01", {"project_name": "Draft Project"}, mode="draft")
print(f"Draft valid: {draft_report.valid}, Warnings: {len(draft_report.warnings)}")
```

### 4. Standalone Offline Document Rendering

Render any artifact to publication-ready styled HTML:

```python
from tasleemat import render_artifact

# Render Project Charter to a styled, print-ready HTML document
html_output = render_artifact("PMO-03.01", lang="ar", out_path="./output/charter_ar.html")
print("Rendered artifact saved to ./output/charter_ar.html")
```

### 5. Standardized Bilingual PMO Terminology

Access standardized PMI/DGA English-Arabic terminology mappings:

```python
from tasleemat import get_lexicon

# Retrieve full bilingual PMO lexicon
lexicon = get_lexicon()
print(f"Loaded {len(lexicon)} terms.")

# Filter by lifecycle category
initiating_terms = get_lexicon(category="Initiating")
for item in initiating_terms[:3]:
    print(f"{item['en_name']} <---> {item['ar_name']}")
```

---

## 🛠️ Global Command-Line Interface (CLI)

The `tasleemat` CLI provides workspace scaffolding, form searches, AI document auto-generation, and testing:

```bash
# 1. Complete CLI reference
tasleemat --help

# 2. Interactive project workspace scaffolder
tasleemat init

# 3. Fast-track automated scaffolding (Tier 2 Standard, Agile Pack, Arabic templates)
tasleemat init --tier 2 --pack agile --lang ar --name "منصة السحابة" --code "PRJ-2026-02" --out ./My_Project

# 4. Search deliverable forms by keyword
tasleemat search "Risk" --lang en
tasleemat search "ميثاق" --lang ar

# 5. List all 114 forms in catalog
tasleemat list --lang en

# 6. Auto-fill project deliverables using AI from meeting notes
tasleemat generate --form PMO-03.01 --notes ./meeting_notes.txt --out ./Project_Charter.md

# 7. Run automated test suite
tasleemat test -v
```

---

## 📦 5-File Synchronized Artifact Architecture

Every one of the 114 deliverables is organized as a synchronized bundle of 5 files:

| File Type | File Pattern | Purpose |
| :--- | :--- | :--- |
| **Printable Template** | `*_Template.md` / `*_قالب.md` | Human-facing document structure with sign-off headers and Document Control tables |
| **Practitioner Guide** | `*_Guide.md` / `*_دليل.md` | In-depth operational guide, field-by-field instructions, and dependency rules |
| **LLM Generation Prompt** | `*.md` | Engineered system prompt for automated AI drafting and LLM completion |
| **JSON Data Schema** | `*.json` | Machine-readable schema specification for API ingestion and validation |
| **Tabular Dictionary** | `*.csv` | 4-column structured dictionary for spreadsheet, PowerBI, and database ingestion |

---

## 🗺️ Project Lifecycle Overview (114 Deliverables)

| Phase Code | Phase Name | Deliverables Count | Focus Area |
| :---: | :--- | :---: | :--- |
| **00** | **Program & Portfolio Management** | **6 Forms** | Portfolio roadmaps, OKR alignment, capacity planning, PMO maturity |
| **01** | **Business & Value Delivery** | **4 Forms** | Business cases, benefits realization plans, value registers |
| **02** | **Project Approach & Tailoring** | **6 Forms** | Tailoring strategy, AI governance, AI ethics baselines, model cards |
| **03** | **Initiating** | **5 Forms** | Project charter, product vision, assumption log, stakeholder register |
| **04** | **Planning** | **52 Forms** | 12 Domains: Scope, Schedule, Cost, Quality, Resources, Communications, Risk, Procurement, Stakeholder, OCM, Sustainability/ESG |
| **05** | **Executing** | **12 Forms** | Issue log, change requests, retrospectives, team performance |
| **06** | **Monitoring & Controlling** | **12 Forms** | Status reports, Earned Value Analysis (EVA), UAT signoff, flow metrics |
| **07** | **Closing** | **5 Forms** | Lessons learned, contract closeouts, operational handover, archive |

---

## 🤖 Using Tasleemat & OKF with LLMs (Claude, ChatGPT, OpenCode & Coding Agents)

Tasleemat is natively engineered for **Generative AI workflows**, **Large Language Models (LLMs)**, and **AI coding assistants** (Claude, ChatGPT, OpenCode, Cursor, GitHub Copilot):

- **In Standard Chat LLMs (Claude & ChatGPT)**:
  - Copy any engineered LLM prompt from `forms/en/` or `forms/ar/` (e.g. `03_01_Project_Charter.md`) and append raw kickoff/meeting notes. The LLM generates a complete, PMI-aligned deliverable with Document Control headers.
  - Upload `forms/` templates and `docs/LEXICON.json` into **Custom GPTs** or **Claude Projects** as persistent institutional knowledge.
- **In Coding Agents & IDEs (Cursor, OpenCode, Windsurf, Cline)**:
  - Connect via native MCP (`tasleemat-mcp`):
    - **Cursor:** Add `tasleemat-mcp` in **Settings** $\rightarrow$ **Features** $\rightarrow$ **MCP**
    - **OpenCode & Cline:** Add `{"mcpServers": {"tasleemat": {"command": "tasleemat-mcp"}}}` to `cline_mcp_settings.json`
    - **Windsurf:** Add `tasleemat-mcp` to `~/.codeium/windsurf/mcp_config.json`
  - Use `@` context referencing (e.g. `@03_01_Project_Charter_Template.md Fill this project charter for...`) to have AI coding agents generate conforming deliverables directly into your workspace.
- **In Multi-Agent Frameworks (CrewAI, LangChain, LlamaIndex)**:
  - **CrewAI Tool:**
    ```python
    from crewai.tools import tool
    import tasleemat

    @tool("PMO Deliverable Retriever")
    def get_pmo_deliverable(artifact_id: str, role: str = "template", lang: str = "en") -> str:
        """Fetches standardized PMO deliverable templates and guides (e.g. PMO-03.01)."""
        return tasleemat.get_artifact_asset(artifact_id, role, lang)
    ```
  - **LangChain Tool:**
    ```python
    from langchain.tools import BaseTool
    from pydantic import BaseModel, Field
    import tasleemat

    class PMOFetchInput(BaseModel):
        artifact_id: str = Field(description="Unique PMO artifact ID, e.g., 'PMO-03.01'")
        role: str = Field(default="template", description="Role: 'template', 'guide', 'prompt', 'schema'")
        lang: str = Field(default="en", description="Language: 'en' or 'ar'")

    class PMOFetchTool(BaseTool):
        name: str = "pmo_fetch_asset"
        description: str = "Retrieve standardized PMBOK-compliant PMO templates and guides in English or Arabic."
        args_schema: type[BaseModel] = PMOFetchInput

        def _run(self, artifact_id: str, role: str = "template", lang: str = "en") -> str:
            return tasleemat.get_artifact_asset(artifact_id, role=role, lang=lang)
    ```
- **Structured Tool Use & Function Calling via OKF**:
  - The root [`datapackage.json`](https://github.com/fakhruldeen/Tasleemat/blob/main/datapackage.json) conforms to the **Open Knowledge Foundation (OKF)** standard. Pass companion JSON schemas into OpenAI Tools or Claude Tool Use parameters to guarantee structured JSON outputs without hallucinated fields.
- **Self-Correction Feedback Loops**:
  - Run `validate_artifact_data` on LLM-generated JSON payloads. If errors occur, pass exact JSON pointer error paths back to the model to self-correct automatically.

---

## 🤖 Integration Architecture for Downstream Agents (e.g. Maharat)

Tasleemat v2.4.0 establishes a clean, decoupled boundary for downstream AI agents and workflow orchestration platforms:

```
┌────────────────────────────────────────────────────────┐
│            DOWNSTREAM AGENTS / MAHARAT                 │
│  - Methodological workflows & PMBOK skill guidance     │
│  - Input suitability, evidence & business checks       │
│  - Stage-gate approvals & multi-agent decisions        │
└───────────────────────────┬────────────────────────────┘
                            │ imports & queries
                            ▼
┌────────────────────────────────────────────────────────┐
│               TASLEEMAT OPERATING SYSTEM               │
│  - 114 Canonical Artifacts & Stable IDs (PMO-XX.YY)    │
│  - Bilingual Templates, Guides & Terminology (Lexicon) │
│  - Structural Data Contracts & JSON Schema Validation  │
│  - Standalone Offline Rendering & Template Preservation│
└────────────────────────────────────────────────────────┘
```

- **Tasleemat owns:** Canonical artifact definitions, stable IDs, templates, structural data schemas, format validation (`strict` and `draft`), bilingual terminology, and offline rendering.
- **Agent Orchestrators (Maharat) own:** Methodological skills, business suitability checks, evidence validation, cross-artifact consistency, and human approval workflows.

---

## 📜 Standards Alignment

- **PMI PMBOK® Guide:** 6th, 7th & 8th Edition alignment.
- **ISO Standards:** ISO 21500:2021 (Project Governance) & ISO 21502:2020 (Project Management).
- **AI Governance:** NIST AI Risk Management Framework (AI RMF 1.0) & EU AI Act readiness.
- **Open Data:** Open Knowledge Foundation (OKF) Frictionless Data Package specification.
- **Saudi DGA PMO Standards:** Terminology aligned with official government digital governance frameworks.

---

## 🔗 Links & Resources

- **GitHub Repository:** [github.com/fakhruldeen/Tasleemat](https://github.com/fakhruldeen/Tasleemat)
- **Interactive Web Portal:** [fakhr.me/Tasleemat](https://fakhr.me/Tasleemat/)
- **Documentation:** [docs/README.md](https://github.com/fakhruldeen/Tasleemat/blob/main/docs/README.md)
- **Zenodo DOI:** [10.5281/zenodo.23193523](https://doi.org/10.5281/zenodo.23193523)

---

<div align="center">
  <sub>Open Source under <a href="https://opensource.org/licenses/MIT">MIT License</a>. Created and maintained by <a href="https://github.com/fakhruldeen">Fakhruldeen</a>.</sub>
</div>
