## 📝 Description of Changes
<!-- Provide a brief summary of the changes made and the problem being solved. -->

## 🌐 Bilingual Parity Checklist
- [ ] Changes in `forms/en/` are mirrored symmetrically in `forms/ar/` (or vice-versa).
- [ ] Section headers and table structures match 1:1.
- [ ] Terminology aligns with [`docs/LEXICON.md`](docs/LEXICON.md).

## 🛡️ Quality & Verification Checks
- [ ] `python3 tools/audit_forms.py` (Passed with 0 errors)
- [ ] `python3 tools/check_rendering.py` (0 AT RISK templates)
- [ ] `python3 tools/parity.py forms/en forms/ar` (PARITY OK)
- [ ] `python3 tools/validate_okf.py` (Frictionless Data Package Valid)

## 🏢 Fictional Data Compliance
- [ ] No real company names, telecommunication brands, ministries, or living individuals are used.
