import os
import json
import csv

# --- Configuration & Placeholders ---
# We will use {{Placeholder}} format as requested.
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

# English to Arabic Dictionary for PMI Terms (GCC Standard)
PMI_DICT = {
    "Project Charter": "ميثاق المشروع",
    "Assumption Log": "سجل الافتراضات",
    "Stakeholder Register": "سجل المعنيين",
    "Stakeholder Analysis": "تحليل المعنيين",
    "Project Management Plan": "خطة إدارة المشروع",
    "Change Management Plan": "خطة إدارة التغيير",
    "Project Roadmap": "خارطة طريق المشروع",
    "Scope Management Plan": "خطة إدارة النطاق",
    "Requirements Management Plan": "خطة إدارة المتطلبات",
    "Requirements Documentation": "وثائق المتطلبات",
    "Requirements Traceability Matrix": "مصفوفة تتبع المتطلبات",
    "Project Scope Statement": "بيان نطاق المشروع",
    "Work Breakdown Structure": "هيكل تجزئة العمل (WBS)",
    "WBS Dictionary": "قاموس هيكل تجزئة العمل",
    "Schedule Management Plan": "خطة إدارة الجدول الزمني",
    "Activity List": "قائمة الأنشطة",
    "Activity Attributes": "خصائص الأنشطة",
    "Milestone List": "قائمة المعالم (Milestones)",
    "Network Diagram": "المخطط الشبكي",
    "Duration Estimates": "تقديرات المدة",
    "Duration Estimating Worksheet": "ورقة عمل تقدير المدة",
    "Project Schedule": "الجدول الزمني للمشروع",
    "Cost Management Plan": "خطة إدارة التكلفة",
    "Cost Estimates": "تقديرات التكلفة",
    "Cost Estimating Worksheet": "ورقة عمل تقدير التكلفة",
    "Cost Baseline": "الخط المرجعي للتكلفة",
    "Quality Management Plan": "خطة إدارة الجودة",
    "Quality Metrics": "مقاييس الجودة",
    "Responsibility Assignment Matrix": "مصفوفة تعيين المسؤوليات (RAM)",
    "Resource Management Plan": "خطة إدارة الموارد",
    "Team Charter": "ميثاق الفريق",
    "Resource Requirements": "متطلبات الموارد",
    "Resource Breakdown Structure": "هيكل تجزئة الموارد (RBS)",
    "Communications Management Plan": "خطة إدارة الاتصالات",
    "Risk Management Plan": "خطة إدارة المخاطر",
    "Risk Register": "سجل المخاطر",
    "Risk Report": "تقرير المخاطر",
    "Probability and Impact Assessment": "تقييم الاحتمالية والأثر",
    "Probability and Impact Matrix": "مصفوفة الاحتمالية والأثر",
    "Risk Data Sheet": "صحيفة بيانات المخاطر",
    "Procurement Management Plan": "خطة إدارة المشتريات",
    "Procurement Strategy": "استراتيجية المشتريات",
    "Source Selection Criteria": "معايير اختيار المصدر",
    "Stakeholder Engagement Plan": "خطة إشراك المعنيين",
    "Issue Log": "سجل المشكلات",
    "Decision Log": "سجل القرارات",
    "Change Request": "طلب تغيير",
    "Change Log": "سجل التغييرات",
    "Lessons Learned Register": "سجل الدروس المستفادة",
    "Quality Audit": "تدقيق الجودة",
    "Team Performance Assessment": "تقييم أداء الفريق",
    "Team Member Status Report": "تقرير حالة عضو الفريق",
    "Project Status Report": "تقرير حالة المشروع",
    "Variance Analysis": "تحليل التباين",
    "Earned Value Analysis": "تحليل القيمة المكتسبة (EVA)",
    "Risk Audit": "تدقيق المخاطر",
    "Contractor Status Report": "تقرير حالة المقاول",
    "Procurement Audit": "تدقيق المشتريات",
    "Contract Closeout Report": "تقرير إغلاق العقد",
    "Product Acceptance Form": "نموذج قبول المنتج",
    "Lessons Learned Summary": "ملخص الدروس المستفادة",
    "Project or Phase Closeout": "إغلاق المشروع أو المرحلة",
    "Product Vision": "رؤية المنتج",
    "Product Backlog": "سجل متأخرات المنتج (Product Backlog)",
    "Release Plan": "خطة الإصدار",
    "Retrospective": "مراجعة المرحلة (Retrospective)",
    
    # New additions
    "Business Case": "دراسة الجدوى (Business Case)",
    "Benefits Management Plan": "خطة إدارة الفوائد",
    "Value Realization Register": "سجل تحقيق القيمة",
    "Tailoring Plan": "خطة التخصيص (Tailoring)",
    "AI Governance Plan": "خطة حوكمة الذكاء الاصطناعي",
    "AI Readiness Assessment": "تقييم جاهزية الذكاء الاصطناعي",
    "AI Use Case Canvas": "نموذج حالة استخدام الذكاء الاصطناعي",
    "Prompt Library Log": "سجل مكتبة الأوامر (Prompts)"
}

