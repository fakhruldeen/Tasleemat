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
        "name": "Enterprise (Tier 1)",
        "general": ["PMO-00.01", "PMO-00.02", "PMO-00.03", "PMO-00.04", "PMO-00.05", "PMO-00.06",
                    "PMO-01.01", "PMO-01.02", "PMO-01.03", "PMO-01.04", "PMO-02.01", "PMO-02.02",
                    "PMO-03.01", "PMO-03.02", "PMO-03.03", "PMO-03.04", "PMO-03.05",
                    "PMO-04.01.01", "PMO-04.01.02", "PMO-04.02.01", "PMO-04.02.02", "PMO-04.03.01",
                    "PMO-04.03.02", "PMO-04.04.01", "PMO-04.04.02", "PMO-04.05.01", "PMO-04.06.01",
                    "PMO-04.07.01", "PMO-04.08.01", "PMO-04.08.02", "PMO-04.09.01", "PMO-04.10.01",
                    "PMO-04.11.01", "PMO-04.12.01", "PMO-05.01", "PMO-05.02", "PMO-05.03", "PMO-05.04",
                    "PMO-06.01", "PMO-06.02", "PMO-06.03", "PMO-06.04", "PMO-06.05", "PMO-06.11",
                    "PMO-07.01", "PMO-07.02", "PMO-07.03", "PMO-07.04", "PMO-07.05"],
        "agile": ["PMO-01.01", "PMO-02.01", "PMO-03.01", "PMO-03.02", "PMO-04.02.01", "PMO-04.03.01",
                  "PMO-04.08.02", "PMO-05.01", "PMO-05.04", "PMO-05.10", "PMO-06.01", "PMO-06.12", "PMO-07.01"],
        "ai": ["PMO-01.01", "PMO-02.01", "PMO-02.02", "PMO-02.03", "PMO-02.04", "PMO-02.05", "PMO-02.06",
               "PMO-03.01", "PMO-04.01.01", "PMO-04.08.02", "PMO-05.01", "PMO-05.09", "PMO-06.01", "PMO-07.01"],
        "predictive": ["PMO-00.01", "PMO-01.01", "PMO-02.01", "PMO-03.01", "PMO-03.04", "PMO-04.01.01",
                       "PMO-04.02.01", "PMO-04.03.01", "PMO-04.04.01", "PMO-04.05.01", "PMO-04.08.02",
                       "PMO-05.01", "PMO-05.03", "PMO-06.01", "PMO-06.05", "PMO-07.03"],
        "hybrid": ["PMO-01.01", "PMO-02.01", "PMO-03.01", "PMO-03.04", "PMO-04.01.01", "PMO-04.02.01",
                   "PMO-04.03.01", "PMO-04.08.02", "PMO-05.01", "PMO-05.04", "PMO-05.10", "PMO-06.01",
                   "PMO-06.05", "PMO-06.12", "PMO-07.01", "PMO-07.03"]
    },
    "2": {
        "name": "Standard (Tier 2)",
        "general": ["PMO-01.01", "PMO-02.01", "PMO-03.01", "PMO-03.04", "PMO-04.01.01", "PMO-04.02.01",
                    "PMO-04.03.01", "PMO-04.04.01", "PMO-04.08.02", "PMO-05.01", "PMO-05.03",
                    "PMO-06.01", "PMO-07.01", "PMO-07.03"],
        "agile": ["PMO-01.01", "PMO-03.01", "PMO-03.02", "PMO-04.02.01", "PMO-04.08.02", "PMO-05.01",
                  "PMO-05.04", "PMO-05.10", "PMO-06.01", "PMO-06.12", "PMO-07.01"],
        "ai": ["PMO-01.01", "PMO-02.02", "PMO-02.03", "PMO-02.05", "PMO-03.01", "PMO-04.08.02",
               "PMO-05.01", "PMO-06.01", "PMO-07.01"],
        "predictive": ["PMO-01.01", "PMO-03.01", "PMO-04.01.01", "PMO-04.02.01", "PMO-04.03.01",
                       "PMO-04.04.01", "PMO-04.08.02", "PMO-05.01", "PMO-06.01", "PMO-07.03"],
        "hybrid": ["PMO-01.01", "PMO-03.01", "PMO-04.01.01", "PMO-04.02.01", "PMO-04.08.02",
                   "PMO-05.01", "PMO-05.10", "PMO-06.01", "PMO-06.12", "PMO-07.01"]
    },
    "3": {
        "name": "Lean / Fast-Track (Tier 3)",
        "general": ["PMO-01.01", "PMO-03.01", "PMO-04.08.02", "PMO-05.01", "PMO-06.01", "PMO-07.03"],
        "agile": ["PMO-03.01", "PMO-03.02", "PMO-04.02.01", "PMO-05.01", "PMO-05.10", "PMO-06.01", "PMO-07.01"],
        "ai": ["PMO-02.03", "PMO-02.05", "PMO-03.01", "PMO-05.01", "PMO-06.01"],
        "predictive": ["PMO-01.01", "PMO-03.01", "PMO-04.02.01", "PMO-04.08.02", "PMO-05.01", "PMO-06.01", "PMO-07.03"],
        "hybrid": ["PMO-03.01", "PMO-04.02.01", "PMO-04.08.02", "PMO-05.01", "PMO-06.01", "PMO-07.01"]
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
        print("  1) Enterprise (Full 52+ baselines)")
        print("  2) Standard (Balanced 14+ baselines)")
        print("  3) Fast-Track / Lean (Minimal 6+ baselines)")
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
            
            matched_folder = None
            for k, folder in forms_map.items():
                if k == clean_id or k.endswith(clean_id) or clean_id.endswith(k):
                    matched_folder = folder
                    break
            
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
        sys.path.insert(0, str(ROOT / "sdk" / "python"))
        from tasleemat.ai import AIClient
        return AIClient(provider=provider, model=model, api_key=api_key)

def configure_llm(args):
    """Configure default LLM provider, model, or API key."""
    try:
        from tasleemat.ai import load_config, save_config
    except ImportError:
        sys.path.insert(0, str(ROOT / "sdk" / "python"))
        from tasleemat.ai import load_config, save_config

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

def run_tests(args):
    """Execute the comprehensive automated test suite."""
    import unittest
    print(f"\n{Colors.HEADER}{Colors.BOLD}===================================================={Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}   🧪 Running Tasleemat Automated Test Suite       {Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}===================================================={Colors.ENDC}\n")
    loader = unittest.TestLoader()
    suite = loader.discover(str(ROOT / "tests"), pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2 if args.verbose else 1)
    result = runner.run(suite)
    if result.wasSuccessful():
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}✅ All Tasleemat tests passed successfully!{Colors.ENDC}\n")
        sys.exit(0)
    else:
        print(f"\n{Colors.FAIL}{Colors.BOLD}❌ Test failures detected!{Colors.ENDC}\n")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Tasleemat PMO Operating System CLI & AI Generator")
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
    config_parser.add_argument("--provider", choices=["gemini", "openai", "anthropic", "ollama", "mock"], help="LLM Provider")
    config_parser.add_argument("--model", help="Model ID (e.g. gemini-2.5-flash, gpt-4o)")
    config_parser.add_argument("--key", help="API Key")
    config_parser.add_argument("--endpoint", help="Custom Endpoint URL")

    # generate command
    gen_parser = subparsers.add_parser("generate", help="Auto-fill PMO artifact using LLM AI account")
    gen_parser.add_argument("-f", "--form", required=True, help="Form ID or name (e.g. PMO-03.01 or Charter)")
    gen_parser.add_argument("-n", "--notes", help="Path to project meeting notes / context text")
    gen_parser.add_argument("-l", "--lang", choices=["ar", "en"], default="en", help="Deliverable language")
    gen_parser.add_argument("-p", "--provider", choices=["gemini", "openai", "anthropic", "ollama", "mock"], help="Override LLM Provider")
    gen_parser.add_argument("-m", "--model", help="Override Model ID")
    gen_parser.add_argument("-k", "--key", help="Override API Key")
    gen_parser.add_argument("-o", "--out", help="Output file path")
    gen_parser.add_argument("--mock", action="store_true", help="Run mock generation without spending API tokens")

    # test command
    test_parser = subparsers.add_parser("test", help="Run automated test suite")
    test_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose test output")

    args = parser.parse_args()
    if args.command == "init":
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
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
