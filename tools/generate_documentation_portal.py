#!/usr/bin/env python3
"""tools/generate_documentation_portal.py
Generates the comprehensive, modern GitHub Pages documentation portal for Tasleemat.
Features separate English and Arabic navigation structures with universal 1-click
bilingual cross-linking on every single page, rich interactive Explorer widget,
and modern Glassmorphic design tokens.
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
    """Sanitize all relative markdown links with balanced parentheses support."""
    pat = r'\[(?:[^\]]*)\]\(((?:[^()]+|\([^()]*\))+)\)'

    def replacer(match):
        full_match = match.group(0)
        text_match = re.match(r'\[(.*)\]\(', full_match)
        text = text_match.group(1) if text_match else "Link"
        url = match.group(1).strip()

        if url.startswith(("http://", "https://", "mailto:", "#")):
            return f"[{text}]({url})"

        clean_url = url.strip("<>").split('#')[0].split('?')[0].strip()

        # 1. Example links
        if "_Example.md" in clean_url or "_مثال.md" in clean_url:
            lang_is_ar = "_مثال.md" in clean_url or "examples/ar/" in clean_url or "/ar/" in str(current_doc_path)
            target = deliverable["doc_ex_ar"] if lang_is_ar else deliverable["doc_ex_en"]
            return f"[{text}]({os.path.relpath(target, current_doc_path.parent)})"

        # 2. Template links
        if "_Template.md" in clean_url or "_قالب.md" in clean_url:
            lang_is_ar = "_قالب.md" in clean_url or "templates/ar/" in clean_url or "/ar/" in str(current_doc_path)
            target = deliverable["doc_tpl_ar"] if lang_is_ar else deliverable["doc_tpl_en"]
            return f"[{text}]({os.path.relpath(target, current_doc_path.parent)})"

        # 3. Guide links
        if "_Guide.md" in clean_url or "_دليل.md" in clean_url:
            lang_is_ar = "_دليل.md" in clean_url or "guides/ar/" in clean_url or "/ar/" in str(current_doc_path)
            target = deliverable["doc_guide_ar"] if lang_is_ar else deliverable["doc_guide_en"]
            return f"[{text}]({os.path.relpath(target, current_doc_path.parent)})"

        # 4. Sibling prompts, CSV, JSON schemas
        if clean_url.endswith((".json", ".csv", ".md")):
            target = (current_doc_path.parent / clean_url).resolve()
            if not target.exists():
                return f"**{text}**"

        return f"[{text}]({url})"

    return re.sub(pat, replacer, content)

def collect_deliverables():
    """Scan all 102 deliverable folders in forms/en and forms/ar and construct full mappings."""
    en_templates = sorted(list(FORMS_EN.rglob("*_Template.md")))
    ar_templates = sorted(list(FORMS_AR.rglob("*_قالب.md")))

    deliverables = []

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

        doc_tpl_en = DOCS_DIR / "templates" / "en" / dest_dir_en / t_en.name
        doc_guide_en = DOCS_DIR / "guides" / "en" / dest_dir_en / guides_en[0].name
        doc_ex_en = DOCS_DIR / "examples" / "en" / dest_dir_en / examples_en[0].name

        doc_tpl_ar = DOCS_DIR / "templates" / "ar" / dest_dir_ar / t_ar.name if t_ar else None
        doc_guide_ar = DOCS_DIR / "guides" / "ar" / dest_dir_ar / guides_ar[0].name if guides_ar else None
        doc_ex_ar = DOCS_DIR / "examples" / "ar" / dest_dir_ar / examples_ar[0].name if examples_ar else None

        tier_info = TIER_MAP.get(phase_prefix, "Tier 1 | Tier 2 | Tier 3")
        if "AI" in name_en or "02_02" in code_raw or "02_03" in code_raw or "02_04" in code_raw or "02_05" in code_raw or "02_06" in code_raw:
            tier_info = "Tier 4 (AI & Specialized)"

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
        })

    return deliverables

def build_portal():
    deliverables = collect_deliverables()
    print(f"Loaded {len(deliverables)} deliverable bundles.")

    # Clean existing generated docs sections
    for sub in ["catalog", "templates", "guides", "examples"]:
        target_dir = DOCS_DIR / sub
        if target_dir.exists():
            shutil.rmtree(target_dir)

    # 1. Write Deliverable Pages
    for d in deliverables:
        for p in [d["doc_tpl_en"], d["doc_guide_en"], d["doc_ex_en"], d["doc_tpl_ar"], d["doc_guide_ar"], d["doc_ex_ar"]]:
            if p:
                p.parent.mkdir(parents=True, exist_ok=True)

        # Build cross-links
        rel_guide_from_tpl = os.path.relpath(d["doc_guide_en"], d["doc_tpl_en"].parent)
        rel_ex_from_tpl = os.path.relpath(d["doc_ex_en"], d["doc_tpl_en"].parent)
        rel_ar_from_tpl = os.path.relpath(d["doc_tpl_ar"], d["doc_tpl_en"].parent)

        rel_tpl_from_guide = os.path.relpath(d["doc_tpl_en"], d["doc_guide_en"].parent)
        rel_ex_from_guide = os.path.relpath(d["doc_ex_en"], d["doc_guide_en"].parent)
        rel_ar_from_guide = os.path.relpath(d["doc_guide_ar"], d["doc_guide_en"].parent)

        rel_tpl_from_ex = os.path.relpath(d["doc_tpl_en"], d["doc_ex_en"].parent)
        rel_guide_from_ex = os.path.relpath(d["doc_guide_en"], d["doc_ex_en"].parent)
        rel_ar_from_ex = os.path.relpath(d["doc_ex_ar"], d["doc_ex_en"].parent)

        rel_guide_from_tpl_ar = os.path.relpath(d["doc_guide_ar"], d["doc_tpl_ar"].parent)
        rel_ex_from_tpl_ar = os.path.relpath(d["doc_ex_ar"], d["doc_tpl_ar"].parent)
        rel_en_from_tpl_ar = os.path.relpath(d["doc_tpl_en"], d["doc_tpl_ar"].parent)

        rel_tpl_from_guide_ar = os.path.relpath(d["doc_tpl_ar"], d["doc_guide_ar"].parent)
        rel_ex_from_guide_ar = os.path.relpath(d["doc_ex_ar"], d["doc_guide_ar"].parent)
        rel_en_from_guide_ar = os.path.relpath(d["doc_guide_en"], d["doc_guide_ar"].parent)

        rel_tpl_from_ex_ar = os.path.relpath(d["doc_tpl_ar"], d["doc_ex_ar"].parent)
        rel_guide_from_ex_ar = os.path.relpath(d["doc_guide_ar"], d["doc_ex_ar"].parent)
        rel_en_from_ex_ar = os.path.relpath(d["doc_ex_en"], d["doc_ex_ar"].parent)

        # 1. EN Template
        content_tpl_en = sanitize_content_links(d["tpl_en"].read_text(encoding="utf-8"), d["doc_tpl_en"], d)
        nav_header_tpl_en = f"""<div class="lang-switch-bar">
  <span>🌐 Dual Language / ثنائي اللغة:</span>
  <a class="lang-switch-btn" href="{rel_ar_from_tpl}">🇸🇦 الانتقال للقالب بالعربية (Arabic Template)</a>
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
    <a class="nav-pill lang-pill" href="{rel_ar_from_tpl}">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

