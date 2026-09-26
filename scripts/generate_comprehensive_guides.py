import os
import json

base_dir_en = "/home/mohamed/Desktop/PMOSKILL/forms"
base_dir_ar = "/home/mohamed/Desktop/PMOSKILL/forms_ar"

PMI_DEFINITIONS = {
    "Business Case": {
        "what_en": "A documented economic feasibility study used to establish the validity of the benefits of a selected component lacking sufficient definition.",
        "why_en": "It provides a basis for the authorization of further project management activities and justifies the investment based on expected business value.",
        "what_ar": "دراسة جدوى اقتصادية موثقة تُستخدم لإثبات صحة فوائد مكون محدد يفتقر إلى تعريف كافٍ.",
        "why_ar": "توفر أساساً لترخيص المزيد من أنشطة إدارة المشروع وتبرر الاستثمار بناءً على قيمة الأعمال المتوقعة."
    },
    "Benefits Management Plan": {
        "what_en": "The documented explanation defining the processes for creating, maximizing, and sustaining the benefits provided by a project or program.",
        "why_en": "Ensures that the project's outcomes align with the organization's strategic goals and that expected value is tracked and realized.",
        "what_ar": "التفسير الموثق الذي يحدد العمليات لإنشاء وتعظيم واستدامة الفوائد التي يقدمها مشروع أو برنامج.",
        "why_ar": "يضمن توافق نتائج المشروع مع الأهداف الاستراتيجية للمؤسسة وتتبع القيمة المتوقعة وتحقيقها."
    },
    "Project Charter": {
        "what_en": "A document issued by the project sponsor that formally authorizes the existence of a project and provides the project manager with authority to apply resources.",
        "why_en": "It establishes a direct link between the project and the strategic objectives of the organization and creates a formal record of the project.",
        "what_ar": "وثيقة صادرة عن راعي المشروع تصرح رسمياً بوجود مشروع وتمنح مدير المشروع الصلاحية لتطبيق الموارد.",
        "why_ar": "تؤسس رابطاً مباشراً بين المشروع والأهداف الاستراتيجية للمؤسسة وتنشئ سجلاً رسمياً للمشروع."
    },
    "Project Management Plan": {
        "what_en": "The document that describes how the project will be executed, monitored, and controlled.",
        "why_en": "It integrates and consolidates all of the subsidiary management plans and baselines to guide the team through project closure.",
        "what_ar": "الوثيقة التي تصف كيفية تنفيذ المشروع ومراقبته والتحكم فيه.",
        "why_ar": "تقوم بدمج وتوحيد جميع خطط الإدارة الفرعية والخطوط المرجعية لتوجيه الفريق حتى إغلاق المشروع."
    },
    "Assumption Log": {
        "what_en": "A project document used to record all assumptions and constraints throughout the project life cycle.",
        "why_en": "Helps in identifying potential risks if assumptions prove false, and clarifies the boundaries and limitations of the project.",
        "what_ar": "وثيقة مشروع تُستخدم لتسجيل جميع الافتراضات والقيود طوال دورة حياة المشروع.",
        "why_ar": "تساعد في تحديد المخاطر المحتملة إذا ثبت خطأ الافتراضات، وتوضح حدود وقيود المشروع."
    },
    "Stakeholder Register": {
        "what_en": "A project document including the identification, assessment, and classification of project stakeholders.",
        "why_en": "Crucial for understanding who impacts or is impacted by the project, enabling effective communication and engagement strategies.",
        "what_ar": "وثيقة مشروع تتضمن تحديد وتقييم وتصنيف المعنيين بالمشروع.",
        "why_ar": "حاسمة لفهم من يؤثر أو يتأثر بالمشروع، مما يتيح استراتيجيات تواصل ومشاركة فعالة."
    },
    "Requirements Traceability Matrix": {
        "what_en": "A grid that links product requirements from their origin to the deliverables that satisfy them.",
        "why_en": "Ensures each requirement adds business value and helps manage changes to the product scope.",
        "what_ar": "شبكة تربط متطلبات المنتج من مصدرها إلى التسليمات التي تلبيها.",
        "why_ar": "تضمن أن كل متطلب يضيف قيمة للعمل وتساعد في إدارة التغييرات في نطاق المنتج."
    },
    "Work Breakdown Structure": {
        "what_en": "A hierarchical decomposition of the total scope of work to be carried out by the project team to accomplish the project objectives.",
        "why_en": "Provides a structured vision of what has to be delivered, breaking complex work into manageable work packages.",
        "what_ar": "تحليل هرمي لإجمالي نطاق العمل الذي سينفذه فريق المشروع لتحقيق أهداف المشروع.",
        "why_ar": "يوفر رؤية منظمة لما يجب تسليمه، مقسماً العمل المعقد إلى حزم عمل يمكن إدارتها."
    },
    "Risk Register": {
        "what_en": "A repository in which outputs of risk management processes are recorded.",
        "why_en": "Provides a central tracking mechanism for individual project risks, their root causes, and planned responses.",
        "what_ar": "مستودع تُسجل فيه مخرجات عمليات إدارة المخاطر.",
        "why_ar": "يوفر آلية تتبع مركزية للمخاطر الفردية للمشروع، وأسبابها الجذرية، والاستجابات المخطط لها."
    },
    "Issue Log": {
        "what_en": "A project document where information about issues is recorded and monitored.",
        "why_en": "Ensures that problems threatening the project's success are formally tracked, assigned, and resolved in a timely manner.",
        "what_ar": "وثيقة مشروع تُسجل فيها وتُراقب المعلومات المتعلقة بالمشكلات.",
        "why_ar": "تضمن أن المشكلات التي تهدد نجاح المشروع يتم تتبعها رسمياً وتعيينها وحلها في الوقت المناسب."
    },
    "Change Request": {
        "what_en": "A formal proposal to modify any document, deliverable, or baseline.",
        "why_en": "Maintains control over the project baselines and ensures all changes are evaluated for impact on time, cost, and scope before approval.",
        "what_ar": "اقتراح رسمي لتعديل أي وثيقة أو تسليمة أو خط مرجعي.",
        "why_ar": "يحافظ على التحكم في الخطوط المرجعية للمشروع ويضمن تقييم جميع التغييرات لمعرفة تأثيرها على الوقت والتكلفة والنطاق قبل الموافقة."
    },
    "Lessons Learned Register": {
        "what_en": "A project document used to record knowledge gained during a project so that it can be used in the current project and entered into the lessons learned repository.",
        "why_en": "Facilitates continuous improvement by documenting both successes and failures to prevent repeating mistakes.",
        "what_ar": "وثيقة مشروع تُستخدم لتسجيل المعرفة المكتسبة خلال المشروع بحيث يمكن استخدامها في المشروع الحالي وإدخالها في مستودع الدروس المستفادة.",
        "why_ar": "تسهل التحسين المستمر من خلال توثيق كل من النجاحات والإخفاقات لتجنب تكرار الأخطاء."
    },
    "Project Status Report": {
        "what_en": "A document providing a summary of project performance, highlighting status, issues, and accomplishments.",
        "why_en": "Keeps all stakeholders informed about the project's health, ensuring transparency and facilitating corrective actions.",
        "what_ar": "وثيقة تقدم ملخصاً لأداء المشروع، وتسلط الضوء على الحالة والمشكلات والإنجازات.",
        "why_ar": "تُبقي جميع المعنيين على علم بحالة المشروع، مما يضمن الشفافية ويسهل الإجراءات التصحيحية."
    }
}

