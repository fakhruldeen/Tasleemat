<!--
---
type: Form
token_pointer: /_tokens/forms/en/07_Closing/02_Contract_Closeout_Report/07_02_Contract_Closeout_Report_Template.npy
token_count: 2307
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.077999+00:00'
form_id: PMO-07.02
language: en
status: approved
---
-->

<!--  LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

Contract closeout involves documenting vendor performance so that the information can be used
to evaluate the vendor for future work. Contract closure supports the project closure process
and helps ensure contractual agreements are completed or terminated.

Before a contract can be fully closed or terminated, all disputes must be resolved, the
product or result must be accepted, and the final payments must be made. Record the contract
completion date, who signed off on it, and the date of the final payment.

The contract closeout report draws on Table 4.8, Elements of a Contract Closeout.

Tailoring Notes:
*   For a small contract you can combine all the information in the vendor performance
    analysis into a single summary paragraph.
*   For small contracts you may not need the contract changes or contract disputes sections.
*   If the project was based around one large contract, you can combine the information in
    the project closeout report with this form.

Alignment: the report should be aligned and consistent with the procurement management plan,
the procurement audit, the change log, and the project closeout.

Section Instructions:
*   **Contract Identification:** Record the contract reference, the vendor, the contract
    type and value, and the closeout status.
*   **What Worked Well:** For the vendor performance analysis, describe what was handled
    well in scope, quality, schedule, and cost, plus any other aspect of the contract or
    procurement.
*   **What Can Be Improved:** For the same five dimensions, describe what could have been
    improved. Every point should be specific and actionable.
*   **Record of Contract Changes:** For each change, enter the change ID, the description,
    and the date approved, taken from the change log.
*   **Record of Contract Disputes:** For each dispute or claim, describe it, the resolution,
    and the date it was resolved. All disputes must be resolved before closure.
*   **Contract Completion and Final Payment:** Record the completion date, who signed off,
    and the date of the final payment.
*   **Comments:** Add any comments that add relevance to the report. -->

<h3 align="right">{{Company_Name}}</h3>
<h2 align="right">{{Project_Name}} - {{Project_ID}}</h2>
<h1 align="center">CONTRACT CLOSEOUT REPORT</h1>

