---
lang: en
layout: default
title: Activity Attributes
nav_order: 3
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">

## Tasleemat Forms Guide
# Project Artifact: Activity Attributes

**Document Reference:** `PMO-04.03.03`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Activity Attributes** in alignment with the
Tasleemat framework.

---

### 1. What?
A comprehensive data sheet capturing technical parameters, logical dependencies, and resource assignments for scheduled activities.

---

### 2. Why?
Provides the precise technical data necessary for accurate critical path calculation and schedule modeling.

---

### 3. When?
Elaborated during activity sequencing and resource estimating within schedule planning.

---

### 4. Who?
Created by Project Scheduler with input from Lead Engineers and Task Owners.

---

### Tailoring Tips
*   Capture story points, dependencies, and assignees directly in agile sprint tracking tools.
*   Maintain exhaustive attribute documentation for safety-critical path activities in infrastructure projects.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Work Breakdown Structure / WBS (PMO-04.02.06)
    *   Scope Statement (PMO-04.02.05)
*   **Optional / Contextual:**
    *   Resource Requirements (PMO-04.06.02)
    *   Risk Register (PMO-04.08.02)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Project Schedule Baseline (PMO-04.03.08)
    *   Earned Value Analysis / EVA (PMO-06.05)
*   **Optional / Contextual:**
    *   Release Plan (PMO-04.03.09)
    *   Lookahead Planning Log (PMO-04.03.10)

---

### 5. How?
To accurately and professionally complete the **Activity Attributes**, the responsible party
must populate the following critical sections based on the project context (ensure `parameters.md` is referenced for global project variables):

*   **Activity Code and Title:** Unique identifier code and full descriptive title of the schedule activity.
*   **Activity Description and Scope Summary:** Detailed technical narrative of the specific scope executed under this activity.
*   **Assigned Work Package Reference:** Corresponding parent WBS code and deliverable component mapping.
*   **Predecessor Activities and Logic:** List of preceding activities with dependency relationships (FS, SS, FF, SF) and lead/lag times.
*   **Successor Activities and Logic:** List of succeeding activities dependent upon the completion or start of this activity.
*   **Required Team Roles and Headcount:** Specific staffing roles, technical disciplines, and quantity of resources required.
*   **Technical Skills and Equipment Needed:** Specialized skill sets, machinery, software licenses, or facilities required for performance.
*   **Imposed Start and Finish Dates:** Contractual or management-mandated fixed start/finish constraint dates.
*   **Activity Assumptions and Location Constraints:** Critical assumptions regarding execution conditions, performance location, and physical constraints.

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [04_03_03_Activity_Attributes_Example.md](../../../../../examples/en/04_Planning/03_Schedule/03_Activity_Attributes/04_03_03_Activity_Attributes_Example.md)

</div>
