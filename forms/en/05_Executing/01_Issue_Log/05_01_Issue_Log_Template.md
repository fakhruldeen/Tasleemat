<!--
---
type: Form
token_pointer: /_tokens/forms/en/05_Executing/01_Issue_Log/05_01_Issue_Log_Template.npy
token_count: 594
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.074356+00:00'
form_id: PMO-05.01
language: en
status: approved
---
-->

<!-- LLM INSTRUCTIONS: Populate the Issue Log based on the project context. Ensure the JSON keys map exactly to the corresponding flat markdown fields.

Section-by-Section Instructions:
- Issue Log: Log all project issues including their type, source, priority (Urgent/High/Medium/Low), impacts, responsible party, status (Open/Closed), and resolution. -->

<h3 align="right">{{Company_Name}}</h3>
<h2 align="right">{{Project_Name}} - {{Project_ID}}</h2>
<h1 align="center">ISSUE LOG</h1>

| **Date Prepared:** {{Current_Date}} | **Project Manager:** {{Project_Manager_Name}} |
| :--- | :--- |

---

## Issue Log Entries

| ID | Type | Source of Issue | Issue Description | Priority | Impact on Objectives | Impacted Stakeholders | Responsible Party | Status | Resolution Date | Final Resolution | Comments |
| :---: | :--- | :--- | :--- | :---: | :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :---: | :---: |
| **Issue Owner / Contributor** | {{Issue_Owner_Name}} | _______________________ | [ .... - .... - .... ] |
| **Project Manager** | {{Project_Manager_Name}} | _______________________ | [ .... - .... - .... ] |
| **PMO Lead** | {{PMO_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> ISSUE LOG | <strong>Ref:</strong> PMO-05.01 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
