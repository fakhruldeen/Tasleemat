---
type: Form
lang: en
Form: Vendor Performance Scorecard (Instructions)
token_pointer: /_tokens/forms/en/06_Monitoring_and_Controlling/09_Vendor_Performance_Scorecard/06_09_Vendor_Performance_Scorecard.npy
token_count: 625
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.045422+00:00'
---

# Vendor Performance Scorecard - LLM Generation Prompt

<!--
SYSTEM INSTRUCTIONS: This document is the detailed instruction set for
generating the Vendor Performance Scorecard. When asked to populate the template, follow the
guidance for each section below to produce the requested content. Refer to
`parameters.md` for the general project variables.
-->

> **Context and Definition:**
> A record of how an external supplier performed against measures the project agreed in advance. The columns are in the order the decisions happen in: the metric, the target agreed for it, what was actually measured, the gap between them, and what is being done about the gap.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Approved Project Baselines (PMO-04.01.01), Work Performance Data & Logs (PMO-05.01 - 05.12)
>   * *Optional:* Risk Register (PMO-04.08.02), Vendor Agreements (PMO-04.09.04)
> * **Downstream Dependents:**
>   * *Mandatory:* Change Requests (PMO-05.03), Project / Phase Closeout (PMO-07.03), Lessons Learned Summary (PMO-07.01)
>   * *Optional:* Transition to Operations Checklist (PMO-07.04), Value Realization Register (PMO-01.03)

---

## Vendor Performance Scorecard Entries

### Metric/KPI
**Instructions:** What is being measured, named so that both sides would recognise it. "Quality" is not a metric; "defects found in acceptance, per hundred items delivered" is, because a word cannot be measured twice and compared across periods.

**Generated Value:** [ Add details... ]

### Target Score
**Instructions:** The level agreed in advance, with the period it applies to. A target written after the result is known is not a target, it is a description, and this column is the one that makes the variance column mean anything.

**Generated Value:** [ Add details... ]

### Actual Score
**Instructions:** What was measured, and how. The measure is stated with the score so that a later reader can tell whether the same method was used in both periods; a number whose method has changed is not comparable to a number whose method did not.

**Generated Value:** [ Add details... ]

### Variance
**Instructions:** Target minus actual, with the direction that matters. Whether a positive number is good or bad depends on the metric, and stating it here is what stops the sign being argued about instead of the performance.

**Generated Value:** [ Add details... ]

### Corrective Action
**Instructions:** What happens because of the variance, and by when. Written only where there is a shortfall, and naming who does it: a scorecard that records a variance and no response produces the same variance next period, because the only thing that changed in between was the number.

**Generated Value:** [ Add details... ]

---
