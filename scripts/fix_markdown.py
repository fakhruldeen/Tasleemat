import os
import json

base_dir = "/home/mohamed/Desktop/PMOSKILL/forms"

# List of keywords that imply the form should be a table
table_keywords = ["log", "register", "matrix", "list", "worksheet", "assessment", "metrics", "schedule", "estimates"]
# Forms that shouldn't be tables despite having a keyword
exceptions = ["project schedule", "schedule management plan", "cost management plan", "quality management plan", "risk management plan", "procurement management plan", "stakeholder engagement plan", "communications management plan", "requirements management plan", "scope management plan", "change management plan", "project management plan", "team performance assessment", "probability and impact assessment", "risk data sheet", "procurement strategy", "source selection criteria", "requirements documentation"]

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".json"):
            json_path = os.path.join(root, f)
            with open(json_path, 'r') as jf:
                data = json.load(jf)
            
            form_name = data.get("form_name", "")
            fields = data.get("fields", {})
            
            md_path = os.path.join(root, f.replace(".json", ".md"))
            
            # Determine if it should be a table
            is_table = False
            lower_name = form_name.lower()
            
            if any(kw in lower_name for kw in table_keywords) and lower_name not in exceptions:
                is_table = True
            if "roadmap" in lower_name or "retrospective" in lower_name:
                is_table = True
                
            # Generate MD
            with open(md_path, 'w') as md:
                md.write(f"---\nForm: {form_name}\n---\n\n")
                md.write(f"# {form_name.upper()}\n\n")
                md.write("**Project Title:** `[Enter Project Title]` &nbsp;&nbsp;&nbsp;&nbsp; **Date Prepared:** `[Enter Date]`\n\n")
                md.write("---\n\n")
                
                if is_table:
                    # Generate a markdown table
                    headers = list(fields.keys())
                    if headers:
                        md.write("| " + " | ".join(headers) + " |\n")
                        md.write("|" + "|".join(["---" for _ in headers]) + "|\n")
                        # Add a few empty rows
                        for _ in range(5):
                            md.write("| " + " | ".join(["" for _ in headers]) + " |\n")
                        md.write("\n\n*Field Guidance:*\n")
                        for h in headers:
                            md.write(f"- **{h}:** {fields[h]['guidance']}\n")
                    else:
                        md.write("*(No specific fields defined)*\n")
                else:
                    # Generate sections
                    for field, info in fields.items():
                        md.write(f"### {field}\n")
                        md.write(f"*{info['guidance']}*\n\n")
                        md.write("> [Enter your response here]\n\n")
                        md.write("---\n\n")

print("Markdown files updated successfully.")
