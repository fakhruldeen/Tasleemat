#!/usr/bin/env python3
"""Generate DOCUMENT_DEPENDENCIES.md, DOCUMENT_DEPENDENCIES_AR.md,
RACI_AUTHORITY_MATRIX.md, and RACI_AUTHORITY_MATRIX_AR.md for Tasleemat.
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Master definitions for all 102 forms
FORMS_METADATA = [
    # 00 Program and Portfolio Management
    {
        "ref": "PMO-00.01",
        "name_en": "Portfolio Roadmap",
        "name_ar": "خارطة طريق المحفظة",
        "category_en": "Program and Portfolio Management",
        "category_ar": "إدارة البرامج والمحافظ",
        "gate": "Gate 0: Strategy & Portfolio Alignment",
        "gate_ar": "بوابة 0: المواءمة الاستراتيجية والمحفظة",
        "predecessors": ["PMO-00.06 OKR Alignment", "PMO-01.01 Business Case"],
        "predecessors_ar": ["PMO-00.06 مواءمة الأهداف والنتائج الرئيسية", "PMO-01.01 حالة الأعمال"],
        "successors": ["PMO-00.02 Program Charter", "PMO-03.01 Project Charter", "PMO-00.04 Capacity Matrix"],
        "successors_ar": ["PMO-00.02 ميثاق البرنامج", "PMO-03.01 ميثاق المشروع", "PMO-00.04 مصفوفة سعة الموارد"],
        "prep_by_en": "Portfolio Director / PMO Lead",
        "prep_by_ar": "مدير المحفظة / قائد مكتب إدارة المشاريع",
        "sign_by_en": "Executive Steering Committee / C-Suite",
        "sign_by_ar": "اللجنة التوجيهية التنفيذية / الإدارة العليا",
        "consult_en": "Program Managers, Enterprise Architects, Finance",
        "consult_ar": "مديرو البرامج، مهندسو المؤسسة، المالية",
        "inform_en": "All Project Managers, PMO Community, Department Heads",
        "inform_ar": "جميع مديري المشاريع، مجتمع PMO، رؤساء الأقسام"
    },
    {
        "ref": "PMO-00.02",
        "name_en": "Program Charter",
        "name_ar": "ميثاق البرنامج",
        "category_en": "Program and Portfolio Management",
        "category_ar": "إدارة البرامج والمحافظ",
        "gate": "Gate 0: Strategy & Portfolio Alignment",
        "gate_ar": "بوابة 0: المواءمة الاستراتيجية والمحفظة",
        "predecessors": ["PMO-00.01 Portfolio Roadmap", "PMO-01.01 Business Case"],
        "predecessors_ar": ["PMO-00.01 خارطة طريق المحفظة", "PMO-01.01 حالة الأعمال"],
        "successors": ["PMO-00.03 Interdependency Register", "PMO-03.01 Project Charter"],
        "successors_ar": ["PMO-00.03 سجل الاعتماديات المتبادلة", "PMO-03.01 ميثاق المشروع"],
        "prep_by_en": "Program Manager",
        "prep_by_ar": "مدير البرنامج",
        "sign_by_en": "Program Sponsor / Executive Governance Board",
        "sign_by_ar": "راعي البرنامج / مجلس الحوكمة التنفيذي",
        "consult_en": "Portfolio Director, Business Unit Leaders",
        "consult_ar": "مدير المحفظة، قادة وحدات الأعمال",
        "inform_en": "Project Managers within Program, Key Stakeholders",
        "inform_ar": "مديرو المشاريع التابعون للبرنامج، المعنيون الرئيسيون"
    },
    {
        "ref": "PMO-00.03",
        "name_en": "Interdependency Register",
        "name_ar": "سجل الاعتماديات المتبادلة",
        "category_en": "Program and Portfolio Management",
        "category_ar": "إدارة البرامج والمحافظ",
        "gate": "Continuous Governance across Program Lifecycle",
        "gate_ar": "حوكمة مستمرة عبر دورة حياة البرنامج",
        "predecessors": ["PMO-00.02 Program Charter", "PMO-04.03.08 Project Schedule"],
        "predecessors_ar": ["PMO-00.02 ميثاق البرنامج", "PMO-04.03.08 الجدول الزمني للمشروع"],
        "successors": ["PMO-04.08.02 Risk Register", "PMO-06.01 Project Status Report"],
        "successors_ar": ["PMO-04.08.02 سجل المخاطر", "PMO-06.01 تقرير حالة المشروع"],
        "prep_by_en": "Governance Lead / Program PMO",
        "prep_by_ar": "مسؤول الحوكمة / مكتب إدارة البرامج",
        "sign_by_en": "Program Manager & Portfolio Director",
        "sign_by_ar": "مدير البرنامج ومدير المحفظة",
        "consult_en": "Individual Project Managers, Technical Leads",
        "consult_ar": "مديرو المشاريع الفردية، القادة التقنيون",
        "inform_en": "All Project Teams across Portfolio",
        "inform_ar": "جميع فرق المشاريع عبر المحفظة"
    },
    {
        "ref": "PMO-00.04",
        "name_en": "Resource Capacity Matrix",
        "name_ar": "مصفوفة سعة الموارد",
        "category_en": "Program and Portfolio Management",
        "category_ar": "إدارة البرامج والمحافظ",
        "gate": "Gate 0 & Continuous Portfolio Planning",
        "gate_ar": "بوابة 0 وتخطيط المحفظة المستمر",
        "predecessors": ["PMO-00.01 Portfolio Roadmap", "PMO-04.06.02 Resource Requirements"],
        "predecessors_ar": ["PMO-00.01 خارطة طريق المحفظة", "PMO-04.06.02 متطلبات الموارد"],
        "successors": ["PMO-04.06.01 Resource Management Plan", "PMO-04.03.08 Project Schedule"],
        "successors_ar": ["PMO-04.06.01 خطة إدارة الموارد", "PMO-04.03.08 الجدول الزمني للمشروع"],
        "prep_by_en": "Resource Planning Manager / PMO Analyst",
        "prep_by_ar": "مدير تخطيط الموارد / محلل مكتب إدارة المشاريع",
        "sign_by_en": "Head of PMO & Department Resource Heads",
        "sign_by_ar": "رئيس مكتب إدارة المشاريع ورؤساء أقسام الموارد",
        "consult_en": "Project Managers, Functional Managers",
        "consult_ar": "مديرو المشاريع، المديرون الوظيفيون",
        "inform_en": "HR, Talent Acquisition, Operations Leads",
        "inform_ar": "الموارد البشرية، استقطاب المواهب، قادة العمليات"
    },
    {
        "ref": "PMO-00.05",
        "name_en": "PMO Maturity Assessment",
        "name_ar": "تقييم نضج مكتب إدارة المشاريع",
        "category_en": "Program and Portfolio Management",
        "category_ar": "إدارة البرامج والمحافظ",
        "gate": "Annual / Semi-Annual PMO Strategic Review",
        "gate_ar": "المراجعة الاستراتيجية السنوية/نصف السنوية لـ PMO",
        "predecessors": ["Organizational Strategic Mandate"],
        "predecessors_ar": ["التكليف الاستراتيجي المؤسسي"],
        "successors": ["PMO-02.01 Tailoring Framework", "PMO Policy Manual"],
        "successors_ar": ["PMO-02.01 إطار التخصيص", "دليل سياسات وإجراءات PMO"],
        "prep_by_en": "PMO Lead / External PMO Assessor",
        "prep_by_ar": "قائد مكتب إدارة المشاريع / مقيّم خارجي معتمد",
        "sign_by_en": "Chief Strategy Officer / PMO Executive Sponsor",
        "sign_by_ar": "رئيس قطاع الاستراتيجية / الراعي التنفيذي لـ PMO",
        "consult_en": "Senior PMs, Department Heads, PMO Staff",
        "consult_ar": "كبار مديري المشاريع، رؤساء الأقسام، فريق PMO",
        "inform_en": "Executive Committee, Enterprise Leadership",
        "inform_ar": "اللجنة التنفيذية، قيادة المنظمة"
    },
    {
        "ref": "PMO-00.06",
        "name_en": "OKR Alignment Matrix",
        "name_ar": "مصفوفة مواءمة الأهداف والنتائج الرئيسية (OKRs)",
        "category_en": "Program and Portfolio Management",
        "category_ar": "إدارة البرامج والمحافظ",
        "gate": "Gate 0: Strategic Alignment",
        "gate_ar": "بوابة 0: المواءمة الاستراتيجية",
        "predecessors": ["Enterprise Strategic Goals / Vision 2030"],
        "predecessors_ar": ["الأهداف الاستراتيجية المؤسسية / مستهدفات الرؤية"],
        "successors": ["PMO-00.01 Portfolio Roadmap", "PMO-01.01 Business Case"],
        "successors_ar": ["PMO-00.01 خارطة طريق المحفظة", "PMO-01.01 حالة الأعمال"],
        "prep_by_en": "Strategy Lead / PMO Director",
        "prep_by_ar": "مسؤول الاستراتيجية / مدير مكتب إدارة المشاريع",
        "sign_by_en": "Executive Strategy Committee",
        "sign_by_ar": "لجنة الاستراتيجية التنفيذية",
        "consult_en": "Portfolio Managers, Business Unit Heads",
        "consult_ar": "مديرو المحافظ، رؤساء وحدات الأعمال",
        "inform_en": "All PMs, Stakeholders",
        "inform_ar": "جميع مديري المشاريع، المعنيين"
    },
    # 01 Business and Value Delivery
    {
        "ref": "PMO-01.01",
        "name_en": "Business Case",
        "name_ar": "حالة الأعمال ودراسة الجدوى الاقتصادية",
        "category_en": "Business and Value Delivery",
        "category_ar": "الأعمال وتحقيق القيمة",
        "gate": "Gate 0: Justification & Funding",
        "gate_ar": "بوابة 0: التبرير والتمويل",
        "predecessors": ["PMO-00.06 OKR Alignment", "PMO-01.04 Value Proposition"],
        "predecessors_ar": ["PMO-00.06 مواءمة OKRs", "PMO-01.04 نموذج القيمة المقترحة"],
        "successors": ["PMO-01.02 Feasibility Study", "PMO-01.03 Benefits Realization", "PMO-03.01 Project Charter"],
        "successors_ar": ["PMO-01.02 دراسة الجدوى", "PMO-01.03 خطة تحقيق المنافع", "PMO-03.01 ميثاق المشروع"],
        "prep_by_en": "Lead Business Analyst / Initiative Proponent",
        "prep_by_ar": "كبير محللي الأعمال / مقدّم المبادرة",
        "sign_by_en": "Investment Committee / Chief Financial Officer (CFO)",
        "sign_by_ar": "لجنة الاستثمار / المدير المالي التنفيذي (CFO)",
        "consult_en": "Technical Architects, Subject Matter Experts, Operations",
        "consult_ar": "المهندسون التقنيون، خبراء المجال، العمليات",
        "inform_en": "PMO Director, Sponsoring Business Unit",
        "inform_ar": "مدير مكتب إدارة المشاريع، وحدة الأعمال الراعية"
    },
    {
        "ref": "PMO-01.02",
        "name_en": "Feasibility Study",
        "name_ar": "دراسة الجدوى الشاملة",
        "category_en": "Business and Value Delivery",
        "category_ar": "الأعمال وتحقيق القيمة",
        "gate": "Gate 0: Justification & Funding",
        "gate_ar": "بوابة 0: التبرير والتمويل",
        "predecessors": ["PMO-01.01 Business Case"],
        "predecessors_ar": ["PMO-01.01 حالة الأعمال"],
        "successors": ["PMO-03.01 Project Charter"],
        "successors_ar": ["PMO-03.01 ميثاق المشروع"],
        "prep_by_en": "Lead Evaluator / Technical Specialist",
        "prep_by_ar": "رئيس فريق التقييم / الأخصائي التقني",
        "sign_by_en": "Steering Committee / Sponsoring Executive",
        "sign_by_ar": "اللجنة التوجيهية / الراعي التنفيذي",
        "consult_en": "Legal, Compliance, Procurement, Engineering",
        "consult_ar": "الشؤون القانونية، الامتثال، المشتريات، الهندسة",
        "inform_en": "Business Analyst, PMO",
        "inform_ar": "محلل الأعمال، مكتب إدارة المشاريع"
    },
    {
        "ref": "PMO-01.03",
        "name_en": "Benefits Realization Plan",
        "name_ar": "خطة تحقيق ومتابعة المنافع",
        "category_en": "Business and Value Delivery",
        "category_ar": "الأعمال وتحقيق القيمة",
        "gate": "Gate 0 through Gate 5 (Lifecycle Long)",
        "gate_ar": "بوابة 0 حتى بوابة 5 (طوال دورة الحياة)",
        "predecessors": ["PMO-01.01 Business Case"],
        "predecessors_ar": ["PMO-01.01 حالة الأعمال"],
        "successors": ["PMO-07.05 Post Implementation Review"],
        "successors_ar": ["PMO-07.05 مراجعة ما بعد التنفيذ"],
        "prep_by_en": "Benefits Owner / Business Analyst",
        "prep_by_ar": "مالك المنافع / محلل الأعمال",
        "sign_by_en": "Business Sponsor & Portfolio Director",
        "sign_by_ar": "الراعي التنفيذي ومدير المحفظة",
        "consult_en": "Project Manager, Operations Director",
        "consult_ar": "مدير المشروع، مدير العمليات التشغيلية",
        "inform_en": "Executive Committee, Finance",
        "inform_ar": "اللجنة التنفيذية، المالية"
    },
    {
        "ref": "PMO-01.04",
        "name_en": "Value Proposition Canvas",
        "name_ar": "نموذج القيمة المقترحة (Canvas)",
        "category_en": "Business and Value Delivery",
        "category_ar": "الأعمال وتحقيق القيمة",
        "gate": "Gate 0: Product & Service Definition",
        "gate_ar": "بوابة 0: تعريف المنتج والخدمة",
        "predecessors": ["Market Research / User Need Analysis"],
        "predecessors_ar": ["أبحاث السوق / تحليل احتياجات المستخدمين"],
        "successors": ["PMO-01.01 Business Case", "PMO-03.02 Product Vision"],
        "successors_ar": ["PMO-01.01 حالة الأعمال", "PMO-03.02 رؤية المنتج"],
        "prep_by_en": "Product Strategist / UX Lead",
        "prep_by_ar": "مخطط المنتج الاستراتيجي / قائد تجربة المستخدم",
        "sign_by_en": "Product Owner / Business Sponsor",
        "sign_by_ar": "مالك المنتج / راعي الأعمال",
        "consult_en": "End Users, Sales/Marketing, Delivery Lead",
        "consult_ar": "المستخدمون النهائيون، المبيعات/التسويق، قائد التسليم",
        "inform_en": "Project Team, PMO",
        "inform_ar": "فريق المشروع، مكتب إدارة المشاريع"
    },
    # 02 Project Approach and Tailoring
    {
        "ref": "PMO-02.01",
        "name_en": "Development Approach Assessment",
        "name_ar": "تقييم منهجية التطوير ودورة الحياة",
        "category_en": "Project Approach and Tailoring",
        "category_ar": "نهج المشروع وتخصيص المنهجية",
        "gate": "Gate 1: Initiation",
        "gate_ar": "بوابة 1: البدء والاعتماد",
        "predecessors": ["PMO-01.01 Business Case", "PMO-02.02 Complexity Model"],
        "predecessors_ar": ["PMO-01.01 حالة الأعمال", "PMO-02.02 نموذج تقييم التعقيد"],
        "successors": ["PMO-03.01 Project Charter", "PMO-04.01.01 Project Management Plan"],
        "successors_ar": ["PMO-03.01 ميثاق المشروع", "PMO-04.01.01 خطة إدارة المشروع"],
        "prep_by_en": "Methodology Lead / Senior PM",
        "prep_by_ar": "مسؤول المنهجية / كبير مديري المشاريع",
        "sign_by_en": "PMO Director",
        "sign_by_ar": "مدير مكتب إدارة المشاريع",
        "consult_en": "Technical Lead, Agile Coach, Project Sponsor",
        "consult_ar": "القائد التقني، مدرب الأجايل، راعي المشروع",
        "inform_en": "Project Team",
        "inform_ar": "فريق المشروع"
    },
    {
        "ref": "PMO-02.02",
        "name_en": "Complexity Assessment Model",
        "name_ar": "نموذج تقييم تعقيد المشروع",
        "category_en": "Project Approach and Tailoring",
        "category_ar": "نهج المشروع وتخصيص المنهجية",
        "gate": "Gate 1: Initiation & Tier Sizing",
        "gate_ar": "بوابة 1: البدء وتحديد فئة المشروع",
        "predecessors": ["PMO-01.01 Business Case"],
        "predecessors_ar": ["PMO-01.01 حالة الأعمال"],
        "successors": ["PMO-02.01 Development Approach", "Project Sizing Tier Assignment"],
        "successors_ar": ["PMO-02.01 منهجية التطوير", "تحديد فئة حوكمة المشروع (Tier)"],
        "prep_by_en": "PMO Assessor / Project Manager",
        "prep_by_ar": "مقيّم مكتب إدارة المشاريع / مدير المشروع",
        "sign_by_en": "PMO Lead",
        "sign_by_ar": "قائد مكتب إدارة المشاريع",
        "consult_en": "Domain Experts, Risk Manager",
        "consult_ar": "خبراء المجال، مدير المخاطر",
        "inform_en": "Project Sponsor",
        "inform_ar": "راعي المشروع"
    },
    {
        "ref": "PMO-02.03",
        "name_en": "AI Ethics and Governance Checklist",
        "name_ar": "قائمة التحقق لأخلاقيات وحوكمة الذكاء الاصطناعي",
        "category_en": "Project Approach and Tailoring",
        "category_ar": "نهج المشروع وتخصيص المنهجية",
        "gate": "Gate 1 & Continuous AI Verification",
        "gate_ar": "بوابة 1 والتحقق المستمر من الذكاء الاصطناعي",
        "predecessors": ["PMO-02.04 AI Use Case Canvas"],
        "predecessors_ar": ["PMO-02.04 بطاقة حالة استخدام الذكاء الاصطناعي"],
        "successors": ["PMO-04.08.02 Risk Register (AI Ethical Risks)"],
        "successors_ar": ["PMO-04.08.02 سجل المخاطر (مخاطر الذكاء الاصطناعي)"],
        "prep_by_en": "AI Governance Lead / AI Engineer",
        "prep_by_ar": "مسؤول حوكمة الذكاء الاصطناعي / مهندس الذكاء الاصطناعي",
        "sign_by_en": "Chief AI / Data Officer & Legal Counsel",
        "sign_by_ar": "كبير مسؤولي البيانات والذكاء الاصطناعي والمستشار القانوني",
        "consult_en": "Data Privacy Officer, Security Lead",
        "consult_ar": "مسؤول خصوصية البيانات، قائد أمن المعلومات",
        "inform_en": "Project Manager, Development Team",
        "inform_ar": "مدير المشروع، فريق التطوير"
    },
    {
        "ref": "PMO-02.04",
        "name_en": "AI Canvas and Use Case Card",
        "name_ar": "بطاقة حالة استخدام الذكاء الاصطناعي (AI Canvas)",
        "category_en": "Project Approach and Tailoring",
        "category_ar": "نهج المشروع وتخصيص المنهجية",
        "gate": "Gate 0 / Gate 1: AI Scoping",
        "gate_ar": "بوابة 0 / بوابة 1: تحديد نطاق الذكاء الاصطناعي",
        "predecessors": ["PMO-01.01 Business Case"],
        "predecessors_ar": ["PMO-01.01 حالة الأعمال"],
        "successors": ["PMO-02.03 AI Ethics Checklist", "PMO-03.01 Project Charter"],
        "successors_ar": ["PMO-02.03 قائمة أخلاقيات الذكاء الاصطناعي", "PMO-03.01 ميثاق المشروع"],
        "prep_by_en": "AI Product Owner / Data Scientist",
        "prep_by_ar": "مالك منتج الذكاء الاصطناعي / عالم البيانات",
        "sign_by_en": "Head of AI / Business Sponsor",
        "sign_by_ar": "رئيس قطاع الذكاء الاصطناعي / راعي الأعمال",
        "consult_en": "Data Engineers, ML Ops Lead",
        "consult_ar": "مهندسو البيانات، قائد عمليات تعلم الآلة MLOps",
        "inform_en": "PMO, Delivery Team",
        "inform_ar": "مكتب إدارة المشاريع، فريق التسليم"
    },
    {
        "ref": "PMO-02.05",
        "name_en": "Governance and Compliance Matrix",
        "name_ar": "مصفوفة الحوكمة والامتثال التنظيمي",
        "category_en": "Project Approach and Tailoring",
        "category_ar": "نهج المشروع وتخصيص المنهجية",
        "gate": "Gate 1 & Gate 2: Planning Baseline",
        "gate_ar": "بوابة 1 وبوابة 2: خط الأساس للتخطيط",
        "predecessors": ["PMO-03.01 Project Charter"],
        "predecessors_ar": ["PMO-03.01 ميثاق المشروع"],
        "successors": ["PMO-04.05.01 Quality Plan", "PMO-06.07 Procurement/Compliance Audit"],
        "successors_ar": ["PMO-04.05.01 خطة الجودة", "PMO-06.07 تدقيق الامتثال"],
        "prep_by_en": "Compliance Officer / PMO Lead",
        "prep_by_ar": "مسؤول الامتثال / قائد مكتب إدارة المشاريع",
        "sign_by_en": "Legal & Regulatory Affairs Director",
        "sign_by_ar": "مدير الشؤون القانونية والتنظيمية",
        "consult_en": "Project Manager, Security Architect",
        "consult_ar": "مدير المشروع، مهندس أمن المعلومات",
        "inform_en": "Steering Committee",
        "inform_ar": "اللجنة التوجيهية"
    },
    # 03 Initiating
    {
        "ref": "PMO-03.01",
        "name_en": "Project Charter",
        "name_ar": "ميثاق المشروع المعتمد",
        "category_en": "Initiating",
        "category_ar": "البدء والاعتماد",
        "gate": "Gate 1: Project Authorization",
        "gate_ar": "بوابة 1: التفويض الرسمي للمشروع",
        "predecessors": ["PMO-01.01 Business Case", "PMO-02.01 Development Approach"],
        "predecessors_ar": ["PMO-01.01 حالة الأعمال", "PMO-02.01 منهجية التطوير"],
        "successors": ["PMO-03.03 Assumption Log", "PMO-03.04 Stakeholder Register", "PMO-04.01.01 Project Management Plan"],
        "successors_ar": ["PMO-03.03 سجل الافتراضات", "PMO-03.04 سجل المعنيين", "PMO-04.01.01 خطة إدارة المشروع"],
        "prep_by_en": "Project Manager / Initiator",
        "prep_by_ar": "مدير المشروع / مقدّم المبادرة",
        "sign_by_en": "Project Sponsor & PMO Lead",
        "sign_by_ar": "راعي المشروع وقائد مكتب إدارة المشاريع",
        "consult_en": "Lead Technical Architect, Business Analyst",
        "consult_ar": "كبير المهندسين التقنيين، محلل الأعمال",
        "inform_en": "All Project Stakeholders & Delivery Team",
        "inform_ar": "جميع المعنيين بالمشروع وفريق التسليم"
    },
    {
        "ref": "PMO-03.02",
        "name_en": "Product Vision",
        "name_ar": "وثيقة رؤية المنتج",
        "category_en": "Initiating",
        "category_ar": "البدء والاعتماد",
        "gate": "Gate 1: Agile / Product Initiation",
        "gate_ar": "بوابة 1: بدء المنتجات والمنهجيات الرشيقة",
        "predecessors": ["PMO-01.04 Value Proposition Canvas"],
        "predecessors_ar": ["PMO-01.04 نموذج القيمة المقترحة"],
        "successors": ["PMO-04.02.08 Product Backlog", "PMO-04.02.09 Story Mapping"],
        "successors_ar": ["PMO-04.02.08 تراكم المنتج", "PMO-04.02.09 خريطة قصص المستخدم"],
        "prep_by_en": "Product Owner / Product Manager",
        "prep_by_ar": "مالك المنتج / مدير المنتج",
        "sign_by_en": "Executive Business Sponsor",
        "sign_by_ar": "الراعي التنفيذي للأعمال",
        "consult_en": "Agile Team, UX Designers, Key Customers",
        "consult_ar": "فريق الأجايل، مصممو تجربة المستخدم، العملاء الرئيسيون",
        "inform_en": "Scrum Master, Development Team, PMO",
        "inform_ar": "سيد السكروم، فريق التطوير، مكتب إدارة المشاريع"
    },
    {
        "ref": "PMO-03.03",
        "name_en": "Assumption Log",
        "name_ar": "سجل الافتراضات والقيود",
        "category_en": "Initiating",
        "category_ar": "البدء والاعتماد",
        "gate": "Gate 1 & Continuous Planning",
        "gate_ar": "بوابة 1 والتخطيط المستمر",
        "predecessors": ["PMO-03.01 Project Charter", "PMO-01.01 Business Case"],
        "predecessors_ar": ["PMO-03.01 ميثاق المشروع", "PMO-01.01 حالة الأعمال"],
        "successors": ["PMO-04.08.02 Risk Register", "PMO-04.02.05 Project Scope Statement"],
        "successors_ar": ["PMO-04.08.02 سجل المخاطر", "PMO-04.02.05 بيان نطاق المشروع"],
        "prep_by_en": "Project Manager",
        "prep_by_ar": "مدير المشروع",
        "sign_by_en": "Project Manager & PMO Lead (Review)",
        "sign_by_ar": "مدير المشروع وقائد مكتب إدارة المشاريع (مراجعة)",
        "consult_en": "Project Team, Technical Leads, Procurement",
        "consult_ar": "فريق المشروع، القادة التقنيون، المشتريات",
        "inform_en": "Project Sponsor",
        "inform_ar": "راعي المشروع"
    },
    {
        "ref": "PMO-03.04",
        "name_en": "Stakeholder Register",
        "name_ar": "سجل المعنيين بالمشروع",
        "category_en": "Initiating",
        "category_ar": "البدء والاعتماد",
        "gate": "Gate 1 & Continuous Stakeholder Mgmt",
        "gate_ar": "بوابة 1 وإدارة المعنيين المستمرة",
        "predecessors": ["PMO-03.01 Project Charter"],
        "predecessors_ar": ["PMO-03.01 ميثاق المشروع"],
        "successors": ["PMO-03.05 Stakeholder Analysis", "PMO-04.10.01 Stakeholder Plan", "PMO-04.07.01 Communications Plan"],
        "successors_ar": ["PMO-03.05 تحليل المعنيين", "PMO-04.10.01 خطة إشراك المعنيين", "PMO-04.07.01 خطة إدارة التواصل"],
        "prep_by_en": "Project Manager",
        "prep_by_ar": "مدير المشروع",
        "sign_by_en": "Project Manager",
        "sign_by_ar": "مدير المشروع",
        "consult_en": "Project Sponsor, PMO, Functional Managers",
        "consult_ar": "راعي المشروع، مكتب إدارة المشاريع، المديرون الوظيفيون",
        "inform_en": "Internal Project Team",
        "inform_ar": "فريق المشروع الداخلي"
    },
    {
        "ref": "PMO-03.05",
        "name_en": "Stakeholder Analysis",
        "name_ar": "تحليل ومصفوفة المعنيين (القوة والاهتمام)",
        "category_en": "Initiating",
        "category_ar": "البدء والاعتماد",
        "gate": "Gate 1 & Gate 2: Planning",
        "gate_ar": "بوابة 1 وبوابة 2: التخطيط",
        "predecessors": ["PMO-03.04 Stakeholder Register"],
        "predecessors_ar": ["PMO-03.04 سجل المعنيين"],
        "successors": ["PMO-04.10.01 Stakeholder Engagement Plan"],
        "successors_ar": ["PMO-04.10.01 خطة إشراك المعنيين"],
        "prep_by_en": "Project Manager / Communications Lead",
        "prep_by_ar": "مدير المشروع / مسؤول التواصل",
        "sign_by_en": "Project Manager",
        "sign_by_ar": "مدير المشروع",
        "consult_en": "Project Sponsor, PMO",
        "consult_ar": "راعي المشروع، مكتب إدارة المشاريع",
        "inform_en": "Project Leadership Team",
        "inform_ar": "فريق قيادة المشروع"
    },
]

def generate_markdown_docs():
    # Build full dependency document in English
    dep_en = """# 🔗 Tasleemat Document Dependencies & Lifecycle Architecture
