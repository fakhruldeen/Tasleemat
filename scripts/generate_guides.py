import os
import json

base_dir_en = "/home/mohamed/Desktop/PMOSKILL/forms"
base_dir_ar = "/home/mohamed/Desktop/PMOSKILL/forms_ar"

def get_phase_info(dir_name):
    # Extracts the phase name from the directory, e.g. "04_Planning" -> "Planning"
    parts = dir_name.split("_", 1)
    if len(parts) > 1:
        return parts[1].replace("_", " ")
    return dir_name

def get_who_en(phase):
    phase = phase.lower()
    if "initiating" in phase or "portfolio" in phase or "business" in phase:
        return "Prepared primarily by the Project Sponsor or Project Manager, with input from key executives, and reviewed by foundational stakeholders."
    elif "planning" in phase or "approach" in phase:
        return "Prepared by the Project Manager in collaboration with the core project team and Subject Matter Experts (SMEs). Formally approved by the Project Sponsor."
    elif "executing" in phase:
        return "Actively managed and updated by the Project Manager, Scrum Master, or designated team members responsible for day-to-day delivery."
    elif "monitoring" in phase:
        return "Maintained rigorously by the Project Manager, PMO, or Quality Assurance leads to track deviations and report to the steering committee."
    elif "closing" in phase:
        return "Finalized by the Project Manager and formally signed off by the Project Sponsor, Client, or Business Owner."
    else:
        return "Managed by the Project Manager and relevant project stakeholders."

def get_who_ar(phase):
    phase = phase.lower()
    if "initiating" in phase or "portfolio" in phase or "business" in phase:
        return "يتم الإعداد بشكل أساسي من قبل راعي المشروع أو مدير المشروع، مع مدخلات من المديرين التنفيذيين، ويتم مراجعته من قبل المعنيين الأساسيين."
    elif "planning" in phase or "approach" in phase:
        return "يتم الإعداد من قبل مدير المشروع بالتعاون مع فريق المشروع الأساسي والخبراء المختصين. يتم الاعتماد رسمياً من قبل راعي المشروع."
    elif "executing" in phase:
        return "يتم إدارته وتحديثه بنشاط من قبل مدير المشروع أو قائد الفريق (Scrum Master) أو أعضاء الفريق المسؤولين عن التسليم اليومي."
    elif "monitoring" in phase:
        return "يتم صيانته بدقة من قبل مدير المشروع أو مكتب إدارة المشاريع (PMO) أو قادة ضمان الجودة لتتبع الانحرافات ورفع التقارير للجنة التوجيهية."
    elif "closing" in phase:
        return "يتم إنجازه بشكل نهائي من قبل مدير المشروع ويتم توقيعه رسمياً من قبل راعي المشروع أو العميل أو مالك العمل."
    else:
        return "يتم إدارته بواسطة مدير المشروع والمعنيين ذوي الصلة."

def get_phase_ar(phase):
    mapping = {
        "program and portfolio management": "إدارة البرامج والمحافظ",
        "business and value delivery": "الأعمال وتسليم القيمة",
        "project approach and tailoring": "منهجية المشروع وتخصيصه",
        "initiating": "البدء (Initiating)",
        "planning": "التخطيط (Planning)",
        "executing": "التنفيذ (Executing)",
        "monitoring and controlling": "المراقبة والتحكم (Monitoring & Controlling)",
        "closing": "الإغلاق (Closing)"
    }
    for k, v in mapping.items():
        if k in phase.lower():
            return v
    return phase

