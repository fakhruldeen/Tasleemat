---
lang: en
layout: default
title: AI Readiness Assessment
nav_order: 1
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">

## Tasleemat Forms Guide
# Project Artifact: AI Readiness Assessment

**Document Reference:** `PMO-02.03`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **AI Readiness Assessment** in alignment
with the Tasleemat framework.

---

### 1. What?
A dated, evidence-backed judgement on whether the organisation is in a position to build the proposed AI capability, and on what terms. It states the decision the assessment supports and its scope, how each dimension was assessed and by whom, then works through data readiness, technical and platform readiness, skills and team readiness, and organisational readiness, and closes with the dimension scores, the weighted aggregate, the gaps that block rather than slow, the recommended route with its conditions, the remediation plan, and what would cause the assessment to be repeated.

---

### 2. Why?
Because the question is asked before the work starts, and the cheapest time to discover that the labelled data does not exist, the access rights are unsettled, or the only person who understands the domain is on another project is before any of it has been built. Each of those is recoverable in week two and very expensive in month six.

The discipline the form imposes is separation. Availability is not permission. A blocked build is not a slow build. A self-declaration is not a measurement. An unweighted average is not a score. Each of these collapses two different facts into one, and the collapse is what allows a programme to proceed on a figure that concealed the gap it would later be stopped by.

---

### 3. When?
This artifact is primarily prepared, utilized, and updated during the **PROJECT APPROACH AND TAILORING Process Group** of the project lifecycle. It is performed before commitment to the initiative, revisited at each phase gate, and repeated on a stated trigger rather than on demand, because readiness decays as staff move and data drifts.

---

### 4. Who?
**Responsibilities:** Performed by the AI or ML Lead jointly with the Data Owner, since a readiness assessment of data performed without the person who owns access rights is a readiness assessment of the wrong thing. Reviewed by the Project Manager against the remediation plan, and approved by the Project Sponsor, who owns the consequence of proceeding on an optimistic reading. Where a dimension is self-declared, the declaring party is named, so that later questions about the score have someone to put to them.

---

### Tailoring Tips
*   A small exploratory initiative may assess two or three dimensions only, but should still state which were assessed and which were not, since an unstated omission reads as a pass.
*   Where the capability is procured rather than built, the technical readiness section should be replaced by a supplier-capability section, and the assessment should record what the contract obliges the supplier to provide, since a capability assumed to be inherited is not a capability the organisation has.
*   Scores from a previous assessment should be carried forward and compared rather than re-derived, because the comparison is what shows whether remediation worked, and a fresh absolute score cannot show that.
*   It is worth recording the dimensions deliberately excluded and the reason, as these are the ones that reappear as dependencies once work is under way.
*   The remediation plan may reference a separate initiative rather than duplicating it, provided each blocking gap still carries an owner and a date here, since a gap tracked elsewhere is a gap nobody is tracking.
*   Where the organisation has assessed before, retain the superseded assessment rather than overwriting it; the trend is the only evidence that the process is working.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Business Case (PMO-01.01)
    *   Data & Technical Architecture Baseline
*   **Optional / Contextual:**
    *   Portfolio Roadmap (PMO-00.01)
    *   Strategic AI Goals

#### 2. Downstream Dependents
*   **Mandatory:**
    *   AI Governance Plan (PMO-02.02)
    *   AI Use Case Canvas (PMO-02.04)
*   **Optional / Contextual:**
    *   Resource Capacity Matrix (PMO-00.04)
    *   Procurement Plan (PMO-04.09.01)

---

### 5. How?
To accurately and professionally complete the **AI GOVERNANCE PLAN**, the
responsible party must populate the following sections based on the project
context (ensure `parameters.md` is referenced for global project variables):