**Document Reference:** `TASLEEMAT-DOC-DEPENDENCIES-v2.0`  
**Standard:** PMI PMBOK® 6th, 7th & 8th Edition Standard  

---

## 🎯 Executive Overview

In the **Tasleemat PMO Operating System**, no document exists in isolation. Every form and artifact functions as a node in a connected **Directed Acyclic Graph (DAG)** of project inputs, baselines, operational logs, monitoring reports, and closeout assets.

```mermaid
flowchart TD
    subgraph G0["Gate 0: Strategic Alignment & Concept"]
        G0_1["PMO-00.06 OKR Alignment"] --> G0_2["PMO-01.01 Business Case"]
        G0_2 --> G0_3["PMO-01.02 Feasibility Study"]
        G0_2 --> G0_4["PMO-01.03 Benefits Realization"]
        G0_2 --> G0_5["PMO-00.01 Portfolio Roadmap"]
    end

    subgraph G1["Gate 1: Initiation & Authorization"]
        G0_2 --> G1_1["PMO-03.01 Project Charter"]
        G1_1 --> G1_2["PMO-03.03 Assumption Log"]
        G1_1 --> G1_3["PMO-03.04 Stakeholder Register"]
        G1_3 --> G1_4["PMO-03.05 Stakeholder Analysis"]
    end

    subgraph G2["Gate 2: Integrated Baseline Sign-off"]
        G1_1 --> G2_PMP["PMO-04.01.01 Project Mgmt Plan"]
        G2_PMP --> G2_SC["PMO-04.02.05 Scope Statement"]
        G2_SC --> G2_WBS["PMO-04.02.06 WBS & Dictionary"]
        G2_WBS --> G2_SCH["PMO-04.03.07 Schedule Baseline"]
        G2_WBS --> G2_CST["PMO-04.04.04 Cost Baseline"]
        G1_2 --> G2_RSK["PMO-04.08.02 Risk Register"]
        G2_PMP --> G2_RACI["PMO-04.06.04 RACI Matrix"]
    end

    subgraph G3["Gate 3: Execution & Control"]
        G2_PMP --> G3_ISS["PMO-05.01 Issue Log"]
        G2_PMP --> G3_DEC["PMO-05.02 Decision Log"]
        G3_ISS --> G3_CR["PMO-05.03 Change Request"]
        G3_CR --> G3_CHG["PMO-05.04 Change Log"]
        G2_SCH --> G3_EVM["PMO-06.05 Earned Value (EVM)"]
        G2_CST --> G3_EVM
        G3_EVM --> G3_PSR["PMO-06.01 Status Report"]
    end

    subgraph G4["Gate 4: Handover & Acceptance"]
        G2_WBS --> G4_UAT["PMO-06.10 UAT Sign-off"]
        G4_UAT --> G4_DEL["PMO-06.08 Deliverable Acceptance"]
        G4_DEL --> G4_OPS["PMO-07.04 Transition to Ops"]
    end

    subgraph G5["Gate 5: Closeout & Realization"]
        G4_OPS --> G5_CL["PMO-07.03 Project Closeout"]
        G3_ISS --> G5_LL["PMO-07.01 Lessons Learned"]
        G2_RSK --> G5_LL
        G5_CL --> G5_BEN["PMO-07.05 Post Implementation Review"]
        G0_4 --> G5_BEN
    end
```

