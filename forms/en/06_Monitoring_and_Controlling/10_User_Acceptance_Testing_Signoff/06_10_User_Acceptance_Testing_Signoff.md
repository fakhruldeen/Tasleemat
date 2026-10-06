---
type: Form
lang: en
Form: User Acceptance Testing Signoff (Instructions)
---

# User Acceptance Testing Signoff - LLM Generation Prompt

<!--
SYSTEM INSTRUCTIONS: This document is the detailed instruction set for
generating the User Acceptance Testing Signoff. When asked to populate the template, follow the
guidance for each section below to produce the requested content. Refer to
`parameters.md` for the general project variables.
-->

> **Context and Definition:**
> A record of a decision rather than a test report. The testing was performed and written up elsewhere; what this document holds is the business's agreement that the thing tested is the thing they asked for. It is the only artifact in this set that cannot be taken back quietly: development testing continues past a failure, and once the business has signed, the project moves on and the outstanding findings stop being worked on.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Approved Project Baselines (PMO-04.01.01), Work Performance Data & Logs (PMO-05.01 - 05.12)
>   * *Optional:* Risk Register (PMO-04.08.02), Vendor Agreements (PMO-04.09.04)
> * **Downstream Dependents:**
>   * *Mandatory:* Change Requests (PMO-05.03), Project / Phase Closeout (PMO-07.03), Lessons Learned Summary (PMO-07.01)
>   * *Optional:* Transition to Operations Checklist (PMO-07.04), Value Realization Register (PMO-01.03)

---

## Acceptance Record

### Test Summary
**Instructions:** What was tested, stated so that a reader can tell whether this was the whole release or a slice of it, and so that the criteria below can be read against something. "The system" is not a test summary; "the three checkout flows plus the refund path" is.

**Generated Value:** [ Add details... ]

### Testing Environment
**Instructions:** Where the testing took place and against what. The environment and the build are part of what was accepted: a pass on a developer's machine is not a pass on the environment the business will use, and a signature that does not record which one was tested cannot be relied on at go-live.

**Generated Value:** [ Add details... ]

### Pass/Fail Criteria
**Instructions:** What was decided before the testing began, not what was concluded after it. The criteria are what make the result mean anything: "the system works" cannot fail, because every system works on the day it is demonstrated, and a criterion written afterwards describes the outcome.

**Generated Value:** [ Add details... ]

### Known Defects
**Instructions:** What was found and accepted rather than fixed, with the severity and who agreed to carry it. This section is what makes the signature honest: an empty defects section says the testing found nothing, which is almost never what happened, and a reader who knows that stops trusting the signature. Anything still open at go-live is discovered by somebody with no authority left to stop it.

**Generated Value:** [ Add details... ]

### Business Owner Sign-off
**Instructions:** The decision, stated in the business's own terms rather than as a signature alone. What is being accepted, what is being accepted with, and what happens if something turns out not to work. This is the line that is read later when the question is whether the business agreed to this.

**Generated Value:** [ Add details... ]

---