def get_pmi_definition(form_name, is_arabic):
    # Try exact match
    if form_name in PMI_DEFINITIONS:
        if is_arabic:
            return PMI_DEFINITIONS[form_name]["what_ar"], PMI_DEFINITIONS[form_name]["why_ar"]
        else:
            return PMI_DEFINITIONS[form_name]["what_en"], PMI_DEFINITIONS[form_name]["why_en"]
            
    # Generic PMI Fallback
    if is_arabic:
        what = f"وثيقة رسمية وفق منهجية معهد إدارة المشاريع (PMI) تُعرف باسم **{form_name}**، وتُستخدم لتخطيط وتوثيق وإدارة العناصر الحيوية المتعلقة بهذا المكون."
        why = f"لضمان التوافق مع معايير PMBOK، ولتوفير الشفافية، ومراقبة الأداء، وإدارة المتغيرات بفعالية طوال دورة حياة المشروع."
    else:
        what = f"A formal PMI-aligned project document known as the **{form_name}**, utilized to plan, document, and manage the critical elements related to this specific knowledge area."
        why = f"To ensure strict alignment with PMBOK standards, establish transparency, monitor project performance, and control variances effectively throughout the project life cycle."
        
    # Check partial match for smarter generic
    lower_form = form_name.lower()
    if "plan" in lower_form:
        if is_arabic:
            what = f"خطة إدارة فرعية منبثقة من معايير PMI تُعرف باسم **{form_name}**، والتي تصف كيف سيتم تخطيط هذا الجانب من المشروع وهيكلته والتحكم فيه."
            why = f"لتوفير مسار واضح وعمليات قياسية لفريق المشروع، مما يمنع انحراف النطاق أو الوقت أو التكلفة."
        else:
            what = f"A subsidiary management plan aligned with PMI standards known as the **{form_name}**, which describes how this specific aspect of the project will be planned, structured, and controlled."
            why = f"To provide a clear roadmap and standardized processes for the project team, preventing unauthorized deviations in scope, time, or cost."
    elif "log" in lower_form or "register" in lower_form:
        if is_arabic:
            what = f"سجل حي وديناميكي (**{form_name}**) يُستخدم لالتقاط وتتبع ومراقبة العناصر اليومية التي تطرأ خلال المشروع."
            why = f"للحفاظ على رؤية مركزية وحل سريع لأي بنود أو مخاطر معلقة يمكن أن تؤثر على تسليم المشروع."
        else:
            what = f"A dynamic, living repository (**{form_name}**) used to capture, track, and monitor items that arise during project execution."
            why = f"To maintain centralized visibility and prompt resolution of any outstanding items, risks, or requests that could impact project delivery."

    return what, why

