---
lang: en
Form: DATA PRIVACY AND ETHICS ASSESSMENT (Instructions)
---

# DATA PRIVACY AND ETHICS ASSESSMENT - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the
> `DATA PRIVACY AND ETHICS ASSESSMENT`. When asked to populate this form, use the guidance
> provided for each section below to accurately generate the required
> content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> A privacy assessment is written by people who are about to do something to a person they will never meet, and it is the only document that forces that asymmetry into the open. Everything else about the work is legible to the team doing it: the schema, the throughput, the cost per request. What is not legible is what happens to the person whose record is in the table, and that is the whole subject of this form. The team that fills it in is not the team that answers for it, which is why the form is a record rather than a feeling.

The seven sections follow the order the questions arrive. Scope and inventory record what is covered and, more importantly, what is not, because an assessment that does not state its exclusions will be read as covering everything and the untested processing lives in that gap. The inventory is a list rather than a count, and it separates the owner from the custodian, since accountability follows the custodian and the budget follows the owner. Lawful basis is recorded per purpose rather than per dataset, because one dataset commonly serves several purposes with very different necessity, and necessity is the question that actually gets asked. Secondary use is called out separately: it is the most common failure in analytics work and the least likely to be noticed, because every individual field still has a lawful origin. Consent records the version of the text that was shown, because a consent record without it cannot be defended later, and withdrawal records whether honouring it is as easy as granting it, since that asymmetry is the standard test. Individual rights records what happens to data that has been aggregated, shared, or trained into a model, and the answer is not that it was deleted, because deleting a row does not unlearn a model. Retention records the basis for each period rather than a default, and deletion records its coverage, because a deletion applied to the primary store while the data persists in replicas, logs, exports and model weights is the most frequent finding in any such assessment. Security records who holds the keys, not only what is encrypted. Sharing gives each recipient its own row and its own basis, because a processor bound by contract is not the same arrangement as a controller sharing on its own purpose, and cross-border transfer is not a hosting region, since remote access by foreign staff is a transfer that no region setting records.

The seventh section is where this form differs from the others in this group. The sixth asks what harm the processing causes that no law prohibits, and it exists because compliance is a floor rather than a ceiling: processing can be lawful, consented, retained properly, secured properly and shared properly, and still be wrong. A form that stops at lawful has answered the question that was easy to answer, and the people who read it will believe the work is finished. Vulnerable individuals, transparency as the recipient reads it rather than the drafter, dark patterns and consent fatigue, and the fairness of automated outcomes are all findings a category-and-volume record cannot produce. The last section records what was found, the risk remaining after the planned actions and who accepts it until when, what happens in the interim because that is where a known finding actually operates, and what would reopen the assessment, since triggers stated after the change are a record of the change rather than a control against it.

The value of the form is in the fields that are inconvenient. An assessment with no exclusions, no secondary use, no deletion-coverage statement, no withdrawal route and no ethics findings describes processing that has not started, because each of those is filled in by something that happened rather than by something that was decided. So the fields to insist on are the ones with no good answer available: where deletion does not reach, what happens to a person whose data is in a trained model, who can refuse and who cannot, and what harm remains after compliance is satisfied. Where a value genuinely is not known, record that it is not known and who must resolve it, which is more useful than a plausible answer, because a plausible answer will be relied on and a declared gap will be closed.

> **Alignment:**
> This data privacy and ethics assessment must be consistent with: AI governance plan, AI model card and fact sheet, risk management plan, data management plan, stakeholder register.

---

## Scope, Data Inventory and Ownership

### Assessment Scope
**Instruction:** The processing, systems, and periods this assessment covers, stated so that its edges are visible. An assessment that does not say what it excludes will be read as covering everything, and the gap between the two is where the untested processing lives.

**Generated value:** [ Add details... ]

### Processing Out of Scope
**Instruction:** What is explicitly not covered, and why. Excluded because another assessment covers it, or excluded because it was not looked at, are very different statements and only the second one is a finding.

**Generated value:** [ Add details... ]

### Data Owners and Custodians
**Instruction:** Who owns each data asset and who administers it day to day. Ownership and custody differ, and the accountability clause follows the custodian while the budget follows the owner.

**Generated value:** [ Add details... ]

### Data Inventory
**Instruction:** One row per data asset: what it is, who owns it, the purpose it is held for, whether it holds personal data, whether that data is special category, and its volume and refresh rate. An inventory described as a count rather than as a list cannot answer any of the questions that follow.

