---
type: Guide
---

<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/02_Project_Approach_and_Tailoring/03_AI_Readiness_Assessment/02_03_AI_Readiness_Assessment_Template.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="../../ar/02_منهجية_المشروع_وتخصيصه/02_03_تقييم_جاهزية_الذكاء_الاصطناعي_قالب.html">🇸🇦 الانتقال للنسخة العربية (Arabic Template) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-02.03</span>
    <span class="badge badge-phase">02. Project Approach & Tailoring</span>
    <span class="badge badge-standard">PMI PMBOK® 6/7/8 • ISO 21500</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill active" href="#">📋 Blank Template</a>
    <a class="nav-pill" href="../../../guides/en/02_Project_Approach_and_Tailoring/02_03_AI_Readiness_Assessment_Guide.html">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../examples/en/02_Project_Approach_and_Tailoring/02_03_AI_Readiness_Assessment_Example.html">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/02_Project_Approach_and_Tailoring/03_AI_Readiness_Assessment/02_03_AI_Readiness_Assessment_Template.md" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="../../ar/02_منهجية_المشروع_وتخصيصه/02_03_تقييم_جاهزية_الذكاء_الاصطناعي_قالب.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

<!--
LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

Section Instructions:

**1. Purpose and Scope of the Assessment**
*   **Assessment Objective:** What decision this assessment is being made to support, and what decision it is not. A readiness assessment with no stated decision attached is a score, and a score nobody needs is the one most often abandoned.
*   **Assessment Scope:** Which systems, processes and teams are in scope, and which are excluded. Excluding something is legitimate; excluding it without writing it down is what lets it reappear as a dependency in month four.
*   **Assessment Method:** How each dimension was assessed: instrumented measurement, walkthrough, interview, or self-declaration. Self-declaration is legitimate and must be labelled, because an unlabelled self-declaration is indistinguishable from a measurement and is trusted accordingly.
*   **Assessor and Date:** Who performed it, on what date, and against which version of the systems. A readiness figure without a date is a figure that decays silently.
*   **Evidence Basis:** What the scores rest on, and where the evidence sits. A score whose source cannot be retrieved cannot be defended when it is challenged, which is the only time its accuracy matters.

**2. Data Readiness**
*   **Data Availability:** Whether the data the use case requires exists, at the volume and coverage needed. Availability is not the same as permission, and the gap between them is the most common reason a data-ready organisation is not an AI-ready one.
*   **Data Quality:** Completeness, consistency, timeliness and validity, each with the measurement used. "Good quality" is a conclusion; a completeness figure against a defined field list is an input to one.
*   **Data Lineage and Documentation:** Whether it can be traced to its origin and meaning. Lineage is what makes a defective output diagnosable rather than merely wrong, and it cannot be reconstructed after the fact.
*   **Labelling and Ground Truth:** Whether labelled examples exist for the intended purpose, in sufficient quantity and quality. Where they do not, say so, because labelling is a programme of work with a cost and a duration, and treating it as a task hides both.
*   **Data Governance and Access:** Who may access what, under what controls, and whether that is settled. Access rights settled late are the usual cause of a launch delay that no one predicted, and they are settled late because they involve people outside the team.

**3. Technical and Platform Readiness**
*   **Compute and Capacity:** Whether the capacity required for training and inference exists, and at what cost. Cost per unit of work is the figure that decides whether the use case is viable at volume, and it is not known until the volume is.
*   **Platform and Tooling:** MLOps, versioning, experiment tracking, deployment and monitoring. The tooling question is not whether a notebook runs but whether a model can be reproduced, rolled back, and monitored in production, since those are the operations a team inherits.
*   **Integration:** Whether the system connects to the surrounding estate, and at what quality. Integration is where readiness assessments are optimistic, because a proof of concept connects to nothing and a production system must connect to everything.
*   **Security and Resilience:** The controls in force for AI workloads, and what happens when the system is unavailable. A system whose fallback is manual reverts to a process that was automated because it was unworkable by hand.
*   **Scalability:** Whether performance and cost hold as volume grows. A model that is accurate and unaffordable at ten times the volume is a prototype, and the assessment is where that is cheapest to discover.

**4. Skills and Team Readiness**
*   **Team Composition:** Who is on the team, and which of the required roles are unfilled. List the gaps by role rather than by competence, because a gap named by competence has no owner and a gap named by role has a vacancy.
*   **AI Skills:** The specific capabilities present, at what level: building, evaluating, deploying, and operating. These are different skills and a team strong in the first may be unable to do the third, which is where readiness usually fails.
*   **Domain Expertise:** Whether the team includes people who know the domain well enough to judge an output is wrong. Without them the team can measure performance and not interpret it, and those are not separable.
*   **Capacity and Availability:** Whether the people named are actually available at the required fraction, given other commitments. A team rostered at half time and a team absent are the same fact expressed differently.
*   **Capability Building:** How gaps will be closed: hire, train, partner, or buy. These have different lead times and the lead time is the constraint, not the preference.