*   **Assessment Objective:** What decision this assessment is being made to support, and what decision it is not. A readiness assessment with no stated decision attached is a score, and a score nobody needs is the one most often abandoned.
*   **Assessment Scope:** Which systems, processes and teams are in scope, and which are excluded. Excluding something is legitimate; excluding it without writing it down is what lets it reappear as a dependency in month four.
*   **Assessment Method:** How each dimension was assessed: instrumented measurement, walkthrough, interview, or self-declaration. Self-declaration is legitimate and must be labelled, because an unlabelled self-declaration is indistinguishable from a measurement and is trusted accordingly.
*   **Assessor and Date:** Who performed it, on what date, and against which version of the systems. A readiness figure without a date is a figure that decays silently.
*   **Evidence Basis:** What the scores rest on, and where the evidence sits. A score whose source cannot be retrieved cannot be defended when it is challenged, which is the only time its accuracy matters.
*   **Data Availability:** Whether the data the use case requires exists, at the volume and coverage needed. Availability is not the same as permission, and the gap between them is the most common reason a data-ready organisation is not an AI-ready one.
*   **Data Quality:** Completeness, consistency, timeliness and validity, each with the measurement used. "Good quality" is a conclusion; a completeness figure against a defined field list is an input to one.
*   **Data Lineage and Documentation:** Whether it can be traced to its origin and meaning. Lineage is what makes a defective output diagnosable rather than merely wrong, and it cannot be reconstructed after the fact.
*   **Labelling and Ground Truth:** Whether labelled examples exist for the intended purpose, in sufficient quantity and quality. Where they do not, say so, because labelling is a programme of work with a cost and a duration, and treating it as a task hides both.
*   **Data Governance and Access:** Who may access what, under what controls, and whether that is settled. Access rights settled late are the usual cause of a launch delay that no one predicted, and they are settled late because they involve people outside the team.
*   **Compute and Capacity:** Whether the capacity required for training and inference exists, and at what cost. Cost per unit of work is the figure that decides whether the use case is viable at volume, and it is not known until the volume is.
*   **Platform and Tooling:** MLOps, versioning, experiment tracking, deployment and monitoring. The tooling question is not whether a notebook runs but whether a model can be reproduced, rolled back, and monitored in production, since those are the operations a team inherits.
*   **Integration:** Whether the system connects to the surrounding estate, and at what quality. Integration is where readiness assessments are optimistic, because a proof of concept connects to nothing and a production system must connect to everything.
*   **Security and Resilience:** The controls in force for AI workloads, and what happens when the system is unavailable. A system whose fallback is manual reverts to a process that was automated because it was unworkable by hand.
*   **Scalability:** Whether performance and cost hold as volume grows. A model that is accurate and unaffordable at ten times the volume is a prototype, and the assessment is where that is cheapest to discover.
*   **Team Composition:** Who is on the team, and which of the required roles are unfilled. List the gaps by role rather than by competence, because a gap named by competence has no owner and a gap named by role has a vacancy.
*   **AI Skills:** The specific capabilities present, at what level: building, evaluating, deploying, and operating. These are different skills and a team strong in the first may be unable to do the third, which is where readiness usually fails.
*   **Domain Expertise:** Whether the team includes people who know the domain well enough to judge an output is wrong. Without them the team can measure performance and not interpret it, and those are not separable.
*   **Capacity and Availability:** Whether the people named are actually available at the required fraction, given other commitments. A team rostered at half time and a team absent are the same fact expressed differently.
*   **Capability Building:** How gaps will be closed: hire, train, partner, or buy. These have different lead times and the lead time is the constraint, not the preference.
*   **Leadership Sponsorship:** Whether there is a sponsor who will fund the consequences as well as the work. Sponsorship that ends at approval has funded a demonstration, and the difference surfaces at the first decision the system makes that somebody disputes.
*   **Operating Model:** Who runs the system in production, and under which service commitment. An operating model decided at go-live is an operating model negotiated in an incident.
*   **Change and Adoption:** Who must change their work, what they gain, and what they lose. A system that makes someone's judgement redundant will not be adopted regardless of its accuracy, and adoption is not a communications problem.
*   **Procurement and Contracting:** Whether the contracts permit the intended use, and what they permit the supplier to do with the data. These are the obligations that cannot be renegotiated after the data has been shared.
*   **Risk Appetite:** What level of failure the organisation will accept, and who accepts it on its behalf. A risk appetite that is never stated becomes, by default, zero tolerance, which is not a position anyone chose.
*   **Dimension Scores:** The score for each dimension, with the scale used stated. A score without its scale cannot be compared with a later assessment, and the comparison is the only reason to take the first one.
*   **Weighted Overall Score:** The aggregate, with the weights and their justification. An unweighted average treats a dimension the business does not depend on as equal to one it cannot operate without.
*   **Blocking Gaps:** The gaps that prevent proceeding, as distinct from those that slow it. This distinction is the assessment's actual output, and a form that records a single list cannot make it.
*   **Recommended Route:** Proceed, proceed with conditions, remediate, or do not proceed, and the condition attached. The route without its conditions is an opinion; the conditions are what can be tracked and closed.
*   **Remediation Plan:** What will be done, by whom, by when, and what it costs. A gap with no owner and no date is not a gap in the plan, it is a gap in the plan's assumptions.
*   **Reassessment Trigger:** What would cause the assessment to be repeated. Readiness decays as staff move and data drifts, and an assessment with no expiry is treated as current indefinitely.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](02_03_AI_Readiness_Assessment_Template.md)
* [🤖 LLM Generation Prompt](02_03_AI_Readiness_Assessment.md)
* [📊 Data Structure (JSON)](02_03_AI_Readiness_Assessment.json)
* [📈 Tabular Data (CSV)](02_03_AI_Readiness_Assessment.csv)

</div>
