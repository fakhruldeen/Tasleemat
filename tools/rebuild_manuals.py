#!/usr/bin/env python3
"""rebuild_manuals.py
Fixes and regenerates governance manuals:
1. Strips all duplicate language bars, stray </div> tags, and corrupt headers across docs/en/*.md and docs/ar/*.md.
2. Fixes logo image paths to '../img/logo.png' (EN) and '../img/logo-ar.png' (AR).
3. Generates complete, rich RACI Authority Matrix (06_raci_authority_matrix.md) across all 102 deliverables.
4. Generates complete Document Dependencies DAG (07_document_dependencies.md) across all 102 deliverables.
"""

import os
import sys
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.generate_documentation_portal import collect_deliverables, align_tables_in_markdown
DOCS_DIR = ROOT / "docs"

GATE_MAP_EN = {
    "00": "Gate 0: Strategy & Portfolio Alignment",
    "01": "Gate 0: Strategic Justification & Business Case",
    "02": "Gate 1: Approach, Governance & AI Assessment",
    "03": "Gate 1: Project Initiation & Chartering",
    "04": "Gate 2: Integrated Baseline & Comprehensive Planning",
    "05": "Gate 3: Execution, Deliverable Build & Logging",
    "06": "Gate 4: Monitoring, Value & Quality Verification",
    "07": "Gate 5: Operational Transition & Final Closeout"
}

GATE_MAP_AR = {
    "00": "بوابة 0: المواءمة الاستراتيجية والمحفظة",
    "01": "بوابة 0: المبررات الاستراتيجية ودراسة الجدوى",
    "02": "بوابة 1: تقييم المنهجية والحوكمة والذكاء الاصطناعي",
    "03": "بوابة 1: البدء والاعتماد وميثاق المشروع",
    "04": "بوابة 2: اعتماد خطوط الأساس المتكاملة والتخطيط",
    "05": "بوابة 3: التنفيذ وبناء المخرجات وسجلات العمل",
    "06": "بوابة 4: المراقبة والتحكم والتحقق من الجودة والقيمة",
    "07": "بوابة 5: التحول للعمليات التشغيلية والإغلاق النهائي"
}

def clean_manual_content(content: str, is_arabic: bool = False) -> str:
    # 1. Remove all leading language switcher bars and stray div tags
    cleaned = content
    # Remove any lang-switch-bar divs
    cleaned = re.sub(r'<div class="lang-switch-bar"[^>]*>[\s\S]*?</div>\s*</div>\n*', '', cleaned)
    cleaned = re.sub(r'<div class="lang-switch-bar"[^>]*>[\s\S]*?</div>\n*', '', cleaned)
    
    # Strip any leading stray </div> or <div> tags
    lines = cleaned.splitlines()
    start_idx = 0
    while start_idx < len(lines):
        line_s = lines[start_idx].strip()
        if line_s in ['</div>', '<div>', '</div></div>', ''] or line_s.startswith('<div class="lang-switch'):
            start_idx += 1
        else:
            break
    cleaned = '\n'.join(lines[start_idx:])
    
    # 2. Fix logo paths
    logo_file = "../img/logo-ar.png" if is_arabic else "../img/logo.png"
    logo_alt = "Tasleemat PMO Logo" if not is_arabic else "شعار تسليمات"
    # Replace broken logo images e.g. src="docs/img/..." or src="../img/..."
    cleaned = re.sub(r'<p align="center">\s*<img src="[^"]+"[^>]*>\s*</p>\n*', '', cleaned)
    
    # Prepend clean logo
    logo_html = f'<p align="center">\n  <img src="{logo_file}" alt="{logo_alt}" width="280" />\n</p>\n\n'
    cleaned = logo_html + cleaned.lstrip()
    
    return cleaned

