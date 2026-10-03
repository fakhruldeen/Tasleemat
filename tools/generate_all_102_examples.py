#!/usr/bin/env python3
"""
Master Example Generator for Tasleemat (102 English & 102 Arabic Forms)
Produces complete, realistic, gold-standard reference examples with zero unfilled placeholders,
preserving all fixed template row labels, ensuring chronological logical coherence,
and using 100% fictional entities (Apex Global Solutions / شركة القمة للحلول المؤسسية المتقدمة).
"""

import os
import re
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORMS_EN_DIR = os.path.join(REPO_ROOT, 'forms', 'en')
FORMS_AR_DIR = os.path.join(REPO_ROOT, 'forms', 'ar')
EXAMPLES_EN_DIR = os.path.join(REPO_ROOT, 'examples', 'en')
EXAMPLES_AR_DIR = os.path.join(REPO_ROOT, 'examples', 'ar')

EN_PLACEHOLDERS = {
    "Company_Name": "Apex Global Solutions",
    "Portfolio_Name": "Enterprise Digital Transformation & Cloud Operations Portfolio",
    "Portfolio_ID": "PORT-2026-X01",
    "Portfolio_or_Program_Name": "Enterprise Digital Transformation & Cloud Operations Portfolio",
    "Program_Name": "Unified Cloud Infrastructure & Enterprise Services Program",
    "Program_ID": "PGM-2026-CX",
    "Program_or_Initiative_Name": "Unified Cloud Infrastructure & Enterprise Services Program",
    "Project_Name": "Apex Unified Cloud ERP & Supply Chain Modernization",
    "Project_ID": "PRJ-2026-ERP-01",
    "Initiative_Name": "Core Modernization & Cloud Migration Initiative",
    "Initiative_or_Project_Name": "Apex Unified Cloud ERP & Supply Chain Modernization",
    "Product_Name": "Apex Enterprise Nexus ERP Platform",
    "Product_ID": "PROD-NX-2026",
    "Product_or_Service_Name": "Apex Enterprise Nexus ERP Platform",
    "AI_Solution_Name": "Apex Enterprise Cognitive Assistant (AECA)",
    "AI_System_or_Program_Name": "Apex Enterprise Cognitive AI System",
    "System_or_Initiative_Name": "Apex Enterprise Nexus ERP Platform",
    "Current_Date": "2026-03-15",
    "Date": "2026-03-15",
    "Today_Date": "2026-03-15",
    "Current_Timestamp": "2026-03-15 10:00 UTC",
    "Creation_Time": "2026-03-15 10:00 UTC",
    "Prepared_By": "Faisal Al-Harbi, PMP (Senior Project Manager)",
    "Author_Name": "Faisal Al-Harbi, PMP (Senior Project Manager)",
    "Document_Author": "Faisal Al-Harbi, PMP (Senior Project Manager)",
    "Preparer_Name": "Faisal Al-Harbi, PMP (Senior Project Manager)",
    "Project_Manager_Name": "Faisal Al-Harbi, PMP",
    "Project_Sponsor_Name": "Dr. Muna Al-Ghamdi (Executive VP of Technology)",
    "Executive_Sponsor_Name": "Dr. Muna Al-Ghamdi (Executive Vice President)",
    "Program_Sponsor_Name": "Dr. Muna Al-Ghamdi (Executive Vice President)",
    "Initiative_Sponsor_Name": "Dr. Muna Al-Ghamdi (Executive Vice President)",
    "Program_Manager_Name": "Khalid Al-Otaibi, PgMP",
    "Program_Director_Name": "Khalid Al-Otaibi, PgMP",
    "Portfolio_Manager_Name": "Elena Vance, PfMP",
    "Portfolio_Director_Name": "Elena Vance, PfMP",
    "PMO_Director_Name": "Tariq Al-Mansoor, PfMP",
    "PMO_Manager_Name": "Tariq Al-Mansoor, PfMP",
    "PMO_Lead_Name": "Tariq Al-Mansoor, PfMP",
    "PMO_Office_Name": "Enterprise Program Management & Transformation Office (PMO)",
    "Business_Owner_Name": "Sultan Al-Dossary (VP of Operations)",
    "Operations_VP_Name": "Sultan Al-Dossary (VP of Operations)",
    "Operations_Lead_Name": "Sultan Al-Dossary (VP of Operations)",
    "Operations_Owner_Name": "Sultan Al-Dossary (VP of Operations)",
    "Lead_Architect_Name": "Fahad Al-Subaie (Chief Solution Architect)",
    "Technical_Lead_Name": "Fahad Al-Subaie (Chief Solution Architect)",
    "Engineering_Lead_Name": "Eng. Tariq Al-Najjar (Principal Systems Engineer)",
    "Chief_Systems_Engineer_Name": "Eng. Omar Al-Khatib",
    "Quality_Manager_Name": "Noura Al-Sayed (Director of Quality Assurance)",
    "QA_Manager_Name": "Noura Al-Sayed (Director of Quality Assurance)",
    "QA_Lead_Name": "Noura Al-Sayed (Director of Quality Assurance)",
    "Lead_Auditor_Name": "Adel Al-Mutairi, CIA",
    "Risk_Manager_Name": "Layla Al-Omari, PMI-RMP",
    "Risk_Analyst_Name": "Layla Al-Omari, PMI-RMP",
    "Risk_Owner_Name": "Faisal Al-Harbi, PMP",
    "Cost_Estimator_Name": "Zaid Al-Ghamdi, CCEA",
    "Lead_Estimator_Name": "Zaid Al-Ghamdi, CCEA",
    "Financial_Controller_Name": "Bader Al-Mutairi (Chief Financial Officer)",
    "Cost_Controller_Name": "Bader Al-Mutairi (Chief Financial Officer)",
    "Procurement_Manager_Name": "Mansour Al-Shehri (Head of Strategic Sourcing)",
    "Procurement_Lead_Name": "Mansour Al-Shehri (Head of Strategic Sourcing)",
    "Tender_Chair_Name": "Mansour Al-Shehri (Head of Strategic Sourcing)",
    "Bids_Chair_Name": "Mansour Al-Shehri (Head of Strategic Sourcing)",
    "Contracts_Manager_Name": "Mansour Al-Shehri (Contracts Director)",
    "Change_Manager_Name": "Dr. Sarah Al-Kuwaiti, Prosci CCP",
    "Change_Lead_Name": "Dr. Sarah Al-Kuwaiti, Prosci CCP",
    "Communications_Lead_Name": "Huda Al-Hashimi (Director of Corporate Communications)",
    "Stakeholder_Lead_Name": "Huda Al-Hashimi (Stakeholder Engagement Lead)",
    "Stakeholder_Representative_Name": "Huda Al-Hashimi (Communications Lead)",
    "HR_Lead_Name": "Sami Al-Ghamdi (HR Business Partner)",
    "HR_Partner_Name": "Sami Al-Ghamdi (HR Business Partner)",
    "HR_Coordinator_Name": "Sami Al-Ghamdi (HR Specialist)",
    "Training_Coordinator_Name": "Reem Al-Shammari (Lead Training Coordinator)",
    "ESG_Officer_Name": "Eng. Yasser Al-Subaie (ESG & Sustainability Director)",
    "DPO_Name": "Abdulaziz Al-Zahrani (Data Protection Officer)",
    "Data_Privacy_Officer_Name": "Abdulaziz Al-Zahrani (Data Protection Officer)",
    "Compliance_Officer_Name": "Abdulaziz Al-Zahrani (Compliance Director)",
    "Legal_Counsel_Name": "Adv. Majed Al-Farooq (Senior Legal Counsel)",
    "AI_Lead_Name": "Dr. Rayan Al-Sulaiman (Lead AI & Data Scientist)",
    "AI_Engineer_Name": "Eng. Layth Al-Husseini (Senior AI/ML Engineer)",
    "AI_Product_Owner_Name": "Mariam Al-Khatib (AI Product Lead)",
    "AI_Governance_Lead_Name": "Dr. Rayan Al-Sulaiman (AI Governance Chair)",
    "ML_Lead_Name": "Dr. Rayan Al-Sulaiman (Lead ML Scientist)",
    "Scrum_Master_Name": "Hassan Al-Majid, CSM",
    "Agile_Coach_Name": "Rania Al-Farhan, PMI-ACP",
    "Product_Owner_Name": "Mariam Al-Khatib (Principal Product Owner)",
    "Product_Strategist_Name": "Mariam Al-Khatib (Product Strategy Lead)",
    "UX_Lead_Name": "Leena Al-Bahrani (Lead UX Architect)",
    "Dev_Lead_Name": "Eng. Walid Al-Hammad (Development Lead)",
    "Delivery_Lead_Name": "Faisal Al-Harbi, PMP",
    "Execution_Lead_Name": "Faisal Al-Harbi, PMP",
    "Work_Package_Lead_Name": "Eng. Tariq Al-Najjar",
    "Team_Lead_Name": "Eng. Walid Al-Hammad (Tech Lead)",
    "Team_Member_Name": "Sarah Al-Rashidi (Senior Functional Analyst)",
    "Team_Representative_Name": "Sarah Al-Rashidi (Team Representative)",
    "Meeting_Chair_Name": "Faisal Al-Harbi, PMP",
    "Minute_Taker_Name": "Amal Al-Obeid (PMO Coordinator)",
    "Requester_Name": "Sultan Al-Dossary (VP Operations)",
    "Lead_BA_Name": "Sarah Jenkins, CBAP",
    "Requirements_Lead_Name": "Sarah Jenkins, CBAP",
    "Resource_Manager_Name": "Sami Al-Ghamdi (Resource Management Lead)",
    "Resource_Planning_Lead_Name": "Sami Al-Ghamdi (Resource Management Lead)",
    "SME_Name": "Dr. Fahad Al-Qahtani (Subject Matter Expert - ERP)",
    "Scheduler_Name": "Ibrahim Al-Dosari, PMI-SP",
    "Steering_Chair_Name": "Dr. Muna Al-Ghamdi (Steering Committee Chair)",
    "Investment_Chair_Name": "Bader Al-Mutairi (Investment Committee Chair)",
    "CCB_Chair_Name": "Dr. Muna Al-Ghamdi (CCB Chairperson)",
    "Head_of_Strategy_Name": "Dr. Tariq Al-Mansoor (Chief Strategy Officer)",
    "Strategy_Lead_Name": "Dr. Tariq Al-Mansoor (Chief Strategy Officer)",
    "Methodology_Lead_Name": "Tariq Al-Mansoor, PfMP",
    "Organization_Unit": "Information Technology & Enterprise Operations",
    "Organization_or_Strategy_Name": "Apex 2028 Strategic Plan",
    "Planning_Period": "2026-Q1 to 2027-Q4",
    "Assessment_Cycle": "2026 Annual Audit",
    "Assessment_ID": "ASSESS-2026-01",
    "Assessor_Name": "Lead PMO Assessor",
    "Lead_Assessor_Name": "Tariq Al-Mansoor, PfMP",
    "Lead_Evaluator_Name": "Dr. Fahad Al-Qahtani",
    "Lead_Reviewer_Name": "Elena Vance, PfMP",
    "Benefit_Owner_Name": "Sultan Al-Dossary (VP Operations)",
    "Benefits_Owner_Name": "Sultan Al-Dossary (VP Operations)",
    "Benefits_Plan_ID": "BEN-2026-ERP-01",
    "Canvas_ID": "CANVAS-AI-2026-04",
    "Use_Case_ID": "UC-AI-2026-04",
    "Complexity_Model_ID": "COMPLEX-2026-ERP",
    "Framework_ID": "GOV-FRM-2026-01",
    "Governance_ID": "GOV-2026-ERP",
    "Governance_Scope": "Enterprise-Wide Cloud Migration",
    "Proposal_ID": "RFP-2026-VEND-012",
    "Study_ID": "FEAS-2026-003",
    "Vendor_Representative_Name": "Robert Vance (Apex Global Services Lead)",
    "Client_Customer_Name": "Apex Enterprise Commercial Division",
    "Client_Representative_Name": "Nasser Al-Ghamdi (Commercial Client Director)",
    "Customer_Representative_Name": "Nasser Al-Ghamdi (Commercial Client Director)",
    "Contractor_Representative_Name": "Robert Vance (Lead Contractor Project Manager)",
    "Contributor_Name": "Ahmed Al-Shehri (Senior Systems Analyst)",
    "Cycle_Period": "Sprint 14 (Q2-2026)",
    "EVM_Specialist_Name": "Ibrahim Al-Dosari, PMI-SP",
    "Issue_Owner_Name": "Eng. Walid Al-Hammad",
    "Release_Lead_Name": "Eng. Walid Al-Hammad (Release Coordinator)",
    "Technical_Evaluation_Lead_Name": "Alex Mercer (Lead Solution Architect)",
}

