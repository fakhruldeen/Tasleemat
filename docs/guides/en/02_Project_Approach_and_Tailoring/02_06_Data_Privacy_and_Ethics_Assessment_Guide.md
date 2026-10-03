<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <a class="lang-switch-btn" href="../../ar/02_منهجية_المشروع_وتخصيصه/02_06_تقييم_خصوصية_البيانات_وأخلاقياتها_دليل.html">🇸🇦 الانتقال للدليل بالعربية (Arabic Guide) →</a>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-02.06</span>
    <span class="badge badge-phase">02. Project Approach & Tailoring</span>
    <span class="badge badge-type">Authoring & Governance Guide</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="../../../templates/en/02_Project_Approach_and_Tailoring/02_06_Data_Privacy_and_Ethics_Assessment_Template.html">📋 Blank Template</a>
    <a class="nav-pill active" href="#">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../examples/en/02_Project_Approach_and_Tailoring/02_06_Data_Privacy_and_Ethics_Assessment_Example.html">💡 Completed Example</a>
    <a class="nav-pill lang-pill" href="../../ar/02_منهجية_المشروع_وتخصيصه/02_06_تقييم_خصوصية_البيانات_وأخلاقياتها_دليل.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

---
lang: en
layout: default
title: Data Privacy and Ethics Assessment
nav_order: 1
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">

## Tasleemat Forms Guide
# Project Artifact: Data Privacy and Ethics Assessment

**Document Reference:** `PMO-02.06`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Data Privacy and Ethics Assessment** in alignment
with the Tasleemat framework.

---

### 1. What?
A record of the personal data a piece of work will process: what is in scope
and what is explicitly out, who owns and who administers each data asset, what
each one is held for and whether it holds special category data, where the
data moves, the lawful basis relied on for each purpose rather than for each
dataset, any use beyond the original purpose, any decision made about a person
without meaningful human involvement, how consent is requested and evidenced
and withdrawn, how an individual's request is answered in time, what happens
to data that has been derived or trained into a model, how long each asset is
kept and on what basis, how deletion reaches replicas, logs, exports and
models, who can reach the data and who holds the keys, who else receives it
and under which mechanism, what constitutes a breach here, where the
processing causes harm that no law prohibits, who is affected while unable to
refuse, what the people in the data are actually told, whether the interface
permits a real choice, how automated outcomes fall across groups, and what
was found, what risk remains, and what would reopen the assessment.

---

### 2. Why?
Because the harm this work can do is invisible from inside it. A team can see
the schema and the throughput and the cost per request, and none of those
show what happens to the person whose record is in the table. So the
questions get answered from assumption, the assumptions differ between the
engineer and the reviewer, and the first person to find out is the individual
who asks for their data and is told the request is being looked into.

The fields that appear empty are the evidence. An assessment with no stated
exclusions, no secondary use, no deletion-coverage statement, no withdrawal
route and no ethics findings describes processing that has not started, since
each of those is filled in by something that happened rather than by something
that was decided. A consent record without the version of the text shown
cannot be defended later, because the terms the person agreed to are then
unrecoverable; a retention period recorded without its basis is a default
adopted and written down as a decision; and deleting a row from the primary
store while the data persists in four other places is the most frequent
finding in any such review, and it is invisible without a coverage statement.

The section on harm beyond legal exposure exists because compliance is a floor
rather than a ceiling. Processing can be lawful, consented, retained properly,
secured properly and shared properly, and still be wrong, and a form that
stops at lawful has answered the question that was easy to answer. The people
who read the completed form will believe the work is finished.

---

### 3. When?
This artifact is primarily prepared, utilized, and updated during the **PROJECT
APPROACH AND TAILORING Process Group** of the project lifecycle. It is drafted
when a processing purpose is proposed, baselined before any personal data is
collected, and revised on every change of purpose, recipient, model, or
jurisdiction, and on any regulatory change, since each of those alters what
the assessment should say. It is read at design review, at procurement, when
a new dataset is proposed, when an individual exercises a right, and at the
incident review.

---

### 4. Who?
**Responsibilities:** Prepared by the Data Protection Officer, who is
accountable for the lawful basis, the retention schedule and the rights
handling process, and who is the person who must be able to answer a request
from an individual without consulting anyone. Reviewed by the Ethics Review
Lead, who is accountable for the section on harm beyond legal exposure and for
the fairness of automated outcomes, and by the data owner for each asset, who
is accountable for the stated purpose being the real one. Approved by the
Project Sponsor, who is accountable for accepting the residual risk. Where
processing was not looked at, record that it was not looked at, rather than
leaving the field blank, since an exclusion and an omission are different
findings.

---

### Tailoring Tips
*   An assessment for processing with no personal data may be short, but the
    scope section must still state what would bring the work into scope, since
    that is the boundary that is later tested.
