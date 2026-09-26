import os
import json
import csv

base_dir_en = "/home/mohamed/Desktop/PMOSKILL/forms"
base_dir_ar = "/home/mohamed/Desktop/PMOSKILL/forms_ar"

EN_PARAMS = {
    "title": "Project Name: `{{Project_Name}}` | Date: `{{Current_Date}}`",
    "header2": "Project Manager: `{{Project_Manager_Name}}` | Prepared By: `{{Prepared_By}}`",
    "instructions": "<!-- \nLLM INSTRUCTIONS:\nFill out the template below. Replace all instances of `[ ... ]` or empty spaces with the relevant project content. Use `parameters.md` for context.\n-->",
    "box_prompt": "[ Provide your detailed response here... ]"
}

AR_PARAMS = {
    "title": "اسم المشروع: `{{Project_Name}}` | التاريخ: `{{Current_Date}}`",
    "header2": "مدير المشروع: `{{Project_Manager_Name}}` | إعداد: `{{Prepared_By}}`",
    "instructions": "<!-- \nتعليمات للنموذج الذكي (LLM):\nقم بملء النموذج أدناه. استبدل جميع العلامات `[ ... ]` أو المساحات الفارغة بمحتوى المشروع ذي الصلة. استخدم `parameters.md` كمرجع.\n-->",
    "box_prompt": "[ أدخل استجابتك المفصلة هنا... ]"
}

