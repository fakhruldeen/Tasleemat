import re
import json
import csv
import os

# Read the generated txt file
with open('/home/mohamed/Desktop/PMOSKILL/forms.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

tables = {}
current_table = None
current_field = None
current_desc = []

for i, line in enumerate(lines):
    line = line.strip()
    
    table_match = re.match(r'^Table\s+\d+\.\d+\s+(?: | )*Elements of a?n?\s+(.*?)(?:\s+\(continued\))?$', line, re.IGNORECASE)
    if table_match:
        form_name = table_match.group(1).strip()
        if form_name.lower() == "lessons learned summary":
            pass
        if form_name not in tables:
            tables[form_name] = []
        current_table = form_name
        current_field = None
        continue
        
    if current_table:
        if line == "Document Element" or line == "Description":
            continue
        
        if line.startswith("Page ") or re.match(r'^Table\s+', line) or line == "Description":
            if current_field:
                tables[current_table].append((current_field, " ".join(current_desc)))
                current_field = None
            current_table = None
            continue
            
        if line.isupper() and len(line) > 5 and line not in ["ID", "WBS", "OBS", "RACI"]:
            if current_field:
                tables[current_table].append((current_field, " ".join(current_desc)))
                current_field = None
            current_table = None
            continue

        if line:
            if len(line) < 40 and not line.endswith('.') and lines[i-1].strip() == "":
                if current_field:
                    tables[current_table].append((current_field, " ".join(current_desc)))
                current_field = line
                current_desc = []
            else:
                if current_field:
                    current_desc.append(line)

# Clean up
for form in tables:
    cleaned = []
    for f, d in tables[form]:
        f = f.strip().strip(":")
        d = d.strip()
        if f and f.lower() not in ["identifier", "project title", "page"]:
            cleaned.append((f, d))
    
    seen = set()
    dedup = []
    for f, d in cleaned:
        if f.lower() not in seen:
            seen.add(f.lower())
            dedup.append((f, d))
            
    tables[form] = dedup

base_dir = "/home/mohamed/Desktop/PMOSKILL/forms"

structure = {
    "1 Initiating Forms": [
        "1.1 Project Charter",
        "1.2 Assumption Log",
        "1.3 Stakeholder Register",
        "1.4 Stakeholder Analysis"
    ],
    "2 Planning Forms": [
        "2.1 Project Management Plan",
        "2.2 Change Management Plan",
        "2.3 Project Roadmap",
        "2.4 Scope Management Plan",
        "2.5 Requirements Management Plan",
        "2.6 Requirements Documentation",
        "2.7 Requirements Traceability Matrix",
        "2.8 Project Scope Statement",
        "2.9 Work Breakdown Structure",
        "2.10 WBS Dictionary",
        "2.11 Schedule Management Plan",
        "2.12 Activity List",
        "2.13 Activity Attributes",
        "2.14 Milestone List",
        "2.15 Network Diagram",
        "2.16 Duration Estimates",
        "2.17 Duration Estimating Worksheet",
        "2.18 Project Schedule",
        "2.19 Cost Management Plan",
        "2.20 Cost Estimates",
        "2.21 Cost Estimating Worksheet",
        "2.22 Cost Baseline",
        "2.23 Quality Management Plan",
        "2.24 Quality Metrics",
        "2.25 Responsibility Assignment Matrix",
        "2.26 Resource Management Plan",
        "2.27 Team Charter",
        "2.28 Resource Requirements",
        "2.29 Resource Breakdown Structure",
        "2.30 Communications Management Plan",
        "2.31 Risk Management Plan",
        "2.32 Risk Register",
        "2.33 Risk Report",
        "2.34 Probability and Impact Assessment",
        "2.35 Probability and Impact Matrix",
        "2.36 Risk Data Sheet",
        "2.37 Procurement Management Plan",
        "2.38 Procurement Strategy",
        "2.39 Source Selection Criteria",
        "2.40 Stakeholder Engagement Plan"
    ],
    "3 Executing Forms": [
        "3.1 Issue Log",
        "3.2 Decision Log",
        "3.3 Change Request",
        "3.4 Change Log",
        "3.5 Lessons Learned Register",
        "3.6 Quality Audit",
        "3.7 Team Performance Assessment"
    ],
    "4 Monitoring and Controlling Forms": [
        "4.1 Team Member Status Report",
        "4.2 Project Status Report",
        "4.3 Variance Analysis",
        "4.4 Earned Value Analysis",
        "4.5 Risk Audit",
        "4.6 Contractor Status Report",
        "4.7 Procurement Audit",
        "4.8 Contract Closeout Report",
        "4.9 Product Acceptance Form"
    ],
    "5 Closing": [
        "5.1 Lessons Learned Summary",
        "5.2 Project or Phase Closeout"
    ],
    "6 Agile": [
        "6.1 Product Vision",
        "6.2 Product Backlog",
        "6.3 Release Plan",
        "6.4 Retrospective"
    ]
}

def find_fields(form_name):
    clean_form_name = form_name.split(" ", 1)[1]
    for k in tables:
        if k.lower() == clean_form_name.lower():
            return tables[k]
    for k in tables:
        if clean_form_name.lower() in k.lower() or k.lower() in clean_form_name.lower():
            return tables[k]
    import difflib
    matches = difflib.get_close_matches(clean_form_name, tables.keys(), n=1, cutoff=0.6)
    if matches:
        return tables[matches[0]]
    return []

for chapter, forms in structure.items():
    chapter_dir = os.path.join(base_dir, chapter.replace(" ", "_"))
    for form in forms:
        form_name = form.split(" ", 1)[1]
        form_dir = os.path.join(chapter_dir, form.replace(" ", "_"))
        
        fields = find_fields(form)
        
        # Markdown Template (Visual)
        md_path = os.path.join(form_dir, f"{form_name.replace(' ', '_')}.md")
        with open(md_path, 'w') as f:
            f.write(f"---\ntitle: {form_name}\n---\n\n")
            f.write(f"<div align=\"center\">\n  <h1>{form_name.upper()}</h1>\n</div>\n\n")
            f.write("<!-- \nLLM INSTRUCTIONS:\nFill out the template below. Replace all instances of `[ ... ]` or empty spaces with the relevant project content.\n-->\n\n")
            
            # Header info
            f.write("**Project Title:** `[Enter Project Title]` hfill **Date Prepared:** `[Enter Date]`  \n")
            if "manager" in form_name.lower() or "charter" in form_name.lower():
                f.write("**Project Manager:** `[Enter Name]` hfill **Project Sponsor:** `[Enter Name]`  \n")
            f.write("\n---\n\n")
            
            if fields:
                # If there are many fields with short names like ID, Category, Status, we can format them as a table
                table_fields = []
                box_fields = []
                
                for field, desc in fields:
                    if len(desc) < 100 and len(field) < 20 and ("id" in field.lower() or "status" in field.lower() or "date" in field.lower() or "category" in field.lower() or "priority" in field.lower()):
                        table_fields.append((field, desc))
                    else:
                        box_fields.append((field, desc))
                
                if len(table_fields) > 2:
                    f.write("| " + " | ".join([x[0] for x in table_fields]) + " |\n")
                    f.write("|" + "|".join(["---" for x in table_fields]) + "|\n")
                    f.write("| " + " | ".join([" `[ ... ]` " for x in table_fields]) + " |\n\n")
                    
                # Handle box fields
                for field, desc in (box_fields if len(table_fields) > 2 else fields):
                    f.write(f"### {field}\n")
                    f.write(f"> *{desc}*\n\n")
                    f.write("```text\n[ Provide your detailed response here... ]\n```\n\n")
                    
            else:
                f.write("### Content\n")
                f.write("> *Please insert the appropriate content for this form here.*\n\n")
                f.write("```text\n[ Provide your detailed response here... ]\n```\n\n")
                
        # JSON Template
        json_path = os.path.join(form_dir, f"{form_name.replace(' ', '_')}.json")
        with open(json_path, 'w') as f:
            json_template = {
                "_llm_instructions": f"Fill out the 'value' properties for each field in this {form_name} template based on the provided project context.",
                "form_name": form_name,
                "project_title": "",
                "date_prepared": "",
                "fields": {}
            }
            if fields:
                for field, desc in fields:
                    json_template["fields"][field] = {
                        "guidance": desc,
                        "value": ""
                    }
            json.dump(json_template, f, indent=4)
            
        # CSV Template
        csv_path = os.path.join(form_dir, f"{form_name.replace(' ', '_')}.csv")
        with open(csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Field", "Guidance", "LLM_Generated_Value"])
            if fields:
                for field, desc in fields:
                    writer.writerow([field, desc, ""])

print("Visual Markdown templates successfully generated.")
