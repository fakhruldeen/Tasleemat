#!/usr/bin/env python3
"""Fix scoping headers in higher level documents and replace <style> tags with clean metadata."""

import os
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMS_DIR = ROOT / "forms"

SCOPE_FIXES = {
    # 00
    "00_01": {
        "en_h2": '<h2 dir="ltr" align="right">{{Portfolio_Name}} - {{Portfolio_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Portfolio Director:** {{Portfolio_Director_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_المحفظة}} - {{معرف_المحفظة}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مدير المحفظة:** {{اسم_مدير_المحفظة}} | **إعداد:** {{المُعِد}} |"
    },
    "00_02": {
        "en_h2": '<h2 dir="ltr" align="right">{{Program_Name}} - {{Program_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Program Manager:** {{Program_Manager_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_البرنامج}} - {{معرف_البرنامج}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مدير البرنامج:** {{اسم_مدير_البرنامج}} | **إعداد:** {{المُعِد}} |"
    },
    "00_03": {
        "en_h2": '<h2 dir="ltr" align="right">{{Portfolio_or_Program_Name}} - {{Governance_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Governance Lead:** {{Governance_Lead_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_المحفظة_أو_البرنامج}} - {{معرف_الحوكمة}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مسؤول الحوكمة:** {{اسم_مسؤول_الحوكمة}} | **إعداد:** {{المُعِد}} |"
    },
    "00_04": {
        "en_h2": '<h2 dir="ltr" align="right">{{Organization_Unit}} - {{Planning_Period}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Resource Planning Manager:** {{Resource_Manager_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{الوحدة_التنظيمية}} - {{فترة_التخطيط}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مدير تخطيط الموارد:** {{اسم_مدير_الموارد}} | **إعداد:** {{المُعِد}} |"
    },
    "00_05": {
        "en_h2": '<h2 dir="ltr" align="right">{{PMO_Name}} - {{Assessment_Cycle}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **PMO Director:** {{PMO_Director_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_مكتب_إدارة_المشاريع}} - {{دورة_التقييم}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مدير مكتب إدارة المشاريع:** {{اسم_مدير_المكتب}} | **إعداد:** {{المُعِد}} |"
    },
    "00_06": {
        "en_h2": '<h2 dir="ltr" align="right">{{Organization_or_Strategy_Name}} - {{Cycle_Period}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Strategy Lead:** {{Strategy_Lead_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_الخطة_الاستراتيجية}} - {{فترة_الدورة}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مسؤول الاستراتيجية:** {{اسم_مسؤول_الاستراتيجية}} | **إعداد:** {{المُعِد}} |"
    },
    # 01
    "01_01": {
        "en_h2": '<h2 dir="ltr" align="right">{{Initiative_Name}} - {{Proposal_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Business Sponsor:** {{Business_Sponsor_Name}} | **Lead Analyst:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_المبادرة}} - {{معرف_المقترح}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **راعي المبادرة:** {{اسم_راعي_المبادرة}} | **كبير المحللين:** {{المُعِد}} |"
    },
    "01_02": {
        "en_h2": '<h2 dir="ltr" align="right">{{Initiative_Name}} - {{Study_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Lead Evaluator:** {{Lead_Evaluator_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_المبادرة}} - {{معرف_الدراسة}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **رئيس فريق التقييم:** {{اسم_المقيّم_الرئيسي}} | **إعداد:** {{المُعِد}} |"
    },
    "01_03": {
        "en_h2": '<h2 dir="ltr" align="right">{{Program_or_Initiative_Name}} - {{Benefits_Plan_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Benefits Owner:** {{Benefits_Owner_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_البرنامج_أو_المبادرة}} - {{معرف_خطة_المنافع}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مالك المنافع:** {{اسم_مالك_المنافع}} | **إعداد:** {{المُعِد}} |"
    },
    "01_04": {
        "en_h2": '<h2 dir="ltr" align="right">{{Product_or_Service_Name}} - {{Canvas_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Product Strategist:** {{Product_Strategist_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_المنتج_أو_الخدمة}} - {{معرف_النموذج}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مخطط المنتج الاستراتيجي:** {{اسم_مخطط_المنتج}} | **إعداد:** {{المُعِد}} |"
    },
    # 02
    "02_01": {
        "en_h2": '<h2 dir="ltr" align="right">{{Initiative_or_Project_Name}} - {{Assessment_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Methodology Lead:** {{Methodology_Lead_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_المبادرة_أو_المشروع}} - {{معرف_التقييم}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مسؤول المنهجية:** {{اسم_مسؤول_المنهجية}} | **إعداد:** {{المُعِد}} |"
    },
    "02_02": {
        "en_h2": '<h2 dir="ltr" align="right">{{Initiative_or_Project_Name}} - {{Complexity_Model_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **PMO Assessor:** {{Assessor_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_المبادرة_أو_المشروع}} - {{معرف_نموذج_التعقيد}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مقيّم مكتب إدارة المشاريع:** {{اسم_المقيّم}} | **إعداد:** {{المُعِد}} |"
    },
    "02_03": {
        "en_h2": '<h2 dir="ltr" align="right">{{AI_System_or_Program_Name}} - {{Governance_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **AI Governance Lead:** {{AI_Governance_Lead_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_نظام_أو_برنامج_الذكاء_الاصطناعي}} - {{معرف_الحوكمة}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مسؤول حوكمة الذكاء الاصطناعي:** {{اسم_مسؤول_الحوكمة}} | **إعداد:** {{المُعِد}} |"
    },
    "02_04": {
        "en_h2": '<h2 dir="ltr" align="right">{{AI_Solution_Name}} - {{Use_Case_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **AI Product Owner:** {{AI_Product_Owner_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_حل_الذكاء_الاصطناعي}} - {{معرف_حالة_الاستخدام}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مالك منتج الذكاء الاصطناعي:** {{اسم_مالك_المنتج}} | **إعداد:** {{المُعِد}} |"
    },
    "02_05": {
        "en_h2": '<h2 dir="ltr" align="right">{{Governance_Scope}} - {{Framework_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Compliance Officer:** {{Compliance_Officer_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{نطاق_الحوكمة}} - {{معرف_إطار_العمل}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مسؤول الامتثال:** {{اسم_مسؤول_الامتثال}} | **إعداد:** {{المُعِد}} |"
    },
    # 03_02 Product Vision
    "03_02": {
        "en_h2": '<h2 dir="ltr" align="right">{{Product_Name}} - {{Product_ID}}</h2>',
        "en_meta": "| **Date Prepared:** {{Current_Date}} | **Product Owner:** {{Product_Owner_Name}} | **Prepared By:** {{Prepared_By}} |",
        "ar_h2": '<h2 dir="rtl" align="left">{{اسم_المنتج}} - {{معرف_المنتج}}</h2>',
        "ar_meta": "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مالك المنتج:** {{اسم_مالك_المنتج}} | **إعداد:** {{المُعِد}} |"
    },
}

