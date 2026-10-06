---
type: Form
lang: en
Form: AI GOVERNANCE PLAN (Instructions)
token_pointer: /_tokens/forms/en/02_Project_Approach_and_Tailoring/04_AI_Use_Case_Canvas/02_04_AI_Use_Case_Canvas.npy
token_count: 2207
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.025346+00:00'
---

# AI GOVERNANCE PLAN - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the
> `AI GOVERNANCE PLAN`. When asked to populate this form, use the guidance
> provided for each section below to accurately generate the required
> content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> An AI use case canvas is the artefact where a proposed use is stated in terms that can be argued with. The governance plan says what is in force for a system that exists; the readiness assessment says whether the organisation can build one; the canvas is the document in between, and it is the only one of the three that is written before anything has been built, which is precisely why it is the one most often written badly.

The five sections follow the order a reviewer asks questions in. Identification names the use case, its owner, the problem in the words of the person who has it, the population that experiences it, and what people do today. That last field is the baseline: a workaround with no stated cost cannot be beaten, so any proposal measured against an unrecorded alternative is measured against nothing. The solution section states the class of approach, what the system does in terms a non-specialist can check, what a person still does, what is excluded, and what must be true for it to work. Data records each source by name and owner, because a source described only as historical data cannot be checked for permission, and permission is what blocks first. Value and cost keeps the build cost and the operating cost apart, states value against a baseline rather than as a return figure, and names the condition for realisation separately from the condition for building, since most systems are built successfully and deliver nothing. The final section ranks the risks specific to this use case, says what the controls do not cover, states which part of the feasibility is unproven, gives the governance route in order, and records the kill criteria.

Two fields do the work that the rest supports. The current workaround establishes the baseline, because a claim of value without one is a number someone chose. The kill criteria establish that this is a proposal rather than a commitment, since a use case entered without an exit condition becomes permanent by default rather than by decision. Where the data cannot be used for model training, the shape of the solution changes, and the canvas is the last place that is cheap to discover. Write the labelling requirement with its cost: it is usually the largest single line in the business case and usually absent from it.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* AI Readiness Assessment (PMO-02.03), Business Case (PMO-01.01)
>   * *Optional:* Product Vision (PMO-03.02), Stakeholder Analysis (PMO-03.05)
> * **Downstream Dependents:**
>   * *Mandatory:* Project Charter (PMO-03.01), AI Governance Plan (PMO-02.02), Requirements Documentation (PMO-04.02.03)
>   * *Optional:* User Story Mapping (PMO-04.02.09), AI Model Card (PMO-02.05)

---

## Use Case Identification

### Use Case Name
**Instruction:** What this use case is called, and where it sits in the portfolio. Naming it makes it possible to say that a later system is the same use case grown, which is usually the difference between a second business case and a repeat of the first.

**Generated value:** [ Add details... ]

### Business Owner
**Instruction:** The person accountable for the outcome, who must be able to say what the system is for without reference to the model. An owner who describes the technology has not been identified.

**Generated value:** [ Add details... ]

### Problem Statement
**Instruction:** The specific problem, in the words of the person who has it, with the cost of leaving it unsolved. "Improve efficiency" is a goal; "a specialist spends forty minutes a day reconciling three spreadsheets" is a problem that can be sized and later checked.

**Generated value:** [ Add details... ]

### Affected Population
**Instruction:** Who experiences the problem, how many, and how often. The population is what converts an annoyance into a cost, and it is also the population the system will act upon.

**Generated value:** [ Add details... ]

### Current Workaround
**Instruction:** What people do today, and what it costs them. A workaround with no stated cost cannot be beaten, so the baseline here is what any proposal is measured against.

**Generated value:** [ Add details... ]

## Proposed Solution

### AI Pattern
**Instruction:** The class of approach, and what makes it fit this problem rather than a neighbouring one. Classification, ranking, generation, forecasting and anomaly detection fail differently, and naming the pattern is what lets the failure modes be anticipated.

**Generated value:** [ Add details... ]

### Solution Description
**Instruction:** What the system does, in one paragraph a non-specialist can check. If the description requires the model architecture to be understood, the description is not yet a description.

**Generated value:** [ Add details... ]

