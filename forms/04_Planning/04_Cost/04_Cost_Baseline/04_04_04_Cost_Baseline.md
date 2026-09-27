---
lang: en
Form: COST BASELINE (Instructions)
---

# COST BASELINE - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `COST BASELINE`. When asked to populate this form, provide the budget summary, the time-phased budget table, and a mermaid xychart-beta representing the S-Curve.

> **Context & Definition:**
> The cost baseline is a time-phased budget used to measure, monitor, and control cost performance. It is developed by summing the costs of the project by the time period and developing a cumulative cost curve (S-curve). It includes contingency reserves but excludes management reserves.
> 
> **Alignment:**
> The cost baseline should be aligned with the Assumption log, Project schedule, Cost estimates, Project team assignments, and Risk register.

---

### Section Generation Instructions
**1. Budget Summary:**
*   **Component:** The structural element of the budget (Activity Cost Estimates, Contingency Reserve, Cost Baseline, Management Reserve, Total Project Budget).
*   **Amount:** The total allocated funds for that component.

**2. Time-Phased Budget:**
*   **Period:** The specific time period (e.g. Month 1, Month 2, Q1).
*   **Planned Period Cost:** The cost planned to be spent during this specific period.
*   **Cumulative Cost:** The running total of planned costs up to and including this period (this represents the S-Curve).
*   **Remarks / Key Activities:** The major work packages or deliverables driving the cost in this period.

**3. S-Curve Graphic:**
*   Generate a `mermaid` diagram of type `xychart-beta`.
*   The `x-axis` should be the Periods using short alphanumeric strings (e.g. `[P1, P2, P3]`) to avoid Mermaid lexical errors.
*   The `y-axis` should map to the Cumulative Cost scale.
*   Use `line` for Cumulative Cost and `bar` for Planned Period Cost.