AR_PLACEHOLDERS = {
    "اسم_الشركة": "شركة القمة للحلول المؤسسية المتقدمة",
    "اسم_المحفظة": "محفظة التحول الرقمي وتحديث العمليات المؤسسية",
    "معرف_المحفظة": "PORT-2026-X01",
    "اسم_المحفظة_أو_البرنامج": "محفظة التحول الرقمي وتحديث العمليات المؤسسية",
    "اسم_البرنامج": "برنامج البنية التحتية السحابية والخدمات الرقمية الموحدة",
    "معرف_البرنامج": "PGM-2026-CX",
    "اسم_البرنامج_أو_المبادرة": "برنامج البنية التحتية السحابية والخدمات الرقمية الموحدة",
    "اسم_المشروع": "مشروع المنظومة السحابية الموحدة لتخطيط الموارد وسلاسل الإمداد",
    "معرف_المشروع": "PRJ-2026-ERP-01",
    "اسم_المبادرة": "مبادرة تحديث الأنظمة الأساسية والترحيل السحابي",
    "اسم_المبادرة_أو_المشروع": "مشروع المنظومة السحابية الموحدة لتخطيط الموارد وسلاسل الإمداد",
    "اسم_المنتج": "منظومة القمة الذكية Nexus لتخطيط الموارد",
    "معرف_المنتج": "PROD-NX-2026",
    "اسم_المنتج_أو_الخدمة": "منظومة القمة الذكية Nexus لتخطيط الموارد",
    "اسم_حل_الذكاء_الاصطناعي": "المساعد المعرفي الذكي لمؤسسة القمة",
    "اسم_نظام_أو_برنامج_الذكاء_الاصطناعي": "نظام الذكاء الاصطناعي المؤسسي الشامل",
    "اسم_النظام_أو_المبادرة": "المنظومة السحابية الموحدة لتخطيط الموارد",
    "التاريخ_الحالي": "2026-03-15",
    "التاريخ الحالي": "2026-03-15",
    "تاريخ_اليوم": "2026-03-15",
    "الطابع_الزمني_الحالي": "2026-03-15 10:00 بتوقيت مكة المكرمة",
    "طابع_زمني_حالي": "2026-03-15 10:00 بتوقيت مكة المكرمة",
    "وقت_الإنشاء": "2026-03-15 10:00 بتوقيت مكة المكرمة",
    "وقت الإنشاء": "2026-03-15 10:00 بتوقيت مكة المكرمة",
    "تم_الإعداد_بواسطة": "م. فيصل الحربي، PMP (مدير المشروع)",
    "المُعِد": "م. فيصل الحربي، PMP (مدير المشروع)",
    "معد_الوثيقة": "م. فيصل الحربي، PMP (مدير المشروع)",
    "اسم_المُعد": "م. فيصل الحربي، PMP (مدير المشروع)",
    "اسم_مدير_المشروع": "م. فيصل الحربي، PMP",
    "اسم_راعي_المشروع": "د. منى الغامدي (نائب الرئيس لتقنية المعلومات)",
    "اسم_الراعي_التنفيذي": "د. منى الغامدي (نائب الرئيس التنفيذي)",
    "اسم_راعي_البرنامج": "د. منى الغامدي (نائب الرئيس التنفيذي)",
    "اسم_راعي_المبادرة": "د. منى الغامدي (نائب الرئيس التنفيذي)",
    "اسم_مدير_البرنامج": "م. خالد العتيبي، PgMP",
    "اسم_مدير_المحفظة": "أ. إلينا فانس، PfMP",
    "اسم_مدير_مكتب_إدارة_المشاريع": "د. طارق المنصور، PfMP",
    "اسم_مدير_مكتب_المشاريع": "د. طارق المنصور، PfMP",
    "اسم_مسؤول_مكتب_إدارة_المشاريع": "د. طارق المنصور، PfMP",
    "اسم_مدير_المكتب": "د. طارق المنصور، PfMP",
    "اسم_مكتب_إدارة_المشاريع": "مكتب إدارة المشاريع والتحول المؤسسي (PMO)",
    "اسم_مالك_الأعمال": "أ. سلطان الدوسري (نائب الرئيس للعمليات)",
    "اسم_مالك_العمليات": "أ. سلطان الدوسري (نائب الرئيس للعمليات)",
    "اسم_قائد_العمليات": "أ. سلطان الدوسري (نائب الرئيس للعمليات)",
    "اسم_مسؤول_العمليات": "أ. سلطان الدوسري (نائب الرئيس للعمليات)",
    "اسم_كبير_المعماريين": "م. فهد السبيعي (كبير مهندسي الحلول)",
    "اسم_القائد_الفني": "م. فهد السبيعي (كبير مهندسي الحلول)",
    "اسم_القائد_الهندسي": "م. طارق النجار (القائد الهندسي)",
    "اسم_كبير_مهندسي_النظم": "م. عمر الخطيب (كبير مهندسي النظم)",
    "اسم_مدير_الجودة": "أ. نورة السيد (مدير ضمان الجودة)",
    "اسم_مسؤول_الجودة": "أ. نورة السيد (مدير ضمان الجودة)",
    "اسم_مسؤول_ضمان_الجودة": "أ. نورة السيد (مدير ضمان الجودة)",
    "اسم_المراجع_الرئيسي": "أ. نورة السيد (مدير ضمان الجودة)",
    "اسم_مدير_المخاطر": "أ. ليلى العمري، PMI-RMP",
    "اسم_محلل_المخاطر": "أ. ليلى العمري، PMI-RMP",
    "اسم_مالك_الخطر": "م. فيصل الحربي، PMP",
    "اسم_مقدر_التكاليف": "م. زيد الغامدي، CCEA",
    "اسم_المقدر_الرئيسي": "م. زيد الغامدي، CCEA",
    "اسم_المراقب_المالي": "أ. بدر المطيري (المدير المالي)",
    "اسم_مراقب_التكاليف": "أ. بدر المطيري (المدير المالي)",
    "اسم_مدير_المشتريات": "أ. منصور الشهري (مدير إدارة المشتريات)",
    "اسم_رئيس_لجنة_المناقصات": "أ. منصور الشهري (مدير إدارة المشتريات)",
    "اسم_رئيس_لجنة_العطاءات": "أ. منصور الشهري (مدير إدارة المشتريات)",
    "اسم_مدير_العقود": "أ. منصور الشهري (مدير إدارة العقود)",
    "اسم_مدير_التغيير": "د. سارة القحطاني، Prosci CCP",
    "اسم_مسؤول_التغيير": "د. سارة القحطاني، Prosci CCP",
    "اسم_مسؤول_إدارة_التغيير": "د. سارة القحطاني، Prosci CCP",
    "اسم_مسؤول_الاتصالات": "أ. هدى الهاشمي (مدير الاتصال المؤسسي)",
    "اسم_مسؤول_علاقات_المعنيين": "أ. هدى الهاشمي (مسؤول علاقات المعنيين)",
    "اسم_ممثل_المعنيين": "أ. هدى الهاشمي (مسؤول الاتصال)",
    "اسم_شريك_الموارد_البشرية": "أ. سامي الغامدي (شريك أعمال الموارد البشرية)",
    "اسم_مسؤول_الموارد_البشرية": "أ. سامي الغامدي (شريك أعمال الموارد البشرية)",
    "اسم_منسق_الموارد_البشرية": "أ. سامي الغامدي (أخصائي الموارد البشرية)",
    "اسم_منسق_التدريب": "أ. ريم الشمري (منسق التدريب والتطوير)",
    "اسم_مسؤول_الاستدامة": "م. ياسر السبيعي (مدير الاستدامة والحوكمة البيئية)",
    "اسم_مسؤول_حماية_البيانات": "أ. عبد العزيز الزهراني (مسؤول حماية البيانات)",
    "اسم_مسؤول_الخصوصية": "أ. عبد العزيز الزهراني (مسؤول حماية البيانات)",
    "اسم_مسؤول_الامتثال": "أ. عبد العزيز الزهراني (مدير الامتثال والحوكمة)",
    "اسم_المستشار_القانوني": "المستشار ماجد الفاروق (المستشار القانوني العام)",
    "اسم_مسؤول_الذكاء_الاصطناعي": "د. ريان السليمان (رئيس فريق الذكاء الاصطناعي)",
    "اسم_مهندس_الذكاء_الاصطناعي": "م. ليث الحسيني (كبير مهندسي الذكاء الاصطناعي)",
    "اسم_مسؤول_تعلم_الآلة": "د. ريان السليمان (رئيس فريق الذكاء الاصطناعي)",
    "اسم_مسؤول_الحوكمة": "د. ريان السليمان (رئيس حوكمة الذكاء الاصطناعي)",
    "اسم_مراجع_الجودة_والأخلاقيات": "د. ريان السليمان",
    "اسم_سيد_سكروم": "م. حسان الماجد، CSM",
    "اسم_الموجه_الرشيق": "أ. رانيا الفرحان، PMI-ACP",
    "اسم_مالك_المنتج": "أ. مريم الخطيب (كبير ملاك المنتجات)",
    "اسم_مسؤول_تجربة_المستخدم": "أ. لينا البحراني (كبير مصممي تجربة المستخدم)",
    "اسم_قائد_فريق_التطوير": "م. وليد الحماد (قائد فريق التطوير)",
    "اسم_قائد_التسليم": "م. فيصل الحربي، PMP",
    "اسم_مسؤول_التسليم": "م. فيصل الحربي، PMP",
    "اسم_قائد_حزمة_العمل": "م. طارق النجار (القائد الهندسي)",
    "اسم_قائد_الفريق": "م. وليد الحماد (قائد التطوير)",
    "اسم_قائد_الموقع": "م. عمر الخطيب",
    "اسم_عضو_الفريق": "أ. سارة الرشيدي (محلل نظم أعمال)",
    "اسم_ممثل_الفريق": "أ. سارة الرشيدي (محلل نظم أعمال)",
    "اسم_رئيس_الاجتماع": "م. فيصل الحربي، PMP",
    "اسم_مسجل_المحضر": "أ. أمل العبيد (أخصائي مكتب المشاريع)",
    "اسم_مقدم_الطلب": "أ. سلطان الدوسري (نائب الرئيس للعمليات)",
    "اسم_كبير_محللي_الأعمال": "أ. سارة القحطاني، CBAP",
    "اسم_كبير_المحللين": "أ. سارة القحطاني، CBAP",
    "اسم_محلل_الأعمال_الرئيسي": "أ. سارة القحطاني، CBAP",
    "اسم_مسؤول_المتطلبات": "أ. سارة القحطاني، CBAP",
    "اسم_مدير_الموارد": "أ. سامي الغامدي (مدير الموارد البشرية)",
    "اسم_مسؤول_تخطيط_الموارد": "أ. سامي الغامدي (مسؤول تخطيط الموارد)",
    "اسم_الخبير_المختص": "د. فهد القحطاني (خبير استشاري - تخطيط الموارد)",
    "اسم_مسؤول_الجدولة": "م. إبراهيم الدوسري، PMI-SP",
    "اسم_رئيس_لجنة_التوجيه": "د. منى الغامدي (رئيس لجنة التوجيه)",
    "اسم_رئيس_لجنة_الاستثمار": "أ. بدر المطيري (رئيس لجنة الاستثمار)",
    "اسم_رئيس_لجنة_التغيير": "د. منى الغامدي (رئيس لجنة ضبط التغيير)",
    "اسم_رئيس_الاستراتيجية": "د. طارق المنصور (رئيس قطاع الاستراتيجية)",
    "اسم_مسؤول_الاستراتيجية": "د. طارق المنصور (رئيس قطاع الاستراتيجية)",
    "اسم_رئيس_التقنية": "د. منى الغامدي (نائب الرئيس لتقنية المعلومات)",
    "اسم_مسؤول_المنهجية": "د. طارق المنصور، PfMP",
    "الوحدة_التنظيمية": "قطاع تقنية المعلومات والعمليات المؤسسية",
    "اسم_الخطة_الاستراتيجية": "الخطة الاستراتيجية للتحول والريادة 2028",
    "فترة_التخطيط": "من الربع الأول 2026 إلى الربع الرابع 2027",
    "دورة_التقييم": "دورة التدقيق السنوية 2026",
    "معرف_التقييم": "ASSESS-2026-01",
    "اسم_المقيّم": "كبير مدققي مكتب المشاريع",
    "اسم_المقيّم_الرئيسي": "د. طارق المنصور، PfMP",
    "اسم_المقيم_الرئيسي": "د. طارق المنصور، PfMP",
    "كبير_المدققين": "أ. عادل المطيري، CIA",
    "اسم_كبير_المدققين": "أ. عادل المطيري، CIA",
    "اسم_مالك_المنافع": "أ. سلطان الدوسري (نائب الرئيس للعمليات)",
    "اسم_مالك_الفوائد": "أ. سلطان الدوسري (نائب الرئيس للعمليات)",
    "معرف_خطة_المنافع": "BEN-2026-ERP-01",
    "معرف_حالة_الاستخدام": "UC-AI-2026-04",
    "معرف_النموذج": "CANVAS-AI-2026-04",
    "معرف_نموذج_التعقيد": "COMPLEX-2026-ERP",
    "معرف_إطار_العمل": "GOV-FRM-2026-01",
    "معرف_الحوكمة": "GOV-2026-ERP",
    "نطاق_الحوكمة": "التحول السحابي الشامل لكافة فروع وإدارات المؤسسة",
    "معرف_المقترح": "RFP-2026-VEND-012",
    "معرف_الدراسة": "FEAS-2026-003",
    "اسم_ممثل_المورد": "أ. روبرت فانس (مدير خدمات المورد المعتمد)",
    "اسم_العميل": "قطاع العمليات التجارية والمبيعات بشركة القمة",
    "اسم_ممثل_العميل": "أ. ناصر الغامدي (مدير قطاع العملاء)",
    "اسم_ممثل_المقاول": "أ. روبرت فانس (مدير المشروع لدى المقاول)",
    "فترة_الدورة": "السبرنت 14 (الربع الثاني 2026)",
    "اسم_أخصائي_القيمة_المكتسبة": "م. إبراهيم الدوسري، PMI-SP",
    "اسم_مالك_المشكلة": "م. وليد الحماد (قائد التطوير)",
    "اسم_مالك_الإجراء": "م. فيصل الحربي، PMP",
    "اسم_مسؤول_الإصدارات": "م. وليد الحماد (منسق الإصدارات)",
    "اسم_مسؤول_التقييم_الفني": "م. فهد السبيعي (كبير مهندسي الحلول)",
}

