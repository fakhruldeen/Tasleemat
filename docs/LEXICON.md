<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Bilingual Resource:</strong> Master Lexicon & Deliverables Catalog | المعجم الموحد للمصطلحات</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/docs/LEXICON.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
  </div>
</div>

</div>

</div>

</div>

<p align="center">
  <img src="img/logo.png" alt="Tasleemat PMO Toolkit Logo" width="280">
</p>

# Project Management Bilingual Lexicon & Forms Catalog
# المعجم الثنائي لإدارة المشاريع ودليل نماذج تسليمات

> **Standard Alignment:** PMI Lexicon of Project Management Terms, PMBOK® Guide (6th, 7th & 8th Edition Ready), and ISO 21500 / ISO 21502.

---

## 1. Directory & File Structure (أين تجد الملفات)

The repository is organized into a mirrored bilingual hierarchy:
- **English Forms (`en`):** Located in [`forms/en/`](forms/en/index.md)
- **Arabic Standardized Forms (`ar`):** Located in [`forms/ar/`](forms/ar/index.md)

### Form Bundle Structure (هيكل حزمة النموذج)
Each form directory contains exactly **5 synchronized files**:
1. `*_Template.md` / `*_قالب.md`: The fillable Markdown template with standard metadata header, structured input sections, and governance approval table.
2. `*_Guide.md` / `*_دليل.md`: Comprehensive practitioner guide explaining intent, section-by-section instructions, column definitions, and mandatory/optional upstream/downstream dependencies.
3. `*.md`: Generation prompt for LLM agents containing context, schema, and alignment rules.
4. `*.json`: Machine-readable data schema with sections, field labels, guidance, and default values.
5. `*.csv`: Tabular field reference matching the JSON schema (`Section`, `Field`, `Guidance`, `LLM_Generated_Value`).

---

## 2. Master Forms Catalog (فهرس النماذج الكامل - 102 نموذجاً)

