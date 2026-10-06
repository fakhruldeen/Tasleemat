<!--
---
type: Form
token_pointer: /_tokens/forms/en/06_Monitoring_and_Controlling/08_Product_Acceptance_Form/06_08_Product_Acceptance_Form_Template.npy
token_count: 1422
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.049922+00:00'
form_id: PMO-06.08
language: en
status: approved
---
-->

<!--  LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

Product acceptance should be done periodically throughout the project as each deliverable or
component is validated and accepted. This form is part of process 5.5 Validate Scope in the
PMBOK Guide - Sixth Edition.

The form records one row per requirement or deliverable, drawing on Table 4.9, Elements of
Product Acceptance: the identifier and requirement text are taken from the requirements
documentation, the acceptance criteria state what must be true, the validation method
describes how that will be shown, the status records whether the item was accepted, and the
sign-off names the party accepting the product.

Keep the identifier exactly as it appears in the requirements documentation, because this
form is a record of that documentation rather than a restatement of it. An acceptance whose
criteria cannot be judged met or not met is not an acceptance, so write the criteria so that
each one can be answered yes or no with evidence.

Tailoring Notes:
*   For a small project with only a few deliverables you may not need this form, and the
    acceptance may instead be recorded in the project status report or the deliverable
    acceptance record.
*   You can add a column to indicate the verification method used to prove that the
    deliverables meet the requirements. In that case the form becomes a product
    verification, validation, and acceptance form. The Verification Method column below
    provides that option; remove it if you do not need it.

Alignment: the form should be aligned and consistent with the scope management plan, the
requirements documentation, the requirements traceability matrix, and the quality management
plan.

Section Instructions:
*   **Product Acceptance Record:** For each requirement or deliverable accepted, record the
    identifier, the requirement, the acceptance criteria, the validation method, the
    verification method if used, the status, the sign-off, the acceptance date, and any
    comments.
*   **Comments:** Add any comments relevant to the acceptance. -->

<h3 align="right">{{Company_Name}}</h3>
<h2 align="right">{{Project_Name}} - {{Project_ID}}</h2>
<h1 align="center">PRODUCT ACCEPTANCE FORM</h1>

| **Date Prepared:** {{Current_Date}} | **Project Manager:** {{Project_Manager_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |  

---

## 1. Product Acceptance Record
<!-- Record one row per requirement or deliverable accepted. Take the ID and the requirement
text from the requirements documentation without rewording them, because this form is a
record of that documentation and a restatement would not reconcile with it. State the
acceptance criteria so that each one can be answered yes or no with evidence: a criterion
that cannot be judged met or not met does not support an acceptance. Describe the validation
method, which shows how the requirement meets the stakeholder's needs, and distinguish it
from the verification method, which proves the deliverable meets the requirement. Record the
status honestly, including a rejected or conditional acceptance, and name the party signing
for the product rather than only the role, so the acceptance is traceable.
- **ID:** the unique requirement identifier from the requirements documentation.
- **Requirement:** the requirement description from the requirements documentation.
- **Acceptance Criteria:** the criteria for acceptance, stated so they can be judged as met
  or not met.
- **Validation Method:** the method of validating that the requirement meets the
  stakeholder's needs.
- **Verification Method:** the method used to prove the deliverable meets the requirement.
  Optional; remove this column if it is not used.
- **Status:** whether the requirement or deliverable was accepted or not.
- **Sign-off:** the signature of the party accepting the product.
- **Acceptance Date:** the date the product was accepted.
- **Comments:** any conditions attached to the acceptance, or items deferred to a later
  acceptance. -->

| ID | Requirement | Acceptance Criteria | Validation Method | Verification Method | Status | Sign-off | Date |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- | :---: |
| [ Add ID... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Sign here... ] | [ .... - .... - .... ] |
| [ Add ID... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Sign here... ] | [ .... - .... - .... ] |
| [ Add ID... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Sign here... ] | [ .... - .... - .... ] |
| [ Add ID... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Sign here... ] | [ .... - .... - .... ] |
| [ Add ID... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Sign here... ] | [ .... - .... - .... ] |

<!--
Tailoring note: Remove the Verification Method column if you do not need it. With that column the form becomes a product verification, validation, and acceptance form.
-->
<!--
Comment guidance: Record any conditions attached to the acceptance, or items deferred to a later acceptance.
-->

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :---: | :---: |
| **Product / Business Owner** | {{Product_Owner_Name}} | _______________________ | [ .... - .... - .... ] |
| **Project Manager** | {{Project_Manager_Name}} | _______________________ | [ .... - .... - .... ] |
| **Client / Customer Representative** | {{Client_Representative_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> PRODUCT ACCEPTANCE FORM | <strong>Ref:</strong> PMO-06.08 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
