import os

base_dir = "/home/mohamed/Desktop/PMOSKILL/forms"

with open(os.path.join(base_dir, 'mapping.md'), 'w', encoding='utf-8') as f:
    f.write("# PMO Lifecycle Artifacts Mapping\n\n")
    f.write("This document is the ultimate index of all PMO artifacts, templates, and forms currently available in the repository. They are organized sequentially by the project lifecycle.\n\n")
    
    # Get all top-level directories, sorted
    top_dirs = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    
    for td in top_dirs:
        td_path = os.path.join(base_dir, td)
        td_clean = td.split("_", 1)[1].replace("_", " ") if "_" in td else td
        
        f.write(f"## {td_clean}\n")
        f.write("| Artifact Name | Directory Path |\n")
        f.write("| --- | --- |\n")
        
        # We need to walk through and find where the .md / .json files are
        # Since some are nested (like 04_Planning/01_Integration), we'll do os.walk
        
        form_entries = []
        for root, dirs, files in os.walk(td_path):
            for file in files:
                if file.endswith(".json"):
                    rel_path = os.path.relpath(root, base_dir)
                    form_name = file.replace(".json", "").replace("_", " ")
                    form_entries.append((form_name, rel_path))
                    
        # Sort by rel_path to keep them in numerical order
        form_entries.sort(key=lambda x: x[1])
        
        for name, path in form_entries:
            f.write(f"| {name} | `{path}` |\n")
            
        f.write("\n")

print("Rebuilt mapping.md successfully.")