"""
        d["doc_tpl_en"].write_text(nav_header_tpl_en + content_tpl_en, encoding="utf-8")

        # 2. EN Guide
        content_guide_en = sanitize_content_links(d["guide_en"].read_text(encoding="utf-8"), d["doc_guide_en"], d)
        nav_header_guide_en = f"""<div class="lang-switch-bar">
  <span>🌐 Dual Language / ثنائي اللغة:</span>
  <a class="lang-switch-btn" href="{rel_ar_from_guide}">🇸🇦 الانتقال للدليل بالعربية (Arabic Guide)</a>
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
    <a class="nav-pill lang-pill" href="{rel_ar_from_guide}">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

"""
        d["doc_guide_en"].write_text(nav_header_guide_en + content_guide_en, encoding="utf-8")

        # 3. EN Example
        content_ex_en = sanitize_content_links(d["ex_en"].read_text(encoding="utf-8"), d["doc_ex_en"], d)
        nav_header_ex_en = f"""<div class="lang-switch-bar">
  <span>🌐 Dual Language / ثنائي اللغة:</span>
  <a class="lang-switch-btn" href="{rel_ar_from_ex}">🇸🇦 الانتقال للمثال بالعربية (Arabic Example)</a>
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
    <a class="nav-pill lang-pill" href="{rel_ar_from_ex}">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

