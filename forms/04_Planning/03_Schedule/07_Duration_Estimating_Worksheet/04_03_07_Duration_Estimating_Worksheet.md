---
lang: en
Form: DURATION ESTIMATING WORKSHEET (Instructions)
> **CRITICAL RULE:** A single project will likely use multiple estimation methods, but **each individual activity should only be estimated using ONE method**. Do not duplicate the same activity ID across different tables. Place each activity in the single table that best fits its estimation approach.

---

# DURATION ESTIMATING WORKSHEET - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `DURATION ESTIMATING WORKSHEET`. Generate three JSON arrays corresponding to the Parametric, Analogous, and Three-Point estimating methods.

> **Context & Definition:**
> A duration estimating worksheet helps develop duration estimates when quantitative methods are used (Parametric, Analogous, or Three-point). It is an input to Duration Estimates and an output from process 6.4 Estimate Activity Duration in the PMBOK® Guide.
> 
> **Alignment:**
> The duration estimating worksheet should be aligned and consistent with the following documents:
• Assumption log
• Scope baseline
• Activity list
• Activity attributes
• Resource requirements
• Risk register

---

### 1. Parametric Estimates
**Instruction:** Calculate duration using effort and resource parameters.
*   **ID:** Unique identifier.
*   **Activity description:** A brief description of the work.
*   **Effort hours:** Amount of labor to accomplish work.
*   **Resource quantity:** Number of resources assigned.
*   **Percent available:** % of time resources are available.
*   **Performance factor:** Productivity factor (1.0 is average).
*   **Duration estimate:** Effort / (Qty * % Avail * Perf Factor).

### 2. Analogous Estimates
**Instruction:** Calculate duration using historical comparisons.
*   **ID:** Unique identifier.
*   **Activity description:** A brief description of the work.
*   **Previous activity:** Description of past similar work.
*   **Previous duration:** Duration of past work.
*   **Current activity:** Description of current work.
*   **Multiplier:** Ratio of current vs previous size/complexity.
*   **Duration estimate:** Prev Duration * Multiplier.

### 3. Three-Point Estimates
**Instruction:** Calculate duration using risk-weighted scenarios (Beta distribution).
*   **ID:** Unique identifier.
*   **Activity description:** A brief description of the work.
*   **Optimistic (tO):** Best-case scenario.
*   **Most Likely (tM):** Normal scenario.
*   **Pessimistic (tP):** Worst-case scenario.
*   **Weighting Equation:** Usually (tO + 4tM + tP) / 6.
*   **Expected Duration (tE):** The calculated result.
