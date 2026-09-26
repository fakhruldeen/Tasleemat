import os
import json

base_dir = "/home/mohamed/Desktop/PMOSKILL/forms"

table_keywords = ["log", "register", "matrix", "list", "worksheet", "assessment", "metrics", "schedule", "estimates"]
exceptions = ["project schedule", "schedule management plan", "cost management plan", "quality management plan", "risk management plan", "procurement management plan", "stakeholder engagement plan", "communications management plan", "requirements management plan", "scope management plan", "change management plan", "project management plan", "team performance assessment", "probability and impact assessment", "risk data sheet", "procurement strategy", "source selection criteria", "requirements documentation"]

for root, dirs, files in os.walk(base_dir):
    json_files = [f for f in files if f.endswith(".json")]
    if not json_files:
        continue
        
    for jf in json_files:
        json_path = os.path.join(root, jf)
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
        except Exception as e:
            continue
            
        form_name = data.get("form_name", "")
        if not form_name:
            continue
            
        fields = data.get("fields", {})
        
        lower_name = form_name.lower()
        is_table = False
        if any(kw in lower_name for kw in table_keywords) and lower_name not in exceptions:
            is_table = True
        if "roadmap" in lower_name or "retrospective" in lower_name:
            is_table = True
            
        # Generate [FormName].md (Detailed Instructions for LLM)
        md_instr_path = os.path.join(root, jf.replace(".json", ".md"))
        with open(md_instr_path, 'w') as f:
            f.write(f"---\nForm: {form_name} (Instructions)\n---\n\n")
            f.write(f"# {form_name.upper()} - LLM GENERATION GUIDE\n\n")
            f.write("> **System Prompt / Instructions:**\n")
            f.write(f"> This document serves as the detailed instruction set for generating the `{form_name}`. ")
            f.write("When asked to populate this form, use the guidance provided for each section below to accurately generate the required content. ")
            f.write("Reference `parameters.md` for global project variables.\n\n")
            f.write("---\n\n")
            
            for field, info in fields.items():
                f.write(f"### {field}\n")
                f.write(f"**Instruction:** {info.get('guidance', '')}\n\n")
                
        # Generate [FormName]_Template.md (Printable Template)
        md_temp_path = os.path.join(root, jf.replace(".json", "_Template.md"))
        with open(md_temp_path, 'w') as f:
            f.write(f"<div align=\"center\">\n  <h1>{form_name.upper()}</h1>\n</div>\n\n")
            f.write("**Project Name:** ___________________________ | **Date:** ___________________________\n\n")
            f.write("**Project Manager:** ________________________ | **Prepared By:** ____________________\n\n")
            f.write("---\n\n")
            
            if is_table:
                headers = list(fields.keys())
                if headers:
                    f.write("| " + " | ".join(headers) + " |\n")
                    f.write("|" + "|".join(["---" for _ in headers]) + "|\n")
                    for _ in range(10):
                        f.write("| " + " | ".join(["" for _ in headers]) + " |\n")
                    f.write("\n")
                else:
                    f.write("*(No specific columns defined)*\n")
            else:
                for field in fields.keys():
                    f.write(f"### {field}\n")
                    f.write("<br><br><br><br>\n\n")

print("Files successfully restructured.")