def translate(text):
    for en, ar in PMI_DICT.items():
        if text.lower() == en.lower():
            return ar
    return text

# Expansion for multi-page forms to ensure COMPLETENESS
EXPANDED_FORMS = {
    "Risk Report": {
        "Executive Summary": "A statement describing the overall project risk exposure and major individual risks.",
        "Overall Project Risk - Status and Trends": "Provide a description of the overall risk of the project.",
        "Overall Project Risk - Significant Drivers": "Identify the significant drivers of overall risk.",
        "Overall Project Risk - Recommended Responses": "Recommendations for overall risk.",
        "Individual Project Risks - Metrics": "Number of scope, schedule, cost, and quality risks. High/Medium/Low distribution.",
        "Individual Project Risks - Top Risks": "The most critical risks and their planned responses.",
        "Individual Project Risks - Changes": "Changes to critical risks since the last report.",
        "Quantitative Analysis Summary - Probabilities": "Probability of meeting scope, schedule, cost, quality objectives.",
        "Quantitative Analysis Summary - Range of Outcomes": "Range of schedule and cost outcomes.",
        "Quantitative Analysis Summary - Key Drivers & Responses": "Drivers of variance and proposed responses.",
        "Reserve Status": "Total Cost/Schedule Reserve, Used to Date, Used This Period, Remaining Reserve.",
        "Risk Audit Summary": "Summary of Risk Events, Risk Management Processes, and Recommendations."
    },
    "Project Status Report": {
        "Accomplishments for This Reporting Period": "List all work packages or other accomplishments completed.",
        "Accomplishments Planned but Not Completed": "Work that was scheduled but delayed.",
        "Root Cause of Variances": "Identify the root cause of schedule or work variances.",
        "Impact to Upcoming Milestones or Due Date": "Identify any impact to critical path or future milestones.",
        "Planned Corrective or Preventive Action": "Actions to recover schedule or prevent delays.",
        "Funds Spent This Reporting Period": "Actual costs incurred.",
        "Funds Planned to Be Spent": "Budgeted costs for the period.",
        "Root Cause of Cost Variances": "Identify causes for any budget overruns or underruns.",
        "Impact to Overall Budget or Contingency": "How the cost variance affects the total budget.",
        "Quality Variances Identified": "Identify any product performance or quality issues.",
        "Accomplishments Planned for Next Period": "Work scheduled for the upcoming period.",
        "Costs Planned for Next Period": "Expected expenditures for the upcoming period.",
        "New Risks Identified": "New risks that should be added to the risk register.",
        "Issues": "New issues that should be added to the issue log.",
        "Comments": "Any additional context."
    },
    "Change Request": {
        "Requestor & Date": "Name of the person requesting the change and the date.",
        "Category of Change": "Scope, Quality, Requirements, Cost, Schedule, or Documents.",
        "Detailed Description of Proposed Change": "Clear explanation of what needs to be changed.",
        "Justification for Proposed Change": "Reasoning and business value for the change.",
        "Impacts of Change - Scope": "How the change affects project scope.",
        "Impacts of Change - Quality": "How the change affects quality standards.",
        "Impacts of Change - Schedule": "How the change affects the timeline.",
        "Impacts of Change - Cost": "How the change affects the budget.",
        "Impacts of Change - Stakeholder/Documents": "Impact on stakeholders and which documents need updates.",
        "Comments": "Additional clarifying information.",
        "Disposition": "Approve, Defer, Reject, and Justification (Filled by CCB)."
    }
}

base_dir_en = "/home/mohamed/Desktop/PMOSKILL/forms"
base_dir_ar = "/home/mohamed/Desktop/PMOSKILL/forms_ar"

def create_dirs(base):
    if not os.path.exists(base): os.makedirs(base)

create_dirs(base_dir_en)
create_dirs(base_dir_ar)

table_keywords = ["log", "register", "matrix", "list", "worksheet", "assessment", "metrics", "schedule", "estimates", "charter"]
exceptions = ["project schedule", "schedule management plan", "cost management plan", "quality management plan", "risk management plan", "procurement management plan", "stakeholder engagement plan", "communications management plan", "requirements management plan", "scope management plan", "change management plan", "project management plan", "team performance assessment", "probability and impact assessment", "risk data sheet", "procurement strategy", "source selection criteria", "requirements documentation", "project charter", "team charter"]