| Document Code | English Form Name | Official Arabic Translation | English Location | Arabic Location |
| :--- | :--- | :--- | :--- | :--- |
| **PMO-00.01** | [Portfolio Roadmap](../forms/en/00_Program_and_Portfolio_Management/01_Portfolio_Roadmap) | [خارطة طريق المحفظة](../forms/ar/00_إدارة_البرامج_والمحافظ/01_خارطة_طريق_المحفظة) | `forms/en/00_Program_and_Portfolio_Management/01_Portfolio_Roadmap` | `forms/ar/00_إدارة_البرامج_والمحافظ/01_خارطة_طريق_المحفظة` |
| **PMO-00.02** | [Program Charter](../forms/en/00_Program_and_Portfolio_Management/02_Program_Charter) | [ميثاق البرنامج](../forms/ar/00_إدارة_البرامج_والمحافظ/02_ميثاق_البرنامج) | `forms/en/00_Program_and_Portfolio_Management/02_Program_Charter` | `forms/ar/00_إدارة_البرامج_والمحافظ/02_ميثاق_البرنامج` |
| **PMO-00.03** | [Interdependency Register](../forms/en/00_Program_and_Portfolio_Management/03_Interdependency_Register) | [سجل الاعتماديات المتبادلة](../forms/ar/00_إدارة_البرامج_والمحافظ/03_سجل_الاعتماديات_المتبادلة) | `forms/en/00_Program_and_Portfolio_Management/03_Interdependency_Register` | `forms/ar/00_إدارة_البرامج_والمحافظ/03_سجل_الاعتماديات_المتبادلة` |
| **PMO-00.04** | [Resource Capacity Matrix](../forms/en/00_Program_and_Portfolio_Management/04_Resource_Capacity_Matrix) | [مصفوفة سعة الموارد](../forms/ar/00_إدارة_البرامج_والمحافظ/04_مصفوفة_سعة_الموارد) | `forms/en/00_Program_and_Portfolio_Management/04_Resource_Capacity_Matrix` | `forms/ar/00_إدارة_البرامج_والمحافظ/04_مصفوفة_سعة_الموارد` |
| **PMO-00.05** | [PMO Maturity Assessment](../forms/en/00_Program_and_Portfolio_Management/05_PMO_Maturity_Assessment) | [تقييم نضج مكتب إدارة المشاريع](../forms/ar/00_إدارة_البرامج_والمحافظ/05_تقييم_نضج_مكتب_إدارة_المشاريع) | `forms/en/00_Program_and_Portfolio_Management/05_PMO_Maturity_Assessment` | `forms/ar/00_إدارة_البرامج_والمحافظ/05_تقييم_نضج_مكتب_إدارة_المشاريع` |
| **PMO-00.06** | [OKR Alignment Matrix](../forms/en/00_Program_and_Portfolio_Management/06_OKR_Alignment_Matrix) | [مصفوفة مواءمة الأهداف والنتائج الرئيسية](../forms/ar/00_إدارة_البرامج_والمحافظ/06_مصفوفة_مواءمة_الأهداف_والنتائج_الرئيسية) | `forms/en/00_Program_and_Portfolio_Management/06_OKR_Alignment_Matrix` | `forms/ar/00_إدارة_البرامج_والمحافظ/06_مصفوفة_مواءمة_الأهداف_والنتائج_الرئيسية` |
| **PMO-01.01** | [Business Case](../forms/en/01_Business_and_Value_Delivery/01_Business_Case) | [دراسة الجدوى](../forms/ar/01_الأعمال_وتسليم_القيمة/01_دراسة_الجدوى_(Business_Case)) | `forms/en/01_Business_and_Value_Delivery/01_Business_Case` | `forms/ar/01_الأعمال_وتسليم_القيمة/01_دراسة_الجدوى_(Business_Case)` |
| **PMO-01.02** | [Benefits Management Plan](../forms/en/01_Business_and_Value_Delivery/02_Benefits_Management_Plan) | [خطة إدارة الفوائد](../forms/ar/01_الأعمال_وتسليم_القيمة/02_خطة_إدارة_الفوائد) | `forms/en/01_Business_and_Value_Delivery/02_Benefits_Management_Plan` | `forms/ar/01_الأعمال_وتسليم_القيمة/02_خطة_إدارة_الفوائد` |
| **PMO-01.03** | [Value Realization Register](../forms/en/01_Business_and_Value_Delivery/03_Value_Realization_Register) | [سجل تحقيق القيمة](../forms/ar/01_الأعمال_وتسليم_القيمة/03_سجل_تحقيق_القيمة) | `forms/en/01_Business_and_Value_Delivery/03_Value_Realization_Register` | `forms/ar/01_الأعمال_وتسليم_القيمة/03_سجل_تحقيق_القيمة` |
| **PMO-01.04** | [Gap Analysis Report](../forms/en/01_Business_and_Value_Delivery/04_Gap_Analysis_Report) | [تقرير تحليل الفجوات](../forms/ar/01_الأعمال_وتسليم_القيمة/04_تقرير_تحليل_الفجوات) | `forms/en/01_Business_and_Value_Delivery/04_Gap_Analysis_Report` | `forms/ar/01_الأعمال_وتسليم_القيمة/04_تقرير_تحليل_الفجوات` |
| **PMO-02.01** | [Tailoring Plan](../forms/en/02_Project_Approach_and_Tailoring/01_Tailoring_Plan) | [خطة التخصيص](../forms/ar/02_منهجية_المشروع_وتخصيصه/01_خطة_التخصيص) | `forms/en/02_Project_Approach_and_Tailoring/01_Tailoring_Plan` | `forms/ar/02_منهجية_المشروع_وتخصيصه/01_خطة_التخصيص` |
| **PMO-02.02** | [AI GOVERNANCE PLAN](../forms/en/02_Project_Approach_and_Tailoring/02_AI_Governance_Plan) | [خطة حوكمة الذكاء الاصطناعي](../forms/ar/02_منهجية_المشروع_وتخصيصه/02_خطة_حوكمة_الذكاء_الاصطناعي) | `forms/en/02_Project_Approach_and_Tailoring/02_AI_Governance_Plan` | `forms/ar/02_منهجية_المشروع_وتخصيصه/02_خطة_حوكمة_الذكاء_الاصطناعي` |
| **PMO-02.03** | [AI Readiness Assessment](../forms/en/02_Project_Approach_and_Tailoring/03_AI_Readiness_Assessment) | [تقييم جاهزية الذكاء الاصطناعي](../forms/ar/02_منهجية_المشروع_وتخصيصه/03_تقييم_جاهزية_الذكاء_الاصطناعي) | `forms/en/02_Project_Approach_and_Tailoring/03_AI_Readiness_Assessment` | `forms/ar/02_منهجية_المشروع_وتخصيصه/03_تقييم_جاهزية_الذكاء_الاصطناعي` |
| **PMO-02.04** | [AI Use Case Canvas](../forms/en/02_Project_Approach_and_Tailoring/04_AI_Use_Case_Canvas) | [نموذج حالة استخدام الذكاء الاصطناعي](../forms/ar/02_منهجية_المشروع_وتخصيصه/04_نموذج_حالة_استخدام_الذكاء_الاصطناعي) | `forms/en/02_Project_Approach_and_Tailoring/04_AI_Use_Case_Canvas` | `forms/ar/02_منهجية_المشروع_وتخصيصه/04_نموذج_حالة_استخدام_الذكاء_الاصطناعي` |
| **PMO-02.05** | [AI MODEL CARD AND FACT SHEET](../forms/en/02_Project_Approach_and_Tailoring/05_AI_Model_Card_and_Fact_Sheet) | [بطاقة نموذج الذكاء الاصطناعي](../forms/ar/02_منهجية_المشروع_وتخصيصه/05_بطاقة_نموذج_الذكاء_الاصطناعي) | `forms/en/02_Project_Approach_and_Tailoring/05_AI_Model_Card_and_Fact_Sheet` | `forms/ar/02_منهجية_المشروع_وتخصيصه/05_بطاقة_نموذج_الذكاء_الاصطناعي` |
| **PMO-02.06** | [DATA PRIVACY AND ETHICS ASSESSMENT](../forms/en/02_Project_Approach_and_Tailoring/06_Data_Privacy_and_Ethics_Assessment) | [تقييم خصوصية البيانات وأخلاقياتها](../forms/ar/02_منهجية_المشروع_وتخصيصه/06_تقييم_خصوصية_البيانات_وأخلاقياتها) | `forms/en/02_Project_Approach_and_Tailoring/06_Data_Privacy_and_Ethics_Assessment` | `forms/ar/02_منهجية_المشروع_وتخصيصه/06_تقييم_خصوصية_البيانات_وأخلاقياتها` |
| **PMO-03.01** | [PROJECT CHARTER](../forms/en/03_Initiating/01_Project_Charter) | [ميثاق المشروع](../forms/ar/03_البدء/01_ميثاق_المشروع) | `forms/en/03_Initiating/01_Project_Charter` | `forms/ar/03_البدء/01_ميثاق_المشروع` |
| **PMO-03.02** | [PRODUCT VISION](../forms/en/03_Initiating/02_Product_Vision) | [بيان رؤية المنتج](../forms/ar/03_البدء/02_رؤية_المنتج) | `forms/en/03_Initiating/02_Product_Vision` | `forms/ar/03_البدء/02_رؤية_المنتج` |
| **PMO-03.03** | [ASSUMPTION LOG](../forms/en/03_Initiating/03_Assumption_Log) | [سجل الافتراضات](../forms/ar/03_البدء/03_سجل_الافتراضات) | `forms/en/03_Initiating/03_Assumption_Log` | `forms/ar/03_البدء/03_سجل_الافتراضات` |
| **PMO-03.04** | [Stakeholder Register](../forms/en/03_Initiating/04_Stakeholder_Register) | [سجل المعنيين](../forms/ar/03_البدء/04_سجل_المعنيين) | `forms/en/03_Initiating/04_Stakeholder_Register` | `forms/ar/03_البدء/04_سجل_المعنيين` |
| **PMO-03.05** | [STAKEHOLDER ANALYSIS](../forms/en/03_Initiating/05_Stakeholder_Analysis) | [تحليل المعنيين](../forms/ar/03_البدء/05_تحليل_المعنيين) | `forms/en/03_Initiating/05_Stakeholder_Analysis` | `forms/ar/03_البدء/05_تحليل_المعنيين` |
| **PMO-04.01.01** | [PROJECT MANAGEMENT PLAN](../forms/en/04_Planning/01_Integration/01_Project_Management_Plan) | [خطة إدارة المشروع](../forms/ar/04_التخطيط/01_التكامل/01_خطة_إدارة_المشروع) | `forms/en/04_Planning/01_Integration/01_Project_Management_Plan` | `forms/ar/04_التخطيط/01_التكامل/01_خطة_إدارة_المشروع` |
| **PMO-04.01.02** | [CHANGE MANAGEMENT PLAN](../forms/en/04_Planning/01_Integration/02_Change_Management_Plan) | [خطة إدارة التغيير](../forms/ar/04_التخطيط/01_التكامل/02_خطة_إدارة_التغيير) | `forms/en/04_Planning/01_Integration/02_Change_Management_Plan` | `forms/ar/04_التخطيط/01_التكامل/02_خطة_إدارة_التغيير` |
| **PMO-04.01.03** | [PROJECT ROADMAP](../forms/en/04_Planning/01_Integration/03_Project_Roadmap) | [خارطة طريق المشروع](../forms/ar/04_التخطيط/01_التكامل/03_خارطة_طريق_المشروع) | `forms/en/04_Planning/01_Integration/03_Project_Roadmap` | `forms/ar/04_التخطيط/01_التكامل/03_خارطة_طريق_المشروع` |
| **PMO-04.02.01** | [SCOPE MANAGEMENT PLAN](../forms/en/04_Planning/02_Scope/01_Scope_Management_Plan) | [خطة إدارة النطاق](../forms/ar/04_التخطيط/02_النطاق/01_خطة_إدارة_النطاق) | `forms/en/04_Planning/02_Scope/01_Scope_Management_Plan` | `forms/ar/04_التخطيط/02_النطاق/01_خطة_إدارة_النطاق` |
| **PMO-04.02.02** | [REQUIREMENTS MANAGEMENT PLAN](../forms/en/04_Planning/02_Scope/02_Requirements_Management_Plan) | [خطة إدارة المتطلبات](../forms/ar/04_التخطيط/02_النطاق/02_خطة_إدارة_المتطلبات) | `forms/en/04_Planning/02_Scope/02_Requirements_Management_Plan` | `forms/ar/04_التخطيط/02_النطاق/02_خطة_إدارة_المتطلبات` |
| **PMO-04.02.03** | [REQUIREMENTS DOCUMENTATION](../forms/en/04_Planning/02_Scope/03_Requirements_Documentation) | [وثائق المتطلبات](../forms/ar/04_التخطيط/02_النطاق/03_وثائق_المتطلبات) | `forms/en/04_Planning/02_Scope/03_Requirements_Documentation` | `forms/ar/04_التخطيط/02_النطاق/03_وثائق_المتطلبات` |
| **PMO-04.02.04** | [REQUIREMENTS TRACEABILITY MATRIX](../forms/en/04_Planning/02_Scope/04_Requirements_Traceability_Matrix) | [مصفوفة تتبع المتطلبات](../forms/ar/04_التخطيط/02_النطاق/04_مصفوفة_تتبع_المتطلبات) | `forms/en/04_Planning/02_Scope/04_Requirements_Traceability_Matrix` | `forms/ar/04_التخطيط/02_النطاق/04_مصفوفة_تتبع_المتطلبات` |
| **PMO-04.02.05** | [PROJECT SCOPE STATEMENT](../forms/en/04_Planning/02_Scope/05_Project_Scope_Statement) | [بيان نطاق المشروع](../forms/ar/04_التخطيط/02_النطاق/05_بيان_نطاق_المشروع) | `forms/en/04_Planning/02_Scope/05_Project_Scope_Statement` | `forms/ar/04_التخطيط/02_النطاق/05_بيان_نطاق_المشروع` |
| **PMO-04.02.06** | [WORK BREAKDOWN STRUCTURE](../forms/en/04_Planning/02_Scope/06_Work_Breakdown_Structure) | [هيكل تجزئة العمل](../forms/ar/04_التخطيط/02_النطاق/06_هيكل_تجزئة_العمل) | `forms/en/04_Planning/02_Scope/06_Work_Breakdown_Structure` | `forms/ar/04_التخطيط/02_النطاق/06_هيكل_تجزئة_العمل` |
| **PMO-04.02.07** | [WBS DICTIONARY](../forms/en/04_Planning/02_Scope/07_WBS_Dictionary) | [قاموس هيكل تجزئة العمل](../forms/ar/04_التخطيط/02_النطاق/07_قاموس_هيكل_تجزئة_العمل) | `forms/en/04_Planning/02_Scope/07_WBS_Dictionary` | `forms/ar/04_التخطيط/02_النطاق/07_قاموس_هيكل_تجزئة_العمل` |
| **PMO-04.02.08** | [PRODUCT BACKLOG](../forms/en/04_Planning/02_Scope/08_Product_Backlog) | [قائمة تراكم المنتج](../forms/ar/04_التخطيط/02_النطاق/08_قائمة_تراكم_المنتج_(Product_Backlog)) | `forms/en/04_Planning/02_Scope/08_Product_Backlog` | `forms/ar/04_التخطيط/02_النطاق/08_قائمة_تراكم_المنتج_(Product_Backlog)` |
| **PMO-04.02.09** | [USER STORY MAPPING CANVAS](../forms/en/04_Planning/02_Scope/09_User_Story_Mapping_Canvas) | [نموذج تخطيط قصص المستخدم](../forms/ar/04_التخطيط/02_النطاق/09_نموذج_تخطيط_قصص_المستخدم) | `forms/en/04_Planning/02_Scope/09_User_Story_Mapping_Canvas` | `forms/ar/04_التخطيط/02_النطاق/09_نموذج_تخطيط_قصص_المستخدم` |
| **PMO-04.03.01** | [SCHEDULE MANAGEMENT PLAN](../forms/en/04_Planning/03_Schedule/01_Schedule_Management_Plan) | [خطة إدارة الجدول الزمني](../forms/ar/04_التخطيط/03_الجدول_الزمني/01_خطة_إدارة_الجدول_الزمني) | `forms/en/04_Planning/03_Schedule/01_Schedule_Management_Plan` | `forms/ar/04_التخطيط/03_الجدول_الزمني/01_خطة_إدارة_الجدول_الزمني` |
| **PMO-04.03.02** | [ACTIVITY LIST](../forms/en/04_Planning/03_Schedule/02_Activity_List) | [قائمة الأنشطة](../forms/ar/04_التخطيط/03_الجدول_الزمني/02_قائمة_الأنشطة) | `forms/en/04_Planning/03_Schedule/02_Activity_List` | `forms/ar/04_التخطيط/03_الجدول_الزمني/02_قائمة_الأنشطة` |
| **PMO-04.03.03** | [ACTIVITY ATTRIBUTES](../forms/en/04_Planning/03_Schedule/03_Activity_Attributes) | [سمات النشاط](../forms/ar/04_التخطيط/03_الجدول_الزمني/03_سمات_النشاط) | `forms/en/04_Planning/03_Schedule/03_Activity_Attributes` | `forms/ar/04_التخطيط/03_الجدول_الزمني/03_سمات_النشاط` |
| **PMO-04.03.04** | [MILESTONE LIST](../forms/en/04_Planning/03_Schedule/04_Milestone_List) | [قائمة المعالم](../forms/ar/04_التخطيط/03_الجدول_الزمني/04_قائمة_المعالم_(Milestones)) | `forms/en/04_Planning/03_Schedule/04_Milestone_List` | `forms/ar/04_التخطيط/03_الجدول_الزمني/04_قائمة_المعالم_(Milestones)` |
| **PMO-04.03.05** | [NETWORK DIAGRAM](../forms/en/04_Planning/03_Schedule/05_Network_Diagram) | [المخطط الشبكي](../forms/ar/04_التخطيط/03_الجدول_الزمني/05_المخطط_الشبكي) | `forms/en/04_Planning/03_Schedule/05_Network_Diagram` | `forms/ar/04_التخطيط/03_الجدول_الزمني/05_المخطط_الشبكي` |
| **PMO-04.03.06** | [DURATION ESTIMATES](../forms/en/04_Planning/03_Schedule/06_Duration_Estimates) | [تقديرات المدة](../forms/ar/04_التخطيط/03_الجدول_الزمني/06_تقديرات_المدة) | `forms/en/04_Planning/03_Schedule/06_Duration_Estimates` | `forms/ar/04_التخطيط/03_الجدول_الزمني/06_تقديرات_المدة` |
| **PMO-04.03.07** | [DURATION ESTIMATING WORKSHEET](../forms/en/04_Planning/03_Schedule/07_Duration_Estimating_Worksheet) | [ورقة عمل تقدير المدة](../forms/ar/04_التخطيط/03_الجدول_الزمني/07_ورقة_عمل_تقدير_المدة) | `forms/en/04_Planning/03_Schedule/07_Duration_Estimating_Worksheet` | `forms/ar/04_التخطيط/03_الجدول_الزمني/07_ورقة_عمل_تقدير_المدة` |
| **PMO-04.03.08** | [PROJECT SCHEDULE](../forms/en/04_Planning/03_Schedule/08_Project_Schedule) | [الجدول الزمني للمشروع](../forms/ar/04_التخطيط/03_الجدول_الزمني/08_الجدول_الزمني_للمشروع) | `forms/en/04_Planning/03_Schedule/08_Project_Schedule` | `forms/ar/04_التخطيط/03_الجدول_الزمني/08_الجدول_الزمني_للمشروع` |
| **PMO-04.03.09** | [RELEASE PLAN](../forms/en/04_Planning/03_Schedule/09_Release_Plan) | [خطة الإصدار](../forms/ar/04_التخطيط/03_الجدول_الزمني/09_خطة_الإصدار) | `forms/en/04_Planning/03_Schedule/09_Release_Plan` | `forms/ar/04_التخطيط/03_الجدول_الزمني/09_خطة_الإصدار` |
| **PMO-04.03.10** | [SPRINT PLANNING LOG](../forms/en/04_Planning/03_Schedule/10_Sprint_Planning_Log) | [سجل تخطيط دورة تطوير](../forms/ar/04_التخطيط/03_الجدول_الزمني/10_سجل_تخطيط_أسبوع_العمل) | `forms/en/04_Planning/03_Schedule/10_Sprint_Planning_Log` | `forms/ar/04_التخطيط/03_الجدول_الزمني/10_سجل_تخطيط_أسبوع_العمل` |
| **PMO-04.04.01** | [COST MANAGEMENT PLAN](../forms/en/04_Planning/04_Cost/01_Cost_Management_Plan) | [خطة إدارة التكلفة](../forms/ar/04_التخطيط/04_التكلفة/01_خطة_إدارة_التكلفة) | `forms/en/04_Planning/04_Cost/01_Cost_Management_Plan` | `forms/ar/04_التخطيط/04_التكلفة/01_خطة_إدارة_التكلفة` |
| **PMO-04.04.02** | [COST ESTIMATES](../forms/en/04_Planning/04_Cost/02_Cost_Estimates) | [تقديرات التكلفة](../forms/ar/04_التخطيط/04_التكلفة/02_تقديرات_التكلفة) | `forms/en/04_Planning/04_Cost/02_Cost_Estimates` | `forms/ar/04_التخطيط/04_التكلفة/02_تقديرات_التكلفة` |
| **PMO-04.04.03** | [COST ESTIMATING WORKSHEET](../forms/en/04_Planning/04_Cost/03_Cost_Estimating_Worksheet) | [ورقة عمل تقدير التكلفة](../forms/ar/04_التخطيط/04_التكلفة/03_ورقة_عمل_تقدير_التكلفة) | `forms/en/04_Planning/04_Cost/03_Cost_Estimating_Worksheet` | `forms/ar/04_التخطيط/04_التكلفة/03_ورقة_عمل_تقدير_التكلفة` |
| **PMO-04.04.04** | [COST BASELINE](../forms/en/04_Planning/04_Cost/04_Cost_Baseline) | [الخط المرجعي للتكلفة](../forms/ar/04_التخطيط/04_التكلفة/04_الخط_المرجعي_للتكلفة) | `forms/en/04_Planning/04_Cost/04_Cost_Baseline` | `forms/ar/04_التخطيط/04_التكلفة/04_الخط_المرجعي_للتكلفة` |
| **PMO-04.05.01** | [QUALITY MANAGEMENT PLAN](../forms/en/04_Planning/05_Quality/01_Quality_Management_Plan) | [خطة إدارة الجودة](../forms/ar/04_التخطيط/05_الجودة/01_خطة_إدارة_الجودة) | `forms/en/04_Planning/05_Quality/01_Quality_Management_Plan` | `forms/ar/04_التخطيط/05_الجودة/01_خطة_إدارة_الجودة` |
| **PMO-04.05.02** | [QUALITY METRICS](../forms/en/04_Planning/05_Quality/02_Quality_Metrics) | [مقاييس الجودة](../forms/ar/04_التخطيط/05_الجودة/02_مقاييس_الجودة) | `forms/en/04_Planning/05_Quality/02_Quality_Metrics` | `forms/ar/04_التخطيط/05_الجودة/02_مقاييس_الجودة` |
| **PMO-04.05.03** | [Definition of Ready and Done Standard](../forms/en/04_Planning/05_Quality/03_Definition_of_Ready_and_Done) | [تعريف الجاهزية والاكتمال](../forms/ar/04_التخطيط/05_الجودة/03_تعريف_الجاهزية_والاكتمال) | `forms/en/04_Planning/05_Quality/03_Definition_of_Ready_and_Done` | `forms/ar/04_التخطيط/05_الجودة/03_تعريف_الجاهزية_والاكتمال` |
| **PMO-04.06.01** | [RESOURCE MANAGEMENT PLAN](../forms/en/04_Planning/06_Resource/01_Resource_Management_Plan) | [خطة إدارة الموارد](../forms/ar/04_التخطيط/06_الموارد/01_خطة_إدارة_الموارد) | `forms/en/04_Planning/06_Resource/01_Resource_Management_Plan` | `forms/ar/04_التخطيط/06_الموارد/01_خطة_إدارة_الموارد` |
| **PMO-04.06.02** | [RESOURCE REQUIREMENTS](../forms/en/04_Planning/06_Resource/02_Resource_Requirements) | [متطلبات الموارد](../forms/ar/04_التخطيط/06_الموارد/02_متطلبات_الموارد) | `forms/en/04_Planning/06_Resource/02_Resource_Requirements` | `forms/ar/04_التخطيط/06_الموارد/02_متطلبات_الموارد` |
| **PMO-04.06.03** | [RESOURCE BREAKDOWN STRUCTURE](../forms/en/04_Planning/06_Resource/03_Resource_Breakdown_Structure) | [هيكل تجزئة الموارد](../forms/ar/04_التخطيط/06_الموارد/03_هيكل_تجزئة_الموارد_(RBS)) | `forms/en/04_Planning/06_Resource/03_Resource_Breakdown_Structure` | `forms/ar/04_التخطيط/06_الموارد/03_هيكل_تجزئة_الموارد_(RBS)` |
| **PMO-04.06.04** | [RESPONSIBILITY ASSIGNMENT MATRIX](../forms/en/04_Planning/06_Resource/04_Responsibility_Assignment_Matrix) | [مصفوفة تعيين المسؤوليات](../forms/ar/04_التخطيط/06_الموارد/04_مصفوفة_تعيين_المسؤوليات_(RAM)) | `forms/en/04_Planning/06_Resource/04_Responsibility_Assignment_Matrix` | `forms/ar/04_التخطيط/06_الموارد/04_مصفوفة_تعيين_المسؤوليات_(RAM)` |
| **PMO-04.06.05** | [TEAM CHARTER](../forms/en/04_Planning/06_Resource/05_Team_Charter) | [ميثاق الفريق](../forms/ar/04_التخطيط/06_الموارد/05_ميثاق_الفريق) | `forms/en/04_Planning/06_Resource/05_Team_Charter` | `forms/ar/04_التخطيط/06_الموارد/05_ميثاق_الفريق` |
| **PMO-04.07.01** | [COMMUNICATIONS MANAGEMENT PLAN](../forms/en/04_Planning/07_Communications/01_Communications_Management_Plan) | [خطة إدارة الاتصالات](../forms/ar/04_التخطيط/07_التواصل/01_خطة_إدارة_الاتصالات) | `forms/en/04_Planning/07_Communications/01_Communications_Management_Plan` | `forms/ar/04_التخطيط/07_التواصل/01_خطة_إدارة_الاتصالات` |
| **PMO-04.08.01** | [RISK MANAGEMENT PLAN](../forms/en/04_Planning/08_Risk/01_Risk_Management_Plan) | [خطة إدارة المخاطر](../forms/ar/04_التخطيط/08_المخاطر/01_خطة_إدارة_المخاطر) | `forms/en/04_Planning/08_Risk/01_Risk_Management_Plan` | `forms/ar/04_التخطيط/08_المخاطر/01_خطة_إدارة_المخاطر` |
| **PMO-04.08.02** | [RISK REGISTER](../forms/en/04_Planning/08_Risk/02_Risk_Register) | [سجل المخاطر](../forms/ar/04_التخطيط/08_المخاطر/02_سجل_المخاطر) | `forms/en/04_Planning/08_Risk/02_Risk_Register` | `forms/ar/04_التخطيط/08_المخاطر/02_سجل_المخاطر` |
| **PMO-04.08.03** | [PROBABILITY AND IMPACT ASSESSMENT](../forms/en/04_Planning/08_Risk/03_Probability_and_Impact_Assessment) | [تقييم الاحتمالية والأثر](../forms/ar/04_التخطيط/08_المخاطر/03_تقييم_الاحتمالية_والأثر) | `forms/en/04_Planning/08_Risk/03_Probability_and_Impact_Assessment` | `forms/ar/04_التخطيط/08_المخاطر/03_تقييم_الاحتمالية_والأثر` |
| **PMO-04.08.04** | [PROBABILITY AND IMPACT MATRIX](../forms/en/04_Planning/08_Risk/04_Probability_and_Impact_Matrix) | [مصفوفة الاحتمالية والأثر](../forms/ar/04_التخطيط/08_المخاطر/04_مصفوفة_الاحتمالية_والأثر) | `forms/en/04_Planning/08_Risk/04_Probability_and_Impact_Matrix` | `forms/ar/04_التخطيط/08_المخاطر/04_مصفوفة_الاحتمالية_والأثر` |
| **PMO-04.08.05** | [RISK DATA SHEET](../forms/en/04_Planning/08_Risk/05_Risk_Data_Sheet) | [ورقة بيانات المخاطر](../forms/ar/04_التخطيط/08_المخاطر/05_ورقة_بيانات_المخاطر) | `forms/en/04_Planning/08_Risk/05_Risk_Data_Sheet` | `forms/ar/04_التخطيط/08_المخاطر/05_ورقة_بيانات_المخاطر` |
| **PMO-04.08.06** | [RISK REPORT](../forms/en/04_Planning/08_Risk/06_Risk_Report) | [تقرير المخاطر](../forms/ar/04_التخطيط/08_المخاطر/06_تقرير_المخاطر) | `forms/en/04_Planning/08_Risk/06_Risk_Report` | `forms/ar/04_التخطيط/08_المخاطر/06_تقرير_المخاطر` |
| **PMO-04.08.07** | [RISK MITIGATION ACTION PLAN](../forms/en/04_Planning/08_Risk/07_Risk_Mitigation_Action_Plan) | [خطة عمل التخفيف من المخاطر](../forms/ar/04_التخطيط/08_المخاطر/07_خطة_عمل_التخفيف_من_المخاطر) | `forms/en/04_Planning/08_Risk/07_Risk_Mitigation_Action_Plan` | `forms/ar/04_التخطيط/08_المخاطر/07_خطة_عمل_التخفيف_من_المخاطر` |
| **PMO-04.09.01** | [PROCUREMENT MANAGEMENT PLAN](../forms/en/04_Planning/09_Procurement/01_Procurement_Management_Plan) | [خطة إدارة المشتريات](../forms/ar/04_التخطيط/09_المشتريات/01_خطة_إدارة_المشتريات) | `forms/en/04_Planning/09_Procurement/01_Procurement_Management_Plan` | `forms/ar/04_التخطيط/09_المشتريات/01_خطة_إدارة_المشتريات` |
| **PMO-04.09.02** | [PROCUREMENT STRATEGY](../forms/en/04_Planning/09_Procurement/02_Procurement_Strategy) | [استراتيجية المشتريات](../forms/ar/04_التخطيط/09_المشتريات/02_استراتيجية_المشتريات) | `forms/en/04_Planning/09_Procurement/02_Procurement_Strategy` | `forms/ar/04_التخطيط/09_المشتريات/02_استراتيجية_المشتريات` |
| **PMO-04.09.03** | [SOURCE SELECTION CRITERIA](../forms/en/04_Planning/09_Procurement/03_Source_Selection_Criteria) | [معايير اختيار المصدر](../forms/ar/04_التخطيط/09_المشتريات/03_معايير_اختيار_المصدر) | `forms/en/04_Planning/09_Procurement/03_Source_Selection_Criteria` | `forms/ar/04_التخطيط/09_المشتريات/03_معايير_اختيار_المصدر` |
| **PMO-04.09.04** | [Statement of Work](../forms/en/04_Planning/09_Procurement/04_Statement_of_Work_SOW) | [بيان العمل](../forms/ar/04_التخطيط/09_المشتريات/04_بيان_العمل_(SOW)) | `forms/en/04_Planning/09_Procurement/04_Statement_of_Work_SOW` | `forms/ar/04_التخطيط/09_المشتريات/04_بيان_العمل_(SOW)` |
| **PMO-04.09.05** | [Request for Proposal](../forms/en/04_Planning/09_Procurement/05_Request_for_Proposal_RFP) | [طلب تقديم العروض](../forms/ar/04_التخطيط/09_المشتريات/05_طلب_تقديم_عروض_(RFP)) | `forms/en/04_Planning/09_Procurement/05_Request_for_Proposal_RFP` | `forms/ar/04_التخطيط/09_المشتريات/05_طلب_تقديم_عروض_(RFP)` |
| **PMO-04.10.01** | [STAKEHOLDER ENGAGEMENT PLAN](../forms/en/04_Planning/10_Stakeholder/01_Stakeholder_Engagement_Plan) | [خطة إشراك المعنيين](../forms/ar/04_التخطيط/10_المعنيين/01_خطة_إشراك_المعنيين) | `forms/en/04_Planning/10_Stakeholder/01_Stakeholder_Engagement_Plan` | `forms/ar/04_التخطيط/10_المعنيين/01_خطة_إشراك_المعنيين` |
| **PMO-04.11.01** | [OCM Strategy and Plan](../forms/en/04_Planning/11_Organizational_Change_Management/01_OCM_Strategy_and_Plan) | [استراتيجية وخطة إدارة التغيير المؤسسي](../forms/ar/04_التخطيط/11_إدارة_التغيير_المؤسسي/01_استراتيجية_وخطة_إدارة_التغيير_المؤسسي) | `forms/en/04_Planning/11_Organizational_Change_Management/01_OCM_Strategy_and_Plan` | `forms/ar/04_التخطيط/11_إدارة_التغيير_المؤسسي/01_استراتيجية_وخطة_إدارة_التغيير_المؤسسي` |
| **PMO-04.11.02** | [Training Plan and Log](../forms/en/04_Planning/11_Organizational_Change_Management/02_Training_Plan_and_Log) | [خطة وسجل التدريب](../forms/ar/04_التخطيط/11_إدارة_التغيير_المؤسسي/02_خطة_وسجل_التدريب) | `forms/en/04_Planning/11_Organizational_Change_Management/02_Training_Plan_and_Log` | `forms/ar/04_التخطيط/11_إدارة_التغيير_المؤسسي/02_خطة_وسجل_التدريب` |
| **PMO-04.12.01** | [Sustainability and ESG Management Plan](../forms/en/04_Planning/12_Sustainability_and_ESG/01_Sustainability_and_ESG_Management_Plan) | [خطة إدارة الاستدامة والمعايير البيئية والاجتماعية والحوكمة](../forms/ar/04_التخطيط/12_الاستدامة_والمعايير_البيئية_والاجتماعية_والحوكمة/01_خطة_إدارة_الاستدامة_والمعايير_البيئية_والاجتماعية_والحوكمة) | `forms/en/04_Planning/12_Sustainability_and_ESG/01_Sustainability_and_ESG_Management_Plan` | `forms/ar/04_التخطيط/12_الاستدامة_والمعايير_البيئية_والاجتماعية_والحوكمة/01_خطة_إدارة_الاستدامة_والمعايير_البيئية_والاجتماعية_والحوكمة` |
| **PMO-05.01** | [ISSUE LOG](../forms/en/05_Executing/01_Issue_Log) | [سجل المشكلات](../forms/ar/05_التنفيذ/01_سجل_المشكلات) | `forms/en/05_Executing/01_Issue_Log` | `forms/ar/05_التنفيذ/01_سجل_المشكلات` |
| **PMO-05.02** | [DECISION LOG](../forms/en/05_Executing/02_Decision_Log) | [سجل القرارات](../forms/ar/05_التنفيذ/02_سجل_القرارات) | `forms/en/05_Executing/02_Decision_Log` | `forms/ar/05_التنفيذ/02_سجل_القرارات` |
| **PMO-05.03** | [CHANGE REQUEST](../forms/en/05_Executing/03_Change_Request) | [طلب تغيير](../forms/ar/05_التنفيذ/03_طلب_تغيير) | `forms/en/05_Executing/03_Change_Request` | `forms/ar/05_التنفيذ/03_طلب_تغيير` |
| **PMO-05.04** | [CHANGE LOG](../forms/en/05_Executing/04_Change_Log) | [سجل التغييرات](../forms/ar/05_التنفيذ/04_سجل_التغييرات) | `forms/en/05_Executing/04_Change_Log` | `forms/ar/05_التنفيذ/04_سجل_التغييرات` |
| **PMO-05.05** | [QUALITY AUDIT REPORT](../forms/en/05_Executing/05_Quality_Audit) | [تقرير تدقيق الجودة](../forms/ar/05_التنفيذ/05_تدقيق_الجودة) | `forms/en/05_Executing/05_Quality_Audit` | `forms/ar/05_التنفيذ/05_تدقيق_الجودة` |
| **PMO-05.06** | [TEAM PERFORMANCE ASSESSMENT](../forms/en/05_Executing/06_Team_Performance_Assessment) | [تقييم أداء الفريق](../forms/ar/05_التنفيذ/06_تقييم_أداء_الفريق) | `forms/en/05_Executing/06_Team_Performance_Assessment` | `forms/ar/05_التنفيذ/06_تقييم_أداء_الفريق` |
| **PMO-05.07** | [LESSONS LEARNED REGISTER](../forms/en/05_Executing/07_Lessons_Learned_Register) | [سجل الدروس المستفادة](../forms/ar/05_التنفيذ/07_سجل_الدروس_المستفادة) | `forms/en/05_Executing/07_Lessons_Learned_Register` | `forms/ar/05_التنفيذ/07_سجل_الدروس_المستفادة` |
| **PMO-05.08** | [RETROSPECTIVE](../forms/en/05_Executing/08_Retrospective) | [مراجعة المرحلة](../forms/ar/05_التنفيذ/08_مراجعة_المرحلة_(Retrospective)) | `forms/en/05_Executing/08_Retrospective` | `forms/ar/05_التنفيذ/08_مراجعة_المرحلة_(Retrospective)` |
| **PMO-05.09** | [Prompt Library Log](../forms/en/05_Executing/09_Prompt_Library_Log) | [سجل مكتبة الأوامر](../forms/ar/05_التنفيذ/09_سجل_مكتبة_الأوامر_(Prompts)) | `forms/en/05_Executing/09_Prompt_Library_Log` | `forms/ar/05_التنفيذ/09_سجل_مكتبة_الأوامر_(Prompts)` |
| **PMO-05.10** | [Impediment Log](../forms/en/05_Executing/10_Impediment_Log) | [سجل العوائق](../forms/ar/05_التنفيذ/10_سجل_العوائق) | `forms/en/05_Executing/10_Impediment_Log` | `forms/ar/05_التنفيذ/10_سجل_العوائق` |
| **PMO-05.11** | [Meeting Minutes](../forms/en/05_Executing/11_Meeting_Minutes) | [محضر الاجتماع](../forms/ar/05_التنفيذ/11_محضر_الاجتماع) | `forms/en/05_Executing/11_Meeting_Minutes` | `forms/ar/05_التنفيذ/11_محضر_الاجتماع` |
| **PMO-05.12** | [Team Onboarding Checklist](../forms/en/05_Executing/12_Team_Onboarding_Checklist) | [قائمة التحقق لتهيئة فريق العمل](../forms/ar/05_التنفيذ/12_قائمة_التحقق_لتهيئة_فريق_العمل) | `forms/en/05_Executing/12_Team_Onboarding_Checklist` | `forms/ar/05_التنفيذ/12_قائمة_التحقق_لتهيئة_فريق_العمل` |
| **PMO-06.01** | [PROJECT STATUS REPORT](../forms/en/06_Monitoring_and_Controlling/01_Project_Status_Report) | [تقرير حالة المشروع](../forms/ar/06_المراقبة_والتحكم/01_تقرير_حالة_المشروع) | `forms/en/06_Monitoring_and_Controlling/01_Project_Status_Report` | `forms/ar/06_المراقبة_والتحكم/01_تقرير_حالة_المشروع` |
| **PMO-06.02** | [TEAM MEMBER STATUS REPORT](../forms/en/06_Monitoring_and_Controlling/02_Team_Member_Status_Report) | [تقرير حالة عضو الفريق](../forms/ar/06_المراقبة_والتحكم/02_تقرير_حالة_عضو_الفريق) | `forms/en/06_Monitoring_and_Controlling/02_Team_Member_Status_Report` | `forms/ar/06_المراقبة_والتحكم/02_تقرير_حالة_عضو_الفريق` |
| **PMO-06.03** | [CONTRACTOR STATUS REPORT](../forms/en/06_Monitoring_and_Controlling/03_Contractor_Status_Report) | [تقرير حالة المقاول](../forms/ar/06_المراقبة_والتحكم/03_تقرير_حالة_المقاول) | `forms/en/06_Monitoring_and_Controlling/03_Contractor_Status_Report` | `forms/ar/06_المراقبة_والتحكم/03_تقرير_حالة_المقاول` |
| **PMO-06.04** | [VARIANCE ANALYSIS](../forms/en/06_Monitoring_and_Controlling/04_Variance_Analysis) | [تحليل التباين](../forms/ar/06_المراقبة_والتحكم/04_تحليل_التباين) | `forms/en/06_Monitoring_and_Controlling/04_Variance_Analysis` | `forms/ar/06_المراقبة_والتحكم/04_تحليل_التباين` |
| **PMO-06.05** | [EARNED VALUE ANALYSIS REPORT](../forms/en/06_Monitoring_and_Controlling/05_Earned_Value_Analysis) | [تقرير تحليل القيمة المكتسبة](../forms/ar/06_المراقبة_والتحكم/05_تحليل_القيمة_المكتسبة_(EVA)) | `forms/en/06_Monitoring_and_Controlling/05_Earned_Value_Analysis` | `forms/ar/06_المراقبة_والتحكم/05_تحليل_القيمة_المكتسبة_(EVA)` |
| **PMO-06.06** | [RISK AUDIT REPORT](../forms/en/06_Monitoring_and_Controlling/06_Risk_Audit) | [تقرير تدقيق المخاطر](../forms/ar/06_المراقبة_والتحكم/06_تدقيق_المخاطر) | `forms/en/06_Monitoring_and_Controlling/06_Risk_Audit` | `forms/ar/06_المراقبة_والتحكم/06_تدقيق_المخاطر` |
| **PMO-06.07** | [PROCUREMENT AUDIT REPORT](../forms/en/06_Monitoring_and_Controlling/07_Procurement_Audit) | [تقرير تدقيق المشتريات](../forms/ar/06_المراقبة_والتحكم/07_تدقيق_المشتريات) | `forms/en/06_Monitoring_and_Controlling/07_Procurement_Audit` | `forms/ar/06_المراقبة_والتحكم/07_تدقيق_المشتريات` |
| **PMO-06.08** | [PRODUCT ACCEPTANCE FORM](../forms/en/06_Monitoring_and_Controlling/08_Product_Acceptance_Form) | [نموذج قبول المنتج](../forms/ar/06_المراقبة_والتحكم/08_نموذج_قبول_المنتج) | `forms/en/06_Monitoring_and_Controlling/08_Product_Acceptance_Form` | `forms/ar/06_المراقبة_والتحكم/08_نموذج_قبول_المنتج` |
| **PMO-06.09** | [Vendor Performance Scorecard](../forms/en/06_Monitoring_and_Controlling/09_Vendor_Performance_Scorecard) | [بطاقة أداء المورد](../forms/ar/06_المراقبة_والتحكم/09_بطاقة_أداء_المورد) | `forms/en/06_Monitoring_and_Controlling/09_Vendor_Performance_Scorecard` | `forms/ar/06_المراقبة_والتحكم/09_بطاقة_أداء_المورد` |
| **PMO-06.10** | [User Acceptance Testing Signoff](../forms/en/06_Monitoring_and_Controlling/10_User_Acceptance_Testing_Signoff) | [نموذج اعتماد اختبار قبول المستخدم](../forms/ar/06_المراقبة_والتحكم/10_نموذج_اعتماد_اختبار_قبول_المستخدم_(UAT)) | `forms/en/06_Monitoring_and_Controlling/10_User_Acceptance_Testing_Signoff` | `forms/ar/06_المراقبة_والتحكم/10_نموذج_اعتماد_اختبار_قبول_المستخدم_(UAT)` |
| **PMO-07.01** | [LESSONS LEARNED SUMMARY](../forms/en/07_Closing/01_Lessons_Learned_Summary) | [ملخص الدروس المستفادة](../forms/ar/07_الإغلاق/01_ملخص_الدروس_المستفادة) | `forms/en/07_Closing/01_Lessons_Learned_Summary` | `forms/ar/07_الإغلاق/01_ملخص_الدروس_المستفادة` |
| **PMO-07.02** | [CONTRACT CLOSEOUT REPORT](../forms/en/07_Closing/02_Contract_Closeout_Report) | [تقرير إغلاق العقد](../forms/ar/07_الإغلاق/02_تقرير_إغلاق_العقد) | `forms/en/07_Closing/02_Contract_Closeout_Report` | `forms/ar/07_الإغلاق/02_تقرير_إغلاق_العقد` |
| **PMO-07.03** | [PROJECT OR PHASE CLOSEOUT](../forms/en/07_Closing/03_Project_or_Phase_Closeout) | [تقرير إغلاق المشروع أو المرحلة](../forms/ar/07_الإغلاق/03_إغلاق_المشروع_أو_المرحلة) | `forms/en/07_Closing/03_Project_or_Phase_Closeout` | `forms/ar/07_الإغلاق/03_إغلاق_المشروع_أو_المرحلة` |
| **PMO-07.04** | [Transition to Operations Checklist](../forms/en/07_Closing/04_Transition_to_Operations_Checklist) | [قائمة التحقق للانتقال إلى العمليات](../forms/ar/07_الإغلاق/04_قائمة_التحقق_للانتقال_إلى_العمليات) | `forms/en/07_Closing/04_Transition_to_Operations_Checklist` | `forms/ar/07_الإغلاق/04_قائمة_التحقق_للانتقال_إلى_العمليات` |
| **PMO-07.05** | [Post-Implementation Review Report](../forms/en/07_Closing/05_Post_Implementation_Review) | [تقرير مراجعة ما بعد التنفيذ](../forms/ar/07_الإغلاق/05_مراجعة_ما_بعد_التنفيذ) | `forms/en/07_Closing/05_Post_Implementation_Review` | `forms/ar/07_الإغلاق/05_مراجعة_ما_بعد_التنفيذ` |