NEW_ARTIFACTS = {
    "08_Program_and_Portfolio_Management": {
        "01_Portfolio_Roadmap": {
            "ar_name": "خارطة طريق المحفظة",
            "is_table": True,
            "fields": {
                "Program/Project Name": "Name of the initiative.",
                "Strategic Objective": "Which strategic goal this maps to.",
                "Start Date": "Expected start quarter/date.",
                "End Date": "Expected end quarter/date.",
                "Budget Estimate": "High level budget allocation.",
                "Status": "Current status."
            }
        },
        "02_Program_Charter": {
            "ar_name": "ميثاق البرنامج",
            "is_table": False,
            "fields": {
                "Program Purpose": "High-level justification for the program.",
                "Program Objectives": "Measurable goals of the program.",
                "Component Projects": "List of the individual projects within the program.",
                "Program Benefits": "Expected synergistic benefits.",
                "Program Manager Authority": "Authority level of the program manager."
            }
        },
        "03_Interdependency_Register": {
            "ar_name": "سجل الاعتماديات المتبادلة",
            "is_table": True,
            "fields": {
                "Dependency ID": "Unique ID.",
                "Predecessor Project": "Project that must finish first.",
                "Successor Project": "Project waiting on the predecessor.",
                "Deliverable/Condition": "What specifically is being waited on.",
                "Required Date": "When the deliverable is needed.",
                "Status": "On track, Delayed, etc."
            }
        },
        "04_Resource_Capacity_Matrix": {
            "ar_name": "مصفوفة سعة الموارد",
            "is_table": True,
            "fields": {
                "Resource Role/Team": "Skillset or team name.",
                "Total Available Capacity": "Total hours/FTE available.",
                "Allocated Capacity": "Hours/FTE already assigned.",
                "Remaining Capacity": "Available hours/FTE.",
                "Critical Constraints": "Any bottlenecks or single points of failure."
            }
        }
    },
    "09_Agile_and_Lean_Artifacts": {
        "01_User_Story_Mapping_Canvas": {
            "ar_name": "نموذج تخطيط قصص المستخدم",
            "is_table": False,
            "fields": {
                "User Persona": "Who the user is.",
                "User Activities (The Backbone)": "High-level tasks the user needs to accomplish.",
                "User Tasks (The Slices)": "Specific steps under each activity.",
                "MVP Release 1": "Stories critical for the first release.",
                "Future Releases": "Stories planned for later."
            }
        },
        "02_Definition_of_Ready_and_Done": {
            "ar_name": "تعريف الجاهزية والاكتمال",
            "is_table": False,
            "fields": {
                "Definition of Ready (DoR)": "Criteria a story must meet before entering a sprint (e.g., clear acceptance criteria, estimated).",
                "Definition of Done (DoD)": "Criteria a story must meet to be considered complete (e.g., coded, tested, documented, approved)."
            }
        },
        "03_Sprint_Planning_Log": {
            "ar_name": "سجل تخطيط أسبوع العمل",
            "is_table": True,
            "fields": {
                "Sprint Goal": "The overarching goal of the sprint.",
                "Story ID": "Jira or board reference.",
                "Story Points": "Estimated effort.",
                "Assignee": "Who is working on it.",
                "Acceptance Criteria": "High level criteria for success."
            }
        },
        "04_Impediment_Log": {
            "ar_name": "سجل العوائق",
            "is_table": True,
            "fields": {
                "Impediment ID": "Unique ID.",
                "Date Raised": "When it was identified.",
                "Description": "What is blocking the team.",
                "Impact": "How it affects the sprint.",
                "Owner": "Scrum Master or person resolving it.",
                "Status": "Open, In Progress, Resolved."
            }
        }
    },
    "10_Organizational_Change_Management": {
        "01_OCM_Strategy_and_Plan": {
            "ar_name": "استراتيجية وخطة إدارة التغيير المؤسسي",
            "is_table": False,
            "fields": {
                "Change Vision": "Why the human change is necessary.",
                "Stakeholder Impact Analysis": "How different groups will be affected.",
                "Communication Strategy": "How changes will be communicated.",
                "Resistance Management": "How to handle pushback from users.",
                "Sponsorship Strategy": "How leaders will champion the change."
            }
        },
        "02_Training_Plan_and_Log": {
            "ar_name": "خطة وسجل التدريب",
            "is_table": True,
            "fields": {
                "Target Audience": "Who needs training.",
                "Training Module": "What they are learning.",
                "Delivery Method": "In-person, webinar, self-paced.",
                "Date/Schedule": "When training occurs.",
                "Completion Status": "Number of users completed."
            }
        },
        "03_Transition_to_Operations_Checklist": {
            "ar_name": "قائمة التحقق للانتقال إلى العمليات",
            "is_table": True,
            "fields": {
                "Checklist Item": "e.g., Code deployed, Support manuals written.",
                "Responsible Party": "Who owns the item.",
                "Sign-off Signature": "Approval.",
                "Date": "When completed.",
                "Notes": "Any handover details."
            }
        }
    },
    "11_Advanced_Procurement_and_Contracts": {
        "01_Statement_of_Work_SOW": {
            "ar_name": "بيان العمل (SOW)",
            "is_table": False,
            "fields": {
                "Scope of Work": "Detailed description of vendor work.",
                "Period of Performance": "Start and end dates.",
                "Deliverables Schedule": "Specific milestones and due dates.",
                "Applicable Standards": "Technical or quality standards to adhere to.",
                "Acceptance Criteria": "How the buyer will accept the deliverables."
            }
        },
        "02_Request_for_Proposal_RFP": {
            "ar_name": "طلب تقديم عروض (RFP)",
            "is_table": False,
            "fields": {
                "Project Overview": "Background and purpose of the project.",
                "Submission Guidelines": "How and when vendors should submit proposals.",
                "Technical Requirements": "What the solution must do.",
                "Evaluation Criteria": "How proposals will be scored.",
                "Terms and Conditions": "Legal and compliance baselines."
            }
        },
        "03_Vendor_Performance_Scorecard": {
            "ar_name": "بطاقة أداء المورد",
            "is_table": True,
            "fields": {
                "Metric/KPI": "What is being measured (e.g., Quality, Timeliness).",
                "Target Score": "Expected performance level.",
                "Actual Score": "Measured performance.",
                "Variance": "Difference between target and actual.",
                "Corrective Action": "Steps to improve if deficient."
            }
        }
    },
    "12_Advanced_AI_and_Data_Governance": {
        "01_AI_Model_Card_and_Fact_Sheet": {
            "ar_name": "بطاقة نموذج الذكاء الاصطناعي",
            "is_table": False,
            "fields": {
                "Model Details": "Architecture, version, developer.",
                "Intended Use": "Primary and secondary use cases.",
                "Factors": "Demographics or environmental factors affecting performance.",
                "Metrics": "Accuracy, precision, recall, etc.",
                "Training Data": "Datasets used to train the model.",
                "Ethical Considerations": "Potential risks or biases."
            }
        },
        "02_Data_Privacy_and_Ethics_Assessment": {
            "ar_name": "تقييم خصوصية البيانات وأخلاقياتها",
            "is_table": False,
            "fields": {
                "Data Source": "Where the data originates.",
                "PII Detection": "Does it contain Personally Identifiable Information?",
                "Consent Management": "How user consent was obtained.",
                "Data Retention Policy": "How long data is stored and how it's deleted.",
                "Compliance Alignment": "GDPR, CCPA, or local regulatory alignment."
            }
        }
    }
}

