<!--
---
type: Overview
---
-->
<!-- mcp-name: io.github.fakhruldeen/tasleemat -->

<div align="center">

<p align="center">
  <img src="docs/img/logo.png" alt="Tasleemat PMO Toolkit Logo" width="340">
</p>

# 🚀 Tasleemat (تسليمات)
### *The Production-Grade, Bilingual PMO Artifact & AI Toolkit*
**114 Standardized Deliverables • 228 English & Arabic Bundles • 6 Stage-Gates • 3 Governance Tiers**  
*Fully Aligned with PMI PMBOK® (6th, 7th & 8th Edition Ready), ISO 21500 / 21502 & NIST AI RMF*

<p align="center">
  <a href="https://pypi.org/project/tasleemat/"><img src="https://img.shields.io/badge/📦_PyPI-v2.5.0-3775a9?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI Package"></a>
  <a href="docs/MCP_INTEGRATION.md"><img src="https://img.shields.io/badge/⚡_MCP_Server-Standard_Protocol-7c3aed?style=for-the-badge" alt="MCP Server"></a>
  <a href="https://fakhr.me/Tasleemat/"><img src="https://img.shields.io/badge/🌐_Interactive_Portal-Live_Demo-006a61?style=for-the-badge" alt="Live Portal"></a>
  <a href="https://fakhr.me/Tasleemat/catalog/en/index.html"><img src="https://img.shields.io/badge/📋_114_Deliverables-Catalog_Explorer-059669?style=for-the-badge" alt="Catalog"></a>
  <a href="README_AR.md"><img src="https://img.shields.io/badge/🇸🇦_النسخة_العربية-Bilingual_RTL-1d4ed8?style=for-the-badge" alt="Arabic Version"></a>
  <a href="https://github.com/fakhruldeen/Tasleemat/stargazers"><img src="https://img.shields.io/github/stars/fakhruldeen/Tasleemat?style=for-the-badge&color=eab308" alt="GitHub Stars"></a>
  <a href="https://doi.org/10.5281/zenodo.23193523"><img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23193523-blue?style=for-the-badge" alt="Zenodo DOI"></a>
</p>

<p align="center">
  <b><a href="https://fakhr.me/Tasleemat/">🌐 Live Web Portal</a></b> • 
  <b><a href="docs/MCP_INTEGRATION.md">⚡ MCP Server (Claude/Cursor)</a></b> • 
  <b><a href="https://fakhr.me/Tasleemat/catalog/en/index.html">📋 Browse 114 Templates</a></b> • 
  <b><a href="https://fakhr.me/Tasleemat/governance.html">🚪 6 Stage-Gates</a></b> • 
  <b><a href="https://fakhr.me/Tasleemat/LEXICON.html">📖 Bilingual Lexicon</a></b> • 
  <b><a href="https://fakhr.me/Tasleemat/developer.html">💻 Developer & CLI</a></b> • 
  <b><a href="README_AR.md">🇸🇦 النسخة العربية</a></b>
</p>

---

</div>

## 💡 Why Tasleemat?

Most Project Management Offices (PMOs) and Project Managers waste hundreds of hours reinventing the wheel with fragmented Word documents, mismatched Excel sheets, and inconsistent governance forms.

**Tasleemat solves this with a unified, auditable, and automated artifact library:**

| What PMs Usually Struggle With 😫 | How Tasleemat Delivers Excellence 🚀 |
| :--- | :--- |
| **Fragmented templates** scattered across folders and platforms | **114 production-ready deliverables** in structured Markdown, CSV data schemas, and JSON metadata |
| **English-only or poor machine translations** | **Handcrafted 1:1 bilingual parity** with Saudi DGA, PMI & ISO approved terminology |
| **One-size-fits-all overhead** that suffocates small projects | **4 Tailoring Tiers** (from a 5-artifact micro setup to a 45+ enterprise governance pack) |
| **Weak gate transition criteria** leading to scope creep & budget overrun | **6 Formal Stage-Gates** (Gate 0 to 5) with concrete RACI checklists and sign-off criteria |
| **Zero AI readiness** | Built-in **NIST AI RMF compliance**, AI model cards, and ready-to-run prompt templates |