# Exhaustive dictionary for bold field names (**Key:** [ Placeholder ])
AR_FIELD_VALUES = {
    # Portfolio & Program Roadmap / Charters / Strategy
    "غرض المحفظة ونطاقها": "قيادة التحول الرقمي الشامل، تحديث البنية التقنية، وأتمتة سلاسل الإمداد والعمليات التشغيلية لشركة القمة عبر كافة الفروع ومراكز التوزيع.",
    "فترة التخطيط": "2026 - 2028 (خطة ثلاثية متجددة)",
    "أفق الخارطة": "24 شهراً مع مراجعة ربع سنوية لأولويات المبادرات",
    "مالك المحفظة": "أ. إلينا فانس، PfMP (مدير المحفظة والتحول المؤسسي)",
    "دورة التخطيط": "دورة التخطيط الاستراتيجي السنوية (تحديث ربع سنوي)",
    "نسخة الخارطة وحالتها": "الإصدار 2.0 (معتمد من لجنة التوجيه الاستراتيجي في 15 مارس 2026)",
    "غرض البرنامج": "تحديث البنية التحتية والأنظمة المؤسسية وتوحيد قنوات الخدمات الرقمية.",
    "نطاق البرنامج": "يشمل كافة الأنظمة الأساسية، الترحيل السحابي، وبوابات الخدمات المتكاملة.",
    "مبرر البرنامج": "خفض التكاليف التشغيلية بنسبة 35% ورفع كفاءة الخدمات بنسبة 50%.",
    "الرؤية الاستراتيجية": "الريادة المؤسسية في تقديم خدمات رقمية سحابية موحدة وموثوقة بحلول 2028.",
    "الجهة الطالبة": "قطاع العمليات التجارية وسلاسل الإمداد",
    "حالة الوثيقة": "معتمدة ونافذة",
    "المرجع": "PMO-REF-2026-01",
    "النوع": "هيكل شجري وظيفي ومكاني",
    "التسمية": "تصنيف خماسي المستويات يشمل الكوادر، المعدات، البرمجيات، والبيئات السحابية.",

    # AI Model Card, Canvas, Ethics & Readiness
    "اسم النموذج وإصداره": "نموذج المساعد المعرفي الذكي لمؤسسة القمة (AECA Engine v2.4)",
    "المطوّر ومصدر النموذج": "فريق الذكاء الاصطناعي وهندسة البيانات بشركة القمة بالتعاون مع المطور السحابي المعتمد",
    "البنية والإعداد": "بنية Transformer مدعومة بطبقة استرجاع معزز (RAG) وقاعدة بيانات متجهية مدمجة",
    "أسلوب التدريب والحوسبة": "ضبط دقيق موجه (Supervised Fine-Tuning) على عنقود حوسبة سحابي مؤمن (8x H100 GPUs)",
    "الترخيص وشروط الاستعمال": "ترخيص مؤسسي داخلي خاص بشركة القمة للحلول المؤسسية المتقدمة",
    "المخرجات المرتبطة": "مستودع النماذج السحابي الآمن (Model Registry Artifacts v2.4)",
    "الاستخدام الرئيس": "أتمتة مطابقة أوامر الشراء، استخلاص بيانات الفواتير، والتنبؤ باحتياجات المخزون",
    "الاستخدام الثانوي": "توليد ملخصات الأداء التشغيلي ومسودات تقارير التدقيق لإدارة العمليات",
    "الاستخدام غير المشمول": "اتخاذ قرارات التوظيف وفصل الموظفين، أو اعتماد التحويلات المالية الكبرى دون توقيع بشري",
    "المستخدم والجمهور": "مدراء العمليات، محللو سلاسل الإمداد، موظفو المشتريات، ومدققو الحسابات بشركة القمة",
    "شروط التشغيل": "بيئة سحابية خاصة مع توفر اتصال شبكي آمن وزمن استجابة < 800 ميلي ثانية",
    "نمط الذكاء الاصطناعي": "نموذج لغوي كبير مدعوم بالتوليد المعزز بالاسترجاع (RAG) لتحليل البيانات المؤسسية",
    "نظام الذكاء الاصطناعي": "منظومة المساعد المعرفي الذكي لمؤسسة القمة (AECA v2.4 Platform)",
    "الاستخدام المعتمد": "أتمتة مطابقة فواتير المشتريات، التنبؤ بالطلب على المخزون، وتوليد التقارير التشغيلية اليومية",
    "معالجة غير مشمولة": "القرارات التأديبية، التقييم الائتماني المباشر للعملاء، وتخزين البيانات غير المصنفة",
    "متطلب الإشراف البشري": "مراجعة بشرية إلزامية لكافة المعاملات المالية التي تتجاوز 50,000 ريال، أو في حال كانت درجة ثقة النموذج أقل من 90%",
    "نقاط الإشراف البشري": "عند اعتماد طلبات الشراء الكبرى، استثناءات المخزون، ونشر التحديثات البرمجية للإنتاج",
    "كلفة عدم الفعل": "خسائر تشغيلية سنوية تقدر بـ 4.2 مليون ريال نتيجة استمرار المعالجة اليدوية وبطء دورة التوريد",
    "لماذا الآن": "انتهاء الدعم الفني للأنظمة القديمة وبدء تطبيق المعايير التنظيمية الإلزامية في الربع القادم",
    "ما الذي يحاول إنجازه": "تقليص زمن معالجة أوامر الشراء بنسبة 40%، وخفض أخطاء إدخال البيانات إلى أقل من 0.1%",
    "من يتأثر بها": "450 موظفاً في قطاعات العمليات، المالية، المشتريات، وإدارة المستودعات",
    "بيان المشكلة": "تشتت البيانات عبر أنظمة قديمة معزولة يؤدي إلى بطء معالجة الطلبات وارتفاع تكاليف التشغيل",
    "وصف الحل": "نشر منظومة سحابية متكاملة مدعومة بمحرك ذكاء اصطناعي لمعالجة البيانات والربط اللحظي بين الفروع",
    "بيانات التدريب": "مجموعة بيانات تاريخية منتقاة ومغفلة الهوية تغطي 5 سنوات من عمليات الشراء والتوريد المؤسسي",
    "العدالة والتحيز": "فحص دوري للبيانات لضمان عدم وجود تحيز ضد أي مورد أو منطقة جغرافية وفق ضوابط الحوكمة",
    "حقوق الأفراد": "تشفير كامل للبيانات الشخصية والامتثال التام لنظام حماية البيانات الشخصية واللوائح التنظيمية",
    "القيود المعروفة": "تقتصر على معالجة المستندات الرقمية والفواتير الواضحة بدقة >= 300 DPI بالريال والدولار.",
    "السلوك خارج نطاق التوزيع": "تفعيل التراجع الآمن وتوجيه المعاملات غير المألوفة إلى طابور المراجعة البشرية فوراً.",
    "المراقبة في الإنتاج": "مراقبة لحظية لمؤشرات الأداء، زمن الاستجابة، ونسبة الدقة عبر لوحة Grafana سحابية.",
    "عتبات المراقبة": "تنبيه فوري عند انخفاض الدقة اليومية عن 90% أو تجاوز زمن الاستجابة 800ms.",
    "سياسة إعادة التدريب والتحديث": "إعادة ضبط وتدريب ربع سنوية باستخدام البيانات المعتمدة بعد اجتياز اختبارات الانحدار.",
    "سجل تغييرات الإصدار": "الإصدار 2.4: تحسين دقة استخلاص الفواتير متعددة الصفحات بنسبة 12% وضبط طبقة RAG.",
    "خطة الإحالة للتقاعد": "الاحتفاظ بالنموذج السابق كخطة طوارئ بديلة (Fallback) لمدة 6 أشهر قبل الأرشفة الآمنة.",

    # Strategy, Benefits & Business Case
    "الوضع الحالي": "أنظمة قديمة معزولة تتطلب إدخال البيانات يدوياً مع بطء معالجة طلبات التوريد.",
    "الوضع المستقبلي دون المشروع": "تراكم الأخطاء التشغيلية، ارتفاع تكاليف الصيانة بنسبة 25%، ومخاطر عدم الامتثال الضريبي.",
    "بيان الحاجة": "الحاجة الملحة لتوحيد وأتمتة العمليات المالية وسلاسل الإمداد عبر منصة سحابية موحدة.",
    "بيان رؤية البرنامج": "الوصول إلى منظومة مؤسسية ذكية ومؤتمتة بالكامل تحقق أعلى معايير الكفاءة بحلول 2028.",
    "بيان صلاحية مدير البرنامج": "صلاحية إدارة وتوجيه كافة مسارات البرنامج، اعتماد المخرجات المرحلية، وتخصيص الموارد حتى 500,000 ريال.",
    "بيانات الفوائد": "تحقيق وفر مالي سنوي قدره 4.2 مليون ريال وتقليص دورة معالجة الطلبات بنسبة 40%.",
    "فئات الفوائد": "وفورات مالية مباشرة، كفاءة تشغيلية، تحسين رضا المستفيدين، وضمان الامتثال التنظيمي.",
    "مالكو الفوائد": "نائب الرئيس للعمليات، المدير المالي، ومدير المشتريات وسلاسل الإمداد.",
    "مخاطر الفوائد": "مقاومة التغيير من المستخدمين وتأخر تكامل واجهات الأنظمة الخارجية.",
    "قواعد حالة الفوائد": "مخططة -> قيد التحقق -> محققة جزئياً -> محققة بالكامل ومستدامة تشغيلياً.",
    "قيم خط الأساس": "زمن دورة الطلب: 12 يوماً؛ نسبة الأخطاء: 4.8%؛ التكلفة التشغيلية: 14.5 مليون ريال سنوياً.",
    "كلفة التطوير": "5,200,000 ريال سعودي موزعة على خدمات الاستشارات والهندسة والتهيئة.",
    "كلفة التشغيل": "1,200,000 ريال سعودي سنوياً لاشتراكات السحابة والدعم الفني المتقدم.",
    "المسار الموصى به": "الاعتماد الكامل على الحل السحابي الموحد (Nexus ERP) مع تكامل تدريجي عبر 3 مراحل.",
    "تقييم الجدوى": "جدوى فنية واقتصادية عالية بمعدل عائد داخلي (IRR) يبلغ 28% وفترة استرداد 2.2 سنة.",

    # Agile, Sprint Planning, Story Mapping, Flow
    "هدف دورة تطوير": "إنجاز وتكامل وحدة الفوترة السحابية الآلية واجتياز اختبارات قبول المستخدمين للدفعة الأولى.",
    "مدة دورة تطوير": "أسبوعان (سبرنت يبدأ من الأحد 2026-04-05 حتى الخميس 2026-04-16).",
    "نتيجة الإصدار الأول": "إطلاق النسخة التجريبية (MVP) في 3 فروع رئيسية للتحقق من كفاءة الأداء واستقرار النظام.",
    "مرشّحو الإصدارات اللاحقة": "تطبيق الجوال للخدمات الذاتية، تكامل بوابات الدفع الدولية، والتحليلات التنبؤية المتقدمة.",
    "الهيكل الرئيسي": "مسار التدفق الرأسي للعملية: من إنشاء طلب الشراء، اعتماد المدير، مطابقة المخزون، والفوترة السحابية.",
    "محددات تدفق القيمة": "الحد الأقصى للعمل قيد التنفيذ (WIP Limit) = 4 مهام لكل مهندس في المرحلة الواحدة.",
    "المنقول من دورة تطوير السابقة": "مهمتان فرعيتان لتحسين واجهة المستخدم واختبار استجابة بوابات الربط البرمجي.",
    "الهيكل العظمي الدقيق": "المسار الرأسي الأدنى المكتمل: إنشاء طلب الشراء -> موافقة النظام -> إصدار الفاتورة السحابية.",
    "حدود النطاق": "المقرات الرئيسية والفروع ومراكز التوزيع؛ يستثنى نقاط البيع الطرفية القديمة.",
    "خارج النطاق صراحةً": "شراء خوادم داخلية محلية وصيانة البرمجيات القديمة خارج فترة الانتقال.",

    # Governance, Security, Privacy & Reporting
    "ضوابط الوصول وأدنى امتياز": "صلاحيات قائمة على الأدوار (RBAC) مع تحقق ثنائي (MFA) وتسجيل كامل للعمليات.",
    "تسجيل الموافقة وإثباتها": "سجل إلكتروني مشفر وموثق بالطابع الزمني لكل موافقة أو تعديل على البيانات الشخصية.",
    "تدفّق البيانات والمستلمون": "تدفق مشفر (TLS 1.3) داخل الشبكة الافتراضية الخاصة للشركة دون مشاركة مع أطراف ثالثة.",
    "النقول عبر الحدود": "تخزين ومعالجة البيانات بالكامل داخل مراكز البيانات السحابية المحلية المعتمدة داخل المملكة.",
    "حقوق القرار والإنصاف": "حق المستخدم في طلب مراجعة بشرية لأي قرار مؤتمت مع معالجة الشكاوى خلال 5 أيام عمل.",
    "فحص الامتثال": "اجتياز كامل الفحوصات الدورية لضوابط الأمن السيبراني وحماية البيانات بنسبة 100%.",
    "جمهور البلاغ": "الراعي التنفيذي، لجنة التوجيه، مدراء القطاعات التشغيلية، ومكتب إدارة المشاريع (PMO).",
    "فترة البلاغ": "تقرير دوري يغطي النصف الأول من شهر مارس 2026 (دورة نصف شهرية).",
    "المقيِّم والتاريخ": "د. طارق المنصور، PfMP (رئيس فريق التدقيق والتقييم) - 2026-03-15",
    "المستندات المصدر": "ميثاق المشروع، دراسة الجدوى، خطة إدارة النطاق، والمواصفات المعمارية المعتمدة.",

    # Cost, EVM, Schedule & Resource
    "الميزانية عند الاكتمال": "12,500,000 ريال سعودي (تشمل 10% احتياطي طوارئ إداري).",
    "قواعد قياس الأداء": "طريقة القيمة المكتسبة المنفذة الفعلية (0/100 للمهام القصيرة، ونسبة الإنجاز المعتمدة للمهام الكبرى).",
    "عتبات انحراف التكلفة": "أي انحراف في مؤشر أداء التكلفة CPI يتجاوز ±5% يستوجب رفع تقرير تحليلي وتصحيحي خلال 48 ساعة.",
    "عتبات انحراف الجدول": "أي تأخير في مؤشر أداء الجدول SPI يقل عن 0.95 يتطلب تفعيل خطة استدراك المسار الحرج.",
    "وحدة قياس السعة": "ساعات العمل الفعلية للموظف المكافئ (FTE Hours) بمتوسط 160 ساعة شهرياً.",
    "وضع التمويل": "تمويل معتمد بالكامل من الميزانية الرأسمالية (CAPEX) للعام المالي 2026-2027.",
    "مالك الخطر والاستجابة": "م. فيصل الحربي، PMP (مدير المشروع) بالتعاون مع أ. ليلى العمري (مدير المخاطر).",
    "مسار التصعيد": "المشرف المباشر -> مدير المشروع -> رئيس مكتب إدارة المشاريع (PMO) -> لجنة التوجيه التنفيذية.",
    "محفزات إعادة التقييم": "حدوث تغيير جوهري في النطاق، انحراف في الميزانية يتجاوز 10%، أو تغيير في التشريعات والأنظمة.",
    "معايير الإيقاف": "تجاوز التكاليف للحد الأقصى المعتمد بنسبة 20% دون جدوى واضحة، أو فشل معايير الأمان السيبراني الحرجة.",
    "منهج قياس القيمة": "احتساب صافي القيمة الحالية (NPV)، فترة استرداد رأس المال (Payback Period)، ومعدل العائد الداخلي (IRR).",
    "معايير التقييم": "الجدارة الفنية (60%)، التكلفة والجدوى المالية (30%)، وخبرة المورد والامتثال (10%).",
    "الميثاق ونطاق العمل": "وثيقة ميثاق متكاملة تشمل الأهداف، المعالم، الميزانية، ومستويات الصلاحيات المعتمدة.",
}