---

## 📋 Comprehensive Dependency Index (Across All 102 Forms)

| Ref ID | Form Name | Primary Stage / Gate | Direct Predecessors (Inputs) | Direct Successors (Outputs) |
| :--- | :--- | :--- | :--- | :--- |
"""
    for item in FORMS_METADATA:
        preds = ", ".join(f"`{p}`" for p in item["predecessors"])
        succs = ", ".join(f"`{s}`" for s in item["successors"])
        dep_en += f"| **`{item['ref']}`** | {item['name_en']} | {item['gate']} | {preds} | {succs} |\n"

    dep_en += """
---
*Note: For the remaining standard domain plans (Communications, Procurement, Quality, Risk, ESG), each plan depends directly on `PMO-04.01.01 Project Management Plan` and `PMO-03.01 Project Charter`, and produces operational logs in Phase 05/06.*
"""

    (ROOT / "docs/en/07_document_dependencies.md").write_text("<p align=\"center\">\n  <img src=\"../img/logo.png\" alt=\"Tasleemat Logo\" width=\"320\" />\n</p>\n\n---\n\n" + dep_en, encoding="utf-8")
    print("Created docs/en/07_document_dependencies.md")

    # Arabic version
    dep_ar = """# 🔗 شبكة اعتماديات الوثائق وهندسة دورة الحياة في تسليمات
