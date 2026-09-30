---
lang: en
layout: default
title: Impediment Log
nav_order: 7
---

## Tasleemat Forms Guide
# Project Artifact: Impediment Log

**Document Reference:** `PMO-05.10`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Impediment Log** in alignment with the
Tasleemat framework.

---

### 1. What?
A table of the things standing between the team and its work, one row each: an identifier, the date it was raised, what it is, what it costs while it stands, who is pursuing it, and whether it is open, in progress or resolved. The owner column is the one that distinguishes this from an issue list, because it names the person chasing the obstacle rather than the person blocked by it.

---

### 2. Why?
Because an impediment that is absorbed is an impediment that is hidden. A team that works around one looks productive for exactly as long as the workaround holds, and the cost of the workaround arrives later and separately, where nobody connects it to the decision not to ask. The log also accumulates something an issue list does not: a record of how each one was cleared, which is the part the next team can actually use.

---

### 3. When?
Raised as soon as it is recognised, and not batched to the end of the cycle. The date it was raised is what makes a stale one visible, because an entry with no date is one nobody can tell has been sitting there. It is closed when the impediment is gone, not when it stops being inconvenient.

---

### 4. Who?
Raised by whoever hits it, which on an agile team is any member rather than the lead. That is the point of the form: the person nearest an obstacle is the one best placed to name it, and a log that only the lead writes is a log of what the lead noticed. The team lead signs because escalation is their responsibility, and the project manager signs because most impediments can only be cleared above the team.

---

### Tailoring Tips
*   Raise it rather than absorb it. The workaround is cheaper this cycle and it hides the cost, which is the whole reason the cost is not being argued about.
*   Name the cost, not the annoyance. An entry that says the work is blocked without saying what it costs cannot be weighed against the other things that need the same person.
*   Write the resolution. The entry closes when the impediment is gone, and the note about how it went is the part anyone can reuse.

---

### Alignment
the issue log, the decision log, and the risk register, because an impediment that recurs is a risk being realised

---

### 5. How?
To accurately complete the Impediment Log, populate the following sections based on
the project context (ensuring reference to `parameters.md` for the general
project variables):

*   **Impediment ID:** A short identifier, so an impediment can be referred to in a stand-up without being described again. A number is enough if it is the only one in use.
*   **Date Raised:** When it was identified. The date is what makes an old impediment visible: an entry with no date is one nobody can tell has been sitting there.
*   **Description:** What is standing between the team and the work, in terms someone outside the team would understand. A description the reader can only decode by asking is not one that can be escalated.
*   **Impact:** What it costs while it stands: the work it holds up and what that costs in the cycle. An impediment with no stated impact cannot be prioritised against anything else.
*   **Owner:** Who is pursuing the resolution, which is not the same as who the impediment affects. The person raising it may be pursuing it and the person who can remove it may be elsewhere.
*   **Status:** Open, in progress, or resolved, and the date it was resolved. A resolved entry with no resolution recorded is worth little, because the next team to hit it cannot use what was learned.

---

### Associated Templates
* [📄 Printable Template (Markdown)](05_10_Impediment_Log_Template.md)
* [🤖 Smart Generation Prompt](05_10_Impediment_Log.md)
* [📊 Data Structure (JSON)](05_10_Impediment_Log.json)
* [📈 Tabular Data (CSV)](05_10_Impediment_Log.csv)