*   Where one dataset serves several purposes, the lawful-basis table gains a
    row per purpose rather than gaining columns, since a form that records a
    basis once will carry it across purposes that do not share it.
*   Retention periods may be inherited from a group standard, provided the row
    records that the period was inherited and on what basis, which is a
    different statement from having chosen it.
*   Where a model is trained on the data, the derived-data row should name the
    model and the training date, because a deletion request after that date
    cannot be answered by deleting a row.
*   It is worth recording which findings were accepted rather than fixed, with
    the name of the person who accepted them and the date the acceptance
    expires, since an acceptance with neither is an unowned risk.
*   Where the ethics section produces nothing, record that it was considered
    and what was considered, since an empty section is read as an omission
    rather than as a conclusion.
*   Superseded assessments should be retained rather than overwritten, since
    the question a complaint generates is almost always about what was in
    force at the time.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   AI Use Case Canvas (PMO-02.04) or Scope Statement (PMO-04.02.05)
    *   Data Flow & System Architecture
*   **Optional / Contextual:**
    *   Regulatory Privacy Requirements (GDPR / Data Protection Acts)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   AI Governance Plan (PMO-02.02)
    *   Risk Register (PMO-04.08.02)
    *   Requirements Documentation (PMO-04.02.03)
*   **Optional / Contextual:**
    *   Statement of Work / SOW (PMO-04.09.04)
    *   Quality Audit (PMO-05.05)

---

### 5. How?
To accurately and professionally complete the **DATA PRIVACY AND ETHICS ASSESSMENT**, the
responsible party must populate the following sections based on the project
context (ensure `parameters.md` is referenced for global project variables):

