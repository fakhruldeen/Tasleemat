<div class="lang-switch-bar">
  <span>🌐 Dual Language / ثنائي اللغة:</span>
  <a class="lang-switch-btn" href="../../ar/02_منهجية_المشروع_وتخصيصه/02_04_نموذج_حالة_استخدام_الذكاء_الاصطناعي_دليل.md">🇸🇦 الانتقال للدليل بالعربية (Arabic Guide)</a>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-02.04</span>
    <span class="badge badge-phase">02. Project Approach & Tailoring</span>
    <span class="badge badge-type">Authoring & Governance Guide</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="../../../templates/en/02_Project_Approach_and_Tailoring/02_04_AI_Use_Case_Canvas_Template.md">📋 Blank Template</a>
    <a class="nav-pill active" href="#">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../examples/en/02_Project_Approach_and_Tailoring/02_04_AI_Use_Case_Canvas_Example.md">💡 Completed Example</a>
    <a class="nav-pill lang-pill" href="../../ar/02_منهجية_المشروع_وتخصيصه/02_04_نموذج_حالة_استخدام_الذكاء_الاصطناعي_دليل.md">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

---
lang: en
layout: default
title: AI Use Case Canvas
nav_order: 1
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">

## Tasleemat Forms Guide
# Project Artifact: AI Use Case Canvas

**Document Reference:** `PMO-02.04`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **AI Use Case Canvas** in alignment
with the Tasleemat framework.

---

### 1. What?
A statement of one proposed AI use that can be argued with before anything is built. It names the use case and its business owner, states the problem in the words of the person who has it with the cost of leaving it unsolved, records the population affected and the workaround in use today, describes the proposed approach and what a person still does, tabulates each data source with its volume, quality status, labelling requirement and permitted use, states the value against a baseline together with the build and operating costs separately, and closes with the risks specific to this use case, the controls and what they do not cover, the governance route in order, and the kill criteria.

---

### 2. Why?
Because a use case is cheap to abandon and expensive to abandon late. The canvas is the only document in the set written before any work exists, so it is the only place where a wrong assumption costs nothing to find. Each of the expensive discoveries has a corresponding field here: data that cannot be used for training, labelling nobody costed, an operating cost that scales faster than the value, a value claim with no baseline, and a risk that turns out to belong to a neighbouring use case.

The discipline the form imposes is separation, as in the readiness assessment but applied to a single proposal. Value is not return. Build cost is not operating cost. Feasible is not proven. Approved is not approved after its data was assessed. A kill criterion is not a risk mitigation. Each of these is a distinct claim, and stating them as one is what allows a use case to pass review and fail in production.

---

### 3. When?
This artifact is primarily prepared, utilized, and updated during the **PROJECT APPROACH AND TAILORING Process Group** of the project lifecycle. It is drafted when a use case is proposed, before any build begins, and revised when the data position or the value measurement changes, since both are the fields most likely to have been recorded optimistically.

---

### 4. Who?
**Responsibilities:** Owned by the Business Owner, who must be able to state the purpose of the system without reference to the model; an owner who describes the technology has not been identified. Completed with the AI or ML Lead, who is accountable for the feasibility statement and for naming which part of it is unproven, and with the Data Protection Officer, who is accountable for the permitted-use and access column. Reviewed by the Project Manager against the business case, and approved by the sponsor, who is the person the kill criteria will later be applied to.

---

### Tailoring Tips
*   A canvas may be brief where the use case is an extension of one already assessed, provided the name makes the parentage explicit and the differences from the assessed version are stated, since an unnamed variant reopens the whole assessment.
*   Where several use cases share a data source, the source may be documented once with a shared reference, but the labelling requirement and permitted use must be restated per use case, because a shared source is the usual point at which a use case quietly acquires data it was never approved for.
*   The kill criteria may be expressed as a threshold against a measure already in the value method, which is preferable to a separate one, since a criterion that needs its own measurement will not be checked.
*   It is worth recording which sections were considered and deliberately left thin, as this is the record that shows the canvas was a judgement rather than an omission.
*   A canvas should be superseded rather than edited in place once approved, so that the version presented for a funding decision remains the version that was presented.
*   Where the use case is procured, the feasibility and data sections should record what the supplier contract obliges, since a capability the organisation assumes is inherited is not one it has.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   AI Readiness Assessment (PMO-02.03)
    *   Business Case (PMO-01.01)
*   **Optional / Contextual:**
    *   Product Vision (PMO-03.02)
    *   Stakeholder Analysis (PMO-03.05)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Project Charter (PMO-03.01)
    *   AI Governance Plan (PMO-02.02)
    *   Requirements Documentation (PMO-04.02.03)
*   **Optional / Contextual:**
    *   User Story Mapping (PMO-04.02.09)
    *   AI Model Card (PMO-02.05)

---

### 5. How?
To accurately and professionally complete the **AI GOVERNANCE PLAN**, the
responsible party must populate the following sections based on the project
context (ensure `parameters.md` is referenced for global project variables):