**Generated value:** [ Add details... ]

### Data Flow and Recipients
**Instruction:** Where the data moves, and who receives it. The flow is what determines which transfers need a mechanism, and a flow that shows only the primary store hides the copies.

**Generated value:** [ Add details... ]

## Lawful Basis and Purpose Limitation

### Processing Purposes and Necessity
**Instruction:** What each processing activity is for, and why it cannot be achieved with less data or a shorter reach. Necessity is assessed per purpose rather than per dataset, because one dataset frequently serves several purposes with very different necessity.

**Generated value:** [ Add details... ]

### Lawful Basis by Purpose
**Instruction:** One row per purpose: the data processed, the basis relied on, the basis for special category data where any is present, and the justification. A form that records a basis once for a dataset will carry one basis across purposes that do not share it.

**Generated value:** [ Add details... ]

### Purpose Compatibility and Secondary Use
**Instruction:** Whether the data is used for any purpose other than the one collected for, and on what basis. Secondary use is the most common privacy failure in analytics work and the one least likely to be noticed, because every individual field still has a lawful origin.

**Generated value:** [ Add details... ]

### Automated Decision-Making
**Instruction:** Any decision made about a person with no meaningful human involvement, the logic involved, and the consequences for them. Recorded because the assessment of a legal basis does not by itself establish that a decision is one a person could contest.

**Generated value:** [ Add details... ]

## Consent and Transparency

### Consent Mechanism
**Instruction:** How consent is requested, and where in the flow it appears. Consent collected after the data is already in use is a record, not a request, and the difference determines what the record is worth.

**Generated value:** [ Add details... ]

### Consent Specificity and Granularity
**Instruction:** What the person was told they were consenting to, and whether the choices are separate. A single consent covering several purposes is consent to none of them in particular, and a bundle of pre-ticked boxes is not a choice.

**Generated value:** [ Add details... ]

### Consent Recording and Evidence
**Instruction:** Where each consent is stored, with the timestamp, the version of the text shown, and the interface shown. A consent record without the version of the text cannot be defended later, because the terms the person agreed to are then unrecoverable.

**Generated value:** [ Add details... ]

### Withdrawal
**Instruction:** How a person withdraws, how much easier it is than granting, and what happens to data already processed on that basis. Asymmetry between granting and withdrawing is the standard test, and a withdrawal that is honoured prospectively only leaves the processing intact behind it.

**Generated value:** [ Add details... ]

### Privacy Notices and Just-in-Time Disclosure
**Instruction:** What is told at collection, what is told at the point the data is used, and where either may be found. A notice published once and never revisited informs nobody who meets the processing for the first time in month three.

**Generated value:** [ Add details... ]

## Individual Rights

### Rights Handling Process
**Instruction:** How a request is received, routed, decided and answered, and by whom. A right stated in a policy with no route to exercise it is a stated right, and it is tested only when someone uses it.

**Generated value:** [ Add details... ]

### Identity Verification
**Instruction:** How the requester is confirmed to be who they claim, and what is refused when that cannot be done. Verification that accepts anyone discloses data; verification that refuses everyone denies the right, and the balance is a decision to record rather than a default.

**Generated value:** [ Add details... ]

### Response Timeframes and Escalation
**Instruction:** The deadline for each type of request, what happens when it is missed, and who is told. The clock is the whole of the right in practice, because a correct answer delivered late is still a breach.

**Generated value:** [ Add details... ]

### Rights Over Derived, Shared and Retired Data
**Instruction:** What happens to a request where the data has been aggregated, shared with a third party, or placed in a model. Deletion cannot reach a trained model by deleting a row, and the form that does not say so will be read as having deleted it.

**Generated value:** [ Add details... ]

## Retention, Security and Sharing

### Retention Schedule
**Instruction:** One row per data asset: the retention period, the basis for that period rather than the convention, what triggers deletion, and how deletion is verified. A period adopted as a default and recorded as a decision is the most common entry, and it is the reason data outlives every justification that justified it.

**Generated value:** [ Add details... ]

### Deletion Mechanism and Coverage
**Instruction:** How deletion is carried out, across primary stores, replicas, logs, exports and derived copies. Deleting a row from one table while the data persists in five other places is the most frequent finding in any such assessment, and it is invisible without a coverage statement.