EN_FIELD_VALUES = {
    # Portfolio & Program Roadmap / Charters / Strategy
    "portfolio purpose and scope": "Drive comprehensive enterprise digital transformation, cloud modernization, and operational supply chain automation across all business units.",
    "planning period": "2026 - 2028 (Rolling 3-Year Strategic Cycle)",
    "roadmap horizon": "24-Month Active Execution Horizon with Quarterly Reprioritization",
    "portfolio owner": "Elena Vance, PfMP (Portfolio & Enterprise Transformation Director)",
    "planning cycle": "Annual Strategic Planning Cycle (Quarterly Rolling Review)",
    "roadmap status and version": "Version 2.0 (Approved by Strategic Steering Committee on March 15, 2026)",
    "program purpose": "Modernize core IT infrastructure, consolidate platforms, and standardize digital services.",
    "program scope": "Encompasses enterprise core systems, cloud migration, and secure API gateways.",
    "program justification": "Reduce recurring operational costs by 35% and improve service throughput by 50%.",
    "strategic vision": "Achieve industry leadership in agile, resilient, and unified enterprise cloud operations by 2028.",
    "requesting department": "Commercial Operations & Supply Chain Division",
    "document status": "Approved & Baselined",
    "reference": "PMO-REF-2026-01",
    "chart form": "Functional & Infrastructure Tree View",
    "node labels": "5-tier classification covering Personnel, Compute, Licensing, Storage, and Environments.",

    # AI Model Card, Canvas, Ethics & Readiness
    "model name and version": "Apex Enterprise Cognitive Assistant Engine (AECA Engine v2.4)",
    "developer and provenance": "Apex Global Solutions AI & Data Engineering Squad in partnership with Certified Cloud Partner",
    "architecture and configuration": "Transformer architecture augmented with Vector Retrieval (RAG) and private vector embeddings",
    "training method and compute": "Supervised Fine-Tuning (SFT) & DPO hosted on secured private cloud GPU clusters (8x H100)",
    "licence and usage terms": "Proprietary Enterprise Commercial License restricted to Apex Global Solutions internal operations",
    "related artefacts": "Secured Cloud Model Registry Artifacts (v2.4 Production Baseline)",
    "primary use": "Automated procurement purchase order matching, invoice data parsing, and predictive replenishment",
    "secondary use": "Operational synthesis reporting and preliminary compliance audit logs for operations management",
    "out-of-scope use": "Autonomous HR hiring/termination decisions, customer credit scoring, or unsupervised fund disbursements",
    "user and audience": "Operations directors, supply chain analysts, procurement specialists, and financial auditors",
    "operating conditions": "Secured enterprise virtual private cloud (VPC) with latency SLA < 800ms and 99.95% uptime",
    "ai pattern": "Retrieval-Augmented Generation (RAG) Large Language Model Pipeline over Enterprise Data",
    "ai system inventory": "Apex Enterprise Cognitive Assistant System (AECA v2.4 Platform)",
    "approved use cases": "Automated vendor invoice matching, demand forecasting, and daily operational synthesis reporting",
    "human oversight requirement": "Mandatory human-in-the-loop review for all financial transactions exceeding $15,000 USD or model confidence < 90%",
    "human oversight points": "Requisition approvals, major inventory adjustments, and production deployment sign-offs",
    "cost of inaction": "Projected annual operational loss of $1.15M USD due to legacy manual latency and error overhead",
    "why now": "Upcoming end-of-life for legacy on-prem platforms and mandatory Q3 regulatory cloud compliance cutoffs",
    "what they are trying to do": "Reduce purchase order cycle time by 40% and eliminate data entry reconciliation errors to < 0.1%",
    "affected population": "450 enterprise business users across supply chain, accounting, procurement, and warehouse logistics",
    "problem statement": "Fragmented data silos across legacy on-prem systems causing 40% longer order cycle times and elevated operational overhead",
    "solution description": "Deploy a scalable cloud ERP platform powered by an intelligent cognitive assistance pipeline for automated real-time operations",
    "ethical principles": "Strict algorithmic fairness, zero demographic bias, complete auditability, and role-based access governance",
    "privacy notices and just-in-time disclosure": "End-to-end data encryption at rest and in transit adhering strictly to enterprise data privacy regulations",
    "known limitations": "Restricted to digital documents and invoices with minimum 300 DPI resolution in USD and SAR.",
    "out-of-distribution behaviour": "Automatic safe fallback routing out-of-distribution inputs directly to human verification queues.",
    "production monitoring": "Real-time telemetry tracking inference latency, accuracy rates, and error anomalies via Grafana dashboards.",
    "monitoring thresholds": "Instant automated alerts triggered if daily accuracy drops below 90% or p95 latency exceeds 800ms.",
    "retraining and update policy": "Quarterly scheduled retraining on curated new operational datasets subject to regression gate verification.",
    "version change record": "Version 2.4: Enhanced multi-page invoice entity extraction accuracy by 12% and optimized RAG embedding layer.",
    "decommissioning plan": "Maintain previous model release in warm standby for 6 months prior to permanent secure archival.",

    # Strategy, Benefits & Business Case
    "current state": "Fragmented legacy on-prem systems requiring manual data entry and elongated procurement cycle times.",
    "future state without the project": "Accumulating operational errors, 25% escalation in legacy maintenance costs, and regulatory compliance exposure.",
    "need statement": "Critical business imperative to modernize and automate supply chain and financial workflows onto a unified cloud platform.",
    "program vision statement": "Establish an intelligent, fully automated enterprise operations ecosystem achieving global best practices by 2028.",
    "program manager authority statement": "Full authority to direct program tracks, approve interim deliverables, and allocate resources up to $150,000 USD.",
    "benefit statements": "Realize $1.15M USD in recurring annual savings and reduce order turnaround cycle times by 40%.",
    "benefit categories": "Direct financial savings, operational velocity, stakeholder satisfaction, and regulatory compliance assurance.",
    "benefit owners": "VP of Operations, Chief Financial Officer, and Head of Strategic Sourcing.",
    "benefit risks": "User change resistance and potential schedule lag in legacy API integration adapters.",
    "benefit status rules": "Planned -> In Realization -> Partially Realized -> Fully Realized & Sustained.",
    "baseline values": "Order cycle: 12 business days; manual error rate: 4.8%; annual legacy operating cost: $4.2M USD.",
    "build cost": "$1,450,000 USD allocated for engineering services, software integration, and configuration.",
    "operating cost": "$350,000 USD annually for cloud hosting subscriptions and Tier-3 managed support.",
    "recommended route": "Full migration to cloud-native unified ERP platform executed across 3 structured rollout waves.",
    "feasibility assessment": "High technical and financial feasibility featuring 28% Internal Rate of Return and 2.2-year payback period.",

    # Agile, Sprint Planning, Story Mapping, Flow
    "sprint goal": "Deliver and integrate the automated cloud e-invoicing module and validate initial batch user acceptance testing.",
    "sprint window": "2-Week Sprint Cycle (Starting Sunday April 5, 2026 through Thursday April 16, 2026).",
    "outcome of the first release": "Pilot rollout (MVP) deployed across 3 regional distribution hubs for performance validation.",
    "later release candidates": "Mobile self-service portal, international payment gateway integrations, and predictive analytics engine.",
    "walking skeleton": "Minimal end-to-end functional thread: Requisition creation, manager approval, and cloud invoice generation.",
    "mvp boundary": "Core procurement, inventory ledger, and financial billing integration.",
    "carry-over from the previous sprint": "Two minor sub-tasks for UI styling polish and API edge-case integration test scripts.",
    "scope boundary": "Enterprise headquarters, regional offices, and distribution centers; excludes retail kiosks.",
    "explicitly out of scope": "On-premise hardware procurement and legacy codebase maintenance beyond cutover window.",

    # Governance, Security, Privacy & Reporting
    "access controls and least privilege": "Role-Based Access Control (RBAC) enforced with Multi-Factor Authentication and audit logging.",
    "consent recording and evidence": "Cryptographically signed, timestamped audit log of all user consent grants and revocations.",
    "data flow and recipients": "Encrypted data transit (TLS 1.3) contained within private cloud VPC with zero unapproved third-party exposure.",
    "cross-border transfers": "All sensitive data residency strictly maintained within authorized in-country sovereign cloud regions.",
    "decision rights and redress": "User entitlement to request human review on automated outputs, with dispute resolution SLA < 5 business days.",
    "compliance check": "100% pass score on enterprise cybersecurity baseline and regulatory data privacy compliance audits.",
    "reporting audience": "Executive Sponsor, Steering Board, Business Operations Directors, and PMO Leadership.",
    "reporting period": "Bi-weekly operational progress reporting cycle covering First Half of March 2026.",
    "assessor and date": "Tariq Al-Mansoor, PfMP (Lead PMO Assessor) - 2026-03-15",
    "source documents": "Project Charter, Business Case, Scope Management Plan, and Solution Architecture Blueprint.",

    # Cost, EVM, Schedule & Resource
    "budget at completion (bac)": "$3,500,000 USD (including 10% management contingency reserve).",
    "measurement method": "Earned Value Management (EVM) using discrete work package milestones (0/100 and percent-complete rules).",
    "monitoring thresholds": "Variance threshold of ±5% on CPI or SPI triggers mandatory corrective action plan within 48 hours.",
    "capacity unit of measure": "Full-Time Equivalent (FTE) Billable Work Hours, benchmarked at 160 hours per month per engineer.",
    "funding position": "Fully funded and pre-approved under FY2026-2027 Capital Expenditure (CAPEX) budget.",
    "risk owner and response": "Faisal Al-Harbi, PMP (Project Manager) in coordination with Layla Al-Omari (Risk Manager).",
    "escalation path": "Squad Lead -> Project Manager -> PMO Director -> Executive Steering Committee.",
    "reassessment triggers": "Scope baseline shift > 10%, schedule slip > 2 weeks, or regulatory framework modifications.",
    "kill criteria": "Budget overrun exceeding 20% without verified ROI, or unresolved critical security/privacy violations.",
    "value measurement method": "Net Present Value (NPV), Payback Period, and Internal Rate of Return (IRR) quarterly tracking.",
    "evaluation criteria": "Technical Capability (60%), Financial/Commercial Viability (30%), and Vendor Track Record (10%).",
}

def clean_template_comments(text: str) -> str:
    """Removes instructional top HTML comments while preserving document structure."""
    text = re.sub(r'^\s*<!--[\s\S]*?-->\s*', '', text)
    text = re.sub(r'<!--\s*(?:LLM|Writing guidance|Tailoring|What the|Record|The intent|Alignment|Where|How|تعليمات|إرشادات)[\s\S]*?-->', '', text)
    return text.strip()

def replace_all_placeholders(text: str, is_arabic: bool = False) -> str:
    """Replaces {{...}} placeholders with realistic fictional values."""
    mapping = AR_PLACEHOLDERS if is_arabic else EN_PLACEHOLDERS
    
    def repl(match):
        key = match.group(1).strip()
        if key in mapping:
            return mapping[key]
        if is_arabic:
            return f"معتمد - {key}"
        return f"Approved - {key.replace('_', ' ')}"

    return re.sub(r'\{\{([^}]+)\}\}', repl, text)

def is_table_divider(line: str) -> bool:
    s = line.strip()
    if not (s.startswith('|') and s.endswith('|')):
        return False
    cells = [c.strip() for c in s.split('|')[1:-1]]
    return len(cells) > 0 and all(c.replace(':', '').replace('-', '') == '' and len(c) >= 3 for c in cells)

def get_field_value(field_name: str, is_arabic: bool) -> str:
    """Returns accurate, domain-specific field value for **Field:** [ Placeholder ]"""
    f_clean = field_name.strip().replace('*', '').replace(':', '').strip()
    f_lower = f_clean.lower()
    
    if is_arabic:
        for k, v in AR_FIELD_VALUES.items():
            if k in f_clean or f_clean in k:
                return v
        
        # High-Fidelity Categorical Fallbacks
        if any(k in f_lower for k in ['ذكاء', 'نموذج', 'خوارزم', 'بيانات التدريب', 'تعلم', 'مطور', 'بنية', 'ترخيص']):
            return "نموذج سحابي متقدم مدرب على بيانات المؤسسة ومصرح للاستخدام الداخلي وفق معايير الأمان."
        if any(k in f_lower for k in ['أخلاق', 'تحيز', 'عدالة', 'حقوق', 'خصوصية', 'حماية', 'موافقة']):
            return "الامتثال التام للوائح حماية البيانات الشخصية والأطر الأخلاقية المؤسسية لمنع التحيز وضمان الشفافية."
        if any(k in f_lower for k in ['إشراف', 'بشري', 'صلاحية', 'حوكمة', 'اعتماد']):
            return "مراجعة واعتماد بشري إلزامي من قِبل مدراء القطاعات المعنية لكافة العمليات الاستثنائية وذات الأثر المالي."
        if any(k in f_lower for k in ['سبرنت', 'أسبوع', 'إصدار', 'قصة', 'تدفق', 'رشيق', 'عائق']):
            return "دورة عمل رشيقة مدتها أسبوعان تركز على إنجاز حزم العمل ذات الأولوية القصوى واجتياز اختبارات القبول."
        if any(k in f_lower for k in ['تكلفة', 'ميزانية', 'قيمة مكتسبة', 'تمويل', 'مالي', 'انحراف التكلفة']):
            return "إدارة ومتابعة المصروفات وفق خط الأساس للتكلفة المعتمد مع تطبيق قواعد القيمة المكتسبة (EVM)."
        if any(k in f_lower for k in ['خطر', 'مشكلة', 'تصعيد', 'انحراف', 'إنذار', 'عتبة']):
            return "مراقبة مستمرة للمؤشرات التشغيلية ورفع تقارير دورية مع تفعيل خطط الاستجابة الفورية عند تجاوز العتبات."
        if any(k in f_lower for k in ['مشتريات', 'عقد', 'مورد', 'مناقصة', 'ترسية', 'sow']):
            return "متابعة أداء المورد وفق مؤشرات الجودة ومطابقة التسليمات لشروط وثيقة نطاق العمل (SOW)."
        if any(k in f_lower for k in ['نطاق', 'غرض', 'هدف', 'مبرر', 'رؤية']):
            return "تحقيق التميز التشغيلي وأتمتة العمليات والربط السحابي الموحد وفق أعلى المعايير القياسية."
        if any(k in f_lower for k in ['فترة', 'تاريخ', 'دورة', 'أفق', 'جدول']):
            return "2026-Q1 إلى 2027-Q4 (دورة سنوية مع مراجعة ربع سنوية)"
        if any(k in f_lower for k in ['مالك', 'مسؤول', 'مدير', 'راعي', 'معد']):
            return "أ. إلينا فانس، PfMP (مدير المحفظة والتحول المؤسسي)"
        if any(k in f_lower for k in ['نسخة', 'حالة', 'وضع', 'مرجع']):
            return "الإصدار 1.0 (معتمد رسمياً)"
        return "تم تحديده وتوثيقه بالتفصيل ليتوافق مع أهداف المشروع والمتطلبات التشغيلية لشركة القمة."
    else:
        for k, v in EN_FIELD_VALUES.items():
            if k in f_lower or f_lower in k:
                return v
        
        # High-Fidelity Categorical Fallbacks
        if any(k in f_lower for k in ['ai', 'model', 'data', 'training', 'algorithm', 'developer', 'architecture', 'licence']):
            return "Enterprise cloud-hosted ML pipeline trained on historical operations and authorized for internal use."
        if any(k in f_lower for k in ['ethics', 'bias', 'fairness', 'privacy', 'rights', 'consent']):
            return "Full adherence to enterprise data privacy regulations, bias prevention protocols, and transparent audit trails."
        if any(k in f_lower for k in ['human', 'oversight', 'authority', 'governance', 'approval']):
            return "Mandatory human-in-the-loop review by business division leads for all exceptional and high-impact operations."
        if any(k in f_lower for k in ['sprint', 'release', 'agile', 'story', 'flow', 'wip', 'impediment']):
            return "Two-week agile delivery sprint focusing on high-priority backlog items and acceptance criteria verification."
        if any(k in f_lower for k in ['cost', 'budget', 'evm', 'funding', 'financial', 'earned value']):
            return "Continuous financial tracking against the approved cost baseline utilizing Earned Value Management (EVM)."
        if any(k in f_lower for k in ['risk', 'issue', 'escalation', 'variance', 'trigger', 'threshold']):
            return "Active operational monitoring with rapid response workflows triggered upon threshold deviations."
        if any(k in f_lower for k in ['procurement', 'contract', 'vendor', 'sow', 'rfp']):
            return "Rigorous vendor performance monitoring against agreed SOW milestones and SLA quality scorecards."
        if any(k in f_lower for k in ['scope', 'purpose', 'objective', 'justification', 'vision']):
            return "Deliver operational excellence, process automation, and unified cloud integration adhering to enterprise standards."
        if any(k in f_lower for k in ['period', 'date', 'cycle', 'horizon', 'schedule']):
            return "2026-Q1 through 2027-Q4 (Annual cycle with quarterly governance refresh)"
        if any(k in f_lower for k in ['owner', 'lead', 'manager', 'sponsor', 'author']):
            return "Elena Vance, PfMP (Portfolio Transformation Director)"
        if any(k in f_lower for k in ['version', 'status', 'state', 'ref']):
            return "Version 1.0 (Formally Approved)"
        return "Fully defined and aligned with Apex Global Solutions operational baseline and project objectives."

