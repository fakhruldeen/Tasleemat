---
lang: en
Form: EARNED VALUE ANALYSIS REPORT (Instructions)
---

# EARNED VALUE ANALYSIS REPORT - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `EARNED VALUE ANALYSIS REPORT`.

> **Context & Definition:**
> Earned value analysis shows specific mathematical metrics that are designed to reflect the health of the project by integrating scope, schedule, and cost information. It is used to forecast total cost at completion and required efficiency.

> **Period columns:**
> Every metric table in sections 1 through 4 is reported across three period columns -
> **Current Reporting Period**, **Current Period Cumulative**, and **Past Period
> Cumulative**. Populate all three columns for each metric. `Budget at Completion (BAC)`
> is a single figure and is not restated per period.

**Tailoring Tips:**
*   The earned value analysis can be done at the control account and/or project level depending on your needs.
*   You may want to add a field that indicates the implications of continued variance. This can include a forecast based on a trend analysis or based on identified responses.
*   Several different equations can be used to calculate the EAC depending on whether the remaining work will be completed at the budgeted rate or at the current rate.
*   There are options to calculate a TCPI. Use the information from your project to determine the best approach for reporting.
*   You may want to add information that indicates the implications of continued schedule variance. This can include a schedule forecast using SPI as the basis for a trend analysis or based on analyzing the critical path.

**Alignment:**
Earned value analysis should be aligned and consistent with the following documents:
*   Project status report
*   Project schedule
*   Project budget
*   Variance analysis
*   Contractor status report

---

### Section Generation Instructions
*   **Report Information:** Provide the reporting period dates, level of analysis (e.g., project, control account), and the project manager's name.
*   **Basic Earned Value Metrics:** Enter Budget at Completion (BAC) once, then enter Planned Value (PV), Earned Value (EV), and Actual Cost (AC) for each of the three period columns.
*   **Variances and Indices:** Calculate Schedule Variance (SV = EV - PV), Cost Variance (CV = EV - AC), Schedule Performance Index (SPI = EV / PV), and Cost Performance Index (CPI = EV / AC) for each period column.
*   **Percentages:** Indicate Percent Planned (PV / BAC), Percent Earned (EV / BAC), and Percent Spent (AC / BAC) for each period column.
*   **Forecasting (Estimates):** Calculate EAC w/CPI (BAC / CPI), EAC w/CPI x SPI (AC + ((BAC - EV) / (CPI x SPI))), and TCPI ((BAC - EV) / (BAC - AC)) for each period column, then record the selected EAC and justify the choice.
*   **Root Cause and Impacts Analysis:** Describe the root causes for variances and their impact on budget, critical path, and deliverables, including trend analysis implications.
*   **Comments:** Document any comments that add relevance to this report.