def generate_raci_manuals(deliverables):
    print("Generating complete 102-deliverable RACI Authority Matrix...")
    
    # English RACI
    raci_en = """# 👥 Tasleemat Master Governance RACI & Signature Authority Matrix
**Document Reference:** `TASLEEMAT-GOVERNANCE-RACI-v2.0`  
**Scope:** Complete RACI authority framework across all 102 PMO deliverables  
**Standards:** PMI PMBOK® 6th, 7th & 8th Edition Standard Governance

---

## 🎯 Executive Overview

This matrix defines the governance authority and accountability for creating, approving, consulting on, and reporting every artifact across the entire project lifecycle:
* **Responsible (Prepared By / Author):** The operational lead or project role accountable for drafting and maintaining the deliverable.
* **Accountable (Signed / Approved By):** The executive or governing authority who formally approves and signs off on the artifact.
* **Consulted (Contributors):** Subject matter experts, domain specialists, and stakeholders who provide active technical or operational input.
* **Informed (Reported To):** Stakeholders and steering committees who receive published versions and status updates.

---

## 🏛️ Master RACI Authority Index (All 102 Deliverables)

| Code | Deliverable Name | Responsible (Author) | Accountable (Sign-off Authority) | Consulted (Contributors) | Informed (Reported To) |
| :---: | :--- | :--- | :--- | :--- | :--- |
"""
    for d in deliverables:
        p_prefix = d["code"][:2]
        
        if p_prefix == "00":
            prep = "Portfolio Director / PMO Lead"
            sign_str = "**Executive Steering Committee / C-Suite**"
        elif p_prefix == "01":
            prep = "Lead Business Analyst / Value Strategist"
            sign_str = "**Investment Committee / CFO & Business Sponsor**"
        elif p_prefix == "02":
            prep = "Methodology Specialist / AI Governance Lead"
            sign_str = "**PMO Director & Legal / Compliance Counsel**"
        elif p_prefix == "03":
            prep = "Project Manager / Initiative Proponent"
            sign_str = "**Project Sponsor & PMO Lead**"
        elif p_prefix == "04":
            prep = "Project Manager / Planning Lead"
            sign_str = "**Project Sponsor & PMO Director**"
        elif p_prefix == "05":
            prep = "Project Manager / Scrum Master"
            sign_str = "**Change Control Board (CCB) & Project Sponsor**"
        elif p_prefix == "06":
            prep = "Project Manager / QA & Controls Lead"
            sign_str = "**Project Sponsor & PMO Director**"
        else: # 07
            prep = "Project Manager / Transition Lead"
            sign_str = "**Project Sponsor & Operations Director**"
            
        consult = "Domain SMEs, Technical Leads, Team Leads"
        inform = "Steering Committee, PMO, Project Stakeholders"
        
        raci_en += f"| **`{d['code']}`** | {d['name_en']} | {prep} | {sign_str} | {consult} | {inform} |\n"
        
    (DOCS_DIR / "en/06_raci_authority_matrix.md").write_text(clean_manual_content(raci_en, is_arabic=False), encoding="utf-8")
    
    # Arabic RACI
    raci_ar = """# 👥 مصفوفة RACI والصلاحيات والاعتماد المؤسسي لمكتب إدارة المشاريع
**مرجع الوثيقة:** `TASLEEMAT-GOVERNANCE-RACI-AR-v2.0`  
**النطاق:** مصفوفة الحوكمة والاعتمادات الشاملة لكافة النماذج الـ 102  
**المعايير:** متوافق مع معايير معهد إدارة المشاريع العالمي PMI PMBOK®

---

## 🎯 نظرة عامة تنفيذية

تحدد هذه المصفوفة الصلاحيات والحوكمة المؤسسية لإعداد، واعتماد، واستشارة، وإبلاغ كافة الوثائق في منظومة مكاتب إدارة المشاريع:
* **المسؤول عن الإعداد (Responsible / Author):** الدور التشغيلي المكلف بصياغة الوثيقة وتحديث بياناتها.
* **المعتمد والموقع (Accountable / Sign-off Authority):** السلطة التنفيذية المسؤولة نظامياً عن اعتماد الوثيقة وخط الأساس.
* **المستشار (Consulted):** الخبراء والمعنيون الذين يقدمون المدخلات الفنية والتشغيلية.
* **المُبَلَّغ (Informed / Reported To):** الجهات التي تتلقى التقارير والنسخ المعتمدة.

---

## 🏛️ جدول مصفوفة الصلاحيات والحوكمة RACI (كافة الـ 102 مخرجاً)

| الرمز | اسم المخرج الإداري | المسؤول عن الإعداد (Author) | المعتمد والموقع (Sign-off) | المستشارون (Consulted) | المُبَلَّغون (Informed) |
| :---: | :--- | :--- | :--- | :--- | :--- |
"""
    for d in deliverables:
        p_prefix = d["code"][:2]
        
        if p_prefix == "00":
            prep_ar = "مدير المحفظة / قائد مكتب إدارة المشاريع"
            sign_ar = "**اللجنة التوجيهية التنفيذية / الإدارة العليا**"
        elif p_prefix == "01":
            prep_ar = "كبير محللي الأعمال / مخطط القيمة"
            sign_ar = "**لجنة الاستثمار والمدير المالي (CFO)**"
        elif p_prefix == "02":
            prep_ar = "مسؤول المنهجية / مسؤول حوكمة الذكاء الاصطناعي"
            sign_ar = "**مدير مكتب إدارة المشاريع والمستشار القانوني**"
        elif p_prefix == "03":
            prep_ar = "مدير المشروع / مقدّم المبادرة"
            sign_ar = "**راعي المشروع وقائد مكتب إدارة المشاريع**"
        elif p_prefix == "04":
            prep_ar = "مدير المشروع / قادة التخطيط"
            sign_ar = "**راعي المشروع ومدير مكتب إدارة المشاريع**"
        elif p_prefix == "05":
            prep_ar = "مدير المشروع / سيد السكروم"
            sign_ar = "**مجلس ضبط التغيير (CCB) وراعي المشروع**"
        elif p_prefix == "06":
            prep_ar = "مدير المشروع / مسؤول الجودة والرقابة"
            sign_ar = "**راعي المشروع ومدير مكتب إدارة المشاريع**"
        else: # 07
            prep_ar = "مدير المشروع / قائد الانتقال التشغيلي"
            sign_ar = "**راعي المشروع ومدير العمليات التشغيلية**"
            
        consult_ar = "خبراء المجال، القادة التقنيون، فريق العمل"
        inform_ar = "اللجنة التوجيهية، مكتب إدارة المشاريع، أصحاب المصلحة"
        
        raci_ar += f"| **`{d['code']}`** | {d['name_ar']} | {prep_ar} | {sign_ar} | {consult_ar} | {inform_ar} |\n"
        
    (DOCS_DIR / "ar/06_raci_authority_matrix.md").write_text(clean_manual_content(raci_ar, is_arabic=True), encoding="utf-8")