def generate_html_form(form_name, fields, is_table, is_arabic):
    if is_arabic:
        title_label = "اسم المشروع:"
        date_label = "التاريخ:"
        pm_label = "مدير المشروع:"
        prep_label = "إعداد:"
        instructions = AR_PARAMS["instructions"]
        placeholder = AR_PARAMS["box_prompt"]
        dir_attr = 'dir="rtl"'
        font_family = "font-family: Arial, sans-serif;"
        prep_sig = "تم الإعداد بواسطة:"
        rev_sig = "تمت المراجعة بواسطة:"
        app_sig = "تم الاعتماد بواسطة:"
        date_sig = "التاريخ:"
        timestamp_text = "تاريخ الإنشاء: {{Current_Timestamp}}"
        timestamp_align = "left"
    else:
        title_label = "Project Title:"
        date_label = "Date Prepared:"
        pm_label = "Project Manager:"
        prep_label = "Prepared By:"
        instructions = EN_PARAMS["instructions"]
        placeholder = EN_PARAMS["box_prompt"]
        dir_attr = 'dir="ltr"'
        font_family = "font-family: Arial, sans-serif;"
        prep_sig = "Prepared By:"
        rev_sig = "Reviewed By:"
        app_sig = "Approved By:"
        date_sig = "Date:"
        timestamp_text = "Generated on: {{Current_Timestamp}}"
        timestamp_align = "right"

    html = []
    html.append(f'<div {dir_attr} style="{font_family}">\n')
    html.append(instructions + "\n\n")
    
    html.append('<table width="100%" style="border-collapse: collapse; border: none; margin-bottom: 20px;">')
    html.append('  <tr>')
    html.append(f'    <td align="center" style="background-color: #34495e; color: white; padding: 15px; font-size: 24px; font-weight: bold; border-radius: 5px;">')
    html.append(f'      {form_name.upper()}')
    html.append('    </td>')
    html.append('  </tr>')
    html.append('</table>\n')

    html.append('<table width="100%" border="1" cellspacing="0" cellpadding="10" style="border-collapse: collapse; border-color: #bdc3c7; margin-bottom: 30px;">')
    html.append('  <tr>')
    html.append(f'    <td width="50%"><b>{title_label}</b> {{{{Project_Name}}}}</td>')
    html.append(f'    <td width="50%"><b>{date_label}</b> {{{{Current_Date}}}}</td>')
    html.append('  </tr>')
    html.append('  <tr>')
    html.append(f'    <td><b>{pm_label}</b> {{{{Project_Manager_Name}}}}</td>')
    html.append(f'    <td><b>{prep_label}</b> {{{{Prepared_By}}}}</td>')
    html.append('  </tr>')
    html.append('</table>\n\n')

    if is_table:
        headers = list(fields.keys())
        if headers:
            html.append('<table width="100%" border="1" cellspacing="0" cellpadding="10" style="border-collapse: collapse; border-color: #bdc3c7;">')
            html.append('  <tr style="background-color: #ecf0f1;">')
            for h in headers:
                html.append(f'    <th>{h}</th>')
            html.append('  </tr>')
            
            for _ in range(8):
                html.append('  <tr>')
                for _ in headers:
                    html.append('    <td><br><br></td>')
                html.append('  </tr>')
            html.append('</table>\n\n')
            
            html.append('<br>\n<div style="background-color: #f9f9f9; padding: 15px; border-left: 5px solid #3498db;">')
            html.append('<b>Field Guidance:</b><br>')
            html.append('<ul>')
            for h, guidance in fields.items():
                html.append(f'<li><b>{h}:</b> <i>{guidance}</i></li>')
            html.append('</ul>')
            html.append('</div>\n')
    else:
        for field, guidance in fields.items():
            html.append('<table width="100%" border="1" cellspacing="0" cellpadding="10" style="border-collapse: collapse; border-color: #bdc3c7; margin-bottom: 20px;">')
            html.append('  <tr style="background-color: #ecf0f1;">')
            html.append(f'    <th align="left" style="padding: 10px;">')
            html.append(f'      <span style="font-size: 16px; color: #2c3e50;">{field}</span><br>')
            if guidance:
                html.append(f'      <span style="font-size: 12px; color: #7f8c8d; font-weight: normal;">{guidance}</span>')
            html.append('    </th>')
            html.append('  </tr>')
            html.append('  <tr>')
            html.append(f'    <td valign="top" style="padding: 15px; color: #34495e;">')
            html.append(f'      <br>{placeholder}<br><br><br>')
            html.append('    </td>')
            html.append('  </tr>')
            html.append('</table>\n')

    html.append('<br><br>\n')
    html.append('<table width="100%" style="border-collapse: collapse; border: none; margin-top: 30px;">')
    html.append('  <tr>')
    html.append(f'    <td width="33%"><b>{prep_sig}</b><br><br>_____________________<br><br>{date_sig} _________________</td>')
    html.append(f'    <td width="33%"><b>{rev_sig}</b><br><br>_____________________<br><br>{date_sig} _________________</td>')
    html.append(f'    <td width="33%"><b>{app_sig}</b><br><br>_____________________<br><br>{date_sig} _________________</td>')
    html.append('  </tr>')
    html.append('</table>\n')
    
    html.append(f'<div align="{timestamp_align}" style="margin-top: 40px; font-size: 10px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 5px;">')
    html.append(f'  <i>{timestamp_text}</i>')
    html.append('</div>\n')

    html.append('</div>\n')
    return "".join(html)

