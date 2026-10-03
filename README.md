<div align="center">

# 🚀 Tasleemat PMO Toolkit | تسليمات
### *The Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Automation Library*
#### *Fully Aligned with PMI PMBOK® Guide 6th, 7th & 8th Edition Ready Standards*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![PMI Standard](https://img.shields.io/badge/Standard-PMI%20PMBOK®%206th%2C%207th%20%26%208th%20Edition-0052cc?style=for-the-badge)](LEXICON.md)
[![Templates](https://img.shields.io/badge/Templates-102%20Bilingual%20Pairs%20(204%20Total)-success?style=for-the-badge)](forms/)
[![Language](https://img.shields.io/badge/Language-English%20%7C%20العربية-darkgreen?style=for-the-badge)](README_AR.md)
[![Format](https://img.shields.io/badge/Formats-Markdown%20%7C%20JSON%20%7C%20CSV-orange?style=for-the-badge)](USAGE_GUIDE.md)

<br/>

**[🇸🇦 اقرأ الدليل الكامل باللغة العربية (Read in Arabic)](README_AR.md)** • **[📖 Master Lexicon](LEXICON.md)** • **[🔗 Dependencies DAG](DOCUMENT_DEPENDENCIES.md)** • **[👥 Governance RACI](RACI_AUTHORITY_MATRIX.md)** • **[🛠️ Usage Guide](USAGE_GUIDE.md)** • **[📂 English Forms](forms/en/)** • **[📂 Arabic Forms](forms/ar/)**

---

</div>

## 🌟 Executive Summary

**Tasleemat (تسليمات)** is a production-grade, open-source Project Management Office (PMO) toolkit designed for project managers, PMO directors, enterprise architects, and AI practitioners. It provides **102 standardized, bilingual (English & Arabic) project management artifacts** (204 synchronized form bundles total) covering the complete chronological project lifecycle—from portfolio strategy, OKR alignment, and business value delivery to predictive baselines, Agile execution, Lean flow metrics, Sustainability/ESG governance, and AI engineering.

Every single artifact is designed as a **5-file synchronized bundle**, bridging the gap between human practitioner workflows, executive print-ready PDF reporting, and autonomous AI document generation.

---

## 💎 Core Highlights & PMBOK® 8th Edition Readiness

- **📚 102 Full-Lifecycle Artifacts (204 Form Bundles):** Complete coverage across 8 lifecycle phases and 12 planning domains.
- **🌱 Sustainability & ESG Project Management (PMBOK 8th Ed):** Dedicated ESG baselines, Scope 1/2/3 carbon footprint reduction tracking, circular resource utilization, and ethical procurement (`PMO-04.12.01`).
- **⚡ Modern Flow Metrics & Value Streams (PMBOK 8th Ed):** Real-time Lean/Agile telemetry tracking Lead Time & Cycle Time percentiles, WIP limits, Flow Efficiency, and delivery throughput (`PMO-06.12`).
- **🧠 Human-Centric Leadership & Psychological Safety (PMBOK 8th Ed):** Quantitative measurement of vulnerability, constructive dissent, blameless culture, cognitive workload balance, and focus time (`PMO-04.06.06`).
- **🎯 Dynamic OKR & Strategic Portfolio Alignment (PMBOK 8th Ed):** Top-down Objective and Key Result (OKR) mapping to project milestones with quarterly confidence tracking and strategic pivoting (`PMO-00.06`).
- **🌐 100% Bilingual Parity (EN & AR):** Strict 1-to-1 structural parity between English source files and native Arabic (RTL) files aligned with the **PMI Lexicon of Project Management Terms**.
- **🤖 AI-Native & GenAI Architecture:** Every form includes dedicated machine-readable JSON schemas and prompt instructions ready for instant automated drafting via Claude, ChatGPT, Gemini, or local LLMs.
- **🖨️ Executive Print & Export Ready:** Clean GitHub-flavored Markdown and HTML tables formatted for seamless PDF conversion with governance sign-off blocks.
- **📖 Official Terminology Lexicon:** Standardized project management terms mapped and defined in [`LEXICON.md`](LEXICON.md) and [`LEXICON.json`](LEXICON.json).

---

## 📂 Repository Architecture

```text
Tasleemat/
├── forms/
│   ├── en/                                         # 🇬🇧 English Artifacts (Root)
│   │   ├── 00_Program_and_Portfolio_Management/    # 6 Roadmaps, OKRs, Maturity & Capacity
│   │   ├── 01_Business_and_Value_Delivery/         # 4 Business Cases, Gap Analysis & Value
│   │   ├── 02_Project_Approach_and_Tailoring/      # 6 Tailoring & AI Governance Plans
│   │   ├── 03_Initiating/                          # 5 Charters, Assumption Logs & Registers
│   │   ├── 04_Planning/                            # 52 Detailed Baselines across 12 Domains
│   │   ├── 05_Executing/                           # 12 Operational Logs & Meeting Records
│   │   ├── 06_Monitoring_and_Controlling/          # 12 Variance, EVA, Flow Metrics & Health
│   │   ├── 07_Closing/                             # 5 Closeout Reports, Handover & PIR
│   │   └── parameters.md                           # Global project variables for AI prompts
│   └── ar/                                         # 🇸🇦 Arabic Localized Artifacts (RTL)
│       ├── 00_إدارة_البرامج_والمحافظ/
│       ├── 01_الأعمال_وتسليم_القيمة/
│       ├── 02_منهجية_المشروع_وتخصيصه/
│       ├── 03_البدء/
│       ├── 04_التخطيط/
│       ├── 05_التنفيذ/
│       ├── 06_المراقبة_والتحكم/
│       ├── 07_الإغلاق/
│       └── parameters.md
├── LEXICON.md                                      # 📖 Master Bilingual PMI Lexicon & Catalog
├── LEXICON.json                                    # 🤖 Machine-readable Schema & Form Index
├── USAGE_GUIDE.md                                  # 📘 Comprehensive English Practitioner Guide
├── USAGE_GUIDE_AR.md                               # 📙 Comprehensive Arabic Practitioner Guide
├── README.md                                       # 🇬🇧 Main Repository Documentation
└── README_AR.md                                    # 🇸🇦 Arabic Repository Documentation
```

---

## 📦 The 5-File Artifact Bundle

Inside every form directory (e.g., [`forms/en/03_Initiating/01_Project_Charter/`](forms/en/03_Initiating/01_Project_Charter/)), you will find exactly 5 synchronized files:

| File Type | Pattern | Purpose & Practitioner Value |
| :--- | :--- | :--- |
| **Printable Template** | `*_Template.md` / `*_قالب.md` | Clean, printable document structure with document metadata headers, detailed sections, and governance approval tables. |
| **Practitioner Guide** | `*_Guide.md` / `*_دليل.md` | In-depth operational guide detailing purpose, writing principles, column guidelines, and upstream/downstream dependencies. |
| **LLM Generation Prompt** | `*.md` | System prompt engineered to instruct AI models on exact field constraints, business context, and output format. |
| **JSON Data Schema** | `*.json` | Machine-readable schema mapping section keys, field labels, practitioner guidance, and target values for API pipelines. |
| **Tabular Data Dictionary** | `*.csv` | 4-column structured dictionary (`Section,Field,Guidance,LLM_Generated_Value`) for Excel, PowerBI, and data pipelines. |

---

## 🗺️ Project Lifecycle Overview (102 Forms)

```mermaid
flowchart LR
    P0["00. Portfolio & Strategy<br/>(6 Forms)"] --> P1["01. Value Delivery<br/>(4 Forms)"]
    P1 --> P2["02. Approach & Tailoring<br/>(6 Forms)"]
    P2 --> P3["03. Initiating<br/>(5 Forms)"]
    P3 --> P4["04. Planning<br/>(52 Forms)"]
    P4 --> P5["05. Executing<br/>(12 Forms)"]
    P5 --> P6["06. Monitoring & Controlling<br/>(12 Forms)"]
    P6 --> P7["07. Closing<br/>(5 Forms)"]
```

### 📑 Lifecycle Phase Summary

1. **[00. Program and Portfolio Management](forms/en/00_Program_and_Portfolio_Management/)** (`PMO-00.01` – `PMO-00.06`): Portfolio roadmaps, program charters, interdependency tracking, capacity planning, PMO maturity assessment, and OKR alignment.
2. **[01. Business and Value Delivery](forms/en/01_Business_and_Value_Delivery/)** (`PMO-01.01` – `PMO-01.04`): Business cases, benefits management plans, value realization registers, and gap analysis reports.
3. **[02. Project Approach and Tailoring](forms/en/02_Project_Approach_and_Tailoring/)** (`PMO-02.01` – `PMO-02.06`): Methodology tailoring, AI governance, AI readiness assessments, model cards, and ethics baselines.
4. **[03. Initiating](forms/en/03_Initiating/)** (`PMO-03.01` – `PMO-03.05`): Project charter, product vision, assumption logs, stakeholder registers, and stakeholder analysis.
5. **[04. Planning](forms/en/04_Planning/)** (`PMO-04.01.01` – `PMO-04.12.01`): 52 detailed planning baselines across 12 domains (Integration, Scope/WBS, Schedule, Cost, Quality, Resources & Psychological Safety, Communications, Risk, Procurement, Stakeholders, OCM, and Sustainability/ESG).
6. **[05. Executing](forms/en/05_Executing/)** (`PMO-05.01` – `PMO-05.12`): Issue logs, change requests, team performance evaluations, retrospectives, and prompt libraries.
7. **[06. Monitoring and Controlling](forms/en/06_Monitoring_and_Controlling/)** (`PMO-06.01` – `PMO-06.12`): Status reports, variance analysis, Earned Value Analysis (EVA), UAT sign-offs, project health check matrices, and Lean flow metrics dashboards.
8. **[07. Closing](forms/en/07_Closing/)** (`PMO-07.01` – `PMO-07.05`): Lessons learned summaries, contract closeouts, project closeouts, operational handover checklists, and post-implementation reviews (PIR).

*For the complete index of all 102 forms with English/Arabic names and direct links, see **[`LEXICON.md`](LEXICON.md)**.*

---

## ⚡ Quick Start: 3 Ways to Use Tasleemat

### 1. Manual Project Management Workflow
1. Navigate to the desired phase folder (e.g., [`forms/en/03_Initiating/01_Project_Charter/`](forms/en/03_Initiating/01_Project_Charter/)).
2. Open `03_01_Project_Charter_Guide.md` to review best practices and required inputs.
3. Copy `03_01_Project_Charter_Template.md` into your editor (VS Code, Obsidian, Notion, or Confluence) or export directly to PDF.

### 2. AI-Powered Generation Workflow (ChatGPT, Claude, Gemini)
Generate complete, compliant PMO documents in seconds:
1. Open [`forms/en/parameters.md`](forms/en/parameters.md) (or [`forms/ar/parameters.md`](forms/ar/parameters.md)) and enter your project parameters (Title, Sponsor, Budget, Scope boundaries).
2. Open the prompt file `*.md` of the desired artifact (e.g., `04_08_02_Risk_Register.md`).
3. Feed both files along with your rough meeting notes into your LLM:
   ```text
   You are an expert PMO Lead. Fill out this artifact based on the project parameters 
   and the following rough notes: [Insert notes here]. 
   Adhere strictly to the field guidance and output the result in Markdown matching the template structure.
   ```
4. Receive a perfectly structured, publication-ready project document!

### 3. Programmatic & Data Engineering Workflow
- Ingest [`LEXICON.json`](LEXICON.json) or individual `*.json` / `*.csv` files directly into Python (`pandas`), PowerBI, or internal web dashboards to track deliverable completion across enterprise portfolios.

---

## 📜 Standards & Compliance Alignment

Tasleemat is strictly aligned with international project management benchmarks:
- **PMI PMBOK® Guide (6th, 7th & 8th Edition Ready)**
- **PMI Process Groups: A Practice Guide**
- **PMI Lexicon of Project Management Terms**
- **ISO 21500:2021 & ISO 21502:2020** (Project, Programme and Portfolio Management)
- **Agile & Lean Practice Guides** (Scrum, Kanban, Value Stream Management, Flow Metrics)
- **NIST AI Risk Management Framework & EU AI Act** (AI Governance Artifacts)
- **UN Sustainable Development Goals (SDGs) & ESG Reporting Frameworks**

---

## 📄 License & Attribution

This project is open-source under the **[MIT License](LICENSE)**. You are free to use, adapt, and integrate these templates in commercial and non-commercial enterprise projects.

---

<div align="center">
  <sub>Built with precision for project leaders worldwide. Maintained by <a href="https://github.com/fakhruldeen">Fakhruldeen</a>.</sub>
</div>