def clean_all_style_tags_and_fix_headers():
    cleaned_styles_count = 0
    headers_fixed_count = 0

    for root, dirs, files in os.walk(FORMS_DIR):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = pathlib.Path(root) / f
            content = path.read_text(encoding="utf-8")
            original = content

            # 1. Remove <style>...</style> completely
            if "<style>" in content or "<style " in content:
                content = re.sub(r"(?is)<style\b[^>]*>.*?</style>\n*", "", content)
                cleaned_styles_count += 1

            # 2. Check if this file belongs to a higher level form
            # Extract key like 00_01, 01_02, etc.
            m = re.search(r"(\d{2})_(\d{2})", f)
            if m:
                key = f"{m.group(1)}_{m.group(2)}"
                if key in SCOPE_FIXES:
                    fixes = SCOPE_FIXES[key]
                    is_ar = "/ar/" in str(path)
                    
                    if is_ar:
                        # Fix AR h2
                        content = re.sub(
                            r'<h2\s+dir="[a-z]{3}"\s+align="(?:left|right)">\{\{اسم_المشروع\}\}\s*-\s*\{\{معرف_المشروع\}\}</h2>',
                            fixes["ar_h2"],
                            content
                        )
                        # Fix AR meta row
                        content = re.sub(
                            r'\|\s*\*\*تاريخ الإعداد:\*\*.*?\|\s*\*\*مدير المشروع:\*\*.*?\|\s*\*\*إعداد:\*\*.*?\|',
                            fixes["ar_meta"],
                            content
                        )
                    else:
                        # Fix EN h2
                        content = re.sub(
                            r'<h2\s+dir="[a-z]{3}"\s+align="(?:left|right)">\{\{Project_Name\}\}\s*-\s*\{\{Project_ID\}\}</h2>',
                            fixes["en_h2"],
                            content
                        )
                        # Fix EN meta row
                        content = re.sub(
                            r'\|\s*\*\*Date Prepared:\*\*.*?\|\s*\*\*Project Manager:\*\*.*?\|\s*\*\*Prepared By:\*\*.*?\|',
                            fixes["en_meta"],
                            content
                        )
                    headers_fixed_count += 1

            if content != original:
                path.write_text(content, encoding="utf-8")

    print(f"Removed <style> blocks from {cleaned_styles_count} files.")
    print(f"Verified/updated scoping headers across {headers_fixed_count} template files.")

if __name__ == "__main__":
    clean_all_style_tags_and_fix_headers()