**مرجع الوثيقة:** `TASLEEMAT-DOC-DEPENDENCIES-AR-v2.0`  
**المعيار:** متوافق مع معايير معهد إدارة المشاريع العالمي PMI PMBOK® الإصدارات 6 و 7 و 8  

---

## 🎯 نظرة عامة تنفيذية

في **نظام تشغيل مكاتب إدارة المشاريع «تسليمات»**، لا توجد وثيقة معزولة. تعمل كل استمارة كعقدة مترابطة في **شبكة اعتماديات موجهة (DAG)** تربط المدخلات الاستراتيجية، وخطوط الأساس المعتمدة، وسجلات المتابعة التشغيلية، وتقارير الرقابة والتحكم، حتى أصول الإغلاق المؤسسي.

```mermaid
flowchart TD
    subgraph G0["بوابة 0: المواءمة الاستراتيجية ودراسة الفكرة"]
        G0_1["PMO-00.06 مواءمة OKRs"] --> G0_2["PMO-01.01 حالة الأعمال"]
        G0_2 --> G0_3["PMO-01.02 دراسة الجدوى"]
        G0_2 --> G0_4["PMO-01.03 خطة المنافع"]
        G0_2 --> G0_5["PMO-00.01 خارطة المحفظة"]
    end

    subgraph G1["بوابة 1: البدء والاعتماد المؤسسي"]
        G0_2 --> G1_1["PMO-03.01 ميثاق المشروع"]
        G1_1 --> G1_2["PMO-03.03 سجل الافتراضات"]
        G1_1 --> G1_3["PMO-03.04 سجل المعنيين"]
        G1_3 --> G1_4["PMO-03.05 تحليل المعنيين"]
    end

    subgraph G2["بوابة 2: اعتماد خط الأساس المتكامل"]
        G1_1 --> G2_PMP["PMO-04.01.01 خطة إدارة المشروع"]
        G2_PMP --> G2_SC["PMO-04.02.05 بيان النطاق"]
        G2_SC --> G2_WBS["PMO-04.02.06 هيكل تجزئة العمل WBS"]
        G2_WBS --> G2_SCH["PMO-04.03.07 خط الأساس للجدول"]
        G2_WBS --> G2_CST["PMO-04.04.04 خط الأساس للتكلفة"]
        G1_2 --> G2_RSK["PMO-04.08.02 سجل المخاطر"]
        G2_PMP --> G2_RACI["PMO-04.06.04 مصفوفة RACI"]
    end

    subgraph G3["بوابة 3: التنفيذ والتحكم اليومي"]
        G2_PMP --> G3_ISS["PMO-05.01 سجل المشكلات"]
        G2_PMP --> G3_DEC["PMO-05.02 سجل القرارات"]
        G3_ISS --> G3_CR["PMO-05.03 طلب التغيير"]
        G3_CR --> G3_CHG["PMO-05.04 سجل التغييرات"]
        G2_SCH --> G3_EVM["PMO-06.05 تحليل القيمة المكتسبة"]
        G2_CST --> G3_EVM
        G3_EVM --> G3_PSR["PMO-06.01 تقرير حالة المشروع"]
    end

    subgraph G4["بوابة 4: القبول والتسليم التشغيلي"]
        G2_WBS --> G4_UAT["PMO-06.10 اعتماد اختبارات UAT"]
        G4_UAT --> G4_DEL["PMO-06.08 القبول الرسمي للمنتج"]
        G4_DEL --> G4_OPS["PMO-07.04 التحول للعمليات التشغيلية"]
    end

    subgraph G5["بوابة 5: الإغلاق المؤسسي وتحقيق المنافع"]
        G4_OPS --> G5_CL["PMO-07.03 وثيقة إغلاق المشروع"]
        G3_ISS --> G5_LL["PMO-07.01 سجل الدروس المستفادة"]
        G2_RSK --> G5_LL
        G5_CL --> G5_BEN["PMO-07.05 مراجعة ما بعد التنفيذ"]
        G0_4 --> G5_BEN
    end
```