# Iterate over existing English structure
for root, dirs, files in os.walk(base_dir_en):
    json_files = [f for f in files if f.endswith(".json")]
    for jf in json_files:
        json_path = os.path.join(root, jf)
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            continue
            
        form_name_en = data.get("form_name", "")
        if not form_name_en: continue
        
        # Override fields if it's one of the expanded multi-page forms
        if form_name_en in EXPANDED_FORMS:
            fields_en = {k: {"guidance": v, "value": ""} for k,v in EXPANDED_FORMS[form_name_en].items()}
        else:
            fields_en = data.get("fields", {})
            
        form_name_ar = translate(form_name_en)
        
        lower_name = form_name_en.lower()
        is_table = False
        if any(kw in lower_name for kw in table_keywords) and lower_name not in exceptions:
            is_table = True
        if "roadmap" in lower_name or "retrospective" in lower_name or "register" in lower_name:
            is_table = True
            
        # Recreate English Template
        md_temp_en = os.path.join(root, jf.replace(".json", "_Template.md"))
        with open(md_temp_en, 'w', encoding='utf-8') as f:
            f.write(f"<div align=\"center\">\n  <h1>{form_name_en.upper()}</h1>\n</div>\n\n")
            f.write(EN_PARAMS["instructions"] + "\n\n")
            f.write(EN_PARAMS["title"] + "\n\n")
            f.write(EN_PARAMS["header2"] + "\n\n---\n\n")
            
            if is_table:
                headers = list(fields_en.keys())
                if headers:
                    f.write("| " + " | ".join(headers) + " |\n")
                    f.write("|" + "|".join(["---" for _ in headers]) + "|\n")
                    for _ in range(8):
                        f.write("| " + " | ".join(["" for _ in headers]) + " |\n")
                    f.write("\n")
            else:
                for field in fields_en.keys():
                    f.write(f"### {field}\n")
                    f.write(f"> *{fields_en[field].get('guidance', 'Provide information here.')}*\n\n")
                    f.write(f"```text\n{EN_PARAMS['box_prompt']}\n```\n\n")
        
        # --- ARABIC VERSION ---
        rel_path = os.path.relpath(root, base_dir_en)
        ar_root = os.path.join(base_dir_ar, rel_path)
        create_dirs(ar_root)
        
        md_temp_ar = os.path.join(ar_root, jf.replace(".json", "_Template.md"))
        with open(md_temp_ar, 'w', encoding='utf-8') as f:
            f.write(f"<div dir=\"rtl\">\n")
            f.write(f"<div align=\"center\">\n  <h1>{form_name_ar}</h1>\n</div>\n\n")
            f.write(AR_PARAMS["instructions"] + "\n\n")
            f.write(AR_PARAMS["title"] + "\n\n")
            f.write(AR_PARAMS["header2"] + "\n\n---\n\n")
            
            if is_table:
                # We won't translate every single field header automatically, but we will output the structure
                # For a true production system, we'd translate the keys. We will leave keys in EN for JSON compatibility but provide AR headers if possible.
                headers = list(fields_en.keys())
                if headers:
                    f.write("| " + " | ".join(headers) + " |\n")
                    f.write("|" + "|".join(["---" for _ in headers]) + "|\n")
                    for _ in range(8):
                        f.write("| " + " | ".join(["" for _ in headers]) + " |\n")
                    f.write("\n")
            else:
                for field in fields_en.keys():
                    f.write(f"### {field}\n")
                    f.write(f"> *يرجى إدخال التفاصيل الخاصة بـ {field} بناءً على سياق المشروع.*\n\n")
                    f.write(f"```text\n{AR_PARAMS['box_prompt']}\n```\n\n")
            f.write(f"</div>\n")
            
        # JSON and CSV for Arabic (just copy structure)
        json_path_ar = os.path.join(ar_root, jf)
        with open(json_path_ar, 'w', encoding='utf-8') as jf_ar:
            ar_data = {
                "_llm_instructions": AR_PARAMS["instructions"],
                "form_name": form_name_ar,
                "fields": fields_en
            }
            json.dump(ar_data, jf_ar, indent=4, ensure_ascii=False)
            
        csv_path_ar = os.path.join(ar_root, jf.replace(".json", ".csv"))
        with open(csv_path_ar, 'w', newline='', encoding='utf-8') as cf_ar:
            writer = csv.writer(cf_ar)
            writer.writerow(["الحقل (Field)", "الإرشادات (Guidance)", "LLM_Generated_Value"])
            for field, info in fields_en.items():
                writer.writerow([field, info.get('guidance',''), ""])

print("Completed updating multi-page forms, visual templates, and generating Arabic GCC versions.")
