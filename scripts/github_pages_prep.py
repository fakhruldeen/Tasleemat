import os

base_dir_en = "/home/mohamed/Desktop/PMOSKILL/forms"
base_dir_ar = "/home/mohamed/Desktop/PMOSKILL/forms_ar"

def add_github_pages_features(base_dir, is_arabic):
    # Walk through the directory to find guides and update them
    for root, dirs, files in os.walk(base_dir):
        guides = [f for f in files if f.endswith("_Guide.md")]
        
        # Get phase name for navigation/frontmatter
        rel_path = os.path.relpath(root, base_dir)
        top_level_dir = rel_path.split(os.sep)[0]
        
        for guide in guides:
            guide_path = os.path.join(root, guide)
            form_name = guide.replace("_Guide.md", "").replace("_", " ")
            form_basename = guide.replace("_Guide.md", "")
            
            with open(guide_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check if frontmatter already exists
            if not content.startswith("---"):
                # Prepare Frontmatter
                frontmatter = f"---\nlayout: default\ntitle: {form_name}\nnav_order: 1\n---\n\n"
                
                # Prepare Downloads Section
                if is_arabic:
                    downloads = f"\n\n### 📥 القوالب المرتبطة\n"
                    downloads += f"* [📄 القالب القابل للطباعة (Markdown)]({form_basename}_Template.md)\n"
                    downloads += f"* [🤖 تعليمات النموذج الذكي (LLM)]({form_basename}.md)\n"
                    downloads += f"* [📊 هيكل البيانات (JSON)]({form_basename}.json)\n"
                    downloads += f"* [📈 البيانات المجدولة (CSV)]({form_basename}.csv)\n"
                else:
                    downloads = f"\n\n### 📥 Associated Templates\n"
                    downloads += f"* [📄 Printable Template (Markdown)]({form_basename}_Template.md)\n"
                    downloads += f"* [🤖 LLM Generation Prompt]({form_basename}.md)\n"
                    downloads += f"* [📊 Data Schema (JSON)]({form_basename}.json)\n"
                    downloads += f"* [📈 Tabular Data (CSV)]({form_basename}.csv)\n"
                
                # Insert downloads before the closing </div> if it exists
                if "</div>" in content:
                    content = content.replace("</div>", downloads + "\n</div>")
                else:
                    content += downloads
                    
                # Write back with frontmatter
                with open(guide_path, 'w', encoding='utf-8') as f:
                    f.write(frontmatter + content)

def generate_index_files(base_dir, is_arabic):
    # Create root index
    root_title = "مكتبة قوالب إدارة المشاريع" if is_arabic else "PMO Toolkit Library"
    root_desc = "دليل شامل وقوالب احترافية متوافقة مع معهد إدارة المشاريع (PMI)." if is_arabic else "A comprehensive, PMI-aligned guide and template library for Project Managers."
    
    with open(os.path.join(base_dir, 'index.md'), 'w', encoding='utf-8') as f:
        f.write(f"---\nlayout: default\ntitle: Home\nnav_order: 1\n---\n\n")
        f.write(f"# {root_title}\n\n")
        f.write(f"{root_desc}\n\n")
        f.write("Please select a project phase from the navigation menu to explore the artifacts.\n")
        
    # Create index for each top-level directory (Phases)
    top_dirs = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    
    for idx, td in enumerate(top_dirs):
        td_path = os.path.join(base_dir, td)
        td_clean = td.split("_", 1)[1].replace("_", " ") if "_" in td else td
        
        with open(os.path.join(td_path, 'index.md'), 'w', encoding='utf-8') as f:
            f.write(f"---\nlayout: default\ntitle: {td_clean}\nhas_children: true\nnav_order: {idx + 2}\n---\n\n")
            f.write(f"# {td_clean}\n\n")
            if is_arabic:
                f.write(f"اختر أحد المخرجات أدناه لعرض الدليل الشامل وتحميل القوالب:\n\n")
            else:
                f.write(f"Select an artifact below to view its comprehensive guide and download the associated templates:\n\n")
            
            # Link to all guides in this phase
            for root, dirs, files in os.walk(td_path):
                guides = sorted([f for f in files if f.endswith("_Guide.md")])
                for guide in guides:
                    rel_to_td = os.path.relpath(os.path.join(root, guide), td_path)
                    name = guide.replace("_Guide.md", "").replace("_", " ")
                    f.write(f"* [{name}]({rel_to_td})\n")

add_github_pages_features(base_dir_en, False)
generate_index_files(base_dir_en, False)

add_github_pages_features(base_dir_ar, True)
generate_index_files(base_dir_ar, True)

print("GitHub Pages optimizations completed.")