---

## 3. Core PMI / PMBOK Lexicon (معجم مصطلحات معهد إدارة المشاريع)

| English Term | Official Arabic (PMI Standard) | Acronym / Note | Definition & Context |
| :--- | :--- | :--- | :--- |
| **Project Charter** | ميثاق المشروع | - | A document issued by the project initiator or sponsor that formally authorizes the existence of a project and provides the PM with authority. |
| **Work Breakdown Structure** | هيكل تجزئة العمل | **WBS** | A hierarchical decomposition of the total scope of work to be carried out by the project team to accomplish project objectives and deliverables. |
| **WBS Dictionary** | قاموس هيكل تجزئة العمل | - | A document that provides detailed deliverable, activity, and scheduling information about each component in the WBS. |
| **Scope Baseline** | الخط المرجعي للنطاق / خط الأساس للنطاق | - | The approved version of a scope statement, WBS, and its associated WBS dictionary. |
| **Schedule Baseline** | الخط المرجعي للجدول الزمني | - | The approved version of a schedule model that can be changed only through formal change control procedures. |
| **Cost Baseline** | الخط المرجعي للتكلفة | - | The approved version of the time-phased project budget, excluding management reserves. |
| **Earned Value Analysis** | تحليل القيمة المكتسبة | **EVA** | A methodology that combines scope, schedule, and resource measurements to assess project performance and progress. |
| **Planned Value** | القيمة المخططة | **PV** | The authorized budget assigned to scheduled work. |
| **Earned Value** | القيمة المكتسبة | **EV** | The measure of work performed expressed in terms of the budget authorized for that work. |
| **Actual Cost** | التكلفة الفعلية | **AC** | The realized cost incurred for the work performed on an activity during a specific time period. |
| **Schedule Variance** | تباين الجدول الزمني | **SV** | A measure of schedule performance expressed as the difference between EV and PV ($SV = EV - PV$). |
| **Cost Variance** | تباين التكلفة | **CV** | A measure of cost performance expressed as the difference between EV and AC ($CV = EV - AC$). |
| **Schedule Performance Index** | مؤشر أداء الجدول الزمني | **SPI** | A measure of schedule efficiency expressed as the ratio of EV to PV ($SPI = EV / PV$). |
| **Cost Performance Index** | مؤشر أداء التكلفة | **CPI** | A measure of the cost efficiency of budgeted resources ($CPI = EV / AC$). |
| **Estimate at Completion** | التقدير عند الاكتمال | **EAC** | The expected total cost of completing all work expressed as the sum of the actual cost and estimate to complete. |
| **Estimate to Complete** | التقدير حتى الاكتمال | **ETC** | The expected cost to finish all the remaining project work. |
| **Variance at Completion** | التباين عند الاكتمال | **VAC** | A projection of the amount of budget deficit or surplus ($VAC = BAC - EAC$). |
| **Responsibility Assignment Matrix** | مصفوفة تعيين المسؤوليات | **RAM / RACI** | A grid that shows the project resources assigned to each work package (Responsible, Accountable, Consulted, Informed). |
| **Resource Breakdown Structure** | هيكل تجزئة الموارد | **RBS** | A hierarchical representation of resources by category and resource type. |
| **Risk Register** | سجل المخاطر | - | A repository in which outputs of risk management processes are recorded. |
| **Probability and Impact Matrix** | مصفوفة الاحتمالية والأثر | - | A grid for mapping the probability of each risk occurrence and its impact on project objectives. |
| **Issue Log** | سجل المشكلات | - | A project document where information about issues is recorded and monitored. |
| **Change Request** | طلب تغيير | **CR** | A formal proposal to modify any document, deliverable, or baseline. |
| **Change Control Board** | مجلس ضبط التغيير | **CCB** | A formally chartered group responsible for reviewing, evaluating, approving, delaying, or rejecting changes to the project. |
| **Quality Audit** | تدقيق الجودة | - | A structured, independent process to determine if project activities comply with organizational and project policies. |
| **Lessons Learned Register** | سجل الدروس المستفادة | - | A project document used to record knowledge gained during a project so that it can be used in the current project and organizational process assets. |
| **Benefits Management Plan** | خطة إدارة الفوائد | - | The documented explanation defining the processes for creating, maximizing, and sustaining the benefits provided by a project or program. |
| **Tailoring Plan** | خطة التخصيص | - | The deliberate adaptation of the project management approach, governance, and processes to fit the specific environment and work. |
| **Statement of Work** | بيان العمل | **SOW** | A narrative description of products, services, or results to be delivered by the project. |
| **Request for Proposal** | طلب تقديم العروض | **RFP** | A type of procurement document used to request proposals from prospective sellers of products or services. |
| **Definition of Ready** | تعريف الجاهزية | **DoR** | A team agreement that a backlog item has all necessary information and acceptance criteria to begin work. |
| **Definition of Done** | تعريف الاكتمال | **DoD** | A team agreement on the criteria that must be met before a product increment is considered complete. |
| **User Acceptance Testing** | اختبار قبول المستخدم | **UAT** | Formal testing with respect to user needs, requirements, and business processes conducted to determine whether a system satisfies the acceptance criteria. |

