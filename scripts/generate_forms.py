import os
import json
import csv

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

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

for chapter, forms in structure.items():
    chapter_dir = os.path.join(base_dir, chapter.replace(" ", "_"))
    if not os.path.exists(chapter_dir):
        os.makedirs(chapter_dir)
    
    for form in forms:
        form_name = form.split(" ", 1)[1]
        form_dir = os.path.join(chapter_dir, form.replace(" ", "_"))
        if not os.path.exists(form_dir):
            os.makedirs(form_dir)
            
        md_path = os.path.join(form_dir, f"{form_name.replace(' ', '_')}.md")
        with open(md_path, 'w') as f:
            f.write(f"# {form_name}\n\n")
            f.write(f"This is the {form_name} document.\n")
            
        json_path = os.path.join(form_dir, f"{form_name.replace(' ', '_')}.json")
        with open(json_path, 'w') as f:
            json.dump({"form_name": form_name, "fields": []}, f, indent=4)
            
        csv_path = os.path.join(form_dir, f"{form_name.replace(' ', '_')}.csv")
        with open(csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Field", "Value"])
            writer.writerow(["Form Name", form_name])

print("Directories and files created successfully.")