---

## 📋 جدول مصفوفة الاعتماديات الشاملة

| رمز النموذج | اسم الوثيقة | المرحلة / بوابة العبور | المدخلات المباشرة (الوثائق السابقة) | المخرجات المباشرة (الوثائق اللاحقة) |
| :--- | :--- | :--- | :--- | :--- |
"""
    for item in FORMS_METADATA:
        preds_ar = ", ".join(f"`{p}`" for p in item["predecessors_ar"])
        succs_ar = ", ".join(f"`{s}`" for s in item["successors_ar"])
        dep_ar += f"| **`{item['ref']}`** | {item['name_ar']} | {item['gate_ar']} | {preds_ar} | {succs_ar} |\n"

    (ROOT / "docs/ar/07_document_dependencies.md").write_text("<p align=\"center\">\n  <img src=\"../img/logo-ar.png\" alt=\"شعار تسليمات\" width=\"320\" />\n</p>\n\n---\n\n" + dep_ar, encoding="utf-8")
    print("Created docs/ar/07_document_dependencies.md")

    # RACI Matrix in English
    raci_en = """# 👥 Tasleemat Master Governance RACI & Signature Authority Matrix
**Document Reference:** `TASLEEMAT-GOVERNANCE-RACI-v2.0`  
**Scope:** Complete RACI authority framework across all 102 forms  

