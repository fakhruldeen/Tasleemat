#!/usr/bin/env python3
"""
Tasleemat PMO Operating System CLI
Interactive project scaffolding, catalog search, automated testing, and LLM AI artifact generation.
"""

import sys
import os
import argparse
import pathlib
import datetime
import json
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMS_DIR = ROOT / "forms"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

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

TIER_PACKS = {
    "1": {
        "name": "Enterprise / Strategic (Tier 1)",
        "general": [
            "PMO-00.01", "PMO-00.02", "PMO-00.03", "PMO-00.04", "PMO-00.05", "PMO-00.06",
            "PMO-01.01", "PMO-01.02", "PMO-01.03", "PMO-01.04",
            "PMO-02.01", "PMO-02.02", "PMO-02.03", "PMO-02.04", "PMO-02.05", "PMO-02.06",
            "PMO-03.01", "PMO-03.02", "PMO-03.03", "PMO-03.04", "PMO-03.05",
            "PMO-04.01.01", "PMO-04.01.02", "PMO-04.01.03",
            "PMO-04.02.01", "PMO-04.02.02", "PMO-04.02.03", "PMO-04.02.04", "PMO-04.02.05", "PMO-04.02.06", "PMO-04.02.07", "PMO-04.02.08", "PMO-04.02.09",
            "PMO-04.03.01", "PMO-04.03.02", "PMO-04.03.03", "PMO-04.03.04", "PMO-04.03.05", "PMO-04.03.06", "PMO-04.03.07", "PMO-04.03.08", "PMO-04.03.09", "PMO-04.03.10",
            "PMO-04.04.01", "PMO-04.04.02", "PMO-04.04.03", "PMO-04.04.04",
            "PMO-04.05.01", "PMO-04.05.02", "PMO-04.05.03",
            "PMO-04.06.01", "PMO-04.06.02", "PMO-04.06.03", "PMO-04.06.04", "PMO-04.06.05", "PMO-04.06.06",
            "PMO-04.07.01", "PMO-04.07.02",
            "PMO-04.08.01", "PMO-04.08.02", "PMO-04.08.03", "PMO-04.08.04", "PMO-04.08.05", "PMO-04.08.06", "PMO-04.08.07",
            "PMO-04.09.01", "PMO-04.09.02", "PMO-04.09.03", "PMO-04.09.04", "PMO-04.09.05",
            "PMO-04.10.01", "PMO-04.10.02",
            "PMO-04.11.01", "PMO-04.11.02",
            "PMO-04.12.01",
            "PMO-04.13.01",
            "PMO-05.01", "PMO-05.02", "PMO-05.03", "PMO-05.04", "PMO-05.05", "PMO-05.06", "PMO-05.07", "PMO-05.08", "PMO-05.09", "PMO-05.10", "PMO-05.11", "PMO-05.12", "PMO-05.13", "PMO-05.14", "PMO-05.15",
            "PMO-06.01", "PMO-06.02", "PMO-06.03", "PMO-06.04", "PMO-06.05", "PMO-06.06", "PMO-06.07", "PMO-06.08", "PMO-06.09", "PMO-06.10", "PMO-06.11", "PMO-06.12", "PMO-06.13", "PMO-06.14", "PMO-06.15", "PMO-06.16",
            "PMO-07.01", "PMO-07.02", "PMO-07.03", "PMO-07.04", "PMO-07.05", "PMO-07.06", "PMO-07.07"
        ],
        "predictive": [
            "PMO-00.01", "PMO-00.02", "PMO-00.03", "PMO-00.04", "PMO-00.05", "PMO-00.06",
            "PMO-01.01", "PMO-01.02", "PMO-01.03", "PMO-01.04",
            "PMO-02.01",
            "PMO-03.01", "PMO-03.03", "PMO-03.04", "PMO-03.05",
            "PMO-04.01.01", "PMO-04.01.02", "PMO-04.01.03",
            "PMO-04.02.01", "PMO-04.02.02", "PMO-04.02.03", "PMO-04.02.04", "PMO-04.02.05", "PMO-04.02.06", "PMO-04.02.07",
            "PMO-04.03.01", "PMO-04.03.02", "PMO-04.03.03", "PMO-04.03.04", "PMO-04.03.05", "PMO-04.03.06", "PMO-04.03.07", "PMO-04.03.08",
            "PMO-04.04.01", "PMO-04.04.02", "PMO-04.04.03", "PMO-04.04.04",
            "PMO-04.05.01", "PMO-04.05.02",
            "PMO-04.06.01", "PMO-04.06.02", "PMO-04.06.03", "PMO-04.06.04", "PMO-04.06.05",
            "PMO-04.07.01", "PMO-04.07.02",
            "PMO-04.08.01", "PMO-04.08.02", "PMO-04.08.03", "PMO-04.08.04", "PMO-04.08.05", "PMO-04.08.06", "PMO-04.08.07",
            "PMO-04.09.01", "PMO-04.09.02", "PMO-04.09.03", "PMO-04.09.04", "PMO-04.09.05",
            "PMO-04.10.01", "PMO-04.10.02",
            "PMO-04.11.01", "PMO-04.11.02",
            "PMO-04.12.01",
            "PMO-04.13.01",
            "PMO-05.01", "PMO-05.02", "PMO-05.03", "PMO-05.04", "PMO-05.05", "PMO-05.06", "PMO-05.07", "PMO-05.11", "PMO-05.12", "PMO-05.13", "PMO-05.15",
            "PMO-06.01", "PMO-06.02", "PMO-06.03", "PMO-06.04", "PMO-06.05", "PMO-06.06", "PMO-06.07", "PMO-06.08", "PMO-06.09", "PMO-06.10", "PMO-06.11", "PMO-06.13", "PMO-06.14", "PMO-06.15", "PMO-06.16",
            "PMO-07.01", "PMO-07.02", "PMO-07.03", "PMO-07.04", "PMO-07.05", "PMO-07.06", "PMO-07.07"
        ],
        "agile": [
            "PMO-01.01", "PMO-01.02", "PMO-01.03",
            "PMO-02.01",
            "PMO-03.01", "PMO-03.02", "PMO-03.04",
            "PMO-04.01.01", "PMO-04.01.03",
            "PMO-04.02.01", "PMO-04.02.03", "PMO-04.02.08", "PMO-04.02.09",
            "PMO-04.03.01", "PMO-04.03.09", "PMO-04.03.10",
            "PMO-04.05.01", "PMO-04.05.03",
            "PMO-04.06.04", "PMO-04.06.05", "PMO-04.06.06",
            "PMO-04.07.01",
            "PMO-04.08.02",
            "PMO-04.13.01",
            "PMO-05.01", "PMO-05.02", "PMO-05.04", "PMO-05.07", "PMO-05.08", "PMO-05.10", "PMO-05.11", "PMO-05.14",
            "PMO-06.01", "PMO-06.08", "PMO-06.10", "PMO-06.11", "PMO-06.12", "PMO-06.15", "PMO-06.16",
            "PMO-07.01", "PMO-07.03", "PMO-07.04", "PMO-07.06"
        ],
        "ai": [
            "PMO-01.01", "PMO-01.03", "PMO-01.04",
            "PMO-02.01", "PMO-02.02", "PMO-02.03", "PMO-02.04", "PMO-02.05", "PMO-02.06",
            "PMO-03.01", "PMO-03.02", "PMO-03.04",
            "PMO-04.01.01", "PMO-04.01.03",
            "PMO-04.02.01", "PMO-04.02.03", "PMO-04.02.08",
            "PMO-04.03.01", "PMO-04.03.09",
            "PMO-04.04.01",
            "PMO-04.05.01", "PMO-04.05.02",
            "PMO-04.06.01", "PMO-04.06.04",
            "PMO-04.08.01", "PMO-04.08.02", "PMO-04.08.06",
            "PMO-04.13.01",
            "PMO-05.01", "PMO-05.02", "PMO-05.07", "PMO-05.09", "PMO-05.15",
            "PMO-06.01", "PMO-06.08", "PMO-06.10", "PMO-06.11", "PMO-06.12", "PMO-06.15", "PMO-06.16",
            "PMO-07.01", "PMO-07.03", "PMO-07.04", "PMO-07.06"
        ],
        "hybrid": [
            "PMO-00.01", "PMO-01.01", "PMO-01.02", "PMO-02.01",
            "PMO-03.01", "PMO-03.02", "PMO-03.04",
            "PMO-04.01.01", "PMO-04.01.03",
            "PMO-04.02.01", "PMO-04.02.03", "PMO-04.02.05", "PMO-04.02.06", "PMO-04.02.08",
            "PMO-04.03.01", "PMO-04.03.04", "PMO-04.03.08", "PMO-04.03.09", "PMO-04.03.10",
            "PMO-04.04.01", "PMO-04.04.04",
            "PMO-04.05.01", "PMO-04.05.03",
            "PMO-04.06.01", "PMO-04.06.04", "PMO-04.06.05",
            "PMO-04.07.01", "PMO-04.07.02",
            "PMO-04.08.01", "PMO-04.08.02", "PMO-04.08.06",
            "PMO-04.09.01", "PMO-04.09.04",
            "PMO-04.10.01",
            "PMO-04.13.01",
            "PMO-05.01", "PMO-05.02", "PMO-05.03", "PMO-05.04", "PMO-05.07", "PMO-05.08", "PMO-05.10", "PMO-05.11",
            "PMO-06.01", "PMO-06.05", "PMO-06.08", "PMO-06.11", "PMO-06.12", "PMO-06.13", "PMO-06.15",
            "PMO-07.01", "PMO-07.03", "PMO-07.04"
        ]
    },
    "2": {
        "name": "Standard (Tier 2)",
        "general": [
            "PMO-01.01", "PMO-02.01", "PMO-03.01", "PMO-03.03", "PMO-03.04",
            "PMO-04.01.01", "PMO-04.02.01", "PMO-04.02.05", "PMO-04.02.06",
            "PMO-04.03.01", "PMO-04.03.04", "PMO-04.03.08",
            "PMO-04.04.01", "PMO-04.04.04",
            "PMO-04.05.01", "PMO-04.06.01", "PMO-04.06.04", "PMO-04.07.01", "PMO-04.07.02",
            "PMO-04.08.01", "PMO-04.08.02", "PMO-04.09.01", "PMO-04.10.01", "PMO-04.13.01",
            "PMO-05.01", "PMO-05.02", "PMO-05.03", "PMO-05.04", "PMO-05.07", "PMO-05.11",
            "PMO-06.01", "PMO-06.04", "PMO-06.05", "PMO-06.11", "PMO-06.13",
            "PMO-07.01", "PMO-07.03", "PMO-07.04"
        ],
        "agile": [
            "PMO-01.01", "PMO-03.01", "PMO-03.02", "PMO-03.04",
            "PMO-04.01.01", "PMO-04.02.01", "PMO-04.02.08", "PMO-04.03.01", "PMO-04.03.09", "PMO-04.03.10",
            "PMO-04.05.03", "PMO-04.06.04", "PMO-04.06.05", "PMO-04.08.02",
            "PMO-05.01", "PMO-05.02", "PMO-05.04", "PMO-05.08", "PMO-05.10", "PMO-05.14",
            "PMO-06.01", "PMO-06.08", "PMO-06.11", "PMO-06.12", "PMO-06.15",
            "PMO-07.01", "PMO-07.03"
        ],
        "ai": [
            "PMO-01.01", "PMO-02.01", "PMO-02.02", "PMO-02.03", "PMO-02.04", "PMO-02.05", "PMO-02.06",
            "PMO-03.01", "PMO-04.01.01", "PMO-04.02.08", "PMO-04.08.02", "PMO-04.13.01",
            "PMO-05.01", "PMO-05.02", "PMO-05.09", "PMO-05.15",
            "PMO-06.01", "PMO-06.10", "PMO-06.11", "PMO-06.15",
            "PMO-07.01", "PMO-07.03"
        ],
        "predictive": [
            "PMO-01.01", "PMO-02.01", "PMO-03.01", "PMO-03.03", "PMO-03.04",
            "PMO-04.01.01", "PMO-04.02.01", "PMO-04.02.05", "PMO-04.02.06",
            "PMO-04.03.01", "PMO-04.03.04", "PMO-04.03.08", "PMO-04.04.01", "PMO-04.04.04",
            "PMO-04.05.01", "PMO-04.06.01", "PMO-04.06.04", "PMO-04.07.01", "PMO-04.08.01", "PMO-04.08.02",
            "PMO-04.09.01", "PMO-04.10.01", "PMO-04.13.01",
            "PMO-05.01", "PMO-05.02", "PMO-05.03", "PMO-05.04", "PMO-05.07",
            "PMO-06.01", "PMO-06.04", "PMO-06.05", "PMO-06.11",
            "PMO-07.01", "PMO-07.03", "PMO-07.04"
        ],
        "hybrid": [
            "PMO-01.01", "PMO-03.01", "PMO-03.02", "PMO-04.01.01",
            "PMO-04.02.01", "PMO-04.02.05", "PMO-04.02.08",
            "PMO-04.03.01", "PMO-04.03.04", "PMO-04.03.08", "PMO-04.03.10",
            "PMO-04.04.01", "PMO-04.05.01", "PMO-04.06.04", "PMO-04.08.02",
            "PMO-05.01", "PMO-05.02", "PMO-05.04", "PMO-05.08", "PMO-05.10",
            "PMO-06.01", "PMO-06.11", "PMO-06.12", "PMO-06.15",
            "PMO-07.01", "PMO-07.03"
        ]
    },
    "3": {
        "name": "Lean / Fast-Track (Tier 3)",
        "general": [
            "PMO-01.01", "PMO-03.01", "PMO-04.02.05", "PMO-04.03.04", "PMO-04.08.02",
            "PMO-05.01", "PMO-05.02", "PMO-06.01", "PMO-07.01", "PMO-07.03"
        ],
        "agile": [
            "PMO-03.01", "PMO-03.02", "PMO-04.02.08", "PMO-04.05.03", "PMO-04.08.02",
            "PMO-05.01", "PMO-05.08", "PMO-05.10", "PMO-06.01", "PMO-06.12", "PMO-07.01"
        ],
        "ai": [
            "PMO-02.03", "PMO-02.04", "PMO-02.05", "PMO-03.01",
            "PMO-04.08.02", "PMO-05.01", "PMO-05.09", "PMO-06.01", "PMO-07.01"
        ],
        "predictive": [
            "PMO-01.01", "PMO-03.01", "PMO-04.02.05", "PMO-04.03.04", "PMO-04.04.04",
            "PMO-04.08.02", "PMO-05.01", "PMO-05.03", "PMO-06.01", "PMO-07.03"
        ],
        "hybrid": [
            "PMO-03.01", "PMO-04.02.05", "PMO-04.02.08", "PMO-04.03.04", "PMO-04.08.02",
            "PMO-05.01", "PMO-05.10", "PMO-06.01", "PMO-06.12", "PMO-07.01"
        ]
    }
}

