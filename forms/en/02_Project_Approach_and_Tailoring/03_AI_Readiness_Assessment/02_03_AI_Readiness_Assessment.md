---
type: Form
lang: en
Form: AI GOVERNANCE PLAN (Instructions)
token_pointer: /_tokens/forms/en/02_Project_Approach_and_Tailoring/03_AI_Readiness_Assessment/02_03_AI_Readiness_Assessment.npy
token_count: 2418
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.021988+00:00'
form_id: PMO-02.03
status: approved
---

# AI GOVERNANCE PLAN - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the
> `AI GOVERNANCE PLAN`. When asked to populate this form, use the guidance
> provided for each section below to accurately generate the required
> content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> An AI readiness assessment answers a prior question to the AI governance plan. The governance plan says what is in force for a system that will exist; the readiness assessment says whether the organisation is in a position to build one, and the second question is asked earlier and answered less often.

The six sections follow the order in which a team discovers what it did not know. Scope states which decision the assessment supports, since a readiness figure with no decision attached is a score, and a score nobody needs is the one most readily abandoned. Data readiness separates availability from permission, which is the distinction most often missed: an organisation can have the data and still not be permitted to use it, and access rights are settled late precisely because they involve people outside the team. Technical readiness asks whether a model can be reproduced, rolled back and monitored in production, rather than whether a notebook runs. Skills separates building, evaluating, deploying and operating, because a team strong in the first is frequently unable to do the last, which is where readiness actually fails. Organisational readiness covers the conditions outside the team's control: sponsorship that funds the consequences as well as the work, an operating model, contracts that permit the intended use, and a stated appetite for failure. The outcome section separates blocking gaps from those that merely slow, because that distinction is the assessment's actual output and a single list of gaps cannot express it.

The failure mode is the undifferentiated average. A readiness score that weights every dimension equally treats a capability the business does not depend on as equal to one it cannot operate without, and the aggregate then conceals the single gap that matters. So record the scale, the weights and their justification, and the severity of each gap separately from the score. Where a dimension was assessed by self-declaration rather than by measurement, say so: self-declaration is legitimate and common, and it becomes a problem only when it is not labelled and is therefore indistinguishable from a measurement. An assessment should also record its own expiry, since readiness decays as people move and data drifts, and an assessment with no reassessment trigger is treated as current indefinitely.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Business Case (PMO-01.01), Data & Technical Architecture Baseline
>   * *Optional:* Portfolio Roadmap (PMO-00.01), Strategic AI Goals
> * **Downstream Dependents:**
>   * *Mandatory:* AI Governance Plan (PMO-02.02), AI Use Case Canvas (PMO-02.04)
>   * *Optional:* Resource Capacity Matrix (PMO-00.04), Procurement Plan (PMO-04.09.01)

---

## Purpose and Scope of the Assessment

### Assessment Objective
**Instruction:** What decision this assessment is being made to support, and what decision it is not. A readiness assessment with no stated decision attached is a score, and a score nobody needs is the one most often abandoned.

**Generated value:** [ Add details... ]

### Assessment Scope
**Instruction:** Which systems, processes and teams are in scope, and which are excluded. Excluding something is legitimate; excluding it without writing it down is what lets it reappear as a dependency in month four.

**Generated value:** [ Add details... ]

### Assessment Method
**Instruction:** How each dimension was assessed: instrumented measurement, walkthrough, interview, or self-declaration. Self-declaration is legitimate and must be labelled, because an unlabelled self-declaration is indistinguishable from a measurement and is trusted accordingly.

**Generated value:** [ Add details... ]

### Assessor and Date
**Instruction:** Who performed it, on what date, and against which version of the systems. A readiness figure without a date is a figure that decays silently.

**Generated value:** [ Add details... ]

### Evidence Basis
**Instruction:** What the scores rest on, and where the evidence sits. A score whose source cannot be retrieved cannot be defended when it is challenged, which is the only time its accuracy matters.

**Generated value:** [ Add details... ]

## Data Readiness

### Data Availability
**Instruction:** Whether the data the use case requires exists, at the volume and coverage needed. Availability is not the same as permission, and the gap between them is the most common reason a data-ready organisation is not an AI-ready one.

**Generated value:** [ Add details... ]

### Data Quality
**Instruction:** Completeness, consistency, timeliness and validity, each with the measurement used. "Good quality" is a conclusion; a completeness figure against a defined field list is an input to one.

**Generated value:** [ Add details... ]

### Data Lineage and Documentation
**Instruction:** Whether it can be traced to its origin and meaning. Lineage is what makes a defective output diagnosable rather than merely wrong, and it cannot be reconstructed after the fact.

**Generated value:** [ Add details... ]

### Labelling and Ground Truth
**Instruction:** Whether labelled examples exist for the intended purpose, in sufficient quantity and quality. Where they do not, say so, because labelling is a programme of work with a cost and a duration, and treating it as a task hides both.

**Generated value:** [ Add details... ]

