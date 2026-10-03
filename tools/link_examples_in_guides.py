#!/usr/bin/env python3
"""
link_examples_in_guides.py

Injects or updates reference links to the newly generated 102 English and 102 Arabic
example templates inside all *_Guide.md and *_دليل.md files.
Properly handles parenthesized URLs using `<...>` markdown wrapper.
"""

import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORMS_EN_DIR = os.path.join(BASE_DIR, "forms", "en")
FORMS_AR_DIR = os.path.join(BASE_DIR, "forms", "ar")
EXAMPLES_EN_DIR = os.path.join(BASE_DIR, "examples", "en")
EXAMPLES_AR_DIR = os.path.join(BASE_DIR, "examples", "ar")

def re_remove_section(content: str, is_arabic: bool) -> str:
    if is_arabic:
        content = re.sub(r'\n*---\s*\n*### 6\.\s*نموذج تطبيقي[\s\S]*?(?=<\/div>|$)', '', content)
    else:
        content = re.sub(r'\n*---\s*\n*### 6\.\s*Reference Example[\s\S]*?(?=<\/div>|$)', '', content)
    return content

def link_en_guides():
    updated = 0
    for root, dirs, files in os.walk(FORMS_EN_DIR):
        for f in files:
            if f.endswith('_Guide.md'):
                guide_path = os.path.join(root, f)
                rel_dir = os.path.relpath(root, FORMS_EN_DIR)
                example_name = f.replace('_Guide.md', '_Example.md')
                example_path = os.path.join(EXAMPLES_EN_DIR, rel_dir, example_name)
                
                if not os.path.exists(example_path):
                    print(f"Warning: Example not found for {guide_path}")
                    continue
                    
                rel_link = os.path.relpath(example_path, start=root)
                # If path contains parentheses or spaces, wrap with <...>
                link_target = f"<{rel_link}>" if ('(' in rel_link or ' ' in rel_link) else rel_link
                
                with open(guide_path, 'r', encoding='utf-8') as fp:
                    content = fp.read()
                    
                content = re_remove_section(content, is_arabic=False)
                
                # Construct Section 6 block
                section_block = (
                    "\n\n---\n\n"
                    "### 6. Reference Example\n"
                    "A fully completed, gold-standard reference example illustrating this artifact in practice is available:\n"
                    f"> 📖 **Completed Example:** [{example_name}]({link_target})\n"
                )
                
                if "</div>" in content:
                    idx = content.rfind("</div>")
                    new_content = content[:idx].rstrip() + section_block + "\n</div>\n"
                else:
                    new_content = content.rstrip() + section_block
                    
                with open(guide_path, 'w', encoding='utf-8') as fp:
                    fp.write(new_content)
                updated += 1
                
    print(f"Updated {updated} English Guide files.")

def link_ar_guides():
    updated = 0
    for root, dirs, files in os.walk(FORMS_AR_DIR):
        for f in files:
            if f.endswith('_دليل.md'):
                guide_path = os.path.join(root, f)
                rel_dir = os.path.relpath(root, FORMS_AR_DIR)
                example_name = f.replace('_دليل.md', '_مثال.md')
                example_path = os.path.join(EXAMPLES_AR_DIR, rel_dir, example_name)
                
                if not os.path.exists(example_path):
                    print(f"Warning: Example not found for {guide_path}")
                    continue
                    
                rel_link = os.path.relpath(example_path, start=root)
                link_target = f"<{rel_link}>" if ('(' in rel_link or ' ' in rel_link) else rel_link
                
                with open(guide_path, 'r', encoding='utf-8') as fp:
                    content = fp.read()
                    
                content = re_remove_section(content, is_arabic=True)
                
                # Construct Arabic Section 6 block
                section_block = (
                    "\n\n---\n\n"
                    "### 6. نموذج تطبيقي معبأ (مثال استرشادي)\n"
                    "يتوفر نموذج تطبيقي مكتمل وعالي الجودة يوضح كيفية تعبئة واستخدام هذا المستند عملياً:\n"
                    f"> 📖 **النموذج التطبيقي المكتمل:** [{example_name}]({link_target})\n"
                )
                
                if "</div>" in content:
                    idx = content.rfind("</div>")
                    new_content = content[:idx].rstrip() + section_block + "\n</div>\n"
                else:
                    new_content = content.rstrip() + section_block
                    
                with open(guide_path, 'w', encoding='utf-8') as fp:
                    fp.write(new_content)
                updated += 1
                
    print(f"Updated {updated} Arabic Guide files.")

if __name__ == '__main__':
    link_en_guides()
    link_ar_guides()
