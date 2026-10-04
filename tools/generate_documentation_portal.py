#!/usr/bin/env python3
"""tools/generate_documentation_portal.py
Generates the modern, enterprise-grade documentation portal for Tasleemat.
Features:
- Streamlined 3-tab top navigation (English Portal, Arabic Portal, Lexicon)
- Universal 1-click bilingual cross-linking on every single page
- Glassmorphic Hero Banners with live counters, badges, and responsive action chips
- Interactive Deliverables Explorer (Search, Phase & Tier filters, Grid/Table views)
- Comprehensive Phase Hub cards and Document Control headers
- Complete 404 prevention with use_directory_urls: false and exact HTML cross-linking
"""

import os
import re
import sys
import yaml
import json
import shutil
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
FORMS_EN = ROOT / "forms" / "en"
FORMS_AR = ROOT / "forms" / "ar"
EXAMPLES_EN = ROOT / "examples" / "en"
EXAMPLES_AR = ROOT / "examples" / "ar"

PHASE_META = {
    "00": {
        "en_title": "00. Program & Portfolio Management",
        "ar_title": "00. إدارة البرامج والمحافظ",
        "en_desc": "Strategic alignment, portfolio balancing, multi-project dependencies, and PMO maturity.",
        "ar_desc": "المواءمة الاستراتيجية، توازن المحفظة، إدارة الاعتماديات بين المشاريع، وتقييم نضج مكتب إدارة المشاريع.",
        "icon": "🏛️"
    },
    "01": {
        "en_title": "01. Business & Value Delivery",
        "ar_title": "01. الأعمال وتسليم القيمة",
        "en_desc": "Business justification, benefit realization planning, value tracking, and gap analysis.",
        "ar_desc": "دراسات الجدوى الاقتصادية، خطط إدارة المنافع، سجلات تحقيق القيمة، وتحليل الفجوات.",
        "icon": "💎"
    },
    "02": {
        "en_title": "02. Project Approach & Tailoring",
        "ar_title": "02. منهجية المشروع وتخصيصه",
        "en_desc": "Tailoring strategy, governance tiers, AI ethics, model cards, and agile/hybrid adoption.",
        "ar_desc": "استراتيجية التخصيص، مستويات الحوكمة، أخلاقيات الذكاء الاصطناعي، وبطاقات النماذج.",
        "icon": "⚖️"
    },
    "03": {
        "en_title": "03. Initiating",
        "ar_title": "03. البدء",
        "en_desc": "Formal authorization, product vision, initial assumptions, and stakeholder identification.",
        "ar_desc": "الترخيص الرسمي للمشروع، رؤية المنتج، سجل الافتراضات الأولية، وتحديد المعنيين.",
        "icon": "🚀"
    },
    "04": {
        "en_title": "04. Planning",
        "ar_title": "04. التخطيط",
        "en_desc": "Comprehensive baselines across Scope, Schedule, Cost, Quality, Resources, Risk, and Procurement.",
        "ar_desc": "الخطوط المرجعية الشاملة للنطاق، الجدول الزمني، التكلفة، الجودة، الموارد، المخاطر، والمشتريات.",
        "icon": "📐"
    },
    "05": {
        "en_title": "05. Executing",
        "ar_title": "05. التنفيذ",
        "en_desc": "Directing work, managing issues, decision logs, change control, and team performance.",
        "ar_desc": "توجيه وإدارة أعمال المشروع، سجل القضايا، سجل القرارات، طلبات التغيير، وأداء الفريق.",
        "icon": "⚡"
    },
    "06": {
        "en_title": "06. Monitoring & Controlling",
        "ar_title": "06. المراقبة والتحكم",
        "en_desc": "Status reporting, Earned Value Analysis (EVA), variance tracking, and quality acceptance.",
        "ar_desc": "تقارير الأداء، تحليل القيمة المكتسبة (EVA)، مراقبة التباين، وضمان الجودة واختبارات القبول.",
        "icon": "📊"
    },
    "07": {
        "en_title": "07. Closing",
        "ar_title": "07. الإغلاق",
        "en_desc": "Formal transition to operations, contract closure, final lessons learned, and post-implementation review.",
        "ar_desc": "الانتقال الرسمي للعمليات التشغيلية، إغلاق العقود، خلاصة الدروس المستفادة، ومراجعة ما بعد التنفيذ.",
        "icon": "🏁"
    }
}

PLANNING_SUBS = {
    "01_Integration": ("01. Integration Management", "01. إدارة التكامل"),
    "02_Scope": ("02. Scope Management", "02. إدارة النطاق"),
    "03_Schedule": ("03. Schedule Management", "03. إدارة الجدول الزمني"),
    "04_Cost": ("04. Cost Management", "04. إدارة التكلفة"),
    "05_Quality": ("05. Quality Management", "05. إدارة الجودة"),
    "06_Resource": ("06. Resource Management", "06. إدارة الموارد"),
    "07_Communications": ("07. Communications Management", "07. إدارة التواصل"),
    "08_Risk": ("08. Risk Management", "08. إدارة المخاطر"),
    "09_Procurement": ("09. Procurement Management", "09. إدارة المشتريات"),
    "10_Stakeholder": ("10. Stakeholder Management", "10. إدارة المعنيين"),
    "11_Organizational_Change_Management": ("11. Organizational Change Management", "11. إدارة التغيير المؤسسي"),
    "12_Sustainability_and_ESG": ("12. Sustainability & ESG", "12. الاستدامة والمعايير البيئية والحوكمة")
}

TIER_MAP = {
    "00": "Tier 1 | Tier 2",
    "01": "Tier 1 | Tier 2",
    "02": "Tier 1 | Tier 2 | Tier 4",
    "03": "Tier 1 | Tier 2 | Tier 3",
    "04": "Tier 1 | Tier 2 | Tier 3",
    "05": "Tier 1 | Tier 2 | Tier 3",
    "06": "Tier 1 | Tier 2 | Tier 3",
    "07": "Tier 1 | Tier 2 | Tier 3"
}

def sanitize_content_links(content, current_doc_path, deliverable):
    """Sanitize all relative markdown links and ensure HTML block elements have markdown="1"."""
    is_ar = "/ar/" in str(current_doc_path) or "_قالب" in str(current_doc_path) or "_دليل" in str(current_doc_path) or "_مثال" in str(current_doc_path)
    pat = re.compile(r'\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(((?:[^()]+|\([^()]*\))+)\)')

    def replacer(match):
        text = match.group(1)
        url = match.group(2).strip()

        if url.startswith(("http://", "https://", "mailto:", "#")):
            return f"[{text}]({url})"

        clean_url = url.strip("<>").split('#')[0].split('?')[0].strip()

        # 1. Example links
        if "_Example.md" in clean_url or "_مثال.md" in clean_url:
            target = deliverable["doc_ex_ar"] if is_ar else deliverable["doc_ex_en"]
            return f"[{text}]({os.path.relpath(target, current_doc_path.parent)})"

        # 2. Template links
        if "_Template.md" in clean_url or "_قالب.md" in clean_url:
            target = deliverable["doc_tpl_ar"] if is_ar else deliverable["doc_tpl_en"]
            return f"[{text}]({os.path.relpath(target, current_doc_path.parent)})"

        # 3. Guide links
        if "_Guide.md" in clean_url or "_دليل.md" in clean_url:
            target = deliverable["doc_guide_ar"] if is_ar else deliverable["doc_guide_en"]
            return f"[{text}]({os.path.relpath(target, current_doc_path.parent)})"

        # 4. Sibling JSON Schema -> Link to GitHub Repository blob
        if clean_url.endswith(".json"):
            target_json = deliverable["json_ar"] if is_ar else deliverable["json_en"]
            if target_json and target_json.exists():
                gh_url = f"https://github.com/fakhruldeen/Tasleemat/blob/main/{target_json.relative_to(ROOT).as_posix()}"
                return f"[{text}]({gh_url})"

        # 5. Sibling CSV Data -> Link to GitHub Repository blob
        if clean_url.endswith(".csv"):
            target_csv = deliverable["csv_ar"] if is_ar else deliverable["csv_en"]
            if target_csv and target_csv.exists():
                gh_url = f"https://github.com/fakhruldeen/Tasleemat/blob/main/{target_csv.relative_to(ROOT).as_posix()}"
                return f"[{text}]({gh_url})"

        # 6. Sibling AI Prompt (e.g. 00_01_Portfolio_Roadmap.md) -> Link to GitHub Repository blob
        if clean_url.endswith(".md"):
            target_prompt = deliverable["prompt_ar"] if is_ar else deliverable["prompt_en"]
            if target_prompt and target_prompt.exists():
                gh_url = f"https://github.com/fakhruldeen/Tasleemat/blob/main/{target_prompt.relative_to(ROOT).as_posix()}"
                return f"[{text}]({gh_url})"

        return f"[{text}]({url})"

    content = pat.sub(replacer, content)

    # Enable Markdown parsing inside HTML <div> tags for md_in_html extension
    def add_markdown_attr(m):
        tag_attrs = m.group(1)
        if "markdown=" in tag_attrs:
            return m.group(0)
        return f'<div {tag_attrs} markdown="1">'

    content = re.sub(r'<div\s+([^>]+)>', add_markdown_attr, content)

    if not is_ar:
        content = align_tables_in_markdown(content)

    return content

def determine_col_alignment_en(col_name: str) -> str:
    clean = col_name.strip()
    clean = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', clean)
    clean = re.sub(r'[*_`]', '', clean).strip()
    low = clean.lower()

    if not low:
        return ':---'

    numeric_exact = {
        'budget', 'costs', 'cost', 'planned funding', 'price', 'npv', 'net present value', 
        'roi', 'rate', 'contingency amount', 'baseline value', 'target value', 
        'actual value', 'variance', 'gap', 'total available', 'allocated', 'remaining', 
        'committed load', 'available', 'required capacity', 'hours', 'story points', 
        'target score', 'actual score', 'weight', 'points', '%', 'amount', 'net value',
        'funding', 'planned capacity', 'estimate', 'estimated cost', 'actual cost',
        'cost variance', 'schedule variance', 'cpi', 'spi', 'ev', 'pv', 'ac', 'bac', 'eac', 'etc',
        'planned budget', 'actual budget', 'variance ($)', 'variance (%)', 'actual cost ($)',
        'estimated cost ($)', 'total cost', 'unit cost', 'hourly rate', 'daily rate'
    }
    if low in numeric_exact:
        return '---:'
    if any(low.endswith(sfx) for sfx in [' ($)', ' (%)', ' (hrs)', ' (hours)', ' (days)', ' (points)', ' (sar)', ' (usd)', ' (eur)', ' (gbp)']):
        return '---:'
    if any(k in low for k in ['budget', 'planned funding', 'net present value', 'contingency amount', 'total available', 'allocated', 'remaining', 'committed load']):
        return '---:'

    center_exact = {
        'id', 'doc id', 'change id', 'component id', 'benefit id', 'dependency id', 
        'req id', 'requirement id', 'risk id', 'issue id', 'action id', 'defect id',
        'item #', 'ref #', 'step #', 'no.', '#', 'code', 'guide #', 'template #', 'example #',
        'status', 'sprint status', 'sign-off status', 'status at closure', 'approval status',
        'priority', 'severity', 'rag', 'tier', 'level', 'phase', 'sprint', 'release', 
        'iteration', 'version', 'signature', 'by when', 'date', 'dates', 'start date', 
        'end date', 'target date', 'review date', 'agreed date', 'resolution date', 
        'realization date', 'handover date', 'date approved', 'date resolved', 'start', 'end',
        'period', 'frequency', 'criticality', 'probability', 'impact score', 'raci',
        'language', 'target sprint or release'
    }
    if low in center_exact:
        return ':---:'
    if low.endswith(' id') or low.startswith('id ') or low.endswith(' status') or low.endswith(' date') or low.startswith('date '):
        return ':---:'
    if low in ['start', 'end'] and ('start date' in low or 'end date' in low or low == 'start' or low == 'end'):
        return ':---:'

    return ':---'

def align_tables_in_markdown(text: str) -> str:
    lines = text.splitlines(keepends=True)
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        line_s = line.strip()
        
        if line_s.startswith('|') and ('---' in line_s) and i > 0:
            prev_line = lines[i-1].strip()
            if prev_line.startswith('|') and not ('---' in prev_line and prev_line.count('|') == line_s.count('|')):
                if '{{' in prev_line or 'Date Prepared:' in prev_line or 'تاريخ الإعداد:' in prev_line:
                    new_lines.append(line)
                    i += 1
                    continue
                
                header_cols = [c.strip() for c in prev_line.strip('|').split('|')]
                sep_cols = [c.strip() for c in line_s.strip('|').split('|')]
                
                if len(header_cols) == len(sep_cols) and len(header_cols) > 0:
                    new_alignments = [determine_col_alignment_en(col) for col in header_cols]
                    new_sep = '| ' + ' | '.join(new_alignments) + ' |\n'
                    indent = len(line) - len(line.lstrip())
                    new_lines.append(' ' * indent + new_sep)
                    i += 1
                    continue

        new_lines.append(line)
        i += 1
        
    return ''.join(new_lines)

