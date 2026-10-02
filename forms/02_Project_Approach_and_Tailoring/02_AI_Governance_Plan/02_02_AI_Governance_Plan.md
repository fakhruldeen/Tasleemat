---
lang: en
Form: AI GOVERNANCE PLAN (Instructions)
---

# AI GOVERNANCE PLAN - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the
> `AI GOVERNANCE PLAN`. When asked to populate this form, use the guidance
> provided for each section below to accurately generate the required
> content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> An AI governance plan is the document that answers one question: for this system, what is in force right now. Every external AI obligation eventually reduces to it, because what a regulator, a client or an internal audit asks for is not a policy in general but the specific set of constraints, data permissions, test thresholds and named owners that applied to this version of this system on the day in question.

The six sections follow the order in which those answers are needed. Scope establishes what the system is, at which version, who it acts upon rather than merely who uses it, and what the plan explicitly does not reach, since governance fails at the boundary where nobody owns the component. The principles and acceptable-use sections state what is refused as well as what is allowed, which is the only reason the document can refuse anything at all. Data governance records what may be used and for what, because the commonest failure is not a leak but reuse for a purpose nobody re-approved. Fairness records the group affected, the specific way the system could be unfair to them, and the threshold that triggers action, written before the result is known. Accountability names a person rather than a committee, and states where a person affected by an output can contest it. Monitoring and change state what forces the plan to be reopened.

The failure mode is category language. A plan that says data is minimised, protected and monitored, that bias is mitigated, and that compliance is maintained describes an intention rather than a system, and reads identically whether or not anyone has checked. The test is whether a reader who was not in the room can tell what would have to change for a decision to be made differently. So record the model version, the key holder, the numeric threshold, the named individual, the event that triggers review. Where a value genuinely is not yet known, record that it is not known and who must resolve it, which is a far more useful sentence than a plausible-looking category.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* AI Use Case Canvas (PMO-02.04), AI Readiness Assessment (PMO-02.03), Organizational AI Ethics Policy
>   * *Optional:* Data Privacy & Ethics Assessment (PMO-02.06), Project Charter (PMO-03.01)
> * **Downstream Dependents:**
>   * *Mandatory:* AI Model Card (PMO-02.05), Quality Metrics (PMO-04.05.02), Risk Management Plan (PMO-04.08.01)
>   * *Optional:* Prompt Library Register (PMO-05.09), UAT Sign-off Form (PMO-06.10)

---

## Governance Context and Scope

### AI System Inventory
**Instruction:** What the system is, at the version that will actually run, and who operates it. Record the version, because a governance plan that covers "the model" covers whichever model happens to be deployed when someone asks, and the answer is rarely the one that was assessed.

**Generated value:** [ Add details... ]

### Intended Purpose and Affected Users
**Instruction:** What the system is for, and who is subject to its output rather than merely its user. The two are routinely confused, and the confusion is how a system that screens applicants comes to be described as a tool that helps recruiters write better.

**Generated value:** [ Add details... ]

### Risk Classification
**Instruction:** The tier assigned and the criteria that put it there, not the tier alone. A classification with no stated criteria cannot be challenged, and an unchallengeable classification is the same as no classification.

**Generated value:** [ Add details... ]

### Scope Exclusions
**Instruction:** What this plan explicitly does not cover, and who owns it instead. Governance plans fail at the boundary: the component nobody assigned sits under a plan that assumed it was included.

**Generated value:** [ Add details... ]

## Ethical Principles and Acceptable Use

### Ethical Principles
**Instruction:** The principles that constrain use on this project, and the case in which one yields to another. Principles that cannot yield to each other are not a decision rule, and a project under time pressure will resolve the conflict silently and after the fact.

**Generated value:** [ Add details... ]

### Prohibited Uses
**Instruction:** Uses that are refused regardless of benefit. This section is what the plan is for, and a plan listing only permitted uses has no way to refuse anything.

**Generated value:** [ Add details... ]

### Approved Use Cases
**Instruction:** The uses that are approved, each with the limits within which it stays approved. An approved use without stated limits is an approved capability, not an approved use.

**Generated value:** [ Add details... ]

### Human Impact Assessment
**Instruction:** Who bears the consequences of a wrong output, and whether they can tell it was wrong. A system whose subject cannot detect its own errors transfers the cost of error to the person least able to contest it.

**Generated value:** [ Add details... ]

## Data Governance

### Data Category
**Instruction:** What kind of data, in terms a data subject would recognise as being about them.

**Generated value:** [ Add details... ]

