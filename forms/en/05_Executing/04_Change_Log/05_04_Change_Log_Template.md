---
type: Form
token_pointer: /_tokens/forms/en/05_Executing/04_Change_Log/05_04_Change_Log_Template.npy
token_count: 527
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.073968+00:00'
---

<!-- LLM INSTRUCTIONS: Populate the Change Log based on the project context. Note: This log must output an array of objects matching the flat table headers. -->

<h3 align="right">{{Company_Name}}</h3>
<h2 align="right">{{Project_Name}} - {{Project_ID}}</h2>
<h1 align="center">CHANGE LOG</h1>

| **Date Prepared:** {{Current_Date}} | **Project Manager:** {{Project_Manager_Name}} |
| :--- | :--- |

---

## Change Log Entries

| ID | Category | Description | Requestor | Submission Date | Status | Disposition | Cost/Schedule Impact | Type (Mandatory/Discretionary) | Configurable Items Impacted |
| :---: | :--- | :--- | :--- | :---: | :---: | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :---: | :---: |
| **Project Manager** | {{Project_Manager_Name}} | _______________________ | [ .... - .... - .... ] |
| **Change Control Board (CCB) Chair** | {{CCB_Chair_Name}} | _______________________ | [ .... - .... - .... ] |
| **PMO Lead** | {{PMO_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> CHANGE LOG | <strong>Ref:</strong> PMO-05.04 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