def collect_deliverables():
    """Scan all 102 deliverable folders in forms/en and forms/ar and construct full mappings."""
    en_templates = sorted(list(FORMS_EN.rglob("*_Template.md")))
    ar_templates = sorted(list(FORMS_AR.rglob("*_قالب.md")))

    deliverables = []
    gh_base = "https://github.com/fakhruldeen/Tasleemat/blob/main"

    for t_en in en_templates:
        folder_en = t_en.parent
        rel_en = folder_en.relative_to(FORMS_EN)
        
        guides_en = list(folder_en.glob("*_Guide.md"))
        prompts_en = [p for p in folder_en.glob("*.md") if not p.name.endswith(("_Template.md", "_Guide.md"))]
        jsons_en = list(folder_en.glob("*.json"))
        csvs_en = list(folder_en.glob("*.csv"))
        
        ex_folder_en = EXAMPLES_EN / rel_en
        examples_en = list(ex_folder_en.glob("*_Example.md"))

        m = re.search(r'(\d{2}_\d{2}(?:_\d{2})?)', t_en.name)
        code_raw = m.group(1) if m else ""
        doc_id = "PMO-" + code_raw.replace("_", ".")

        name_en = t_en.stem.replace("_Template", "")
        name_en_clean = re.sub(r'^\d{2}_\d{2}(?:_\d{2})?_', '', name_en).replace("_", " ")

        phase_prefix = str(rel_en).split("/")[0][:2]
        
        # Exact prefix match for Arabic template
        matching_ar = [t for t in ar_templates if t.name.startswith(f"{code_raw}_")]
        t_ar = matching_ar[0] if matching_ar else None
        folder_ar = t_ar.parent if t_ar else None
        rel_ar = folder_ar.relative_to(FORMS_AR) if folder_ar else None
        guides_ar = list(folder_ar.glob("*_دليل.md")) if folder_ar else []
        prompts_ar = [p for p in folder_ar.glob("*.md") if not p.name.endswith(("_قالب.md", "_دليل.md"))] if folder_ar else []
        jsons_ar = list(folder_ar.glob("*.json")) if folder_ar else []
        csvs_ar = list(folder_ar.glob("*.csv")) if folder_ar else []
        
        ex_folder_ar = EXAMPLES_AR / rel_ar if rel_ar else None
        examples_ar = list(ex_folder_ar.glob("*_مثال.md")) if ex_folder_ar else []
        
        name_ar = t_ar.stem.replace("_قالب", "") if t_ar else ""
        name_ar_clean = re.sub(r'^\d{2}_\d{2}(?:_\d{2})?_', '', name_ar).replace("_", " ")

        if phase_prefix == "04":
            sub_en = rel_en.parts[1]
            sub_ar = rel_ar.parts[1] if rel_ar and len(rel_ar.parts) > 1 else sub_en
            dest_dir_en = pathlib.Path("04_Planning") / sub_en
            dest_dir_ar = pathlib.Path(rel_ar.parts[0]) / sub_ar if rel_ar else dest_dir_en
        else:
            dest_dir_en = pathlib.Path(rel_en.parts[0])
            dest_dir_ar = pathlib.Path(rel_ar.parts[0]) if rel_ar else dest_dir_en

        doc_tpl_en = DOCS_DIR / "forms" / "en" / dest_dir_en / t_en.name
        doc_guide_en = DOCS_DIR / "guides" / "en" / dest_dir_en / guides_en[0].name
        doc_ex_en = DOCS_DIR / "examples" / "en" / dest_dir_en / examples_en[0].name

        doc_tpl_ar = DOCS_DIR / "forms" / "ar" / dest_dir_ar / t_ar.name if t_ar else None
        doc_guide_ar = DOCS_DIR / "guides" / "ar" / dest_dir_ar / guides_ar[0].name if guides_ar else None
        doc_ex_ar = DOCS_DIR / "examples" / "ar" / dest_dir_ar / examples_ar[0].name if examples_ar else None

        tier_info = TIER_MAP.get(phase_prefix, "Tier 1 | Tier 2 | Tier 3")
        if "AI" in name_en or "02_02" in code_raw or "02_03" in code_raw or "02_04" in code_raw or "02_05" in code_raw or "02_06" in code_raw:
            tier_info = "Tier 4 (AI & Specialized)"

        gh_tpl_en = f"{gh_base}/{t_en.relative_to(ROOT).as_posix()}"
        gh_guide_en = f"{gh_base}/{guides_en[0].relative_to(ROOT).as_posix()}" if guides_en else ""
        gh_ex_en = f"{gh_base}/{examples_en[0].relative_to(ROOT).as_posix()}" if examples_en else ""
        gh_prompt_en = f"{gh_base}/{prompts_en[0].relative_to(ROOT).as_posix()}" if prompts_en else ""
        gh_json_en = f"{gh_base}/{jsons_en[0].relative_to(ROOT).as_posix()}" if jsons_en else ""
        gh_csv_en = f"{gh_base}/{csvs_en[0].relative_to(ROOT).as_posix()}" if csvs_en else ""

        gh_tpl_ar = f"{gh_base}/{t_ar.relative_to(ROOT).as_posix()}" if t_ar else ""
        gh_guide_ar = f"{gh_base}/{guides_ar[0].relative_to(ROOT).as_posix()}" if guides_ar else ""
        gh_ex_ar = f"{gh_base}/{examples_ar[0].relative_to(ROOT).as_posix()}" if examples_ar else ""
        gh_prompt_ar = f"{gh_base}/{prompts_ar[0].relative_to(ROOT).as_posix()}" if prompts_ar else ""
        gh_json_ar = f"{gh_base}/{jsons_ar[0].relative_to(ROOT).as_posix()}" if jsons_ar else ""
        gh_csv_ar = f"{gh_base}/{csvs_ar[0].relative_to(ROOT).as_posix()}" if csvs_ar else ""

        deliverables.append({
            "code": doc_id,
            "code_raw": code_raw,
            "phase": phase_prefix,
            "tier": tier_info,
            "rel_en": rel_en,
            "rel_ar": rel_ar,
            "dest_dir_en": dest_dir_en,
            "dest_dir_ar": dest_dir_ar,
            "name_en": name_en_clean,
            "name_ar": name_ar_clean,
            "tpl_en": t_en,
            "guide_en": guides_en[0] if guides_en else None,
            "prompt_en": prompts_en[0] if prompts_en else None,
            "json_en": jsons_en[0] if jsons_en else None,
            "csv_en": csvs_en[0] if csvs_en else None,
            "ex_en": examples_en[0] if examples_en else None,
            "tpl_ar": t_ar,
            "guide_ar": guides_ar[0] if guides_ar else None,
            "prompt_ar": prompts_ar[0] if prompts_ar else None,
            "json_ar": jsons_ar[0] if jsons_ar else None,
            "csv_ar": csvs_ar[0] if csvs_ar else None,
            "ex_ar": examples_ar[0] if examples_ar else None,
            "doc_tpl_en": doc_tpl_en,
            "doc_guide_en": doc_guide_en,
            "doc_ex_en": doc_ex_en,
            "doc_tpl_ar": doc_tpl_ar,
            "doc_guide_ar": doc_guide_ar,
            "doc_ex_ar": doc_ex_ar,
            "gh_tpl_en": gh_tpl_en,
            "gh_guide_en": gh_guide_en,
            "gh_ex_en": gh_ex_en,
            "gh_prompt_en": gh_prompt_en,
            "gh_json_en": gh_json_en,
            "gh_csv_en": gh_csv_en,
            "gh_tpl_ar": gh_tpl_ar,
            "gh_guide_ar": gh_guide_ar,
            "gh_ex_ar": gh_ex_ar,
            "gh_prompt_ar": gh_prompt_ar,
            "gh_json_ar": gh_json_ar,
            "gh_csv_ar": gh_csv_ar,
        })

    return deliverables

def build_portal():
    deliverables = collect_deliverables()
    print(f"Loaded {len(deliverables)} deliverable bundles.")

    # Clean existing generated docs sections
    for sub in ["catalog", "forms", "guides", "examples"]:
        target_dir = DOCS_DIR / sub
        if target_dir.exists():
            shutil.rmtree(target_dir)

    # 1. Write Deliverable Pages
    for d in deliverables:
        for p in [d["doc_tpl_en"], d["doc_guide_en"], d["doc_ex_en"], d["doc_tpl_ar"], d["doc_guide_ar"], d["doc_ex_ar"]]:
            if p:
                p.parent.mkdir(parents=True, exist_ok=True)

        # Cross-links with .html for raw HTML tags
        rel_guide_from_tpl = os.path.relpath(d["doc_guide_en"], d["doc_tpl_en"].parent).replace(".md", ".html")
        rel_ex_from_tpl = os.path.relpath(d["doc_ex_en"], d["doc_tpl_en"].parent).replace(".md", ".html")
        rel_ar_from_tpl = os.path.relpath(d["doc_tpl_ar"], d["doc_tpl_en"].parent).replace(".md", ".html")

        rel_tpl_from_guide = os.path.relpath(d["doc_tpl_en"], d["doc_guide_en"].parent).replace(".md", ".html")
        rel_ex_from_guide = os.path.relpath(d["doc_ex_en"], d["doc_guide_en"].parent).replace(".md", ".html")
        rel_ar_from_guide = os.path.relpath(d["doc_guide_ar"], d["doc_guide_en"].parent).replace(".md", ".html")

        rel_tpl_from_ex = os.path.relpath(d["doc_tpl_en"], d["doc_ex_en"].parent).replace(".md", ".html")
        rel_guide_from_ex = os.path.relpath(d["doc_guide_en"], d["doc_ex_en"].parent).replace(".md", ".html")
        rel_ar_from_ex = os.path.relpath(d["doc_ex_ar"], d["doc_ex_en"].parent).replace(".md", ".html")

        rel_guide_from_tpl_ar = os.path.relpath(d["doc_guide_ar"], d["doc_tpl_ar"].parent).replace(".md", ".html")
        rel_ex_from_tpl_ar = os.path.relpath(d["doc_ex_ar"], d["doc_tpl_ar"].parent).replace(".md", ".html")
        rel_en_from_tpl_ar = os.path.relpath(d["doc_tpl_en"], d["doc_tpl_ar"].parent).replace(".md", ".html")

        rel_tpl_from_guide_ar = os.path.relpath(d["doc_tpl_ar"], d["doc_guide_ar"].parent).replace(".md", ".html")
        rel_ex_from_guide_ar = os.path.relpath(d["doc_ex_ar"], d["doc_guide_ar"].parent).replace(".md", ".html")
        rel_en_from_guide_ar = os.path.relpath(d["doc_guide_en"], d["doc_guide_ar"].parent).replace(".md", ".html")

        rel_tpl_from_ex_ar = os.path.relpath(d["doc_tpl_ar"], d["doc_ex_ar"].parent).replace(".md", ".html")
        rel_guide_from_ex_ar = os.path.relpath(d["doc_guide_ar"], d["doc_ex_ar"].parent).replace(".md", ".html")
        rel_en_from_ex_ar = os.path.relpath(d["doc_ex_en"], d["doc_ex_ar"].parent).replace(".md", ".html")

        # 1. EN Template
        content_tpl_en = sanitize_content_links(d["tpl_en"].read_text(encoding="utf-8"), d["doc_tpl_en"], d)
        nav_header_tpl_en = f"""<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="{d['gh_tpl_en']}" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_ar_from_tpl}">🇸🇦 الانتقال للنسخة العربية (Arabic Template) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">{d['code']}</span>
    <span class="badge badge-phase">{PHASE_META[d['phase']]['en_title']}</span>
    <span class="badge badge-standard">PMI PMBOK® 6/7/8 • ISO 21500</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill active" href="#">📋 Blank Template</a>
    <a class="nav-pill" href="{rel_guide_from_tpl}">📖 Authoring Guide</a>
    <a class="nav-pill" href="{rel_ex_from_tpl}">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="{d['gh_tpl_en']}" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="{rel_ar_from_tpl}">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

"""
        d["doc_tpl_en"].write_text(nav_header_tpl_en + content_tpl_en, encoding="utf-8")

        # 2. EN Guide
        content_guide_en = sanitize_content_links(d["guide_en"].read_text(encoding="utf-8"), d["doc_guide_en"], d)
        nav_header_guide_en = f"""<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="{d['gh_guide_en']}" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_ar_from_guide}">🇸🇦 الانتقال للدليل بالعربية (Arabic Guide) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">{d['code']}</span>
    <span class="badge badge-phase">{PHASE_META[d['phase']]['en_title']}</span>
    <span class="badge badge-type">Authoring & Governance Guide</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="{rel_tpl_from_guide}">📋 Blank Template</a>
    <a class="nav-pill active" href="#">📖 Authoring Guide</a>
    <a class="nav-pill" href="{rel_ex_from_guide}">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="{d['gh_guide_en']}" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="{rel_ar_from_guide}">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

"""
        d["doc_guide_en"].write_text(nav_header_guide_en + content_guide_en, encoding="utf-8")

        # 3. EN Example
        content_ex_en = sanitize_content_links(d["ex_en"].read_text(encoding="utf-8"), d["doc_ex_en"], d)
        nav_header_ex_en = f"""<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="{d['gh_ex_en']}" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_ar_from_ex}">🇸🇦 الانتقال للمثال بالعربية (Arabic Example) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">{d['code']}</span>
    <span class="badge badge-phase">{PHASE_META[d['phase']]['en_title']}</span>
    <span class="badge badge-example">Realistic Case Study Benchmark</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="{rel_tpl_from_ex}">📋 Blank Template</a>
    <a class="nav-pill" href="{rel_guide_from_ex}">📖 Authoring Guide</a>
    <a class="nav-pill active" href="#">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="{d['gh_ex_en']}" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="{rel_ar_from_ex}">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

"""
        d["doc_ex_en"].write_text(nav_header_ex_en + content_ex_en, encoding="utf-8")

        # 4. AR Template
        content_tpl_ar = sanitize_content_links(d["tpl_ar"].read_text(encoding="utf-8"), d["doc_tpl_ar"], d)
        nav_header_tpl_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> التوثيق باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="{d['gh_tpl_ar']}" target="_blank" rel="noopener noreferrer">🐙 عرض على GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_en_from_tpl_ar}">🇬🇧 Switch to English Template (النسخة الإنجليزية) ←</a>
  </div>
</div>

<div class="deliverable-header-card rtl-card" dir="rtl">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">{d['code']}</span>
    <span class="badge badge-phase">{PHASE_META[d['phase']]['ar_title']}</span>
    <span class="badge badge-standard">معايير PMI PMBOK® 6/7/8 • ISO 21500</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill active" href="#">📋 القالب الفارغ</a>
    <a class="nav-pill" href="{rel_guide_from_tpl_ar}">📖 دليل الاستخدام والتحرير</a>
    <a class="nav-pill" href="{rel_ex_from_tpl_ar}">💡 مثال واقعي مكتمل</a>
    <a class="nav-pill github-pill" href="{d['gh_tpl_ar']}" target="_blank" rel="noopener noreferrer">🐙 مستند GitHub ↗</a>
    <a class="nav-pill lang-pill" href="{rel_en_from_tpl_ar}">🇬🇧 English Version</a>
  </div>
</div>

---

