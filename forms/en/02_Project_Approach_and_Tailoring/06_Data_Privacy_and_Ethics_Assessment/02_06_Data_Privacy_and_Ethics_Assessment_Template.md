<!--
LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

Section Instructions:

**1. Scope, Data Inventory and Ownership**
*   **Assessment Scope:** The processing, systems, and periods this assessment covers, stated so that its edges are visible. An assessment that does not say what it excludes will be read as covering everything, and the gap between the two is where the untested processing lives.
*   **Processing Out of Scope:** What is explicitly not covered, and why. Excluded because another assessment covers it, or excluded because it was not looked at, are very different statements and only the second one is a finding.
*   **Data Owners and Custodians:** Who owns each data asset and who administers it day to day. Ownership and custody differ, and the accountability clause follows the custodian while the budget follows the owner.
*   **Data Inventory:** One row per data asset: what it is, who owns it, the purpose it is held for, whether it holds personal data, whether that data is special category, and its volume and refresh rate. An inventory described as a count rather than as a list cannot answer any of the questions that follow.
*   **Data Flow and Recipients:** Where the data moves, and who receives it. The flow is what determines which transfers need a mechanism, and a flow that shows only the primary store hides the copies.

**2. Lawful Basis and Purpose Limitation**
*   **Processing Purposes and Necessity:** What each processing activity is for, and why it cannot be achieved with less data or a shorter reach. Necessity is assessed per purpose rather than per dataset, because one dataset frequently serves several purposes with very different necessity.
*   **Lawful Basis by Purpose:** One row per purpose: the data processed, the basis relied on, the basis for special category data where any is present, and the justification. A form that records a basis once for a dataset will carry one basis across purposes that do not share it.
*   **Purpose Compatibility and Secondary Use:** Whether the data is used for any purpose other than the one collected for, and on what basis. Secondary use is the most common privacy failure in analytics work and the one least likely to be noticed, because every individual field still has a lawful origin.
*   **Automated Decision-Making:** Any decision made about a person with no meaningful human involvement, the logic involved, and the consequences for them. Recorded because the assessment of a legal basis does not by itself establish that a decision is one a person could contest.

**3. Consent and Transparency**
*   **Consent Mechanism:** How consent is requested, and where in the flow it appears. Consent collected after the data is already in use is a record, not a request, and the difference determines what the record is worth.
*   **Consent Specificity and Granularity:** What the person was told they were consenting to, and whether the choices are separate. A single consent covering several purposes is consent to none of them in particular, and a bundle of pre-ticked boxes is not a choice.
*   **Consent Recording and Evidence:** Where each consent is stored, with the timestamp, the version of the text shown, and the interface shown. A consent record without the version of the text cannot be defended later, because the terms the person agreed to are then unrecoverable.
*   **Withdrawal:** How a person withdraws, how much easier it is than granting, and what happens to data already processed on that basis. Asymmetry between granting and withdrawing is the standard test, and a withdrawal that is honoured prospectively only leaves the processing intact behind it.
*   **Privacy Notices and Just-in-Time Disclosure:** What is told at collection, what is told at the point the data is used, and where either may be found. A notice published once and never revisited informs nobody who meets the processing for the first time in month three.

**4. Individual Rights**
*   **Rights Handling Process:** How a request is received, routed, decided and answered, and by whom. A right stated in a policy with no route to exercise it is a stated right, and it is tested only when someone uses it.
*   **Identity Verification:** How the requester is confirmed to be who they claim, and what is refused when that cannot be done. Verification that accepts anyone discloses data; verification that refuses everyone denies the right, and the balance is a decision to record rather than a default.
*   **Response Timeframes and Escalation:** The deadline for each type of request, what happens when it is missed, and who is told. The clock is the whole of the right in practice, because a correct answer delivered late is still a breach.
*   **Rights Over Derived, Shared and Retired Data:** What happens to a request where the data has been aggregated, shared with a third party, or placed in a model. Deletion cannot reach a trained model by deleting a row, and the form that does not say so will be read as having deleted it.