---

## 🧭 Choose Your Persona & Fast-Track

<table>
<tr>
<td width="33%" valign="top">

### 👔 For Project Managers
**Start running projects immediately**
- 🚀 **[Project Charter (PMO-03.01)](forms/en/03_Initiating/01_Project_Charter/03_01_Project_Charter_Template.md)**: Formal authorization
- 📐 **[WBS & Scope Baseline](forms/en/04_Planning/02_Scope/07_WBS_Dictionary/04_02_07_WBS_Dictionary_Template.md)**: Clear work breakdown
- 📊 **[Status Report & EVA](forms/en/06_Monitoring_and_Controlling/01_Project_Status_Report/06_01_Project_Status_Report_Template.md)**: Executive dashboards
- 🚪 **[Stage-Gate Checklists](docs/en/04_stage_gates_and_governance.md)**: Phase transitions
- 📖 **[PM Quick Start Guide](docs/en/01_getting_started.md)**: 5-minute kickoff

</td>
<td width="33%" valign="top">

### 🏛️ For PMO Directors & Executives
**Institutionalize standards across the enterprise**
- ⚖️ **[Tailoring Matrix (Tiers 1–3)](docs/en/05_tailoring_profiles.md)**: Size governance to project risk
- 💎 **[Benefits Management Plan](forms/en/01_Business_and_Value_Delivery/02_Benefits_Management_Plan/01_02_Benefits_Management_Plan_Template.md)**: Strategic value tracking
- 🛡️ **[Stage-Gate Governance Policy](docs/en/04_stage_gates_and_governance.md)**: 3-decision gating control
- 📚 **[PMO Terminology Lexicon](docs/LEXICON.md)**: 164+ standardized bilingual definitions
- 🏆 **[PMO Maturity Assessment](forms/en/00_Program_and_Portfolio_Management/05_PMO_Maturity_Assessment/00_05_PMO_Maturity_Assessment_Template.md)**: Institutional benchmarking

</td>
<td width="33%" valign="top">

