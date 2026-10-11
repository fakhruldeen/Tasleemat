---
type: Guide
---
# Tasleemat Release Notes

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
