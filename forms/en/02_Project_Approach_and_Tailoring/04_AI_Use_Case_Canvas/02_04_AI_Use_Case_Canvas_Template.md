<!--
LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

Section Instructions:

**1. Use Case Identification**
*   **Use Case Name:** What this use case is called, and where it sits in the portfolio. Naming it makes it possible to say that a later system is the same use case grown, which is usually the difference between a second business case and a repeat of the first.
*   **Business Owner:** The person accountable for the outcome, who must be able to say what the system is for without reference to the model. An owner who describes the technology has not been identified.
*   **Problem Statement:** The specific problem, in the words of the person who has it, with the cost of leaving it unsolved. "Improve efficiency" is a goal; "a specialist spends forty minutes a day reconciling three spreadsheets" is a problem that can be sized and later checked.
*   **Affected Population:** Who experiences the problem, how many, and how often. The population is what converts an annoyance into a cost, and it is also the population the system will act upon.
*   **Current Workaround:** What people do today, and what it costs them. A workaround with no stated cost cannot be beaten, so the baseline here is what any proposal is measured against.

**2. Proposed Solution**
*   **AI Pattern:** The class of approach, and what makes it fit this problem rather than a neighbouring one. Classification, ranking, generation, forecasting and anomaly detection fail differently, and naming the pattern is what lets the failure modes be anticipated.
*   **Solution Description:** What the system does, in one paragraph a non-specialist can check. If the description requires the model architecture to be understood, the description is not yet a description.
*   **Human Role:** What a person still does, and at which points they can stop the system. A system described as assisting usually replaces something, and the thing replaced should be named so the change is visible to those affected.
*   **Scope Boundary:** What this use case explicitly does not include. Scope stated only as a positive is unbounded, and an unbounded use case absorbs its neighbours' costs.
*   **Assumptions:** What must be true for the solution to work, and what happens if each is not. Assumptions recorded after the build are records of what was believed, not of what was assumed.

**3. Data**
*   **Data Sources:** Where each input comes from, as a named system or collection with an owner. A source named only as "historical data" cannot be checked for permission, and permission is the first thing that blocks.
*   **Data Category and Volume:** What kind of data, at what volume and frequency. Frequency is the field most often omitted and the one that determines whether the system is retrained, refreshed or left to drift.
*   **Data Quality Status:** What is known about completeness, consistency and timeliness, and what has not been checked. Recording what was not checked is as useful as recording what was, because it bounds the confidence of the estimate.
*   **Labelling Requirement:** Whether labelled examples exist, who will produce them, and at what cost. This is usually the largest single line in the business case, and it is usually absent from it.
*   **Permitted Use and Access:** What the data may be used for within this use case, and who approves it. Where the data cannot be used for model training, the shape of the solution changes, and that is better known before than after.

**4. Value and Cost**
*   **Value Proposition:** What changes for whom, expressed as a change in the process rather than a return figure. A return calculated before the operating cost is a number that survives no review.
*   **Value Measurement Method:** How the value will be measured, against what baseline, and by whom. Value stated without a baseline is a claim, and the baseline is usually already recorded in the current-workaround cost above.
*   **Beneficiaries:** Who gains, and who bears the cost of the change. These are rarely the same people, and the form is the place where the second group becomes visible.
*   **Build Cost:** What it will cost to build, and what is included. The cost that is excluded is the operating cost below, and stating the exclusion is what keeps the total honest.
*   **Operating Cost:** What it will cost to run per unit of work, and at what volume. Cost per unit rather than total, because the total scales with volume and the viability question is asked per unit.
*   **Value Realisation Condition:** What must be true for the value to be realised, as distinct from for the system to be built. Most systems are built successfully and deliver nothing, and the difference is nearly always one of these conditions.

**5. Risks, Controls and Governance Route**
*   **Key Risks:** The risks specific to this use case, ranked, with the consequence if each materialises. A generic risk register applied here records that data may be biased without saying for whom or how it would be detected.
*   **Risk Controls:** What is in place for each risk, and what it does not cover. The second half is the useful half, and a control that covers everything is a control that has been described rather than designed.
*   **Feasibility Assessment:** Whether this is technically feasible, at what maturity, and what is unproven. A feasibility statement that does not say which part is unproven is a statement that all of it is proven.
*   **Governance Route:** Which governance artefacts this use case must pass through, and in what order. The order is the content: privacy, then fairness, then approval, because a system approved before its data is assessed cannot be un-approved.
*   **Kill Criteria:** What result would cause this use case to be stopped. A use case with no kill criteria is a commitment, and a commitment entered without an exit condition is the failure mode this field exists to prevent.
*   **Related Artefacts:** The business case, AI governance plan, model card and privacy assessment for this use case, so that a reader holding the canvas can find the decisions that depend on it.
-->

<h3 dir="ltr" align="right">{{Company_Name}}</h3>
<h2 dir="ltr" align="right">{{AI_Solution_Name}} - {{Use_Case_ID}}</h2>
<h1 dir="ltr" align="center">AI USE CASE CANVAS</h1>

| **Date Prepared:** {{Current_Date}} | **AI Product Owner:** {{AI_Product_Owner_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |

---

## 1. Use Case Identification
<!-- What this is called, who owns the outcome, the problem in the words of the person who has it, who it affects, and what people do today. -->

**Use Case Name:** [ Add details... ]

**Business Owner:** [ Add details... ]

**Problem Statement:** [ Add details... ]

**Affected Population:** [ Add details... ]

**Current Workaround:** [ Add details... ]

---

## 2. Proposed Solution
<!-- The class of approach, what the system does in terms a non-specialist can check, what a person still does, what is out of scope, and what must be true for it to work. -->

**AI Pattern:** [ Add details... ]

**Solution Description:** [ Add details... ]

**Human Role:** [ Add details... ]

**Scope Boundary:** [ Add details... ]

**Assumptions:** [ Add details... ]

---

## 3. Data
<!-- One row per source: where it comes from, what it is, what is known about its quality, what labelling is required, and what use is permitted. -->

| Data Source | Data Category and Volume | Data Quality Status | Labelling Requirement | Permitted Use and Access |
| :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 4. Value and Cost
<!-- The value, how it will be measured and against what baseline, who gains and who bears the cost, and the build and operating costs kept separate. -->

**Value Proposition:** [ Add details... ]

**Value Measurement Method:** [ Add details... ]

**Beneficiaries:** [ Add details... ]

**Build Cost:** [ Add details... ]

**Operating Cost:** [ Add details... ]

**Value Realisation Condition:** [ Add details... ]

---

## 5. Risks, Controls and Governance Route
<!-- The risks specific to this use case and what they would cause, what is in place and what it does not cover, whether it is feasible, which governance it passes through, and what would stop it. -->

**Key Risks:** [ Add details... ]

**Risk Controls:** [ Add details... ]

**Feasibility Assessment:** [ Add details... ]

**Governance Route:** [ Add details... ]

**Kill Criteria:** [ Add details... ]

**Related Artefacts:** [ Add details... ]

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Product / Business Owner** | {{Business_Owner_Name}} | _______________________ | [ .... - .... - .... ] |
| **AI Technical Lead** | {{AI_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
| **Project Sponsor** | {{Project_Sponsor_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> AI USE CASE CANVAS | <strong>Ref:</strong> PMO-02.04 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
