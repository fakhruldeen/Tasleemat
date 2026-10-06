#!/usr/bin/env python3
import os
import sys
import re

FILES = [
    "forms/en/03_Initiating/01_Project_Charter/03_01_Project_Charter_Template.md",
    "forms/en/04_Planning/08_Risk/02_Risk_Register/04_08_02_Risk_Register_Template.md",
    "forms/en/06_Monitoring_and_Controlling/01_Project_Status_Report/06_01_Project_Status_Report_Template.md",
    "forms/en/06_Monitoring_and_Controlling/05_Earned_Value_Analysis/06_05_Earned_Value_Analysis_Template.md",
    "forms/en/07_Closing/04_Transition_to_Operations_Checklist/07_04_Transition_to_Operations_Checklist_Template.md",
    "forms/ar/03_البدء/01_ميثاق_المشروع/03_01_ميثاق_المشروع_قالب.md",
    "forms/ar/04_التخطيط/08_المخاطر/02_سجل_المخاطر/04_08_02_سجل_المخاطر_قالب.md",
    "forms/ar/06_المراقبة_والتحكم/01_تقرير_حالة_المشروع/06_01_تقرير_حالة_المشروع_قالب.md",
    "forms/ar/06_المراقبة_والتحكم/05_تحليل_القيمة_المكتسبة_(EVA)/06_05_تحليل_القيمة_المكتسبة_(EVA)_قالب.md",
    "forms/ar/07_الإغلاق/04_قائمة_التحقق_للانتقال_إلى_العمليات/07_04_قائمة_التحقق_للانتقال_إلى_العمليات_قالب.md"
]

def migrate():
    for filepath in FILES:
        if not os.path.exists(filepath):
            print(f"Error: {filepath} not found")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if not content.startswith('---'):
            continue
            
        end_idx = content.find('\n---', 3)
        if end_idx == -1:
            continue
            
        frontmatter = content[3:end_idx]
        body = content[end_idx+4:]
        
        # Extract ID (e.g. 03_01 or 04_08_02)
        basename = os.path.basename(filepath)
        id_match = re.match(r'^(\d+_\d+(?:_\d+)?).*', basename)
        if not id_match:
            continue
            
        form_id = f"PMO-{id_match.group(1).replace('_', '.')}"
        
        # Language
        lang = "en" if "/en/" in filepath else "ar"
        
        # We need to make sure form_id, language, status are present.
        # But we must be idempotent.
        if "form_id:" not in frontmatter:
            frontmatter += f"\nform_id: {form_id}"
            
        if "language:" not in frontmatter and "lang:" not in frontmatter:
            frontmatter += f"\nlanguage: {lang}"
            
        if "status:" not in frontmatter:
            frontmatter += f"\nstatus: approved"
            
        # Clean up double newlines in frontmatter
        frontmatter = re.sub(r'\n\n+', '\n', frontmatter)
        
        new_content = f"---{frontmatter}\n---{body}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    print("Migration pilot successful.")

if __name__ == '__main__':
    migrate()
