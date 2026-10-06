---
type: Form
lang: en
Form: TAILORING PLAN (Instructions)
token_pointer: /_tokens/forms/en/02_Project_Approach_and_Tailoring/01_Tailoring_Plan/02_01_Tailoring_Plan.npy
token_count: 1378
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.025940+00:00'
form_id: PMO-02.01
status: approved
---

# TAILORING PLAN - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the
> `TAILORING PLAN`. When asked to populate this form, use the guidance
> provided for each section below to accurately generate the required
> content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> Tailoring is the deliberate departure from a standard method, recorded as such. The distinction that matters is between a decision and a default: a methodology says what to do unless there is a reason not to, and tailoring is the part where the reason is written down. An unwritten deviation is not tailoring, it is a departure that will be discovered later by someone auditing the project, and by then the team has built its way around it.

The three sections follow the life of a tailoring decision. The basis establishes what is being tailored from, what forces a change, what cannot be traded away, and what the project has already inherited from above it. The decisions record each change with the default it departs from, because without the default a reader cannot tell whether a requirement was loosened or merely renamed. The governance section establishes who may approve what, and what would cause a decision to be reopened.

The field most often skipped is the consequence. Every tailoring has a cost, and a plan that records only what improves is a summary of intentions. Recording what becomes harder is what makes the decision reviewable by someone who was not in the conversation when it was made.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Project Charter (PMO-03.01), Organizational PMO Methodology
>   * *Optional:* Program Charter (PMO-00.02), Risk Management Plan (PMO-04.08.01)
> * **Downstream Dependents:**
>   * *Mandatory:* Project Management Plan (PMO-04.01.01), Quality Management Plan (PMO-04.05.01)
>   * *Optional:* AI Governance Plan (PMO-02.02), Team Charter (PMO-04.06.05)

---

## 1. Tailoring Basis

### Organizational Methodology
**Instruction:** The methodology this project is tailoring from, with its version. The version matters because a decision to deviate from a methodology is meaningless without knowing which one, and two projects claiming to follow the same methodology may be following different editions of it.

**Generated value:** [ Add details... ]

### Tailoring Drivers
**Instruction:** What makes this project different from the standard: size, risk, complexity, regulatory context, or organisational constraint. A tailoring plan written without drivers lists arbitrary decisions, because where nothing is forcing a change any change looks equally reasonable.

**Generated value:** [ Add details... ]

### Applicable Standards
**Instruction:** The governance, quality or regulatory standards that apply regardless of tailoring, and which cannot be traded away. These are the floor the tailoring operates above, and a plan that does not state them invites a decision to drop a mandatory control as an efficiency measure.

**Generated value:** [ Add details... ]

### Inherited Tailoring
**Instruction:** Any tailoring already decided at programme or portfolio level that this project inherits rather than makes. Most deviations in a project are inherited, and a plan that records only its own decisions implies it has full control over the approach when it does not.

**Generated value:** [ Add details... ]

## 2. Tailoring Decisions

### Process or Artifact
**Instruction:** What is being tailored, named specifically enough to be found in the methodology. "The risk process" is not a decision anyone can approve, because there are several and the one approved may not be the one implemented.

**Generated value:** [ Add details... ]

### Standard Requirement
**Instruction:** What the methodology requires by default, stated before the change. Without the default written down the reader cannot tell whether the tailoring loosened a requirement or only renamed it, which is the commonest form of undeclared tailoring.

**Generated value:** [ Add details... ]

### Decision
**Instruction:** Added, removed, or modified, and specifically what changes. Record the effect on the process itself, not the intent, since "simplified" is an intent and "the weekly risk review is replaced by a fortnightly one" is an effect.

**Generated value:** [ Add details... ]

### Rationale
**Instruction:** Why this change is right for this project, tied to a driver. A rationale that would be equally valid for any project is not a rationale, and is the usual reason a tailoring decision cannot survive a later challenge.

**Generated value:** [ Add details... ]

### Consequence
**Instruction:** What becomes harder because of the change. Every tailoring has a cost, and a plan that records only what improves is a summary of intentions; recording what is given up is what makes the decision reviewable.

**Generated value:** [ Add details... ]

### Reversibility
**Instruction:** Whether the change can be undone, and what would trigger reversing it. Most tailoring is reversible in principle and irreversible in practice, because by the time the cost becomes clear the team has built its way around the change.

**Generated value:** [ Add details... ]

### Impact on Artifacts
**Instruction:** Which downstream artifacts change as a result, such as the risk register, the schedule format, or the reporting cadence. A decision that changes a process without changing the artifacts that process produces leaves two versions of the truth in circulation.

**Generated value:** [ Add details... ]

## 3. Governance of Tailoring

### Decision Authority
**Instruction:** Who may approve a tailoring decision, and at what level each class of change is approved. Without an authority map the project either escalates everything or decides things nobody authorised.

**Generated value:** [ Add details... ]

### Review and Reapproval
**Instruction:** When the plan is reviewed, and what would cause a decision to be reopened. Tailoring decisions are rarely revisited, so the trigger has to exist before the decision rather than being invented once the cost is known.

**Generated value:** [ Add details... ]

### Compliance Check
**Instruction:** How the plan is checked against the applicable standards, and who performs the check. A self-check performed by the party that wanted the change is not a check.

**Generated value:** [ Add details... ]

### Change Control Link
**Instruction:** How a later change to a baselined decision is raised, since tailoring is baselined and any subsequent change is a change to the plan rather than an update to it.

**Generated value:** [ Add details... ]

---