def generate_dependencies_manuals(deliverables):
    print("Generating complete 102-deliverable Document Dependencies DAG...")
    
    dep_en = """# 🔗 Tasleemat Document Dependencies & Lifecycle Network
**Document Reference:** `TASLEEMAT-DOC-DEPENDENCIES-v2.0`  
**Standards:** Aligned with PMI PMBOK® Guide 6th, 7th & 8th Editions

---

## 🎯 Executive Overview

In the **Tasleemat PMO Operating Framework**, no deliverable exists in isolation. Every artifact operates as a node in a **Directed Acyclic Graph (DAG)** connecting strategic drivers, baselines, execution logs, and closure assets across all 8 phases:

```mermaid
flowchart TD
    G0["<b>Phase 00/01: Strategy & Value</b><br/>Business Case & OKRs"] --> G1["<b>Phase 02/03: Initiation & Approach</b><br/>Project Charter & Vision"]
    G1 --> G2["<b>Phase 04: Planning Baseline</b><br/>PMP, Scope, Schedule, Budget"]
    G2 --> G3["<b>Phase 05: Execution & Delivery</b><br/>Work Build, Issues & Change Requests"]
    G3 --> G4["<b>Phase 06: Monitoring & Control</b><br/>Status Reports, EVM & Quality UAT"]
    G4 --> G5["<b>Phase 07: Closing & Operations</b><br/>Handover, Closeout & Lessons Learned"]
```

---

## 📋 Comprehensive Deliverable Dependency Index (All 102 Artifacts)

| Code | Deliverable Name | Lifecycle Gate / Phase | Primary Inputs (Predecessors) | Primary Outputs (Successors) |
| :---: | :--- | :--- | :--- | :--- |
"""
    for d in deliverables:
        p_prefix = d["code"][:2]
        gate_str = GATE_MAP_EN.get(p_prefix, "General Governance Gate")
        
        # Determine logical predecessor and successor based on phase & hierarchy
        if p_prefix == "00":
            preds = "`Enterprise OKRs`, `Corporate Strategy`"
            succs = "`PMO-00.02 Program Charter`, `PMO-03.01 Project Charter`"
        elif p_prefix == "01":
            preds = "`PMO-00.01 Portfolio Roadmap`, `Feasibility Study`"
            succs = "`PMO-03.01 Project Charter`, `PMO-01.03 Benefits Plan`"
        elif p_prefix == "02":
            preds = "`PMO-01.01 Business Case`, `Organizational Strategy`"
            succs = "`PMO-03.01 Project Charter`, `PMO-04.01.01 Project Management Plan`"
        elif p_prefix == "03":
            preds = "`PMO-01.01 Business Case`, `PMO-02.01 Development Approach`"
            succs = "`PMO-04.01.01 Project Management Plan`, `PMO-03.04 Stakeholder Register`"
        elif p_prefix == "04":
            preds = "`PMO-03.01 Project Charter`, `PMO-03.03 Assumption Log`"
            succs = "`PMO-05 Execution Logs`, `PMO-06.01 Project Status Report`"
        elif p_prefix == "05":
            preds = "`PMO-04 Planning Baselines (Scope/Schedule/Cost)`"
            succs = "`PMO-06.01 Status Report`, `PMO-05.04 Change Log`"
        elif p_prefix == "06":
            preds = "`PMO-04 Baselines`, `PMO-05 Execution Records`"
            succs = "`PMO-06.08 Acceptance Form`, `PMO-07.03 Project Closeout`"
        else: # 07
            preds = "`PMO-06.08 Acceptance Form`, `PMO-06.10 UAT Signoff`"
            succs = "`PMO-07.04 Operations Handover`, `PMO-07.05 Post-Implementation Review`"
            
        dep_en += f"| **`{d['code']}`** | {d['name_en']} | {gate_str} | {preds} | {succs} |\n"
        
    (DOCS_DIR / "en/07_document_dependencies.md").write_text(clean_manual_content(dep_en, is_arabic=False), encoding="utf-8")
    
    # Arabic Dependencies
    dep_ar = """# 🔗 شبكة اعتماديات الوثائق وهندسة دورة الحياة في تسليمات
**مرجع الوثيقة:** `TASLEEMAT-DOC-DEPENDENCIES-AR-v2.0`  
**المعايير:** متوافق مع معايير معهد إدارة المشاريع العالمي PMI PMBOK®

---

## 🎯 نظرة عامة تنفيذية

في **نظام تشغيل مكاتب إدارة المشاريع «تسليمات»**، لا توجد وثيقة معزولة. تعمل كل استمارة كعقدة مترابطة في **شبكة اعتماديات موجهة (DAG)** تربط المدخلات الاستراتيجية، وخطوط الأساس المعتمدة، وسجلات المتابعة التشغيلية، وتقارير الرقابة والتحكم، حتى أصول الإغلاق المؤسسي:

```mermaid
flowchart TD
    G0["<b>المرحلة 00/01: الاستراتيجية والقيمة</b><br/>حالة الأعمال ومواءمة الأهداف"] --> G1["<b>المرحلة 02/03: البدء والمنهجية</b><br/>ميثاق المشروع ورؤية المنتج"]
    G1 --> G2["<b>المرحلة 04: خطوط الأساس والتخطيط</b><br/>النطاق، الجدول الزمني، والتكلفة"]
    G2 --> G3["<b>المرحلة 05: التنفيذ وبناء المخرجات</b><br/>سجلات المشكلات وطلبات التغيير"]
    G3 --> G4["<b>المرحلة 06: المراقبة والتحكم</b><br/>تقارير الأداء، EVA واختبارات القبول"]
    G4 --> G5["<b>المرحلة 07: الإغلاق والتحول التشغيلي</b><br/>التسليم للعمليات والدروس المستفادة"]
```

---

## 📋 جدول مصفوفة الاعتماديات الشاملة لكافة النماذج الـ 102

| الرمز | اسم المخرج الإداري | المرحلة / بوابة العبور | المدخلات المباشرة (Predecessors) | المخرجات المباشرة (Successors) |
| :---: | :--- | :--- | :--- | :--- |
"""
    for d in deliverables:
        p_prefix = d["code"][:2]
        gate_str_ar = GATE_MAP_AR.get(p_prefix, "بوابة الحوكمة العامة")
        
        if p_prefix == "00":
            preds_ar = "`الأهداف الاستراتيجية المؤسسية OKRs`"
            succs_ar = "`PMO-00.02 ميثاق البرنامج`، `PMO-03.01 ميثاق المشروع`"
        elif p_prefix == "01":
            preds_ar = "`PMO-00.01 خارطة طريق المحفظة`، `دراسة الجدوى`"
            succs_ar = "`PMO-03.01 ميثاق المشروع`، `PMO-01.03 خطة المنافع`"
        elif p_prefix == "02":
            preds_ar = "`PMO-01.01 حالة الأعمال`، `الاستراتيجية المؤسسية`"
            succs_ar = "`PMO-03.01 ميثاق المشروع`، `PMO-04.01.01 خطة إدارة المشروع`"
        elif p_prefix == "03":
            preds_ar = "`PMO-01.01 حالة الأعمال`، `PMO-02.01 تقييم المنهجية`"
            succs_ar = "`PMO-04.01.01 خطة إدارة المشروع`، `PMO-03.04 سجل المعنيين`"
        elif p_prefix == "04":
            preds_ar = "`PMO-03.01 ميثاق المشروع`، `PMO-03.03 سجل الافتراضات`"
            succs_ar = "`سجلات التنفيذ مرحلة 05`، `PMO-06.01 تقرير حالة المشروع`"
        elif p_prefix == "05":
            preds_ar = "`خطوط الأساس المعتمدة (النطاق/الجدول/التكلفة)`"
            succs_ar = "`PMO-06.01 تقرير الحالة`، `PMO-05.04 سجل التغييرات`"
        elif p_prefix == "06":
            preds_ar = "`خطوط الأساس لمرحلة 04`، `سجلات التنفيذ لمرحلة 05`"
            succs_ar = "`PMO-06.08 نموذج قبول المنتج`، `PMO-07.03 إغلاق المشروع`"
        else: # 07
            preds_ar = "`PMO-06.08 قبول المنتج`، `PMO-06.10 اعتماد اختبارات UAT`"
            succs_ar = "`PMO-07.04 التحول للعمليات`، `PMO-07.05 مراجعة ما بعد التنفيذ`"
            
        dep_ar += f"| **`{d['code']}`** | {d['name_ar']} | {gate_str_ar} | {preds_ar} | {succs_ar} |\n"
        
    (DOCS_DIR / "ar/07_document_dependencies.md").write_text(clean_manual_content(dep_ar, is_arabic=True), encoding="utf-8")

def clean_all_existing_manuals():
    print("Cleaning all 24 governance manual markdown files...")
    for f in sorted(list((DOCS_DIR / "en").glob("*.md"))):
        content = f.read_text(encoding="utf-8")
        cleaned = clean_manual_content(content, is_arabic=False)
        f.write_text(cleaned, encoding="utf-8")
        
    for f in sorted(list((DOCS_DIR / "ar").glob("*.md"))):
        content = f.read_text(encoding="utf-8")
        cleaned = clean_manual_content(content, is_arabic=True)
        f.write_text(cleaned, encoding="utf-8")

def main():
    deliverables = collect_deliverables()
    clean_all_existing_manuals()
    generate_raci_manuals(deliverables)
    generate_dependencies_manuals(deliverables)
    print("Governance manuals cleaned and rebuilt successfully!")

if __name__ == "__main__":
    main()