"""
        d["doc_tpl_ar"].write_text(nav_header_tpl_ar + content_tpl_ar, encoding="utf-8")

        # 5. AR Guide
        content_guide_ar = sanitize_content_links(d["guide_ar"].read_text(encoding="utf-8"), d["doc_guide_ar"], d)
        nav_header_guide_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> التوثيق باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="{d['gh_guide_ar']}" target="_blank" rel="noopener noreferrer">🐙 عرض على GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_en_from_guide_ar}">🇬🇧 Switch to English Guide (النسخة الإنجليزية) ←</a>
  </div>
</div>

<div class="deliverable-header-card rtl-card" dir="rtl">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">{d['code']}</span>
    <span class="badge badge-phase">{PHASE_META[d['phase']]['ar_title']}</span>
    <span class="badge badge-type">دليل إرشادي وحوكمي</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="{rel_tpl_from_guide_ar}">📋 القالب الفارغ</a>
    <a class="nav-pill active" href="#">📖 دليل الاستخدام والتحرير</a>
    <a class="nav-pill" href="{rel_ex_from_guide_ar}">💡 مثال واقعي مكتمل</a>
    <a class="nav-pill github-pill" href="{d['gh_guide_ar']}" target="_blank" rel="noopener noreferrer">🐙 مستند GitHub ↗</a>
    <a class="nav-pill lang-pill" href="{rel_en_from_guide_ar}">🇬🇧 English Version</a>
  </div>
</div>

---

"""
        d["doc_guide_ar"].write_text(nav_header_guide_ar + content_guide_ar, encoding="utf-8")

        # 6. AR Example
        content_ex_ar = sanitize_content_links(d["ex_ar"].read_text(encoding="utf-8"), d["doc_ex_ar"], d)
        nav_header_ex_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> التوثيق باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="{d['gh_ex_ar']}" target="_blank" rel="noopener noreferrer">🐙 عرض على GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_en_from_ex_ar}">🇬🇧 Switch to English Example (النسخة الإنجليزية) ←</a>
  </div>
</div>

<div class="deliverable-header-card rtl-card" dir="rtl">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">{d['code']}</span>
    <span class="badge badge-phase">{PHASE_META[d['phase']]['ar_title']}</span>
    <span class="badge badge-example">دراسة حالة واقعية مكتملة</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="{rel_tpl_from_ex_ar}">📋 القالب الفارغ</a>
    <a class="nav-pill" href="{rel_guide_from_ex_ar}">📖 دليل الاستخدام والتحرير</a>
    <a class="nav-pill active" href="#">💡 مثال واقعي مكتمل</a>
    <a class="nav-pill github-pill" href="{d['gh_ex_ar']}" target="_blank" rel="noopener noreferrer">🐙 مستند GitHub ↗</a>
    <a class="nav-pill lang-pill" href="{rel_en_from_ex_ar}">🇬🇧 English Version</a>
  </div>
</div>

---

"""
        d["doc_ex_ar"].write_text(nav_header_ex_ar + content_ex_ar, encoding="utf-8")

    # 2. Build Landing Pages (Hero Banners + Metric Stat Grids)
    build_landing_pages()

    # 3. Generate Client-Side Data JS for Interactive Explorer
    generate_tasleemat_data_js(deliverables)

    # 4. Build Master Catalogs with Interactive Explorer
    build_master_catalogs(deliverables)

    # 4. Build Section Index Pages
    build_section_indexes(deliverables)

    # 5. Build Phase Index Pages
    build_phase_indexes(deliverables)

    # 6. Update Master Governance Manuals with Language Switch Bar
    update_governance_manuals_lang_bars()

    # 7. Update Lexicon with top GitHub bar
    update_lexicon_bar()

    # 8. Audit and repair all internal markdown links across all docs/ files
    fix_all_internal_links(deliverables)

    # 9. Update mkdocs.yml navigation
    update_mkdocs_config(deliverables)

    print("Documentation portal successfully generated!")

def build_landing_pages():
    """Build modern Hero Landing pages for English (docs/index.md) and Arabic (docs/README_AR.md)."""
    # 1. English Landing Page
    index_en = """<div class="hero-wrapper">
  <div class="hero-tag">
    <span class="pulse-dot"></span> Enterprise PMO Operating System 2.0 • PMI PMBOK® 6/7/8 & NIST AI RMF
  </div>
  <h1 class="hero-title">Tasleemat PMO Operating System</h1>
  <p class="hero-subtitle">
    The premier bilingual (English & Arabic) enterprise project management framework, delivery artifacts library, and AI governance suite with 100% mathematical symmetry, zero vendor lock-in, and automated validation.
  </p>
  <div class="hero-actions">
    <a href="catalog/en/index.html" class="btn-primary">🚀 Explore Master Catalog</a>
    <a href="forms/en/index.html" class="btn-secondary">📋 Browse Templates</a>
    <a href="en/01_getting_started.html" class="btn-secondary">📚 Governance Manuals</a>
    <a href="https://github.com/fakhruldeen/Tasleemat" class="btn-secondary" target="_blank" rel="noopener noreferrer">🐙 GitHub Repository ↗</a>
    <a href="README_AR.html" class="btn-lang">🇸🇦 الانتقال للبوابة العربية</a>
  </div>
  <div class="stat-grid">
    <div class="stat-card">
      <div class="stat-number">102</div>
      <div class="stat-label">Bilingual Deliverables</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">24</div>
      <div class="stat-label">Governance Manuals</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">8</div>
      <div class="stat-label">Lifecycle Phases</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">4</div>
      <div class="stat-label">Project Sizing Tiers</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">100%</div>
      <div class="stat-label">OKF Validated</div>
    </div>
  </div>
</div>

## 🧭 Project Lifecycle & Stage-Gates Architecture

```mermaid
flowchart TD
    subgraph G0["Gate 0: Strategic Alignment"]
        P00["00. Program & Portfolio"]
        P01["01. Business & Value"]
    end

    subgraph G1["Gate 1: Project Charter"]
        P02["02. Approach & Tailoring"]
        P03["03. Initiating"]
    end

    subgraph G2["Gate 2: Baseline Approval"]
        P04["04. Planning (12 Areas)"]
    end

    subgraph G3["Gate 3: Execution & Control"]
        P05["05. Executing"]
        P06["06. Monitoring & Controlling"]
    end

    subgraph G4["Gate 4 & 5: Operational Handover & Closeout"]
        P07["07. Closing"]
    end

    G0 --> G1 --> G2 --> G3 --> G4
```

---

## 🏛️ Browse by Lifecycle Phase

