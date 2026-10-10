<!--
---
type: Guide
---
-->

# Developer Manual, CLI Scaffolder & Python SDK (`tasleemat.ai`)

> **Bilingual PMO Governance, Automated Scaffolding & Standardized Terminology**  
> *دليل المطورين، أدوات سطر الأوامر (CLI)، وحزمة بايثون، والمعجم الموحد*

[![PyPI Version](https://img.shields.io/pypi/v/tasleemat.svg?color=blue)](https://pypi.org/project/tasleemat/)
[![Python Versions](https://img.shields.io/pypi/pyversions/tasleemat.svg)](https://pypi.org/project/tasleemat/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23193523-blue)](https://doi.org/10.5281/zenodo.23193523)

---

## ⚡ Quick Start & Installation

Install the official Tasleemat distribution package directly from PyPI:

```bash
# Install the core CLI and Python SDK
pip install --upgrade tasleemat

# Verify CLI version and environment health
tasleemat --version
tasleemat doctor
```

### Standards & Compliance Grounding

| Dimension | Specification | Notes |
|:---|:---|:---|
| **Global Standard** | PMI PMBOK® 6th, 7th & 8th Edition | Complete alignment with Performance Domains |
| **Data Architecture** | OKF Frictionless Datapackage (v0.2) | Machine-readable schema validation |
| **International Quality**| ISO 21500 / ISO 21502:2021 | Governance and guidance for project management |
| **AI Governance** | NIST AI RMF 1.0 & ISO 42001 | Grounded prompts and audit checklists |
| **Language Parity** | Dual RTL/LTR (Arabic & English) | 1:1 bilingual field parity |

---

## 🛠️ CLI Automation & Project Scaffolding

Tasleemat includes an interactive scaffolding engine designed for command-line automation and CI/CD pipelines.

### Common CLI Commands

```bash
# 1. Initialize a Standard Tier 2 Project in Arabic
tasleemat init --tier 2 --pack standard --lang ar --name "منصة_التحول_الرقمي"

# 2. Initialize a Fast Agile / Scrum Project with Dual Language
tasleemat init --tier 4 --pack agile --lang both --name "digital_agile_hub"

# 3. Scaffold an Individual Deliverable Template
tasleemat scaffold FORM-03-01 --lang dual --out ./deliverables/

# 4. Validate All Deliverables against Frictionless Data Schemas
tasleemat validate ./deliverables/ --strict
```

### Supported Governance Sizing Tiers

1. **Tier 1 (Micro / Small - 5 Artifacts):** Lean execution for experimental or internal departmental initiatives.
2. **Tier 2 (Standard Core - 18 Artifacts):** Standard enterprise project delivery with foundational governance.
3. **Tier 3 (Enterprise Transformation - 45+ Artifacts):** High-budget, mission-critical transformations with strict oversight.
4. **Tier 4 (Agile / AI Iterative - 25 Artifacts):** Sprint-based delivery with continuous AI validation loops.

---

## 🤖 Programmatic Python SDK (`tasleemat.ai`)

Automate document drafting and LLM verification using the Python SDK:

```python
from tasleemat.ai import AIClient

# 1. Initialize client (supports Gemini, OpenAI, Claude, or local mock engines)
client = AIClient(provider="gemini", model="gemini-2.5-flash")

# 2. Automated artifact population using PMI PMBOK principle grounding
charter_md = client.generate_deliverable(
    code="FORM-03-01",
    lang="ar",
    project_context={
        "name": "منصة الحوكمة الرقمية",
        "sponsor": "معالي رئيس الهيئة",
        "budget": "4,500,000 SAR",
        "strategic_goal": "أتمتة مخرجات PMO وتحقيق مستهدفات التحول الرقمي 2030"
    }
)

print(charter_md)
```

---

## 📖 Master Bilingual PMO Lexicon

Core terminology aligned with the official PMI PMBOK® Lexicon and MENA government project standards:

| English Term | المصطلح العربي المعتمد | Definition & Context (التعريف والسياق) | Lifecycle Domain | Standard Reference |
|:---|:---|:---|:---|:---|
| **Baseline** | **الخط الأساسي** | The approved version of a work product, schedule, or cost envelope that can only be changed through formal change control. | Planning | PMBOK® 6/7/8 |
| **Work Breakdown Structure (WBS)** | **هيكل تجزئة العمل** | A hierarchical decomposition of the total scope of work to be carried out by the project team. | Scope (04.02) | ISO 21502 / PMBOK® |
| **Earned Value Analysis (EVA)** | **تحليل القيمة المكتسبة** | Methodology that combines scope, schedule, and resource measurements to assess project performance and progress. | Monitoring (06) | ANSI/EIA-748 |
| **Stage-Gate Review** | **مراجعة بوابة المرحلة** | A formal checkpoint at the end of a phase where a decision is made to continue, conditionally proceed, or terminate. | Governance (00-07) | PMI Standard |
| **Deliverable** | **المُسلَّم / التسليمة القياسية** | Any unique and verifiable product, result, or capability to perform a service that is required to be produced to complete a phase. | All Lifecycle | OKF / PMBOK® |
| **Stakeholder Engagement** | **إشراك أصحاب المصلحة** | Strategies and actions to involve individuals and groups in project decisions and execution based on interests and influence. | Initiating (03) | PMBOK® Principle 3 |
| **Risk Appetite** | **القابلية للمخاطر** | The degree of uncertainty an organization or individual is willing to accept in anticipation of a reward. | Risk (04.08) | ISO 31000 |
| **Contingency Reserve** | **احتياطي الطوارئ** | Time or budget allocated within the cost baseline for known-unknown risks managed by the Project Manager. | Cost (04.04) | PMBOK® 6th/7th |

*For the complete bilingual lexicon of standardized project terminology, see [docs/LEXICON.md](LEXICON.md).*

---

## 📚 Academic Citation & Zenodo DOI

If you utilize the Tasleemat framework or dataset in enterprise research, audit manuals, or academia, please cite:

```bibtex
@software{fakhruldeen_tasleemat_2026,
  author       = {Fakhruldeen, Mohamed (Fouad)},
  title        = {Tasleemat: The Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Governance Framework},
  year         = {2026},
  version      = {v2.0.2},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23193523},
  url          = {https://doi.org/10.5281/zenodo.23193523}
}
```

---

## 🔗 Related Resources

- [Stage-Gate Governance & Tailoring](governance.md)
- [Master Bilingual Lexicon](LEXICON.md)
- [Getting Started Guide (English)](en/01_getting_started.md)
- [دليل البدء السريع (العربية)](ar/01_getting_started.md)
- [GitHub Repository](https://github.com/fakhruldeen/Tasleemat)