def fill_table_cell(cell_val: str, row_label: str, col_header: str, sec_name: str, table_row_idx: int, is_arabic: bool) -> str:
    """Intelligently fills a specific cell in a table, preserving fixed labels and matching row/col context."""
    c = cell_val.strip()
    if not ('[ Add' in c or '[ أضف' in c or '[ ....' in c or c == '' or c == '[ Project Name ]'):
        return cell_val

    col_h = col_header.strip().lower().replace('*', '')
    row_l = row_label.strip().lower().replace('*', '')

    if is_arabic:
        # 1. Fixed-Row Tables: Authority & Governance
        if 'توظيف' in row_l:
            return 'صلاحية اختيار وتكليف أعضاء الفريق، تقييم الأداء الدوري، وتحديد خطط التدريب'
        if any(k in row_l for k in ['ميزانية', 'تكلفة']) and any(k in row_l for k in ['تباين', 'إدارة']):
            return 'صلاحية اعتماد المصروفات حتى 150,000 ريال؛ التباين > 5% يتطلب مصادقة الراعي التنفيذي'
        if 'فنية' in row_l or 'تقنية' in row_l:
            return 'اعتماد المواصفات الهندسية والمعمارية المتوافقة مع معايير السحابة المؤسسية'
        if 'نزاعات' in row_l or 'نزاع' in row_l:
            return 'حل النزاعات التشغيلية داخل الفريق، وتصعيد النزاعات الجوهرية إلى لجنة التوجيه'

        # Fixed-Row Tables: Project Charter Core Objectives
        if 'نطاق' in row_l:
            if 'معايير' in col_h or 'نجاح' in col_h:
                return 'أتمتة 100% من دورات سلاسل الإمداد والفوترة السحابية بنجاح'
            return 'نشر وتشغيل المنظومة السحابية الموحدة وتكاملها مع الأنظمة الأساسية'
        if 'جدول' in row_l or 'زمني' in row_l:
            if 'معايير' in col_h or 'نجاح' in col_h:
                return 'إنجاز كافة المعالم الحرجة في المواعيد المحددة دون تباين سلبي'
            return 'إنجاز كافة مراحل المشروع والتسليم التشغيلي خلال 18 شهراً'
        if 'تكلفة' in row_l or 'ميزانية' in row_l:
            if 'معايير' in col_h or 'نجاح' in col_h:
                return 'مؤشر أداء التكلفة CPI >= 1.00 وعدم تجاوز الميزانية المعتمدة'
            return 'تنفيذ المشروع بالكامل ضمن سقف الميزانية المعتمدة (12,500,000 ريال)'
        if 'أخرى' in row_l or 'جودة' in row_l:
            if 'معايير' in col_h or 'نجاح' in col_h:
                return 'تحقيق نسبة رضا مستخدمين >= 90% وزمن استجابة < 800ms'
            return 'تحقيق أعلى معايير الجودة والأمان الرقمي وسلاسة تجربة المستخدم'

        # 2. Open-Grid Tables: Match by Column Headers
        if any(k in col_h for k in ['معرف التغيير', 'change id']):
            return f"CR-2026-0{table_row_idx+1}"
        if any(k in col_h for k in ['معرف الخطر', 'رمز الخطر']):
            return f"RSK-0{table_row_idx+1}"
        if any(k in col_h for k in ['معرف', 'الرمز', 'كود', 'rbs']):
            prefixes = ['INIT', 'REQ', 'ACT', 'BEN', 'WBS', 'DEL', 'AUD']
            p = prefixes[table_row_idx % len(prefixes)]
            return f"{p}-0{table_row_idx+1}"
        if '#' in col_h or col_h in ['م', 'الرقم', 'ت']:
            return str(table_row_idx + 1)
        
        # AI Specific Tables (Datasets, Metrics, Ethics)
        if any(k in col_h for k in ['مجموعة البيانات', 'بيانات التدريب', 'مجموعة بيانات']):
            ds = ['بيانات أوامر الشراء والمخزون التاريخية', 'سجلات مطابقة الفواتير وعروض الأسعار', 'بيانات تفاعلات المستخدمين وبلاغات الدعم']
            return ds[table_row_idx % len(ds)]
        if any(k in col_h for k in ['المصدر وطريقة الجمع', 'طريقة الجمع']):
            sources = ['استخراج آلي مباشر من قواعد البيانات المركزية', 'أرشفة إلكترونية مؤمنة مع تدقيق التوافق', 'واجهات الربط البرمجي API مع سجلات مشفرة']
            return sources[table_row_idx % len(sources)]
        if any(k in col_h for k in ['التغطية السكانية والجغرافية', 'التغطية']):
            covs = ['كافة الفروع والمستودعات الإقليمية (المملكة)', 'عمليات المشتريات المركزية والفرعية', 'المعاملات التجارية لموردي الفئة (أ) و(ب)']
            return covs[table_row_idx % len(covs)]
        if any(k in col_h for k in ['الترخيص وسند الموافقة', 'سند الموافقة']):
            lics = ['ملكية بيانات مؤسسية خاصة بشركة القمة', 'ترخيص استخدام داخلي متوافق مع سياسة الخصوصية', 'موافقة رسمية من الإدارة المالية والامتثال']
            return lics[table_row_idx % len(lics)]
        if any(k in col_h for k in ['ما قبل المعالجة والترشيح', 'الترشيح', 'المعالجة']):
            filters = ['إغفال الهوية وإزالة البيانات الشخصية الحساسة', 'إزالة السجلات المكررة وتصحيح القيم الشاذة', 'توحيد صيغ التواريخ والعملات وفق ISO 4217']
            return filters[table_row_idx % len(filters)]
        if any(k in col_h for k in ['القيود المعروفة', 'قيود المنهج']):
            lims = ['تقتصر على العمليات المنفذة بالريال والدولار', 'عدم شمول المعاملات النقدية اليدوية القديمة', 'تتطلب تدقيقاً بشرياً للفواتير ذات البنود المتعددة']
            return lims[table_row_idx % len(lims)]
        if any(k in col_h for k in ['بيانات التقييم واستقلالها', 'بيانات التقييم']):
            eval_data = ['عينة اختبار معزولة (15% من البيانات التاريخية)', 'حزمة بيانات اختبارية جديدة من الربع الأول 2026', 'مجموعة تقييم أداء مستقلة ومحققة يدوياً']
            return eval_data[table_row_idx % len(eval_data)]
        if any(k in col_h for k in ['القيمة وحجم العينة', 'حجم العينة']):
            samples = ['دقة 94.2% (حجم العينة: 50,000 معاملة)', 'درجة F1 = 0.91 (حجم العينة: 25,000 فاتورة)', 'زمن استجابة 620ms (10,000 طلب متزامن)']
            return samples[table_row_idx % len(samples)]
        if any(k in col_h for k in ['الأداء بحسب الفئة', 'الفئة المتأثرة']):
            slices = ['دقة 96% للفواتير القياسية و91% للفواتير المعقدة', 'دقة 95% لموردي التجزئة و93% للخدمات', 'أداء متكافئ عبر كافة الفروع الإقليمية']
            return slices[table_row_idx % len(slices)]
        if any(k in col_h for k in ['المقارنة بخط الأساس', 'خط الأساس']):
            bases = ['تحسن بنسبة +28% مقارنة بالمعالجة التقليدية', 'خفض معدل الأخطاء بنسبة 65% عن النظام القديم', 'تفوق على خط الأساس بنسبة 18% في زمن المعالجة']
            return bases[table_row_idx % len(bases)]
        if any(k in col_h for k in ['العتبة السارية', 'العتبة']):
            thresh = ['الحد الأدنى للدقة المقبولة >= 90%', 'الحد الأقصى للخطأ <= 2%', 'الحد الأعلى لزمن الاستجابة <= 800ms']
            return thresh[table_row_idx % len(thresh)]
        if any(k in col_h for k in ['الاعتبار', 'الاعتبارات']):
            cons = ['عدالة التقييم وعدم التحيز للموردين الكبار', 'حماية خصوصية بيانات المعاملات والأسعار', 'موثوقية مخرجات التنبؤ بالمخزون']
            return cons[table_row_idx % len(cons)]
        if any(k in col_h for k in ['الفئات المتأثرة', 'الفئات']):
            aff = ['الموردون المحليون والمؤسسات الصغيرة والمتوسطة', 'موظفو إدارة المشتريات وسلاسل الإمداد', 'العملاء المستفيدون من سرعة تسليم الطلبات']
            return aff[table_row_idx % len(aff)]
        if any(k in col_h for k in ['النتيجة المحددة', 'الأثر المتوقع']):
            outcomes = ['فرص متكافئة في الترسية بناءً على الأداء الموضوعي', 'منع تسريب البيانات المالية الحساسة عبر التشفير', 'تقليل الهدر في المخزون بنسبة 15%']
            return outcomes[table_row_idx % len(outcomes)]
        if any(k in col_h for k in ['الخطورة', 'درجة الخطورة']):
            sevs = ['متوسطة (تتطلب مراجعة دورية)', 'منخفضة (ضمن الحدود المقبولة)', 'عالية (تتطلب إشرافاً بشرياً إلزامياً)']
            return sevs[table_row_idx % len(sevs)]
        if any(k in col_h for k in ['ما أُخذ من إجراء', 'الإجراء المتخذ', 'إجراء المعالجة']):
            acts = ['تطبيق اختبارات التكافؤ الإحصائي ومراقبة الانحياز', 'تفعيل بروتوكولات التشفير وإدارة مفاتيح الأمان', 'مراجعة بشرية للطلبات ذات القيمة العالية']
            return acts[table_row_idx % len(acts)]

        # Stakeholders & Executive Names
        if any(k in col_h for k in ['الاسم / المنصب', 'الاسم', 'المعني', 'أصحاب المصلحة', 'المعني (المعنيون)']):
            names = [
                'د. منى الغامدي (نائب الرئيس لتقنية المعلومات والعمليات)',
                'أ. سلطان الدوسري (نائب الرئيس للعمليات)',
                'أ. ناصر الغامدي (مدير قطاع العملاء)',
                'أ. عبد العزيز الزهراني (مدير الامتثال والحوكمة)',
                'د. طارق المنصور (مدير مكتب إدارة المشاريع PMO)'
            ]
            return names[table_row_idx % len(names)]
        
        # Authority & Roles
        if any(k in col_h for k in ['مستوى الصلاحية', 'الصلاحية']):
            auths = [
                'كامل الصلاحية لاعتماد ميثاق المشروع وتخصيص الميزانية والموارد المؤسسية',
                'اعتماد متطلبات الأعمال وقبول التسليمات المرحلية والنهائية',
                'حوكمة المنهجية واعتماد تقارير الأداء وبوابات العبور الرسمية',
                'المصادقة على معايير الامتثال والأمن السيبراني وحماية البيانات'
            ]
            return auths[table_row_idx % len(auths)]
        if any(k in col_h for k in ['الدور', 'الأدوار', 'الدور (الأدوار)']):
            roles = [
                'الرعاية الاستراتيجية وتوفير الموارد والمصادقة على الميثاق',
                'مالك متطلبات الأعمال وسلاسل الإمداد وقبول المخرجات',
                'المستفيد التجاري الرئيسي والمشاركة في اختبارات القبول UAT',
                'ضمان الامتثال للأمن السيبراني وحماية البيانات الشخصية'
            ]
            return roles[table_row_idx % len(roles)]

        # Milestones (Chronologically ordered)
        if any(k in col_h for k in ['معالم', 'معلم']):
            milestones = [
                'اعتماد وثيقة المتطلبات والتصميم المعماري',
                'تجهيز بيئة الاختبارات السحابية والتكامل',
                'اكتمال ترحيل ومطابقة البيانات التاريخية',
                'اجتياز اختبارات قبول المستخدمين (UAT)',
                'الإطلاق التشغيلي الحي وبدء مرحلة الدعم المركز'
            ]
            return milestones[table_row_idx % len(milestones)]

        # Initiatives & Work Packages
        if any(k in col_h for k in ['اسم المبادرة', 'المبادرة', 'اسم المشروع', 'المخرج', 'النشاط', 'المكون', 'حزمة']):
            names = [
                'المنظومة السحابية الموحدة لتخطيط الموارد',
                'أتمتة سلاسل الإمداد والمستودعات الذكية',
                'منصة التقارير التحليلية والذكاء المؤسسي',
                'بوابة الخدمات الذاتية وإدارة رأس المال البشري',
                'طبقة التكامل السحابي والربط البرمجي API'
            ]
            return names[table_row_idx % len(names)]
        if any(k in col_h for k in ['المبادرة التابعة', 'التابعة', 'اللاحقة']):
            names = ['أتمتة سلاسل الإمداد الذكية', 'منصة التقارير التحليلية المتقدمة', 'بوابة الخدمات الذاتية الموحدة', 'طبقة التكامل السحابي']
            return names[table_row_idx % len(names)]
        if any(k in col_h for k in ['السابقة', 'المتطلب السابق']):
            names = ['INIT-01 (المنظومة السحابية)', 'INIT-02 (سلاسل الإمداد)', 'INIT-01 (البنية التحتية)', 'INIT-03 (البيانات)']
            return names[table_row_idx % len(names)]
        if any(k in col_h for k in ['نوع الاعتمادية']):
            types = ['نهاية إلى بداية (FS)', 'بداية إلى بداية (SS)', 'نهاية إلى نهاية (FF)', 'نهاية إلى بداية (FS)']
            return types[table_row_idx % len(types)]
        if any(k in col_h for k in ['النوع', 'الفئة', 'التصنيف', 'مجال']):
            types = ['تقني وتكاملي', 'تنظيمي وتشغيلي', 'حوكمة وامتثال', 'بنية سحابية', 'أمن معلومات']
            return types[table_row_idx % len(types)]
        if any(k in col_h for k in ['الهدف الاستراتيجي', 'الهدف', 'أهداف المشروع']):
            objs = [
                'التحول الرقمي والتميز التشغيلي',
                'أتمتة العمليات وخفض التكاليف بنسبة 40%',
                'تمكين اتخاذ القرار بالبيانات اللحظية',
                'ضمان الامتثال التنظيمي والأمني بنسبة 100%'
            ]
            return objs[table_row_idx % len(objs)]
        if any(k in col_h for k in ['معايير النجاح', 'المقياس', 'مقياس']):
            metrics = [
                'دقة النموذج ومطابقة البيانات >= 95%',
                'تحقيق وفورات تشغيلية سنوية >= 3.5M ريال',
                'زمن استجابة للعمليات < 800 ميلي ثانية',
                'نسبة رضا المستخدمين النهائيين >= 90%'
            ]
            return metrics[table_row_idx % len(metrics)]

        # Dates (Chronological Progression)
        if any(k in col_h for k in ['البداية', 'تاريخ البدء']) or col_h == 'من':
            starts = ['2026-04-01', '2026-06-01', '2026-08-15', '2026-10-01', '2026-12-01']
            return starts[table_row_idx % len(starts)]
        if any(k in col_h for k in ['النهاية', 'تاريخ الانتهاء', 'مطلوب بحلول', 'تاريخ الاستحقاق', 'تاريخ المراجعة', 'تاريخ الإنجاز', 'تاريخ الهدف', 'تاريخ']) or col_h == 'إلى':
            ends = ['2026-06-30', '2026-09-30', '2026-11-30', '2027-01-31', '2027-03-31']
            return ends[table_row_idx % len(ends)]
        if any(k in col_h for k in ['الفترة']):
            periods = ['الربع الثاني 2026', 'الربع الثالث 2026', 'الربع الرابع 2026', 'الربع الأول 2027', 'الربع الثاني 2027']
            return periods[table_row_idx % len(periods)]
        
        # Financials & Capacity
        if any(k in col_h for k in ['التمويل المخطط', 'الميزانية', 'التكلفة', 'المبلغ', 'الميزانية المعتمدة', 'القيمة']):
            budgets = ['3,500,000 ريال', '4,200,000 ريال', '2,800,000 ريال', '1,950,000 ريال', '1,250,000 ريال']
            return budgets[table_row_idx % len(budgets)]
        if any(k in col_h for k in ['السعة المخططة', 'السعة']):
            caps = ['480 ساعة عمل / شهر', '620 ساعة عمل / شهر', '540 ساعة عمل / شهر', '500 ساعة عمل / شهر']
            return caps[table_row_idx % len(caps)]
        if any(k in col_h for k in ['العبء الملتزم']):
            loads = ['420 ساعة عمل / شهر', '580 ساعة عمل / شهر', '490 ساعة عمل / شهر', '440 ساعة عمل / شهر']
            return loads[table_row_idx % len(loads)]
        if any(k in col_h for k in ['المتاح']):
            avails = ['60 ساعة عمل (فائض)', '40 ساعة عمل (فائض)', '50 ساعة عمل (فائض)', '60 ساعة عمل (فائض)']
            return avails[table_row_idx % len(avails)]
        if any(k in col_h for k in ['الحالة', 'الوضع']):
            statuses = ['قيد التنفيذ', 'مكتمل', 'مخطط', 'معتمد']
            return statuses[table_row_idx % len(statuses)]
        if any(k in col_h for k in ['الأثر عند التأخر', 'الأثر على خارطة الطريق', 'الأثر']):
            impacts = [
                'تأخير بدء اختبارات التكامل لمدة أسبوعين',
                'إعادة جدولة نافذة الإطلاق التشغيلي التجريبي',
                'زيادة طفيفة في استهلاك ساعات الاستشارات التقنية',
                'ترحيل تاريخ التدريب للمجموعة الثانية'
            ]
            return impacts[table_row_idx % len(impacts)]
        if any(k in col_h for k in ['السبب']):
            reasons = [
                'تحديث متطلبات التكامل الأمني السحابي',
                'توسيع نطاق التقارير التحليلية لإدارة العمليات',
                'مواءمة مسارات النشر مع إغلاق الربع المالي',
                'إضافة متطلبات الأرشفة الرقمية والامتثال'
            ]
            return reasons[table_row_idx % len(reasons)]
        if any(k in col_h for k in ['المبادرات المتأثرة']):
            return 'INIT-01, INIT-02'
        if any(k in col_h for k in ['المالك', 'المسؤول', 'اعتمده', 'المستفيد']):
            owners = [
                'أ. إلينا فانس، PfMP',
                'م. فيصل الحربي، PMP',
                'د. طارق المنصور، PfMP',
                'أ. سلطان الدوسري'
            ]
            return owners[table_row_idx % len(owners)]
        if any(k in col_h for k in ['الوصف', 'تفاصيل', 'بيان', 'موجز']):
            descs = [
                'نشر وتجهيز البنية السحابية وقواعد البيانات الموحدة',
                'أتمتة دورة المشتريات والمستودعات والربط المباشر',
                'بناء لوحات المؤشرات التفاعلية والتحليلات المتقدمة',
                'تفعيل قنوات الدعم الفني والتدريب للمستخدمين'
            ]
            return descs[table_row_idx % len(descs)]
        if any(k in col_h for k in ['ملاحظات', 'ملاحظة', 'الإجراء']):
            notes = [
                'تم التحقق من الجاهزية والامتثال لضوابط الأمن السيبراني',
                'جلسات المتابعة والتنسيق مستمرة وفق الجدول المعتمد',
                'تم رصد مخصص الطوارئ المعتمد لهذه المرحلة',
                'مؤشرات الأداء التشغيلي ضمن الحدود المستهدفة'
            ]
            return notes[table_row_idx % len(notes)]
        return 'معتمد ومطابق للمعايير القياسية لشركة القمة'

    else:
        # English
        # 1. Fixed-Row Tables: Authority & Governance
        if 'staffing' in row_l:
            return 'Authority to select project team members, assign tasks, and evaluate performance'
        if any(k in row_l for k in ['budget', 'cost']) and any(k in row_l for k in ['variance', 'management']):
            return 'Authorize expenditures up to $40,000 USD; variances > 5% require Sponsor approval'
        if 'technical' in row_l:
            return 'Approve solution architecture designs compliant with enterprise cloud standards'
        if 'conflict' in row_l:
            return 'Resolve team operational conflicts; escalate strategic disputes to Steering Committee'

        # Fixed-Row Tables: Project Charter Core Objectives
        if 'scope' in row_l:
            if 'criteria' in col_h or 'success' in col_h:
                return '100% automation of procurement, supply chain, and billing cycles'
            return 'Deploy and integrate unified cloud ERP platform across all enterprise units'
        if 'schedule' in row_l:
            if 'criteria' in col_h or 'success' in col_h:
                return 'Deliver all phases within 18 months with zero critical path slippage'
            return 'Complete end-to-end system rollout and cutover within 18 months'
        if 'cost' in row_l:
            if 'criteria' in col_h or 'success' in col_h:
                return 'Maintain Cost Performance Index (CPI) >= 1.00 within approved budget'
            return 'Execute project within pre-approved $3,500,000 USD budget envelope'
        if 'other' in row_l or 'quality' in row_l:
            if 'criteria' in col_h or 'success' in col_h:
                return 'Achieve >= 90% user satisfaction and sub-second transaction latency'
            return 'Deliver high system reliability (99.95% uptime) and superior user experience'

        # 2. Open-Grid Tables: Match by Column Headers
        if any(k in col_h for k in ['change id']):
            return f"CR-2026-0{table_row_idx+1}"
        if any(k in col_h for k in ['risk id']):
            return f"RSK-0{table_row_idx+1}"
        if any(k in col_h for k in ['id', 'code', 'rbs']):
            prefixes = ['INIT', 'REQ', 'ACT', 'BEN', 'WBS', 'DEL', 'AUD']
            p = prefixes[table_row_idx % len(prefixes)]
            return f"{p}-0{table_row_idx+1}"
        if '#' in col_h or col_h in ['no', 'item', 'seq']:
            return str(table_row_idx + 1)
        
        # AI Specific Tables (Datasets, Metrics, Ethics)
        if any(k in col_h for k in ['dataset', 'training data', 'training datasets']):
            ds = ['Historical Purchase Orders & Inventory Logs', 'Vendor Invoices & RFQ Quotation Records', 'User Operational Interaction & Ticket Logs']
            return ds[table_row_idx % len(ds)]
        if any(k in col_h for k in ['source', 'provenance', 'collection method']):
            sources = ['Automated database ETL pipeline extraction', 'Secure electronic archiving with compliance audit', 'API ingestion streams with tokenized logging']
            return sources[table_row_idx % len(sources)]
        if any(k in col_h for k in ['population', 'geographic coverage', 'coverage']):
            covs = ['Enterprise-wide regional logistics hubs', 'Central and regional procurement units', 'Tier-1 and Tier-2 commercial vendors']
            return covs[table_row_idx % len(covs)]
        if any(k in col_h for k in ['licence', 'consent', 'license and consent']):
            lics = ['Proprietary enterprise internal asset', 'Authorized operational telemetry under policy', 'Formal CFO & Compliance authorization sign-off']
            return lics[table_row_idx % len(lics)]
        if any(k in col_h for k in ['preprocessing', 'filtering', 'cleaning']):
            filters = ['PII de-identification and masking protocols', 'Deduplication and anomaly detection cleaning', 'Standardized ISO datetime and currency normalization']
            return filters[table_row_idx % len(filters)]
        if any(k in col_h for k in ['known limitations', 'limitations']):
            lims = ['Restricted to USD and SAR transaction types', 'Excludes legacy manual offline paper cash slips', 'Requires human-in-the-loop review on multi-line POs']
            return lims[table_row_idx % len(lims)]
        if any(k in col_h for k in ['evaluation data', 'eval data']):
            eval_data = ['Isolated test holdout partition (15% dataset)', 'Fresh Q1-2026 transaction batch', 'Independent manually annotated validation set']
            return eval_data[table_row_idx % len(eval_data)]
        if any(k in col_h for k in ['value and sample size', 'sample size']):
            samples = ['94.2% accuracy (Sample Size: 50,000 records)', 'F1-Score: 0.91 (Sample Size: 25,000 invoices)', 'Latency: 620ms (10,000 concurrent requests)']
            return samples[table_row_idx % len(samples)]
        if any(k in col_h for k in ['performance by slice', 'slice performance']):
            slices = ['96% accuracy on standard POs; 91% on complex POs', '95% on retail suppliers; 93% on service vendors', 'Consistent latency parity across all regions']
            return slices[table_row_idx % len(slices)]
        if any(k in col_h for k in ['baseline comparison', 'baseline']):
            bases = ['+28% throughput increase over legacy manual flow', '65% error reduction compared to legacy baseline', '+18% speedup over existing ERP workflow']
            return bases[table_row_idx % len(bases)]
        if any(k in col_h for k in ['threshold', 'applicable threshold']):
            thresh = ['Minimum acceptable accuracy >= 90%', 'Maximum error tolerance <= 2%', 'Maximum latency SLA <= 800ms']
            return thresh[table_row_idx % len(thresh)]
        if any(k in col_h for k in ['consideration', 'ethical consideration']):
            cons = ['Fairness and zero bias across supplier sizes', 'Data privacy protection for commercial terms', 'Demand forecasting reliability and robustness']
            return cons[table_row_idx % len(cons)]
        if any(k in col_h for k in ['affected group', 'affected population']):
            aff = ['Local small-and-medium enterprise suppliers', 'Procurement and inventory operations personnel', 'Commercial clients benefiting from timely deliveries']
            return aff[table_row_idx % len(aff)]
        if any(k in col_h for k in ['specific outcome', 'expected outcome']):
            outcomes = ['Equitable bidding evaluation based on objective metrics', 'Zero exposure of sensitive commercial pricing data', '15% reduction in stockout incidents']
            return outcomes[table_row_idx % len(outcomes)]
        if any(k in col_h for k in ['severity', 'risk level']):
            sevs = ['Medium (Subject to quarterly audit)', 'Low (Within acceptable operating bounds)', 'High (Requires mandatory human approval)']
            return sevs[table_row_idx % len(sevs)]
        if any(k in col_h for k in ['action taken', 'mitigation action']):
            acts = ['Statistical parity validation and bias monitoring', 'Key rotation and end-to-end encryption protocols', 'Human review required for transactions > $15,000 USD']
            return acts[table_row_idx % len(acts)]

        # Stakeholders & Executive Names
        if any(k in col_h for k in ['name / position', 'name', 'stakeholder', 'stakeholder(s)']):
            names = [
                'Dr. Muna Al-Ghamdi (Executive VP of Technology & Operations)',
                'Sultan Al-Dossary (VP of Operations)',
                'Nasser Al-Ghamdi (Commercial Client Director)',
                'Abdulaziz Al-Zahrani (Compliance & Governance Director)',
                'Tariq Al-Mansoor, PfMP (PMO Director)'
            ]
            return names[table_row_idx % len(names)]
        
        # Authority & Roles
        if any(k in col_h for k in ['authority level', 'authority']):
            auths = [
                'Full executive authority to charter project, approve budget envelope, and commit resources',
                'Business requirements sign-off and final operational acceptance authority',
                'Governance oversight, stage-gate audit validation, and method compliance',
                'Information security, regulatory compliance, and data privacy validation'
            ]
            return auths[table_row_idx % len(auths)]
        if any(k in col_h for k in ['role', 'roles', 'role(s)']):
            roles = [
                'Strategic executive oversight and resource authorization',
                'Business process owner and final acceptance authority',
                'Primary commercial user champion and UAT stakeholder',
                'Regulatory compliance and data governance validator'
            ]
            return roles[table_row_idx % len(roles)]

        # Milestones (Chronologically ordered)
        if any(k in col_h for k in ['milestone', 'milestones']):
            milestones = [
                'Architecture Design & Requirements Sign-off',
                'Cloud Infrastructure & Sandbox Readiness',
                'Historical Data Migration & Verification',
                'User Acceptance Testing (UAT) Sign-off',
                'Production Go-Live & Hypercare Transition'
            ]
            return milestones[table_row_idx % len(milestones)]

        # Initiatives & Components
        if any(k in col_h for k in ['initiative name', 'initiative', 'project name', 'task', 'activity', 'component', 'work package']):
            names = [
                'Unified Cloud ERP Core Architecture',
                'Automated Procurement & Smart Supply Chain Engine',
                'Executive Business Intelligence & Reporting Platform',
                'Employee Self-Service & HR Capital Portal',
                'Enterprise API Gateway & Security Integration'
            ]
            return names[table_row_idx % len(names)]
        if any(k in col_h for k in ['dependent initiative', 'successor']):
            names = ['Smart Supply Chain Engine', 'Executive BI Platform', 'Employee Self-Service Portal', 'Enterprise API Gateway']
            return names[table_row_idx % len(names)]
        if any(k in col_h for k in ['predecessor']):
            names = ['INIT-01 (Cloud ERP Core)', 'INIT-02 (Supply Chain)', 'INIT-01 (Cloud Architecture)', 'INIT-03 (Data Layer)']
            return names[table_row_idx % len(names)]
        if any(k in col_h for k in ['dependency type']):
            types = ['Finish-to-Start (FS)', 'Start-to-Start (SS)', 'Finish-to-Finish (FF)', 'Finish-to-Start (FS)']
            return types[table_row_idx % len(types)]
        if any(k in col_h for k in ['type', 'category', 'classification', 'domain', 'authority area']):
            types = ['Technical & Integration', 'Operational & Functional', 'Governance & Compliance', 'Cloud Infrastructure', 'Cybersecurity']
            return types[table_row_idx % len(types)]
        if any(k in col_h for k in ['strategic objective', 'objective', 'goal', 'project objectives']):
            objs = [
                'Digital Transformation & Operational Agility',
                'Process Automation & 40% Cycle Time Reduction',
                'Real-time Data-Driven Executive Decision Making',
                '100% Security & Regulatory Compliance Assurance'
            ]
            return objs[table_row_idx % len(objs)]
        if any(k in col_h for k in ['measure', 'success criteria', 'metric']):
            metrics = [
                'Model inference accuracy & data reconciliation >= 95%',
                'Annual recurring operational savings >= $950K USD',
                'Sub-second transaction response latency (< 800ms)',
                'End-user CSAT score >= 90% in audit'
            ]
            return metrics[table_row_idx % len(metrics)]

        # Dates (Chronological Progression)
        if any(k in col_h for k in ['start date', 'start']) or col_h == 'from':
            starts = ['2026-04-01', '2026-06-01', '2026-08-15', '2026-10-01', '2026-12-01']
            return starts[table_row_idx % len(starts)]
        if any(k in col_h for k in ['end date', 'end', 'required by', 'due date', 'review date', 'target date', 'date']) or col_h == 'to':
            ends = ['2026-06-30', '2026-09-30', '2026-11-30', '2027-01-31', '2027-03-31']
            return ends[table_row_idx % len(ends)]
        if any(k in col_h for k in ['period']):
            periods = ['2026-Q2', '2026-Q3', '2026-Q4', '2027-Q1', '2027-Q2']
            return periods[table_row_idx % len(periods)]
        
        # Financials & Capacity
        if any(k in col_h for k in ['planned funding', 'budget', 'cost', 'amount', 'value']):
            budgets = ['$950,000 USD', '$1,150,000 USD', '$780,000 USD', '$520,000 USD', '$350,000 USD']
            return budgets[table_row_idx % len(budgets)]
        if any(k in col_h for k in ['planned capacity', 'capacity']):
            caps = ['480 FTE Hours / mo', '620 FTE Hours / mo', '540 FTE Hours / mo', '500 FTE Hours / mo']
            return caps[table_row_idx % len(caps)]
        if any(k in col_h for k in ['committed load']):
            loads = ['420 FTE Hours / mo', '580 FTE Hours / mo', '490 FTE Hours / mo', '440 FTE Hours / mo']
            return loads[table_row_idx % len(loads)]
        if any(k in col_h for k in ['available']):
            avails = ['60 FTE Hours (Buffer)', '40 FTE Hours (Buffer)', '50 FTE Hours (Buffer)', '60 FTE Hours (Buffer)']
            return avails[table_row_idx % len(avails)]
        if any(k in col_h for k in ['status', 'state', 'progress']):
            statuses = ['In Progress', 'Completed', 'Planned', 'Approved']
            return statuses[table_row_idx % len(statuses)]
        if any(k in col_h for k in ['impact if late', 'impact on roadmap', 'impact on program', 'impact']):
            impacts = [
                '2-week schedule slippage on integration testing window',
                'Rescheduling of operational pilot rollout date',
                'Minor reallocation of cloud professional services',
                'Postponement of cohort 2 training wave'
            ]
            return impacts[table_row_idx % len(impacts)]
        if any(k in col_h for k in ['reason']):
            reasons = [
                'Security baseline compliance enhancement',
                'Operational scope extension for branch logistics',
                'Alignment with quarterly fiscal cutover milestones',
                'Integration with new compliance data stream'
            ]
            return reasons[table_row_idx % len(reasons)]
        if any(k in col_h for k in ['affected initiatives']):
            return 'INIT-01, INIT-02'
        if any(k in col_h for k in ['owner', 'approved by', 'responsible', 'assigned to', 'beneficiary']):
            owners = [
                'Elena Vance, PfMP',
                'Faisal Al-Harbi, PMP',
                'Tariq Al-Mansoor, PfMP',
                'Sultan Al-Dossary'
            ]
            return owners[table_row_idx % len(owners)]
        if any(k in col_h for k in ['description', 'summary', 'details']):
            descs = [
                'Deploy hardened cloud environment and master databases',
                'Automate procurement requisition and inventory workflows',
                'Build interactive executive dashboards and KPI reports',
                'Conduct comprehensive end-user enablement workshops'
            ]
            return descs[table_row_idx % len(descs)]
        if any(k in col_h for k in ['notes', 'comments', 'remarks']):
            notes = [
                'Validated against enterprise ISO27001 cloud security standards.',
                'Weekly steering coordination meetings on schedule.',
                'Contingency reserve allocated for critical path dependencies.',
                'Operational KPIs performing within target tolerance.'
            ]
            return notes[table_row_idx % len(notes)]
        return 'Approved and aligned with Apex Global Solutions governance baseline'