<div class="phase-cards-grid">
  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 00</span>
      <span style="font-size: 1.5rem;">🏛️</span>
    </div>
    <h3 class="phase-hub-title">Program & Portfolio Management</h3>
    <p class="phase-hub-desc">Strategic alignment, portfolio balancing, multi-project dependencies, and PMO maturity (6 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/00_Program_and_Portfolio_Management/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/00_Program_and_Portfolio_Management/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/00_Program_and_Portfolio_Management/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 01</span>
      <span style="font-size: 1.5rem;">💎</span>
    </div>
    <h3 class="phase-hub-title">Business & Value Delivery</h3>
    <p class="phase-hub-desc">Business justification, benefit realization planning, value tracking, and gap analysis (4 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/01_Business_and_Value_Delivery/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/01_Business_and_Value_Delivery/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/01_Business_and_Value_Delivery/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 02</span>
      <span style="font-size: 1.5rem;">⚖️</span>
    </div>
    <h3 class="phase-hub-title">Project Approach & Tailoring</h3>
    <p class="phase-hub-desc">Tailoring strategy, governance tiers, AI ethics, model cards, and agile/hybrid adoption (6 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/02_Project_Approach_and_Tailoring/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/02_Project_Approach_and_Tailoring/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/02_Project_Approach_and_Tailoring/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 03</span>
      <span style="font-size: 1.5rem;">🚀</span>
    </div>
    <h3 class="phase-hub-title">Initiating</h3>
    <p class="phase-hub-desc">Formal authorization, product vision, initial assumptions, and stakeholder identification (5 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/03_Initiating/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/03_Initiating/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/03_Initiating/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 04</span>
      <span style="font-size: 1.5rem;">📐</span>
    </div>
    <h3 class="phase-hub-title">Planning (12 Domains)</h3>
    <p class="phase-hub-desc">Comprehensive baselines across Scope, Schedule, Cost, Quality, Resources, Risk, and Procurement (47 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/04_Planning/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/04_Planning/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/04_Planning/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 05</span>
      <span style="font-size: 1.5rem;">⚡</span>
    </div>
    <h3 class="phase-hub-title">Executing</h3>
    <p class="phase-hub-desc">Directing work, managing issues, decision logs, change control, and team performance (12 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/05_Executing/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/05_Executing/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/05_Executing/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 06</span>
      <span style="font-size: 1.5rem;">📊</span>
    </div>
    <h3 class="phase-hub-title">Monitoring & Controlling</h3>
    <p class="phase-hub-desc">Status reporting, Earned Value Analysis (EVA), variance tracking, and quality acceptance (12 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/06_Monitoring_and_Controlling/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/06_Monitoring_and_Controlling/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/06_Monitoring_and_Controlling/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 07</span>
      <span style="font-size: 1.5rem;">🏁</span>
    </div>
    <h3 class="phase-hub-title">Closing</h3>
    <p class="phase-hub-desc">Formal transition to operations, contract closure, final lessons learned, and PIR (5 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/07_Closing/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/07_Closing/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/07_Closing/index.html">💡 Examples</a>
    </div>
  </div>
</div>

---

## 📑 Master Governance Manuals (12 Systems Guides)

| Guide # | Document Title | Language | Description & Key Value |
| :---: | :--- | :---: | :--- |
| **01** | [**Getting Started**](en/01_getting_started.md) | 🇬🇧 EN | Quick-start lifecycle overview, onboarding steps from Day 1 to Day 30. |
| **02** | [**Practitioner Usage Guide**](en/02_usage_guide.md) | 🇬🇧 EN | Field syntax, Markdown conventions, JSON/CSV integration, and authoring guidelines. |
| **03** | [**PMO Policy Manual**](en/03_pmo_policy_manual.md) | 🇬🇧 EN | Enterprise governance mandates, change control thresholds, and audit rules. |
| **04** | [**Stage-Gates Framework**](en/04_stage_gates_and_governance.md) | 🇬🇧 EN | 6 Stage-Gates (Gate 0 to 5), entry/exit criteria, and executive review gates. |
| **05** | [**Tailoring Profiles**](en/05_tailoring_profiles.md) | 🇬🇧 EN | 4 project tiers (Enterprise, Medium, Agile, AI) and deliverable requirements. |
| **06** | [**RACI Authority Matrix**](en/06_raci_authority_matrix.md) | 🇬🇧 EN | Full 102-form governance matrix defining author and approval sign-off roles. |
| **07** | [**Document Dependencies**](en/07_document_dependencies.md) | 🇬🇧 EN | Directed acyclic graph (DAG) mapping upstream inputs to downstream outputs. |
| **08** | [**AI Governance Framework**](en/08_ai_governance_framework.md) | 🇬🇧 EN | AI Canvas, Model Cards, Ethics, NIST AI RMF, and MLOps monitoring. |
| **09** | [**Agile & Hybrid Integration**](en/09_agile_hybrid_integration.md) | 🇬🇧 EN | Mapping forms to Scrum/Kanban ceremonies, Flow metrics, and DoD/DoR. |
| **10** | [**FAQ & Troubleshooting**](en/10_faq_and_troubleshooting.md) | 🇬🇧 EN | 25+ practical answers to governance hurdles, sizing disputes, and EVM issues. |
| **11** | [**Tools & Automation Guide**](en/11_tools_and_automation.md) | 🇬🇧 EN | Python validation suite, CI/CD pipelines, JIRA/Azure DevOps integration. |
| **12** | [**Open Knowledge Framework (OKF)**](en/12_open_knowledge_framework.md) | 🇬🇧 EN | Frictionless Data Package standard, FAIR data principles, datapackage.json. |
| **LEX** | [**Master Lexicon & Catalog**](LEXICON.md) | 🌐 Bi | Master bilingual terminology glossary and cross-reference table. |

---

## 👤 Persona-Based Reading Pathways

* **For Project Managers:** Start with [`01_getting_started.md`](en/01_getting_started.md) → [`05_tailoring_profiles.md`](en/05_tailoring_profiles.md) → [`02_usage_guide.md`](en/02_usage_guide.md) → [Templates Library](forms/en/index.md).
* **For PMO Directors & Governance Leads:** Read [`03_pmo_policy_manual.md`](en/03_pmo_policy_manual.md) → [`04_stage_gates_and_governance.md`](en/04_stage_gates_and_governance.md) → [`06_raci_authority_matrix.md`](en/06_raci_authority_matrix.md).
* **For Scrum Masters & Product Owners:** Focus on [`09_agile_hybrid_integration.md`](en/09_agile_hybrid_integration.md) → [`05_tailoring_profiles.md`](en/05_tailoring_profiles.md) → [Agile Backlog & Retrospective](forms/en/05_Executing/index.md).
* **For AI Engineers & Tech PMs:** Deep dive into [`08_ai_governance_framework.md`](en/08_ai_governance_framework.md) → [AI Governance Templates](forms/en/02_Project_Approach_and_Tailoring/index.md).
* **For DevOps & Tool Admins:** Explore [`11_tools_and_automation.md`](en/11_tools_and_automation.md) → [`12_open_knowledge_framework.md`](en/12_open_knowledge_framework.md).
"""
    (DOCS_DIR / "index.md").write_text(index_en, encoding="utf-8")

    # 2. Arabic Landing Page
    index_ar = """<div class="hero-wrapper" dir="rtl">
  <div class="hero-tag">
    <span class="pulse-dot"></span> نظام التشغيل الحوكمي لإدارة المشاريع 2.0 • PMI PMBOK® 6/7/8 وأخلاقيات الذكاء الاصطناعي (سدايا)
  </div>
  <h1 class="hero-title">نظام تسليمات لإدارة المشاريع الحوكمية</h1>
  <p class="hero-subtitle">
    المرجع المؤسسي الشامل ثنائي اللغة (عربي/إنجليزي) لمكتب إدارة المشاريع (PMO)، وحزمة المخرجات الإدارية، وحوكمة مشاريع الذكاء الاصطناعي بتناظر رياضي 100% ودون أي قيود أو تبعية تقنية.
  </p>
  <div class="hero-actions">
    <a href="catalog/ar/index.html" class="btn-primary">🚀 استكشاف الفهرس الشامل</a>
    <a href="forms/ar/index.html" class="btn-secondary">📋 تصفح القوالب القياسية</a>
    <a href="ar/01_getting_started.html" class="btn-secondary">📚 الأدلة والسياسات</a>
    <a href="https://github.com/fakhruldeen/Tasleemat" class="btn-secondary" target="_blank" rel="noopener noreferrer">🐙 مستودع GitHub ↗</a>
    <a href="index.html" class="btn-lang">🇬🇧 Switch to English Portal</a>
  </div>
  <div class="stat-grid">
    <div class="stat-card">
      <div class="stat-number">102</div>
      <div class="stat-label">مخرجاً إدارياً ثنائياً</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">24</div>
      <div class="stat-label">دليلاً حوكمياً معتمداً</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">8</div>
      <div class="stat-label">مراحل لدورة الحياة</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">4</div>
      <div class="stat-label">مستويات لتخصيص المشاريع</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">100%</div>
      <div class="stat-label">مطابقة لمعيار OKF</div>
    </div>
  </div>
</div>

## 🧭 مخطط دورة حياة المشروع وبوابات العبور الحوكمية

```mermaid
flowchart TD
    subgraph G0["بوابة 0: المواءمة الاستراتيجية ودراسة الجدوى"]
        P00["00. إدارة البرامج والمحافظ"]
        P01["01. الأعمال وتسليم القيمة"]
    end

    subgraph G1["بوابة 1: ميثاق المشروع والتخصيص"]
        P02["02. منهجية المشروع وتخصيصه"]
        P03["03. البدء"]
    end

    subgraph G2["بوابة 2: اعتماد خطوط الأساس"]
        P04["04. التخطيط (12 مجالاً معرفياً)"]
    end

    subgraph G3["بوابة 3: التنفيذ والتحكم في الأداء"]
        P05["05. التنفيذ"]
        P06["06. المراقبة والتحكم"]
    end

    subgraph G4["بوابة 4 و 5: التسليم التشغيلي والإغلاق"]
        P07["07. الإغلاق"]
    end

    G0 --> G1 --> G2 --> G3 --> G4
```

---

## 🏛️ تصفح النماذج والمخرجات حسب مراحل دورة الحياة

<div class="phase-cards-grid" dir="rtl">
  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 00</span>
      <span style="font-size: 1.5rem;">🏛️</span>
    </div>
    <h3 class="phase-hub-title">إدارة البرامج والمحافظ</h3>
    <p class="phase-hub-desc">المواءمة الاستراتيجية، توازن المحفظة، إدارة الاعتماديات بين المشاريع، وتقييم نضج PMO (6 مخرجات).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/00_إدارة_البرامج_والمحافظ/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/00_إدارة_البرامج_والمحافظ/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/00_إدارة_البرامج_والمحافظ/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 01</span>
      <span style="font-size: 1.5rem;">💎</span>
    </div>
    <h3 class="phase-hub-title">الأعمال وتسليم القيمة</h3>
    <p class="phase-hub-desc">دراسات الجدوى الاقتصادية، خطط إدارة المنافع، سجلات تحقيق القيمة، وتحليل الفجوات (4 مخرجات).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/01_الأعمال_وتسليم_القيمة/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/01_الأعمال_وتسليم_القيمة/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/01_الأعمال_وتسليم_القيمة/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 02</span>
      <span style="font-size: 1.5rem;">⚖️</span>
    </div>
    <h3 class="phase-hub-title">منهجية المشروع وتخصيصه</h3>
    <p class="phase-hub-desc">استراتيجية التخصيص، مستويات الحوكمة، أخلاقيات الذكاء الاصطناعي، وبطاقات النماذج (6 مخرجات).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/02_منهجية_المشروع_وتخصيصه/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/02_منهجية_المشروع_وتخصيصه/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/02_منهجية_المشروع_وتخصيصه/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 03</span>
      <span style="font-size: 1.5rem;">🚀</span>
    </div>
    <h3 class="phase-hub-title">البدء</h3>
    <p class="phase-hub-desc">الترخيص الرسمي للمشروع، رؤية المنتج، سجل الافتراضات الأولية، وتحديد المعنيين (5 مخرجات).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/03_البدء/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/03_البدء/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/03_البدء/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 04</span>
      <span style="font-size: 1.5rem;">📐</span>
    </div>
    <h3 class="phase-hub-title">التخطيط (12 مجالاً معرفياً)</h3>
    <p class="phase-hub-desc">الخطوط المرجعية للنطاق، الجدول الزمني، التكلفة، الجودة، الموارد، المخاطر، والمشتريات (47 مخرجاً).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/04_التخطيط/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/04_التخطيط/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/04_التخطيط/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 05</span>
      <span style="font-size: 1.5rem;">⚡</span>
    </div>
    <h3 class="phase-hub-title">التنفيذ</h3>
    <p class="phase-hub-desc">توجيه وإدارة أعمال المشروع، سجل القضايا، سجل القرارات، طلبات التغيير، وأداء الفريق (12 مخرجاً).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/05_التنفيذ/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/05_التنفيذ/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/05_التنفيذ/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 06</span>
      <span style="font-size: 1.5rem;">📊</span>
    </div>
    <h3 class="phase-hub-title">المراقبة والتحكم</h3>
    <p class="phase-hub-desc">تقارير الأداء، تحليل القيمة المكتسبة (EVA)، مراقبة التباين، وضمان الجودة واختبارات القبول (12 مخرجاً).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/06_المراقبة_والتحكم/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/06_المراقبة_والتحكم/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/06_المراقبة_والتحكم/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 07</span>
      <span style="font-size: 1.5rem;">🏁</span>
    </div>
    <h3 class="phase-hub-title">الإغلاق</h3>
    <p class="phase-hub-desc">الانتقال الرسمي للعمليات التشغيلية، إغلاق العقود، خلاصة الدروس المستفادة، ومراجعة ما بعد التنفيذ (5 مخرجات).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/07_الإغلاق/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/07_الإغلاق/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/07_الإغلاق/index.html">💡 الأمثلة</a>
    </div>
  </div>
</div>

---

## 📑 جدول الأدلة والوثائق الإرشادية (12 دليلاً حوكمياً)

| رقم الدليل | عنوان الوثيقة | اللغة | الوصف والقيمة التشغيلية |
| :---: | :--- | :---: | :--- |
| **01** | [**دليل البدء السريع**](ar/01_getting_started.md) | 🇸🇦 AR | خطوات الانطلاق في المشروع وإجراءات العمل من اليوم 1 حتى اليوم 30. |
| **02** | [**دليل الممارس الشامل**](ar/02_usage_guide.md) | 🇸🇦 AR | قواعد تحرير النماذج، بناء حقول Markdown، والتكامل مع ملفات JSON و CSV. |
| **03** | [**دليل سياسات PMO**](ar/03_pmo_policy_manual.md) | 🇸🇦 AR | سياسات الحوكمة المؤسسية، إدارة خطوط الأساس، وضوابط التدقيق والامتثال. |
| **04** | [**بوابات العبور والمراجعات**](ar/04_stage_gates_and_governance.md) | 🇸🇦 AR | إطار بوابات العبور الست (بوابة 0 إلى 5)، معايير الدخول والخروج والاعتماد. |
| **05** | [**ملفات التخصيص وتصنيف المشاريع**](ar/05_tailoring_profiles.md) | 🇸🇦 AR | تصنيف المشاريع إلى 4 مستويات وتحديد المخرجات الإلزامية لكل مستوى. |
| **06** | [**مصفوفة الصلاحيات RACI**](ar/06_raci_authority_matrix.md) | 🇸🇦 AR | جدول الصلاحيات والمسؤوليات لكافة الـ 102 نموذج وتحديد سلطات التوقيع. |
| **07** | [**شبكة اعتماديات الوثائق**](ar/07_document_dependencies.md) | 🇸🇦 AR | خريطة تدفق البيانات والاعتماديات السابقة واللاحقة لكافة مخرجات المشروع. |
| **08** | [**إطار حوكمة الذكاء الاصطناعي**](ar/08_ai_governance_framework.md) | 🇸🇦 AR | لوحة الاستخدام، بطاقات النماذج، مواءمة سدايا و NIST ومراقبة MLOps. |
| **09** | [**المنهجيات الرشيقة والهجينة**](ar/09_agile_hybrid_integration.md) | 🇸🇦 AR | مواءمة النماذج مع سكرم وكانبان، مقاييس التدفق، وتعريف الجاهزية والانتهاء. |
| **10** | [**الأسئلة الشائعة وحل المشكلات**](ar/10_faq_and_troubleshooting.md) | 🇸🇦 AR | أكثر من 25 إجابة عملية لحل المشكلات الحوكمية، الخلافات التوثيقية وحسابات EVM. |
| **11** | [**دليل الأدوات والأتمتة**](ar/11_tools_and_automation.md) | 🇸🇦 AR | حزمة الفحص الآلي في بايثون، وخطوط أنابيب CI/CD والربط مع JIRA و DevOps. |
| **12** | [**معيار مؤسسة المعرفة المفتوحة (OKF)**](ar/12_open_knowledge_framework.md) | 🇸🇦 AR | حزم البيانات السلسة (Frictionless Data)، مبادئ FAIR، وملف datapackage.json. |
| **LEX** | [**المعجم الموحد للمصطلحات**](LEXICON.md) | 🌐 ثنائي | المعجم الرسمي المعتمد للمصطلحات الإنجليزية والعربية وفهرس النماذج. |

---

## 👤 مسارات القراءة الموصى بها بحسب الدور الوظيفي

* **لمديري المشاريع:** ابدأ بـ [`01_getting_started.md`](ar/01_getting_started.md) → [`05_tailoring_profiles.md`](ar/05_tailoring_profiles.md) → [`02_usage_guide.md`](ar/02_usage_guide.md) → [مكتبة القوالب](forms/ar/index.md).
* **لمدراء مكاتب إدارة المشاريع (PMO):** راجع [`03_pmo_policy_manual.md`](ar/03_pmo_policy_manual.md) → [`04_stage_gates_and_governance.md`](ar/04_stage_gates_and_governance.md) → [`06_raci_authority_matrix.md`](ar/06_raci_authority_matrix.md).
* **لقادة سكرم والتحول الرشيق:** ركز على [`09_agile_hybrid_integration.md`](ar/09_agile_hybrid_integration.md) → [`05_tailoring_profiles.md`](ar/05_tailoring_profiles.md) → [سجلات سكرم والمراجعات](forms/ar/05_التنفيذ/index.md).
* **لمدراء مشاريع الذكاء الاصطناعي:** تعمق في [`08_ai_governance_framework.md`](ar/08_ai_governance_framework.md) → [قوالب حوكمة الذكاء الاصطناعي](forms/ar/02_منهجية_المشروع_وتخصيصه/index.md).
* **لمسؤولي الأنظمة والأتمتة:** استكشف [`11_tools_and_automation.md`](ar/11_tools_and_automation.md) → [`12_open_knowledge_framework.md`](ar/12_open_knowledge_framework.md).
"""
    (DOCS_DIR / "README_AR.md").write_text(index_ar, encoding="utf-8")

def clean_manual_content_string(content: str) -> str:
    cleaned = re.sub(r'<div class="lang-switch-bar"[^>]*>[\s\S]*?</div>\s*</div>\n*', '', content)
    cleaned = re.sub(r'<div class="lang-switch-bar"[^>]*>[\s\S]*?</div>\n*', '', cleaned)
    lines = cleaned.splitlines()
    start_idx = 0
    while start_idx < len(lines):
        line_s = lines[start_idx].strip()
        if line_s in ['</div>', '<div>', '</div></div>', ''] or line_s.startswith('<div class="lang-switch'):
            start_idx += 1
        else:
            break
    return '\n'.join(lines[start_idx:])

def update_governance_manuals_lang_bars():
    """Ensure all 12 EN and 12 AR governance manuals have top language switcher bars."""
    for i in range(1, 13):
        en_files = list((DOCS_DIR / "en").glob(f"{i:02d}_*.md"))
        ar_files = list((DOCS_DIR / "ar").glob(f"{i:02d}_*.md"))

        if en_files and ar_files:
            en_f, ar_f = en_files[0], ar_files[0]
            rel_ar = os.path.relpath(ar_f, en_f.parent).replace(".md", ".html")
            rel_en = os.path.relpath(en_f, ar_f.parent).replace(".md", ".html")

            en_content = clean_manual_content_string(en_f.read_text(encoding="utf-8"))
            bar_en = f"""<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Manual</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/docs/en/{en_f.name}" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_ar}">🇸🇦 الانتقال للنسخة العربية (Arabic Manual) →</a>
  </div>
</div>

"""
            en_f.write_text(bar_en + en_content.lstrip(), encoding="utf-8")

            ar_content = clean_manual_content_string(ar_f.read_text(encoding="utf-8"))
            bar_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> الدليل باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/docs/ar/{ar_f.name}" target="_blank" rel="noopener noreferrer">🐙 عرض على GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_en}">🇬🇧 Switch to English Version (النسخة الإنجليزية) ←</a>
  </div>
</div>

"""
            ar_f.write_text(bar_ar + ar_content.lstrip(), encoding="utf-8")

def update_lexicon_bar():
    """Ensure docs/LEXICON.md has a top language switch and GitHub repo bar."""
    lex_file = DOCS_DIR / "LEXICON.md"
    if not lex_file.exists():
        return
    content = clean_manual_content_string(lex_file.read_text(encoding="utf-8"))
    bar = """<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Bilingual Resource:</strong> Master Lexicon & Deliverables Catalog | المعجم الموحد للمصطلحات</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/docs/LEXICON.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
  </div>
</div>

"""
    lex_file.write_text(bar + content.lstrip(), encoding="utf-8")

def fix_all_internal_links(deliverables):
    """Audit and automatically resolve all relative markdown links across docs/ to guarantee zero 404s."""
    en_tpls = {re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name).group(1): p for p in (DOCS_DIR / "forms" / "en").rglob("*_Template.md") if re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name)}
    ar_tpls = {re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name).group(1): p for p in (DOCS_DIR / "forms" / "ar").rglob("*_قالب.md") if re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name)}

    en_guides = {re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name).group(1): p for p in (DOCS_DIR / "guides" / "en").rglob("*_Guide.md") if re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name)}
    ar_guides = {re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name).group(1): p for p in (DOCS_DIR / "guides" / "ar").rglob("*_دليل.md") if re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name)}

    en_exs = {re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name).group(1): p for p in (DOCS_DIR / "examples" / "en").rglob("*_Example.md") if re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name)}
    ar_exs = {re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name).group(1): p for p in (DOCS_DIR / "examples" / "ar").rglob("*_مثال.md") if re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", p.name)}

    en_manuals = {f"{i:02d}": list((DOCS_DIR / "en").glob(f"{i:02d}_*.md"))[0] for i in range(1, 13) if list((DOCS_DIR / "en").glob(f"{i:02d}_*.md"))}
    ar_manuals = {f"{i:02d}": list((DOCS_DIR / "ar").glob(f"{i:02d}_*.md"))[0] for i in range(1, 13) if list((DOCS_DIR / "ar").glob(f"{i:02d}_*.md"))}

    link_pat = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(((?:[^()]+|\([^()]*\))+)\)")

    def fix_link(md_file, match):
        text = match.group(1)
        url = match.group(2).strip()

        if url.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)

        clean_url = url.split("#")[0].split("?")[0].strip()
        fragment = ("#" + url.split("#")[1]) if "#" in url else ""

        target = (md_file.parent / clean_url).resolve()
        if target.exists() and target.is_file():
            return match.group(0)

        is_ar = "/ar/" in str(md_file) or "README_AR" in str(md_file) or "_قالب" in str(md_file) or "_دليل" in str(md_file) or "_مثال" in str(md_file)

        # 1. Manuals
        m_man = re.search(r"(\d{2})_[a-z_]+\.md", clean_url)
        if m_man and m_man.group(1) in en_manuals:
            num = m_man.group(1)
            target_man = ar_manuals[num] if is_ar else en_manuals[num]
            rel = os.path.relpath(target_man, md_file.parent)
            return f"[{text}]({rel}{fragment})"

        # 2. Deliverable code
        m_code = re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", clean_url) or re.search(r"(\d{2}_\d{2}(?:_\d{2})?)", text) or re.search(r"PMO-(\d{2}\.\d{2}(?:\.\d{2})?)", text)
        if m_code:
            raw_code = m_code.group(1).replace(".", "_")
            if "guide" in clean_url.lower() or "دليل" in clean_url or "دليل" in text or "Guide" in text:
                target_del = ar_guides.get(raw_code) if is_ar else en_guides.get(raw_code)
            elif "example" in clean_url.lower() or "مثال" in clean_url or "مثال" in text or "Example" in text:
                target_del = ar_exs.get(raw_code) if is_ar else en_exs.get(raw_code)
            else:
                target_del = ar_tpls.get(raw_code) if is_ar else en_tpls.get(raw_code)

            if target_del:
                rel = os.path.relpath(target_del, md_file.parent)
                return f"[{text}]({rel}{fragment})"

        # 3. Root forms or docs index
        if clean_url in ["../forms/en/", "../forms/ar/", "forms/en/", "forms/ar/", "../../forms/en/", "../../forms/ar/"]:
            target_f = (DOCS_DIR / "forms" / ("ar" if "ar" in clean_url else "en") / "index.md")
            rel = os.path.relpath(target_f, md_file.parent)
            return f"[{text}]({rel})"

        return match.group(0)

    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        new_content = link_pat.sub(lambda m: fix_link(md_file, m), content)
        if new_content != content:
            md_file.write_text(new_content, encoding="utf-8")