def load_lexicon():
    lex_file = ROOT / "docs" / "LEXICON.json"
    if lex_file.exists():
        with open(lex_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def find_form_files(lang="en"):
    """Index all available forms by form prefix ID."""
    base_dir = FORMS_DIR / lang
    forms_map = {}
    if not base_dir.exists():
        return forms_map
    pattern = "*_Template.md" if lang == "en" else "*_قالب.md"
    for p in base_dir.rglob(pattern):
        filename = p.name
        prefix_match = re.match(r"^(\d{2}(?:_\d{2})+)", filename)
        if prefix_match:
            prefix = prefix_match.group(1)
            forms_map[prefix] = p.parent
    return forms_map

def scaffold_project(args):
    print(f"\n{Colors.HEADER}{Colors.BOLD}===================================================={Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}   🚀 Tasleemat Project Workspace Scaffolder        {Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}===================================================={Colors.ENDC}\n")

    code = args.code or input("Enter Project Code [e.g. PRJ-2026-001]: ").strip() or "PRJ-2026-001"
    name = args.name or input("Enter Project Name: ").strip() or "New Strategic Initiative"
    pm = args.pm or input("Enter Project Manager Name: ").strip() or "Lead PM"
    sponsor = args.sponsor or input("Enter Project Sponsor Name: ").strip() or "Executive Sponsor"

    tier = args.tier
    if not tier:
        print("\nSelect Governance Tier:")
        print("  1) Enterprise / Strategic (35–50 deliverables)")
        print("  2) Standard Enterprise (18–25 deliverables)")
        print("  3) Fast-Track / Lean (7–9 deliverables)")
        choice = input("Choice [1-3, default=2]: ").strip()
        tier = choice if choice in ["1", "2", "3"] else "2"

    pack = args.pack
    if not pack:
        print("\nSelect Methodology Pack:")
        print("  1) General / PMBOK")
        print("  2) Agile / Scrum")
        print("  3) AI Governance & Engineering")
        print("  4) Predictive / Waterfall")
        print("  5) Hybrid")
        p_choice = input("Choice [1-5, default=1]: ").strip()
        pack_map = {"1": "general", "2": "agile", "3": "ai", "4": "predictive", "5": "hybrid"}
        pack = pack_map.get(p_choice, "general")

    lang = args.lang
    if not lang:
        print("\nSelect Deliverable Language:")
        print("  1) Both (English & Arabic)")
        print("  2) Arabic Only")
        print("  3) English Only")
        l_choice = input("Choice [1-3, default=1]: ").strip()
        lang_map = {"1": "both", "2": "ar", "3": "en"}
        lang = lang_map.get(l_choice, "both")

    out = args.out or input(f"Enter Output Directory [default=./{code}_Workspace]: ").strip() or f"./{code}_Workspace"
    out_dir = pathlib.Path(out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    selected_ids = TIER_PACKS.get(tier, {}).get(pack, TIER_PACKS["2"]["general"])
    date_str = datetime.date.today().isoformat()

    print(f"\n{Colors.OKBLUE}Scaffolding workspace for '{name}' ({code})...{Colors.ENDC}")
    print(f"Tier: {Colors.BOLD}{TIER_PACKS[tier]['name']}{Colors.ENDC} | Pack: {Colors.BOLD}{pack.upper()}{Colors.ENDC} | Language: {Colors.BOLD}{lang.upper()}{Colors.ENDC}\n")

    target_langs = ["en", "ar"] if lang == "both" else [lang]
    scaffolded_count = 0

    for l in target_langs:
        lang_dir = out_dir / l
        lang_dir.mkdir(parents=True, exist_ok=True)
        forms_map = find_form_files(l)

        for item_id in selected_ids:
            # Match item_id like PMO-03.01 or PMO-04.08.02
            clean_id = item_id.replace("PMO-", "").replace(".", "_")
            
            matched_folder = forms_map.get(clean_id)
            
            if matched_folder and matched_folder.exists():
                dest_folder = lang_dir / matched_folder.relative_to(FORMS_DIR / l)
                dest_folder.mkdir(parents=True, exist_ok=True)

                for item in matched_folder.iterdir():
                    if item.is_file():
                        content = item.read_text(encoding="utf-8")
                        content = content.replace("{{اسم_المشروع}}", name).replace("{{Project_Name}}", name)
                        content = content.replace("{{معرف_المشروع}}", code).replace("{{Project_ID}}", code).replace("{{Project_Code}}", code)
                        content = content.replace("{{اسم_مدير_المشروع}}", pm).replace("{{Project_Manager}}", pm)
                        content = content.replace("{{اسم_راعي_المشروع}}", sponsor).replace("{{Sponsor_Name}}", sponsor)
                        content = content.replace("{{التاريخ_الحالي}}", date_str).replace("{{Current_Date}}", date_str)
                        content = content.replace("{{اسم_الشركة}}", "حلول القمة المؤسسية (Apex Solutions)").replace("{{Company_Name}}", "Apex Enterprise Solutions")
                        
                        import hashlib
                        content_for_hash = content.replace("{{رمز_تجزئة_التدقيق_SHA256}}", "").replace("{{Audit_Trail_SHA256_Hash}}", "")
                        audit_hash = hashlib.sha256(content_for_hash.encode("utf-8")).hexdigest()
                        content = content.replace("{{رمز_تجزئة_التدقيق_SHA256}}", audit_hash).replace("{{Audit_Trail_SHA256_Hash}}", audit_hash)
                        
                        content = re.sub(r'(\*\*اسم المشروع:\*\*|\*\*Project Name:\*\*)\s*\[.*?\]', rf'\1 {name}', content)
                        content = re.sub(r'(\*\*رمز المشروع:\*\*|\*\*Project ID:\*\*|\*\*Project Code:\*\*)\s*\[.*?\]', rf'\1 {code}', content)
                        content = re.sub(r'(\*\*مدير المشروع:\*\*|\*\*Project Manager:\*\*)\s*\[.*?\]', rf'\1 {pm}', content)
                        content = re.sub(r'(\*\*راعي المشروع:\*\*|\*\*Project Sponsor:\*\*)\s*\[.*?\]', rf'\1 {sponsor}', content)
                        content = re.sub(r'(\*\*تاريخ الوثيقة:\*\*|\*\*Date:\*\*)\s*\[.*?\]', rf'\1 {date_str}', content)
                        
                        (dest_folder / item.name).write_text(content, encoding="utf-8")
                scaffolded_count += 1

    readme_content = f"""# 📋 {name} (`{code}`) — Project Management Workspace
**Governance Tier:** Tier {tier} | **Methodology Pack:** {pack.upper()} | **Date:** {date_str}  
**Project Manager:** {pm} | **Project Sponsor:** {sponsor}  

---

## 🎯 Deliverables & Stage-Gate Checklist
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

def get_ai_client(provider=None, model=None, api_key=None):
    try:
        from tasleemat.ai import AIClient
        return AIClient(provider=provider, model=model, api_key=api_key)
    except ImportError:
        try:
            from tools.ai import AIClient
            return AIClient(provider=provider, model=model, api_key=api_key)
        except ImportError:
            sys.path.insert(0, str(ROOT))
            from tools.ai import AIClient
            return AIClient(provider=provider, model=model, api_key=api_key)

def configure_llm(args):
    """Configure default LLM provider, model, or API key."""
    try:
        from tasleemat.ai import load_config, save_config
    except ImportError:
        from tools.ai import load_config, save_config

    cfg = load_config()
    if args.action == "set":
        if args.provider:
            cfg["provider"] = args.provider
        if args.model:
            cfg["model"] = args.model
        if args.key:
            cfg["api_key"] = args.key
        if args.endpoint:
            cfg["endpoint"] = args.endpoint
        save_config(cfg)
        print(f"\n{Colors.OKGREEN}✅ Updated Tasleemat LLM configuration at ~/.tasleemat/config.json{Colors.ENDC}\n")
    else:
        print(f"\n{Colors.HEADER}{Colors.BOLD}--- Current Tasleemat LLM Configuration ---{Colors.ENDC}")
        print(f"Provider : {Colors.OKCYAN}{cfg.get('provider', 'gemini (default)')}{Colors.ENDC}")
        print(f"Model    : {Colors.OKCYAN}{cfg.get('model', 'gemini-2.5-flash (default)')}{Colors.ENDC}")
        print(f"Endpoint : {cfg.get('endpoint', 'N/A')}")
        key = cfg.get("api_key")
        masked = f"{key[:6]}...{key[-4:]}" if key and len(key) > 10 else ("Set" if key else "Not Set (Uses Env Var)")
        print(f"API Key  : {Colors.OKBLUE}{masked}{Colors.ENDC}\n")

def generate_artifact(args):
    """Generate or auto-fill a PMO artifact using LLM AI client."""
    client = get_ai_client(provider=args.provider, model=args.model, api_key=args.key)
    print(f"\n{Colors.HEADER}{Colors.BOLD}===================================================={Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}   🤖 Tasleemat AI Deliverable Generator           {Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}===================================================={Colors.ENDC}\n")
    print(f"{Colors.OKBLUE}Using Provider:{Colors.ENDC} {client.provider} (Model: {client.model})")

    context = ""
    if args.notes and os.path.exists(args.notes):
        with open(args.notes, "r", encoding="utf-8") as f:
            context = f.read()
    elif args.notes:
        context = args.notes

    lang = args.lang or "en"
    forms_map = find_form_files(lang)
    target_folder = None
    form_id = None
    
    clean_query = args.form.lower().replace("pmo-", "").replace(".", "_")
    for k, folder in forms_map.items():
        if clean_query in k.lower() or clean_query in folder.name.lower() or args.form.lower() in folder.name.lower():
            target_folder = folder
            form_id = k
            break

    if not target_folder:
        print(f"{Colors.FAIL}❌ Form or template matching '{args.form}' not found in {lang}!{Colors.ENDC}")
        sys.exit(1)

    template_file = target_folder / f"{form_id}_Template.md"
    if not template_file.exists():
        template_file = target_folder / f"{form_id}_قالب.md"

    if not template_file.exists():
        md_files = list(target_folder.glob("*.md"))
        if md_files:
            template_file = md_files[0]

    if not template_file or not template_file.exists():
        print(f"{Colors.FAIL}❌ Template file for '{form_id}' not found!{Colors.ENDC}")
        sys.exit(1)

    template_content = template_file.read_text(encoding="utf-8")
    system_instruction = "You are an expert PMO Lead & Governance Specialist. Auto-fill the project artifact template adhering strictly to field guidance."
    full_prompt = f"PROJECT CONTEXT & MEETING NOTES:\n{context}\n\nARTIFACT TEMPLATE TO AUTO-FILL:\n{template_content}"

    print(f"{Colors.OKBLUE}Generating deliverable via {client.provider}...{Colors.ENDC}")
    output = client.generate(full_prompt, system_instruction=system_instruction, mock=args.mock)

    if args.out:
        out_path = pathlib.Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
        print(f"\n{Colors.OKGREEN}✅ Successfully generated artifact saved to: {out_path}{Colors.ENDC}\n")
    else:
        print(f"\n{Colors.OKGREEN}--- Generated Output ---{Colors.ENDC}\n")
        print(output)

def render_progress_bar(pct: float, width: int = 24) -> str:
    """Render a visual terminal progress bar."""
    filled = int(round(width * (pct / 100.0)))
    empty = width - filled
    bar = "█" * filled + "░" * empty
    color = Colors.OKGREEN if pct >= 80 else (Colors.WARNING if pct >= 50 else Colors.FAIL)
    return f"{color}[{bar}] {pct:5.1f}%{Colors.ENDC}"

def audit_project_cli(args):
    """Execute project governance audit and display KPIs, progress bars, and verification checks."""
    from tasleemat.audit import audit_project

    target_path = pathlib.Path(args.path or pathlib.Path.cwd()).resolve()
    if not getattr(args, "json", False):
        print(f"\n{Colors.HEADER}{Colors.BOLD}================================================================================{Colors.ENDC}")
        print(f"{Colors.HEADER}{Colors.BOLD}   🛡️  Tasleemat PMO Project Governance Audit & Structural Verification          {Colors.ENDC}")
        print(f"{Colors.HEADER}{Colors.BOLD}================================================================================{Colors.ENDC}\n")
        print(f"Auditing workspace: {Colors.OKBLUE}{target_path}{Colors.ENDC}\n")

    try:
        report = audit_project(
            project_path=target_path,
            tier=getattr(args, "tier", None),
            pack=getattr(args, "pack", None),
            strict_schema=not getattr(args, "no_schema", False),
        )
    except Exception as e:
        print(f"{Colors.FAIL}❌ Audit failed to execute: {e}{Colors.ENDC}\n")
        sys.exit(1)

    if getattr(args, "json", False):
        report_json = json.dumps(report.to_dict(), indent=2, ensure_ascii=False)
        if getattr(args, "out", None):
            out_file = pathlib.Path(args.out)
            out_file.write_text(report_json, encoding="utf-8")
            print(f"{Colors.OKGREEN}✅ Audit report exported to: {out_file}{Colors.ENDC}\n")
        else:
            print(report_json)
        sys.exit(0 if report.is_compliant else 1)

    # Display Project Metadata
    print(f"{Colors.BOLD}Project Name:{Colors.ENDC}    {report.project_name}")
    print(f"{Colors.BOLD}Project Code:{Colors.ENDC}    {report.project_code}")
    print(f"{Colors.BOLD}Governance Tier:{Colors.ENDC} Tier {report.tier}")
    print(f"{Colors.BOLD}Methodology:{Colors.ENDC}     {report.pack.upper()}")
    print(f"{Colors.BOLD}Languages:{Colors.ENDC}       {', '.join(report.detected_langs).upper()}")
    if report.agent_integrations_found:
        print(f"{Colors.BOLD}Agent Integrations:{Colors.ENDC} {', '.join(report.agent_integrations_found)}")
    print()

    # Display High-Level KPIs & Progress Bars
    print(f"{Colors.BOLD}--- 📊 Governance KPIs & Progress Metrics ---{Colors.ENDC}")
    print(f"Overall Completion:    {render_progress_bar(report.overall_progress_pct)} ({report.total_present}/{report.total_required} Deliverables)")
    print(f"Governance Score:      {render_progress_bar(report.governance_score_pct)} ({report.total_valid}/{report.total_required} Fully Compliant)")
    print(f"Schema Integrity:      {render_progress_bar(report.schema_compliance_pct)} ({report.total_schema_errors} Schema Errors)")
    print()

    # Display Stage-Gate Readiness Matrix
    print(f"{Colors.BOLD}--- 🚪 Stage-Gate Readiness Matrix ---{Colors.ENDC}")
    print(f"{'Gate ID':<10} {'Stage Name':<42} {'Progress':<32} {'Status'}")
    print("-" * 92)
    for g in report.gate_readiness:
        status_color = Colors.OKGREEN if g.status == "PASS" else (Colors.WARNING if g.status == "WARN" else Colors.FAIL)
        bar = render_progress_bar(g.percentage, width=16)
        comp_str = f"({g.completed_count}/{g.required_count})"
        print(f"{g.gate_id:<10} {g.gate_name_en[:40]:<42} {bar} {comp_str:<8} {status_color}[{g.status}]{Colors.ENDC}")
    print("-" * 92)
    print()

    # Display Deliverable Findings Breakdown
    print(f"{Colors.BOLD}--- 📋 Deliverable Findings Details ---{Colors.ENDC}")
    for f in report.findings:
        if f.status == "valid":
            badge = f"{Colors.OKGREEN}✓ VALID{Colors.ENDC}"
        elif f.status == "incomplete":
            badge = f"{Colors.WARNING}⚠ INCOMPLETE{Colors.ENDC}"
        elif f.status == "schema_error":
            badge = f"{Colors.FAIL}✖ SCHEMA ERR{Colors.ENDC}"
        else:
            badge = f"{Colors.FAIL}✗ MISSING{Colors.ENDC}"

        files_info = f"({len(f.found_files)} files)" if f.found_files else "(no files)"
        print(f"[{badge}] {Colors.BOLD}{f.artifact_id:<14}{Colors.ENDC} {f.name_en[:38]:<40} {files_info}")
        if f.messages:
            for m in f.messages:
                print(f"         ↳ {Colors.WARNING}{m}{Colors.ENDC}")

    print()
    if report.is_compliant:
        print(f"{Colors.OKGREEN}{Colors.BOLD}✅ AUDIT PASSED: Workspace is 100% compliant with Tier {report.tier} ({report.pack.upper()}) governance standards!{Colors.ENDC}\n")
        sys.exit(0)
    else:
        print(f"{Colors.WARNING}{Colors.BOLD}⚠️  AUDIT NOTICE: {report.total_missing} missing deliverables, {report.total_schema_errors} schema errors.{Colors.ENDC}")
        print(f"To remediate, use {Colors.OKBLUE}tasleemat generate{Colors.ENDC} or the interactive {Colors.OKBLUE}tasleemat tui{Colors.ENDC} workstation.\n")
        sys.exit(0 if not getattr(args, "strict", False) else 1)

def run_tests(args):
    """Execute the comprehensive automated test suite."""
    import unittest
    print(f"\n{Colors.HEADER}{Colors.BOLD}===================================================={Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}   🧪 Running Tasleemat Automated Test Suite       {Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}===================================================={Colors.ENDC}\n")
    tests_dir = ROOT / "tests"
    if not tests_dir.exists():
        tests_dir = pathlib.Path.cwd() / "tests"
    if not tests_dir.exists():
        print(f"{Colors.WARNING}⚠️ Test directory not found in the installed distribution package.{Colors.ENDC}")
        print("To run the full developer test suite, clone the Tasleemat repository from GitHub.")
        sys.exit(0)
    loader = unittest.TestLoader()
    suite = loader.discover(str(tests_dir), pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2 if args.verbose else 1)
    result = runner.run(suite)
    if result.wasSuccessful():
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}✅ All Tasleemat tests passed successfully!{Colors.ENDC}\n")
        sys.exit(0)
    else:
        print(f"\n{Colors.FAIL}{Colors.BOLD}❌ Test failures detected!{Colors.ENDC}\n")
        sys.exit(1)

def print_comprehensive_help(target_cmd=None):
    """Print complete, comprehensive CLI help listing all commands, flags, arguments, choices, and examples."""
    header = f"{Colors.HEADER}{Colors.BOLD}================================================================================{Colors.ENDC}\n"
    header += f"{Colors.HEADER}{Colors.BOLD}   🚀 Tasleemat PMO Operating System CLI — Complete Help & Parameter Reference   {Colors.ENDC}\n"
    header += f"{Colors.HEADER}{Colors.BOLD}================================================================================{Colors.ENDC}\n"

    usage = f"{Colors.BOLD}USAGE:{Colors.ENDC}\n"
    usage += f"  {Colors.OKBLUE}tasleemat{Colors.ENDC} <command> [options] [arguments]\n"
    usage += f"  {Colors.OKBLUE}tasleemat{Colors.ENDC} --help | -h | help [subcommand]\n\n"

    cmds = {
        "init": {
            "title": "init — Scaffold a new tailored project workspace",
            "desc": "Interactively or via flags, builds a complete project folder populated with 5-file deliverable bundles.",
            "args": [
                ("-n, --name TEXT", "Project name (e.g., 'Enterprise Cloud Migration')"),
                ("-c, --code TEXT", "Project ID code (e.g., 'PRJ-2026-001')"),
                ("--pm TEXT", "Project Manager name"),
                ("--sponsor TEXT", "Executive Sponsor name"),
                ("-t, --tier {1,2,3}", "Governance Tier: 1=Enterprise (35–50 deliverables), 2=Standard (18–25 deliverables), 3=Lean (7–9 deliverables)"),
                ("-p, --pack {general,agile,ai,predictive,hybrid}", "Methodology Pack (Default: general)"),
                ("-l, --lang {ar,en,both}", "Deliverable language selection (Default: both)"),
                ("-o, --out PATH", "Target output directory (Default: ./<code_Workspace>)")
            ],
            "example": "tasleemat init --tier 2 --pack agile --lang ar --name 'منصة التحول الرقمي' --code 'PRJ-2026-01'"
        },
        "list": {
            "title": "list — List all available project management forms & templates",
            "desc": "Displays the complete catalog of 114 bilingual forms indexed by phase and form code.",
            "args": [
                ("-l, --lang {ar,en}", "Catalog language filter (Default: en)")
            ],
            "example": "tasleemat list --lang en"
        },
        "search": {
            "title": "search — Search deliverable templates by keyword or form ID",
            "desc": "Searches the bilingual catalog for matching form titles or PMO form codes.",
            "args": [
                ("query TEXT", "Search keyword or code (e.g., 'Risk', 'Charter', 'ميثاق', 'PMO-03.01')"),
                ("-l, --lang {ar,en}", "Search catalog language (Default: en)")
            ],
            "example": "tasleemat search 'Risk' --lang en"
        },
        "config": {
            "title": "config — Manage default LLM AI provider & API credentials",
            "desc": "Saves or displays LLM credentials at ~/.tasleemat/config.json for automated AI drafting.",
            "args": [
                ("action {set,show}", "Configuration action to perform (Default: show)"),
                ("--provider {gemini,openai,anthropic,openrouter,custom,ollama,mock}", "LLM AI Provider selection"),
                ("--model TEXT", "Model ID (e.g., 'gemini-2.5-flash', 'gpt-4o', 'anthropic/claude-3.5-sonnet', 'deepseek/deepseek-r1')"),
                ("--key TEXT", "API Key string"),
                ("--endpoint TEXT", "Custom Endpoint URL (e.g. https://openrouter.ai/api/v1 or http://localhost:11434)")
            ],
            "example": "tasleemat config set --provider openrouter --model anthropic/claude-3.5-sonnet --key 'YOUR_KEY'"
        },
        "generate": {
            "title": "generate — Auto-fill PMO artifact using LLM AI client",
            "desc": "Passes raw project notes and template prompt schemas to LLMs to auto-fill deliverables.",
            "args": [
                ("-f, --form TEXT", "Form ID or keyword [REQUIRED] (e.g., 'PMO-03.01' or 'Charter')"),
                ("-n, --notes TEXT/PATH", "Path to text file with meeting notes or direct prompt context string"),
                ("-l, --lang {ar,en}", "Deliverable output language (Default: en)"),
                ("-p, --provider {gemini,openai,anthropic,openrouter,custom,ollama,mock}", "Override default LLM Provider"),
                ("-m, --model TEXT", "Override default Model ID"),
                ("-k, --key TEXT", "Override default API Key"),
                ("-o, --out PATH", "Output Markdown file path"),
                ("--mock", "Run mock generation offline without calling API APIs")
            ],
            "example": "tasleemat generate --form PMO-03.01 --notes ./meeting_notes.txt --out ./Project_Charter.md"
        },
        "mcp": {
            "title": "mcp — Run Model Context Protocol server over stdio",
            "desc": "Runs the official MCP server exposing all 114 deliverables, schemas, and governance tools to AI agents.",
            "args": [],
            "example": "tasleemat mcp"
        },
        "tui": {
            "title": "tui — Launch interactive Bilingual Terminal User Interface (TUI)",
            "desc": "Launches the full-screen terminal workstation with Scaffolder Wizard, Catalog Explorer, Stage-Gates, Lexicon, and Agent Hub.",
            "args": [
                ("-l, --lang {ar,en}", "Default interface language (Default: en)")
            ],
            "example": "tasleemat tui --lang ar"
        },
        "audit": {
            "title": "audit — Audit and verify a project workspace against PMO governance tiers",
            "desc": "Inspects project deliverables, calculates governance KPIs, progress percentage, Stage-Gate readiness, and Draft 2020-12 schema validation.",
            "args": [
                ("path PATH", "Path to project directory (Default: current directory)"),
                ("-t, --tier {1,2,3}", "Override governance tier (Default: auto-detect from project)"),
                ("-p, --pack {general,agile,ai,predictive,hybrid}", "Override methodology pack (Default: auto-detect)"),
                ("--strict", "Exit with code 1 if any deliverable is missing or schema validation fails"),
                ("--no-schema", "Skip deep JSON schema verification"),
                ("--json", "Output audit report as structured JSON for CI/CD"),
                ("-o, --out PATH", "Save JSON audit report to target file")
            ],
            "example": "tasleemat audit ./projects/PRJ-01 --tier 2 --pack agile --strict"
        },
        "test": {
            "title": "test — Run complete automated test suite",
            "desc": "Executes 130+ unit & integration tests covering forms, schemas, data packages, CLI, and links.",
            "args": [
                ("-v, --verbose", "Enable verbose detailed test output")
            ],
            "example": "tasleemat test -v"
        },
        "help": {
            "title": "help — Display complete CLI help reference manual",
            "desc": "Shows help and argument documentation for all commands or a specific command.",
            "args": [
                ("subcommand TEXT", "Optional: Specific subcommand to view help for (e.g., init, generate)")
            ],
            "example": "tasleemat help init"
        }
    }

    if target_cmd and target_cmd in cmds:
        info = cmds[target_cmd]
        out = header + usage
        out += f"{Colors.BOLD}{info['title']}{Colors.ENDC}\n"
        out += f"  {Colors.OKCYAN}{info['desc']}{Colors.ENDC}\n\n"
        out += f"  {Colors.BOLD}Arguments & Options:{Colors.ENDC}\n"
        for opt, opt_desc in info["args"]:
            out += f"    {Colors.OKGREEN}{opt:<36}{Colors.ENDC} {opt_desc}\n"
        out += f"\n  {Colors.BOLD}Example:{Colors.ENDC}\n"
        out += f"    {Colors.OKBLUE}{info['example']}{Colors.ENDC}\n\n"
        print(out)
        return

    commands_detail = f"{Colors.BOLD}AVAILABLE COMMANDS & DETAILED ARGUMENTS:{Colors.ENDC}\n\n"
    body = ""
    for cmd_key, info in cmds.items():
        body += f"{Colors.BOLD}• {info['title']}{Colors.ENDC}\n"
        body += f"  {Colors.OKCYAN}{info['desc']}{Colors.ENDC}\n"
        body += f"  {Colors.BOLD}Arguments & Flags:{Colors.ENDC}\n"
        for opt, opt_desc in info["args"]:
            body += f"    {Colors.OKGREEN}{opt:<36}{Colors.ENDC} {opt_desc}\n"
        body += f"  {Colors.BOLD}Example:{Colors.ENDC} {Colors.OKBLUE}{info['example']}{Colors.ENDC}\n\n"

    print(header + usage + commands_detail + body)

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help", "help"]:
        subcmd = sys.argv[2] if len(sys.argv) > 2 else None
        print_comprehensive_help(subcmd)
        sys.exit(0)

    parser = argparse.ArgumentParser(description="Tasleemat PMO Operating System CLI & AI Generator", add_help=False)
    parser.add_argument("-h", "--help", action="store_true", help="Show complete help manual for all commands")
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

    # config command
    config_parser = subparsers.add_parser("config", help="Manage default LLM provider & credentials")
    config_parser.add_argument("action", choices=["set", "list", "show"], default="show", nargs="?", help="Action: set or show")
    config_parser.add_argument("--provider", choices=["gemini", "openai", "anthropic", "openrouter", "custom", "ollama", "mock"], help="LLM Provider")
    config_parser.add_argument("--model", help="Model ID (e.g. gemini-2.5-flash, gpt-4o, anthropic/claude-3.5-sonnet, deepseek/deepseek-r1)")
    config_parser.add_argument("--key", help="API Key")
    config_parser.add_argument("--endpoint", help="Custom Endpoint URL")

    # generate command
    gen_parser = subparsers.add_parser("generate", help="Auto-fill PMO artifact using LLM AI account")
    gen_parser.add_argument("-f", "--form", required=True, help="Form ID or name (e.g. PMO-03.01 or Charter)")
    gen_parser.add_argument("-n", "--notes", help="Path to project meeting notes / context text")
    gen_parser.add_argument("-l", "--lang", choices=["ar", "en"], default="en", help="Deliverable language")
    gen_parser.add_argument("-p", "--provider", choices=["gemini", "openai", "anthropic", "openrouter", "custom", "ollama", "mock"], help="Override LLM Provider")
    gen_parser.add_argument("-m", "--model", help="Override Model ID")
    gen_parser.add_argument("-k", "--key", help="Override API Key")
    gen_parser.add_argument("-o", "--out", help="Output file path")
    gen_parser.add_argument("--mock", action="store_true", help="Run mock generation without spending API tokens")

    # test command
    test_parser = subparsers.add_parser("test", help="Run automated test suite")
    test_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose test output")

    # mcp command
    mcp_parser = subparsers.add_parser("mcp", help="Start Model Context Protocol (MCP) server over stdio")

    # tui / ui command
    tui_parser = subparsers.add_parser("tui", help="Launch interactive Bilingual Terminal User Interface (TUI)")
    tui_parser.add_argument("-l", "--lang", choices=["ar", "en"], default="en", help="Default interface language (Default: en)")

    ui_parser = subparsers.add_parser("ui", help="Alias for tui")
    ui_parser.add_argument("-l", "--lang", choices=["ar", "en"], default="en", help="Default interface language (Default: en)")

    # audit command
    audit_parser = subparsers.add_parser("audit", help="Audit and verify a project workspace against PMO governance tiers")
    audit_parser.add_argument("path", nargs="?", default=".", help="Path to project workspace (Default: current directory)")
    audit_parser.add_argument("-t", "--tier", choices=["1", "2", "3"], help="Override governance tier (Default: auto-detect)")
    audit_parser.add_argument("-p", "--pack", choices=["general", "agile", "ai", "predictive", "hybrid"], help="Override methodology pack (Default: auto-detect)")
    audit_parser.add_argument("--strict", action="store_true", help="Exit with code 1 if any deliverable is missing or schema fails")
    audit_parser.add_argument("--no-schema", action="store_true", help="Skip deep Draft 2020-12 schema validation on JSON payloads")
    audit_parser.add_argument("--json", action="store_true", help="Output audit report as structured JSON")
    audit_parser.add_argument("-o", "--out", help="Save JSON report to file")

    # help command
    help_parser = subparsers.add_parser("help", help="Display complete CLI help manual")
    help_parser.add_argument("subcommand", nargs="?", help="Optional subcommand for specific help")

    args = parser.parse_args()
    if args.help or args.command == "help":
        target = getattr(args, "subcommand", None)
        print_comprehensive_help(target)
    elif args.command == "init":
        scaffold_project(args)
    elif args.command == "list":
        list_forms(args)
    elif args.command == "search":
        search_forms(args)
    elif args.command == "config":
        configure_llm(args)
    elif args.command == "generate":
        generate_artifact(args)
    elif args.command == "test":
        run_tests(args)
    elif args.command == "audit":
        audit_project_cli(args)
    elif args.command == "mcp":
        from tasleemat.mcp.server import main as mcp_main
        sys.exit(mcp_main())
    elif args.command in ["tui", "ui"]:
        try:
            from tasleemat.tui import launch_tui
            launch_tui(lang=getattr(args, "lang", "en"))
        except ImportError:
            sys.path.insert(0, str(ROOT))
            from tasleemat.tui import launch_tui
            launch_tui(lang=getattr(args, "lang", "en"))
    else:
        print_comprehensive_help()

if __name__ == "__main__":
    main()

