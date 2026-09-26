import os
import re

base_dir_en = "/home/mohamed/Desktop/PMOSKILL/forms"
base_dir_ar = "/home/mohamed/Desktop/PMOSKILL/forms_ar"

def get_doc_id(rel_path):
    parts = rel_path.split(os.sep)
    nums = []
    for p in parts:
        match = re.match(r'^(\d+)', p)
        if match:
            nums.append(match.group(1))
    if nums:
        return "PMO-" + ".".join(nums)
    return "PMO-XX"

def update_files(base_dir, is_arabic):
    for root, dirs, files in os.walk(base_dir):
        rel_path = os.path.relpath(root, base_dir)
        if rel_path == ".":
            continue
            
        doc_id = get_doc_id(rel_path)
        if doc_id == "PMO-XX":
            continue
            
        # 1. Update _Template.md
        templates = [f for f in files if f.endswith("_Template.md")]
        for t in templates:
            t_path = os.path.join(root, t)
            with open(t_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check if already injected
            if "Doc Ref:" not in content and "مرجع الوثيقة:" not in content:
                ref_text = f"مرجع الوثيقة: <b>{doc_id}</b>" if is_arabic else f"Doc Ref: <b>{doc_id}</b>"
                align = "left" if is_arabic else "right" # In RTL, left is opposite of start
                
                target = '<table width="100%" style="border-collapse: collapse; border: none; margin-bottom: 20px;">\n  <tr>'
                replacement = f'<table width="100%" style="border-collapse: collapse; border: none; margin-bottom: 20px;">\n  <tr>\n    <td align="{align}" style="font-size: 12px; color: #7f8c8d; padding-bottom: 5px;">{ref_text}</td>\n  </tr>\n  <tr>'
                
                new_content = content.replace(target, replacement)
                with open(t_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                    
        # 2. Update _Guide.md
        guides = [f for f in files if f.endswith("_Guide.md")]
        for g in guides:
            g_path = os.path.join(root, g)
            with open(g_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if "**Document Reference:**" not in content and "**مرجع الوثيقة:**" not in content:
                if is_arabic:
                    target = re.search(r'# المخرج \(Artifact\): (.*?)\n', content)
                    if target:
                        replacement = f"{target.group(0)}\n**مرجع الوثيقة:** `{doc_id}`\n"
                        content = content.replace(target.group(0), replacement)
                else:
                    target = re.search(r'# Project Artifact: (.*?)\n', content)
                    if target:
                        replacement = f"{target.group(0)}\n**Document Reference:** `{doc_id}`\n"
                        content = content.replace(target.group(0), replacement)
                        
                with open(g_path, 'w', encoding='utf-8') as f:
                    f.write(content)

def rebuild_mapping(base_dir):
    with open(os.path.join(base_dir, 'mapping.md'), 'w', encoding='utf-8') as f:
        f.write("# PMO Lifecycle Artifacts Mapping\n\n")
        f.write("This document is the ultimate index of all PMO artifacts, templates, and forms currently available in the repository. They are organized sequentially by the project lifecycle and assigned a unique Document Reference ID.\n\n")
        
        top_dirs = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
        
        for td in top_dirs:
            td_path = os.path.join(base_dir, td)
            td_clean = td.split("_", 1)[1].replace("_", " ") if "_" in td else td
            
            f.write(f"## {td_clean}\n")
            f.write("| Doc ID | Artifact Name | Directory Path |\n")
            f.write("| --- | --- | --- |\n")
            
            form_entries = []
            for root, dirs, files in os.walk(td_path):
                for file in files:
                    if file.endswith(".json"):
                        rel_path = os.path.relpath(root, base_dir)
                        form_name = file.replace(".json", "").replace("_", " ")
                        doc_id = get_doc_id(rel_path)
                        form_entries.append((doc_id, form_name, rel_path))
                        
            form_entries.sort(key=lambda x: x[2])
            
            for doc_id, name, path in form_entries:
                f.write(f"| **{doc_id}** | {name} | `{path}` |\n")
            f.write("\n")

def rebuild_indexes(base_dir, is_arabic):
    top_dirs = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    for td in top_dirs:
        td_path = os.path.join(base_dir, td)
        td_clean = td.split("_", 1)[1].replace("_", " ") if "_" in td else td
        
        index_path = os.path.join(td_path, 'index.md')
        if not os.path.exists(index_path):
            continue
            
        with open(index_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        new_lines = []
        for line in lines:
            if line.startswith("* ["):
                # Extract path to calculate doc id
                match = re.search(r'\((.*?)\)', line)
                if match:
                    guide_rel = match.group(1)
                    full_rel = os.path.join(td, guide_rel)
                    doc_id = get_doc_id(os.path.dirname(full_rel))
                    # Insert doc id into the link text
                    name_match = re.search(r'\[(.*?)\]', line)
                    if name_match:
                        name = name_match.group(1)
                        line = f"* **{doc_id}**: [{name}]({guide_rel})\n"
            new_lines.append(line)
            
        with open(index_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

update_files(base_dir_en, False)
update_files(base_dir_ar, True)

rebuild_mapping(base_dir_en)

rebuild_indexes(base_dir_en, False)
rebuild_indexes(base_dir_ar, True)

print("Document numbering applied globally.")
