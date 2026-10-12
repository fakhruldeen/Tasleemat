---
type: Document
token_pointer: /_tokens/CHANGELOG.npy
token_count: 631
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.026815+00:00'
---

# 📜 Changelog

All notable changes to the **Tasleemat (تسليمات)** PMO Operating System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.4.0] - 2026-10-12 — Programmatic Python API, Structural Validation & Agent Integration

### 🧩 Programmatic Python API (`import tasleemat`)
- **Direct Library Access:** Exposed public API functions in `tasleemat`: `list_artifacts`, `get_artifact_definition`, `get_artifact_assets`, `get_artifact_asset`, `get_tailoring_profile`, `get_lexicon`, `validate_artifact_data`, and `render_artifact`.
- **Deterministic Artifact Catalog:** Generated centralized `tasleemat/data/catalog.json` indexing all 114 deliverables with verified SHA-256 content fingerprints and bilingual metadata.
- **Bilingual PMO Terminology Registry:** Bundled `tasleemat/data/lexicon.json` with `get_lexicon(category=...)` supporting filtered queries for PMI/DGA PMO terminology pairs.

### 🔍 Structural Data Validation Contracts
- **Draft 2020-12 Companion JSON Schemas:** Delivered strict schemas for representative deliverables (`PMO-03.01`, `PMO-04.08.02`, `PMO-06.01`) in `tasleemat/schemas/completed/`.
- **Validation Engine:** Built-in validator supporting `strict` mode (for formal stage-gate approval) and `draft` mode (for non-blocking agent drafting loops with warnings).
- **Traceable Error Reporting:** Detailed `ValidationReport` returning field paths (`/project_name`), error codes (`REQUIRED_FIELD_MISSING`, `INVALID_TYPE`), human-readable messages, and package version stamp.

### 🎨 Standalone Offline Rendering
- **Zero-Dependency Document Renderer:** Generates styled, print-ready HTML with responsive styling, status badges, and Document Control tables via `tasleemat.render_artifact`.
- **Strict Immutability Guards:** Runtime path verification prevents rendering exports into the protected `forms/` directory.

### 🤖 Downstream Agent Integration Contract (Maharat Ready)
- **Decoupled Boundary:** Established clear division of responsibility where Tasleemat provides canonical artifact definitions, templates, structural schemas, and validation, while downstream orchestrators (like Maharat) handle methodological reasoning, evidence checks, and human approvals.
- **Comprehensive Test Suite:** Added 23 new test cases across `test_consumer_interface.py`, `test_maharat_integration_contract.py`, and `test_wheel_clean_install.py` verifying programmatic execution outside source checkouts.

---

## [2.3.1] - 2026-10-11 — Portal Enhancements, Cryptographic Audit Trail & Release Polish

### 🔒 Governance & Cryptographic Integrity
- **SHA-256 Electronic Audit Trail:** Embedded standardized audit trail placeholders (`{{Audit_Trail_SHA256_Hash}}` in English and `{{رمز_تجزئة_التدقيق_SHA256}}` in Arabic) across all 228 project templates, positioned directly above template reference lines for post-approval signing.
- **Automated CLI Hash Calculation:** Updated `tasleemat init` and workspace scaffolder to automatically compute cryptographic SHA-256 document hashes upon workspace generation.

### 🌐 Web Portal & Usability Overhaul
- **Catalog Filter Hit-Testing Fix:** Eliminated modal/drawer click-blocking overlays (`display: none`), restoring full interactivity for Phase and Tailoring Tier filters across both English and Arabic portals.
- **Dedicated Bilingual Stage-Gate Portal (`governance_ar.html`):** Built a 100% Arabic symmetrical governance portal with interactive exit checklists for all 6 gates (Gate 00 to 05), RACI matrices, live decision logging to local audit history, and Markdown dossier export.
- **Rendered Markdown in Deliverable Inspector:** Integrated `marked.js` to render formatted HTML (tables, checklists, badges) by default with an instant raw Markdown toggle in catalog slide-over drawers.
- **Bilingual PMO Lexicon Page (`LEXICON.html`):** Added a dedicated standalone reference page indexing 164+ standardized PMI and DGA PMO terminology pairs.
- **Executive Navigation & Author Profile:** Overhauled root `README.md` and `README_AR.md` with persona-based jump-links, visual 8-phase lifecycle charts, 4 tailoring tiers, and official maintainer links.

### 📦 Packaging & Standards
- **Open Knowledge Foundation (OKF) Data Package v2.3.1:** Updated root `datapackage.json` with 228 verified JSON schemas conforming to Frictionless Data specs.
- **PyPI Release (v2.3.1):** Bumped version to `2.3.1` in `sdk/python/setup.py` and synchronized package distributions.

---

## [2.3.0] - 2026-10-10 — 114 Deliverables & Bidirectional Web Portal

### 🚀 Highlights
- **Expanded Deliverables Corpus:** Scaled from 102 to 114 comprehensive deliverables (228 total bilingual bundles).
- **Bidirectional GitHub Pages Portal:** Launched executive documentation portal with full RTL/LTR parity deployed via GitHub Actions.
- **Interactive Tailoring Sizing Tool:** Sizing calculator mapping project budget, duration, and risk profile to 4 governance tiers.

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
