---
type: Form
lang: en
Form: RISK MITIGATION ACTION PLAN (Instructions)
token_pointer: /_tokens/forms/en/04_Planning/08_Risk/07_Risk_Mitigation_Action_Plan/04_08_07_Risk_Mitigation_Action_Plan.npy
token_count: 718
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.986652+00:00'
---

# RISK MITIGATION ACTION PLAN - LLM Generation Prompt

<!--
SYSTEM INSTRUCTIONS: This document is the detailed instruction set for
generating the RISK MITIGATION ACTION PLAN. When asked to populate the template, follow the
guidance for each section below to produce the requested content. Refer to
`parameters.md` for the general project variables.
-->

> **Context and Definition:**
> The commitment of what will be done about one named risk: the treatment it is given, the steps that deliver that treatment, what the steps cost, and the score the project expects to reach once they are done. It is an output of Plan Risk Responses, and it exists so that a risk which has been identified does not stay identified.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Project Charter (PMO-03.01), Assumption Log (PMO-03.03), Project Baselines (Scope/Schedule/Cost)
>   * *Optional:* AI Governance Plan (PMO-02.02), Procurement Strategy (PMO-04.09.02)
> * **Downstream Dependents:**
>   * *Mandatory:* Risk Register (PMO-04.08.02), Risk Reports (PMO-04.08.06), Risk Audits (PMO-06.06)
>   * *Optional:* Risk Mitigation Action Plan (PMO-04.08.07), Decision Log (PMO-05.02)

---

## Risk Assessment

### Risk ID and Title
**Instructions:** The identifier and title of the risk exactly as the risk register carries them, so this plan can be joined back to the register. A title written here that differs from the register's is the defect that makes the two documents disagree about what is being planned for.

**Generated Value:** [ Add details... ]

### Current Risk Score
**Instructions:** The probability multiplied by the impact, each on the scale the register uses, with both factors shown rather than only the product. A score given on its own hides the reason for it, and a score whose factors cannot be read back cannot be recalculated when one of them changes.

**Generated Value:** [ Add details... ]

## Mitigation Plan

### Mitigation Strategy
**Instructions:** Which of the four treatments the risk is given: avoid, transfer, mitigate, or accept. Accept is a decision that needs a reason, so an accepted risk carries the reason and the name of whoever accepted it.

**Generated Value:** [ Add details... ]

### Detailed Action Steps
**Instructions:** The plan as ordered steps, each with an owner and a date, so that the plan can be read as work rather than as intent. A step with no owner is a wish, and a step with no date is a step that never starts.

**Generated Value:** [ Add details... ]

### Resource Requirements
**Instructions:** What executing the plan costs and who has to be assigned to it: the budget, the people, and the time. Stated so the request can be approved against something, rather than argued in a meeting where no one can check it.

**Generated Value:** [ Add details... ]

### Target Risk Score
**Instructions:** The score the plan is expected to reach, with the assumptions it depends on. A target written without saying which steps deliver it cannot be checked afterwards, which leaves no way to know whether the plan worked.

**Generated Value:** [ Add details... ]

---
