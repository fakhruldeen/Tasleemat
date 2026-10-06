---
type: Form
lang: en
Form: INTERDEPENDENCY REGISTER (Instructions)
token_pointer: /_tokens/forms/en/00_Program_and_Portfolio_Management/03_Interdependency_Register/00_03_Interdependency_Register.npy
token_count: 1913
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.036782+00:00'
---

# INTERDEPENDENCY REGISTER - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the
> `INTERDEPENDENCY REGISTER`. When asked to populate this form, use the guidance
> provided for each section below to accurately generate the required content.
> Reference `parameters.md` for global project variables.

> **Context & Definition:**
> The interdependency register records the relationships between the components
> of a program, portfolio, or project, in the specific sense that one cannot
> proceed, or cannot proceed on its own dates, until another delivers
> something. It is a forward-looking record: it is what tells the reader what
> will have to be true before the plan works.

> **Alignment:**
> This interdependency register must be consistent with: Portfolio roadmap,
> Program charter, Project management plan, Schedule management plan.

### Register Scope and Level

**Instruction:** What this register covers and at what level it is maintained, whether portfolio-wide, program-level, or project-level. The level decides which plan the register is compared against, and a portfolio register read against a project schedule produces conclusions that are true of neither.

**Generated value:** [ Add details... ]

### Programs or Projects Covered

**Instruction:** The programs, projects, or components whose mutual dependencies are recorded, by name and identifier so the list can be joined to the portfolio roadmap. A register that names no components cannot be checked for completeness, and an incomplete register reads as a complete one.

**Generated value:** [ Add details... ]

### Source of Truth or Extract

**Instruction:** Whether this register is the authoritative record or an extract from a planning tool. Record which, because a reader who treats an extract as authoritative will act on a date that has since moved, and the error is invisible until the dependency is missed.

**Generated value:** [ Add details... ]

### Review Cycle

**Instruction:** How often the register is reviewed and by which forum. The cycle is what makes two versions comparable, and a register refreshed on no cycle describes the portfolio as it once was rather than as it is.

**Generated value:** [ Add details... ]

### Register Owner

**Instruction:** The single role accountable for the register as a whole, which is normally not the owner of any one dependency in it. Where this is left blank, the register has contributors but no one who notices that a row has gone stale.

**Generated value:** [ Add details... ]

### Last Updated

**Instruction:** The date the register was last reviewed, and against which version of the portfolio roadmap. Without it, a reader has no way to tell a current register from an abandoned one, and the two look identical on the page.

**Generated value:** [ Add details... ]

### ID

**Instruction:** The identifier for the dependency, used in the escalation section and in reporting so a threatened dependency can be referred to without ambiguity.

**Generated value:** [ Add details... ]

### Predecessor

**Instruction:** The project or component that must deliver first, named and identified so the row can be joined to the portfolio roadmap. "Project B" is not a predecessor; the component's own identifier is, because that is what survives it being renamed.

**Generated value:** [ Add details... ]

### Successor

**Instruction:** The project or component that is waiting. Where the same predecessor is needed by several successors, record a row for each rather than listing them together, because the required dates and the impacts differ and one date cannot serve all of them.

**Generated value:** [ Add details... ]

### Deliverable or Condition

**Instruction:** What specifically is being waited on, stated so that it can be confirmed as delivered or not. "Waiting for Project B" cannot be chased when Project B slips, because nobody knows what to ask for; "waiting for the signed data migration specification from Project B" can be chased, and can be closed.

**Generated value:** [ Add details... ]

### Dependency Type

**Instruction:** Whether the relationship is Finish to Start, Start to Start, Finish to Finish, or Start to Finish. The type determines how much float the successor has, and Finish to Start is the only one needing no explanation; the others arise where two projects must move together and cannot be read from the names alone.

**Generated value:** [ Add details... ]

### Required By

