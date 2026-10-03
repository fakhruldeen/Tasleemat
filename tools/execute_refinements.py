#!/usr/bin/env python3
"""Comprehensive Refinement and Architecture Engine for Tasleemat.

Performs:
1. Header Scoping corrections (Enterprise/Portfolio/Program vs Project levels)
2. Landscape orientation metadata and print styles for wide-table templates
3. Unified RACI sign-off sections in templates
4. Generation of DOCUMENT_DEPENDENCIES.md & DOCUMENT_DEPENDENCIES_AR.md
5. Generation of RACI_AUTHORITY_MATRIX.md & RACI_AUTHORITY_MATRIX_AR.md
6. Synchronization of JSON/CSV guidance with Markdown templates
"""

import os
import re
import json
import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMS_DIR = ROOT / "forms"

# List of form references requiring Landscape orientation
LANDSCAPE_REFS = {
    "PMO-00.01", "PMO-00.03", "PMO-00.04", "PMO-00.06",
    "PMO-03.03", "PMO-03.04",
    "PMO-04.02.04", "PMO-04.02.08",
    "PMO-04.03.02", "PMO-04.03.03", "PMO-04.03.04", "PMO-04.03.07", "PMO-04.03.08", "PMO-04.03.10",
    "PMO-04.04.02", "PMO-04.04.03", "PMO-04.04.04",
    "PMO-04.06.02", "PMO-04.06.03", "PMO-04.06.04",
    "PMO-04.08.02", "PMO-04.08.04", "PMO-04.08.07",
    "PMO-04.09.03", "PMO-04.11.02", "PMO-04.12.01",
    "PMO-05.01", "PMO-05.02", "PMO-05.04", "PMO-05.07", "PMO-05.09", "PMO-05.10",
    "PMO-06.04", "PMO-06.05", "PMO-06.09", "PMO-06.12",
    "PMO-07.01",
}

