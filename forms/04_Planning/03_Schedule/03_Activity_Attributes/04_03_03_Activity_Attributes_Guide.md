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

This document provides a comprehensive reference for understanding the **Activity Attributes** document.

---

### 1. What?
Multiple attributes associated with each schedule activity that can be included within the activity list. It includes activity codes, predecessor/successor activities, logical relationships, leads and lags, resource requirements, imposed dates, constraints, and assumptions.

---

### 2. Why?
While the Activity List provides a high-level overview of what needs to be done, the Activity Attributes provide the granular "how, where, and when." This information is vital for building the mathematical schedule model (Network Diagram) and assigning resources.

---

### 3. When?
Developed throughout the **PLANNING Process Group** (Process 6.2 Define Activities). They are progressively elaborated as more information becomes available.

---

### 4. Who?
**Responsibilities:** Project Manager, Subject Matter Experts (SMEs), and Schedulers.

---

### Tailoring Tips
• Only include the fields you feel necessary to effectively manage your project.
• For projects that use an adaptive development approach you may want to add a field that indicates the planned release or iteration for each activity.

### Alignment
The activity attributes should be aligned and consistent with the following documents:
• Assumption log
• WBS
• WBS dictionary
• Milestone list
• Activity list
• Network diagram
• Duration estimates
• Schedule
• Cost estimates
• Resource requirements


### 5. How?
To accurately and professionally complete the **ACTIVITY ATTRIBUTES**, the responsible party must populate the following details for EVERY activity:

#### 1. General Information
*   **ID:** Unique identifier.
*   **Activity Name:** A brief statement starting with a verb summarizing the activity.
*   **Planned Release / Iteration:** Indicate the planned release or iteration.
*   **Description of Work:** Detailed requirements.

#### 2. Dependencies & Scheduling
*   **Predecessor / Successor:** Identify activities that must occur before or after.
*   **Logical relationships:** Describe the nature of the relationship (e.g., start-to-start, finish-to-start).
*   **Leads and lags:** Required delays (lag) or accelerations (lead) applying to logical relationships.

#### 3. Resource Requirements
*   **Number & Type of Team Resources Required:** Headcount and roles.
*   **Skill Requirements:** Required competency levels.
*   **Required Resources:** Equipment, materials, or facilities.

#### 4. Execution Requirements
*   **Imposed dates:** Required dates for start or completion.
*   **Constraints:** Any limitations.
*   **Assumptions:** Any assumptions impacting the activity.
*   **Location of performance:** Where the work takes place.
*   **Type of effort:** Fixed duration, fixed effort, etc.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](04_03_03_Activity_Attributes_Template.md)
* [🤖 LLM Generation Prompt](04_03_03_Activity_Attributes.md)
* [📊 Data Schema (JSON)](04_03_03_Activity_Attributes.json)
* [📈 Tabular Data - Main (CSV)](04_03_03_Activity_Attributes.csv)
* [📈 Tabular Data - Dependencies (CSV)](04_03_03_Activity_Attributes_Dependencies.csv)
*(Note: ID serves as the relational foreign key)*

</div>
