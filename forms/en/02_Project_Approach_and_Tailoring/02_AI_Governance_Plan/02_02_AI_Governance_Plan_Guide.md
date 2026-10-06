---
type: Form
lang: en
layout: default
title: AI Governance Plan
nav_order: 1
token_pointer: /_tokens/forms/en/02_Project_Approach_and_Tailoring/02_AI_Governance_Plan/02_02_AI_Governance_Plan_Guide.npy
token_count: 2716
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.020011+00:00'
form_id: PMO-02.02
status: approved
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">

## Tasleemat Forms Guide
# Project Artifact: AI Governance Plan

**Document Reference:** `PMO-02.02`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **AI Governance Plan** in alignment
with the Tasleemat framework.

---

### 1. What?
A record of the constraints, permissions, test results and named owners
governing a specific AI system, at a specific version, for a specific set of
affected people. It states what the system is and what it excludes, the uses
prohibited outright and the uses approved within stated limits, the lawful
basis and permitted use of each data category together with the control
applied and the deletion date, the fairness test for each affected group with
the threshold that triggers action, the obligations each control satisfies, and
the named individual who may stop the system. It is baselined, and it is
reopened by events rather than by preference.

---

### 2. Why?
Because an AI system's behaviour is not visible from its outputs. The same
model behaves differently on different data, and the configuration, the
approved use, and the threshold in force are all invisible to the person the
output affects. Without a baselined record, every question about a past
decision becomes unanswerable, and the questions that arrive are always
retroactive: why was this data used, who approved this classification, what
happened when the drift test failed. Governance is worth what those questions
are worth, and they are the ones that arrive at the worst possible moment.

The specific discipline the form imposes is naming rather than classifying. A
plan that records 'minimised' and 'monitored' will pass review and tell a
reader nothing, because those words describe a class of control and not the
control in force. The version number, the key holder, the numeric threshold
and the named owner are what make the record usable later.

---

### 3. When?
This artifact is primarily prepared, utilized, and updated during the
**PROJECT APPROACH AND TAILORING Process Group** of the project lifecycle. It
is drafted before the system is used in production and baselined at the point
of release, and it is reopened on a model version change, a new data source, a
new approved use, or a regulatory change. Those events are frequent; a plan
reviewed only on a calendar will miss all of them.

---

### 4. Who?
**Responsibilities:** Prepared by the AI or ML Lead with the Data Protection
Officer, since the plan is only credible if the person who assessed the data
and the person accountable for the system are both signatories. Approved by
the Accountable Owner, who must be an individual with the authority to halt the
system without convening anyone, and by the sponsor where the system affects
external parties. Reviewed by the same signatories on each triggering event.

---

### Tailoring Tips
*   A plan may cover several models as a portfolio rather than writing one per
    model, provided the inventory names the version each constraint applies to,
    since the failure this prevents is a constraint quoted against the wrong
    one.
*   Where a system is procured rather than built, governance applies to the
    supplier too. Record what was contractually required, since a control the
    organisation assumed it had is not a control it has.
*   A material model or intent change in performance should reopen the plan
    even where the system is unchanged, because a model that performs well on
    yesterday's population is not thereby fit for tomorrow's.
*   Plans for lower-risk internal uses may be abbreviated, but the sections to
    keep regardless of tier are the prohibited-use list, the named owner and
    the incident definition, since those are the three a reader needs in the
    first hour of an incident.
*   The plan should be kept with the model card rather than merged into it, as
    the card describes what the system is and this document describes what is
    permitted, and the two diverge at every review.
*   Superseded plans should be retained rather than overwritten, since the
    question an incident generates is almost always about what was in force at
    the time.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   AI Use Case Canvas (PMO-02.04)
    *   AI Readiness Assessment (PMO-02.03)
    *   Organizational AI Ethics Policy
*   **Optional / Contextual:**
    *   Data Privacy & Ethics Assessment (PMO-02.06)
    *   Project Charter (PMO-03.01)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   AI Model Card (PMO-02.05)
    *   Quality Metrics (PMO-04.05.02)
    *   Risk Management Plan (PMO-04.08.01)
*   **Optional / Contextual:**
    *   Prompt Library Register (PMO-05.09)
    *   UAT Sign-off Form (PMO-06.10)

---

### 5. How?
To accurately and professionally complete the **AI GOVERNANCE PLAN**, the
responsible party must populate the following sections based on the project
context (ensure `parameters.md` is referenced for global project variables):