def build_master_catalogs(deliverables):
    """Build comprehensive interactive master catalog pages with live Explorer widget."""
    target_en = DOCS_DIR / "catalog/en/index.md"
    target_en.parent.mkdir(parents=True, exist_ok=True)
    rel_ar_catalog = os.path.relpath(DOCS_DIR / "catalog/ar/index.md", target_en.parent).replace(".md", ".html")

    catalog_en = f"""<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Master Catalog</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/docs/catalog/en" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_ar_catalog}">🇸🇦 الانتقال للفهرس العام بالعربية (Arabic Catalog) →</a>
  </div>
</div>

# 📑 Master Deliverables & Artifacts Catalog
**Standard Alignment:** PMI PMBOK® 6th, 7th & 8th Editions • NIST AI RMF • ISO 21500  
**Total Matrix:** 102 Bilingual Forms (204 Standard Templates • 204 Authoring Guides • 204 Case Studies)

---

<div id="tasleemat-explorer" class="explorer-wrapper">
  <div class="explorer-toolbar">
    <input type="text" id="explorer-search" class="explorer-search-box" placeholder="🔍 Instant search by code (e.g. PMO-03.01), deliverable name, phase, tier, or standard..." />
    
    <div class="explorer-filter-group">
      <span class="explorer-filter-label">Phase:</span>
      <button class="filter-chip filter-phase-btn active" data-phase="all">All (102)</button>
      <button class="filter-chip filter-phase-btn" data-phase="00">00. Portfolio (6)</button>
      <button class="filter-chip filter-phase-btn" data-phase="01">01. Value (4)</button>
      <button class="filter-chip filter-phase-btn" data-phase="02">02. Tailoring (6)</button>
      <button class="filter-chip filter-phase-btn" data-phase="03">03. Initiating (5)</button>
      <button class="filter-chip filter-phase-btn" data-phase="04">04. Planning (47)</button>
      <button class="filter-chip filter-phase-btn" data-phase="05">05. Executing (12)</button>
      <button class="filter-chip filter-phase-btn" data-phase="06">06. Monitoring (12)</button>
      <button class="filter-chip filter-phase-btn" data-phase="07">07. Closing (5)</button>
    </div>

    <div class="explorer-filter-group">
      <span class="explorer-filter-label">Governance Tier:</span>
      <button class="filter-chip filter-tier-btn active" data-tier="all">All Tiers</button>
      <button class="filter-chip filter-tier-btn" data-tier="Tier 1">🔴 Tier 1 (Mega / Strategic)</button>
      <button class="filter-chip filter-tier-btn" data-tier="Tier 2">🟡 Tier 2 (Standard Enterprise)</button>
      <button class="filter-chip filter-tier-btn" data-tier="Tier 3">🟢 Tier 3 (Lean Fast-Track)</button>
      <button class="filter-chip filter-tier-btn" data-tier="Tier 4">🤖 Tier 4 (AI & Specialized)</button>
    </div>

    <div class="explorer-filter-group" style="justify-content: space-between; margin-top: 6px;">
      <span style="font-size: 0.86rem; color: var(--text-muted); font-weight: 600;">Showing <span id="results-count" style="color: var(--brand-primary); font-weight: 800;">102</span> deliverables</span>
      <div style="display: flex; gap: 6px;">
        <button class="filter-chip view-toggle-btn active" data-view="cards">🗂️ Card Grid View</button>
        <button class="filter-chip view-toggle-btn" data-view="table">📊 Table View</button>
      </div>
    </div>
  </div>

  <div id="explorer-cards" class="explorer-grid-cards">
"""

    for d in deliverables:
        rel_tpl = os.path.relpath(d["doc_tpl_en"], target_en.parent).replace(".md", ".html")
        rel_guide = os.path.relpath(d["doc_guide_en"], target_en.parent).replace(".md", ".html")
        rel_ex = os.path.relpath(d["doc_ex_en"], target_en.parent).replace(".md", ".html")
        rel_ar_tpl = os.path.relpath(d["doc_tpl_ar"], target_en.parent).replace(".md", ".html")
        phase_title = PHASE_META[d['phase']]['en_title']

        search_str = f"{d['code']} {d['name_en']} {d['name_ar']} {phase_title} {d['tier']} PMI PMBOK".lower()

        catalog_en += f"""    <div class="explorer-card-item" data-phase="{d['phase']}" data-tier="{d['tier']}" data-search="{search_str}">
      <div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
          <span class="badge badge-code">{d['code']}</span>
          <span style="font-size: 0.74rem; color: var(--text-muted); font-weight: 600;">{d['tier']}</span>
        </div>
        <h5>{d['name_en']}</h5>
        <div style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 4px;">🇸🇦 {d['name_ar']}</div>
        <div style="font-size: 0.75rem; color: #0284c7; font-weight: 600;">{phase_title}</div>
      </div>
      <div class="explorer-card-actions">
        <a class="card-action-link" href="{rel_tpl}">📋 Template</a>
        <a class="card-action-link" href="{rel_guide}">📖 Guide</a>
        <a class="card-action-link" href="{rel_ex}">💡 Example</a>
        <a class="card-action-link" style="background: rgba(16, 185, 129, 0.1); color: #34d399 !important;" href="{rel_ar_tpl}">🇸🇦 عربي</a>
      </div>
    </div>
"""

    catalog_en += """  </div>

  <div id="explorer-table" style="display: none; overflow-x: auto; margin-top: 16px;">
    <table>
      <thead>
        <tr>
          <th style="text-align: center;">Doc ID</th>
          <th>Deliverable Title</th>
          <th>Phase / Domain</th>
          <th>Governance Tier</th>
          <th style="text-align: center;">Actions</th>
        </tr>
      </thead>
      <tbody>
"""

    for d in deliverables:
        rel_tpl = os.path.relpath(d["doc_tpl_en"], target_en.parent).replace(".md", ".html")
        rel_guide = os.path.relpath(d["doc_guide_en"], target_en.parent).replace(".md", ".html")
        rel_ex = os.path.relpath(d["doc_ex_en"], target_en.parent).replace(".md", ".html")
        phase_title = PHASE_META[d['phase']]['en_title']
        search_str = f"{d['code']} {d['name_en']} {d['name_ar']} {phase_title} {d['tier']} PMI PMBOK".lower()

        catalog_en += f"""        <tr class="explorer-table-row" data-phase="{d['phase']}" data-tier="{d['tier']}" data-search="{search_str}">
          <td style="text-align: center;"><strong><code>{d['code']}</code></strong></td>
          <td><strong>{d['name_en']}</strong><br/><small style="color: var(--text-muted);">🇸🇦 {d['name_ar']}</small></td>
          <td>{phase_title}</td>
          <td><span class="badge badge-phase">{d['tier']}</span></td>
          <td style="text-align: center; white-space: nowrap;">
            <a class="card-action-link" href="{rel_tpl}">📋 Template</a>
            <a class="card-action-link" href="{rel_guide}">📖 Guide</a>
            <a class="card-action-link" href="{rel_ex}">💡 Example</a>
          </td>
        </tr>
"""

    catalog_en += """      </tbody>
    </table>
  </div>
</div>
"""

    target_en.write_text(catalog_en, encoding="utf-8")

    # 2. AR Master Catalog with Interactive Explorer
    target_ar = DOCS_DIR / "catalog/ar/index.md"
    target_ar.parent.mkdir(parents=True, exist_ok=True)
    rel_en_catalog = os.path.relpath(DOCS_DIR / "catalog/en/index.md", target_ar.parent).replace(".md", ".html")

    catalog_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> الفهرس العام باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/docs/catalog/ar" target="_blank" rel="noopener noreferrer">🐙 عرض على GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_en_catalog}">🇬🇧 Switch to English Catalog (الفهرس الإنجليزي) ←</a>
  </div>
</div>

# 📑 الفهرس العام والمستكشف التفاعلي للمخرجات والنماذج
**التوافق مع المعايير:** معهد إدارة المشاريع PMI PMBOK® الإصدارات 6 و 7 و 8 • أخلاقيات الذكاء الاصطناعي (سدايا) • ISO 21500  
**إجمالي المخرجات:** 102 مخرجاً إدارياً ثنائياً (204 قوالب قياسية • 204 أدلة إرشادية • 204 دراسات حالة وأمثلة واقعية)

---

<div id="tasleemat-explorer" class="explorer-wrapper" dir="rtl">
  <div class="explorer-toolbar">
    <input type="text" id="explorer-search" class="explorer-search-box" placeholder="🔍 بحث فوري بالرمز (مثل PMO-03.01)، الاسم، المرحلة، المستوى، أو الكلمات المفتاحية..." />
    
    <div class="explorer-filter-group">
      <span class="explorer-filter-label">المرحلة:</span>
      <button class="filter-chip filter-phase-btn active" data-phase="all">الكل (102)</button>
      <button class="filter-chip filter-phase-btn" data-phase="00">00. البرامج والمحافظ (6)</button>
      <button class="filter-chip filter-phase-btn" data-phase="01">01. الأعمال والقيمة (4)</button>
      <button class="filter-chip filter-phase-btn" data-phase="02">02. التخصيص والمنهجية (6)</button>
      <button class="filter-chip filter-phase-btn" data-phase="03">03. البدء (5)</button>
      <button class="filter-chip filter-phase-btn" data-phase="04">04. التخطيط (47)</button>
      <button class="filter-chip filter-phase-btn" data-phase="05">05. التنفيذ (12)</button>
      <button class="filter-chip filter-phase-btn" data-phase="06">06. المراقبة والتحكم (12)</button>
      <button class="filter-chip filter-phase-btn" data-phase="07">07. الإغلاق (5)</button>
    </div>

    <div class="explorer-filter-group">
      <span class="explorer-filter-label">مستوى الحوكمة:</span>
      <button class="filter-chip filter-tier-btn active" data-tier="all">كافة المستويات</button>
      <button class="filter-chip filter-tier-btn" data-tier="Tier 1">🔴 المستوى 1 (المشاريع الكبرى)</button>
      <button class="filter-chip filter-tier-btn" data-tier="Tier 2">🟡 المستوى 2 (المشاريع المتوسطة)</button>
      <button class="filter-chip filter-tier-btn" data-tier="Tier 3">🟢 المستوى 3 (المشاريع السريعة)</button>
      <button class="filter-chip filter-tier-btn" data-tier="Tier 4">🤖 المستوى 4 (الذكاء الاصطناعي)</button>
    </div>

    <div class="explorer-filter-group" style="justify-content: space-between; margin-top: 6px;">
      <span style="font-size: 0.86rem; color: var(--text-muted); font-weight: 600;">يتم عرض <span id="results-count" style="color: var(--brand-primary); font-weight: 800;">102</span> نموذجاً</span>
      <div style="display: flex; gap: 6px;">
        <button class="filter-chip view-toggle-btn active" data-view="cards">🗂️ عرض البطاقات</button>
        <button class="filter-chip view-toggle-btn" data-view="table">📊 عرض الجدول</button>
      </div>
    </div>
  </div>

  <div id="explorer-cards" class="explorer-grid-cards">