def fill_narrative_placeholder(section_title: str, is_arabic: bool) -> str:
    """Generates rich, realistic narrative text tailored to specific section titles."""
    sec_lower = section_title.lower()
    
    if is_arabic:
        # AI, Machine Learning, Ethics & Governance
        if any(k in sec_lower for k in ['ذكاء', 'نموذج', 'خوارزم']) and any(k in sec_lower for k in ['جاهزية', 'تقييم', 'حوكمة', 'بطاقة']):
            return ("تم تقييم جاهزية الذكاء الاصطناعي لمنظومة القمة بدرجة 'متقدمة' (88/100). تم التحقق من جودة واستقرار خطوط أنابيب البيانات، "
                    "وتجهيز بيئة التدريب السحابية المعزولة مع تفعيل ضوابط الحوكمة الصارمة للتحكم في الوصول ومنع الانجراف المعرفي.")
        elif any(k in sec_lower for k in ['أخلاق', 'عدالة', 'تحيز', 'إنصاف']):
            return ("تلتزم المنظومة بالمبادئ الأخلاقية المعتمدة لحوكمة الذكاء الاصطناعي، وتتضمن آليات كشف وتحييد أي انحياز خوارزمي محتمل "
                    "ضد أي شريحة من الموردين أو العملاء، مع توفير سجل تدقيق رقمي كامل لكافة الاستدلالات والتوصيات المولدة.")
        elif any(k in sec_lower for k in ['بيانات التدريب', 'جودة البيانات', 'مصادر البيانات']):
            return ("تعتمد المنظومة على بيانات تشغيلية وتاريخية معتمدة ومغفلة الهوية تغطي 5 سنوات من المعاملات المؤسسية (2.4 مليون سجل)، "
                    "تم تنقيحها ومطابقتها للتأكد من خلوها من القيم الشاذة ومطابقتها لمعايير الجودة ISO 8000.")
        elif any(k in sec_lower for k in ['إشراف بشري', 'مساءلة', 'تدخل بشري']):
            return ("تطبق المنظومة مبدأ 'الإشراف البشري في الحلقة' (Human-in-the-Loop)؛ حيث تتطلب كافة المعاملات ذات الحساسية المالية "
                    "أو القرارات الاستراتيجية مراجعة ومصادقة صريحة من المسؤول المخول قبل التنفيذ النهائي في بيئة الإنتاج.")

        # Purpose, Strategy & Vision
        elif any(k in sec_lower for k in ['غرض', 'الهدف', 'مبرر', 'رؤية', 'حاجة', 'استراتيج', 'سياق']):
            return ("يهدف هذا المشروع إلى توحيد وأتمتة كافة العمليات التشغيلية وسلاسل الإمداد "
                    "والإدارة المالية لشركة القمة من خلال الانتقال إلى منظومة سحابية متطورة (Nexus ERP). "
                    "يعالج المشروع التحديات التشغيلية الناتجة عن تشتت البيانات في أنظمة قديمة معزولة، "
                    "ويحقق وفراً تشغيلياً سنوياً يقدر بـ 4.2 مليون ريال مع تقليص دورة معالجة الطلبات بنسبة 40%، "
                    "بما يتماشى مباشرة مع الركيزة الاستراتيجية للتحول الرقمي والتميز التشغيلي 2028.")
        
        # Scope, Deliverables & Boundaries
        elif any(k in sec_lower for k in ['حدود', 'استثناء', 'استثناءات']):
            return ("حدود النطاق المؤسسي:\n"
                    "* يشمل المشروع جميع المقرات الرئيسية والفروع الإقليمية ومراكز التوزيع التابعة للشركة.\n"
                    "* يستثنى من النطاق الحالي ترقية أنظمة نقاط البيع الطرفية القديمة (مؤجلة للمرحلة الثانية).\n"
                    "* يستثنى شراء خوادم داخلية محلية نظراً للاعتماد الكامل على البنية السحابية المعتمدة.")
        elif any(k in sec_lower for k in ['تسليمات', 'مخرجات', 'منتج']):
            return ("التسليمات الرئيسية المعتمدة:\n"
                    "* وثيقة التصميم المعماري التفصيلي وخطة التكامل المؤسسي.\n"
                    "* بيئة الإنتاج السحابية المهيأة والمؤمنة وفق معايير الأمن المؤسسي.\n"
                    "* قواعد البيانات الموحدة بعد ترحيل ومطابقة البيانات التاريخية.\n"
                    "* حزمة التدريب والأدلة الإرشادية لـ 450 موظفاً ومستخدماً نهائياً.\n"
                    "* شهادات اجتياز اختبارات الأداء وقبول المستخدمين (UAT) والجاهزية التشغيلية.")
        elif any(k in sec_lower for k in ['وصف', 'نطاق', 'بيان', 'معمار']):
            return ("يتضمن نطاق المشروع بناء ونشر منظومة سحابية موحدة وشاملة تشمل الوحدات الوظيفية التالية:\n"
                    "1. إدارة المشتريات والمستودعات وسلاسل الإمداد الذكية.\n"
                    "2. الإدارة المالية والمحاسبية وإعداد التقارير والامتثال الضريبي.\n"
                    "3. إدارة رأس المال البشري والرواتب والخدمات الذاتية للموظفين.\n"
                    "4. طبقة التكامل والربط الإلكتروني الآمن مع البوابات المؤسسية.\n"
                    "5. لوحات مؤشرات الأداء والتحليلات التنبؤية المتقدمة للإدارة التنفيذية.")

        # Financials, Cost & EVM
        elif any(k in sec_lower for k in ['قيمة مكتسبة', 'eva', 'تباين التكلفة', 'أداء التكلفة']):
            return ("أظهر تحليل القيمة المكتسبة (EVA) أداءً مالياً منضبطاً للشهر الحالي؛ حيث بلغ مؤشر أداء التكلفة CPI = 1.04 "
                    "ومؤشر أداء الجدول SPI = 1.01، مما يؤكد سير المشروع وفق الميزانية المعتمدة مع وفر محقق قدره 180,000 ريال.")
        elif any(k in sec_lower for k in ['مالي', 'مالية', 'موارد', 'ميزانية', 'تمويل', 'تكلفة', 'تكاليف']):
            return ("الموارد المالية والتمويل المعتمد مسبقاً:\n"
                    "* الميزانية الكلية المعتمدة للمشروع: **12,500,000 ريال سعودي** موزعة كالتالي:\n"
                    "  - تراخيص المنظومة السحابية والاشتراكات السنوية: 4,800,000 ريال.\n"
                    "  - خدمات الاستشارات والتنفيذ والتهيئة: 5,200,000 ريال.\n"
                    "  - تدريب الكوادر وإدارة التغيير المؤسسي: 1,250,000 ريال.\n"
                    "  - احتياطي الطوارئ الإداري (10%): 1,250,000 ريال.")

        # Governance, Approval & Exit Criteria
        elif any(k in sec_lower for k in ['اعتماد', 'موافقة', 'حوكمة', 'شروط']) and any(k in sec_lower for k in ['متطلبات', 'مشروع', 'معايير']):
            return ("متطلبات اعتماد ونجاح المشروع:\n"
                    "1. استيفاء 100% من معايير القبول الفنية واجتياز اختبارات قبول المستخدمين دون ملاحظات حرجة.\n"
                    "2. توقيع محاضر الاستلام والتسليم التشغيلي من الراعي التنفيذي ونائب الرئيس للعمليات.\n"
                    "3. تقديم تقرير إغلاق المرحلة والمصادقة عليه من قبل مكتب إدارة المشاريع (PMO).")
        elif any(k in sec_lower for k in ['خروج', 'إغلاق', 'معايير']):
            return ("معايير الخروج والقبول النهائي:\n"
                    "1. اجتياز اختبارات قبول المستخدمين بنسبة 100% وإغلاق كافة الملاحظات عالية الخطورة.\n"
                    "2. اكتمال ترحيل البيانات ومطابقتها وتوقيع محاضر الاستلام من الإدارة المالية والعمليات.\n"
                    "3. إتمام تدريب 95% على الأقل من المستخدمين المستهدفين واجتيازهم لتقييم الكفاءة.\n"
                    "4. استقرار النظام في بيئة الإنتاج لمدة 30 يوماً متواصلة دون انقطاعات حرجة.")

        # Risk, Issues & Health Check
        elif any(k in sec_lower for k in ['مخاطر', 'مخاطرة', 'خطر']):
            return ("المخاطر الكلية واستراتيجية المعالجة:\n"
                    "تم تقييم مستوى المخاطر الكلي للمشروع بدرجة 'متوسطة إلى عالية' نظراً لتعدد واجهات التكامل وتأثير التغيير على العمليات اليومية. "
                    "تم وضع خطط تخفيف تشمل تكليف فريق دعم مخصص للترحيل، تطبيق منهجية تدريجية للإطلاق التجريبي (Pilot)، "
                    "ورصد احتياطي طوارئ مالي بنسبة 10% واحتياطي زمني قدره 4 أسابيع على المسار الحرج.")
        elif any(k in sec_lower for k in ['مشكلات', 'عوائق', 'انحرافات']):
            return ("تم حصر المشكلات التشغيلية وتصنيفها؛ حيث يجري التعامل مع تأخر توريد بعض التراخيص عبر البيئة التجريبية "
                    "دون أي تأثير مباشر على الجدول الزمني للمسار الحرج.")

        # Requirements, Specifications & Assumptions
        elif any(k in sec_lower for k in ['متطلبات', 'مواصفات']):
            return ("المتطلبات الأساسية عالية المستوى:\n"
                    "* توفير زمن استجابة للعمليات لا يتجاوز 800 ميلي ثانية تحت ذروة تشغيل 1,200 مستخدم متزامن.\n"
                    "* التوافق الكامل مع معايير الفوترة الإلكترونية والأنظمة المحاسبية المعتمدة.\n"
                    "* ضمان توفر النظام بنسبة لا تقل عن 99.95% مع خطة استعادة أعمال في زمن RTO < ساعتين.\n"
                    "* توفير تطبيق جوال للخدمات الذاتية والموافقات السريعة للمدراء التنفيذيين.")
        elif any(k in sec_lower for k in ['افتراض', 'افتراضات', 'قيد', 'قيود']):
            return ("الافتراضات والقيود المؤسسية:\n"
                    "* **الافتراضات:** توفر كوادر الأعمال المتخصصة للمشاركة في ورش العمل بنسبة 25% من وقتهم؛ استقرار واجهات الأنظمة الخارجية.\n"
                    "* **القيود:** الالتزام بالموعد النهائي للإطلاق قبل بداية الربع المالي الجديد؛ سقف الميزانية الرأسمالية المعتمد 12.5 مليون ريال؛ الالتزام الصارم بضوابط حماية البيانات.")

        # OCM, Training & Communication
        elif any(k in sec_lower for k in ['تغيير', 'تواصل', 'تدريب', 'تبني']):
            return ("خطة إدارة التغيير والتأهيل المؤسسي:\n"
                    "تستهدف الخطة تدريب 450 مستخدماً عبر 18 ورشة تدريبية عملية وتوفير أدلة إرشادية رقمية تفاعلية، "
                    "مع إطلاق حملة توعوية دورية لرفع نسبة الجاهزية والتبني المؤسسي إلى أكثر من 95% قبل موعد الإطلاق الحي.")
        elif any(k in sec_lower for k in ['جودة', 'تدقيق', 'امتثال']):
            return ("ضمان الجودة والامتثال المؤسسي:\n"
                    "تخضع كافة مخرجات المشروع لتدقيق دوري وفق معايير مكتب إدارة المشاريع (PMO) ومواصفات ISO 9001 وISO 27001، "
                    "مع إجراء مراجعات مرحلية عند كل بوابة عبور لضمان الجودة الشاملة ومطابقة المواصفات.")
        else:
            return ("تم توثيق هذا القسم واعتماده بالتفصيل وفق خطة المشروع التشغيلية لشركة القمة للحلول المؤسسية المتقدمة، "
                    "بما يضمن التوافق الكامل مع أفضل ممارسات الحوكمة الصادرة عن مكتب إدارة المشاريع (PMO).")

    else:
        # AI, Machine Learning, Ethics & Governance
        if any(k in sec_lower for k in ['ai', 'model', 'learning']) and any(k in sec_lower for k in ['readiness', 'assessment', 'governance', 'card']):
            return ("The enterprise AI readiness assessment scored 88/100 ('Advanced Readiness'). Data pipelines and feature stores "
                    "have been verified for stability, and isolated cloud sandbox environments are provisioned with automated drift detection.")
        elif any(k in sec_lower for k in ['ethics', 'fairness', 'bias', 'equity']):
            return ("The solution strictly adheres to the Enterprise Responsible AI Framework. Ongoing statistical parity tests "
                    "and explainability layers ensure zero demographic or regional bias across vendor evaluations and automated recommendations.")
        elif any(k in sec_lower for k in ['training data', 'data provenance', 'datasets']):
            return ("The model is trained on 5 years of verified, anonymized enterprise transaction records (2.4M records), "
                    "cleansed and validated in compliance with ISO 8000 data quality and privacy standards.")
        elif any(k in sec_lower for k in ['human oversight', 'oversight', 'accountability']):
            return ("A mandatory 'Human-in-the-Loop' policy is enforced for all automated decisions exceeding $15,000 USD "
                    "or where the model confidence threshold drops below 90%, requiring explicit management sign-off.")

        # Purpose, Strategy & Vision
        elif any(k in sec_lower for k in ['purpose', 'justification', 'vision', 'objective', 'need', 'context']):
            return ("The purpose of this project is to consolidate, modernize, and automate Apex Global Solutions' "
                    "end-to-end supply chain, financial management, and operational workflows by deploying a state-of-the-art "
                    "cloud-native ERP platform (Apex Enterprise Nexus). This initiative directly eliminates data silos from legacy systems, "
                    "achieves a projected annual operational savings of $1.15M USD, reduces order cycle times by 40%, and "
                    "directly advances Enterprise Strategic Pillar 1 (Digital Agility & Operational Excellence).")
        
        # Scope, Deliverables & Boundaries
        elif any(k in sec_lower for k in ['boundaries', 'boundary', 'exclusion']):
            return ("Scope Boundaries & Exclusions:\n"
                    "* **In-Scope:** Corporate headquarters, regional business units, distribution fulfillment centers, and cloud infrastructure.\n"
                    "* **Out-of-Scope:** Hardware replacement for physical POS terminals at retail kiosks (deferred to Phase 2).\n"
                    "* **Exclusions:** On-premise server acquisitions; legacy custom code maintenance beyond the migration period.")
        elif any(k in sec_lower for k in ['deliverable', 'output', 'product']):
            return ("Key Project Deliverables:\n"
                    "* Detailed Solution Architecture & Data Integration Blueprint.\n"
                    "* Fully provisioned, hardened cloud production environment meeting enterprise security standards.\n"
                    "* Validated historical master data migration package (99.98% reconciliation rate).\n"
                    "* Comprehensive training curriculum delivered to 450+ business users and functional admins.\n"
                    "* User Acceptance Testing (UAT) sign-off certificates and Operational Handover dossier.")
        elif any(k in sec_lower for k in ['description', 'scope', 'statement', 'architecture']):
            return ("The project encompasses the end-to-end implementation and rollout of a unified cloud ERP suite comprising:\n"
                    "1. Automated Procurement, Inventory Management, and Smart Supply Chain logistics.\n"
                    "2. Core Financials, General Ledger, Multi-currency Treasury, and Tax Compliance modules.\n"
                    "3. Human Capital Management (HCM), Payroll automation, and Employee Self-Service portals.\n"
                    "4. Secure enterprise API integration middleware connecting CRM, BI, and banking gateways.\n"
                    "5. Real-time executive dashboards and predictive operational analytics engines.")

        # Financials, Cost & EVM
        elif any(k in sec_lower for k in ['earned value', 'eva', 'cost variance', 'cost performance']):
            return ("Earned Value Analysis (EVA) confirms robust cost control for the active reporting period. "
                    "The project exhibits a Cost Performance Index (CPI) of 1.04 and a Schedule Performance Index (SPI) of 1.01, "
                    "yielding a favorable cost variance of $48,000 USD against the baseline.")
        elif any(k in sec_lower for k in ['financial', 'resource', 'budget', 'cost', 'funding']):
            return ("Preapproved Financial Resources & Budget Envelope:\n"
                    "* Total Approved Capital & Operational Envelope: **$3,500,000 USD**, structured as:\n"
                    "  - Cloud SaaS Licensing & Infrastructure Subscription: $1,350,000 USD.\n"
                    "  - Systems Integration & Professional Engineering Services: $1,450,000 USD.\n"
                    "  - Organizational Change Management & User Enablement: $350,000 USD.\n"
                    "  - Management Contingency Reserve (10%): $350,000 USD.")

        # Governance, Approval & Exit Criteria
        elif any(k in sec_lower for k in ['approval', 'governance']) and any(k in sec_lower for k in ['requirement', 'project', 'criteria']):
            return ("Project Approval Requirements:\n"
                    "1. Unanimous consensus from Executive Sponsor and VP Operations on final UAT results.\n"
                    "2. Formal verification of all stage-gate deliverables by PMO Lead.\n"
                    "3. Complete execution of cutover checklist and operational transition sign-off.")
        elif any(k in sec_lower for k in ['exit', 'criteria', 'acceptance']):
            return ("Project Exit & Acceptance Criteria:\n"
                    "1. 100% passing rate on UAT test cases with zero open Sev-1 or Sev-2 defect tickets.\n"
                    "2. Verified cutover and data reconciliation signed off by Chief Financial Officer and VP Operations.\n"
                    "3. Minimum 95% user training attendance and proficiency certification completed across all departments.\n"
                    "4. 30 consecutive days of incident-free production operation under hypercare support.")

        # Risk, Issues & Health Check
        elif any(k in sec_lower for k in ['risk', 'threat']):
            return ("Overall Project Risk Assessment:\n"
                    "Overall risk is classified as 'Moderate-High' due to multi-system integration complexity and cross-departmental change impact. "
                    "Key mitigation actions include dedicated middleware squads, a phased regional rollout strategy (Pilot first), "
                    "a 10% contingency management reserve, and active weekly risk reviews with the executive steering board.")
        elif any(k in sec_lower for k in ['issue', 'impediment', 'blocker']):
            return ("Operational impediments have been cataloged and prioritized; vendor sandbox environment provisioning "
                    "has been expedited to ensure zero impact on critical path development sprint milestones.")

        # Requirements, Specifications & Assumptions
        elif any(k in sec_lower for k in ['requirement', 'specification']):
            return ("High-Level System & Business Requirements:\n"
                    "* Sub-second transaction response latency under peak load of 1,200 concurrent active users.\n"
                    "* Full compliance with national e-invoicing mandates and enterprise accounting standards.\n"
                    "* System availability SLA of >= 99.95% with Disaster Recovery Recovery Time Objective (RTO) < 2 hours.\n"
                    "* Role-based access control (RBAC), multi-factor authentication, and end-to-end audit logging.")
        elif any(k in sec_lower for k in ['assumption', 'constraint']):
            return ("Assumptions and Constraints:\n"
                    "* **Assumptions:** Subject matter experts (SMEs) are allocated at 25% dedicated capacity during Sprint cycles; external vendor API schemas remain stable.\n"
                    "* **Constraints:** Hard completion deadline prior to Q4 fiscal year close; pre-approved budget limit of $3.5M USD; mandatory adherence to corporate data protection guidelines.")

        # OCM, Training & Communication
        elif any(k in sec_lower for k in ['change', 'communication', 'training', 'adoption']):
            return ("Change Management & Stakeholder Enablement:\n"
                    "A structured Prosci ADKAR change campaign engages 450+ enterprise users across branches "
                    "via bi-weekly newsletters, hands-on sandbox labs, and train-the-trainer workshops, targeting >= 95% adoption at launch.")
        elif any(k in sec_lower for k in ['quality', 'audit', 'compliance']):
            return ("Quality Assurance & Governance Audit:\n"
                    "All deliverables are audited against PMO Stage-Gate quality gates, ISO 9001 quality standards, "
                    "and ISO 27001 cloud security protocols prior to executive milestone sign-off.")
        else:
            return ("This section has been thoroughly documented and validated in accordance with Apex Global Solutions "
                    "operational baseline and PMO delivery governance standards.")