*   **AI System Inventory:** What the system is, at the version that will actually run, and who operates it. Record the version, because a governance plan that covers "the model" covers whichever model happens to be deployed when someone asks, and the answer is rarely the one that was assessed.
*   **Intended Purpose and Affected Users:** What the system is for, and who is subject to its output rather than merely its user. The two are routinely confused, and the confusion is how a system that screens applicants comes to be described as a tool that helps recruiters write better.
*   **Risk Classification:** The tier assigned and the criteria that put it there, not the tier alone. A classification with no stated criteria cannot be challenged, and an unchallengeable classification is the same as no classification.
*   **Scope Exclusions:** What this plan explicitly does not cover, and who owns it instead. Governance plans fail at the boundary: the component nobody assigned sits under a plan that assumed it was included.
*   **Ethical Principles:** The principles that constrain use on this project, and the case in which one yields to another. Principles that cannot yield to each other are not a decision rule, and a project under time pressure will resolve the conflict silently and after the fact.
*   **Prohibited Uses:** Uses that are refused regardless of benefit. This section is what the plan is for, and a plan listing only permitted uses has no way to refuse anything.
*   **Approved Use Cases:** The uses that are approved, each with the limits within which it stays approved. An approved use without stated limits is an approved capability, not an approved use.
*   **Human Impact Assessment:** Who bears the consequences of a wrong output, and whether they can tell it was wrong. A system whose subject cannot detect its own errors transfers the cost of error to the person least able to contest it.
*   **Data Category:** What kind of data, in terms a data subject would recognise as being about them.
*   **Provenance and Lawful Basis:** Where the data came from and under what basis it is processed. Data that arrived with the model cannot have its basis added later, so a model trained before this question was asked holds data whose status nobody can now evidence.
*   **Permitted Use:** What the data may be used for within this system, and what it may not. The most common governance failure is not a leak but reuse for a purpose nobody re-approved.
*   **Protection Control:** The specific control applied, not the category of control. "Encrypted" is a category, and the sentence that matters is which key, held by whom, and rotated how.
*   **Retention and Deletion:** When the data is deleted, and how deletion is verified. Deletion that is asserted rather than evidenced is how a training set outlives the project that justified it.
*   **Affected Group:** The group whose outcomes are affected, named. Groups are described in aggregate on the basis of a test, and the group that matters is the one that performs worst on it.
*   **Bias Risk:** The specific way this system could be unfair to this group, stated so it could be false. "Bias risk" as a heading is not a risk; "the model scores this group lower on historic completion rates" is a risk that can be measured and can turn out to be wrong.
*   **Test Method and Threshold:** How it is tested and what result triggers action, with the threshold written before the result is known. A threshold set after seeing the number is a description of that number.
*   **Mitigation:** What will be done about a confirmed disparity, and what the system does in the meantime. Most bias mitigation plans describe the end state and are silent on whether the system runs while the question is open.
*   **Ongoing Indicator:** The metric watched after release, and its frequency. Bias is not a property of a model at launch but of the data it keeps meeting, so the launch measurement is the first of a series and not the last.
*   **Applicable Regulations:** The instruments that bind this system, named, with the clause where the obligation is specific. A list of regulation names is a research note, not a compliance position.
*   **Control Mapping:** Which control satisfies which obligation, and which obligations have no control yet. The second half is the useful half, and a mapping that covers every obligation is nearly always a mapping that was written to be complete rather than to be true.
*   **Evidence and Records:** What is retained to demonstrate compliance, for how long, and who may inspect it. Compliance demonstrated only by assertion cannot be audited, and what cannot be audited is not demonstrable to a regulator.
*   **Compliance Review Cadence:** How often compliance is revisited and what triggers an off-cycle review. A model version change, a new data source, and a new use are all events, and a plan that reviews only on a calendar will miss all three.
*   **Accountable Owner:** The named person answerable for this system's behaviour, with the authority to stop it. Accountability assigned to a committee is distributed to nobody, and the test is whether the named person can halt the system without convening anyone.
*   **Human Oversight Points:** The specific points where a human can override, and where they cannot. Oversight that exists everywhere in principle and nowhere in the workflow is a statement of values, and the points that matter are the ones where override is expensive.
*   **Decision Rights and Redress:** Who decides what the system is permitted to do after launch, and how a person affected by its output contests that output. Redress is the only mechanism that makes accountability reachable by the person who needs it.
*   **Incident Reporting:** What counts as an incident, to whom it is reported, and within what time. An incident definition written broadly enough to catch everything is one nobody can apply under time pressure, and a narrow one misses precisely the cases that were not foreseeable when it was written.
*   **Performance and Drift Monitoring:** What is watched in operation, and against what baseline. A production model is a different system from the one assessed, and the difference accumulates rather than announcing itself.
*   **Reassessment Triggers:** The events that require the plan to be reopened, stated so they can be recognised by someone who was not in the room. Triggers described in terms of materiality always resolve towards not triggering.
*   **Change Control Link:** How a change to the system is raised, since the system, its data, and its approved uses are all governed by this plan and a change to any of them is a change to the plan.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](02_02_AI_Governance_Plan_Template.md)
* [🤖 LLM Generation Prompt](02_02_AI_Governance_Plan.md)
* [📊 Data Structure (JSON)](02_02_AI_Governance_Plan.json)
* [📈 Tabular Data (CSV)](02_02_AI_Governance_Plan.csv)

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [02_02_AI_Governance_Plan_Example.md](../../../../examples/en/02_Project_Approach_and_Tailoring/02_AI_Governance_Plan/02_02_AI_Governance_Plan_Example.md)

</div>