### Data Governance and Access
**Instruction:** Who may access what, under what controls, and whether that is settled. Access rights settled late are the usual cause of a launch delay that no one predicted, and they are settled late because they involve people outside the team.

**Generated value:** [ Add details... ]

## Technical and Platform Readiness

### Compute and Capacity
**Instruction:** Whether the capacity required for training and inference exists, and at what cost. Cost per unit of work is the figure that decides whether the use case is viable at volume, and it is not known until the volume is.

**Generated value:** [ Add details... ]

### Platform and Tooling
**Instruction:** MLOps, versioning, experiment tracking, deployment and monitoring. The tooling question is not whether a notebook runs but whether a model can be reproduced, rolled back, and monitored in production, since those are the operations a team inherits.

**Generated value:** [ Add details... ]

### Integration
**Instruction:** Whether the system connects to the surrounding estate, and at what quality. Integration is where readiness assessments are optimistic, because a proof of concept connects to nothing and a production system must connect to everything.

**Generated value:** [ Add details... ]

### Security and Resilience
**Instruction:** The controls in force for AI workloads, and what happens when the system is unavailable. A system whose fallback is manual reverts to a process that was automated because it was unworkable by hand.

**Generated value:** [ Add details... ]

### Scalability
**Instruction:** Whether performance and cost hold as volume grows. A model that is accurate and unaffordable at ten times the volume is a prototype, and the assessment is where that is cheapest to discover.

**Generated value:** [ Add details... ]

## Skills and Team Readiness

### Team Composition
**Instruction:** Who is on the team, and which of the required roles are unfilled. List the gaps by role rather than by competence, because a gap named by competence has no owner and a gap named by role has a vacancy.

**Generated value:** [ Add details... ]

### AI Skills
**Instruction:** The specific capabilities present, at what level: building, evaluating, deploying, and operating. These are different skills and a team strong in the first may be unable to do the third, which is where readiness usually fails.

**Generated value:** [ Add details... ]

### Domain Expertise
**Instruction:** Whether the team includes people who know the domain well enough to judge an output is wrong. Without them the team can measure performance and not interpret it, and those are not separable.

**Generated value:** [ Add details... ]

### Capacity and Availability
**Instruction:** Whether the people named are actually available at the required fraction, given other commitments. A team rostered at half time and a team absent are the same fact expressed differently.

**Generated value:** [ Add details... ]

### Capability Building
**Instruction:** How gaps will be closed: hire, train, partner, or buy. These have different lead times and the lead time is the constraint, not the preference.

**Generated value:** [ Add details... ]

## Organisational Readiness

### Leadership Sponsorship
**Instruction:** Whether there is a sponsor who will fund the consequences as well as the work. Sponsorship that ends at approval has funded a demonstration, and the difference surfaces at the first decision the system makes that somebody disputes.

**Generated value:** [ Add details... ]

### Operating Model
**Instruction:** Who runs the system in production, and under which service commitment. An operating model decided at go-live is an operating model negotiated in an incident.

**Generated value:** [ Add details... ]

### Change and Adoption
**Instruction:** Who must change their work, what they gain, and what they lose. A system that makes someone's judgement redundant will not be adopted regardless of its accuracy, and adoption is not a communications problem.

**Generated value:** [ Add details... ]

### Procurement and Contracting
**Instruction:** Whether the contracts permit the intended use, and what they permit the supplier to do with the data. These are the obligations that cannot be renegotiated after the data has been shared.

**Generated value:** [ Add details... ]

### Risk Appetite
**Instruction:** What level of failure the organisation will accept, and who accepts it on its behalf. A risk appetite that is never stated becomes, by default, zero tolerance, which is not a position anyone chose.

**Generated value:** [ Add details... ]

## Assessment Outcome and Route Forward

### Dimension Scores
**Instruction:** The score for each dimension, with the scale used stated. A score without its scale cannot be compared with a later assessment, and the comparison is the only reason to take the first one.

**Generated value:** [ Add details... ]

### Weighted Overall Score
**Instruction:** The aggregate, with the weights and their justification. An unweighted average treats a dimension the business does not depend on as equal to one it cannot operate without.

**Generated value:** [ Add details... ]

### Blocking Gaps
**Instruction:** The gaps that prevent proceeding, as distinct from those that slow it. This distinction is the assessment's actual output, and a form that records a single list cannot make it.

**Generated value:** [ Add details... ]

### Recommended Route
**Instruction:** Proceed, proceed with conditions, remediate, or do not proceed, and the condition attached. The route without its conditions is an opinion; the conditions are what can be tracked and closed.

**Generated value:** [ Add details... ]

### Remediation Plan
**Instruction:** What will be done, by whom, by when, and what it costs. A gap with no owner and no date is not a gap in the plan, it is a gap in the plan's assumptions.

**Generated value:** [ Add details... ]

### Reassessment Trigger
**Instruction:** What would cause the assessment to be repeated. Readiness decays as staff move and data drifts, and an assessment with no expiry is treated as current indefinitely.

**Generated value:** [ Add details... ]

---