**5. Organisational Readiness**
*   **Leadership Sponsorship:** Whether there is a sponsor who will fund the consequences as well as the work. Sponsorship that ends at approval has funded a demonstration, and the difference surfaces at the first decision the system makes that somebody disputes.
*   **Operating Model:** Who runs the system in production, and under which service commitment. An operating model decided at go-live is an operating model negotiated in an incident.
*   **Change and Adoption:** Who must change their work, what they gain, and what they lose. A system that makes someone's judgement redundant will not be adopted regardless of its accuracy, and adoption is not a communications problem.
*   **Procurement and Contracting:** Whether the contracts permit the intended use, and what they permit the supplier to do with the data. These are the obligations that cannot be renegotiated after the data has been shared.
*   **Risk Appetite:** What level of failure the organisation will accept, and who accepts it on its behalf. A risk appetite that is never stated becomes, by default, zero tolerance, which is not a position anyone chose.

**6. Assessment Outcome and Route Forward**
*   **Dimension Scores:** The score for each dimension, with the scale used stated. A score without its scale cannot be compared with a later assessment, and the comparison is the only reason to take the first one.
*   **Weighted Overall Score:** The aggregate, with the weights and their justification. An unweighted average treats a dimension the business does not depend on as equal to one it cannot operate without.
*   **Blocking Gaps:** The gaps that prevent proceeding, as distinct from those that slow it. This distinction is the assessment's actual output, and a form that records a single list cannot make it.
*   **Recommended Route:** Proceed, proceed with conditions, remediate, or do not proceed, and the condition attached. The route without its conditions is an opinion; the conditions are what can be tracked and closed.
*   **Remediation Plan:** What will be done, by whom, by when, and what it costs. A gap with no owner and no date is not a gap in the plan, it is a gap in the plan's assumptions.
*   **Reassessment Trigger:** What would cause the assessment to be repeated. Readiness decays as staff move and data drifts, and an assessment with no expiry is treated as current indefinitely.
-->

<h3 dir="ltr" align="right">{{Company_Name}}</h3>
<h2 dir="ltr" align="right">{{AI_System_or_Program_Name}} - {{Assessment_ID}}</h1>
<h1 dir="ltr" align="center">AI READINESS ASSESSMENT</h1>

| **Date Prepared:** {{Current_Date}} | **AI Governance Lead:** {{AI_Governance_Lead_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |

---

## 1. Purpose and Scope of the Assessment
<!-- What decision this assessment supports, what is in and out of scope, how it was assessed, and what the scores rest on. -->

**Assessment Objective:** [ Add details... ]

**Assessment Scope:** [ Add details... ]

**Assessment Method:** [ Add details... ]

**Assessor and Date:** [ Add details... ]

**Evidence Basis:** [ Add details... ]

---

## 2. Data Readiness
<!-- One row per data source: does the data exist, is it fit, can it be traced, is it labelled, and is access settled. -->

| Data Source | Data Availability | Data Quality | Data Lineage and Documentation | Labelling and Ground Truth | Data Governance and Access |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 3. Technical and Platform Readiness
<!-- One row per platform concern: capacity, tooling, integration, resilience, and what happens as volume grows. -->

| Concern | Current State | Gap | Cost and Effort to Close | Severity |
| :--- | :--- | ---: | :--- | :---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 4. Skills and Team Readiness
<!-- One row per role: whether it is filled, what the person can actually do, and how the gap closes. -->

| Role | Filled | Level | Domain Knowledge | How the Gap Closes |
| :--- | :--- | :---: | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 5. Organisational Readiness
<!-- One row per organisational condition, with the evidence rather than the assertion, and who owns closing it. -->

| Condition | Current State | Evidence | Owner | Note |
| :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 6. Assessment Outcome and Route Forward
<!-- The scores, the aggregate and its weights, the gaps that block rather than slow, the recommended route, and what would reopen the assessment. -->

**Dimension Scores:** [ Add details... ]

**Weighted Overall Score:** [ Add details... ]

**Blocking Gaps:** [ Add details... ]

**Recommended Route:** [ Add details... ]

**Remediation Plan:** [ Add details... ]

**Reassessment Trigger:** [ Add details... ]

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :---: | :---: |
| **AI / Data Lead** | {{AI_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
| **Enterprise Architect / IT Lead** | {{IT_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
| **Project Sponsor** | {{Project_Sponsor_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;" markdown="1">
  <strong>Template:</strong> AI READINESS ASSESSMENT | <strong>Ref:</strong> PMO-02.03 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
