<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/02_Project_Approach_and_Tailoring/02_AI_Governance_Plan/02_02_AI_Governance_Plan_Template.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="../../ar/02_منهجية_المشروع_وتخصيصه/02_02_خطة_حوكمة_الذكاء_الاصطناعي_قالب.html">🇸🇦 الانتقال للنسخة العربية (Arabic Template) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-02.02</span>
    <span class="badge badge-phase">02. Project Approach & Tailoring</span>
    <span class="badge badge-standard">PMI PMBOK® 6/7/8 • ISO 21500</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill active" href="#">📋 Blank Template</a>
    <a class="nav-pill" href="../../../guides/en/02_Project_Approach_and_Tailoring/02_02_AI_Governance_Plan_Guide.html">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../examples/en/02_Project_Approach_and_Tailoring/02_02_AI_Governance_Plan_Example.html">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/02_Project_Approach_and_Tailoring/02_AI_Governance_Plan/02_02_AI_Governance_Plan_Template.md" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="../../ar/02_منهجية_المشروع_وتخصيصه/02_02_خطة_حوكمة_الذكاء_الاصطناعي_قالب.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

<!--
LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

Section Instructions:

**1. Governance Context and Scope**
*   **AI System Inventory:** What the system is, at the version that will actually run, and who operates it. Record the version, because a governance plan that covers "the model" covers whichever model happens to be deployed when someone asks, and the answer is rarely the one that was assessed.
*   **Intended Purpose and Affected Users:** What the system is for, and who is subject to its output rather than merely its user. The two are routinely confused, and the confusion is how a system that screens applicants comes to be described as a tool that helps recruiters write better.
*   **Risk Classification:** The tier assigned and the criteria that put it there, not the tier alone. A classification with no stated criteria cannot be challenged, and an unchallengeable classification is the same as no classification.
*   **Scope Exclusions:** What this plan explicitly does not cover, and who owns it instead. Governance plans fail at the boundary: the component nobody assigned sits under a plan that assumed it was included.

**2. Ethical Principles and Acceptable Use**
*   **Ethical Principles:** The principles that constrain use on this project, and the case in which one yields to another. Principles that cannot yield to each other are not a decision rule, and a project under time pressure will resolve the conflict silently and after the fact.
*   **Prohibited Uses:** Uses that are refused regardless of benefit. This section is what the plan is for, and a plan listing only permitted uses has no way to refuse anything.
*   **Approved Use Cases:** The uses that are approved, each with the limits within which it stays approved. An approved use without stated limits is an approved capability, not an approved use.
*   **Human Impact Assessment:** Who bears the consequences of a wrong output, and whether they can tell it was wrong. A system whose subject cannot detect its own errors transfers the cost of error to the person least able to contest it.

**3. Data Governance**
*   **Data Category:** What kind of data, in terms a data subject would recognise as being about them.
*   **Provenance and Lawful Basis:** Where the data came from and under what basis it is processed. Data that arrived with the model cannot have its basis added later, so a model trained before this question was asked holds data whose status nobody can now evidence.
*   **Permitted Use:** What the data may be used for within this system, and what it may not. The most common governance failure is not a leak but reuse for a purpose nobody re-approved.
*   **Protection Control:** The specific control applied, not the category of control. "Encrypted" is a category, and the sentence that matters is which key, held by whom, and rotated how.
*   **Retention and Deletion:** When the data is deleted, and how deletion is verified. Deletion that is asserted rather than evidenced is how a training set outlives the project that justified it.

**4. Fairness, Bias and Transparency**
*   **Affected Group:** The group whose outcomes are affected, named. Groups are described in aggregate on the basis of a test, and the group that matters is the one that performs worst on it.
*   **Bias Risk:** The specific way this system could be unfair to this group, stated so it could be false. "Bias risk" as a heading is not a risk; "the model scores this group lower on historic completion rates" is a risk that can be measured and can turn out to be wrong.
*   **Test Method and Threshold:** How it is tested and what result triggers action, with the threshold written before the result is known. A threshold set after seeing the number is a description of that number.
*   **Mitigation:** What will be done about a confirmed disparity, and what the system does in the meantime. Most bias mitigation plans describe the end state and are silent on whether the system runs while the question is open.
*   **Ongoing Indicator:** The metric watched after release, and its frequency. Bias is not a property of a model at launch but of the data it keeps meeting, so the launch measurement is the first of a series and not the last.

