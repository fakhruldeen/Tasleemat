# Global Project Parameters

This file holds all the global variables and placeholders needed across the project forms. When using an LLM to generate or fill out forms, provide these parameters so the LLM can accurately populate the templates.

## 1. Project Information
- **Project Name:** `[Enter Project Name]`
- **Project Acronym/ID:** `[Enter Project ID]`
- **Project Description:** `[Enter Brief Description]`
- **Start Date:** `[Enter Start Date]`
- **End Date / Target Date:** `[Enter End Date]`

## 2. Key Personnel
- **Project Manager Name:** `[Enter Name]`
- **Project Manager Email:** `[Enter Email]`
- **Project Sponsor Name:** `[Enter Name]`
- **Project Sponsor Email:** `[Enter Email]`
- **Client/Customer Name:** `[Enter Name]`
- **Client/Customer Organization:** `[Enter Organization]`

## 3. Organizational Context
- **Company/Organization Name:** `[Enter Company Name]`
- **Performing Department/Unit:** `[Enter Department]`
- **Program/Portfolio Name:** `[Enter Program Name, if applicable]`

## 4. Financial & Constraints
- **Approved Budget:** `[Enter Budget]`
- **Primary Currency:** `[Enter Currency, e.g., USD]`
- **Major Constraints:** `[Enter Key Constraints]`

## 5. Sign-off & Approval Roles (used in the "Sign-off and Approvals" table)
Each template closes with a *Sign-off and Approvals* table listing the roles that must
prepare, review, audit, or approve that specific form. Fill only the roles that appear in
that form; leave the rest blank.

| Variable | Role | Arabic placeholder |
| :--- | :--- | :--- |
| `{{Project_Manager_Name}}` | Project Manager | `{{اسم_مدير_المشروع}}` |
| `{{Project_Sponsor_Name}}` | Project Sponsor / Client | `{{اسم_راعي_المشروع}}` |
| `{{Client_Customer_Name}}` | Client Representative | `{{اسم_العميل}}` |
| `{{PMO_Lead_Name}}` | PMO Lead | `{{اسم_مسؤول_مكتب_إدارة_المشاريع}}` |
| `{{Finance_Controller_Name}}` | Finance Controller | `{{اسم_المراقب_المالي}}` |
| `{{Cost_Controller_Name}}` | Cost Controller / Cost & Finance Lead | `{{اسم_مراقب_التكاليف}}` |
| `{{Program_Manager_Name}}` | Program Manager | `{{اسم_مدير_البرنامج}}` |
| `{{Program_Sponsor_Name}}` | Program Sponsor | `{{اسم_راعي_البرنامج}}` |
| `{{Business_Owner_Name}}` | Business Owner | `{{اسم_مالك_الأعمال}}` |
| `{{Product_Owner_Name}}` | Product Owner | `{{اسم_مالك_المنتج}}` |
| `{{Business_Analyst_Name}}` | Business Analyst | `{{اسم_محلل_الأعمال}}` |
| `{{Requirements_Manager_Name}}` | Requirements Manager | `{{اسم_مدير_المتطلبات}}` |
| `{{Team_Lead_Name}}` | Team Lead | `{{اسم_قائد_الفريق}}` |
| `{{Planning_Lead_Name}}` | Planning Lead / Scheduler | `{{اسم_مسؤول_التخطيط}}` |
| `{{Quality_Manager_Name}}` | Quality Manager / QA Lead | `{{اسم_مدير_الجودة}}` |
| `{{Lead_Auditor_Name}}` | Lead Auditor | `{{اسم_رئيس_التدقيق}}` |
| `{{Risk_Manager_Name}}` | Risk Manager | `{{اسم_مدير_المخاطر}}` |
| `{{Risk_Owner_Name}}` | Risk Owner | `{{اسم_مالك_المخاطر}}` |
| `{{Procurement_Manager_Name}}` | Procurement Manager | `{{اسم_مدير_المشتريات}}` |
| `{{Vendor_Representative_Name}}` | Vendor / Contractor Representative | `{{اسم_ممثل_المورد}}` |
| `{{Resource_Manager_Name}}` | Resource Manager | `{{اسم_مدير_الموارد}}` |
| `{{Communications_Lead_Name}}` | Communications Lead | `{{اسم_مسؤول_الاتصالات}}` |
| `{{Change_Manager_Name}}` | Change Manager | `{{اسم_مدير_التغيير}}` |
| `{{Training_Coordinator_Name}}` | Training Coordinator | `{{اسم_منسق_التدريب}}` |
| `{{AI_ML_Lead_Name}}` | AI / ML Lead | `{{اسم_مسؤول_الذكاء_الاصطناعي}}` |
| `{{Data_Protection_Officer_Name}}` | Data Protection Officer | `{{اسم_مسؤول_حماية_البيانات}}` |
| `{{Ethics_Review_Lead_Name}}` | Ethics Review Lead | `{{اسم_مسؤول_مراجعة_الأخلاقيات}}` |
| `{{Operations_Owner_Name}}` | Operations / Service Owner | `{{اسم_مالك_التشغيل}}` |
| `{{CCB_Chair_Name}}` | Change Control Board (CCB) Chair | `{{اسم_رئيس_لجنة_إدارة_التغيير}}` |
| `{{Evaluation_Chair_Name}}` | Evaluation Committee Chair | `{{اسم_رئيس_لجنة_التقييم}}` |
| `{{Contract_Manager_Name}}` | Contract Manager | `{{اسم_مدير_العقد}}` |
| `{{Dependency_Owner_Name}}` | Dependency Owner | `{{اسم_مالك_الاعتماد_المتبادل}}` |
| `{{Meeting_Chair_Name}}` | Meeting Chair | `{{اسم_رئيس_الاجتماع}}` |
| `{{Note_Taker_Name}}` | Note Taker | `{{اسم_مسجل_المحضر}}` |
| `{{Prepared_By}}` | Document author / contributor | `{{معد_الوثيقة}}` |
| `{{Reviewed_By}}` | Document reviewer | `{{مُراجع_الوثيقة}}` |
| `{{Approved_By}}` | Document approver | `{{معتمد_الوثيقة}}` |

*Note to LLM:* Use these global parameters to automatically fill in the corresponding `[Placeholders]` in the various project management form templates.
