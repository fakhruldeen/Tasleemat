---
type: Guide
---
# Tasleemat Release Notes

## 🚀 Tasleemat v2.6.1 — 100% Tailoring Matrix Coverage, Native MCP Project Auditor & Modern Packaging

**Release Date:** October 16, 2026  
**PyPI Version:** [`tasleemat 2.6.1`](https://pypi.org/project/tasleemat/2.6.1/)  
**Git Tag:** [`v2.6.1`](https://github.com/fakhruldeen/Tasleemat/releases/tag/v2.6.1)  

---

### 🎯 100% Tailoring Matrix & Tier Pack Mapping
- **Zero Unmapped Deliverables:** Mapped 100% of all 114 deliverables across Tier 1 (Enterprise/Strategic), Tier 2 (Standard Enterprise), and Tier 3 (Lean/Fast-Track).
- **5 Comprehensive Methodology Packs:** Enhanced `General / PMBOK`, `Agile / Scrum`, `AI Governance & Engineering`, `Predictive / Waterfall`, and `Hybrid` packs to cover the full project governance spectrum.
- **Dynamic Scaffolding:** CLI `tasleemat init` and TUI Scaffolding Wizard now scaffold any methodology or governance tier without omitting core planning deliverables.

### 🤖 Native MCP Project Governance Auditor (`tasleemat_audit_project`)
- **Direct Protocol Tool:** Exposes `audit_project()` over JSON-RPC stdio transport in `tasleemat.mcp.server`, enabling AI agents (Cursor, Claude, Antigravity, OpenCode) to audit project workspaces directly.
- **Multi-Pack Discovery:** Added `pack` filtering (`general`, `agile`, `ai`, `predictive`, `hybrid`) to `tasleemat_list_artifacts`.

### 📦 Standardized PEP 517/518 Packaging Architecture
- **Root `pyproject.toml`:** Modernized build architecture eliminating pip build deprecation warnings.
- **Metadata Polish:** Refined PyPI package classifiers to reflect enterprise management and project office domains.

---

## 🚀 Tasleemat v2.6.0 — Bilingual Terminal Workstation (TUI), Governance Auditor & 8 AI Agent Integrations

**Release Date:** October 15, 2026  
**PyPI Version:** [`tasleemat 2.6.0`](https://pypi.org/project/tasleemat/2.6.0/)  
**Git Tag:** [`v2.6.0`](https://github.com/fakhruldeen/Tasleemat/releases/tag/v2.6.0)  

---

### 🖥️ Interactive Bilingual Terminal User Interface (TUI)
- Full-screen terminal dashboard powered by Textual with real-time bidirectional Arabic text shaping (`arabic-reshaper` & `python-bidi`).
- **8 Dedicated Workspaces:** Scaffolding Wizard, Deliverables Browser, Live AI Generator, Governance Auditor & Verification, MCP Diagnostics, Earned Value Analysis (EVA) Calculator, Bilingual Lexicon Dictionary, and Settings.

### 🛡️ Project Governance Auditor & Verification Engine
- Analyzes scaffolded project workspaces against required methodology packs and governance tiers.
- Generates compliance KPIs: Overall Completion %, Governance Score %, and Schema Compliance %.
- 6-Stage Gate Readiness Matrix (Gate 0 Strategic Alignment through Gate 5 Operational Handover & Closeout).

### 🤖 Universal Multi-Agent Ecosystem (8 Native Integrations)
- 1-click workspace scaffolding and rule generation for Cursor, Google Antigravity, Claude Desktop, VS Code, OpenCode, Cline, Windsurf, and OpenAI CLI.

### 🌐 Universal Multi-Provider LLM Engine
- Zero-lockin multi-provider client supporting Google Gemini (defaulting to `gemini-3.8-flash`), Anthropic, OpenAI, OpenRouter, DeepSeek, Groq, and Ollama.

---

## 🚀 Tasleemat v2.5.0 — 100% Completed-Data Companion Schema Coverage & Pure-Python Validation Engine

**Release Date:** October 13, 2026  
**PyPI Version:** [`tasleemat 2.5.0`](https://pypi.org/project/tasleemat/2.5.0/)  
**Git Tag:** [`v2.5.0`](https://github.com/fakhruldeen/Tasleemat/releases/tag/v2.5.0)  

---

### 🔍 100% Completed-Data Companion Schema Coverage
- Companion JSON schemas (Draft 2020-12) delivered for all 114 deliverables in `tasleemat/schemas/completed/`.
- Pure-Python validation engine supporting RFC format checks, strict stage-gate evaluation, and draft warning modes.

---

## 🚀 Tasleemat v2.4.1 — Native Model Context Protocol (MCP) Server & LLM Ecosystem Integration

**Release Date:** October 12, 2026  
**PyPI Version:** [`tasleemat 2.4.1`](https://pypi.org/project/tasleemat/2.4.1/)  
**Git Tag:** [`v2.4.1`](https://github.com/fakhruldeen/Tasleemat/releases/tag/v2.4.1)  

---

### ⚡ Standard Model Context Protocol (MCP) Server (`tasleemat.mcp`)
- **Native JSON-RPC 2.0 Stdio Server:** Built a zero-dependency Model Context Protocol (MCP) server enabling instant, seamless plug-and-play integration with Claude Desktop, Cursor, OpenCode, and any MCP-compliant AI client.
- **6 Standard PMO Tools:**
  1. `tasleemat_list_artifacts`: Filter and discover deliverables by phase or tailoring tier.
  2. `tasleemat_get_artifact`: Inspect metadata, available languages, and assets for any deliverable ID (`PMO-XX.YY`).
  3. `tasleemat_get_asset`: Fetch raw bilingual templates, guides, checklists, or prompt templates.
  4. `tasleemat_get_lexicon`: Query standardized English-Arabic PMI/DGA PMO terminology.
  5. `tasleemat_validate_data`: Perform strict or draft JSON schema validation against completed deliverable payloads.
  6. `tasleemat_render_artifact`: Render offline, print-ready HTML documents with document control headers.
- **Direct MCP Resources:**
  - `pmo://catalog`: Real-time JSON manifest of all 114 deliverables.
  - `pmo://lexicon`: Full bilingual English-Arabic PMO terminology dictionary.
- **Standard MCP Prompts:** Pre-engineered, parameterized prompt templates:
  - `draft_project_charter`: Guided bilingual charter generation with scope, stakeholders, and milestones.
  - `conduct_risk_assessment`: Systematic risk identification, scoring, and response planning.
- **Dual Execution Entrypoints:** Launch directly via `tasleemat-mcp` or `tasleemat mcp`.

---

### 🤖 LLM Assistant Ecosystem & Workflows
- **Multi-Client MCP Configuration Guide (`docs/MCP_INTEGRATION.md`):** Comprehensive instructions, step-by-step screenshots/JSON configs for Claude Desktop (`claude_desktop_config.json`), Cursor IDE, and OpenCode.
- **Frictionless OKF Context Injection:** Detailed blueprints on feeding `datapackage.json` directly into LLM prompts (ChatGPT, Claude, Gemini, OpenCode) to ground agents on exact schema types, field names, and validation rules.
- **Prompt Engineering Templates:** Ready-to-use prompt patterns for bilingual project document generation and review.

---

### 🧪 Test Coverage & Packaging Polish
- **11 New MCP Server Tests:** Added `tests/test_mcp_server.py` verifying MCP protocol initialization, tools listing, tool invocation, resource reading, prompt fetching, and error formatting (expanding total test suite to 73 unit tests).
- **Synchronized Distribution Builds:** Rebuilt wheel (`tasleemat-2.4.1-py3-none-any.whl`) and sdist archive (`tasleemat-2.4.1.tar.gz`).
- **Complete Forms Immutability:** 100% preservation of all 1,162 files in the `forms/` directory verified against baseline SHA-256 manifests.

---

## 🚀 Tasleemat v2.4.0 — Programmatic Python API, Structural Validation & Agent Integration

**Release Date:** October 12, 2026  
**PyPI Version:** [`tasleemat 2.4.0`](https://pypi.org/project/tasleemat/2.4.0/)  
**Git Tag:** [`v2.4.0`](https://github.com/fakhruldeen/Tasleemat/releases/tag/v2.4.0)  

---

### 🧩 First-Class Programmatic Python API (`import tasleemat`)
- **Direct Python Import:** Reusable, clean top-level functions `list_artifacts()`, `get_artifact_definition()`, `get_artifact_assets()`, `get_artifact_asset()`, `get_tailoring_profile()`, `get_lexicon()`, `validate_artifact_data()`, and `render_artifact()`.
- **Deterministic 114-Deliverable Catalog:** Generated and bundled `tasleemat/data/catalog.json` with SHA-256 content fingerprints and bilingual metadata for instant offline discovery without disk scans.
- **Bilingual PMO Terminology API:** Dedicated `get_lexicon(category=...)` function providing fast lookup for standardized English-Arabic PMI and Saudi DGA terminology.

### 🔍 Structural JSON Data Validation & Contracts
- **Draft 2020-12 Companion Schemas:** Added complete structural data schemas for representative deliverables (`PMO-03.01`, `PMO-04.08.02`, `PMO-06.01`) in `tasleemat/schemas/completed/`.
- **Strict vs. Draft Modes:** Full support for strict production validation (for stage-gate approvals) alongside draft validation (for AI agent generation cycles) with non-blocking warnings.
- **Traceable Error Structure:** Returns structured `ValidationReport` with JSON pointer field paths, machine-readable error codes, messages, and package version tracking.

### 🎨 Standalone Offline Rendering Engine
- **Print-Ready HTML Generation:** Self-contained document renderer with responsive typography, document sign-off blocks, and document control tables.
- **Strict Immutability Assurance:** Enforced write protection blocking any rendered exports inside the immutable `forms/` directory.

### 🤖 Decoupled Downstream Agent Integration (Maharat Ready)
- **Clear Governance Boundary:** Documented contract separating Tasleemat structural data contracts from downstream methodological/evidence checks.
- **Clean Environment Wheel Execution:** Full verification suite ensuring the distributed wheel installs and runs seamlessly outside repository source trees.

---

## 🚀 Tasleemat v2.3.1 — Electronic Audit Trail, Portal Interactivity & GitBook Sync

**Release Date:** October 11, 2026  
**PyPI Version:** [`tasleemat 2.3.1`](https://pypi.org/project/tasleemat/2.3.1/)  
**Git Tag:** [`v2.3.1`](https://github.com/fakhruldeen/Tasleemat/releases/tag/v2.3.1)  

---

### 🔒 Cryptographic Audit Trail & Governance Assurance
- **Standardized SHA-256 Audit Trail Placeholder:** Embedded `سجل التدقيق الإلكتروني: Hash SHA256: (####)` in all Arabic templates and `Electronic Audit Trail: Hash SHA256: (####)` in all English templates directly above the document approval and control blocks across all 228 project artifacts.
- **Automated Workspace Hash Computing:** Integrated automated cryptographic SHA-256 calculation hooks into the CLI scaffolder and Python SDK (`tasleemat init`) for automatic hash population upon artifact generation and sign-off.
- **Strict CI Audit Parity:** Resolved CI linting and schema parity checks to enforce 100% document control consistency and field alignments between English and Arabic bundles.

---

### 🌐 Bilingual Web Portal & Interactive Experience
- **Catalog Navigation & Filter Hit-Testing:** Fixed z-index layering and modal backdrop hit-testing issues on both English and Arabic catalog interfaces (`catalog/en/index.html` and `catalog/ar/index.html`), restoring smooth filtering across project lifecycle phases and tailoring tiers.
- **Native Arabic Governance Stage-Gate Portal (`governance_ar.html`):** Released a fully localized Arabic Stage-Gate console matching `governance.html`, featuring interactive exit criteria checklists for all 6 gates (Gate 00 to Gate 05), local decision logging with persistent audit trails, and instant Markdown governance dossier export.
- **Markdown Inspector Engine (`marked.js`):** Slide-over inspect drawers in the deliverable catalogs now render richly formatted HTML with tables, checklists, and status badges by default, with a one-click toggle to view raw Markdown source.
- **Interactive Tailoring Sizing Calculator:** Resolved bundle profile export issues in the interactive sizing tool, enabling project managers to download tailored deliverable packs based on budget, team size, and risk rating.
- **Dedicated PMO Lexicon Portal (`LEXICON.html`):** Added a searchable, categorized bilingual reference index with 164+ standardized PMI/DGA PMO terminology pairs.

---

### 📚 GitBook Site Git Sync Integration
- **Canonical `gitbook-docs.yaml` Manifest:** Created and verified configuration conforming to the GitBook schema specification, structuring the repository into 8 bilingual sections and spaces:
  - Governance Manuals (`docs/en` & `docs/ar`)
  - Implementation Guides (`docs/guides/en` & `docs/guides/ar`)
  - Forms & Templates (`docs/forms/en` & `docs/forms/ar`)
  - Reference Examples (`docs/examples/en` & `docs/examples/ar`)

---

### 📦 Standards, Packaging & Badging
- **OKF Data Package Manifest v2.3.1:** Updated `datapackage.json` and generator tools (`tools/generate_datapackage.py`) covering all 228 bilingual JSON schema resources conforming to Frictionless Data specs.
- **PyPI Release (v2.3.1):** Rebuilt and released source distribution (`.tar.gz`) and wheel (`.whl`) packages for the `tasleemat` Python package.
- **Refreshed Visual Badges:** Added official PyPI badges (`for-the-badge` style) to both `README.md` and `README_AR.md`.

---

## 📦 Tasleemat v2.3.0 — 114 Deliverables & Bidirectional Web Portal

- **Expanded Deliverables Corpus:** Scaled library from 102 to 114 bilingual deliverable bundles (228 total artifacts).
- **Bidirectional GitHub Pages Portal:** Launched executive documentation portal with full RTL/LTR parity deployed via GitHub Actions.
- **Interactive Tailoring Sizing Tool:** Sizing calculator mapping project budget, duration, and risk profile to 4 governance tiers.

---


### 🤖 Multi-Provider LLM Engine (`tasleemat.ai` & CLI `tasleemat generate`)
- **Multi-Model Support**: Integrated a zero-dependency AI engine supporting 5 providers: **Google Gemini API** (`gemini-2.5-flash`), **OpenAI API** (`gpt-4o`), **Anthropic Claude API** (`claude-3-5-sonnet-20241022`), **Local Ollama** (`llama3.2`), and an offline **Mock Engine**.
- **CLI Configuration (`tasleemat config`)**: Command-line key management and provider switching (`tasleemat config set --provider gemini --model gemini-2.5-flash`).
- **Automated Form Auto-Filling (`tasleemat generate`)**: Auto-fill any of the 102 PMO artifacts in seconds from raw meeting notes or project parameters.
- **Python SDK Package**: Official PyPI release `tasleemat` version 2.1.0 featuring programmable Python API (`from tasleemat.ai import AIClient`).

### 📦 PyPI & Packaging Improvements
- **SDK Build Pipeline**: Introduced `sdk/python/build.sh` and modular `setup.py` packaging for PyPI distribution.
- **PyPI Release**: Successfully published to PyPI ([https://pypi.org/project/tasleemat/2.1.0/](https://pypi.org/project/tasleemat/2.1.0/)).

---

## 🛠️ Tasleemat v2.0.3 & v2.0.2

- **Zenodo DOI Integration**: Updated DOI badges and citations to the concept master DOI `10.5281/zenodo.23193523`.
- **Hidden Template Frontmatter**: Wrapped OKF YAML metadata in `<!-- -->` HTML comments across all templates and README files so browsers do not render metadata tables directly.
- **Audit Tooling Patch**: Patched `tools/audit_forms.py` to strip HTML comments before evaluating bilingual character parity.