"""

    for d in deliverables:
        rel_tpl = os.path.relpath(d["doc_tpl_ar"], target_ar.parent).replace(".md", ".html")
        rel_guide = os.path.relpath(d["doc_guide_ar"], target_ar.parent).replace(".md", ".html")
        rel_ex = os.path.relpath(d["doc_ex_ar"], target_ar.parent).replace(".md", ".html")
        rel_en_tpl = os.path.relpath(d["doc_tpl_en"], target_ar.parent).replace(".md", ".html")
        phase_title = PHASE_META[d['phase']]['ar_title']

        search_str = f"{d['code']} {d['name_en']} {d['name_ar']} {phase_title} {d['tier']} ميثاق خطة سجل".lower()

        catalog_ar += f"""    <div class="explorer-card-item" data-phase="{d['phase']}" data-tier="{d['tier']}" data-search="{search_str}">
      <div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
          <span class="badge badge-code">{d['code']}</span>
          <span style="font-size: 0.74rem; color: var(--text-muted); font-weight: 600;">{d['tier']}</span>
        </div>
        <h5>{d['name_ar']}</h5>
        <div style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 4px;">🇬🇧 {d['name_en']}</div>
        <div style="font-size: 0.75rem; color: #0284c7; font-weight: 600;">{phase_title}</div>
      </div>
      <div class="explorer-card-actions">
        <a class="card-action-link" href="{rel_tpl}">📋 القالب</a>
        <a class="card-action-link" href="{rel_guide}">📖 الدليل</a>
        <a class="card-action-link" href="{rel_ex}">💡 مثال واقعي</a>
        <a class="card-action-link" style="background: rgba(56, 189, 248, 0.1); color: var(--color-ref) !important;" href="{rel_en_tpl}">🇬🇧 EN</a>
      </div>
    </div>
"""

    catalog_ar += """  </div>

  <div id="explorer-table" style="display: none; overflow-x: auto; margin-top: 16px;">
    <table>
      <thead>
        <tr>
          <th style="text-align: center;">الرمز</th>
          <th>اسم المخرج الإداري</th>
          <th>المرحلة / المجال</th>
          <th>مستوى الحوكمة</th>
          <th style="text-align: center;">الإجراءات والروابط</th>
        </tr>
      </thead>
      <tbody>
"""

    for d in deliverables:
        rel_tpl = os.path.relpath(d["doc_tpl_ar"], target_ar.parent).replace(".md", ".html")
        rel_guide = os.path.relpath(d["doc_guide_ar"], target_ar.parent).replace(".md", ".html")
        rel_ex = os.path.relpath(d["doc_ex_ar"], target_ar.parent).replace(".md", ".html")
        phase_title = PHASE_META[d['phase']]['ar_title']
        search_str = f"{d['code']} {d['name_en']} {d['name_ar']} {phase_title} {d['tier']}".lower()

        catalog_ar += f"""        <tr class="explorer-table-row" data-phase="{d['phase']}" data-tier="{d['tier']}" data-search="{search_str}">
          <td style="text-align: center;"><strong><code>{d['code']}</code></strong></td>
          <td><strong>{d['name_ar']}</strong><br/><small style="color: var(--text-muted);">🇬🇧 {d['name_en']}</small></td>
          <td>{phase_title}</td>
          <td><span class="badge badge-phase">{d['tier']}</span></td>
          <td style="text-align: center; white-space: nowrap;">
            <a class="card-action-link" href="{rel_tpl}">📋 القالب</a>
            <a class="card-action-link" href="{rel_guide}">📖 الدليل</a>
            <a class="card-action-link" href="{rel_ex}">💡 المثال</a>
          </td>
        </tr>
"""

    catalog_ar += """      </tbody>
    </table>
  </div>
</div>
"""

    target_ar.write_text(catalog_ar, encoding="utf-8")

def build_section_indexes(deliverables):
    """Build root index pages for templates, guides, and examples with cross-language switches."""
    # 1. EN Templates Index
    target_tpl_en = DOCS_DIR / "forms/en/index.md"
    target_tpl_en.parent.mkdir(parents=True, exist_ok=True)
    rel_ar_tpl_idx = os.path.relpath(DOCS_DIR / "forms/ar/index.md", target_tpl_en.parent).replace(".md", ".html")
    tpl_idx_en = f"""<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/forms/en" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="lang-switch-btn" href="{rel_ar_tpl_idx}">🇸🇦 الانتقال لفهرس القوالب بالعربية (Arabic Templates) →</a>
  </div>
</div>

# 📋 Tasleemat Templates Library (English)
**Standardized, Copy-Ready Markdown Deliverable Templates** aligned with PMI PMBOK® 6th, 7th & 8th Editions.

---

## 🧭 Browse Templates by Lifecycle Phase

"""
    for p_code, p_info in sorted(PHASE_META.items()):
        p_items = [d for d in deliverables if d["phase"] == p_code]
        tpl_idx_en += f"### {p_info['icon']} {p_info['en_title']} ({len(p_items)} Templates)\n\n"
        tpl_idx_en += f"{p_info['en_desc']}\n\n"
        tpl_idx_en += "| Code | Template Name | Links |\n| :---: | :--- | :---: |\n"
        for d in p_items:
            rel_t = os.path.relpath(d["doc_tpl_en"], target_tpl_en.parent)
            rel_g = os.path.relpath(d["doc_guide_en"], target_tpl_en.parent)
            rel_e = os.path.relpath(d["doc_ex_en"], target_tpl_en.parent)
            tpl_idx_en += f"| **`{d['code']}`** | [**{d['name_en']}**]({rel_t}) | [📖 Guide]({rel_g}) • [💡 Example]({rel_e}) |\n"
        tpl_idx_en += "\n---\n\n"

    target_tpl_en.write_text(tpl_idx_en, encoding="utf-8")

    # 2. AR Templates Index
    target_tpl_ar = DOCS_DIR / "forms/ar/index.md"
    target_tpl_ar.parent.mkdir(parents=True, exist_ok=True)
    rel_en_tpl_idx = os.path.relpath(DOCS_DIR / "forms/en/index.md", target_tpl_ar.parent).replace(".md", ".html")
    tpl_idx_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> التوثيق باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/forms/ar" target="_blank" rel="noopener noreferrer">🐙 مصدر GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_en_tpl_idx}">🇬🇧 Switch to English Templates (قوالب إنجليزية) ←</a>
  </div>
</div>

# 📋 مكتبة قوالب ونماذج تسليمات (بالعربية)
**قوالب عمل قياسية جاهزة للاستخدام بصيغة Markdown** متوافقة مع معايير معهد إدارة المشاريع PMI PMBOK®.

---

## 🧭 تصفح القوالب حسب مراحل دورة حياة المشروع

"""
    for p_code, p_info in sorted(PHASE_META.items()):
        p_items = [d for d in deliverables if d["phase"] == p_code]
        tpl_idx_ar += f"### {p_info['icon']} {p_info['ar_title']} ({len(p_items)} نموذجاً)\n\n"
        tpl_idx_ar += f"{p_info['ar_desc']}\n\n"
        tpl_idx_ar += "| الرمز | اسم القالب | الروابط |\n| :---: | :--- | :---: |\n"
        for d in p_items:
            rel_t = os.path.relpath(d["doc_tpl_ar"], target_tpl_ar.parent)
            rel_g = os.path.relpath(d["doc_guide_ar"], target_tpl_ar.parent)
            rel_e = os.path.relpath(d["doc_ex_ar"], target_tpl_ar.parent)
            tpl_idx_ar += f"| **`{d['code']}`** | [**{d['name_ar']}**]({rel_t}) | [📖 الدليل]({rel_g}) • [💡 المثال]({rel_e}) |\n"
        tpl_idx_ar += "\n---\n\n"

    target_tpl_ar.write_text(tpl_idx_ar, encoding="utf-8")

    # 3. EN Guides Index
    target_g_en = DOCS_DIR / "guides/en/index.md"
    target_g_en.parent.mkdir(parents=True, exist_ok=True)
    rel_ar_g_idx = os.path.relpath(DOCS_DIR / "guides/ar/index.md", target_g_en.parent).replace(".md", ".html")
    guides_idx_en = f"""<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/forms/en" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="lang-switch-btn" href="{rel_ar_g_idx}">🇸🇦 الانتقال لأدلة النماذج بالعربية (Arabic Guides) →</a>
  </div>
</div>

# 📖 Deliverable Authoring & Governance Guides (English)
**Step-by-step instructions, RACI authority assignments, required inputs, and stage-gate acceptance criteria for all 102 deliverables.**

---

## 🧭 Browse Authoring Guides by Phase

"""
    for p_code, p_info in sorted(PHASE_META.items()):
        p_items = [d for d in deliverables if d["phase"] == p_code]
        guides_idx_en += f"### {p_info['icon']} {p_info['en_title']} ({len(p_items)} Guides)\n\n"
        guides_idx_en += "| Code | Guide Title | Links |\n| :---: | :--- | :---: |\n"
        for d in p_items:
            rel_g = os.path.relpath(d["doc_guide_en"], target_g_en.parent)
            rel_t = os.path.relpath(d["doc_tpl_en"], target_g_en.parent)
            rel_e = os.path.relpath(d["doc_ex_en"], target_g_en.parent)
            guides_idx_en += f"| **`{d['code']}`** | [**{d['name_en']} Guide**]({rel_g}) | [📋 Template]({rel_t}) • [💡 Example]({rel_e}) |\n"
        guides_idx_en += "\n---\n\n"

    target_g_en.write_text(guides_idx_en, encoding="utf-8")

    # 4. AR Guides Index
    target_g_ar = DOCS_DIR / "guides/ar/index.md"
    target_g_ar.parent.mkdir(parents=True, exist_ok=True)
    rel_en_g_idx = os.path.relpath(DOCS_DIR / "guides/en/index.md", target_g_ar.parent).replace(".md", ".html")
    guides_idx_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> التوثيق باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/forms/ar" target="_blank" rel="noopener noreferrer">🐙 مصدر GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_en_g_idx}">🇬🇧 Switch to English Guides (أدلة إنجليزية) ←</a>
  </div>
</div>

# 📖 أدلة إعداد وتعبئة النماذج (بالعربية)
**إرشادات خطوة بخطوة، مصفوفة الصلاحيات RACI، المدخلات والمخرجات المطلوبة، ومعايير القبول والاعتماد.**

---

## 🧭 تصفح الأدلة الإرشادية حسب المرحلة

"""
    for p_code, p_info in sorted(PHASE_META.items()):
        p_items = [d for d in deliverables if d["phase"] == p_code]
        guides_idx_ar += f"### {p_info['icon']} {p_info['ar_title']} ({len(p_items)} دليلاً)\n\n"
        guides_idx_ar += "| الرمز | عنوان الدليل | الروابط |\n| :---: | :--- | :---: |\n"
        for d in p_items:
            rel_g = os.path.relpath(d["doc_guide_ar"], target_g_ar.parent)
            rel_t = os.path.relpath(d["doc_tpl_ar"], target_g_ar.parent)
            rel_e = os.path.relpath(d["doc_ex_ar"], target_g_ar.parent)
            guides_idx_ar += f"| **`{d['code']}`** | [**دليل {d['name_ar']}**]({rel_g}) | [📋 القالب]({rel_t}) • [💡 المثال]({rel_e}) |\n"
        guides_idx_ar += "\n---\n\n"

    target_g_ar.write_text(guides_idx_ar, encoding="utf-8")

    # 5. EN Examples Index
    target_ex_en = DOCS_DIR / "examples/en/index.md"
    target_ex_en.parent.mkdir(parents=True, exist_ok=True)
    rel_ar_ex_idx = os.path.relpath(DOCS_DIR / "examples/ar/index.md", target_ex_en.parent).replace(".md", ".html")
    ex_idx_en = f"""<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/examples/en" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="lang-switch-btn" href="{rel_ar_ex_idx}">🇸🇦 الانتقال للأمثلة الواقعية بالعربية (Arabic Examples) →</a>
  </div>
</div>

# 💡 Reference Examples & Case Studies Showcase (English)
**102 fully populated, realistic enterprise case study examples** showcasing best practice completion across all lifecycle phases.

---

## 🧭 Browse Case Studies by Phase

"""
    for p_code, p_info in sorted(PHASE_META.items()):
        p_items = [d for d in deliverables if d["phase"] == p_code]
        ex_idx_en += f"### {p_info['icon']} {p_info['en_title']} ({len(p_items)} Examples)\n\n"
        ex_idx_en += "| Code | Completed Case Study | Links |\n| :---: | :--- | :---: |\n"
        for d in p_items:
            rel_e = os.path.relpath(d["doc_ex_en"], target_ex_en.parent)
            rel_t = os.path.relpath(d["doc_tpl_en"], target_ex_en.parent)
            rel_g = os.path.relpath(d["doc_guide_en"], target_ex_en.parent)
            ex_idx_en += f"| **`{d['code']}`** | [**{d['name_en']} Example**]({rel_e}) | [📋 Template]({rel_t}) • [📖 Guide]({rel_g}) |\n"
        ex_idx_en += "\n---\n\n"

    target_ex_en.write_text(ex_idx_en, encoding="utf-8")

    # 6. AR Examples Index
    target_ex_ar = DOCS_DIR / "examples/ar/index.md"
    target_ex_ar.parent.mkdir(parents=True, exist_ok=True)
    rel_en_ex_idx = os.path.relpath(DOCS_DIR / "examples/en/index.md", target_ex_ar.parent).replace(".md", ".html")
    ex_idx_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> التوثيق باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/examples/ar" target="_blank" rel="noopener noreferrer">🐙 مصدر GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_en_ex_idx}">🇬🇧 Switch to English Examples (أمثلة إنجليزية) ←</a>
  </div>
</div>

# 💡 معرض الأمثلة الواقعية ودراسات الحالة (بالعربية)
**102 مثال واقعي مكتمل ومعتمد** يغطي دراسات حالة تطبيقية نموذجية لكافة مخرجات دورة حياة المشروع.

---

## 🧭 تصفح دراسات الحالة والأمثلة حسب المرحلة

"""
    for p_code, p_info in sorted(PHASE_META.items()):
        p_items = [d for d in deliverables if d["phase"] == p_code]
        ex_idx_ar += f"### {p_info['icon']} {p_info['ar_title']} ({len(p_items)} مثالاً واقعياً)\n\n"
        ex_idx_ar += "| الرمز | دراسة الحالة المكتملة | الروابط |\n| :---: | :--- | :---: |\n"
        for d in p_items:
            rel_e = os.path.relpath(d["doc_ex_ar"], target_ex_ar.parent)
            rel_t = os.path.relpath(d["doc_tpl_ar"], target_ex_ar.parent)
            rel_g = os.path.relpath(d["doc_guide_ar"], target_ex_ar.parent)
            ex_idx_ar += f"| **`{d['code']}`** | [**مثال {d['name_ar']}**]({rel_e}) | [📋 القالب]({rel_t}) • [📖 الدليل]({rel_g}) |\n"
        ex_idx_ar += "\n---\n\n"

    target_ex_ar.write_text(ex_idx_ar, encoding="utf-8")