def transform_template_to_example(raw_content: str, is_arabic: bool, title: str, doc_ref: str) -> str:
    """Accurately parses template structure and builds a complete reference example."""
    content = clean_template_comments(raw_content)
    content = replace_all_placeholders(content, is_arabic)
    
    # Specific handling for Resource Breakdown Structure (04_06_03)
    if "04.06.03" in doc_ref or "04_06_03" in title:
        if is_arabic:
            content = content.replace("| 1 | [ أضف التفاصيل... ] |", "| 1 | منظومة القمة لتخطيط الموارد (Nexus ERP) |")
            content = content.replace("| 1.1.1 | [ أضف التفاصيل... ] |", "| 1.1.1 | مهندسو الحلول والمعماريون السحابيون |")
            content = content.replace("| 1.1.2 | [ أضف التفاصيل... ] |", "| 1.1.2 | محللو الأعمال ومختبرو النظم |")
            content = content.replace("| 1.2.1 | [ أضف التفاصيل... ] |", "| 1.2.1 | خوادم الاختبار والتكامل السحابي |")
            content = content.replace("| 1.3.1 | [ أضف التفاصيل... ] |", "| 1.3.1 | تراخيص برمجيات المنظومة وقواعد البيانات |")
            content = content.replace("| 1.4.1 | [ أضف التفاصيل... ] |", "| 1.4.1 | اشتراكات التخزين السحابي وعروض النطاق |")
            content = content.replace("| 1.5.1 | [ أضف التفاصيل... ] |", "| 1.5.1 | مركز البيانات الرئيسي والشبكة الافتراضية VPC |")
            content = content.replace("**النوع:** [ أضف التفاصيل... ]", "**النوع:** هيكل شجري وظيفي ومكاني")
            content = content.replace("**التسمية:**\n[ أضف التفاصيل... ]", "**التسمية:** تصنيف خماسي المستويات يشمل الكوادر، المعدات، البرمجيات، والبيئات السحابية.")
            content = content.replace('PlaceholderP1["[ أضف التفاصيل... ]"]', 'PlaceholderP1["مهندسو الحلول والمعماريون"]')
            content = content.replace('PlaceholderP2["[ أضف التفاصيل... ]"]', 'PlaceholderP2["محللو الأعمال والمطورون"]')
            content = content.replace('PlaceholderE1["[ أضف التفاصيل... ]"]', 'PlaceholderE1["خوادم التطوير والاختبار"]')
            content = content.replace('PlaceholderE2["[ أضف التفاصيل... ]"]', 'PlaceholderE2["أجهزة القياس والربط الشبكي"]')
            content = content.replace('PlaceholderM1["[ أضف التفاصيل... ]"]', 'PlaceholderM1["تراخيص البرمجيات وقواعد البيانات"]')
            content = content.replace('PlaceholderM2["[ أضف التفاصيل... ]"]', 'PlaceholderM2["واجهات الربط البرمجي API"]')
            content = content.replace('PlaceholderS1["[ أضف التفاصيل... ]"]', 'PlaceholderS1["سعات التخزين السحابي"]')
            content = content.replace('PlaceholderS2["[ أضف التفاصيل... ]"]', 'PlaceholderS2["وحدات معالجة البيانات"]')
            content = content.replace('PlaceholderL1["[ أضف التفاصيل... ]"]', 'PlaceholderL1["مركز البيانات الرئيسي"]')
            content = content.replace('PlaceholderL2["[ أضف التفاصيل... ]"]', 'PlaceholderL2["البيئة السحابية الافتراضية VPC"]')
        else:
            content = content.replace("| 1 | [ Project Name ] |", "| 1 | Apex Enterprise Nexus ERP |")
            content = content.replace("| 1.1.1 | [ Add details... ] |", "| 1.1.1 | Solution Architects & Cloud Engineers |")
            content = content.replace("| 1.1.2 | [ Add details... ] |", "| 1.1.2 | Functional Analysts & QA Engineers |")
            content = content.replace("| 1.2.1 | [ Add details... ] |", "| 1.2.1 | Cloud Integration & Build Clusters |")
            content = content.replace("| 1.3.1 | [ Add details... ] |", "| 1.3.1 | SaaS Enterprise Licenses & Database Engine |")
            content = content.replace("| 1.4.1 | [ Add details... ] |", "| 1.4.1 | Cloud Storage & Compute Credits |")
            content = content.replace("| 1.5.1 | [ Add details... ] |", "| 1.5.1 | Primary Data Center & Virtual Staging VPC |")
            content = content.replace("**Chart Form:** [ Add details... ]", "**Chart Form:** Functional & Infrastructure Tree View")
            content = content.replace("**Node Labels:**\n[ Add details... ]", "**Node Labels:** 5-tier classification covering Personnel, Compute, Licensing, Storage, and Environments.")
            content = content.replace('PlaceholderP1["[ Add details... ]"]', 'PlaceholderP1["Solution Architects & Engineers"]')
            content = content.replace('PlaceholderP2["[ Add details... ]"]', 'PlaceholderP2["Business Analysts & QA Testers"]')
            content = content.replace('PlaceholderE1["[ Add details... ]"]', 'PlaceholderE1["Development & Test Build Clusters"]')
            content = content.replace('PlaceholderE2["[ Add details... ]"]', 'PlaceholderE2["Network Gateways & Security Appliances"]')
            content = content.replace('PlaceholderM1["[ Add details... ]"]', 'PlaceholderM1["Software & Database Licenses"]')
            content = content.replace('PlaceholderM2["[ Add details... ]"]', 'PlaceholderM2["API Connectors & Integration Adapters"]')
            content = content.replace('PlaceholderS1["[ Add details... ]"]', 'PlaceholderS1["Object Storage Credits"]')
            content = content.replace('PlaceholderS2["[ Add details... ]"]', 'PlaceholderS2["Compute Processing Capacity"]')
            content = content.replace('PlaceholderL1["[ Add details... ]"]', 'PlaceholderL1["Primary Cloud Region"]')
            content = content.replace('PlaceholderL2["[ Add details... ]"]', 'PlaceholderL2["Virtual Private Cloud (VPC)"]')

    # Dates and Signatures replacement
    content = re.sub(r'\[\s*\.\.\.\.\s*-\s*\.\.\.\.\s*-\s*\.\.\.\.\s*\]', '2026-03-18', content)
    content = re.sub(r'\[\s*\.\.\.\.\s*-\s*\.\.\.\.\s*\]', '2026-03-18', content)
    if is_arabic:
        content = re.sub(r'_{5,}', '[معتمد إلكترونياً]', content)
    else:
        content = re.sub(r'_{5,}', '[Electronically Signed]', content)

    lines = content.split('\n')
    output = []
    i = 0
    current_h2 = ""
    current_table_headers = []
    in_table = False
    table_row_idx = 0

    while i < len(lines):
        line = lines[i]
        line_str = line.strip()

        # Track H2 section
        if line_str.startswith('## '):
            current_h2 = line_str.replace('## ', '').strip()
            output.append(line)
            in_table = False
            current_table_headers = []
            table_row_idx = 0
            i += 1
            continue

        # Check for Table Header line (followed by divider)
        if line_str.startswith('|') and i + 1 < len(lines) and is_table_divider(lines[i+1].strip()):
            in_table = True
            table_row_idx = 0  # Reset row index for every individual table!
            current_table_headers = [c.strip() for c in line_str.split('|')[1:-1]]
            output.append(line)
            output.append(lines[i+1])
            i += 2
            continue

        # Process Table Body Rows
        if in_table and line_str.startswith('|'):
            cells = [c.strip() for c in line_str.split('|')[1:-1]]
            row_label = cells[0] if cells else ""
            
            new_cells = []
            for col_idx, cell in enumerate(cells):
                col_h = current_table_headers[col_idx] if col_idx < len(current_table_headers) else ""
                val = fill_table_cell(cell, row_label, col_h, current_h2, table_row_idx, is_arabic)
                new_cells.append(val)
                
            output.append("| " + " | ".join(new_cells) + " |")
            table_row_idx += 1
            i += 1
            continue

        if in_table and not line_str.startswith('|'):
            in_table = False
            current_table_headers = []
            table_row_idx = 0

        # Replace standalone narrative placeholder [ Add details... ] / [ أضف التفاصيل... ]
        if line_str == '[ Add details... ]' or line_str == '[ أضف التفاصيل... ]':
            narrative = fill_narrative_placeholder(current_h2, is_arabic)
            output.append(narrative)
            i += 1
            continue

        # Replace **Key:** [ Add details... ] or `* **Key:** [ Add details... ]`
        kv_match = re.match(r'^([\*\s-]*\*\*([^*]+)\*\*:?\s*)(?:\[\s*(?:Add details|أضف التفاصيل)[^\]]*\])$', line_str)
        if kv_match:
            prefix = kv_match.group(1)
            field_name = kv_match.group(2)
            val = get_field_value(field_name, is_arabic)
            output.append(f"{prefix}{val}")
            i += 1
            continue

        # Replace any remaining inline placeholder in bullet item
        if ('[ Add details' in line_str or '[ أضف' in line_str) and not line_str.startswith('|'):
            b_match = re.search(r'\*\*([^*]+)\*\*', line_str)
            if b_match:
                field_name = b_match.group(1)
                val = get_field_value(field_name, is_arabic)
                line = re.sub(r'\[\s*(?:Add details|أضف التفاصيل)[^\]]*\]', val, line_str)
            else:
                if is_arabic:
                    line = re.sub(r'\[\s*أضف التفاصيل[^\]]*\]', 'تم تحديده وتوثيقه بالتفصيل ليتوافق مع الخطة التشغيلية لشركة القمة.', line_str)
                else:
                    line = re.sub(r'\[\s*Add details[^\]]*\]', 'Fully defined and verified in accordance with Apex Global Solutions operational baseline.', line_str)
            output.append(line)
            i += 1
            continue

        output.append(line)
        i += 1

    result = '\n'.join(output)

    # Prepend Clean Gold Standard Banner
    clean_title = re.sub(r'^\d+(_\d+)*_', '', title).replace('_', ' ')
    if is_arabic:
        banner = (
            f"# {clean_title} (نموذج تطبيقي معبأ)\n"
            f"> 🏆 **نموذج استرشادي مكتمل (Gold Standard):** يوضح هذا المستند التطبيق العملي المتكامل "
            f"لهذا النموذج وفق معايير تسليمات (`{doc_ref}`). كافة الأسماء والبيانات الواردة هي لأغراض العرض التوضيحي والمحاكاة المؤسسية الفرضية.\n\n"
            f"---\n\n"
        )
        if "<div dir=\"rtl\">" in result:
            result = result.replace("<div dir=\"rtl\">", "<div dir=\"rtl\">\n\n" + banner, 1)
        else:
            result = banner + result
    else:
        banner = (
            f"# {clean_title} (Reference Example)\n"
            f"> 🏆 **Gold Standard Reference Example:** This document illustrates a fully completed, "
            f"production-grade artifact adhering to the Tasleemat PMO Framework (`{doc_ref}`). "
            f"All company names, project references, and figures are realistic fictional simulations.\n\n"
            f"---\n\n"
        )
        result = banner + result

    return result

