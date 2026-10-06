---
type: Form
lang: en
Form: RELEASE PLAN (Instructions)
token_pointer: /_tokens/forms/en/04_Planning/03_Schedule/09_Release_Plan/04_03_09_Release_Plan.npy
token_count: 863
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.974554+00:00'
form_id: PMO-04.03.09
status: approved
---

# RELEASE PLAN - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `RELEASE PLAN`. When asked to populate this form, use the guidance provided for each section below to accurately generate the required content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> The product vision provides the future view of the product being developed. It is aspirational, yet achievable and realistic, and is developed at the very beginning of a project, where it is often an input to the business case. On agile-based projects it is often used in place of a project charter, and it is developed once, at the beginning.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Work Breakdown Structure / WBS (PMO-04.02.06), Scope Statement (PMO-04.02.05)
>   * *Optional:* Resource Requirements (PMO-04.06.02), Risk Register (PMO-04.08.02)
> * **Downstream Dependents:**
>   * *Mandatory:* Project Schedule Baseline (PMO-04.03.08), Earned Value Analysis / EVA (PMO-06.05)
>   * *Optional:* Release Plan (PMO-04.03.09), Lookahead Planning Log (PMO-04.03.10)

---

## Releases

### Release

**Instruction:** The release identifier and name, for example R1 or Release 1. A release is the unit the customer receives, not an internal milestone, so name it the way the customer would recognise it.

**Generated value:** [ Add details... ]

---

### Start Date

**Instruction:** When the release starts. For a high-level plan a month or a quarter is honest; a day-level date implies a precision the plan does not have.

**Generated value:** [ Add details... ]

---

### End Date

**Instruction:** When the release finishes. Give the duration as well as the end date, since the two together are what show whether the release is gaining or losing ground.

**Generated value:** [ Add details... ]

---

### User Stories

**Instruction:** The requirements or user stories from the backlog assigned to this release, referenced by their backlog identifier rather than restated, so the plan and the backlog cannot drift apart.

**Generated value:** [ Add details... ]

---

### Release Goal

**Instruction:** What this release is for, in one sentence. A release without a goal turns into a list of everything that happened to fit, which is how releases acquire unrelated work.

**Generated value:** [ Add details... ]

---

### Status

**Instruction:** Not started, in progress, or released. This is the column that makes the plan honest: once a sprint has started its contents cannot change, so anything still marked in progress is committed, and anything not started can still move.

**Generated value:** [ Add details... ]

---

## Sprint Breakdown

### Sprint

**Instruction:** The sprint identifier and the release it belongs to, so the plan can be read per release rather than as one long list.

**Generated value:** [ Add details... ]

---

### Dates

**Instruction:** When the sprint starts and ends. A sprint with no dates cannot be told apart from one that is still open to negotiation, and once it has started its contents are fixed.

**Generated value:** [ Add details... ]

---

### Sprint Goal

**Instruction:** What this sprint is for, in one sentence. Several sprints toward one release goal is the normal case; a sprint goal that contradicts the release goal is a sign the release is carrying two unrelated pieces of work.

**Generated value:** [ Add details... ]

---

### Sprint User Stories

**Instruction:** The user stories committed to this sprint, by backlog identifier. Once the sprint has started this list is what was committed, and a change to it is a change to the commitment rather than to the plan.

**Generated value:** [ Add details... ]

---

### Sprint Status

**Instruction:** Not started, in progress, or complete.

**Generated value:** [ Add details... ]

---