def build_phase_indexes(deliverables):
    """Build individual phase index pages inside each phase folder for templates, guides, and examples."""
    for p_code, p_info in PHASE_META.items():
        p_items = [d for d in deliverables if d["phase"] == p_code]
        if not p_items:
            continue
        
        phase_dir_en = p_items[0]["dest_dir_en"].parts[0]
        phase_dir_ar = p_items[0]["dest_dir_ar"].parts[0]

        # 1. Templates Phase Index (EN)
        target_t_en = DOCS_DIR / "forms" / "en" / phase_dir_en / "index.md"
        target_t_en.parent.mkdir(parents=True, exist_ok=True)
        rel_ar_phase_tpl = os.path.relpath(DOCS_DIR / "forms" / "ar" / phase_dir_ar / "index.md", target_t_en.parent).replace(".md", ".html")
        idx_content_en = f"""<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/forms/en/{phase_dir_en}" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="lang-switch-btn" href="{rel_ar_phase_tpl}">🇸🇦 الانتقال لقوالب المرحلة بالعربية (Arabic Templates) →</a>
  </div>
</div>

# {p_info['icon']} {p_info['en_title']} (Templates)
{p_info['en_desc']}

---

## 📑 Phase Templates ({len(p_items)} Artifacts)

| Code | Deliverable Name | Template | Guide | Completed Example |
| :---: | :--- | :---: | :---: | :---: |
"""
        for d in p_items:
            rel_t = os.path.relpath(d["doc_tpl_en"], target_t_en.parent)
            rel_g = os.path.relpath(d["doc_guide_en"], target_t_en.parent)
            rel_e = os.path.relpath(d["doc_ex_en"], target_t_en.parent)
            idx_content_en += f"| **`{d['code']}`** | **{d['name_en']}** | [📋 Template]({rel_t}) | [📖 Guide]({rel_g}) | [💡 Example]({rel_e}) |\n"
        target_t_en.write_text(idx_content_en, encoding="utf-8")

        # 2. Templates Phase Index (AR)
        target_t_ar = DOCS_DIR / "forms" / "ar" / phase_dir_ar / "index.md"
        target_t_ar.parent.mkdir(parents=True, exist_ok=True)
        rel_en_phase_tpl = os.path.relpath(DOCS_DIR / "forms" / "en" / phase_dir_en / "index.md", target_t_ar.parent).replace(".md", ".html")
        idx_content_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> التوثيق باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/forms/ar/{phase_dir_ar}" target="_blank" rel="noopener noreferrer">🐙 مصدر GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_en_phase_tpl}">🇬🇧 Switch to English Templates (قوالب إنجليزية) ←</a>
  </div>
</div>

# {p_info['icon']} {p_info['ar_title']} (القوالب)
{p_info['ar_desc']}

---

## 📑 قوالب المرحلة ({len(p_items)} نموذجاً)

| الرمز | اسم المخرج الإداري | القالب | الدليل الإرشادي | مثال واقعي |
| :---: | :--- | :---: | :---: | :---: |
"""
        for d in p_items:
            rel_t = os.path.relpath(d["doc_tpl_ar"], target_t_ar.parent)
            rel_g = os.path.relpath(d["doc_guide_ar"], target_t_ar.parent)
            rel_e = os.path.relpath(d["doc_ex_ar"], target_t_ar.parent)
            idx_content_ar += f"| **`{d['code']}`** | **{d['name_ar']}** | [📋 القالب]({rel_t}) | [📖 الدليل]({rel_g}) | [💡 المثال]({rel_e}) |\n"
        target_t_ar.write_text(idx_content_ar, encoding="utf-8")

        # 3. Guides Phase Index (EN)
        target_g_en = DOCS_DIR / "guides" / "en" / phase_dir_en / "index.md"
        target_g_en.parent.mkdir(parents=True, exist_ok=True)
        rel_ar_phase_g = os.path.relpath(DOCS_DIR / "guides" / "ar" / phase_dir_ar / "index.md", target_g_en.parent).replace(".md", ".html")
        g_content_en = f"""<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/forms/en/{phase_dir_en}" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="lang-switch-btn" href="{rel_ar_phase_g}">🇸🇦 الانتقال لأدلة المرحلة بالعربية (Arabic Guides) →</a>
  </div>
</div>

# {p_info['icon']} {p_info['en_title']} (Authoring Guides)
{p_info['en_desc']}

---

## 📖 Phase Authoring Guides ({len(p_items)} Guides)

| Code | Guide Title | Template | Guide | Completed Example |
| :---: | :--- | :---: | :---: | :---: |
"""
        for d in p_items:
            rel_t = os.path.relpath(d["doc_tpl_en"], target_g_en.parent)
            rel_g = os.path.relpath(d["doc_guide_en"], target_g_en.parent)
            rel_e = os.path.relpath(d["doc_ex_en"], target_g_en.parent)
            g_content_en += f"| **`{d['code']}`** | **{d['name_en']}** | [📋 Template]({rel_t}) | [📖 Guide]({rel_g}) | [💡 Example]({rel_e}) |\n"
        target_g_en.write_text(g_content_en, encoding="utf-8")

        # 4. Guides Phase Index (AR)
        target_g_ar = DOCS_DIR / "guides" / "ar" / phase_dir_ar / "index.md"
        target_g_ar.parent.mkdir(parents=True, exist_ok=True)
        rel_en_phase_g = os.path.relpath(DOCS_DIR / "guides" / "en" / phase_dir_en / "index.md", target_g_ar.parent).replace(".md", ".html")
        g_content_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> التوثيق باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/forms/ar/{phase_dir_ar}" target="_blank" rel="noopener noreferrer">🐙 مصدر GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_en_phase_g}">🇬🇧 Switch to English Guides (أدلة إنجليزية) ←</a>
  </div>
</div>

# {p_info['icon']} {p_info['ar_title']} (الأدلة الإرشادية)
{p_info['ar_desc']}

---

## 📖 أدلة المرحلة ({len(p_items)} دليلاً)

| الرمز | عنوان الدليل | القالب | الدليل الإرشادي | مثال واقعي |
| :---: | :--- | :---: | :---: | :---: |
"""
        for d in p_items:
            rel_t = os.path.relpath(d["doc_tpl_ar"], target_g_ar.parent)
            rel_g = os.path.relpath(d["doc_guide_ar"], target_g_ar.parent)
            rel_e = os.path.relpath(d["doc_ex_ar"], target_g_ar.parent)
            g_content_ar += f"| **`{d['code']}`** | **{d['name_ar']}** | [📋 القالب]({rel_t}) | [📖 الدليل]({rel_g}) | [💡 المثال]({rel_e}) |\n"
        target_g_ar.write_text(g_content_ar, encoding="utf-8")

        # 5. Examples Phase Index (EN)
        target_e_en = DOCS_DIR / "examples" / "en" / phase_dir_en / "index.md"
        target_e_en.parent.mkdir(parents=True, exist_ok=True)
        rel_ar_phase_e = os.path.relpath(DOCS_DIR / "examples" / "ar" / phase_dir_ar / "index.md", target_e_en.parent).replace(".md", ".html")
        e_content_en = f"""<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/examples/en/{phase_dir_en}" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="lang-switch-btn" href="{rel_ar_phase_e}">🇸🇦 الانتقال لأمثلة المرحلة بالعربية (Arabic Examples) →</a>
  </div>
</div>

# {p_info['icon']} {p_info['en_title']} (Reference Examples)
{p_info['en_desc']}

---

## 💡 Phase Case Studies ({len(p_items)} Examples)

| Code | Case Study Title | Template | Guide | Completed Example |
| :---: | :--- | :---: | :---: | :---: |
"""
        for d in p_items:
            rel_t = os.path.relpath(d["doc_tpl_en"], target_e_en.parent)
            rel_g = os.path.relpath(d["doc_guide_en"], target_e_en.parent)
            rel_e = os.path.relpath(d["doc_ex_en"], target_e_en.parent)
            e_content_en += f"| **`{d['code']}`** | **{d['name_en']}** | [📋 Template]({rel_t}) | [📖 Guide]({rel_g}) | [💡 Example]({rel_e}) |\n"
        target_e_en.write_text(e_content_en, encoding="utf-8")

        # 6. Examples Phase Index (AR)
        target_e_ar = DOCS_DIR / "examples" / "ar" / phase_dir_ar / "index.md"
        target_e_ar.parent.mkdir(parents=True, exist_ok=True)
        rel_en_phase_e = os.path.relpath(DOCS_DIR / "examples" / "en" / phase_dir_en / "index.md", target_e_ar.parent).replace(".md", ".html")
        e_content_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> التوثيق باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/tree/main/examples/ar/{phase_dir_ar}" target="_blank" rel="noopener noreferrer">🐙 مصدر GitHub ↗</a>
    <a class="lang-switch-btn" href="{rel_en_phase_e}">🇬🇧 Switch to English Examples (أمثلة إنجليزية) ←</a>
  </div>
</div>

# {p_info['icon']} {p_info['ar_title']} (الأمثلة الواقعية)
{p_info['ar_desc']}

---

## 💡 أمثلة ودراسات حالة المرحلة ({len(p_items)} مثالاً)

