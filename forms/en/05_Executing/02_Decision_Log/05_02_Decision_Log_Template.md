---
type: Form
token_pointer: /_tokens/forms/en/05_Executing/02_Decision_Log/05_02_Decision_Log_Template.npy
token_count: 528
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.064810+00:00'
form_id: PMO-05.02
language: en
status: approved
---

<!-- LLM INSTRUCTIONS: Populate the Decision Log based on the project context. Ensure the JSON keys map exactly to the corresponding flat markdown fields.

Section-by-Section Instructions:
- Decision Log: Record all project decisions. Include the category, the decision itself, impacts on objectives, affected stakeholders, the responsible party, the date, and any comments (such as alternatives considered or reasoning). -->

<h3 align="right">{{Company_Name}}</h3>
<h2 align="right">{{Project_Name}} - {{Project_ID}}</h2>
<h1 align="center">DECISION LOG</h1>

| **Date Prepared:** {{Current_Date}} | **Project Manager:** {{Project_Manager_Name}} |
| :--- | :--- |

---

## Decision Log Entries

| ID | Category | Decision | Impacts on Deliverables/Objectives | Impacted Stakeholders | Responsible Party | Date | Comments |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :---: | :---: |
| **Decision Maker / PM** | {{Project_Manager_Name}} | _______________________ | [ .... - .... - .... ] |
| **Key Stakeholder Representative** | {{Stakeholder_Representative_Name}} | _______________________ | [ .... - .... - .... ] |
| **Project Sponsor** | {{Project_Sponsor_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> DECISION LOG | <strong>Ref:</strong> PMO-05.02 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