def main():
    print("=== Re-generating all 102 English and 102 Arabic Examples with Exhaustive Domain Data ===")
    
    en_count = 0
    ar_count = 0
    
    # Process English Forms
    for root, dirs, files in os.walk(FORMS_EN_DIR):
        for f in files:
            if f.endswith('_Template.md'):
                rel_dir = os.path.relpath(root, FORMS_EN_DIR)
                target_dir = os.path.join(EXAMPLES_EN_DIR, rel_dir)
                os.makedirs(target_dir, exist_ok=True)
                
                src_path = os.path.join(root, f)
                example_name = f.replace('_Template.md', '_Example.md')
                dst_path = os.path.join(target_dir, example_name)
                
                doc_title = f.replace('_Template.md', '')
                doc_ref = "PMO-" + f[:5].replace('_', '.')
                
                with open(src_path, 'r', encoding='utf-8') as fp:
                    raw_content = fp.read()
                    
                example_content = transform_template_to_example(raw_content, is_arabic=False, title=doc_title, doc_ref=doc_ref)
                
                with open(dst_path, 'w', encoding='utf-8') as fp:
                    fp.write(example_content)
                en_count += 1

    # Process Arabic Forms
    for root, dirs, files in os.walk(FORMS_AR_DIR):
        for f in files:
            if f.endswith('_قالب.md'):
                rel_dir = os.path.relpath(root, FORMS_AR_DIR)
                target_dir = os.path.join(EXAMPLES_AR_DIR, rel_dir)
                os.makedirs(target_dir, exist_ok=True)
                
                src_path = os.path.join(root, f)
                example_name = f.replace('_قالب.md', '_مثال.md')
                dst_path = os.path.join(target_dir, example_name)
                
                doc_title = f.replace('_قالب.md', '')
                doc_ref = "PMO-" + f[:5].replace('_', '.')
                
                with open(src_path, 'r', encoding='utf-8') as fp:
                    raw_content = fp.read()
                    
                example_content = transform_template_to_example(raw_content, is_arabic=True, title=doc_title, doc_ref=doc_ref)
                
                with open(dst_path, 'w', encoding='utf-8') as fp:
                    fp.write(example_content)
                ar_count += 1

    print(f"Successfully generated {en_count} EN examples and {ar_count} AR examples.")

if __name__ == '__main__':
    main()