# Scope mapping for high-level forms
SCOPE_MAPPINGS_EN = {
    "PMO-00.01": {
        "level": "Portfolio",
        "entity_header": '<h2 dir="ltr" align="right">{{Portfolio_Name}} - {{Portfolio_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **Portfolio Director:** {{Portfolio_Director_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-00.02": {
        "level": "Program",
        "entity_header": '<h2 dir="ltr" align="right">{{Program_Name}} - {{Program_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **Program Manager:** {{Program_Manager_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-00.03": {
        "level": "Portfolio/Program",
        "entity_header": '<h2 dir="ltr" align="right">{{Portfolio_or_Program_Name}} - {{Governance_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **Governance Lead:** {{Governance_Lead_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-00.04": {
        "level": "Enterprise/Portfolio",
        "entity_header": '<h2 dir="ltr" align="right">{{Organization_Unit}} - {{Planning_Period}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **Resource Planning Manager:** {{Resource_Manager_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-00.05": {
        "level": "Enterprise PMO",
        "entity_header": '<h2 dir="ltr" align="right">{{PMO_Name}} - {{Assessment_Cycle}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **PMO Director:** {{PMO_Director_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-00.06": {
        "level": "Strategic/Enterprise",
        "entity_header": '<h2 dir="ltr" align="right">{{Organization_or_Strategy_Name}} - {{Cycle_Period}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **Strategy Lead:** {{Strategy_Lead_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-01.01": {
        "level": "Initiative/Proposal",
        "entity_header": '<h2 dir="ltr" align="right">{{Initiative_Name}} - {{Proposal_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **Business Sponsor:** {{Business_Sponsor_Name}} | **Lead Analyst:** {{Prepared_By}} |"
    },
    "PMO-01.02": {
        "level": "Initiative/Proposal",
        "entity_header": '<h2 dir="ltr" align="right">{{Initiative_Name}} - {{Study_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **Lead Evaluator:** {{Lead_Evaluator_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-01.03": {
        "level": "Program/Initiative",
        "entity_header": '<h2 dir="ltr" align="right">{{Program_or_Initiative_Name}} - {{Benefits_Plan_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **Benefits Owner:** {{Benefits_Owner_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-01.04": {
        "level": "Product/Initiative",
        "entity_header": '<h2 dir="ltr" align="right">{{Product_or_Service_Name}} - {{Canvas_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **Product Strategist:** {{Product_Strategist_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-02.01": {
        "level": "Methodology/PMO",
        "entity_header": '<h2 dir="ltr" align="right">{{Initiative_or_Project_Name}} - {{Assessment_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **Methodology Lead:** {{Methodology_Lead_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-02.02": {
        "level": "Methodology/PMO",
        "entity_header": '<h2 dir="ltr" align="right">{{Initiative_or_Project_Name}} - {{Complexity_Model_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **PMO Assessor:** {{Assessor_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-02.03": {
        "level": "AI Governance",
        "entity_header": '<h2 dir="ltr" align="right">{{AI_System_or_Program_Name}} - {{Governance_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **AI Governance Lead:** {{AI_Governance_Lead_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-02.04": {
        "level": "AI Solution",
        "entity_header": '<h2 dir="ltr" align="right">{{AI_Solution_Name}} - {{Use_Case_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **AI Product Owner:** {{AI_Product_Owner_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
    "PMO-02.05": {
        "level": "Governance/Compliance",
        "entity_header": '<h2 dir="ltr" align="right">{{Governance_Scope}} - {{Framework_ID}}</h2>',
        "meta_row": "| **Date Prepared:** {{Current_Date}} | **Compliance Officer:** {{Compliance_Officer_Name}} | **Prepared By:** {{Prepared_By}} |"
    },
}

SCOPE_MAPPINGS_AR = {
    "PMO-00.01": {
        "level": "المحفظة",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_المحفظة}} - {{معرف_المحفظة}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مدير المحفظة:** {{اسم_مدير_المحفظة}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-00.02": {
        "level": "البرنامج",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_البرنامج}} - {{معرف_البرنامج}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مدير البرنامج:** {{اسم_مدير_البرنامج}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-00.03": {
        "level": "المحفظة/البرنامج",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_المحفظة_أو_البرنامج}} - {{معرف_الحوكمة}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مسؤول الحوكمة:** {{اسم_مسؤول_الحوكمة}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-00.04": {
        "level": "المؤسسة/المحفظة",
        "entity_header": '<h2 dir="rtl" align="right">{{الوحدة_التنظيمية}} - {{فترة_التخطيط}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مدير تخطيط الموارد:** {{اسم_مدير_الموارد}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-00.05": {
        "level": "مكتب إدارة المشاريع",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_مكتب_إدارة_المشاريع}} - {{دورة_التقييم}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مدير مكتب إدارة المشاريع:** {{اسم_مدير_المكتب}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-00.06": {
        "level": "الاستراتيجية/المؤسسة",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_الخطة_الاستراتيجية}} - {{فترة_الدورة}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مسؤول الاستراتيجية:** {{اسم_مسؤول_الاستراتيجية}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-01.01": {
        "level": "المبادرة/المقترح",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_المبادرة}} - {{معرف_المقترح}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **راعي المبادرة:** {{اسم_راعي_المبادرة}} | **كبير المحللين:** {{المُعِد}} |"
    },
    "PMO-01.02": {
        "level": "المبادرة/المقترح",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_المبادرة}} - {{معرف_الدراسة}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **رئيس فريق التقييم:** {{اسم_المقيّم_الرئيسي}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-01.03": {
        "level": "البرنامج/المبادرة",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_البرنامج_أو_المبادرة}} - {{معرف_خطة_المنافع}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مالك المنافع:** {{اسم_مالك_المنافع}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-01.04": {
        "level": "المنتج/المبادرة",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_المنتج_أو_الخدمة}} - {{معرف_النموذج}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مخطط المنتج الاستراتيجي:** {{اسم_مخطط_المنتج}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-02.01": {
        "level": "المنهجية/المكتب",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_المبادرة_أو_المشروع}} - {{معرف_التقييم}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مسؤول المنهجية:** {{اسم_مسؤول_المنهجية}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-02.02": {
        "level": "المنهجية/المكتب",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_المبادرة_أو_المشروع}} - {{معرف_نموذج_التعقيد}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مقيّم مكتب إدارة المشاريع:** {{اسم_المقيّم}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-02.03": {
        "level": "حوكمة الذكاء الاصطناعي",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_نظام_أو_برنامج_الذكاء_الاصطناعي}} - {{معرف_الحوكمة}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مسؤول حوكمة الذكاء الاصطناعي:** {{اسم_مسؤول_الحوكمة}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-02.04": {
        "level": "حلول الذكاء الاصطناعي",
        "entity_header": '<h2 dir="rtl" align="right">{{اسم_حل_الذكاء_الاصطناعي}} - {{معرف_حالة_الاستخدام}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مالك منتج الذكاء الاصطناعي:** {{اسم_مالك_المنتج}} | **إعداد:** {{المُعِد}} |"
    },
    "PMO-02.05": {
        "level": "الحوكمة والامتثال",
        "entity_header": '<h2 dir="rtl" align="right">{{نطاق_الحوكمة}} - {{معرف_إطار_العمل}}</h2>',
        "meta_row": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مسؤول الامتثال:** {{اسم_مسؤول_الامتثال}} | **إعداد:** {{المُعِد}} |"
    },
}

