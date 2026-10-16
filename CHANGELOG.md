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

## [2.6.2] - 2026-10-17 — Offline Airgapped Documentation, UNIX Man Pages, Brand Identity & PyPI Discoverability

### 📚 Comprehensive Offline Knowledge Base & Documentation (`tasleemat docs`)
- **Airgapped Operations Handbook (`tasleemat docs airgap`):** Complete guide for zero-telemetry installations, offline wheel deployment via `pip install --no-index --find-links`, local LLM inference (Ollama, vLLM, mock mode), and local Draft 2020-12 schema validation.
- **Deep-Dive Knowledge Guides:** Added 9 integrated offline topics accessible with zero network connectivity: `airgap`, `tiers` (governance sizing matrix), `packs` (5 methodology packs), `gates` (6 Stage-Gates criteria & RACI), `eva` (mathematical Earned Value formulas), `mcp` (AI agent orchestration), `catalog` (114 deliverables directory), `lexicon` (bilingual dictionary), and `cli` (command manual).

### 📖 Standard UNIX Man Pages (`tasleemat man` & `docs/tasleemat.1`)
- **System Man Integration:** Created official troff/groff manual page `docs/tasleemat.1` compatible with standard Linux/Unix `man ./docs/tasleemat.1`.
- **Interactive Terminal Viewer:** `tasleemat man [command]` launches with interactive pager support (`less -R`).

### ⚡ Enhanced CLI Help System (`--help` / `-h`)
- **Dynamic Color Configuration:** Added automatic `NO_COLOR` and non-tty detection for clean piping and automated logging.
- **Subcommand Manuals:** Upgraded root and subcommand help (`tasleemat init -h`, `tasleemat audit -h`) with rich parameter tables, airgap notes, and real-world examples.

### 🎨 Visual Identity & PyPI Discoverability
- **Brand Assets:** Integrated high-resolution architecture overview banner (`Readme.jpeg`), square package logo (`logo-sq.png`), unified brand logo (`logo.png`), and social preview cards (`social.jpeg`).
- **PyPI Showcase:** Enhanced package metadata in `setup.py` with custom logo rendering, author profile (Mohamed Fakhruldeen), verified URLs (`fakhr.me` & `fakhr.me/Tasleemat`), search keywords, and 29 validated Trove classifiers.

---

## [2.6.1] - 2026-10-16 — 100% Tailoring Matrix Coverage, Native MCP Project Auditor & Modern Packaging

### 🎯 100% Tailoring Matrix Coverage (Zero Unmapped Deliverables)
- **Complete Tier Mapping:** Mapped all 114 deliverables across Tier 1 (Enterprise/Strategic), Tier 2 (Standard Enterprise), and Tier 3 (Lean/Fast-Track) in `tools/tasleemat_cli.py` (`TIER_PACKS`).
- **Comprehensive Methodology Packs:** Full coverage across all 5 methodology packs: `General / PMBOK`, `Agile / Scrum`, `AI Governance & Engineering`, `Predictive / Waterfall`, and `Hybrid`.
- **Verified Zero Gaps:** Validated that 100% of deliverables in `tasleemat/data/catalog.json` feature non-empty tailoring tiers and packs.

### 🤖 Native MCP Project Governance Auditor (`tasleemat_audit_project`)
- **Direct Protocol Tool:** Exposes `audit_project()` over JSON-RPC stdio transport in `tasleemat.mcp.server`, allowing AI agents (Cursor, Claude, Antigravity) to audit project workspaces directly.
- **Multi-Pack Discovery:** Added `pack` filtering (`general`, `agile`, `ai`, `predictive`, `hybrid`) to `tasleemat_list_artifacts`.

### 📦 Standardized PEP 517/518 Packaging Architecture
- **Root `pyproject.toml`:** Modernized build architecture eliminating pip build deprecation warnings.
- **Metadata Polish:** Refined PyPI package classifiers to reflect enterprise management and project office domains.

---

## [2.6.0] - 2026-10-15 — Bilingual Terminal Workstation (TUI), Project Governance Auditor & 8 AI Agent Integrations

