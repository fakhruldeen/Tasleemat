---
type: Guide
---
# Tasleemat Release Notes

## 🚀 Tasleemat v2.1.0 — LLM AI Integration & PyPI Packaging Release

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
