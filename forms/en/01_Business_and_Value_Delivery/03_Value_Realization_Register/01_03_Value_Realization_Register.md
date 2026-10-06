---
type: Form
lang: en
Form: VALUE REALIZATION REGISTER (Instructions)
token_pointer: /_tokens/forms/en/01_Business_and_Value_Delivery/03_Value_Realization_Register/01_03_Value_Realization_Register.npy
token_count: 1442
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.091950+00:00'
---

# VALUE REALIZATION REGISTER - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the
> `VALUE REALIZATION REGISTER`. When asked to populate this form, use the
> guidance provided for each section below to accurately generate the required
> content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> A value realization register is the running record of whether the things the business case promised are actually happening. It is not the plan of the benefits, which is the benefits management plan, and it is not the project's own record of what it delivered. It is the document that survives the project, because the project team that could testify to what was supposed to happen will have dispersed by the time the benefits are due.

The register exists to make one movement visible: the difference between what a measure was, what it was expected to be, and what it is. That requires a baseline, a signed variance and a date of measurement, none of which can be reconstructed later. A value measured early in the period and reported as final is the ordinary way a shortfall is presented as success, and it is only the date that distinguishes the two cases.

A register also needs rules for what happens to a benefit that does not arrive. Without a stated trigger for escalation, a variance is absorbed at each review until it stops being a variance and becomes the plan, and the plan has quietly become the record of what happened.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Benefits Management Plan (PMO-01.02), Business Case (PMO-01.01)
>   * *Optional:* Project Status Reports (PMO-06.01), Product Acceptance Form (PMO-06.08)
> * **Downstream Dependents:**
>   * *Mandatory:* Lessons Learned Summary (PMO-07.01), Project / Phase Closeout (PMO-07.03)
>   * *Optional:* Post-Project Benefit Reviews, Operational KPI Dashboards

---

## 1. Register Control

### Register Purpose
**Instruction:** What this register is tracking and which benefits it covers. State the scope, because a register that silently omits a benefit reads as a benefit that was never claimed, and the two are indistinguishable to a later reader.

**Generated value:** [ Add details... ]

### Reporting Period
**Instruction:** The period the entries cover and the date the register was last updated. Without a date a register of moving values is indistinguishable from one that was abandoned, and the two look identical on the page.

**Generated value:** [ Add details... ]

### Source Documents
**Instruction:** The business case and benefits management plan the entries derive from. The register does not create benefits; it tracks benefits defined elsewhere, and the source is what lets a reader check a target against the case that authorised it.

**Generated value:** [ Add details... ]

### Entry Rules
**Instruction:** What qualifies for an entry, and what does not. A register that accumulates everything makes no claim on anyone's attention, and the entries that get reviewed are then the ones that were easiest to write.

**Generated value:** [ Add details... ]

## 2. Value Realization Register

### Benefit ID
**Instruction:** The identifier for the benefit, matching the benefits management plan. Without a shared identifier the register cannot be reconciled against the plan, and a benefit can be tracked in one and dropped from the other without anyone deciding to drop it.

**Generated value:** [ Add details... ]

### Benefit Description
**Instruction:** The benefit as a measurable change, restated in the form it will be measured. The register is where a benefit written in prose has to become a number, so the description must be the one the measure actually refers to.

**Generated value:** [ Add details... ]

### Benefit Owner
**Instruction:** The role accountable for realising the benefit, which is normally not the project manager. The project manager can report the value; only the operating role can change the practice the value depends on.

**Generated value:** [ Add details... ]

### Measurement Method
**Instruction:** How the value is calculated, stated so two people would compute it the same way. Most disputes about a realised value turn on method rather than on the outcome, and an unstated method invites whichever reading suits the reader.

**Generated value:** [ Add details... ]

### Baseline Value
**Instruction:** The value the measure stood at before the project. Without it the actual figure has nothing to be compared against, and the register becomes a list of numbers rather than evidence of change.

**Generated value:** [ Add details... ]

### Target Value and Date
**Instruction:** The value expected and the date it is expected by. A target without a date cannot be late, and an undated target is met every day it goes unexamined.

**Generated value:** [ Add details... ]

### Actual Value and Date
**Instruction:** The value measured and the date it was measured. The date of measurement matters as much as the figure, because a value measured early in the year and reported as final is the most common way a shortfall is reported as success.

**Generated value:** [ Add details... ]

### Variance
**Instruction:** The difference between actual and target, signed. This is the column the register exists to produce, and a register that records only the actuals has omitted the only figure anyone reads.

**Generated value:** [ Add details... ]

### Status
**Instruction:** Where the benefit stands against its plan. The status should follow a stated rule rather than a judgement, since a status chosen to match the reporting is a status that reports nothing.

**Generated value:** [ Add details... ]

## 3. Realization Actions

### Variance Explanation
**Instruction:** Why the actual differs from the target, recorded as a cause rather than as a gap. A variance with no cause cannot be acted on, and a benefit that is off plan for a reason nobody has established will stay off plan for a reason nobody has established.

**Generated value:** [ Add details... ]

### Corrective Action
**Instruction:** What is being done, by whom, and by when. An action without an owner is a note, and notes appear in the next version of the register as unresolved.

**Generated value:** [ Add details... ]

### Escalation Trigger
**Instruction:** The event that requires the benefit to be escalated rather than adjusted. Without a trigger the variance is absorbed at each review until it is no longer a variance but the plan, and the plan has quietly become the record of what happened.

**Generated value:** [ Add details... ]

### Benefit Withdrawal
**Instruction:** The grounds for removing a benefit from the register. Without them benefits are never withdrawn, only left at their last reported value, and a withdrawn benefit and a stalled one look the same forever.

**Generated value:** [ Add details... ]

---