"""
        d["doc_ex_en"].write_text(nav_header_ex_en + content_ex_en, encoding="utf-8")

        # 4. AR Template
        content_tpl_ar = sanitize_content_links(d["tpl_ar"].read_text(encoding="utf-8"), d["doc_tpl_ar"], d)
        nav_header_tpl_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span>🌐 اللغة / Language:</span>
  <a class="lang-switch-btn" href="{rel_en_from_tpl_ar}">🇬🇧 Switch to English Template (النسخة الإنجليزية)</a>
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
    <a class="nav-pill lang-pill" href="{rel_en_from_tpl_ar}">🇬🇧 English Version</a>
  </div>
</div>

---

"""
        d["doc_tpl_ar"].write_text(nav_header_tpl_ar + content_tpl_ar, encoding="utf-8")

        # 5. AR Guide
        content_guide_ar = sanitize_content_links(d["guide_ar"].read_text(encoding="utf-8"), d["doc_guide_ar"], d)
        nav_header_guide_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span>🌐 اللغة / Language:</span>
  <a class="lang-switch-btn" href="{rel_en_from_guide_ar}">🇬🇧 Switch to English Guide (النسخة الإنجليزية)</a>
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
    <a class="nav-pill lang-pill" href="{rel_en_from_guide_ar}">🇬🇧 English Version</a>
  </div>
</div>

---

"""
        d["doc_guide_ar"].write_text(nav_header_guide_ar + content_guide_ar, encoding="utf-8")

        # 6. AR Example
        content_ex_ar = sanitize_content_links(d["ex_ar"].read_text(encoding="utf-8"), d["doc_ex_ar"], d)
        nav_header_ex_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span>🌐 اللغة / Language:</span>
  <a class="lang-switch-btn" href="{rel_en_from_ex_ar}">🇬🇧 Switch to English Example (النسخة الإنجليزية)</a>
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
    <a class="nav-pill lang-pill" href="{rel_en_from_ex_ar}">🇬🇧 English Version</a>
  </div>
</div>

---

"""
        d["doc_ex_ar"].write_text(nav_header_ex_ar + content_ex_ar, encoding="utf-8")

    # 2. Build Master Catalogs with Interactive Explorer
    build_master_catalogs(deliverables)

    # 3. Build Section Index Pages
    build_section_indexes(deliverables)

    # 4. Build Phase Index Pages
    build_phase_indexes(deliverables)

    # 5. Update Master Governance Manuals with Language Switch Bar
    update_governance_manuals_lang_bars()

    # 6. Update mkdocs.yml navigation
    update_mkdocs_config(deliverables)

    print("Documentation portal successfully generated!")

def update_governance_manuals_lang_bars():
    """Ensure all 12 EN and 12 AR governance manuals have top language switcher bars."""
    for i in range(1, 13):
        en_files = list((DOCS_DIR / "en").glob(f"{i:02d}_*.md"))
        ar_files = list((DOCS_DIR / "ar").glob(f"{i:02d}_*.md"))

        if en_files and ar_files:
            en_f, ar_f = en_files[0], ar_files[0]
            rel_ar = os.path.relpath(ar_f, en_f.parent)
            rel_en = os.path.relpath(en_f, ar_f.parent)

            en_content = en_f.read_text(encoding="utf-8")
            if "lang-switch-bar" not in en_content:
                bar_en = f"""<div class="lang-switch-bar">
  <span>🌐 Language / اللغة:</span>
  <a class="lang-switch-btn" href="{rel_ar}">🇸🇦 الانتقال للنسخة العربية (Arabic Version)</a>
</div>

"""
                en_f.write_text(bar_en + en_content, encoding="utf-8")

            ar_content = ar_f.read_text(encoding="utf-8")
            if "lang-switch-bar" not in ar_content:
                bar_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span>🌐 اللغة / Language:</span>
  <a class="lang-switch-btn" href="{rel_en}">🇬🇧 Switch to English Version (النسخة الإنجليزية)</a>