---

## 🎯 Executive Overview

This matrix defines the strict governance authority and accountability for creating, approving, consulting on, and reporting every artifact within the PMO ecosystem:
* **Responsible (Prepared By / Author):** The operational role accountable for authoring and maintaining the document.
* **Accountable (Signed / Approved By):** The sole executive authority who approves and signs the document into formal baseline.
* **Consulted:** Subject matter experts and operational stakeholders who provide vital input.
* **Informed / Reported To:** Stakeholders who receive status reports and final signed copies.

---

## 🏛️ Master RACI Authority Index

| Ref ID | Form Name | Responsible (Prepared By) | Accountable (Signed / Approved By) | Consulted (Contributors) | Informed (Reported To) |
| :--- | :--- | :--- | :--- | :--- | :--- |
"""
    for item in FORMS_METADATA:
        raci_en += f"| **`{item['ref']}`** | {item['name_en']} | {item['prep_by_en']} | **{item['sign_by_en']}** | {item['consult_en']} | {item['inform_en']} |\n"

    (ROOT / "docs/en/06_raci_authority_matrix.md").write_text("<p align=\"center\">\n  <img src=\"../img/logo.png\" alt=\"Tasleemat Logo\" width=\"320\" />\n</p>\n\n---\n\n" + raci_en, encoding="utf-8")
    print("Created docs/en/06_raci_authority_matrix.md")

    # RACI Matrix in Arabic
    raci_ar = """# 👥 مصفوفة RACI والصلاحيات والاعتماد المؤسسي لمكتب إدارة المشاريع