### 🖥️ Interactive Bilingual Terminal User Interface (TUI)
- **Textual-Powered Dashboard:** Full-screen terminal dashboard (`tasleemat tui`) with real-time bidirectional Arabic text shaping (`arabic-reshaper` and `python-bidi`).
- **8 Dedicated Workspaces:** Scaffolding Wizard, Deliverables Browser, Live AI Generator, Governance Auditor, MCP Diagnostics, Earned Value Analysis (EVA) Calculator, Lexicon Dictionary, and Settings.

### 🛡️ Project Governance Auditor & Verification Engine
- **Command & Library:** Introduced `tasleemat audit [path]` and `tasleemat.audit_project()`.
- **Compliance Metrics:** Real-time ANSI progress bars for Overall Completion %, Governance Score %, and Schema Compliance %.
- **6-Stage Gate Readiness Matrix:** Evaluates transition criteria across Gate 0 (Strategic Alignment) through Gate 5 (Handover & Closeout).

### 🤖 Universal Multi-Agent Ecosystem (8 Native Integrations)
- **1-Click Agent Setup:** Automated scaffolding and rule generation for Cursor, Google Antigravity, Claude Desktop, VS Code, OpenCode, Cline, Windsurf, and OpenAI CLI.

### 🌐 Universal Multi-Provider LLM Engine
- **Dynamic AI Client:** Zero-lockin multi-provider client supporting Google Gemini (defaulting to `gemini-3.8-flash`), Anthropic, OpenAI, OpenRouter, DeepSeek, Groq, and Ollama.

---

## [2.5.0] - 2026-10-13 — 100% Completed-Data Companion Schema Coverage & Pure-Python Validation Engine

### 🔍 100% Structural JSON Schema Coverage
- **114 Companion Schemas:** Added Draft 2020-12 companion JSON schemas for all 114 deliverables in `tasleemat/schemas/completed/`.
- **Pure-Python Validation:** Built-in validation engine supporting RFC format checks, strict stage-gate evaluation, and draft warning modes.

---

## [2.4.1] - 2026-10-12 — Native Model Context Protocol (MCP) Server & LLM Ecosystem Integration

### ⚡ Standard Model Context Protocol (MCP) Server
- **Zero-Dependency Stdio MCP Server:** Introduced `tasleemat.mcp` module providing a standard JSON-RPC 2.0 stdio MCP server executable via `tasleemat-mcp` or `python -m tasleemat.mcp`.
- **6 Enterprise PMO Tools:** Exposes `tasleemat_list_artifacts`, `tasleemat_get_artifact`, `tasleemat_get_asset`, `tasleemat_get_lexicon`, `tasleemat_validate_data`, and `tasleemat_render_artifact`.
- **Standardized MCP Resources:** Exposes `pmo://catalog` (full 114 artifact catalog JSON) and `pmo://lexicon` (complete bilingual terminology dictionary) for direct LLM context retrieval.
- **Pre-Engineered PMO Prompts:** Exposes `draft_project_charter` and `conduct_risk_assessment` parameterized workflows for AI agents.
- **CLI Command:** Added `tasleemat mcp` subcommand to launch the server directly from the standard CLI.

### 🤖 LLM Ecosystem Guides & Integration Docs
- **Multi-Client MCP Guide (`docs/MCP_INTEGRATION.md`):** Complete setup guides and configuration snippets for Claude Desktop (`claude_desktop_config.json`), Cursor IDE, and OpenCode.
- **Frictionless OKF in LLM Context:** Documented how to feed `datapackage.json` and artifact field dictionaries into LLM context windows to achieve 100% structural fidelity and eliminate hallucinations.
- **Enhanced Documentation:** Updated `README.md`, `README_AR.md`, and `sdk/python/README.md` with instructions for ChatGPT, Claude, and OpenCode workflows.

### 🧪 Test Coverage & Package Polish
- **MCP Test Suite:** Added `tests/test_mcp_server.py` with 11 comprehensive unit tests covering protocol handshakes, tool executions, resource reads, prompt rendering, and error handling (bringing total suite to 73 tests).
- **Distribution Packages:** Built updated wheel (`tasleemat-2.4.1-py3-none-any.whl`) and source distribution (`tasleemat-2.4.1.tar.gz`).
- **Catalog & Version Synchronization:** Updated package versions across `datapackage.json`, `setup.py`, and `tasleemat/data/catalog.json`.

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
