# 🤝 Contributing to Tasleemat PMO Operating System

Thank you for your interest in contributing to **Tasleemat (تسليمات)**! As an enterprise-grade, open-source project management standard, we maintain rigorous quality and parity standards to ensure trust and consistency for practitioners worldwide.

---

## 🏛️ Core Principles & Requirements

Before submitting any contribution, please review these core rules:

### 1. 🌐 Strict 1:1 Bilingual Parity
Every deliverable in Tasleemat exists in **symmetric English and Arabic pairs**:
- If you add or modify a form in `forms/en/`, you **must** make the equivalent modification in `forms/ar/`.
- Both versions must match in section headings, table columns, field schemas, JSON structures, and CSV dictionaries.
- Always use standard PMI-approved Arabic terminology as codified in [`docs/LEXICON.md`](docs/LEXICON.md).

### 2. 🗂️ The 5-File Artifact Bundle Standard
Every form directory must contain exactly 5 synchronized files:
1. `*_Template.md` / `*_قالب.md` (Pure fillable markdown template with Document Control table)
2. `*_Guide.md` / `*_دليل.md` (Practitioner operational instructions, RACI, and dependencies)
3. `*.md` (LLM prompt for autonomous drafting)
4. `*.json` (Machine-readable schema definition)
5. `*.csv` (4-column tabular dictionary conforming to OKF Frictionless Data standard)

### 3. 🛡️ 100% Fictional Data Compliance
- **Never use real company names, telecommunication brands, ministries, or living individuals** in examples or documentation.
- Standardize on fictional benchmark entities (e.g. *Apex Global Solutions*, *Nexus ERP*).

---

## 🛠️ Local Development & Testing Workflow

### 1. Fork & Clone Repository
```bash
git clone https://github.com/your-username/Tasleemat.git
cd Tasleemat
```

### 2. Run Built-In Verification Suite
Before opening a Pull Request, run the full verification suite to ensure 0 errors:

```bash
# 1. Check form structure and sign-off tables
python3 tools/audit_forms.py

# 2. Verify web rendering and syntax
python3 tools/check_rendering.py

# 3. Verify English/Arabic 1:1 structural symmetry
python3 tools/parity.py forms/en forms/ar

# 4. Verify Open Knowledge Foundation (OKF) Frictionless Data compliance
python3 tools/validate_okf.py
```

All tests must output **0 errors** and **PARITY OK**.

---

## 📬 Pull Request Process

1. Create a descriptive feature branch: `git checkout -b feat/add-evm-agile-metric`.
2. Commit with conventional commit messages (e.g., `feat:`, `fix:`, `docs:`, `refactor:`).
3. Push to your fork and open a Pull Request against `main`.
4. Ensure all GitHub Actions CI checks pass.

Thank you for making project management better for everyone!
