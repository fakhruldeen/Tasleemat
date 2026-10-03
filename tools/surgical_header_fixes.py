#!/usr/bin/env python3
"""Surgically clean up all remaining project placeholders in higher-level documents (00, 01, 02)."""

import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

EXACT_REPLACEMENTS = [
    # 00_05 PMO Maturity Assessment AR
    (
        "forms/ar/00_إدارة_البرامج_والمحافظ/05_تقييم_نضج_مكتب_إدارة_المشاريع/00_05_تقييم_نضج_مكتب_إدارة_المشاريع_قالب.md",
        "| **تاريخ الإعداد:** {{تاريخ_اليوم}} | **مدير المشروع:** {{اسم_مدير_المشروع}} | **أُعد بواسطة:** {{اسم_المُعد}} |",
        "| **تاريخ الإعداد:** {{تاريخ_اليوم}} | **مدير مكتب إدارة المشاريع:** {{اسم_مدير_المكتب}} | **أُعد بواسطة:** {{اسم_المُعد}} |"
    ),
    # 00_06 OKR Alignment AR
    (
        "forms/ar/00_إدارة_البرامج_والمحافظ/06_مصفوفة_مواءمة_الأهداف_والنتائج_الرئيسية/00_06_مصفوفة_مواءمة_الأهداف_والنتائج_الرئيسية_قالب.md",
        "| **تاريخ الإعداد:** {{تاريخ_اليوم}} | **مدير المشروع:** {{اسم_مدير_المشروع}} | **أُعد بواسطة:** {{اسم_المُعد}} |",
        "| **تاريخ الإعداد:** {{تاريخ_اليوم}} | **مسؤول الاستراتيجية:** {{اسم_مسؤول_الاستراتيجية}} | **أُعد بواسطة:** {{اسم_المُعد}} |"
    ),
    # 01_04 Gap Analysis Report AR
    (
        "forms/ar/01_الأعمال_وتسليم_القيمة/04_تقرير_تحليل_الفجوات/01_04_تقرير_تحليل_الفجوات_قالب.md",
        "| **تاريخ الإعداد:** {{تاريخ_اليوم}} | **مدير المشروع:** {{اسم_مدير_المشروع}} | **أُعد بواسطة:** {{اسم_المُعد}} |",
        "| **تاريخ الإعداد:** {{تاريخ_اليوم}} | **كبير محللي الأعمال:** {{اسم_كبير_المحللين}} | **أُعد بواسطة:** {{اسم_المُعد}} |"
    ),
    # 02_01 Tailoring Plan AR & EN
    (
        "forms/ar/02_منهجية_المشروع_وتخصيصه/01_خطة_التخصيص/02_01_خطة_التخصيص_قالب.md",
        "| **مدير المشروع** | {{اسم_مدير_المشروع}} |",
        "| **مسؤول المنهجية** | {{اسم_مسؤول_المنهجية}} |"
    ),
    (
        "forms/en/02_Project_Approach_and_Tailoring/01_Tailoring_Plan/02_01_Tailoring_Plan_Template.md",
        "| **Project Manager** | {{Project_Manager_Name}} |",
        "| **Methodology Lead** | {{Methodology_Lead_Name}} |"
    ),
    # 02_06 Data Privacy & Ethics AR
    (
        "forms/ar/02_منهجية_المشروع_وتخصيصه/06_تقييم_خصوصية_البيانات_وأخلاقياتها/02_06_تقييم_خصوصية_البيانات_وأخلاقياتها_قالب.md",
        "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مدير المشروع:** {{اسم_مدير_المشروع}} | **إعداد:** {{معد_الوثيقة}} |",
        "| **تاريخ الإعداد:** {{التاريخ_الحالي}} | **مسؤول خصوصية البيانات:** {{اسم_مسؤول_الخصوصية}} | **إعداد:** {{معد_الوثيقة}} |"
    ),
]

def apply_surgical_fixes():
    fixed = 0
    for rel_path, old_text, new_text in EXACT_REPLACEMENTS:
        file_path = ROOT / rel_path
        if file_path.exists():
            content = file_path.read_text(encoding="utf-8")
            if old_text in content:
                content = content.replace(old_text, new_text)
                file_path.write_text(content, encoding="utf-8")
                fixed += 1
                print(f"Fixed placeholder in: {rel_path}")
            else:
                print(f"Old text not found in: {rel_path}")
        else:
            print(f"File does not exist: {rel_path}")

    print(f"Applied {fixed} surgical placeholder replacements.")

if __name__ == "__main__":
    apply_surgical_fixes()
