#!/usr/bin/env python3
"""Tasleemat PMO Operating System - Official CLI Tool
Scaffold tailored project workspaces, search the deliverable catalog,
and inspect forms, RACI authorities, and dependencies.
"""

import os
import sys
import argparse
import datetime
import json
import shutil
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMS_DIR = ROOT / "forms"
DOCS_DIR = ROOT / "docs"
LEXICON_PATH = DOCS_DIR / "LEXICON.json"

# Color formatting for terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Form subsets by Tier & Methodology Pack
TIER_FORMS = {
    "1": [ # Tier 1: Strategic / Mega Enterprise (~45 forms)
        "00_01", "00_02", "00_03", "00_04", "00_06",
        "01_01", "01_02", "01_03", "01_04",
        "02_01", "02_02", "02_03", "02_04", "02_05", "02_06",
        "03_01", "03_02", "03_03", "03_04", "03_05",
        "04_01_01", "04_01_02", "04_01_03",
        "04_02_01", "04_02_03", "04_02_04", "04_02_05", "04_02_06", "04_02_07",
        "04_03_01", "04_03_02", "04_03_04", "04_03_07", "04_03_08",
        "04_04_01", "04_04_02", "04_04_04",
        "04_05_01", "04_05_02",
        "04_06_01", "04_06_04", "04_06_05", "04_06_06",
        "04_07_01",
        "04_08_01", "04_08_02", "04_08_03", "04_08_07",
        "04_09_01", "04_09_02", "04_09_04",
        "04_10_01", "04_11_01", "04_11_02", "04_12_01",
        "05_01", "05_02", "05_03", "05_04", "05_05", "05_06", "05_07", "05_11",
        "06_01", "06_04", "06_05", "06_06", "06_07", "06_08", "06_09", "06_10", "06_11",
        "07_01", "07_02", "07_03", "07_04", "07_05"
    ],
    "2": [ # Tier 2: Standard Enterprise (~24 forms)
        "01_01", "02_01",
        "03_01", "03_03", "03_04",
        "04_01_01", "04_02_05", "04_02_06",
        "04_03_07", "04_03_08",
        "04_04_04", "04_06_04", "04_07_01", "04_08_02",
        "05_01", "05_02", "05_03", "05_04",
        "06_01", "06_04", "06_08", "06_10",
        "07_01", "07_03", "07_04"
    ],
    "3": [ # Tier 3: Lean / Fast-Track (~9 forms)
        "03_01", "04_02_08", "04_03_02", "04_08_02",
        "05_01", "05_02", "06_01", "06_08", "07_03", "07_04"
    ]
}

PACK_FORMS = {
    "agile": [
        "03_02", "04_02_08", "04_02_09", "04_03_09", "04_03_10",
        "04_05_03", "04_06_06", "05_08", "06_12"
    ],
    "ai": [
        "02_02", "02_03", "02_04", "02_05", "02_06",
        "05_09", "06_11"
    ],
    "predictive": [
        "04_02_05", "04_02_06", "04_02_07", "04_03_05", "04_03_07",
        "04_04_02", "04_04_04", "04_08_03", "04_08_07", "06_05"
    ],
    "hybrid": [
        "03_01", "03_02", "04_01_03", "04_02_08", "04_02_09",
        "04_03_10", "04_05_03", "04_08_02", "05_01", "05_08",
        "06_01", "06_12", "07_03", "07_04"
    ]
}