def get_phase_info(dir_name):
    parts = dir_name.split("_", 1)
    if len(parts) > 1:
        return parts[1].replace("_", " ")
    return dir_name

def get_who_en(phase, form_name):
    phase = phase.lower()
    if "initiating" in phase or "portfolio" in phase or "business" in phase:
        return "Initiated by the Project Sponsor, drafted by the Project Manager, and validated by key stakeholders."
    elif "planning" in phase or "approach" in phase:
        return "Developed by the Project Manager with input from the project team and Subject Matter Experts (SMEs), then baselined."
    elif "executing" in phase:
        return "Managed actively by the Project Manager and the core executing team, updated as work is performed."
    elif "monitoring" in phase:
        return "Maintained by the Project Manager or PMO to track actuals against the baselined plans and report to the steering committee."
    elif "closing" in phase:
        return "Finalized by the Project Manager for formal sign-off by the Sponsor or Customer, and archived for historical records."
    else:
        return "Managed by the Project Manager and authorized by project governance."

def get_who_ar(phase, form_name):
    phase = phase.lower()
    if "initiating" in phase or "portfolio" in phase or "business" in phase:
        return "يتم البدء به من قبل راعي المشروع، وتتم صياغته من قبل مدير المشروع، ويصادق عليه المعنيون الأساسيون."
    elif "planning" in phase or "approach" in phase:
        return "يُطور بواسطة مدير المشروع مع مدخلات من فريق المشروع والخبراء المختصين، ثم يُعتمد كخط مرجعي."
    elif "executing" in phase:
        return "يُدار بنشاط من قبل مدير المشروع وفريق التنفيذ الأساسي، ويتم تحديثه كلما تم إنجاز العمل."
    elif "monitoring" in phase:
        return "يُصان بواسطة مدير المشروع أو مكتب إدارة المشاريع لتتبع الأداء الفعلي مقابل الخطط المرجعية وإعداد تقارير للجنة التوجيهية."
    elif "closing" in phase:
        return "يُنجز نهائياً من قبل مدير المشروع ليتم التوقيع عليه رسمياً من قبل الراعي أو العميل، ويُحفظ كسجل تاريخي."
    else:
        return "يُدار بواسطة مدير المشروع ويُصرح به من قبل إدارة حوكمة المشروع."