**مرجع الوثيقة:** `TASLEEMAT-GOVERNANCE-RACI-AR-v2.0`  
**النطاق:** مصفوفة الحوكمة والاعتمادات الشاملة لكافة النماذج الـ 102  

---

## 🎯 نظرة عامة تنفيذية

تحدد هذه المصفوفة الصلاحيات والحوكمة المؤسسية لإعداد، واعتماد، واستشارة، وإبلاغ كافة الوثائق في منظومة مكاتب إدارة المشاريع:
* **المسؤول عن الإعداد (Responsible / Prepared By):** الدور التشغيلي المكلف بصياغة الوثيقة وتحديثها.
* **المعتمد والموقع (Accountable / Signed By):** السلطة التنفيذية المسؤولة قانونياً ومؤسسياً عن اعتماد الوثيقة.
* **المستشار (Consulted):** الخبراء والمعنيون الذين يتم الرجوع إليهم لتقديم المدخلات التخصصية.
* **المُبَلَّغ (Informed / Reported To):** الفئات التي يتم إطلاعها وإرسال التقارير والنسخ المعتمدة إليها.

---

## 🏛️ جدول مصفوفة الصلاحيات والحوكمة RACI

| رمز النموذج | اسم الوثيقة | المسؤول عن الإعداد (Prepared By) | المعتمد والموقع (Approved By) | المستشارون (Consulted) | المُبَلَّغون (Informed To) |
| :--- | :--- | :--- | :--- | :--- | :--- |
"""
    for item in FORMS_METADATA:
        raci_ar += f"| **`{item['ref']}`** | {item['name_ar']} | {item['prep_by_ar']} | **{item['sign_by_ar']}** | {item['consult_ar']} | {item['inform_ar']} |\n"

    (ROOT / "docs/ar/06_raci_authority_matrix.md").write_text("<p align=\"center\">\n  <img src=\"../img/logo-ar.png\" alt=\"شعار تسليمات\" width=\"320\" />\n</p>\n\n---\n\n" + raci_ar, encoding="utf-8")
    print("Created docs/ar/06_raci_authority_matrix.md")

def main():
    generate_markdown_docs()

if __name__ == "__main__":
    main()