def load_lexicon():
    if LEXICON_PATH.exists():
        with open(LEXICON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def find_form_files(lang="en"):
    """Index all available forms by form prefix ID."""
    base_dir = FORMS_DIR / lang
    forms_map = {}
    pattern = "*_Template.md" if lang == "en" else "*_قالب.md"
    for p in base_dir.rglob(pattern):
        # extract form prefix from filename e.g. 03_01 or 04_01_01
        filename = p.name
        prefix_match = re.match(r"^(\d{2}(?:_\d{2})+)", filename)
        if prefix_match:
            prefix = prefix_match.group(1)
            forms_map[prefix] = p.parent
    return forms_map

def scaffold_project(args):
    """Scaffold a new project workspace based on tier, pack, and language."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}===================================================={Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}   🚀 Tasleemat Project Workspace Scaffolder        {Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}===================================================={Colors.ENDC}\n")

    name = args.name or input(f"{Colors.OKCYAN}Enter Project Name [e.g. Smart City Platform]: {Colors.ENDC}").strip() or "Sample Project"
    code = args.code or input(f"{Colors.OKCYAN}Enter Project Code [e.g. PRJ-2026-001]: {Colors.ENDC}").strip() or "PRJ-2026-001"
    pm = args.pm or input(f"{Colors.OKCYAN}Enter Project Manager Name: {Colors.ENDC}").strip() or "Project Lead"
    sponsor = args.sponsor or input(f"{Colors.OKCYAN}Enter Project Sponsor Name: {Colors.ENDC}").strip() or "Executive Sponsor"
    tier = str(args.tier or input(f"{Colors.OKCYAN}Select Governance Tier [1=Enterprise, 2=Standard, 3=Lean] (default: 2): {Colors.ENDC}").strip() or "2")
    pack = (args.pack or input(f"{Colors.OKCYAN}Select Methodology Pack [general, agile, ai, predictive, hybrid] (default: general): {Colors.ENDC}").strip() or "general").lower()
    lang = (args.lang or input(f"{Colors.OKCYAN}Select Language [ar, en, both] (default: ar): {Colors.ENDC}").strip() or "ar").lower()
    
    out_dir_path = args.out or f"./{code}_{name.replace(' ', '_')}"
    out_dir = pathlib.Path(out_dir_path).resolve()

    # Determine form IDs
    selected_ids = set(TIER_FORMS.get(tier, TIER_FORMS["2"]))
    if pack in PACK_FORMS:
        selected_ids.update(PACK_FORMS[pack])

    target_langs = ["ar", "en"] if lang == "both" else [lang]
    print(f"\n{Colors.OKGREEN}⚡ Scaffolding {len(selected_ids)} tailored deliverables into: {out_dir}{Colors.ENDC}")

    date_str = datetime.date.today().isoformat()
    scaffolded_count = 0

    for l in target_langs:
        lang_dir = out_dir / l
        lang_dir.mkdir(parents=True, exist_ok=True)
        form_index = find_form_files(l)

        for form_id in sorted(selected_ids):
            # match prefix
            matched_folder = None
            for k, folder in form_index.items():
                if k == form_id or k.startswith(form_id + "_") or form_id.startswith(k + "_"):
                    matched_folder = folder
                    break
            
            if matched_folder and matched_folder.exists():
                dest_folder = lang_dir / matched_folder.relative_to(FORMS_DIR / l)
                dest_folder.mkdir(parents=True, exist_ok=True)

                # Copy files with header replacement
                for item in matched_folder.iterdir():
                    if item.is_file():
                        content = item.read_text(encoding="utf-8")
                        
                        # Replace curly-brace template variables
                        content = content.replace("{{اسم_المشروع}}", name)
                        content = content.replace("{{Project_Name}}", name)
                        content = content.replace("{{معرف_المشروع}}", code)
                        content = content.replace("{{Project_ID}}", code)
                        content = content.replace("{{Project_Code}}", code)
                        content = content.replace("{{اسم_مدير_المشروع}}", pm)
                        content = content.replace("{{Project_Manager}}", pm)
                        content = content.replace("{{اسم_راعي_المشروع}}", sponsor)
                        content = content.replace("{{Sponsor_Name}}", sponsor)
                        content = content.replace("{{التاريخ_الحالي}}", date_str)
                        content = content.replace("{{Current_Date}}", date_str)
                        content = content.replace("{{اسم_الشركة}}", "حلول القمة المؤسسية (Apex Solutions)")
                        content = content.replace("{{Company_Name}}", "Apex Enterprise Solutions")
                        
                        # Replace bracketed markdown field headers
                        content = re.sub(r'(\*\*اسم المشروع:\*\*|\*\*Project Name:\*\*)\s*\[.*?\]', rf'\1 {name}', content)
                        content = re.sub(r'(\*\*رمز المشروع:\*\*|\*\*Project ID:\*\*|\*\*Project Code:\*\*)\s*\[.*?\]', rf'\1 {code}', content)
                        content = re.sub(r'(\*\*مدير المشروع:\*\*|\*\*Project Manager:\*\*)\s*\[.*?\]', rf'\1 {pm}', content)
                        content = re.sub(r'(\*\*راعي المشروع:\*\*|\*\*Project Sponsor:\*\*)\s*\[.*?\]', rf'\1 {sponsor}', content)
                        content = re.sub(r'(\*\*تاريخ الوثيقة:\*\*|\*\*Date:\*\*)\s*\[.*?\]', rf'\1 {date_str}', content)
                        
                        (dest_folder / item.name).write_text(content, encoding="utf-8")
                scaffolded_count += 1

    # Create Tailored PROJECT_README.md
    readme_content = f"""# 📋 {name} (`{code}`) — Project Management Workspace
**Governance Tier:** Tier {tier} | **Methodology Pack:** {pack.upper()} | **Date:** {date_str}  
**Project Manager:** {pm} | **Project Sponsor:** {sponsor}  

---

## 🎯 Deliverables & Stage-Gate Checklist

| Phase | Deliverable Name | File Link | Status | Owner |
| :--- | :--- | :--- | :---: | :--- |
"""
    for l in target_langs:
        readme_content += f"\n### 📂 Deliverables ({'Arabic' if l == 'ar' else 'English'})\n"
        for form_id in sorted(selected_ids):
            readme_content += f"- [ ] **`{form_id}`** — `[{l.upper()}]` [Open Deliverable Folder]({l}/)\n"

    readme_content += """
---
*Generated automatically by **Tasleemat PMO Operating System** CLI.*
"""
    (out_dir / "PROJECT_README.md").write_text(readme_content, encoding="utf-8")

    print(f"\n{Colors.OKGREEN}✅ Successfully created project workspace with {scaffolded_count} deliverable bundles!{Colors.ENDC}")
    print(f"👉 Workspace Path: {Colors.BOLD}{out_dir}{Colors.ENDC}")
    print(f"👉 Project Guide: {Colors.BOLD}{out_dir / 'PROJECT_README.md'}{Colors.ENDC}\n")

def list_forms(args):
    """List all available forms."""
    lang = args.lang or "en"
    forms_map = find_form_files(lang)
    print(f"\n{Colors.HEADER}{Colors.BOLD}📚 Tasleemat Master Forms Catalog ({lang.upper()}){Colors.ENDC}\n")
    for k in sorted(forms_map.keys()):
        folder = forms_map[k]
        print(f"  • {Colors.OKCYAN}{k:<12}{Colors.ENDC} {folder.name}")
    print(f"\nTotal forms found: {len(forms_map)}\n")

def search_forms(args):
    """Search forms by keyword."""
    query = args.query.lower()
    lang = args.lang or "en"
    forms_map = find_form_files(lang)
    print(f"\n{Colors.HEADER}🔍 Searching forms for '{query}' ({lang.upper()}):{Colors.ENDC}\n")
    matches = 0
    for k, folder in sorted(forms_map.items()):
        if query in folder.name.lower() or query in k.lower():
            print(f"  [{Colors.OKGREEN}MATCH{Colors.ENDC}] {Colors.BOLD}{k}{Colors.ENDC} : {folder.name}")
            matches += 1
    if matches == 0:
        print(f"  No forms matching '{query}'.")
    print(f"\nTotal matches: {matches}\n")

def main():
    parser = argparse.ArgumentParser(description="Tasleemat PMO Operating System CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init / scaffold command
    init_parser = subparsers.add_parser("init", help="Scaffold a new tailored project workspace")
    init_parser.add_argument("-n", "--name", help="Project name")
    init_parser.add_argument("-c", "--code", help="Project code (e.g. PRJ-2026-001)")
    init_parser.add_argument("--pm", help="Project manager name")
    init_parser.add_argument("--sponsor", help="Project sponsor name")
    init_parser.add_argument("-t", "--tier", choices=["1", "2", "3"], help="Governance tier (1=Enterprise, 2=Standard, 3=Lean)")
    init_parser.add_argument("-p", "--pack", choices=["general", "agile", "ai", "predictive", "hybrid"], help="Methodology pack")
    init_parser.add_argument("-l", "--lang", choices=["ar", "en", "both"], help="Deliverable language")
    init_parser.add_argument("-o", "--out", help="Output directory")

    # list command
    list_parser = subparsers.add_parser("list", help="List all available forms")
    list_parser.add_argument("-l", "--lang", choices=["ar", "en"], default="en", help="Language")

    # search command
    search_parser = subparsers.add_parser("search", help="Search forms by keyword")
    search_parser.add_argument("query", help="Search keyword")
    search_parser.add_argument("-l", "--lang", choices=["ar", "en"], default="en", help="Language")

    args = parser.parse_args()
    if args.command == "init":
        scaffold_project(args)
    elif args.command == "list":
        list_forms(args)
    elif args.command == "search":
        search_forms(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