def get_phase_ar(phase):
    mapping = {
        "program and portfolio management": "إدارة البرامج والمحافظ (قبل المشروع)",
        "business and value delivery": "تسليم القيمة والأعمال (ما قبل البدء)",
        "project approach and tailoring": "منهجية وتخصيص المشروع",
        "initiating": "مرحلة البدء (Initiating Process Group)",
        "planning": "مرحلة التخطيط (Planning Process Group)",
        "executing": "مرحلة التنفيذ (Executing Process Group)",
        "monitoring and controlling": "مرحلة المراقبة والتحكم (Monitoring & Controlling Process Group)",
        "closing": "مرحلة الإغلاق (Closing Process Group)"
    }
    for k, v in mapping.items():
        if k in phase.lower():
            return v
    return phase

def generate_guide(is_arabic, form_name, phase_name, fields, output_path):
    what, why = get_pmi_definition(form_name, is_arabic)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        if is_arabic:
            ar_phase = get_phase_ar(phase_name)
            ar_who = get_who_ar(phase_name, form_name)
            
            f.write(f'<div dir="rtl" style="font-family: Arial, sans-serif; line-height: 1.6;">\n\n')
            f.write(f"## الدليل الشامل لمعايير إدارة المشاريع\n")
            f.write(f"# المخرج (Artifact): {form_name}\n\n")
            f.write(f"يوفر هذا المستند مرجعاً تفصيلياً واحترافياً لفهم الغرض من **{form_name}** واستخدامه بفعالية كجزء من منهجية معهد إدارة المشاريع (PMI).\n\n")
            f.write("---\n\n")
            
            f.write(f"### 1. ما هو (What)؟\n")
            f.write(f"{what}\n\n")
            
            f.write(f"### 2. لماذا (Why)؟\n")
            f.write(f"{why}\n\n")
            
            f.write(f"### 3. متى (When)؟\n")
            f.write(f"يتم إعداد هذا المخرج (Artifact) وتحديثه بشكل أساسي خلال **{ar_phase}** من دورة حياة المشروع.\n\n")
            
            f.write(f"### 4. مَن (Who)؟\n")
            f.write(f"**المسؤوليات:** {ar_who}\n\n")
            
            f.write(f"### 5. كيف (How)؟\n")
            f.write(f"لإكمال **{form_name}** بطريقة احترافية ومتوافقة مع المعايير، يجب تعبئة الأقسام الحرجة التالية بشكل مفصل (يرجى الرجوع إلى ملف `parameters.md` لضمان توافق المتغيرات العامة للمشروع):\n\n")
            
            for field, guidance in fields.items():
                desc = guidance.get('guidance', '') if isinstance(guidance, dict) else guidance
                if desc:
                    f.write(f"*   **{field}:** {desc}\n")
                else:
                    f.write(f"*   **{field}**\n")
            
            f.write(f"\n</div>\n")
            
        else:
            en_who = get_who_en(phase_name, form_name)
            
            f.write(f'<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">\n\n')
            f.write(f"## PMBOK Standard Guide\n")
            f.write(f"# Project Artifact: {form_name}\n\n")
            f.write(f"This document provides a comprehensive, professional reference to understand the purpose and effective usage of the **{form_name}** in alignment with Project Management Institute (PMI) standards.\n\n")
            f.write("---\n\n")
            
            f.write(f"### 1. What?\n")
            f.write(f"{what}\n\n")
            
            f.write(f"### 2. Why?\n")
            f.write(f"{why}\n\n")
            
            f.write(f"### 3. When?\n")
            f.write(f"This artifact is primarily prepared, utilized, and updated during the **{phase_name.upper()} Process Group** of the project lifecycle.\n\n")
            
            f.write(f"### 4. Who?\n")
            f.write(f"**Responsibilities:** {en_who}\n\n")
            
            f.write(f"### 5. How?\n")
            f.write(f"To accurately and professionally complete the **{form_name}**, the responsible party must populate the following critical sections based on the project context (ensure `parameters.md` is referenced for global project variables):\n\n")
            
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
            
            en_filename = jf.replace(".json", "")
            guide_path = os.path.join(root, f"{en_filename}_Guide.md")
            generate_guide(is_arabic, form_name, phase_name, fields, guide_path)

process_directory(base_dir_en, False)
process_directory(base_dir_ar, True)

print("Comprehensive PMI Guides generated successfully.")