**Instruction:** The date by which the successor needs the deliverable. This is the successor's requirement, and recording the predecessor's forecast here instead hides the gap between what is needed and what has been promised, which is the only figure worth watching.

**Generated value:** [ Add details... ]

### Agreed Date

**Instruction:** The date the predecessor has committed to. Kept beside the required date so the gap between the two is visible in the register itself; where the agreed date is later than the required date, that gap is the dependency's risk, and it is usually found out by being overrun rather than by being read.

**Generated value:** [ Add details... ]

### Status

**Instruction:** Where the dependency currently stands against the fixed set agreed for this register, such as On Track, At Risk, Breached, or Agreed. A free-text status cannot be filtered, and a register of forty dependencies that cannot be filtered is a document nobody consults when they need to answer a question about one of them.

**Generated value:** [ Add details... ]

### Impact if Late

**Instruction:** What happens to the successor if the predecessor misses the required date, in schedule, cost, or scope terms. A dependency with no stated impact cannot be escalated, because nobody can say what is at stake, and an escalation that cannot state the stake is usually declined.

**Generated value:** [ Add details... ]

### ID

**Instruction:** The identifier for the external dependency, so it can be referred to in reporting and joined to any contract or correspondence that covers it.

**Generated value:** [ Add details... ]

### External Party

**Instruction:** The organisation outside the program through which the dependency runs, named by the role it plays rather than by the individual, so the row survives a change of contact and remains readable to someone who has not met them.

**Generated value:** [ Add details... ]

### Dependency Description

**Instruction:** What the external party is expected to provide, approve, or decide, and by when. State it as something that can be confirmed as done, since a dependency described as ongoing support cannot be closed and will therefore never show as satisfied.

**Generated value:** [ Add details... ]

### Contractual Basis

**Instruction:** Whether the dependency is covered by a contract, a memorandum of understanding, a formal letter, or nothing in writing. This column decides whether the dependency can be enforced, and a commitment taken in correspondence and one written into a contract look identical in every other column while being entirely different in practice.

**Generated value:** [ Add details... ]

### Required By

**Instruction:** The date the program needs this, which for an external dependency is usually a hard commercial or regulatory date rather than a date the program chose. Record where the date comes from, because an external date the program did not set is a date it cannot move.

**Generated value:** [ Add details... ]

### Status

**Instruction:** Where the dependency stands against the fixed set. For external dependencies record separately whether the external party has confirmed it, since the program can know its own position accurately and the other party's only by asking.

**Generated value:** [ Add details... ]

### Owner

**Instruction:** Who is accountable for the relationship with the external party, which is normally not the person who needs the deliverable. Separating the two is what stops the urgency of a need being communicated through whoever happens to have the contact.

**Generated value:** [ Add details... ]

### Dependency ID

**Instruction:** The dependency the escalation concerns, so the row can be joined back to the register. An escalation recorded without this reference cannot be traced to the thing it was about, and the next cycle repeats it.

**Generated value:** [ Add details... ]

### Trigger

**Instruction:** What caused the escalation: a missed agreed date, an explicit refusal, a change on the predecessor's side, or a commercial dispute. The remedy differs in each case, and an escalation that does not distinguish them tends to produce a general escalation that resolves nothing.

**Generated value:** [ Add details... ]

### Escalated To

**Instruction:** Who it was escalated to, named rather than described, so the reader knows whether the person holds the authority to decide. An escalation to somebody who cannot decide records the disagreement without recording a resolution.

**Generated value:** [ Add details... ]

### Action Agreed

**Instruction:** What was decided or agreed, which is what stops the same question being escalated again next cycle with the same outcome. Where nothing was agreed, record that explicitly, because a blank action and an unresolved escalation look identical once the register has been read a few times.

**Generated value:** [ Add details... ]

### Date

**Instruction:** When the escalation happened, and where relevant when it will next be reviewed. An escalation without a date has no position in the sequence, and the register becomes a list of grievances rather than a record of decisions.

**Generated value:** [ Add details... ]