**5. Retention, Security and Sharing**
*   **Retention Schedule:** One row per data asset: the retention period, the basis for that period rather than the convention, what triggers deletion, and how deletion is verified. A period adopted as a default and recorded as a decision is the most common entry, and it is the reason data outlives every justification that justified it.
*   **Deletion Mechanism and Coverage:** How deletion is carried out, across primary stores, replicas, logs, exports and derived copies. Deleting a row from one table while the data persists in five other places is the most frequent finding in any such assessment, and it is invisible without a coverage statement.
*   **Backups and Derived Data:** How deletion propagates to backups and to models trained on the data, and over what period. Backups are the usual reason a deletion is incomplete, and a trained model is a copy no deletion request reaches.
*   **Access Controls and Least Privilege:** Who can reach the data, by what route, under what approval, and how access is reviewed. Access is the control that fails quietly, since misuse of legitimate credentials is indistinguishable from legitimate use without a review.
*   **Encryption and Key Management:** What is encrypted in transit and at rest, and who holds the keys. Encryption whose keys sit beside the data is a control on paper, and the key custody arrangement is the part that is not written down.
*   **Third-Party Sharing:** One row per recipient: the recipient, the purpose, the data shared, the contractual safeguard relied on, and the region processed in. Each row needs its own basis, because a processor bound by contract to a controller is not the same arrangement as a controller sharing on its own purpose.
*   **Cross-Border Transfers:** Where data or processing leaves the jurisdiction, under which transfer mechanism, and what supplementary measures apply. A hosting region is not a transfer analysis, and remote access by a foreign staff member is a transfer that no region setting records.
*   **Breach Notification:** What constitutes a breach here, who is notified, within what time, and who decides. Recorded because a response plan written after an incident is always written for that incident, and the decision threshold is the part that is usually left out.

**6. Ethics Beyond Compliance**
*   **Harm Beyond Legal Exposure:** Where this processing causes harm that no law prohibits. This section exists because compliance is a floor: processing can be lawful, consented, retained properly and shared properly, and still be wrong, and a form that stops at lawful has answered the question it was easy to answer.
*   **Vulnerable Individuals and Groups:** Who is affected in a state of reduced ability to refuse, to understand, or to bear the consequence. Vulnerability here is a property of the situation rather than of the person, and it is invisible to a record of categories and volumes.
*   **Transparency to Affected People:** What the people in the data are actually told, in language they use, as distinct from what the notice says. A notice that is accurate, complete and unread is the standard failure, and reading it as a recipient rather than as a drafter is the only way to see it.
*   **Manipulation, Dark Patterns and Consent Fatigue:** Whether the interface nudges, pre-ticks, buries refusal, or asks repeatedly, and whether the volume of requests is such that a refusal is impractical. Consent obtained by a design choice is not freely given, whatever the record says.
*   **Fairness of Automated Decisions:** Whether the processing produces outcomes for people, and what the distribution of those outcomes is across groups. A lawful basis for a decision is not a defence of its fairness, and the two are assessed against different questions.

**7. Findings, Remediation and Review**
*   **Findings Register:** One row per finding: the finding, the risk it poses to individuals, the severity, the owner, and the action being taken. Severity is what determines the order of work, and a register with no severity column is a list of observations.
*   **Residual Risk and Acceptance:** The risk remaining after the planned actions, who accepts it, and until when. Acceptance is a decision with an owner and an expiry date; an acceptance with neither is an unowned risk that will be rediscovered at the next assessment.
*   **Remediation Plan:** The actions, their owners and their dates, and what is being done in the interim. The interim period is where a known finding actually operates, so it is the part of the plan most worth writing down.
*   **Review Triggers:** What would cause this assessment to be revisited before its scheduled date, such as a new purpose, a new recipient, a new model, or a regulatory change. Triggers stated after the change have occurred are a record of the change.
*   **Reassessment Triggers:** When this assessment expires and on what cycle. An assessment with no expiry is treated as permanent by everyone who did not write it, including the people who inherited it.
-->

<h3 dir="ltr" align="right">{{Company_Name}}</h3>
<h2 dir="ltr" align="right">{{System_or_Initiative_Name}} - {{Assessment_ID}}</h2>
<h1 dir="ltr" align="center">DATA PRIVACY AND ETHICS ASSESSMENT</h1>