**5. Compliance and Accountability**
*   **Applicable Regulations:** The instruments that bind this system, named, with the clause where the obligation is specific. A list of regulation names is a research note, not a compliance position.
*   **Control Mapping:** Which control satisfies which obligation, and which obligations have no control yet. The second half is the useful half, and a mapping that covers every obligation is nearly always a mapping that was written to be complete rather than to be true.
*   **Evidence and Records:** What is retained to demonstrate compliance, for how long, and who may inspect it. Compliance demonstrated only by assertion cannot be audited, and what cannot be audited is not demonstrable to a regulator.
*   **Compliance Review Cadence:** How often compliance is revisited and what triggers an off-cycle review. A model version change, a new data source, and a new use are all events, and a plan that reviews only on a calendar will miss all three.
*   **Accountable Owner:** The named person answerable for this system's behaviour, with the authority to stop it. Accountability assigned to a committee is distributed to nobody, and the test is whether the named person can halt the system without convening anyone.
*   **Human Oversight Points:** The specific points where a human can override, and where they cannot. Oversight that exists everywhere in principle and nowhere in the workflow is a statement of values, and the points that matter are the ones where override is expensive.
*   **Decision Rights and Redress:** Who decides what the system is permitted to do after launch, and how a person affected by its output contests that output. Redress is the only mechanism that makes accountability reachable by the person who needs it.
*   **Incident Reporting:** What counts as an incident, to whom it is reported, and within what time. An incident definition written broadly enough to catch everything is one nobody can apply under time pressure, and a narrow one misses precisely the cases that were not foreseeable when it was written.

**6. Monitoring and Change**
*   **Performance and Drift Monitoring:** What is watched in operation, and against what baseline. A production model is a different system from the one assessed, and the difference accumulates rather than announcing itself.
*   **Reassessment Triggers:** The events that require the plan to be reopened, stated so they can be recognised by someone who was not in the room. Triggers described in terms of materiality always resolve towards not triggering.
*   **Change Control Link:** How a change to the system is raised, since the system, its data, and its approved uses are all governed by this plan and a change to any of them is a change to the plan.
-->

<h3 dir="ltr" align="right">{{Company_Name}}</h3>
<h2 dir="ltr" align="right">{{Initiative_or_Project_Name}} - {{Complexity_Model_ID}}</h2>
<h1 dir="ltr" align="center">AI GOVERNANCE PLAN</h1>

| **Date Prepared:** {{Current_Date}} | **PMO Assessor:** {{Assessor_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |

---

## 1. Governance Context and Scope
<!-- What the system is, who it acts on, how risky it is, and what this plan does not reach. -->

**AI System Inventory:** [ Add details... ]

**Intended Purpose and Affected Users:** [ Add details... ]

**Risk Classification:** [ Add details... ]

**Scope Exclusions:** [ Add details... ]

---

## 2. Ethical Principles and Acceptable Use
<!-- The constraints that bind use, the uses refused outright, the uses approved within limits, and who bears the cost of error. -->

**Ethical Principles:** [ Add details... ]

**Prohibited Uses:** [ Add details... ]

**Approved Use Cases:** [ Add details... ]

**Human Impact Assessment:** [ Add details... ]

---

## 3. Data Governance
<!-- One row per data category: what it is, where it came from, what it may be used for, how it is protected, and when it is deleted. -->

| Data Category | Provenance and Lawful Basis | Permitted Use | Protection Control | Retention and Deletion |
| :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 4. Fairness, Bias and Transparency
<!-- One row per affected group: the way this system could be unfair to them, how that is tested, what happens if the test fails, and what is watched afterwards. -->

| Affected Group | Bias Risk | Test Method and Threshold | Mitigation | Ongoing Indicator |
| :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 5. Compliance and Accountability
<!-- The instruments that bind the system, the controls that satisfy them, the evidence retained, who is answerable, and where a person can contest an output. -->

**Applicable Regulations:** [ Add details... ]

**Control Mapping:** [ Add details... ]

**Evidence and Records:** [ Add details... ]

**Compliance Review Cadence:** [ Add details... ]

**Accountable Owner:** [ Add details... ]

**Human Oversight Points:** [ Add details... ]

**Decision Rights and Redress:** [ Add details... ]

**Incident Reporting:** [ Add details... ]

---

## 6. Monitoring and Change
<!-- What is watched in operation, what forces the plan to be reopened, and how a change to the system is raised. -->

**Performance and Drift Monitoring:** [ Add details... ]

**Reassessment Triggers:** [ Add details... ]

**Change Control Link:** [ Add details... ]

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **AI Technical Lead** | {{AI_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
| **Data Protection Officer (DPO)** | {{DPO_Name}} | _______________________ | [ .... - .... - .... ] |
| **Project Sponsor / Executive** | {{Project_Sponsor_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;" markdown="1">
  <strong>Template:</strong> AI GOVERNANCE PLAN | <strong>Ref:</strong> PMO-02.02 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