*   **Assessment Scope:** The processing, systems, and periods this assessment covers, stated so that its edges are visible. An assessment that does not say what it excludes will be read as covering everything, and the gap between the two is where the untested processing lives.
*   **Processing Out of Scope:** What is explicitly not covered, and why. Excluded because another assessment covers it, or excluded because it was not looked at, are very different statements and only the second one is a finding.
*   **Data Owners and Custodians:** Who owns each data asset and who administers it day to day. Ownership and custody differ, and the accountability clause follows the custodian while the budget follows the owner.
*   **Data Inventory:** One row per data asset: what it is, who owns it, the purpose it is held for, whether it holds personal data, whether that data is special category, and its volume and refresh rate. An inventory described as a count rather than as a list cannot answer any of the questions that follow.
*   **Data Flow and Recipients:** Where the data moves, and who receives it. The flow is what determines which transfers need a mechanism, and a flow that shows only the primary store hides the copies.
*   **Processing Purposes and Necessity:** What each processing activity is for, and why it cannot be achieved with less data or a shorter reach. Necessity is assessed per purpose rather than per dataset, because one dataset frequently serves several purposes with very different necessity.
*   **Lawful Basis by Purpose:** One row per purpose: the data processed, the basis relied on, the basis for special category data where any is present, and the justification. A form that records a basis once for a dataset will carry one basis across purposes that do not share it.
*   **Purpose Compatibility and Secondary Use:** Whether the data is used for any purpose other than the one collected for, and on what basis. Secondary use is the most common privacy failure in analytics work and the one least likely to be noticed, because every individual field still has a lawful origin.
*   **Automated Decision-Making:** Any decision made about a person with no meaningful human involvement, the logic involved, and the consequences for them. Recorded because the assessment of a legal basis does not by itself establish that a decision is one a person could contest.
*   **Consent Mechanism:** How consent is requested, and where in the flow it appears. Consent collected after the data is already in use is a record, not a request, and the difference determines what the record is worth.
*   **Consent Specificity and Granularity:** What the person was told they were consenting to, and whether the choices are separate. A single consent covering several purposes is consent to none of them in particular, and a bundle of pre-ticked boxes is not a choice.
*   **Consent Recording and Evidence:** Where each consent is stored, with the timestamp, the version of the text shown, and the interface shown. A consent record without the version of the text cannot be defended later, because the terms the person agreed to are then unrecoverable.
*   **Withdrawal:** How a person withdraws, how much easier it is than granting, and what happens to data already processed on that basis. Asymmetry between granting and withdrawing is the standard test, and a withdrawal that is honoured prospectively only leaves the processing intact behind it.
*   **Privacy Notices and Just-in-Time Disclosure:** What is told at collection, what is told at the point the data is used, and where either may be found. A notice published once and never revisited informs nobody who meets the processing for the first time in month three.
*   **Rights Handling Process:** How a request is received, routed, decided and answered, and by whom. A right stated in a policy with no route to exercise it is a stated right, and it is tested only when someone uses it.
*   **Identity Verification:** How the requester is confirmed to be who they claim, and what is refused when that cannot be done. Verification that accepts anyone discloses data; verification that refuses everyone denies the right, and the balance is a decision to record rather than a default.
*   **Response Timeframes and Escalation:** The deadline for each type of request, what happens when it is missed, and who is told. The clock is the whole of the right in practice, because a correct answer delivered late is still a breach.
*   **Rights Over Derived, Shared and Retired Data:** What happens to a request where the data has been aggregated, shared with a third party, or placed in a model. Deletion cannot reach a trained model by deleting a row, and the form that does not say so will be read as having deleted it.
*   **Retention Schedule:** One row per data asset: the retention period, the basis for that period rather than the convention, what triggers deletion, and how deletion is verified. A period adopted as a default and recorded as a decision is the most common entry, and it is the reason data outlives every justification that justified it.
*   **Deletion Mechanism and Coverage:** How deletion is carried out, across primary stores, replicas, logs, exports and derived copies. Deleting a row from one table while the data persists in five other places is the most frequent finding in any such assessment, and it is invisible without a coverage statement.
*   **Backups and Derived Data:** How deletion propagates to backups and to models trained on the data, and over what period. Backups are the usual reason a deletion is incomplete, and a trained model is a copy no deletion request reaches.
*   **Access Controls and Least Privilege:** Who can reach the data, by what route, under what approval, and how access is reviewed. Access is the control that fails quietly, since misuse of legitimate credentials is indistinguishable from legitimate use without a review.
*   **Encryption and Key Management:** What is encrypted in transit and at rest, and who holds the keys. Encryption whose keys sit beside the data is a control on paper, and the key custody arrangement is the part that is not written down.
*   **Third-Party Sharing:** One row per recipient: the recipient, the purpose, the data shared, the contractual safeguard relied on, and the region processed in. Each row needs its own basis, because a processor bound by contract to a controller is not the same arrangement as a controller sharing on its own purpose.
*   **Cross-Border Transfers:** Where data or processing leaves the jurisdiction, under which transfer mechanism, and what supplementary measures apply. A hosting region is not a transfer analysis, and remote access by a foreign staff member is a transfer that no region setting records.
*   **Breach Notification:** What constitutes a breach here, who is notified, within what time, and who decides. Recorded because a response plan written after an incident is always written for that incident, and the decision threshold is the part that is usually left out.
*   **Harm Beyond Legal Exposure:** Where this processing causes harm that no law prohibits. This section exists because compliance is a floor: processing can be lawful, consented, retained properly and shared properly, and still be wrong, and a form that stops at lawful has answered the question it was easy to answer.
*   **Vulnerable Individuals and Groups:** Who is affected in a state of reduced ability to refuse, to understand, or to bear the consequence. Vulnerability here is a property of the situation rather than of the person, and it is invisible to a record of categories and volumes.
*   **Transparency to Affected People:** What the people in the data are actually told, in language they use, as distinct from what the notice says. A notice that is accurate, complete and unread is the standard failure, and reading it as a recipient rather than as a drafter is the only way to see it.
*   **Manipulation, Dark Patterns and Consent Fatigue:** Whether the interface nudges, pre-ticks, buries refusal, or asks repeatedly, and whether the volume of requests is such that a refusal is impractical. Consent obtained by a design choice is not freely given, whatever the record says.
*   **Fairness of Automated Decisions:** Whether the processing produces outcomes for people, and what the distribution of those outcomes is across groups. A lawful basis for a decision is not a defence of its fairness, and the two are assessed against different questions.
*   **Findings Register:** One row per finding: the finding, the risk it poses to individuals, the severity, the owner, and the action being taken. Severity is what determines the order of work, and a register with no severity column is a list of observations.
*   **Residual Risk and Acceptance:** The risk remaining after the planned actions, who accepts it, and until when. Acceptance is a decision with an owner and an expiry date; an acceptance with neither is an unowned risk that will be rediscovered at the next assessment.
*   **Remediation Plan:** The actions, their owners and their dates, and what is being done in the interim. The interim period is where a known finding actually operates, so it is the part of the plan most worth writing down.
*   **Review Triggers:** What would cause this assessment to be revisited before its scheduled date, such as a new purpose, a new recipient, a new model, or a regulatory change. Triggers stated after the change have occurred are a record of the change.
*   **Reassessment Triggers:** When this assessment expires and on what cycle. An assessment with no expiry is treated as permanent by everyone who did not write it, including the people who inherited it.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](../../../templates/en/02_Project_Approach_and_Tailoring/02_06_Data_Privacy_and_Ethics_Assessment_Template.md)
* **🤖 LLM Generation Prompt**
* **📊 Data Structure (JSON)**
* **📈 Tabular Data (CSV)**

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [02_06_Data_Privacy_and_Ethics_Assessment_Example.md](../../../examples/en/02_Project_Approach_and_Tailoring/02_06_Data_Privacy_and_Ethics_Assessment_Example.md)

</div>