### 💻 For Developers & AI Engineers
**Automate documentation & workflows**
- 📦 **[CLI Scaffolder (`tasleemat init`)](TECHNICAL.md#1-tasleemat-cli-scaffolder--search-tool)**: One-command project scaffolding
- 🐍 **[Python SDK (`tasleemat.ai`)](TECHNICAL.md#2-programmatic-python-sdk-tasleematai)**: Programmatic artifact generator
- 🗄️ **[OKF Frictionless Data Schemas](TECHNICAL.md#3-data-architecture--synchronized-5-file-bundles)**: Validate tables with JSON schemas
- 🤖 **[NIST AI Model Cards](forms/en/02_Project_Approach_and_Tailoring/05_AI_Model_Card_and_Fact_Sheet/02_05_AI_Model_Card_and_Fact_Sheet_Template.md)**: AI ethics and governance
- ⚙️ **[TECHNICAL.md Manual](TECHNICAL.md)**: Architecture & pipeline docs

</td>
</tr>
</table>

---

## 🗺️ The Complete 8-Phase Lifecycle Map (114 Deliverables)

Every deliverable is organized chronologically into the standard **8 Lifecycle Phases**. Every folder delivers a **5-file synchronized bundle** (`Template.md`, `Guide.md`, `Example.md`, `schema.json`, `data.csv`).

```mermaid
flowchart LR
    P0["🏛️ 00. Portfolio<br/>(6 Forms)"] --> P1["💎 01. Business<br/>(4 Forms)"]
    P1 --> P2["⚖️ 02. Approach<br/>(6 Forms)"]
    P2 --> P3["🚀 03. Initiating<br/>(5 Forms)"]
    P3 --> P4["📐 04. Planning<br/>(52 Forms)"]
    P4 --> P5["⚙️ 05. Executing<br/>(12 Forms)"]
    P5 --> P6["📊 06. Controlling<br/>(12 Forms)"]
    P6 --> P7["🏁 07. Closing<br/>(5 Forms)"]
```

### 📑 Lifecycle Phase Directory

| Phase | Phase Name | Focus & Scope | Forms Count | Quick Links |
| :---: | :--- | :--- | :---: | :---: |
| **00** | **[Program & Portfolio Strategy](forms/en/00_Program_and_Portfolio_Management/)** | Strategic alignment, OKRs, portfolio roadmap, dependencies, PMO maturity | **6 Forms** | [English](forms/en/00_Program_and_Portfolio_Management/) • [العربية](forms/ar/00_إدارة_البرامج_والمحافظ/) |
| **01** | **[Business & Value Delivery](forms/en/01_Business_and_Value_Delivery/)** | Business case justification, feasibility studies, benefits realization | **4 Forms** | [English](forms/en/01_Business_and_Value_Delivery/) • [العربية](forms/ar/01_الأعمال_وتسليم_القيمة/) |
| **02** | **[Project Approach & Tailoring](forms/en/02_Project_Approach_and_Tailoring/)** | Governance tailoring strategy, agile/hybrid selection, AI ethics & model cards | **6 Forms** | [English](forms/en/02_Project_Approach_and_Tailoring/) • [العربية](forms/ar/02_منهجية_المشروع_وتخصيصه/) |
| **03** | **[Initiating](forms/en/03_Initiating/)** | Project charter, initial assumption log, stakeholder identification register | **5 Forms** | [English](forms/en/03_Initiating/) • [العربية](forms/ar/03_البدء/) |
| **04** | **[Integrated Planning](forms/en/04_Planning/)** | Scope/WBS, schedule, cost/budget, quality, risk, ESG, procurement, security | **52 Forms** | [English](forms/en/04_Planning/) • [العربية](forms/ar/04_التخطيط/) |
| **05** | **[Executing & Delivering](forms/en/05_Executing/)** | Issue logs, change requests, team charter, sprint backlog, retrospectives | **12 Forms** | [English](forms/en/05_Executing/) • [العربية](forms/ar/05_التنفيذ/) |
| **06** | **[Monitoring & Controlling](forms/en/06_Monitoring_and_Controlling/)** | Status reports, Earned Value (EVA), variance tracking, quality acceptance | **12 Forms** | [English](forms/en/06_Monitoring_and_Controlling/) • [العربية](forms/ar/06_المراقبة_والتحكم/) |
| **07** | **[Closing & Transition](forms/en/07_Closing/)** | Operational handover, lessons learned register, contract closeout sign-off | **5 Forms** | [English](forms/en/07_Closing/) • [العربية](forms/ar/07_الإغلاق/) |

---

## 🚪 The 6 Governance Stage-Gates

Ensure auditable decision-making before allocating capital to successive phases:

```mermaid
flowchart TD
    G0["Gate 00: Concept & Strategic Alignment"] --> G1["Gate 01: Project Charter & Authorization"]
    G1 --> G2["Gate 02: Integrated Baselines Sign-off"]
    G2 --> G3["Gate 03: Delivery Review & Quality Acceptance"]
    G3 --> G4["Gate 04: Operational Handover & Readiness"]
    G4 --> G5["Gate 05: Final Closeout & Benefits Verification"]
```

Every gate produces one of **3 Formal Outcomes**:
1. 🟢 **Proceed (Go)**: 100% exit criteria met, budget unlocked for next phase.
2. 🟡 **Conditional Approval**: Proceed with mandatory 14-day Corrective Action Plan (CAPA).
3. 🔴 **Hold / Terminate**: Significant variance or strategic misalignment; project paused or shelved.

👉 *Explore the interactive gate matrix and checklists in the **[Stage-Gate Governance Portal](https://fakhr.me/Tasleemat/governance.html)**.*

---

## 🎯 4 Tailoring Sizing Profiles

Avoid governance paralysis by matching the paperwork to the actual risk and scale of your initiative:

| Sizing Tier | Profile Description | Typical Scale | Artifact Count | Core Deliverables Included |
| :--- | :--- | :--- | :---: | :--- |
| **Tier 1: Enterprise / Mega** | Strategic transformations, multi-vendor | > \$10M • Critical | **45+ Artifacts** | All 6 Stage-Gates, Audit Dossiers, Procurement Pack, ESG & Security Baselines |
| **Tier 2: Standard** | Departmental initiatives, medium risk | \$1M–\$10M • 3–9 months | **18–25 Artifacts** | Full Baselines (Scope, Schedule, Budget), Risk Register, RACI, Change Management |
| **Tier 3: Lean / Fast-Track** | Fast-paced, low-complexity projects | < \$1M • < 3 months | **7–9 Artifacts** | Project Charter, Schedule, Action Log, Monthly Status, Closeout Handover |

> 💡 **Methodology Packs**: Methodology packs (*General*, *Agile*, *AI Governance*, *Predictive*, *Hybrid*) apply orthogonally across all tiers.

---

## ⚡ Quick Start: 4 Ways to Use Tasleemat

### Option 1: Explore on the Web *(Fastest)*
Visit the interactive portal to search, preview, and copy templates with one click:
- 🌐 **[https://fakhr.me/Tasleemat/](https://fakhr.me/Tasleemat/)**
- 📋 **[114 Templates Explorer](https://fakhr.me/Tasleemat/catalog/en/index.html)**

### Option 2: Programmatic Python Library (`import tasleemat`)
Install directly from PyPI to access templates, data schemas, validation, and rendering in Python:
```bash
pip install tasleemat
```
```python
import tasleemat

# 1. Discover registered deliverables (114 artifacts)
charter = tasleemat.get_artifact_definition("PMO-03.01")

# 2. Retrieve bilingual templates or guides directly
en_template = tasleemat.get_artifact_asset("PMO-03.01", role="template", lang="en")
ar_template = tasleemat.get_artifact_asset("PMO-03.01", role="template", lang="ar")

# 3. Validate structured data against JSON schemas
report = tasleemat.validate_artifact_data("PMO-03.01", {"project_name": "Cloud Platform"}, mode="draft")
print(f"Valid: {report.valid}, Warnings: {len(report.warnings)}")

# 4. Render offline to publication-ready styled HTML
tasleemat.render_artifact("PMO-03.01", lang="en", out_path="./charter.html")
```

### Option 3: Automate via CLI Scaffolder
Scaffold an entire project governance directory with customized templates:
```bash
# Interactive wizard or fast-track command
tasleemat init --tier 2 --pack agile --lang ar --out ./My_Project
```

### Option 4: Clone & Use Native Markdown Directly in GitHub
All deliverables are plain, clean Markdown files. You can clone the repo and use them directly in VS Code, Obsidian, Notion, or Confluence:
```bash
git clone https://github.com/fakhruldeen/Tasleemat.git
cd Tasleemat
# Browse English templates: forms/en/
# Browse Arabic templates: forms/ar/
```

---

## 🤖 Using Tasleemat & OKF with LLMs (Claude, ChatGPT, OpenCode & AI Coding Agents)

Tasleemat is natively engineered for **Generative AI workflows**, **Large Language Models (LLMs)**, and **AI coding assistants** (Claude, ChatGPT, OpenCode, Cursor, GitHub Copilot).

### 1. In Standard Chat LLMs (Claude & ChatGPT)

Every form folder in `forms/` contains a dedicated, pre-engineered LLM prompt file (e.g. `03_01_Project_Charter.md`) and a clean template (`*_Template.md`):

#### Workflow A: Direct Prompt Injection
1. **Copy the Prompt**: Open the deliverable's prompt file (e.g. `forms/en/03_Initiating/01_Project_Charter/03_01_Project_Charter.md` or Arabic equivalent).
2. **Paste into Claude or ChatGPT**: Paste the prompt into your chat window as the System Instructions or prompt prefix.
3. **Attach Your Notes**: Append your raw project kickoff notes, meeting transcripts, or charter inputs:
   ```text
   [PASTE TASLEEMAT PROMPT HERE]

   Project Kickoff Notes:
   - Project: Riyadh Smart Logistics Hub
   - Sponsor: Logistics Development Authority
   - Budget: 12M SAR
   - Timeline: 14 Months
   - Key Scope: Automate sorting center, deploy IoT fleet tracking
   ```
4. **Result**: The LLM outputs a complete, audit-compliant PMO deliverable following official PMI PMBOK® formatting and document control sign-off tables.

#### Workflow B: Custom GPTs & Claude Projects
- Create a **Claude Project** or **Custom GPT** titled *"PMO Enterprise Architect"*.
- Upload the `forms/` templates and `docs/LEXICON.json` as project knowledge files.
- Set the project instructions to: *"Always use Tasleemat artifact structures, Document Control headers, and bilingual terminology for all requested PMO deliverables."*

---

### 2. In Coding Agents & IDEs (Cursor, OpenCode, Windsurf, Cline)

Tasleemat runs natively as an MCP server (`tasleemat-mcp`) across all agentic IDEs:

#### A. Cursor IDE
Add to `.cursor/mcp.json` or via **Cursor Settings** $\rightarrow$ **Features** $\rightarrow$ **MCP**:
```json
{
  "mcpServers": {
    "tasleemat": {
      "command": "tasleemat-mcp"
    }
  }
}
```

#### B. OpenCode Setup
In your OpenCode MCP settings or workspace configuration:
```json
{
  "mcpServers": {
    "tasleemat": {
      "command": "tasleemat-mcp"
    }
  }
}
```

#### C. Windsurf (Codeium) Setup
Configure in `~/.codeium/windsurf/mcp_config.json`:
```json
{
  "mcpServers": {
    "tasleemat": {
      "command": "tasleemat-mcp"
    }
  }
}
```

#### D. Cline / Roo Code (VS Code Extension)
In `cline_mcp_settings.json`:
```json
{
  "mcpServers": {
    "tasleemat": {
      "command": "tasleemat-mcp"
    }
  }
}
```

- **Reference via `@` Context in Chat**:
  - `@03_01_Project_Charter_Template.md Fill this project charter for a modern mobile banking app with biometric authentication.`
- **Repository Rules (`.cursorrules` / `.windsurfrules`)**:
  ```markdown
  When generating project documentation, always adhere to the schema and templates defined in forms/en/ and forms/ar/. Enforce Document Control blocks and never remove placeholder audit hashes.
  ```

---

### 3. In Multi-Agent Frameworks (CrewAI, LangChain, LlamaIndex)

Because `tasleemat` is a standard package on PyPI (`pip install tasleemat`), autonomous agent frameworks can import it directly:

#### CrewAI Custom Tool:
```python
from crewai.tools import tool
import tasleemat

@tool("PMO Deliverable Retriever")
def get_pmo_deliverable(artifact_id: str, role: str = "template", lang: str = "en") -> str:
    """Fetches standardized PMO deliverable templates and guides (e.g. PMO-03.01)."""
    return tasleemat.get_artifact_asset(artifact_id, role, lang)
```

#### LangChain Custom Tool:
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

#### LlamaIndex Function Tool:
```python
from llama_index.core.tools import FunctionTool
import tasleemat

def fetch_pmo_template(artifact_id: str, lang: str = "en") -> str:
    """Retrieve an authoritative bilingual PMO template by ID."""
    return tasleemat.get_artifact_asset(artifact_id, role="template", lang=lang)

pmo_tool = FunctionTool.from_defaults(
    fn=fetch_pmo_template,
    name="tasleemat_pmo_template",
    description="Provides access to 114 standardized bilingual PMO deliverable templates."
)
```

---

### 4. Using the Open Knowledge Foundation (OKF) Data Package with LLMs

Tasleemat includes a root [`datapackage.json`](datapackage.json) following the **OKF Frictionless Data Package** standard, which indexes all 228 form schema resources.

#### A. Structured Function Calling & Tool Use
LLMs often hallucinate fields when asked to produce JSON. With Tasleemat's OKF schemas, you can supply formal parameter definitions to LLM function calling (OpenAI Tools / Claude Tool Use):

```python
import json
import tasleemat

# Load the schema directly from the companion contracts
defn = tasleemat.get_artifact_asset("PMO-03.01", role="schema", lang="en")

# Pass into Claude / OpenAI tool definitions:
tools = [
    {
        "name": "create_project_charter",
        "description": "Generate a PMI-compliant Project Charter",
        "parameters": defn  # Exact JSON schema constraints
    }
]
```

#### B. In-Context Validation & Self-Correction Loops
When using LLMs to draft project records, use `validate_artifact_data` in an automated feedback loop:

```python
import tasleemat

# 1. Ask LLM to generate structured artifact JSON
llm_json_output = {"artifact_id": "PMO-03.01", "project_name": "Incomplete Project"}

# 2. Validate against Tasleemat structural contract
report = tasleemat.validate_artifact_data("PMO-03.01", llm_json_output, mode="strict")

# 3. If invalid, feed exact error pointers back to the LLM to self-correct:
if not report.valid:
    feedback_prompt = f"Your output had validation errors: {[(e.field_path, e.message) for e in report.errors]}. Please correct and return valid JSON."
    # Re-prompt LLM with feedback_prompt
```

---

## 📜 International Standards Alignment

Tasleemat is engineered to comply with leading global project governance and technical benchmarks:

- **PMI PMBOK® Guide**: 6th Edition (Process Groups), 7th Edition (Performance Domains), and 8th Edition Ready.
- **ISO 21500:2021 & ISO 21502:2020**: Guidance on project, programme, and portfolio management.
- **Saudi Digital Government Authority (DGA)**: Enterprise architecture and government PMO requirements.
- **NIST AI 100-1 (AI RMF)**: AI model documentation, bias evaluations, and ethical deployment controls.
- **Open Knowledge Foundation (OKF)**: Frictionless Data specifications (JSON schemas + CSV definitions).
- **ESG / UN Sustainable Development Goals**: Sustainability integration in project charter and benefits.

---

## 👨‍💼 Creator & Lead Maintainer

<table border="0">
  <tr>
    <td width="110" align="center" valign="middle">
      <a href="https://fakhruldeen.github.io">
        <img src="https://avatars.githubusercontent.com/u/1162549?v=4" width="100" height="100" style="border-radius:50%;" alt="Fakhruldeen">
      </a>
    </td>
    <td valign="middle">
      <b>Mohamed (Fouad) Fakhruldeen</b><br/>
      <i>Enterprise Project Management & Digital Transformation Leader</i><br/>
      <a href="https://linkedin.com/in/fakhruldeen"><img src="https://img.shields.io/badge/LinkedIn-0077b5?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
      <a href="https://fakhruldeen.github.io"><img src="https://img.shields.io/badge/Personal_Website-10b981?style=flat-square&logo=google-chrome&logoColor=white" alt="Website"></a>
      <a href="https://github.com/fakhruldeen"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"></a>
    </td>
  </tr>
</table>

---

## 📚 Citation & Academic Reference

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23193523.svg)](https://doi.org/10.5281/zenodo.23193523)

If you use Tasleemat in your PMO operations, institutional research, or consulting projects, please cite:
```bibtex
@software{fakhruldeen_tasleemat_2026,
  author       = {Fakhruldeen, Mohamed (Fouad)},
  title        = {Tasleemat: The Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Toolkit},
  month        = oct,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v2.3.0},
  doi          = {10.5281/zenodo.23193523},
  url          = {https://doi.org/10.5281/zenodo.23193523}
}
```

---

## ⚖️ License

Distributed under the **[MIT License](LICENSE)**. Free to use, adapt, and integrate into internal organizational PMOs, public sector transformations, and commercial software.

<div align="center">
  <sub>Built with passion for project excellence across the Arab world and globally. © 2026 Tasleemat Contributors.</sub>
</div>
