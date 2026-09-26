<div align="center">
  <h1>🚀 Tasleemat PMO Toolkit</h1>
  <p><b>The Ultimate AI-Ready, Dual-Language (English & Arabic) Project Management Framework</b></p>
  <a href="./README_AR.md">🇸🇦 اقرأ هذا باللغة العربية (Read in Arabic)</a>
</div>

---

## 🌟 Overview
**Tasleemat (تسليمات)** is an enterprise-grade Project Management Office (PMO) toolkit. It provides a complete chronological lifecycle of over 68 professional project artifacts, ranging from Portfolio Roadmaps to Project Charters, Agile Sprint Planning, and AI Governance.

This repository is uniquely engineered for the modern era:
- **🤖 LLM-Ready:** Every form includes a dedicated `.json` schema and Markdown prompt designed to be injected directly into ChatGPT, Claude, or Gemini for automated, highly-accurate document generation.
- **🌐 Dual-Language (i18n):** Flawlessly localized into formal Arabic (RTL) alongside the primary English templates, including fully translated file names and cross-reference links.
- **🖨️ Print-Ready:** Beautiful HTML/Markdown hybrid templates that export perfectly to PDF with signature footers and document control numbers.
- **📖 GitHub Pages Ready:** Completely configured with Jekyll metadata and navigation files.

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
├── scripts/               # Python generators used to build the repo
├── source_files/          # Original reference materials
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

## 🌐 Deploying to GitHub Pages
This repository is pre-configured to be hosted as a beautiful documentation website.
1. Push this repository to GitHub.
2. Go to your repository **Settings** > **Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Select the `main` branch and `/ (root)` folder, then click **Save**.
5. Within minutes, your toolkit will be live online!

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