**Generated value:** [ Add details... ]

### Backups and Derived Data
**Instruction:** How deletion propagates to backups and to models trained on the data, and over what period. Backups are the usual reason a deletion is incomplete, and a trained model is a copy no deletion request reaches.

**Generated value:** [ Add details... ]

### Access Controls and Least Privilege
**Instruction:** Who can reach the data, by what route, under what approval, and how access is reviewed. Access is the control that fails quietly, since misuse of legitimate credentials is indistinguishable from legitimate use without a review.

**Generated value:** [ Add details... ]

### Encryption and Key Management
**Instruction:** What is encrypted in transit and at rest, and who holds the keys. Encryption whose keys sit beside the data is a control on paper, and the key custody arrangement is the part that is not written down.

**Generated value:** [ Add details... ]

### Third-Party Sharing
**Instruction:** One row per recipient: the recipient, the purpose, the data shared, the contractual safeguard relied on, and the region processed in. Each row needs its own basis, because a processor bound by contract to a controller is not the same arrangement as a controller sharing on its own purpose.

**Generated value:** [ Add details... ]

### Cross-Border Transfers
**Instruction:** Where data or processing leaves the jurisdiction, under which transfer mechanism, and what supplementary measures apply. A hosting region is not a transfer analysis, and remote access by a foreign staff member is a transfer that no region setting records.

**Generated value:** [ Add details... ]

### Breach Notification
**Instruction:** What constitutes a breach here, who is notified, within what time, and who decides. Recorded because a response plan written after an incident is always written for that incident, and the decision threshold is the part that is usually left out.

**Generated value:** [ Add details... ]

## Ethics Beyond Compliance

### Harm Beyond Legal Exposure
**Instruction:** Where this processing causes harm that no law prohibits. This section exists because compliance is a floor: processing can be lawful, consented, retained properly and shared properly, and still be wrong, and a form that stops at lawful has answered the question it was easy to answer.

**Generated value:** [ Add details... ]

### Vulnerable Individuals and Groups
**Instruction:** Who is affected in a state of reduced ability to refuse, to understand, or to bear the consequence. Vulnerability here is a property of the situation rather than of the person, and it is invisible to a record of categories and volumes.

**Generated value:** [ Add details... ]

### Transparency to Affected People
**Instruction:** What the people in the data are actually told, in language they use, as distinct from what the notice says. A notice that is accurate, complete and unread is the standard failure, and reading it as a recipient rather than as a drafter is the only way to see it.

**Generated value:** [ Add details... ]

### Manipulation, Dark Patterns and Consent Fatigue
**Instruction:** Whether the interface nudges, pre-ticks, buries refusal, or asks repeatedly, and whether the volume of requests is such that a refusal is impractical. Consent obtained by a design choice is not freely given, whatever the record says.

**Generated value:** [ Add details... ]

### Fairness of Automated Decisions
**Instruction:** Whether the processing produces outcomes for people, and what the distribution of those outcomes is across groups. A lawful basis for a decision is not a defence of its fairness, and the two are assessed against different questions.

**Generated value:** [ Add details... ]

## Findings, Remediation and Review

### Findings Register
**Instruction:** One row per finding: the finding, the risk it poses to individuals, the severity, the owner, and the action being taken. Severity is what determines the order of work, and a register with no severity column is a list of observations.

**Generated value:** [ Add details... ]

### Residual Risk and Acceptance
**Instruction:** The risk remaining after the planned actions, who accepts it, and until when. Acceptance is a decision with an owner and an expiry date; an acceptance with neither is an unowned risk that will be rediscovered at the next assessment.

**Generated value:** [ Add details... ]

### Remediation Plan
**Instruction:** The actions, their owners and their dates, and what is being done in the interim. The interim period is where a known finding actually operates, so it is the part of the plan most worth writing down.

**Generated value:** [ Add details... ]

### Review Triggers
**Instruction:** What would cause this assessment to be revisited before its scheduled date, such as a new purpose, a new recipient, a new model, or a regulatory change. Triggers stated after the change have occurred are a record of the change.

**Generated value:** [ Add details... ]

### Reassessment Triggers
**Instruction:** When this assessment expires and on what cycle. An assessment with no expiry is treated as permanent by everyone who did not write it, including the people who inherited it.

**Generated value:** [ Add details... ]

---