### Provenance and Lawful Basis
**Instruction:** Where the data came from and under what basis it is processed. Data that arrived with the model cannot have its basis added later, so a model trained before this question was asked holds data whose status nobody can now evidence.

**Generated value:** [ Add details... ]

### Permitted Use
**Instruction:** What the data may be used for within this system, and what it may not. The most common governance failure is not a leak but reuse for a purpose nobody re-approved.

**Generated value:** [ Add details... ]

### Protection Control
**Instruction:** The specific control applied, not the category of control. "Encrypted" is a category, and the sentence that matters is which key, held by whom, and rotated how.

**Generated value:** [ Add details... ]

### Retention and Deletion
**Instruction:** When the data is deleted, and how deletion is verified. Deletion that is asserted rather than evidenced is how a training set outlives the project that justified it.

**Generated value:** [ Add details... ]

## Fairness, Bias and Transparency

### Affected Group
**Instruction:** The group whose outcomes are affected, named. Groups are described in aggregate on the basis of a test, and the group that matters is the one that performs worst on it.

**Generated value:** [ Add details... ]

### Bias Risk
**Instruction:** The specific way this system could be unfair to this group, stated so it could be false. "Bias risk" as a heading is not a risk; "the model scores this group lower on historic completion rates" is a risk that can be measured and can turn out to be wrong.

**Generated value:** [ Add details... ]

### Test Method and Threshold
**Instruction:** How it is tested and what result triggers action, with the threshold written before the result is known. A threshold set after seeing the number is a description of that number.

**Generated value:** [ Add details... ]

### Mitigation
**Instruction:** What will be done about a confirmed disparity, and what the system does in the meantime. Most bias mitigation plans describe the end state and are silent on whether the system runs while the question is open.

**Generated value:** [ Add details... ]

### Ongoing Indicator
**Instruction:** The metric watched after release, and its frequency. Bias is not a property of a model at launch but of the data it keeps meeting, so the launch measurement is the first of a series and not the last.

**Generated value:** [ Add details... ]

## Compliance and Accountability

### Applicable Regulations
**Instruction:** The instruments that bind this system, named, with the clause where the obligation is specific. A list of regulation names is a research note, not a compliance position.

**Generated value:** [ Add details... ]

### Control Mapping
**Instruction:** Which control satisfies which obligation, and which obligations have no control yet. The second half is the useful half, and a mapping that covers every obligation is nearly always a mapping that was written to be complete rather than to be true.

**Generated value:** [ Add details... ]

### Evidence and Records
**Instruction:** What is retained to demonstrate compliance, for how long, and who may inspect it. Compliance demonstrated only by assertion cannot be audited, and what cannot be audited is not demonstrable to a regulator.

**Generated value:** [ Add details... ]

### Compliance Review Cadence
**Instruction:** How often compliance is revisited and what triggers an off-cycle review. A model version change, a new data source, and a new use are all events, and a plan that reviews only on a calendar will miss all three.

**Generated value:** [ Add details... ]

### Accountable Owner
**Instruction:** The named person answerable for this system's behaviour, with the authority to stop it. Accountability assigned to a committee is distributed to nobody, and the test is whether the named person can halt the system without convening anyone.

**Generated value:** [ Add details... ]

### Human Oversight Points
**Instruction:** The specific points where a human can override, and where they cannot. Oversight that exists everywhere in principle and nowhere in the workflow is a statement of values, and the points that matter are the ones where override is expensive.

**Generated value:** [ Add details... ]

### Decision Rights and Redress
**Instruction:** Who decides what the system is permitted to do after launch, and how a person affected by its output contests that output. Redress is the only mechanism that makes accountability reachable by the person who needs it.

**Generated value:** [ Add details... ]

### Incident Reporting
**Instruction:** What counts as an incident, to whom it is reported, and within what time. An incident definition written broadly enough to catch everything is one nobody can apply under time pressure, and a narrow one misses precisely the cases that were not foreseeable when it was written.

**Generated value:** [ Add details... ]

## Monitoring and Change

### Performance and Drift Monitoring
**Instruction:** What is watched in operation, and against what baseline. A production model is a different system from the one assessed, and the difference accumulates rather than announcing itself.

**Generated value:** [ Add details... ]

### Reassessment Triggers
**Instruction:** The events that require the plan to be reopened, stated so they can be recognised by someone who was not in the room. Triggers described in terms of materiality always resolve towards not triggering.

**Generated value:** [ Add details... ]

### Change Control Link
**Instruction:** How a change to the system is raised, since the system, its data, and its approved uses are all governed by this plan and a change to any of them is a change to the plan.

**Generated value:** [ Add details... ]

---