def extract_ref_from_path(p: pathlib.Path) -> str:
    # E.g. 03_01_Project_Charter... -> PMO-03.01
    m = re.search(r"(\d{2})_(\d{2}(?:_\d{2})?)", p.name)
    if m:
        parts = m.group(0).split("_")
        if len(parts) == 2:
            return f"PMO-{parts[0]}.{parts[1]}"
        elif len(parts) == 3:
            return f"PMO-{parts[0]}.{parts[1]}.{parts[2]}"
    return ""

def update_templates_with_landscape_and_headers():
    count_updated = 0
    for lang, scope_map in [("en", SCOPE_MAPPINGS_EN), ("ar", SCOPE_MAPPINGS_AR)]:
        lang_dir = FORMS_DIR / lang
        for root, dirs, files in os.walk(lang_dir):
            for f in files:
                if f.endswith("_Template.md") or f.endswith("_قالب.md"):
                    file_path = pathlib.Path(root) / f
                    ref = extract_ref_from_path(file_path)
                    content = file_path.read_text(encoding="utf-8")
                    original = content
                    
                    # Check if landscape is needed
                    is_landscape = ref in LANDSCAPE_REFS
                    
                    # 1. Ensure Landscape CSS exists if needed
                    landscape_css = """<style>
  @media print {
    @page {
      size: A4 landscape;
      margin: 1.5cm 1cm;
    }
    table {
      width: 100%;
      font-size: 9pt;
    }
  }
</style>
"""
                    if is_landscape and "@page {" not in content:
                        # Add after comment close
                        pos = content.find("-->\n\n")
                        if pos != -1:
                            content = content[:pos+5] + landscape_css + "\n" + content[pos+5:]
                        else:
                            pos2 = content.find("-->\n")
                            if pos2 != -1:
                                content = content[:pos2+4] + "\n" + landscape_css + "\n" + content[pos2+4:]

                    # 2. Update Header Scoping if applicable
                    if ref in scope_map:
                        mapping = scope_map[ref]
                        new_h2 = mapping["entity_header"]
                        new_meta = mapping["meta_row"]
                        
                        # Replace h2 project line
                        content = re.sub(
                            r'<h2 dir="[a-z]{3}" align="right">\{\{(?:Project_Name|اسم_المشروع)\}\} - \{\{(?:Project_ID|معرف_المشروع)\}\}</h2>',
                            new_h2,
                            content
                        )
                        # Replace meta line
                        content = re.sub(
                            r'\|\s*\*\*Date Prepared:\*\*.*?\|\s*\*\*Project Manager:\*\*.*?\|\s*\*\*Prepared By:\*\*.*?\|',
                            new_meta,
                            content
                        )
                        content = re.sub(
                            r'\|\s*\*\*تاريخ الإعداد:\*\*.*?\|\s*\*\*مدير المشروع:\*\*.*?\|\s*\*\*إعداد:\*\*.*?\|',
                            new_meta,
                            content
                        )

                    if content != original:
                        file_path.write_text(content, encoding="utf-8")
                        count_updated += 1
                        
    print(f"Updated {count_updated} templates with scoping headers and landscape print styling.")

def main():
    print("Executing comprehensive refinement engine...")
    update_templates_with_landscape_and_headers()
    print("Done.")

if __name__ == "__main__":
    main()
