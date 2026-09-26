import os
import re

base_dir_en = "/home/mohamed/Desktop/PMOSKILL/forms"
base_dir_ar = "/home/mohamed/Desktop/PMOSKILL/forms_ar"

def get_id_prefix(rel_path):
    parts = rel_path.split(os.sep)
    nums = []
    for p in parts:
        match = re.match(r'^(\d+)', p)
        if match:
            nums.append(match.group(1))
    if nums:
        return "_".join(nums) + "_"
    return ""

def rename_and_update(base_dir, is_arabic):
    for root, dirs, files in os.walk(base_dir):
        # Skip if root is base_dir or a top-level dir like '04_Planning'
        rel_path = os.path.relpath(root, base_dir)
        if rel_path == "." or os.sep not in rel_path and not any(f.endswith('.json') for f in files):
            continue
            
        prefix = get_id_prefix(rel_path)
        if not prefix:
            continue
            
        # Rename files
        old_to_new = {}
        for file in files:
            # Avoid double renaming if script is run twice
            if re.match(r'^\d+_\d+', file):
                continue
                
            if file == "index.md":
                continue
                
            new_name = prefix + file
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            old_to_new[file] = new_name
            
        # Read the newly named Guide file and update the download links at the bottom
        for file in os.listdir(root):
            if file.endswith("_Guide.md"):
                guide_path = os.path.join(root, file)
                with open(guide_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Update links
                for old_f, new_f in old_to_new.items():
                    # Markdown links look like ](Filename.md)
                    content = content.replace(f"]({old_f})", f"]({new_f})")
                    content = content.replace(f"](./{old_f})", f"](./{new_f})")
                    
                with open(guide_path, 'w', encoding='utf-8') as f:
                    f.write(content)

def rebuild_indexes(base_dir, is_arabic):
    top_dirs = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    for td in top_dirs:
        td_path = os.path.join(base_dir, td)
        td_clean = td.split("_", 1)[1].replace("_", " ") if "_" in td else td
        
        index_path = os.path.join(td_path, 'index.md')
        if not os.path.exists(index_path):
            continue
            
        # Re-generate the index entirely
        with open(index_path, 'w', encoding='utf-8') as f:
            idx = top_dirs.index(td)
            f.write(f"---\nlayout: default\ntitle: {td_clean}\nhas_children: true\nnav_order: {idx + 2}\n---\n\n")
            f.write(f"# {td_clean}\n\n")
            if is_arabic:
                f.write(f"اختر أحد المخرجات أدناه لعرض الدليل الشامل وتحميل القوالب:\n\n")
            else:
                f.write(f"Select an artifact below to view its comprehensive guide and download the associated templates:\n\n")
            
            # Find all guides in this td
            form_entries = []
            for root, dirs, files in os.walk(td_path):
                guides = [f for f in files if f.endswith("_Guide.md")]
                for g in guides:
                    rel_to_td = os.path.relpath(os.path.join(root, g), td_path)
                    
                    # Extract the ID from the file name
                    doc_id_match = re.match(r'^(\d+(?:_\d+)+)_', g)
                    doc_id_formatted = "PMO-XX"
                    if doc_id_match:
                        doc_id_formatted = "PMO-" + doc_id_match.group(1).replace("_", ".")
                        
                    # Extract the readable name (strip prefix and _Guide.md)
                    clean_name = g
                    if doc_id_match:
                        clean_name = clean_name[len(doc_id_match.group(0)):]
                    clean_name = clean_name.replace("_Guide.md", "").replace("_", " ")
                    
                    form_entries.append((doc_id_formatted, clean_name, rel_to_td))
                    
            form_entries.sort(key=lambda x: x[2])
            
            for doc_id, name, path in form_entries:
                f.write(f"* **{doc_id}**: [{name}]({path})\n")

rename_and_update(base_dir_en, False)
rename_and_update(base_dir_ar, True)

rebuild_indexes(base_dir_en, False)
rebuild_indexes(base_dir_ar, True)

print("Files renamed with ID prefixes successfully.")
