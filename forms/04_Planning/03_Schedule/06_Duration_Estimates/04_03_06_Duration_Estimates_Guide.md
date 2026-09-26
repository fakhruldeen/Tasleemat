---
lang: en
layout: default
title: Duration Estimates
nav_order: 1
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">

## Tasleemat Forms Guide
# Project Artifact: Duration Estimates

**Document Reference:** `PMO-04.03.06`

This document provides a comprehensive, professional reference to understand the purpose and effective usage of the **Duration Estimates** in alignment with Tasleemat framework.

---

### 1. What?
A formal Tasleemat-aligned project document known as the **Duration Estimates**, utilized to plan, document, and manage the critical elements related to this specific knowledge area.

---

### 2. Why?
To ensure strict alignment with Tasleemat standards, establish transparency, monitor project performance, and control variances effectively throughout the project life cycle.

---

### 3. When?
This artifact is primarily prepared, utilized, and updated during the **PLANNING Process Group** of the project lifecycle.

---

### 4. Who?
**Responsibilities:** Developed by the Project Manager with input from the project team and Subject Matter Experts (SMEs), then baselined.

---

### 5. How?
To accurately and professionally complete the **Duration Estimates**, the responsible party must populate the following critical sections based on the project context (ensure `parameters.md` is referenced for global project variables):

*   **ID**
*   **Unique identifier**
*   **Parametric estimates:** Effort hours Enter amount of labor it will take to accomplish the work. Usually shown in hours, but may also be shown in days. Example: 150 hours
*   **Resource quantity:** Document the number of resources available. Example: 2 people
*   **Percent available:** Enter amount of time the resources are available. Usually shown as the percent of time available per day or per week. Example: 75 percent of the time
*   **Performance factor:** Estimate a performance factor if appropriate. Generally effort hours are estimated based on the amount of effort it would take the average resource to complete the work. This can be modified if you have a highly skilled resource or someone who has very little experience. The more skilled the resource, the lower the performance factor. For example, an average resource would have a 1.0 performance factor. A highly skilled resource could get the work done faster, so you multiply the effort hours times a performance factor of .8. A less skilled resource will take longer to get the work done, so you would multiply the effort hours times 1.2. Example: A skilled worker with a performance factor of .8
*   **Duration estimate:** Divide the effort hours by the resource quantity times the percent available times the performance factor to determine the length of time it will take to accomplish the work. The equation is: Effort/ ( quantity × percent available × performance factor ) = duration Example: 150/ ( 2 × ⋅75 × ⋅8 ) = 125 hours
*   **Analogous estimates:** Previous activity Enter a description of the previous activity. Example: Build a 160 square foot deck.
*   **Previous duration:** Document the duration of the previous activity. Example: 10 days
*   **Current activity:** Describe how the current activity is different. Example: Build a 200 square foot deck.
*   **Multiplier:** Divide the current activity by the previous activity to get a multiplier. Example: 200/160 = 1.25
*   **Most likely duration:** Determine a most likely duration estimate. Most likely estimates assume that there will be some delays but nothing out of the ordinary. Example: 25 days
*   **Pessimistic duration:** Determine a pessimistic duration estimate. Pessimistic estimates assume there are significant risks that will materialize and cause delays. Example: 36 days
*   **Weighting equation:** Weight the three estimates and divide. The most common method of weighting is the beta distribution: tE = (tO + 4tM + tP)/6 Example: (20 + 4(25) + 36 )/6
*   **Expected duration:** Enter the expected duration based on the beta distribution calculation. Example: 26 days

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](04_03_06_Duration_Estimates_Template.md)
* [🤖 LLM Generation Prompt](04_03_06_Duration_Estimates.md)
* [📊 Data Schema (JSON)](04_03_06_Duration_Estimates.json)
* [📈 Tabular Data (CSV)](04_03_06_Duration_Estimates.csv)

</div>
