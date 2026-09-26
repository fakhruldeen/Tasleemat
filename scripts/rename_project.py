import os
import re

base_dir_en = "/home/mohamed/Desktop/PMOSKILL/forms"
base_dir_ar = "/home/mohamed/Desktop/PMOSKILL/forms_ar"

# Using lists to enforce replacement order (longer phrases first)
en_replacements = [
    (r"PMBOK Standard Guide", "Tasleemat Forms Guide"),
    (r"Project Management Institute \(PMI\) standards", "Tasleemat framework"),
    (r"Project Management Institute \(PMI\)", "Tasleemat framework"),
    (r"PMI standards", "Tasleemat standards"),
    (r"PMI-aligned", "Tasleemat-aligned"),
    (r"PMBOK standards", "Tasleemat standards"),
    (r"PMBOK Forms Mapping", "Tasleemat Forms Mapping"),
    (r"PMBOK 8th Edition", "Tasleemat Advanced Standards"),
    (r"PMBOK 8th Ed\.", "Tasleemat Advanced Standards"),
    (r"PMBOK® Guide", "Tasleemat framework"),
    (r"\bPMBOK\b", "Tasleemat"),
    (r"\bPMI\b", "Tasleemat"),
    (r"\bPMP\b", "Project Professional")
]

ar_replacements = [
    (r"الدليل الشامل لمعايير إدارة المشاريع", "دليل نماذج تسليمات"),
    (r"معهد إدارة المشاريع \(PMI\)", "منهجية تسليمات"),
    (r"معايير PMBOK", "معايير تسليمات"),
    (r"معايير PMI", "معايير تسليمات"),
    (r"منهجية معهد إدارة المشاريع \(PMI\)", "منهجية تسليمات"),
    (r"\bPMBOK\b", "تسليمات"),
    (r"\bPMI\b", "تسليمات"),
    (r"\bPMP\b", "محترف مشاريع")
]

def replace_in_files(base_dir, replacements):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith((".md", ".json", ".csv")):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    original_content = content
                    
                    for pattern, replacement in replacements:
                        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                        
                    if content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

print("Applying English replacements...")
replace_in_files(base_dir_en, en_replacements)

print("Applying Arabic replacements...")
replace_in_files(base_dir_ar, ar_replacements)

print("Project successfully renamed to Tasleemat (تسليمات).")
