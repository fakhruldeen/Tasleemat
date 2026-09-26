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
    "06_Monitoring_and_Controlling": {
        "10_User_Acceptance_Testing_Signoff": {
            "ar_name": "نموذج اعتماد اختبار قبول المستخدم (UAT)",
            "is_table": False,
            "fields": {
                "Test Summary": "Overview of what was tested.",
                "Testing Environment": "Where the testing took place.",
                "Pass/Fail Criteria": "What determined the success.",
                "Known Defects": "Any non-critical bugs accepted.",
                "Business Owner Sign-off": "Formal acceptance statement."
            }
        }
    },
    "05_Executing": {
        "11_Meeting_Minutes": {
            "ar_name": "محضر الاجتماع",
            "is_table": False,
            "fields": {
                "Meeting Objective": "Purpose of the meeting.",
                "Attendees": "Who was present.",
                "Key Discussion Points": "Main topics discussed.",
                "Decisions Made": "What was agreed upon.",
                "Action Items": "Tasks, owners, and due dates."
            }
        },
        "12_Team_Onboarding_Checklist": {
            "ar_name": "قائمة التحقق لتهيئة فريق العمل",
            "is_table": True,
            "fields": {
                "Task": "Onboarding activity (e.g. System access granted).",
                "Assigned To": "Who is responsible.",
                "Due Date": "When it should be completed.",
                "Status": "Done/Pending."
            }
        }
    },
    "04_Planning/08_Risk": {
        "07_Risk_Mitigation_Action_Plan": {
            "ar_name": "خطة عمل التخفيف من المخاطر",
            "is_table": False,
            "fields": {
                "Risk ID and Title": "Reference to the Risk Register.",
                "Current Risk Score": "Probability x Impact.",
                "Mitigation Strategy": "Avoid, Transfer, Mitigate, Accept.",
                "Detailed Action Steps": "Step by step plan to reduce the risk.",
                "Resource Requirements": "Budget or people needed to execute the plan.",
                "Target Risk Score": "Expected score after mitigation."
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
            
            md_instr_path = os.path.join(form_dir, f"{form_name_en.replace(' ', '_')}.md")
            with open(md_instr_path, 'w', encoding='utf-8') as f:
                f.write(f"---\nForm: {form_name} (Instructions)\n---\n\n")
                f.write(f"# {form_name.upper()} - LLM GENERATION GUIDE\n\n")
                f.write("> **System Prompt / Instructions:**\n")
                f.write(f"> This document serves as the detailed instruction set for generating the `{form_name}`. ")
                f.write("Reference `parameters.md` for global project variables.\n\n---\n\n")
                for field, desc in fields.items():
                    f.write(f"### {field}\n**Instruction:** {desc}\n\n")
            
            template_path = os.path.join(form_dir, f"{form_name_en.replace(' ', '_')}_Template.md")
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(generate_html_form(form_name, fields, is_table, is_arabic))
                
            json_path = os.path.join(form_dir, f"{form_name_en.replace(' ', '_')}.json")
            with open(json_path, 'w', encoding='utf-8') as f:
                json_template = {
                    "_llm_instructions": AR_PARAMS["instructions"] if is_arabic else EN_PARAMS["instructions"],
                    "form_name": form_name,
                    "fields": {k: {"guidance": v, "value": ""} for k, v in fields.items()}
                }
                json.dump(json_template, f, indent=4, ensure_ascii=False)
                
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

print("Created 4 new operational deliverables.")
