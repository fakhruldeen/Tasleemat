# Tasleemat v2.0.2

### 🛠️ Bug Fixes & Refinements
- **Hidden Template Frontmatter**: Wrapped the OKF YAML frontmatter in `<!-- -->` HTML comments across all `_Template.md`, `_قالب.md`, and `README.md` files. This ensures that browsers (e.g., GitHub Web UI) do not render the machine-readable metadata tables directly to human end-users.
- **Audit Tooling Patch**: Re-engineered `tools/audit_forms.py` to correctly strip the content *inside* HTML comments prior to evaluating English/Arabic character parity. This resolves the CI/CD pipeline failure where the English OKF metadata inside Arabic templates was incorrectly flagged as "untranslated Latin".
