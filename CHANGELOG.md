---
type: Document
---

# 📜 Changelog

All notable changes to the **Tasleemat (تسليمات)** PMO Operating System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2026-10-03 — Enterprise Bilingual Release

### 🚀 Major Highlights
- **102 Full-Lifecycle Bilingual Artifacts (204 Form Bundles):** Complete 1:1 structural symmetry across English and Arabic covering 8 lifecycle phases and 12 planning domains.
- **204 Authentic Reference Implementations:** Fully populated real-world benchmark examples in `examples/en/` and `examples/ar/` with 100% fictional enterprise data and zero fallback boilerplate.
- **Open Knowledge Foundation (OKF) Compliance:** Conforms to Frictionless Data Package specifications with a root `datapackage.json` indexing all 204 tabular schemas.
- **12 Comprehensive Bilingual Guides:** Reorganized documentation in `docs/` covering Onboarding, Usage, PMO Policies, Stage-Gates, Tailoring, RACI Matrix, Document Dependencies DAG, AI Governance, Agile/Hybrid, FAQ, Developer Tools, and OKF.
- **Official CLI Scaffolder (`tools/tasleemat_cli.py`):** Interactive and fast-track command-line wizard for generating tailored project workspaces by tier and pack with automatic metadata pre-population.
- **Batch Exporter (`tools/export_deliverables.py`):** Converts Markdown deliverables into print-ready styled HTML documents with full Arabic RTL typography support.
- **Material for MkDocs Portal (`mkdocs.yml`):** Mobile-friendly, searchable web portal with dark/light themes and Mermaid diagram support.
- **Automated CI/CD Quality Pipeline (`.github/workflows/`):** Continuous integration workflows for parity, schema audit, rendering checks, OKF validation, and GitHub Pages deployment.

### 🌟 PMBOK® 8th Edition Ready Features
- **AI & GenAI Governance:** Dedicated AI Readiness, Use Case Canvas, Model Cards, Prompt Library, and Ethics Baselines.
- **Flow Metrics & Value Streams:** Real-time Lead/Cycle Time percentiles, WIP limits, Flow Efficiency, and throughput tracking (`PMO-06.12`).
- **Sustainability & ESG:** Scope 1/2/3 carbon tracking, circular utilization, and ethical procurement (`PMO-04.12.01`).
- **Psychological Safety & Wellbeing:** Quantitative team health, constructive dissent, and cognitive balance index (`PMO-04.06.06`).
- **Dynamic OKR Alignment:** Objective and Key Result portfolio mapping with quarterly confidence tracking (`PMO-00.06`).

---

## [1.0.0] - 2026-09-26 — Initial Release
- Initial baseline collection of project management templates and guide files.