---

## 4. AI & Digital Governance Terminology (مصطلحات حوكمة الذكاء الاصطناعي)

| English Term | Official Arabic Translation | Definition & Context |
| :--- | :--- | :--- |
| **AI Governance Plan** | خطة حوكمة الذكاء الاصطناعي | Framework specifying oversight, risk controls, compliance, and ethical boundaries for AI solutions. |
| **AI Readiness Assessment** | تقييم جاهزية الذكاء الاصطناعي | Evaluation of data infrastructure, organizational capabilities, ethics, and technical readiness for AI adoption. |
| **AI Use Case Canvas** | نموذج حالة استخدام الذكاء الاصطناعي | One-page structured framework mapping business problem, ML task, value, data requirements, and risks. |
| **AI Model Card & Fact Sheet** | بطاقة نموذج الذكاء الاصطناعي وورقة الحقائق | Standardized documentation of model architecture, training data, performance benchmarks, limitations, and bias metrics. |
| **Data Privacy & Ethics Assessment** | تقييم خصوصية البيانات وأخلاقياتها | Audit of data protection compliance (GDPR/PII), fairness, algorithmic bias, and ethical safety. |
| **Prompt Library Log** | سجل مكتبة الأوامر التوجيهية | Catalog of engineered prompts, system instructions, versioning, and observed performance outputs. |

