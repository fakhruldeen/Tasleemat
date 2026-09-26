import os
import json

base_dirs = ["/home/mohamed/Desktop/PMOSKILL/forms", "/home/mohamed/Desktop/PMOSKILL/forms_ar"]

table_keywords = ["log", "register", "matrix", "list", "worksheet", "assessment", "metrics", "schedule", "estimates"]
exceptions = ["project schedule", "schedule management plan", "cost management plan", "quality management plan", "risk management plan", "procurement management plan", "stakeholder engagement plan", "communications management plan", "requirements management plan", "scope management plan", "change management plan", "project management plan", "team performance assessment", "probability and impact assessment", "risk data sheet", "procurement strategy", "source selection criteria", "requirements documentation"]

def generate_html_form(form_name, fields, is_table, is_arabic):
    if is_arabic:
        title_label = "اسم المشروع:"
        date_label = "التاريخ:"
        pm_label = "مدير المشروع:"
        prep_label = "إعداد:"
        instructions = "<!-- تعليمات للنموذج الذكي (LLM): قم بملء المساحات الفارغة [ ... ] بناءً على سياق المشروع -->"
        placeholder = "[ أدخل استجابتك المفصلة هنا... ]"
        dir_attr = 'dir="rtl"'
        font_family = "font-family: Arial, sans-serif;"
    else:
        title_label = "Project Title:"
        date_label = "Date Prepared:"
        pm_label = "Project Manager:"
        prep_label = "Prepared By:"
        instructions = "<!-- LLM INSTRUCTIONS: Fill in the [ ... ] placeholders based on project context. -->"
        placeholder = "[ Provide your detailed response here... ]"
        dir_attr = 'dir="ltr"'
        font_family = "font-family: Arial, sans-serif;"

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
            for h, info in fields.items():
                guidance = info.get('guidance', '')
                html.append(f'<li><b>{h}:</b> <i>{guidance}</i></li>')
            html.append('</ul>')
            html.append('</div>\n')

    else:
        for field, info in fields.items():
            guidance = info.get('guidance', '')
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

    html.append('</div>\n')
    return "\n".join(html)

for b_dir in base_dirs:
    is_arabic = "forms_ar" in b_dir
    
    for root, dirs, files in os.walk(b_dir):
        json_files = [f for f in files if f.endswith(".json")]
        for jf in json_files:
            json_path = os.path.join(root, jf)
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception:
                continue
                
            form_name = data.get("form_name", "")
            if not form_name: continue
            
            fields = data.get("fields", {})
            
            lower_name = jf.lower()
            is_table = False
            if any(kw in lower_name for kw in table_keywords) and not any(exc in lower_name for exc in exceptions):
                is_table = True
            if "roadmap" in lower_name or "retrospective" in lower_name or "register" in lower_name:
                is_table = True
                
            template_path = os.path.join(root, jf.replace(".json", "_Template.md"))
            html_content = generate_html_form(form_name, fields, is_table, is_arabic)
            
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(html_content)

print("Fixed Charter issue.")
