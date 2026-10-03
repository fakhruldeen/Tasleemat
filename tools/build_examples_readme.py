#!/usr/bin/env python3
"""
build_examples_readme.py

Generates complete, beautifully formatted examples/README.md and examples/README_AR.md
indexing all 102 forms with direct links to both English and Arabic examples.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

phases = [
    ('00_Program_and_Portfolio_Management', '00_إدارة_البرامج_والمحافظ', '00. Program & Portfolio Management', '00. إدارة البرامج والمحافظ'),
    ('01_Business_and_Value_Delivery', '01_الأعمال_وتسليم_القيمة', '01. Business & Value Delivery', '01. الأعمال وتسليم القيمة'),
    ('02_Project_Approach_and_Tailoring', '02_نهج_المشروع_والمواءمة', '02. Project Approach & Tailoring', '02. نهج المشروع والمواءمة'),
    ('03_Initiating', '03_البدء', '03. Initiating Phase', '03. مرحلة البدء'),
    ('04_Planning', '04_التخطيط', '04. Planning Phase', '04. مرحلة التخطيط'),
    ('05_Executing', '05_التنفيذ', '05. Executing Phase', '05. مرحلة التنفيذ'),
    ('06_Monitoring_and_Controlling', '06_المراقبة_والتحكم', '06. Monitoring & Controlling Phase', '06. مرحلة المراقبة والتحكم'),
    ('07_Closing', '07_الإغلاق', '07. Closing Phase', '07. مرحلة الإغلاق')
]

en_md = '''# 🏆 Tasleemat Gold-Standard Reference Examples
**Directory:** `examples/`  
**Coverage:** 102 Bilingual Forms (204 Completed Reference Artifacts)  

---

## 🎯 Overview
This directory contains fully populated, production-grade **reference examples for all 102 PMO artifacts** in both English (`examples/en/`) and Arabic (`examples/ar/`).

Every artifact demonstrates realistic, high-caliber PMBOK 6/7/8, Agile, Hybrid, ESG, and AI governance implementations using consistent, fictional enterprise scenarios:
* **Apex Global Solutions / شركة القمة للحلول المؤسسية المتقدمة** (Enterprise Holding)
* **Nexus ERP & Smart Supply Chain** (`PRJ-2026-ERP-01`)
* **NextGen Cloud Infrastructure Program** (`PGM-2026-CX`)
* **Enterprise Digital Modernization Portfolio** (`PORT-2026-X01`)

> **Notice:** All company names, projects, and personal names are purely fictional simulations created for educational and operational benchmarking.

---

## 📚 Complete Artifact Index (102 Examples)

'''

ar_md = '''# 🏆 النماذج التطبيقية الاسترشادية الشاملة - إطار تسليمات
**دليل النماذج:** `examples/`  
**نطاق التغطية:** 102 نموذجاً ثنائي اللغة (204 ملفاً تطبيقياً مكتملاً)  

---

## 🎯 نظرة عامة
يحتوي هذا المجلد على **نماذج تطبيقية استرشادية مكتملة ومعبأة بالكامل لجميع نماذج تسليمات الـ 102** باللغتين العربية (`examples/ar/`) والإنجليزية (`examples/en/`).

تجسد هذه النماذج أعلى المعايير المهنية المعتمدة دولياً في إدارة المشاريع (PMBOK 6/7/8)، والمنهجيات الرشيقة، والحوكمة، والاستدامة المؤسسية، وحوكمة الذكاء الاصطناعي، اعتماداً على سيناريوهات مؤسسية افتراضية متكاملة:
* **شركة القمة للحلول المؤسسية المتقدمة** (المؤسسة القابضة الافتراضية)
* **مشروع المنظومة السحابية الموحدة لتخطيط الموارد وسلاسل الإمداد** (`PRJ-2026-ERP-01`)
* **برنامج البنية التحتية السحابية والخدمات الرقمية** (`PGM-2026-CX`)
* **محفظة التحول الرقمي وتحديث العمليات المؤسسية** (`PORT-2026-X01`)

> **تنبيه:** كافة أسماء الشركات والمشاريع والأشخاص المذكورة هي نماذج افتراضية ومحاكاة مهنية لأغراض الاسترشاد والتدريب والامتثال.

---

## 📚 الفهرس الشامل للنماذج التطبيقية (102 نموذج)

'''

for en_phase, ar_phase, en_title, ar_title in phases:
    en_md += f"### {en_title}\n\n| Ref ID | Artifact Name | English Example | Arabic Example |\n| :---: | :--- | :---: | :---: |\n"
    ar_md += f"### {ar_title}\n\n| رمز المستند | اسم المستند | النموذج بالعربية | النموذج بالإنجليزية |\n| :---: | :--- | :---: | :---: |\n"
    
    en_dir = os.path.join(BASE_DIR, 'examples', 'en', en_phase)
    items = []
    for root, dirs, files in os.walk(en_dir):
        for f in files:
            if f.endswith('_Example.md'):
                en_path = os.path.join(root, f)
                rel_en = os.path.relpath(en_path, os.path.join(BASE_DIR, 'examples'))
                
                parts = f.replace('_Example.md', '').split('_')
                num_parts = [p for p in parts if p.isdigit()]
                code = '_'.join(num_parts)
                doc_ref = "PMO-" + '.'.join(num_parts)
                clean_name = ' '.join([p for p in parts if not p.isdigit()])
                
                ar_dir = os.path.join(BASE_DIR, 'examples', 'ar', ar_phase)
                ar_match_rel = ''
                ar_clean_name = ''
                for ar_root, ar_dirs, ar_files in os.walk(ar_dir):
                    for af in ar_files:
                        if af.endswith('_مثال.md'):
                            af_nums = [p for p in af.replace('_مثال.md', '').split('_') if p.isdigit()]
                            if '_'.join(af_nums) == code:
                                ar_path = os.path.join(ar_root, af)
                                ar_match_rel = os.path.relpath(ar_path, os.path.join(BASE_DIR, 'examples'))
                                ar_clean_name = ' '.join([p for p in af.replace('_مثال.md', '').split('_') if not p.isdigit()])
                                break
                items.append((code, doc_ref, clean_name, ar_clean_name, rel_en, ar_match_rel))
    
    items.sort(key=lambda x: [int(n) for n in x[0].split('_')])
    for code, doc_ref, clean_name, ar_clean_name, rel_en, rel_ar in items:
        safe_en = f"<{rel_en}>" if ('(' in rel_en or ' ' in rel_en) else rel_en
        safe_ar = f"<{rel_ar}>" if ('(' in rel_ar or ' ' in rel_ar) else rel_ar
        en_md += f"| `{doc_ref}` | **{clean_name}** | [English Example]({safe_en}) | [Arabic Example]({safe_ar}) |\n"
        ar_md += f"| `{doc_ref}` | **{ar_clean_name or clean_name}** | [النموذج بالعربية]({safe_ar}) | [English Example]({safe_en}) |\n"
        
    en_md += "\n---\n\n"
    ar_md += "\n---\n\n"

with open(os.path.join(BASE_DIR, 'examples', 'README.md'), 'w', encoding='utf-8') as fp:
    fp.write(en_md)
with open(os.path.join(BASE_DIR, 'examples', 'README_AR.md'), 'w', encoding='utf-8') as fp:
    fp.write(ar_md)

print("Generated clean examples/README.md and examples/README_AR.md successfully.")