def create_files(base_dir, is_arabic):
    for chapter, forms in NEW_ARTIFACTS.items():
        chapter_dir = os.path.join(base_dir, chapter)
        if not os.path.exists(chapter_dir):
            os.makedirs(chapter_dir)
            
        for form_dir_name, data in forms.items():
            form_name_en = form_dir_name.split("_", 1)[1].replace("_", " ")
            form_name = data["ar_name"] if is_arabic else form_name_en
            
            form_dir = os.path.join(chapter_dir, form_dir_name)
            if not os.path.exists(form_dir):
                os.makedirs(form_dir)
                
            fields = data["fields"]
            is_table = data["is_table"]
            
            # Instruction MD
            md_instr_path = os.path.join(form_dir, f"{form_name_en.replace(' ', '_')}.md")
            with open(md_instr_path, 'w', encoding='utf-8') as f:
                f.write(f"---\nForm: {form_name} (Instructions)\n---\n\n")
                f.write(f"# {form_name.upper()} - LLM GENERATION GUIDE\n\n")
                f.write("> **System Prompt / Instructions:**\n")
                f.write(f"> This document serves as the detailed instruction set for generating the `{form_name}`. ")
                f.write("Reference `parameters.md` for global project variables.\n\n---\n\n")
                for field, desc in fields.items():
                    f.write(f"### {field}\n**Instruction:** {desc}\n\n")
            
            # Template MD
            template_path = os.path.join(form_dir, f"{form_name_en.replace(' ', '_')}_Template.md")
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(generate_html_form(form_name, fields, is_table, is_arabic))
                
            # JSON
            json_path = os.path.join(form_dir, f"{form_name_en.replace(' ', '_')}.json")
            with open(json_path, 'w', encoding='utf-8') as f:
                json_template = {
                    "_llm_instructions": AR_PARAMS["instructions"] if is_arabic else EN_PARAMS["instructions"],
                    "form_name": form_name,
                    "fields": {k: {"guidance": v, "value": ""} for k, v in fields.items()}
                }
                json.dump(json_template, f, indent=4, ensure_ascii=False)
                
            # CSV
            csv_path = os.path.join(form_dir, f"{form_name_en.replace(' ', '_')}.csv")
            with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
                writer = csv.writer(cf)
                if is_arabic:
                    writer.writerow(["الحقل (Field)", "الإرشادات (Guidance)", "LLM_Generated_Value"])
                else:
                    writer.writerow(["Field", "Guidance", "LLM_Generated_Value"])
                for field, desc in fields.items():
                    writer.writerow([field, desc, ""])

create_files(base_dir_en, False)
create_files(base_dir_ar, True)

# Update mapping.md to include the new additions
with open(os.path.join(base_dir_en, 'mapping.md'), 'a', encoding='utf-8') as f:
    f.write("\n## Newly Added Advanced PMO Artifacts (Enterprise & Agile)\n\n")
    f.write("These artifacts have been added to support enterprise-grade PMOs, advanced Agile, Organizational Change Management, and AI Governance.\n\n")
    f.write("| Category | Artifact Name | Directory Path |\n")
    f.write("| --- | --- | --- |\n")
    for chapter, forms in NEW_ARTIFACTS.items():
        for form_dir_name in forms.keys():
            form_name = form_dir_name.split("_", 1)[1].replace("_", " ")
            f.write(f"| {chapter} | {form_name} | `{chapter}/{form_dir_name}` |\n")

print("Advanced artifacts generated and mapping updated.")
