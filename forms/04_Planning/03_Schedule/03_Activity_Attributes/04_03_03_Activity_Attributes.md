---
lang: en
Form: ACTIVITY ATTRIBUTES (Instructions)
---

# ACTIVITY ATTRIBUTES - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `ACTIVITY ATTRIBUTES`. When asked to populate this form, generate an array of detailed attribute objects for each scheduled activity.

---

### Activity Entries
**Instruction:** Repeat the following block of attributes for EVERY activity defined in the Activity List.

#### 1. General Information
*   **ID:** Unique identifier.
*   **Activity Name:** A brief statement starting with a verb summarizing the activity.
*   **Planned Release / Iteration:** Indicate the planned release or iteration.
*   **Description of Work:** Detailed requirements.

#### 2. Dependencies & Scheduling
**Instruction:** Generate a table of dependencies.
*   **Columns:** Predecessor, Predecessor Relationship, Predecessor Lead/Lag, Successor, Successor Relationship, Successor Lead/Lag.

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