</div>

"""
                ar_f.write_text(bar_ar + ar_content, encoding="utf-8")

def build_master_catalogs(deliverables):
    """Build comprehensive interactive master catalog pages with live Explorer widget."""
    target_en = DOCS_DIR / "catalog/en/index.md"
    target_en.parent.mkdir(parents=True, exist_ok=True)
    rel_ar_catalog = os.path.relpath(DOCS_DIR / "catalog/ar/index.md", target_en.parent)

    catalog_en = f"""<div class="lang-switch-bar">
  <span>🌐 Language / اللغة:</span>
  <a class="lang-switch-btn" href="{rel_ar_catalog}">🇸🇦 الانتقال للفهرس العام بالعربية (Arabic Catalog)</a>
</div>

# 📑 Master Deliverables & Artifacts Catalog
**Standard:** PMI PMBOK® 6th, 7th & 8th Editions • NIST AI RMF • ISO 21500  
**Total Deliverables:** 102 Bilingual Forms (204 Standard Templates • 204 Authoring Guides • 204 Completed Case Studies)

---

<div id="tasleemat-explorer" class="explorer-wrapper">
  <div class="explorer-toolbar">
    <input type="text" id="explorer-search" class="explorer-search-box" placeholder="🔍 Search by code (e.g. PMO-03.01), name, phase, tier, or keyword..." />
    
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
      <span style="font-size: 0.85rem; color: #64748b; font-weight: 600;">Showing <span id="results-count" style="color: #2563eb; font-weight: 800;">102</span> deliverables</span>
      <div style="display: flex; gap: 6px;">
        <button class="filter-chip view-toggle-btn active" data-view="cards">🗂️ Card Grid View</button>
        <button class="filter-chip view-toggle-btn" data-view="table">📊 Table View</button>
      </div>
    </div>
  </div>

  <div id="explorer-cards" class="explorer-grid-cards">