def generate_guide(is_arabic, form_name, phase_name, fields, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        if is_arabic:
            ar_phase = get_phase_ar(phase_name)
            ar_who = get_who_ar(phase_name)
            
            f.write(f'<div dir="rtl" style="font-family: Arial, sans-serif;">\n\n')
            f.write(f"# دليل النموذج: {form_name}\n\n")
            f.write(f"يوفر هذا المستند مرجعاً تفصيلياً (ماذا، ولماذا، ومتى، ومن، وكيف) لفهم الغرض من **{form_name}** واستخدامه بفعالية داخل المشروع.\n\n")
            f.write("---\n\n")
            
            f.write(f"### 1. ماذا؟ (What)\n")
            f.write(f"**{form_name}** هي وثيقة استراتيجية متخصصة تُستخدم لتوثيق وتتبع التفاصيل الرئيسية المرتبطة بهذا الجانب من المشروع. تحتوي على حقول بيانات مهيكلة تضمن عدم إغفال أي معلومات حيوية أثناء التوثيق.\n\n")
            
            f.write(f"### 2. لماذا؟ (Why)\n")
            f.write(f"هذا النموذج ضروري لفرض حوكمة واضحة للمشروع، والحفاظ على التوافق والتواصل الفعال بين المعنيين، وتوفير مرجع تاريخي وقانوني للقرارات والتخطيط الخاص بـ {form_name}.\n\n")
            
            f.write(f"### 3. متى؟ (When)\n")
            f.write(f"يتم إعداد هذا النموذج وتحديثه بشكل أساسي خلال مرحلة **{ar_phase}** من دورة حياة المشروع.\n\n")
            
            f.write(f"### 4. مَن؟ (Who)\n")
            f.write(f"**المسؤوليات:** {ar_who}\n\n")
            
            f.write(f"### 5. كيف؟ (How)\n")
            f.write(f"لإكمال هذا النموذج بشكل صحيح، يجب على الشخص المسؤول تعبئة الأقسام الحرجة التالية بناءً على سياق المشروع (تأكد من استخدام `parameters.md` كمرجع أساسي للمتغيرات العابرة للمشروع):\n\n")
            
            for field, guidance in fields.items():
                desc = guidance.get('guidance', '') if isinstance(guidance, dict) else guidance
                if desc:
                    f.write(f"*   **{field}:** {desc}\n")
                else:
                    f.write(f"*   **{field}**\n")
            
            f.write(f"\n</div>\n")
            
        else:
            en_who = get_who_en(phase_name)
            
            f.write(f'<div dir="ltr" style="font-family: Arial, sans-serif;">\n\n')
            f.write(f"# Artifact Guide: {form_name}\n\n")
            f.write(f"This document provides a comprehensive 5Ws reference (What, Why, When, Who, How) to understand the purpose and effective usage of the **{form_name}** within the project.\n\n")
            f.write("---\n\n")
            
            f.write(f"### 1. What?\n")
            f.write(f"The **{form_name}** is a specialized strategic document used to document and track key details related to this aspect of the project. It contains structured data fields ensuring no vital information is overlooked during documentation.\n\n")
            
            f.write(f"### 2. Why?\n")
            f.write(f"This template is critical to enforce clear project governance, maintain alignment and effective communication among stakeholders, and provide a historical and auditable reference for planning and decisions regarding the {form_name}.\n\n")
            
            f.write(f"### 3. When?\n")
            f.write(f"This artifact is primarily prepared, utilized, and updated during the **{phase_name}** phase of the project lifecycle.\n\n")
            
            f.write(f"### 4. Who?\n")
            f.write(f"**Responsibilities:** {en_who}\n\n")
            
            f.write(f"### 5. How?\n")
            f.write(f"To accurately complete this template, the responsible party must populate the following critical sections based on the project context (ensure `parameters.md` is referenced for global project variables):\n\n")
            
            for field, guidance in fields.items():
                desc = guidance.get('guidance', '') if isinstance(guidance, dict) else guidance
                if desc:
                    f.write(f"*   **{field}:** {desc}\n")
                else:
                    f.write(f"*   **{field}**\n")
            
            f.write(f"\n</div>\n")

def process_directory(base_dir, is_arabic):
    for root, dirs, files in os.walk(base_dir):
        json_files = [f for f in files if f.endswith(".json")]
        if not json_files:
            continue
            
        # Determine the phase from the top-level directory
        rel_path = os.path.relpath(root, base_dir)
        top_level_dir = rel_path.split(os.sep)[0]
        phase_name = get_phase_info(top_level_dir)
        
        for jf in json_files:
            json_path = os.path.join(root, jf)
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception:
                continue
                
            form_name = data.get("form_name", "")
            if not form_name:
                continue
                
            fields = data.get("fields", {})
            
            # Write Guide
            en_filename = jf.replace(".json", "")
            guide_path = os.path.join(root, f"{en_filename}_Guide.md")
            generate_guide(is_arabic, form_name, phase_name, fields, guide_path)

process_directory(base_dir_en, False)
process_directory(base_dir_ar, True)

print("Guides generated successfully for all forms.")