### Human Role
**Instruction:** What a person still does, and at which points they can stop the system. A system described as assisting usually replaces something, and the thing replaced should be named so the change is visible to those affected.

**Generated value:** [ Add details... ]

### Scope Boundary
**Instruction:** What this use case explicitly does not include. Scope stated only as a positive is unbounded, and an unbounded use case absorbs its neighbours' costs.

**Generated value:** [ Add details... ]

### Assumptions
**Instruction:** What must be true for the solution to work, and what happens if each is not. Assumptions recorded after the build are records of what was believed, not of what was assumed.

**Generated value:** [ Add details... ]

## Data

### Data Sources
**Instruction:** Where each input comes from, as a named system or collection with an owner. A source named only as "historical data" cannot be checked for permission, and permission is the first thing that blocks.

**Generated value:** [ Add details... ]

### Data Category and Volume
**Instruction:** What kind of data, at what volume and frequency. Frequency is the field most often omitted and the one that determines whether the system is retrained, refreshed or left to drift.

**Generated value:** [ Add details... ]

### Data Quality Status
**Instruction:** What is known about completeness, consistency and timeliness, and what has not been checked. Recording what was not checked is as useful as recording what was, because it bounds the confidence of the estimate.

**Generated value:** [ Add details... ]

### Labelling Requirement
**Instruction:** Whether labelled examples exist, who will produce them, and at what cost. This is usually the largest single line in the business case, and it is usually absent from it.

**Generated value:** [ Add details... ]

### Permitted Use and Access
**Instruction:** What the data may be used for within this use case, and who approves it. Where the data cannot be used for model training, the shape of the solution changes, and that is better known before than after.

**Generated value:** [ Add details... ]

## Value and Cost

### Value Proposition
**Instruction:** What changes for whom, expressed as a change in the process rather than a return figure. A return calculated before the operating cost is a number that survives no review.

**Generated value:** [ Add details... ]

### Value Measurement Method
**Instruction:** How the value will be measured, against what baseline, and by whom. Value stated without a baseline is a claim, and the baseline is usually already recorded in the current-workaround cost above.

**Generated value:** [ Add details... ]

### Beneficiaries
**Instruction:** Who gains, and who bears the cost of the change. These are rarely the same people, and the form is the place where the second group becomes visible.

**Generated value:** [ Add details... ]

### Build Cost
**Instruction:** What it will cost to build, and what is included. The cost that is excluded is the operating cost below, and stating the exclusion is what keeps the total honest.

**Generated value:** [ Add details... ]

### Operating Cost
**Instruction:** What it will cost to run per unit of work, and at what volume. Cost per unit rather than total, because the total scales with volume and the viability question is asked per unit.

**Generated value:** [ Add details... ]

### Value Realisation Condition
**Instruction:** What must be true for the value to be realised, as distinct from for the system to be built. Most systems are built successfully and deliver nothing, and the difference is nearly always one of these conditions.

**Generated value:** [ Add details... ]

## Risks, Controls and Governance Route

### Key Risks
**Instruction:** The risks specific to this use case, ranked, with the consequence if each materialises. A generic risk register applied here records that data may be biased without saying for whom or how it would be detected.

**Generated value:** [ Add details... ]

### Risk Controls
**Instruction:** What is in place for each risk, and what it does not cover. The second half is the useful half, and a control that covers everything is a control that has been described rather than designed.

**Generated value:** [ Add details... ]

### Feasibility Assessment
**Instruction:** Whether this is technically feasible, at what maturity, and what is unproven. A feasibility statement that does not say which part is unproven is a statement that all of it is proven.

**Generated value:** [ Add details... ]

### Governance Route
**Instruction:** Which governance artefacts this use case must pass through, and in what order. The order is the content: privacy, then fairness, then approval, because a system approved before its data is assessed cannot be un-approved.

**Generated value:** [ Add details... ]

### Kill Criteria
**Instruction:** What result would cause this use case to be stopped. A use case with no kill criteria is a commitment, and a commitment entered without an exit condition is the failure mode this field exists to prevent.

**Generated value:** [ Add details... ]

### Related Artefacts
**Instruction:** The business case, AI governance plan, model card and privacy assessment for this use case, so that a reader holding the canvas can find the decisions that depend on it.

**Generated value:** [ Add details... ]

---