| الرمز | اسم المخرج / دراسة الحالة | القالب | الدليل الإرشادي | مثال واقعي |
| :---: | :--- | :---: | :---: | :---: |
"""
        for d in p_items:
            rel_t = os.path.relpath(d["doc_tpl_ar"], target_e_ar.parent)
            rel_g = os.path.relpath(d["doc_guide_ar"], target_e_ar.parent)
            rel_e = os.path.relpath(d["doc_ex_ar"], target_e_ar.parent)
            e_content_ar += f"| **`{d['code']}`** | **{d['name_ar']}** | [📋 القالب]({rel_t}) | [📖 الدليل]({rel_g}) | [💡 المثال]({rel_e}) |\n"
        target_e_ar.write_text(e_content_ar, encoding="utf-8")

def update_mkdocs_config(deliverables):
    """Update mkdocs.yml with sleek, streamlined 3-tab top navigation and use_directory_urls: false."""
    mkdocs_file = ROOT / "mkdocs.yml"

    def make_phase_nav_en(phase_prefix, section_type="templates"):
        items = [d for d in deliverables if d["phase"] == phase_prefix]
        nav_list = []
        
        if phase_prefix == "04":
            sub_groups = {}
            for d in items:
                sub_name = d["dest_dir_en"].parts[1]
                if sub_name not in sub_groups:
                    sub_groups[sub_name] = []
                sub_groups[sub_name].append(d)
            
            for sub_k in sorted(sub_groups.keys()):
                sub_title = PLANNING_SUBS.get(sub_k, (sub_k.replace("_", " "), ""))[0]
                sub_items = []
                for d in sub_groups[sub_k]:
                    if section_type == "forms":
                        target = os.path.relpath(d["doc_tpl_en"], DOCS_DIR)
                    elif section_type == "guides":
                        target = os.path.relpath(d["doc_guide_en"], DOCS_DIR)
                    else:
                        target = os.path.relpath(d["doc_ex_en"], DOCS_DIR)
                    sub_items.append({f"{d['code']} {d['name_en']}": target})
                nav_list.append({sub_title: sub_items})
        else:
            for d in items:
                if section_type == "forms":
                    target = os.path.relpath(d["doc_tpl_en"], DOCS_DIR)
                elif section_type == "guides":
                    target = os.path.relpath(d["doc_guide_en"], DOCS_DIR)
                else:
                    target = os.path.relpath(d["doc_ex_en"], DOCS_DIR)
                nav_list.append({f"{d['code']} {d['name_en']}": target})
        return nav_list

    def make_phase_nav_ar(phase_prefix, section_type="templates"):
        items = [d for d in deliverables if d["phase"] == phase_prefix]
        nav_list = []
        
        if phase_prefix == "04":
            sub_groups = {}
            for d in items:
                sub_name = d["dest_dir_ar"].parts[1]
                if sub_name not in sub_groups:
                    sub_groups[sub_name] = []
                sub_groups[sub_name].append(d)
            
            for sub_k in sorted(sub_groups.keys()):
                en_match = [k for k in PLANNING_SUBS.keys() if k[:2] == sub_k[:2]]
                sub_title = PLANNING_SUBS[en_match[0]][1] if en_match else sub_k.replace("_", " ")
                sub_items = []
                for d in sub_groups[sub_k]:
                    if section_type == "forms":
                        target = os.path.relpath(d["doc_tpl_ar"], DOCS_DIR)
                    elif section_type == "guides":
                        target = os.path.relpath(d["doc_guide_ar"], DOCS_DIR)
                    else:
                        target = os.path.relpath(d["doc_ex_ar"], DOCS_DIR)
                    sub_items.append({f"{d['code']} {d['name_ar']}": target})
                nav_list.append({sub_title: sub_items})
        else:
            for d in items:
                if section_type == "forms":
                    target = os.path.relpath(d["doc_tpl_ar"], DOCS_DIR)
                elif section_type == "guides":
                    target = os.path.relpath(d["doc_guide_ar"], DOCS_DIR)
                else:
                    target = os.path.relpath(d["doc_ex_ar"], DOCS_DIR)
                nav_list.append({f"{d['code']} {d['name_ar']}": target})
        return nav_list

    # Streamlined 3-Tab Architecture
    nav = [
        # === 🇬🇧 ENGLISH PORTAL TAB ===
        {"🇬🇧 English Portal": [
            {"Home & Overview": "index.md"},
            {"📑 Interactive Master Catalog": "catalog/en/index.md"},
            {"📚 PMO Governance Manuals (01-12)": [
                {"01. Getting Started": "en/01_getting_started.md"},
                {"02. Usage Guide": "en/02_usage_guide.md"},
                {"03. PMO Policy Manual": "en/03_pmo_policy_manual.md"},
                {"04. Stage-Gates & Governance": "en/04_stage_gates_and_governance.md"},
                {"05. Tailoring Profiles": "en/05_tailoring_profiles.md"},
                {"06. RACI Authority Matrix": "en/06_raci_authority_matrix.md"},
                {"07. Document Dependencies": "en/07_document_dependencies.md"},
                {"08. AI Governance Framework": "en/08_ai_governance_framework.md"},
                {"09. Agile & Hybrid Integration": "en/09_agile_hybrid_integration.md"},
                {"10. FAQ & Troubleshooting": "en/10_faq_and_troubleshooting.md"},
                {"11. Tools & Automation": "en/11_tools_and_automation.md"},
                {"12. Open Knowledge Framework (OKF)": "en/12_open_knowledge_framework.md"}
            ]},
            {"📋 Standard Templates Library": [
                {"Templates Overview": "forms/en/index.md"},
                {PHASE_META["00"]["en_title"]: make_phase_nav_en("00", "forms")},
                {PHASE_META["01"]["en_title"]: make_phase_nav_en("01", "forms")},
                {PHASE_META["02"]["en_title"]: make_phase_nav_en("02", "forms")},
                {PHASE_META["03"]["en_title"]: make_phase_nav_en("03", "forms")},
                {PHASE_META["04"]["en_title"]: make_phase_nav_en("04", "forms")},
                {PHASE_META["05"]["en_title"]: make_phase_nav_en("05", "forms")},
                {PHASE_META["06"]["en_title"]: make_phase_nav_en("06", "forms")},
                {PHASE_META["07"]["en_title"]: make_phase_nav_en("07", "forms")}
            ]},
            {"📖 Deliverable Authoring Guides": [
                {"Guides Overview": "guides/en/index.md"},
                {PHASE_META["00"]["en_title"]: make_phase_nav_en("00", "guides")},
                {PHASE_META["01"]["en_title"]: make_phase_nav_en("01", "guides")},
                {PHASE_META["02"]["en_title"]: make_phase_nav_en("02", "guides")},
                {PHASE_META["03"]["en_title"]: make_phase_nav_en("03", "guides")},
                {PHASE_META["04"]["en_title"]: make_phase_nav_en("04", "guides")},
                {PHASE_META["05"]["en_title"]: make_phase_nav_en("05", "guides")},
                {PHASE_META["06"]["en_title"]: make_phase_nav_en("06", "guides")},
                {PHASE_META["07"]["en_title"]: make_phase_nav_en("07", "guides")}
            ]},
            {"💡 Real-World Reference Examples": [
                {"Case Studies Showcase": "examples/en/index.md"},
                {PHASE_META["00"]["en_title"]: make_phase_nav_en("00", "examples")},
                {PHASE_META["01"]["en_title"]: make_phase_nav_en("01", "examples")},
                {PHASE_META["02"]["en_title"]: make_phase_nav_en("02", "examples")},
                {PHASE_META["03"]["en_title"]: make_phase_nav_en("03", "examples")},
                {PHASE_META["04"]["en_title"]: make_phase_nav_en("04", "examples")},
                {PHASE_META["05"]["en_title"]: make_phase_nav_en("05", "examples")},
                {PHASE_META["06"]["en_title"]: make_phase_nav_en("06", "examples")},
                {PHASE_META["07"]["en_title"]: make_phase_nav_en("07", "examples")}
            ]}
        ]},

        # === 🇸🇦 ARABIC PORTAL TAB ===
        {"🇸🇦 البوابة التوثيقية (Arabic)": [
            {"الرئيسية ودليل الانطلاق": "README_AR.md"},
            {"📑 الفهرس التفاعلي الشامل": "catalog/ar/index.md"},
            {"📚 الأدلة والسياسات الحوكمية (01-12)": [
                {"01. دليل البدء السريع": "ar/01_getting_started.md"},
                {"02. دليل الممارس الشامل": "ar/02_usage_guide.md"},
                {"03. دليل سياسات PMO": "ar/03_pmo_policy_manual.md"},
                {"04. بوابات العبور والمراجعات": "ar/04_stage_gates_and_governance.md"},
                {"05. ملفات التخصيص وتصنيف المشاريع": "ar/05_tailoring_profiles.md"},
                {"06. مصفوفة الصلاحيات RACI": "ar/06_raci_authority_matrix.md"},
                {"07. شبكة اعتماديات الوثائق": "ar/07_document_dependencies.md"},
                {"08. إطار حوكمة الذكاء الاصطناعي": "ar/08_ai_governance_framework.md"},
                {"09. دليل المنهجيات الرشيقة والهجينة": "ar/09_agile_hybrid_integration.md"},
                {"10. الأسئلة الشائعة وحل المشكلات": "ar/10_faq_and_troubleshooting.md"},
                {"11. دليل الأدوات والأتمتة": "ar/11_tools_and_automation.md"},
                {"12. معيار مؤسسة المعرفة المفتوحة (OKF)": "ar/12_open_knowledge_framework.md"}
            ]},
            {"📋 مكتبة القوالب والنماذج": [
                {"الفهرس العام للقوالب": "forms/ar/index.md"},
                {PHASE_META["00"]["ar_title"]: make_phase_nav_ar("00", "forms")},
                {PHASE_META["01"]["ar_title"]: make_phase_nav_ar("01", "forms")},
                {PHASE_META["02"]["ar_title"]: make_phase_nav_ar("02", "forms")},
                {PHASE_META["03"]["ar_title"]: make_phase_nav_ar("03", "forms")},
                {PHASE_META["04"]["ar_title"]: make_phase_nav_ar("04", "forms")},
                {PHASE_META["05"]["ar_title"]: make_phase_nav_ar("05", "forms")},
                {PHASE_META["06"]["ar_title"]: make_phase_nav_ar("06", "forms")},
                {PHASE_META["07"]["ar_title"]: make_phase_nav_ar("07", "forms")}
            ]},
            {"📖 أدلة إعداد النماذج": [
                {"الفهرس العام للأدلة": "guides/ar/index.md"},
                {PHASE_META["00"]["ar_title"]: make_phase_nav_ar("00", "guides")},
                {PHASE_META["01"]["ar_title"]: make_phase_nav_ar("01", "guides")},
                {PHASE_META["02"]["ar_title"]: make_phase_nav_ar("02", "guides")},
                {PHASE_META["03"]["ar_title"]: make_phase_nav_ar("03", "guides")},
                {PHASE_META["04"]["ar_title"]: make_phase_nav_ar("04", "guides")},
                {PHASE_META["05"]["ar_title"]: make_phase_nav_ar("05", "guides")},
                {PHASE_META["06"]["ar_title"]: make_phase_nav_ar("06", "guides")},
                {PHASE_META["07"]["ar_title"]: make_phase_nav_ar("07", "guides")}
            ]},
            {"💡 معرض الأمثلة الواقعية": [
                {"معرض دراسات الحالة": "examples/ar/index.md"},
                {PHASE_META["00"]["ar_title"]: make_phase_nav_ar("00", "examples")},
                {PHASE_META["01"]["ar_title"]: make_phase_nav_ar("01", "examples")},
                {PHASE_META["02"]["ar_title"]: make_phase_nav_ar("02", "examples")},
                {PHASE_META["03"]["ar_title"]: make_phase_nav_ar("03", "examples")},
                {PHASE_META["04"]["ar_title"]: make_phase_nav_ar("04", "examples")},
                {PHASE_META["05"]["ar_title"]: make_phase_nav_ar("05", "examples")},
                {PHASE_META["06"]["ar_title"]: make_phase_nav_ar("06", "examples")},
                {PHASE_META["07"]["ar_title"]: make_phase_nav_ar("07", "examples")}
            ]}
        ]},

        # === 📖 BILINGUAL LEXICON TAB ===
        {"📖 Master Bilingual Lexicon": "LEXICON.md"}
    ]

    header_yaml = """site_name: Tasleemat PMO Operating System | تسليمات
site_url: https://fakhr.me/Tasleemat/
site_description: Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Automation Library aligned with PMI PMBOK® 6th, 7th & 8th Edition standards.
site_author: Fakhruldeen & Tasleemat Contributors
repo_url: https://github.com/fakhruldeen/Tasleemat
repo_name: fakhruldeen/Tasleemat
docs_dir: docs
use_directory_urls: false

theme:
  name: material
  language: en
  palette:
    # Dark mode (PMOSkills Obsidian Default)
    - scheme: slate
      primary: slate
      accent: cyan
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
    # Light mode (Clean Professional Theme)
    - scheme: default
      primary: white
      accent: indigo
      toggle:
        icon: material/weather-night
        name: Switch to dark mode
  features:
    - navigation.sections
    - navigation.expand
    - navigation.top
    - navigation.tracking
    - navigation.path
    - navigation.indexes
    - search.suggest
    - search.highlight
    - search.share
    - content.code.copy
    - content.code.annotate
    - content.tabs.link
    - content.tooltips
  logo: img/logo.png
  favicon: img/logo.png

extra_css:
  - assets/custom.css
  - https://unpkg.com/katex@0/dist/katex.min.css

extra_javascript:
  - assets/tasleemat_data.js
  - assets/explorer.js
  - assets/katex.js
  - https://unpkg.com/katex@0/dist/katex.min.js
  - https://unpkg.com/katex@0/dist/contrib/auto-render.min.js

plugins:
  - search

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.arithmatex:
      generic: true
  - tables
  - attr_list
  - md_in_html
"""

    nav_yaml = yaml.dump({"nav": nav}, allow_unicode=True, sort_keys=False, default_flow_style=False)
    mkdocs_file.write_text(header_yaml.strip() + "\n\n" + nav_yaml + "\n", encoding="utf-8")
    print("mkdocs.yml navigation updated successfully.")

def generate_tasleemat_data_js(deliverables):
    """Generate docs/assets/tasleemat_data.js containing full client-side bundles for all 102 deliverables."""
    data_list = []
    for d in deliverables:
        tpl_en = d["tpl_en"].read_text(encoding="utf-8") if d["tpl_en"] and d["tpl_en"].exists() else ""
        tpl_ar = d["tpl_ar"].read_text(encoding="utf-8") if d["tpl_ar"] and d["tpl_ar"].exists() else ""
        guide_en = d["guide_en"].read_text(encoding="utf-8") if d["guide_en"] and d["guide_en"].exists() else ""
        guide_ar = d["guide_ar"].read_text(encoding="utf-8") if d["guide_ar"] and d["guide_ar"].exists() else ""
        ex_en = d["ex_en"].read_text(encoding="utf-8") if d["ex_en"] and d["ex_en"].exists() else ""
        ex_ar = d["ex_ar"].read_text(encoding="utf-8") if d["ex_ar"] and d["ex_ar"].exists() else ""
        prompt_en = d["prompt_en"].read_text(encoding="utf-8") if d["prompt_en"] and d["prompt_en"].exists() else ""
        prompt_ar = d["prompt_ar"].read_text(encoding="utf-8") if d["prompt_ar"] and d["prompt_ar"].exists() else ""
        json_en = d["json_en"].read_text(encoding="utf-8") if d["json_en"] and d["json_en"].exists() else ""
        json_ar = d["json_ar"].read_text(encoding="utf-8") if d["json_ar"] and d["json_ar"].exists() else ""
        csv_en = d["csv_en"].read_text(encoding="utf-8") if d["csv_en"] and d["csv_en"].exists() else ""
        csv_ar = d["csv_ar"].read_text(encoding="utf-8") if d["csv_ar"] and d["csv_ar"].exists() else ""

        rel_tpl_en = os.path.relpath(d["doc_tpl_en"], DOCS_DIR).replace(".md", ".html")
        rel_tpl_ar = os.path.relpath(d["doc_tpl_ar"], DOCS_DIR).replace(".md", ".html") if d["doc_tpl_ar"] else ""
        rel_guide_en = os.path.relpath(d["doc_guide_en"], DOCS_DIR).replace(".md", ".html")
        rel_guide_ar = os.path.relpath(d["doc_guide_ar"], DOCS_DIR).replace(".md", ".html") if d["doc_guide_ar"] else ""
        rel_ex_en = os.path.relpath(d["doc_ex_en"], DOCS_DIR).replace(".md", ".html")
        rel_ex_ar = os.path.relpath(d["doc_ex_ar"], DOCS_DIR).replace(".md", ".html") if d["doc_ex_ar"] else ""

        data_list.append({
            "code": d["code"],
            "code_raw": d["code_raw"],
            "phase": d["phase"],
            "phase_name_en": PHASE_META[d["phase"]]["en_title"],
            "phase_name_ar": PHASE_META[d["phase"]]["ar_title"],
            "phase_icon": PHASE_META[d["phase"]]["icon"],
            "tier": d["tier"],
            "name_en": d["name_en"],
            "name_ar": d["name_ar"],
            "template_en": tpl_en,
            "template_ar": tpl_ar,
            "guide_en": guide_en,
            "guide_ar": guide_ar,
            "example_en": ex_en,
            "example_ar": ex_ar,
            "prompt_en": prompt_en,
            "prompt_ar": prompt_ar,
            "json_en": json_en,
            "json_ar": json_ar,
            "csv_en": csv_en,
            "csv_ar": csv_ar,
            "url_tpl_en": rel_tpl_en,
            "url_tpl_ar": rel_tpl_ar,
            "url_guide_en": rel_guide_en,
            "url_guide_ar": rel_guide_ar,
            "url_ex_en": rel_ex_en,
            "url_ex_ar": rel_ex_ar,
            "gh_tpl_en": d.get("gh_tpl_en", ""),
            "gh_tpl_ar": d.get("gh_tpl_ar", ""),
            "gh_guide_en": d.get("gh_guide_en", ""),
            "gh_guide_ar": d.get("gh_guide_ar", ""),
            "gh_ex_en": d.get("gh_ex_en", ""),
            "gh_ex_ar": d.get("gh_ex_ar", ""),
            "gh_prompt_en": d.get("gh_prompt_en", ""),
            "gh_prompt_ar": d.get("gh_prompt_ar", ""),
            "gh_json_en": d.get("gh_json_en", ""),
            "gh_json_ar": d.get("gh_json_ar", ""),
            "gh_csv_en": d.get("gh_csv_en", ""),
            "gh_csv_ar": d.get("gh_csv_ar", ""),
        })

    out_file = DOCS_DIR / "assets" / "tasleemat_data.js"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    json_str = json.dumps(data_list, ensure_ascii=False)
    out_file.write_text(f"window.TASLEEMAT_DATA = {json_str};\n", encoding="utf-8")
    print(f"Generated {out_file} with {len(data_list)} deliverables ({len(json_str)} bytes).")

if __name__ == "__main__":
    build_portal()