---

## 5. Governance Roles & Sign-off Responsibilities (الأدوار وصلاحيات الاعتماد)

| Role (EN) | المسمى الوظيفي بالعربية | Governance Responsibility & Templates Signed |
| :--- | :--- | :--- |
| **Project Sponsor** | راعي المشروع | Project Charter (03.01), Business Case (01.01), Project Closeout (07.03), Scope Baseline (04.02.05). |
| **Project Manager** | مدير المشروع | Operational owner across all 102 forms; responsible for preparation, execution tracking, and sign-offs. |
| **Finance Controller / CFO** | المراقب المالي / المدير المالي | Cost Management Plan (04.04.01), Cost Baseline (04.04.04), Procurement Strategy (04.09.02), Contract Closeout (07.02). |
| **CCB Chair** | رئيس مجلس ضبط التغيير | Change Management Plan (04.01.02), Change Requests (05.03), Change Log (05.04). |
| **Quality Assurance Lead** | مسؤول ضمان الجودة | Quality Management Plan (04.05.01), Quality Metrics (04.05.02), Quality Audit (05.05), Product Acceptance (06.08). |
| **Lead Systems Engineer** | كبير مهندسي النظم | WBS (04.02.06), WBS Dictionary (04.02.07), Requirements Traceability Matrix (04.02.04), Architecture Baselines. |
| **Procurement Committee Chair** | رئيس لجنة المشتريات | Procurement Management Plan (04.09.01), SOW (04.09.04), RFP (04.09.05), Vendor Scorecard (06.09). |
| **Data Protection Officer (DPO)** | مسؤول حماية البيانات | Data Privacy & Ethics Assessment (02.06), Security & Regulatory Compliance Baselines. |
| **AI Ethics Officer / Lead** | مسؤول أخلاقيات الذكاء الاصطناعي | AI Governance Plan (02.02), AI Model Card (02.05), AI Readiness (02.03). |
| **Key Stakeholder / Business Client** | العميل / المعني الرئيسي | Stakeholder Engagement Plan (04.10.01), Product Acceptance Form (06.08), UAT Sign-off (06.10). |
| **Operations Handover Lead** | مسؤول الانتقال للعمليات | Transition to Operations Checklist (07.04), Lessons Learned Summary (07.01). |