"""

    for d in deliverables:
        rel_tpl = os.path.relpath(d["doc_tpl_en"], target_en.parent)
        rel_guide = os.path.relpath(d["doc_guide_en"], target_en.parent)
        rel_ex = os.path.relpath(d["doc_ex_en"], target_en.parent)
        rel_ar_tpl = os.path.relpath(d["doc_tpl_ar"], target_en.parent)
        phase_title = PHASE_META[d['phase']]['en_title']

        search_str = f"{d['code']} {d['name_en']} {d['name_ar']} {phase_title} {d['tier']} PMI PMBOK".lower()

        catalog_en += f"""    <div class="explorer-card-item" data-phase="{d['phase']}" data-tier="{d['tier']}" data-search="{search_str}">
      <div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
          <span class="badge badge-code">{d['code']}</span>
          <span style="font-size: 0.75rem; color: #64748b; font-weight: 600;">{d['tier']}</span>
        </div>
        <h5>{d['name_en']}</h5>
        <div style="font-size: 0.78rem; color: #64748b; margin-bottom: 4px;">🇸🇦 {d['name_ar']}</div>
        <div style="font-size: 0.75rem; color: #0284c7; font-weight: 600;">{phase_title}</div>
      </div>
      <div class="explorer-card-actions">
        <a class="card-action-link" href="{rel_tpl}">📋 Template</a>
        <a class="card-action-link" href="{rel_guide}">📖 Guide</a>
        <a class="card-action-link" href="{rel_ex}">💡 Example</a>
        <a class="card-action-link" style="background: #ecfdf5; color: #065f46 !important;" href="{rel_ar_tpl}">🇸🇦 عربي</a>
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
        rel_tpl = os.path.relpath(d["doc_tpl_en"], target_en.parent)
        rel_guide = os.path.relpath(d["doc_guide_en"], target_en.parent)
        rel_ex = os.path.relpath(d["doc_ex_en"], target_en.parent)
        rel_ar_tpl = os.path.relpath(d["doc_tpl_ar"], target_en.parent)
        phase_title = PHASE_META[d['phase']]['en_title']
        search_str = f"{d['code']} {d['name_en']} {d['name_ar']} {phase_title} {d['tier']} PMI PMBOK".lower()

        catalog_en += f"""        <tr class="explorer-table-row" data-phase="{d['phase']}" data-tier="{d['tier']}" data-search="{search_str}">
          <td style="text-align: center;"><strong><code>{d['code']}</code></strong></td>
          <td><strong>{d['name_en']}</strong><br/><small style="color: #64748b;">🇸🇦 {d['name_ar']}</small></td>
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
    rel_en_catalog = os.path.relpath(DOCS_DIR / "catalog/en/index.md", target_ar.parent)

    catalog_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span>🌐 اللغة / Language:</span>
  <a class="lang-switch-btn" href="{rel_en_catalog}">🇬🇧 Switch to English Catalog (الفهرس الإنجليزي)</a>
</div>

# 📑 الفهرس العام والمستكشف التفاعلي للمخرجات والنماذج
**التوافق مع المعايير:** معهد إدارة المشاريع PMI PMBOK® الإصدارات 6 و 7 و 8 • أخلاقيات الذكاء الاصطناعي (سدايا) • ISO 21500  
**إجمالي المخرجات:** 102 مخرجاً إدارياً ثنائياً (204 قوالب قياسية • 204 أدلة إرشادية • 204 دراسات حالة وأمثلة واقعية)

---

<div id="tasleemat-explorer" class="explorer-wrapper" dir="rtl">
  <div class="explorer-toolbar">
    <input type="text" id="explorer-search" class="explorer-search-box" placeholder="🔍 ابحث بالرمز (مثل PMO-03.01)، الاسم، المرحلة، المستوى، أو الكلمات المفتاحية..." />
    
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
      <span style="font-size: 0.85rem; color: #64748b; font-weight: 600;">يتم عرض <span id="results-count" style="color: #2563eb; font-weight: 800;">102</span> نموذجاً</span>
      <div style="display: flex; gap: 6px;">
        <button class="filter-chip view-toggle-btn active" data-view="cards">🗂️ عرض البطاقات</button>
        <button class="filter-chip view-toggle-btn" data-view="table">📊 عرض الجدول</button>
      </div>
    </div>
  </div>

  <div id="explorer-cards" class="explorer-grid-cards">
"""

    for d in deliverables:
        rel_tpl = os.path.relpath(d["doc_tpl_ar"], target_ar.parent)
        rel_guide = os.path.relpath(d["doc_guide_ar"], target_ar.parent)
        rel_ex = os.path.relpath(d["doc_ex_ar"], target_ar.parent)
        rel_en_tpl = os.path.relpath(d["doc_tpl_en"], target_ar.parent)
        phase_title = PHASE_META[d['phase']]['ar_title']

        search_str = f"{d['code']} {d['name_en']} {d['name_ar']} {phase_title} {d['tier']} ميثاق خطة سجل".lower()

        catalog_ar += f"""    <div class="explorer-card-item" data-phase="{d['phase']}" data-tier="{d['tier']}" data-search="{search_str}">
      <div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
          <span class="badge badge-code">{d['code']}</span>
          <span style="font-size: 0.75rem; color: #64748b; font-weight: 600;">{d['tier']}</span>
        </div>
        <h5>{d['name_ar']}</h5>
        <div style="font-size: 0.78rem; color: #64748b; margin-bottom: 4px;">🇬🇧 {d['name_en']}</div>
        <div style="font-size: 0.75rem; color: #0284c7; font-weight: 600;">{phase_title}</div>
      </div>
      <div class="explorer-card-actions">
        <a class="card-action-link" href="{rel_tpl}">📋 القالب</a>
        <a class="card-action-link" href="{rel_guide}">📖 الدليل</a>
        <a class="card-action-link" href="{rel_ex}">💡 مثال واقعي</a>
        <a class="card-action-link" style="background: #eff6ff; color: #1e40af !important;" href="{rel_en_tpl}">🇬🇧 EN</a>
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
        rel_tpl = os.path.relpath(d["doc_tpl_ar"], target_ar.parent)
        rel_guide = os.path.relpath(d["doc_guide_ar"], target_ar.parent)
        rel_ex = os.path.relpath(d["doc_ex_ar"], target_ar.parent)
        phase_title = PHASE_META[d['phase']]['ar_title']
        search_str = f"{d['code']} {d['name_en']} {d['name_ar']} {phase_title} {d['tier']}".lower()

        catalog_ar += f"""        <tr class="explorer-table-row" data-phase="{d['phase']}" data-tier="{d['tier']}" data-search="{search_str}">
          <td style="text-align: center;"><strong><code>{d['code']}</code></strong></td>
          <td><strong>{d['name_ar']}</strong><br/><small style="color: #64748b;">🇬🇧 {d['name_en']}</small></td>
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
    target_tpl_en = DOCS_DIR / "templates/en/index.md"
    target_tpl_en.parent.mkdir(parents=True, exist_ok=True)
    rel_ar_tpl_idx = os.path.relpath(DOCS_DIR / "templates/ar/index.md", target_tpl_en.parent)
    tpl_idx_en = f"""<div class="lang-switch-bar">
  <span>🌐 Language / اللغة:</span>
  <a class="lang-switch-btn" href="{rel_ar_tpl_idx}">🇸🇦 الانتقال لفهرس القوالب بالعربية (Arabic Templates)</a>
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
    target_tpl_ar = DOCS_DIR / "templates/ar/index.md"
    target_tpl_ar.parent.mkdir(parents=True, exist_ok=True)
    rel_en_tpl_idx = os.path.relpath(DOCS_DIR / "templates/en/index.md", target_tpl_ar.parent)
    tpl_idx_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span>🌐 اللغة / Language:</span>
  <a class="lang-switch-btn" href="{rel_en_tpl_idx}">🇬🇧 Switch to English Templates (قوالب إنجليزية)</a>
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
    rel_ar_g_idx = os.path.relpath(DOCS_DIR / "guides/ar/index.md", target_g_en.parent)
    guides_idx_en = f"""<div class="lang-switch-bar">
  <span>🌐 Language / اللغة:</span>
  <a class="lang-switch-btn" href="{rel_ar_g_idx}">🇸🇦 الانتقال لأدلة النماذج بالعربية (Arabic Guides)</a>
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
    rel_en_g_idx = os.path.relpath(DOCS_DIR / "guides/en/index.md", target_g_ar.parent)
    guides_idx_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span>🌐 اللغة / Language:</span>
  <a class="lang-switch-btn" href="{rel_en_g_idx}">🇬🇧 Switch to English Guides (أدلة إنجليزية)</a>
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
    rel_ar_ex_idx = os.path.relpath(DOCS_DIR / "examples/ar/index.md", target_ex_en.parent)
    ex_idx_en = f"""<div class="lang-switch-bar">
  <span>🌐 Language / اللغة:</span>
  <a class="lang-switch-btn" href="{rel_ar_ex_idx}">🇸🇦 الانتقال للأمثلة الواقعية بالعربية (Arabic Examples)</a>
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
    rel_en_ex_idx = os.path.relpath(DOCS_DIR / "examples/en/index.md", target_ex_ar.parent)
    ex_idx_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span>🌐 اللغة / Language:</span>
  <a class="lang-switch-btn" href="{rel_en_ex_idx}">🇬🇧 Switch to English Examples (أمثلة إنجليزية)</a>
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
        target_t_en = DOCS_DIR / "templates" / "en" / phase_dir_en / "index.md"
        target_t_en.parent.mkdir(parents=True, exist_ok=True)
        rel_ar_phase_tpl = os.path.relpath(DOCS_DIR / "templates" / "ar" / phase_dir_ar / "index.md", target_t_en.parent)
        idx_content_en = f"""<div class="lang-switch-bar">
  <span>🌐 Language / اللغة:</span>
  <a class="lang-switch-btn" href="{rel_ar_phase_tpl}">🇸🇦 الانتقال لقوالب المرحلة بالعربية (Arabic Templates)</a>
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
        target_t_ar = DOCS_DIR / "templates" / "ar" / phase_dir_ar / "index.md"
        target_t_ar.parent.mkdir(parents=True, exist_ok=True)
        rel_en_phase_tpl = os.path.relpath(DOCS_DIR / "templates" / "en" / phase_dir_en / "index.md", target_t_ar.parent)
        idx_content_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span>🌐 اللغة / Language:</span>
  <a class="lang-switch-btn" href="{rel_en_phase_tpl}">🇬🇧 Switch to English Templates (قوالب إنجليزية)</a>
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
        rel_ar_phase_g = os.path.relpath(DOCS_DIR / "guides" / "ar" / phase_dir_ar / "index.md", target_g_en.parent)
        g_content_en = f"""<div class="lang-switch-bar">
  <span>🌐 Language / اللغة:</span>
  <a class="lang-switch-btn" href="{rel_ar_phase_g}">🇸🇦 الانتقال لأدلة المرحلة بالعربية (Arabic Guides)</a>
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
        rel_en_phase_g = os.path.relpath(DOCS_DIR / "guides" / "en" / phase_dir_en / "index.md", target_g_ar.parent)
        g_content_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span>🌐 اللغة / Language:</span>
  <a class="lang-switch-btn" href="{rel_en_phase_g}">🇬🇧 Switch to English Guides (أدلة إنجليزية)</a>
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
        rel_ar_phase_e = os.path.relpath(DOCS_DIR / "examples" / "ar" / phase_dir_ar / "index.md", target_e_en.parent)
        e_content_en = f"""<div class="lang-switch-bar">
  <span>🌐 Language / اللغة:</span>
  <a class="lang-switch-btn" href="{rel_ar_phase_e}">🇸🇦 الانتقال لأمثلة المرحلة بالعربية (Arabic Examples)</a>
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
        rel_en_phase_e = os.path.relpath(DOCS_DIR / "examples" / "en" / phase_dir_en / "index.md", target_e_ar.parent)
        e_content_ar = f"""<div class="lang-switch-bar" dir="rtl">
  <span>🌐 اللغة / Language:</span>
  <a class="lang-switch-btn" href="{rel_en_phase_e}">🇬🇧 Switch to English Examples (أمثلة إنجليزية)</a>
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
    """Update mkdocs.yml with separated English and Arabic navigation structures."""
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
                    if section_type == "templates":
                        target = os.path.relpath(d["doc_tpl_en"], DOCS_DIR)
                    elif section_type == "guides":
                        target = os.path.relpath(d["doc_guide_en"], DOCS_DIR)
                    else:
                        target = os.path.relpath(d["doc_ex_en"], DOCS_DIR)
                    sub_items.append({f"{d['code']} {d['name_en']}": target})
                nav_list.append({sub_title: sub_items})
        else:
            for d in items:
                if section_type == "templates":
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
                    if section_type == "templates":
                        target = os.path.relpath(d["doc_tpl_ar"], DOCS_DIR)
                    elif section_type == "guides":
                        target = os.path.relpath(d["doc_guide_ar"], DOCS_DIR)
                    else:
                        target = os.path.relpath(d["doc_ex_ar"], DOCS_DIR)
                    sub_items.append({f"{d['code']} {d['name_ar']}": target})
                nav_list.append({sub_title: sub_items})
        else:
            for d in items:
                if section_type == "templates":
                    target = os.path.relpath(d["doc_tpl_ar"], DOCS_DIR)
                elif section_type == "guides":
                    target = os.path.relpath(d["doc_guide_ar"], DOCS_DIR)
                else:
                    target = os.path.relpath(d["doc_ex_ar"], DOCS_DIR)
                nav_list.append({f"{d['code']} {d['name_ar']}": target})
        return nav_list

    nav = [
        # === 🇬🇧 ENGLISH SECTION ===
        {"🇬🇧 English Portal": [
            {"Home & Overview": "index.md"},
            {"📑 Master Deliverables Catalog": "catalog/en/index.md"},
            {"📖 Master Lexicon & Terms": "LEXICON.md"},
            {"🇸🇦 للانتقال للبوابة العربية (Arabic Portal)": "README_AR.md"}
        ]},
        {"📚 Governance Manuals (EN)": [
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
        {"📋 Templates Library (EN)": [
            {"Templates Overview": "templates/en/index.md"},
            {PHASE_META["00"]["en_title"]: make_phase_nav_en("00", "templates")},
            {PHASE_META["01"]["en_title"]: make_phase_nav_en("01", "templates")},
            {PHASE_META["02"]["en_title"]: make_phase_nav_en("02", "templates")},
            {PHASE_META["03"]["en_title"]: make_phase_nav_en("03", "templates")},
            {PHASE_META["04"]["en_title"]: make_phase_nav_en("04", "templates")},
            {PHASE_META["05"]["en_title"]: make_phase_nav_en("05", "templates")},
            {PHASE_META["06"]["en_title"]: make_phase_nav_en("06", "templates")},
            {PHASE_META["07"]["en_title"]: make_phase_nav_en("07", "templates")}
        ]},
        {"📖 Authoring Guides (EN)": [
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
        {"💡 Reference Examples (EN)": [
            {"Case Studies Showcase": "examples/en/index.md"},
            {PHASE_META["00"]["en_title"]: make_phase_nav_en("00", "examples")},
            {PHASE_META["01"]["en_title"]: make_phase_nav_en("01", "examples")},
            {PHASE_META["02"]["en_title"]: make_phase_nav_en("02", "examples")},
            {PHASE_META["03"]["en_title"]: make_phase_nav_en("03", "examples")},
            {PHASE_META["04"]["en_title"]: make_phase_nav_en("04", "examples")},
            {PHASE_META["05"]["en_title"]: make_phase_nav_en("05", "examples")},
            {PHASE_META["06"]["en_title"]: make_phase_nav_en("06", "examples")},
            {PHASE_META["07"]["en_title"]: make_phase_nav_en("07", "examples")}
        ]},

        # === 🇸🇦 ARABIC SECTION ===
        {"🇸🇦 البوابة التوثيقية (AR)": [
            {"الرئيسية ودليل الانطلاق": "README_AR.md"},
            {"📑 الفهرس العام الشامل للنماذج": "catalog/ar/index.md"},
            {"📖 المعجم الموحد للمصطلحات": "LEXICON.md"},
            {"🇬🇧 Switch to English Portal": "index.md"}
        ]},
        {"📚 الأدلة والسياسات الحوكمية (AR)": [
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
        {"📋 مكتبة القوالب والنماذج (AR)": [
            {"الفهرس العام للقوالب": "templates/ar/index.md"},
            {PHASE_META["00"]["ar_title"]: make_phase_nav_ar("00", "templates")},
            {PHASE_META["01"]["ar_title"]: make_phase_nav_ar("01", "templates")},
            {PHASE_META["02"]["ar_title"]: make_phase_nav_ar("02", "templates")},
            {PHASE_META["03"]["ar_title"]: make_phase_nav_ar("03", "templates")},
            {PHASE_META["04"]["ar_title"]: make_phase_nav_ar("04", "templates")},
            {PHASE_META["05"]["ar_title"]: make_phase_nav_ar("05", "templates")},
            {PHASE_META["06"]["ar_title"]: make_phase_nav_ar("06", "templates")},
            {PHASE_META["07"]["ar_title"]: make_phase_nav_ar("07", "templates")}
        ]},
        {"📖 أدلة إعداد النماذج (AR)": [
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
        {"💡 معرض الأمثلة الواقعية (AR)": [
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
    ]

    raw_cfg = mkdocs_file.read_text(encoding="utf-8")
    header_part = raw_cfg.split("nav:")[0]

    # Add extra_javascript if not already present
    if "assets/explorer.js" not in header_part:
        header_part = header_part.replace(
            "extra_css:\n  - assets/custom.css",
            "extra_css:\n  - assets/custom.css\n\nextra_javascript:\n  - assets/explorer.js"
        )

    nav_yaml = yaml.dump({"nav": nav}, allow_unicode=True, sort_keys=False, default_flow_style=False)
    mkdocs_file.write_text(header_part.strip() + "\n\n" + nav_yaml + "\n", encoding="utf-8")
    print("mkdocs.yml navigation updated successfully.")

if __name__ == "__main__":
    build_portal()
