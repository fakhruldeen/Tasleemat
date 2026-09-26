<div align="center">
  <h1>🚀 Tasleemat PMO Toolkit</h1>
  <p><b>A Comprehensive, Dual-Language (English & Arabic) Reference Guide and Template Library for Project Managers</b></p>
  <a href="./README_AR.md">🇸🇦 اقرأ هذا باللغة العربية (Read in Arabic)</a>
</div>

---

## 🌟 Overview
**Tasleemat (تسليمات)** is an enterprise-grade Project Management Office (PMO) toolkit. It provides a complete chronological lifecycle of over 68 professional project artifacts, ranging from Portfolio Roadmaps to Project Charters, Agile Sprint Planning, and AI Governance.

This repository is built primarily as a powerful reference tool for Project Managers, with advanced AI capabilities built-in:
- **📚 Comprehensive PMO Reference:** A complete guide for project managers covering the What, Why, When, Who, and How of 68+ essential project artifacts.
- **🖨️ Professional Templates:** Beautifully formatted, print-ready templates that export perfectly to PDF with signature footers and document control numbers.
- **🌐 Dual-Language (i18n):** Flawlessly localized into formal Arabic (RTL) alongside the primary English guidelines.
- **🤖 LLM-Ready (Advanced Usage):** Every form includes a dedicated `.json` schema and Markdown prompt designed to be injected into ChatGPT or Claude for automated document generation.
- **📖 GitHub Pages Ready:** Completely configured to serve as a live documentation website.

## 📂 Repository Structure
```text
Tasleemat/
├── forms/                 # 🇬🇧 English Artifacts (Root)
│   ├── 00_Program_and_Portfolio_Management/
│   ├── 01_Business_and_Value_Delivery/
│   ├── ... (Chronological Phases 02 to 07)
│   └── ar/                # 🇸🇦 Arabic Localized Artifacts
│       ├── 00_إدارة_البرامج_والمحافظ/
│       ├── 03_البدء/
│       └── ...
├── mapping.md             # The master registry of all Document IDs
└── USAGE_GUIDE.md         # Detailed instructions on how to use the toolkit
```

## 🛠️ How to Use (Quick Start)

### 1. Manual Usage
Navigate to any phase folder (e.g., `03_Initiating/01_Project_Charter`) and open the `_Template.md` file. You can print this file, export it to PDF, or copy it into Word/Notion to fill it out manually with your team.

### 2. AI-Powered Generation (Recommended)
Want to generate a Risk Register in seconds? 
1. Open the `parameters.md` file and define your project's global variables (Name, Budget, Sponsor, etc.).
2. Open the `.md` (Prompt) or `.json` file of the artifact you need.
3. Paste the prompt, the parameters, and your rough notes into an LLM (like ChatGPT).
4. Watch as the AI flawlessly populates the `_Template.md` structure for you!
*See [USAGE_GUIDE.md](./USAGE_GUIDE.md) for detailed AI workflows.*

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
