# 🚀 Tasleemat (تسليمات) — Enterprise Bilingual PMO Operating System & Python SDK

<!-- mcp-name: io.github.fakhruldeen/tasleemat -->

[![PyPI version](https://img.shields.io/pypi/v/tasleemat.svg?style=flat-square&color=blue)](https://pypi.org/project/tasleemat/)
[![Python Versions](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg?style=flat-square)](https://pypi.org/project/tasleemat/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PMI Standard](https://img.shields.io/badge/Standard-PMI%20PMBOK®%206th%2C%207th%20%26%208th%20Edition-0052cc)](https://github.com/fakhruldeen/Tasleemat)
[![Deliverables](https://img.shields.io/badge/Deliverables-114%20Bilingual%20Pairs%20(228%20Total)-059669)](https://github.com/fakhruldeen/Tasleemat)
[![TUI Workstation](https://img.shields.io/badge/TUI-Interactive%20Terminal%20Workstation-0284c7.svg?style=flat-square)](https://github.com/fakhruldeen/Tasleemat)
[![AI Agents](https://img.shields.io/badge/Agent%20Integrations-8%20IDEs%20%26%20Agents-8b5cf6.svg?style=flat-square)](https://github.com/fakhruldeen/Tasleemat)
[![Auditor](https://img.shields.io/badge/Auditor-Stage--Gate%20Verification-10b981.svg?style=flat-square)](https://github.com/fakhruldeen/Tasleemat)
[![Data Package](https://img.shields.io/badge/Data%20Package-OKF%20Frictionless-orange)](https://github.com/fakhruldeen/Tasleemat/blob/main/datapackage.json)
[![MCP Server](https://img.shields.io/badge/MCP%20Server-Standard%20Protocol-7c3aed)](https://github.com/fakhruldeen/Tasleemat/blob/main/docs/MCP_INTEGRATION.md)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23193523.svg)](https://doi.org/10.5281/zenodo.23193523)

**Tasleemat (تسليمات)** is an enterprise-grade, open-source Project Management Office (PMO) operating system and programmatic Python library designed for **Project Managers, PMO Directors, Business Leaders, Data Engineers, and Autonomous AI Agents**.

It provides **114 standardized, bilingual (English & Arabic) project management deliverables** (228 synchronized form bundles total) covering the complete project lifecycle—from strategic portfolio roadmaps and business cases to scope baselines, risk registers, stage-gate reviews, Earned Value Analysis (EVA), and project closeouts.

With **Version 2.6.0**, Tasleemat introduces an **Interactive Bilingual Terminal User Interface (TUI)** workstation, a **Project Governance Auditor & Verification Engine** with Stage-Gate readiness KPIs, **1-Click Native Integration for 8 Leading AI Coding Agents and IDEs**, and a universal **Multi-Provider LLM Engine**.

---

## 🌟 What's New in v2.6.0

- 🖥️ **Interactive Bilingual Terminal User Interface (TUI)** (`tasleemat tui` / `pip install "tasleemat[tui]"`):
  - Full-screen terminal dashboard powered by Textual with real-time bidirectional Arabic text shaping (`arabic-reshaper` & `python-bidi`).
  - **8 Specialized Workspaces:**
    1. **Scaffolding Wizard:** Guided project workspace creation tailored by Governance Tier (1, 2, 3), Methodology Pack (General, Agile, AI Governance, Predictive, Hybrid), and Language (EN/AR/Both).
    2. **Deliverables Browser:** Interactive explorer across all 114 standardized bilingual deliverables with tabbed views for Templates, Practitioner Guides, AI Prompts, Schemas, and Examples.
    3. **Live AI Generator:** Interactive deliverable generation with streaming completions, customizable prompts, and multi-provider selection.
    4. **Governance Auditor & Verification:** Automated project workspace audit with real-time ANSI progress bars, Governance Score %, Deliverable Completion %, and a 6-Stage Gate Readiness Matrix (Gate 0 to Gate 5).
    5. **MCP Diagnostics & Server:** Real-time Model Context Protocol telemetry, server status, tools registry, and connection verification.
    6. **Earned Value Analysis (EVA) Calculator:** Real-time computation of Cost Variance (CV), Schedule Variance (SV), Cost Performance Index (CPI), Schedule Performance Index (SPI), Estimate at Completion (EAC), Estimate to Complete (ETC), and To-Complete Performance Index (TCPI).
    7. **Bilingual PMO Lexicon Dictionary:** Searchable English/Arabic PMBOK & Saudi DGA terminology lookup with instant translations.
    8. **System & LLM Settings:** Provider, model, API endpoint, and key configuration with secure persistence.

- 🛡️ **Comprehensive Project Governance Auditor (`tasleemat audit [path]` / `tasleemat.audit_project`)**:
  - Available across **PIP SDK**, **CLI**, and **TUI**.
  - Analyzes scaffolded project workspaces against required methodology packs and governance tiers.
  - Generates compliance KPIs: Overall Completion %, Governance Score %, and Schema Compliance %.
  - Delivers a 6-Stage Gate Readiness Matrix (Gate 0 Strategic Alignment through Gate 5 Operational Handover & Closeout).
  - Itemized deliverable verification (`VALID`, `INCOMPLETE`, `MISSING`, `SCHEMA ERROR`) with diagnostic remediation advice and `--strict` / `--json` export flags.

- 🤖 **Universal Multi-Agent Ecosystem (8 Native IDE & Agent Integrations)**:
  - 1-click workspace scaffolding and configuration for:
    - **Cursor:** `.cursor/mcp.json` and `.cursorrules`
    - **Google Antigravity:** `.antigravityrules` and `skills/pmo-governance`
    - **Claude Desktop:** `claude_desktop_config.json` and `CLAUDE.md`
    - **VS Code:** `.vscode/mcp.json`
    - **OpenCode:** `.opencode/mcp.json` and `OPENCODE.md`
    - **Cline:** `.cline/mcp.json` and `.clinerules`
    - **Windsurf:** `.windsurf/mcp.json` and `.windsurfrules`
    - **OpenAI CLI Replicas:** `.openai/agent_runner.py`

- 🌐 **Flexible Multi-Provider LLM Engine**:
  - Zero-lockin AI client supporting **Google Gemini**, **OpenAI**, **Anthropic**, **OpenRouter**, **DeepSeek**, **Groq**, **Ollama**, and custom OpenAI-compatible endpoints with dynamic model selection and encrypted token storage (`~/.tasleemat/config.json`).

---

## 💻 Installation

Install the official package from PyPI:

```bash
# Standard SDK, CLI, and MCP Server:
pip install tasleemat

# With Interactive Terminal Workstation (TUI & BiDi Arabic rendering):
pip install "tasleemat[tui]"
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

### 6. Automated Project Governance & Stage-Gate Auditing

Perform structural compliance verification and stage-gate readiness evaluation on any project workspace:

```python
from tasleemat import audit_project

# Perform complete governance audit
report = audit_project("./My_Project", strict_schema=True)

# High-Level KPIs
print(f"Project:            {report.project_name} ({report.project_code})")
print(f"Governance Tier:    Tier {report.tier} ({report.pack.upper()})")
print(f"Overall Progress:   {report.overall_progress_pct:.1f}%")
print(f"Governance Score:   {report.governance_score_pct:.1f}%")
print(f"Schema Compliance:  {report.schema_compliance_pct:.1f}%")

# Stage-Gate Readiness Matrix (Gate 0 through Gate 5)
print("\n--- Stage-Gate Readiness Matrix ---")
for gate in report.gate_readiness:
    status_icon = "✅ [PASS]" if gate.status == "PASS" else "⚠️ [ACTION REQUIRED]"
    print(f"{gate.gate_id:7} | {gate.stage_name:40} | {gate.readiness_pct:5.1f}% | {status_icon}")

# Itemized Findings Breakdown
print(f"\nDeliverables: {report.total_valid} Valid, {report.total_incomplete} Incomplete, {report.total_missing} Missing")
for finding in report.findings:
    if finding.status != "valid":
        print(f"[{finding.status.upper()}] {finding.artifact_id} - {finding.name_en}: {finding.messages}")
```

---

## 🛠️ Global Command-Line Interface (CLI) & TUI Workstation

The `tasleemat` CLI provides workspace scaffolding, visual terminal workstations, governance auditing, form searches, and AI document auto-generation:

```bash
# 1. Complete CLI reference
tasleemat --help

# 2. Launch the Interactive Bilingual Terminal Workstation (TUI)
tasleemat tui

# 3. Launch TUI in Arabic directly with full BiDi shaping
tasleemat tui --lang ar

# 4. Perform complete Project Governance Audit with visual progress bars
tasleemat audit ./My_Project

# 5. Strict Governance Audit with machine-readable JSON report export
tasleemat audit ./My_Project --strict --json ./audit_report.json

# 6. Interactive project workspace scaffolder with agent configurations
tasleemat init

# 7. Fast-track automated scaffolding (Tier 2 Standard, Agile Pack, Arabic templates)
tasleemat init --tier 2 --pack agile --lang ar --name "منصة السحابة" --code "PRJ-2026-02" --out ./My_Project

# 8. Configure default LLM provider, model, or custom API endpoints
tasleemat config-llm --provider openrouter --model anthropic/claude-3.7-sonnet --key "sk-or-..."

# 9. Search deliverable forms by keyword
tasleemat search "Risk" --lang en
tasleemat search "ميثاق" --lang ar

# 10. List all 114 forms in catalog
tasleemat list --lang en

# 11. Auto-fill project deliverables using AI from meeting notes
tasleemat generate --form PMO-03.01 --notes ./meeting_notes.txt --out ./Project_Charter.md

# 12. Run automated test suite
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