| **Date Prepared:** {{Current_Date}} | **Data Privacy Officer:** {{Data_Privacy_Officer_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |
---

## 1. Scope, Data Inventory and Ownership
<!-- What this assessment covers, what it does not, who owns and administers the data, what assets exist, and where the data moves. -->

**Assessment Scope:** [ Add details... ]

**Processing Out of Scope:** [ Add details... ]

**Data Owners and Custodians:** [ Add details... ]

**Data Inventory:**

| Data Asset | Owner | Stated Purpose | Personal Data | Special Category | Volume and Refresh |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

**Data Flow and Recipients:** [ Add details... ]

---

## 2. Lawful Basis and Purpose Limitation
<!-- What each processing is for and why it needs the data it uses, the basis relied on per purpose, any use beyond the original purpose, and any decision made about a person automatically. -->

**Processing Purposes and Necessity:** [ Add details... ]

**Lawful Basis by Purpose:**

| Purpose | Data Processed | Lawful Basis | Special Category Basis | Justification |
| :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

**Purpose Compatibility and Secondary Use:** [ Add details... ]

**Automated Decision-Making:** [ Add details... ]

---

## 3. Consent and Transparency
<!-- How consent is requested, what it covers, how it is evidenced, how it is withdrawn, and what the people in the data are told. -->

**Consent Mechanism:** [ Add details... ]

**Consent Specificity and Granularity:** [ Add details... ]

**Consent Recording and Evidence:** [ Add details... ]

**Withdrawal:** [ Add details... ]

**Privacy Notices and Just-in-Time Disclosure:** [ Add details... ]

---

## 4. Individual Rights
<!-- How a request for an individual's data is received, decided and answered in time, and what happens where the data has been derived, shared or used to build a model. -->

**Rights Handling Process:** [ Add details... ]

**Identity Verification:** [ Add details... ]

**Response Timeframes and Escalation:** [ Add details... ]

**Rights Over Derived, Shared and Retired Data:** [ Add details... ]

---

## 5. Retention, Security and Sharing
<!-- How long each asset is kept and on what basis, how deletion reaches every copy, who can reach the data, who else receives it, where it crosses a border, and what happens on a breach. -->

**Retention Schedule:**

| Data Asset | Retention Period | Basis for Period | Deletion Trigger | Deletion Verified |
| :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

**Deletion Mechanism and Coverage:** [ Add details... ]

**Backups and Derived Data:** [ Add details... ]

**Access Controls and Least Privilege:** [ Add details... ]

**Encryption and Key Management:** [ Add details... ]

**Third-Party Sharing:**

| Recipient | Purpose | Data Shared | Contractual Safeguard | Region |
| :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

**Cross-Border Transfers:** [ Add details... ]

**Breach Notification:** [ Add details... ]

---

## 6. Ethics Beyond Compliance
<!-- Where this processing causes harm that no law prohibits, who is affected while unable to refuse, what people are actually told, whether the interface permits a real choice, and how automated outcomes fall across groups. -->

**Harm Beyond Legal Exposure:** [ Add details... ]

**Vulnerable Individuals and Groups:** [ Add details... ]

**Transparency to Affected People:** [ Add details... ]

**Manipulation, Dark Patterns and Consent Fatigue:** [ Add details... ]

**Fairness of Automated Decisions:** [ Add details... ]

---

## 7. Findings, Remediation and Review
<!-- What was found, the risk remaining after the planned actions, what happens in the meantime, and what would cause this assessment to be reopened. -->

**Findings Register:**

| Finding | Risk to Individuals | Severity | Owner | Action |
| :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

**Residual Risk and Acceptance:** [ Add details... ]

**Remediation Plan:** [ Add details... ]

**Review Triggers:** [ Add details... ]

**Reassessment Triggers:** [ Add details... ]

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Data Protection Officer (DPO)** | {{DPO_Name}} | _______________________ | [ .... - .... - .... ] |
| **Legal / Compliance Counsel** | {{Legal_Counsel_Name}} | _______________________ | [ .... - .... - .... ] |
| **Project Manager** | {{Project_Manager_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> DATA PRIVACY AND ETHICS ASSESSMENT | <strong>Ref:</strong> PMO-02.06 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