| **Date Prepared:** {{Current_Date}} | **Project Manager:** {{Project_Manager_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |  

---

## 1. Contract Identification
<!-- Identify the contract being closed so this record can be filed against the right
agreement and reused when the vendor is evaluated for future work. Record the contract
reference, the vendor, the contract type and value, and whether the contract is being
closed as completed or terminated. The closeout status matters because a terminated
contract is also closed, but the performance record is interpreted differently.
- **Contract Reference:** the contract or purchase order number.
- **Vendor:** the legal entity that performed the work.
- **Contract Type and Value:** the contract type, for example fixed price or cost
  reimbursable, and the total contracted value.
- **Closeout Status:** completed or terminated, and the date closure was initiated. -->

| Field | Entry |
| :--- | :--- |
| **Contract Reference** | [ Add details... ] |
| **Vendor** | [ Add details... ] |
| **Contract Type and Value** | [ Add details... ] |
| **Closeout Status** | [ Add details... ] |

---

## 2. Vendor Performance Analysis: What Worked Well
<!-- Record what the vendor did well, across the five dimensions of Table 4.8. This record
exists so the vendor can be evaluated for future work, so state the specific practice and
the evidence behind it rather than a general assessment. Keep the dimensions separate, since
a conclusion that mixes quality and cost cannot be acted on. The Other row is where
qualitative points belong, for example how easy the vendor was to work with.
- **Scope:** aspects of contract scope that were handled well.
- **Quality:** aspects of product quality that were handled well.
- **Schedule:** aspects of the contract schedule that were handled well.
- **Cost:** aspects of the contract budget that were handled well.
- **Other:** any other aspect of the contract or procurement handled well, including how
  easy the vendor was to work with. -->

| Dimension | What Was Handled Well | Evidence or Example |
| :--- | :--- | :--- |
| **Scope** | [ Add details... ] | [ Add details... ] |
| **Quality** | [ Add details... ] | [ Add details... ] |
| **Schedule** | [ Add details... ] | [ Add details... ] |
| **Cost** | [ Add details... ] | [ Add details... ] |
| **Other** | [ Add details... ] | [ Add details... ] |

<!--
Tailoring note: For a small contract, all of the vendor performance information may be combined into a single summary paragraph.
-->

---

## 3. Vendor Performance Analysis: What Can Be Improved
<!-- Record what should have been done better, across the same five dimensions. Every point
must be specific and actionable: state the deficiency, its effect on the contract or
project, and what should be done instead. This section carries the most value for future
procurement, because a defect recorded here will change how the next contract is written or
managed. Where the cause was organisational rather than vendor-specific, say so.
- **Scope:** aspects of contract scope that could be improved.
- **Quality:** aspects of product quality that could be improved.
- **Schedule:** aspects of the contract schedule that could be improved.
- **Cost:** aspects of the contract budget that could be improved.
- **Other:** any other aspect of the contract or procurement that could be improved. -->

| Dimension | What Could Be Improved | Recommended Action |
| :--- | :--- | :--- |
| **Scope** | [ Add details... ] | [ Add details... ] |
| **Quality** | [ Add details... ] | [ Add details... ] |
| **Schedule** | [ Add details... ] | [ Add details... ] |
| **Cost** | [ Add details... ] | [ Add details... ] |
| **Other** | [ Add details... ] | [ Add details... ] |

<!--
Comment guidance: State the deficiency, its effect, and what should be done instead.
-->

---

## 4. Record of Contract Changes
<!-- Record every change made to the contract during its execution, taking all three
elements from the change log rather than restating them from memory. A change alters the
contracted scope, price, or schedule, so an unrecorded change leaves the contract
discrepant against the final account. Give the change ID exactly as it appears in the
change log so the two records can be reconciled.
- **Change ID:** the change identifier from the change log.
- **Change Description:** the description from the change log.
- **Date Approved:** the date approved from the change log. -->

| Change ID | Change Description | Date Approved |
| :---: | :--- | :---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] |

<!--
Tailoring note: For small contracts, this section may not be needed.
-->

---

## 5. Record of Contract Disputes
<!-- Record every dispute or claim raised against the contract, and its outcome. All
disputes must be resolved before a contract can be fully closed or terminated, so any
entry still open at the date of this report blocks closure. Give the resolution in
concrete terms, including any settlement amount, because the resolution is what releases
the contract.
- **Dispute Description:** describe the dispute or claim.
- **Resolution:** describe the resolution.
- **Date Resolved:** the date the dispute or claim was resolved. -->

| Dispute Description | Resolution | Date Resolved |
| :--- | :--- | :---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] |

<!--
Tailoring note: For small contracts, this section may not be needed.
-->

---

## 6. Contract Completion and Final Payment
<!-- Record the three elements that evidence closure. All disputes must be resolved, the
product or result must be accepted, and the final payments must be made before a contract
can be fully closed or terminated. Name the person who signed off, not just the role, so
the acceptance is traceable. If the contract is being terminated rather than completed, say
so here and explain why in the comments section.
- **Contract Completion Date:** the date the contract was completed.
- **Signed Off By:** who signed off on the contract completion.
- **Final Payment Date:** the date of the final payment. -->

| Field | Entry |
| :--- | :--- |
| **Contract Completion Date** | [ Add details... ] |
| **Signed Off By** | [ Add details... ] |
| **Final Payment Date** | [ Add details... ] |

<!--
Comment guidance: All disputes must be resolved, the result accepted, and final payment made before closure.
-->

---

## 7. Comments
<!-- Add any comments that give the report additional relevance, such as the reason a
contract was terminated rather than completed, scope limitations, or context needed by
the project closeout report. -->


---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :---: | :---: |
| **Contract Manager** | {{Contract_Manager_Name}} | _______________________ | [ .... - .... - .... ] |
| **Procurement Manager** | {{Procurement_Manager_Name}} | _______________________ | [ .... - .... - .... ] |
| **Finance Controller / Legal Counsel** | {{Finance_Controller_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> CONTRACT CLOSEOUT REPORT | <strong>Ref:</strong> PMO-07.02 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