*   **Use Case Name:** What this use case is called, and where it sits in the portfolio. Naming it makes it possible to say that a later system is the same use case grown, which is usually the difference between a second business case and a repeat of the first.
*   **Business Owner:** The person accountable for the outcome, who must be able to say what the system is for without reference to the model. An owner who describes the technology has not been identified.
*   **Problem Statement:** The specific problem, in the words of the person who has it, with the cost of leaving it unsolved. "Improve efficiency" is a goal; "a specialist spends forty minutes a day reconciling three spreadsheets" is a problem that can be sized and later checked.
*   **Affected Population:** Who experiences the problem, how many, and how often. The population is what converts an annoyance into a cost, and it is also the population the system will act upon.
*   **Current Workaround:** What people do today, and what it costs them. A workaround with no stated cost cannot be beaten, so the baseline here is what any proposal is measured against.
*   **AI Pattern:** The class of approach, and what makes it fit this problem rather than a neighbouring one. Classification, ranking, generation, forecasting and anomaly detection fail differently, and naming the pattern is what lets the failure modes be anticipated.
*   **Solution Description:** What the system does, in one paragraph a non-specialist can check. If the description requires the model architecture to be understood, the description is not yet a description.
*   **Human Role:** What a person still does, and at which points they can stop the system. A system described as assisting usually replaces something, and the thing replaced should be named so the change is visible to those affected.
*   **Scope Boundary:** What this use case explicitly does not include. Scope stated only as a positive is unbounded, and an unbounded use case absorbs its neighbours' costs.
*   **Assumptions:** What must be true for the solution to work, and what happens if each is not. Assumptions recorded after the build are records of what was believed, not of what was assumed.
*   **Data Sources:** Where each input comes from, as a named system or collection with an owner. A source named only as "historical data" cannot be checked for permission, and permission is the first thing that blocks.
*   **Data Category and Volume:** What kind of data, at what volume and frequency. Frequency is the field most often omitted and the one that determines whether the system is retrained, refreshed or left to drift.
*   **Data Quality Status:** What is known about completeness, consistency and timeliness, and what has not been checked. Recording what was not checked is as useful as recording what was, because it bounds the confidence of the estimate.
*   **Labelling Requirement:** Whether labelled examples exist, who will produce them, and at what cost. This is usually the largest single line in the business case, and it is usually absent from it.
*   **Permitted Use and Access:** What the data may be used for within this use case, and who approves it. Where the data cannot be used for model training, the shape of the solution changes, and that is better known before than after.
*   **Value Proposition:** What changes for whom, expressed as a change in the process rather than a return figure. A return calculated before the operating cost is a number that survives no review.
*   **Value Measurement Method:** How the value will be measured, against what baseline, and by whom. Value stated without a baseline is a claim, and the baseline is usually already recorded in the current-workaround cost above.
*   **Beneficiaries:** Who gains, and who bears the cost of the change. These are rarely the same people, and the form is the place where the second group becomes visible.
*   **Build Cost:** What it will cost to build, and what is included. The cost that is excluded is the operating cost below, and stating the exclusion is what keeps the total honest.
*   **Operating Cost:** What it will cost to run per unit of work, and at what volume. Cost per unit rather than total, because the total scales with volume and the viability question is asked per unit.
*   **Value Realisation Condition:** What must be true for the value to be realised, as distinct from for the system to be built. Most systems are built successfully and deliver nothing, and the difference is nearly always one of these conditions.
*   **Key Risks:** The risks specific to this use case, ranked, with the consequence if each materialises. A generic risk register applied here records that data may be biased without saying for whom or how it would be detected.
*   **Risk Controls:** What is in place for each risk, and what it does not cover. The second half is the useful half, and a control that covers everything is a control that has been described rather than designed.
*   **Feasibility Assessment:** Whether this is technically feasible, at what maturity, and what is unproven. A feasibility statement that does not say which part is unproven is a statement that all of it is proven.
*   **Governance Route:** Which governance artefacts this use case must pass through, and in what order. The order is the content: privacy, then fairness, then approval, because a system approved before its data is assessed cannot be un-approved.
*   **Kill Criteria:** What result would cause this use case to be stopped. A use case with no kill criteria is a commitment, and a commitment entered without an exit condition is the failure mode this field exists to prevent.
*   **Related Artefacts:** The business case, AI governance plan, model card and privacy assessment for this use case, so that a reader holding the canvas can find the decisions that depend on it.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](../../../templates/en/02_Project_Approach_and_Tailoring/02_04_AI_Use_Case_Canvas_Template.md)
* **🤖 LLM Generation Prompt**
* **📊 Data Structure (JSON)**
* **📈 Tabular Data (CSV)**

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [02_04_AI_Use_Case_Canvas_Example.md](../../../examples/en/02_Project_Approach_and_Tailoring/02_04_AI_Use_Case_Canvas_Example.md)

</div>
