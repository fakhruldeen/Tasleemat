<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <a class="lang-switch-btn" href="../../../ar/04_التخطيط/06_الموارد/04_06_03_هيكل_تجزئة_الموارد_(RBS)_دليل.html">🇸🇦 الانتقال للدليل بالعربية (Arabic Guide) →</a>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-04.06.03</span>
    <span class="badge badge-phase">04. Planning</span>
    <span class="badge badge-type">Authoring & Governance Guide</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="../../../../templates/en/04_Planning/06_Resource/04_06_03_Resource_Breakdown_Structure_Template.html">📋 Blank Template</a>
    <a class="nav-pill active" href="#">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../../examples/en/04_Planning/06_Resource/04_06_03_Resource_Breakdown_Structure_Example.html">💡 Completed Example</a>
    <a class="nav-pill lang-pill" href="../../../ar/04_التخطيط/06_الموارد/04_06_03_هيكل_تجزئة_الموارد_(RBS)_دليل.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

---
lang: en
layout: default
title: Resource Breakdown Structure
nav_order: 3
---

## Tasleemat Forms Guide
# Project Artifact: Resource Breakdown Structure

**Document Reference:** `PMO-04.06.03`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Resource Breakdown Structure** in alignment with the
Tasleemat framework.

---

### 1. What?
A list of the project's resources arranged as a tree: the project at the top, resource categories beneath it, and individual resources with their quantities below those. It answers the question of what the project needs and in what groupings, without repeating the schedule.

---

### 2. Why?
Because a resource list sorted flat by name cannot be checked against anything. As a tree, a reader can see at once which category is carrying the load, which branch is empty, and where a single resource sits deep enough that it may be split. The tree is also what makes the estimate arguable: a claim that a branch is adequately resourced is checkable against a branch that is not.

---

### 3. When?
Built when activities are being estimated, once enough of the scope is settled to know what the activities are. It is revised whenever scope changes, because resources follow scope: a stable scope gives a stable resource tree, and an evolving one gives a tree that must be re-examined each time scope moves.

---

### 4. Who?
Prepared by whoever estimates the activities, which is usually the team lead, and reviewed by the resource manager who holds the wider picture of what the organisation can supply. The project manager signs it because the tree is the shape of the estimate they are committing to.

---

### Tailoring Tips
*   Decompose the people branch further when the team mixes skill levels, required certifications, or locations. A branch that holds all three together cannot be estimated against anything.
*   Organise by geography instead of by type when the work is spread across sites and the constraint is where people are, not what they do.
*   Keep the numbering contiguous. A gap in the codes reads as a missing node rather than as a deliberate skip, and the reader cannot tell which it was meant to be.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Work Breakdown Structure / WBS (PMO-04.02.06)
    *   Project Schedule (PMO-04.03.08)
*   **Optional / Contextual:**
    *   Resource Capacity Matrix (PMO-00.04)
    *   Cost Management Plan (PMO-04.04.01)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Responsibility Assignment Matrix / RAM (PMO-04.06.04)
    *   Team Charter (PMO-04.06.05)
    *   Team Performance Assessment (PMO-05.06)
*   **Optional / Contextual:**
    *   Team Onboarding Checklist (PMO-05.12)
    *   Training Plan & Log (PMO-04.11.02)

---

### 5. How?
To accurately complete the Resource Breakdown Structure, populate the following sections based on
the project context (ensuring reference to `parameters.md` for the general
project variables):

*   **RBS Code:** The position of the node in the hierarchy, written as 1, 1.1, 1.1.1 so a reader can reconstruct the tree from the text alone. A node numbered 1.2.1 with no 1.2 above it means a level was skipped.
*   **Resource Node:** What the node names. A first-level node is the project, a second-level node is a resource category such as people or equipment, and a third-level node is an individual resource carrying its quantity. A category node with nothing beneath it leaves the branch empty.
*   **Chart Form:** Which view the chart takes: a mindmap for a single hierarchy, or a flowchart where the nodes carry relationships rather than only parentage. Stated so a reader knows what the diagram is meant to show.
*   **Node Labels:** The node labels, one per line, in the same order as the outline. The chart and the outline must agree: a branch present in one and absent from the other is the defect this section exists to prevent.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](../../../../templates/en/04_Planning/06_Resource/04_06_03_Resource_Breakdown_Structure_Template.md)
* **🤖 LLM Generation Prompt**
* **📊 Data Structure (JSON)**
* **📈 Tabular Data (CSV)**

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [04_06_03_Resource_Breakdown_Structure_Example.md](../../../../examples/en/04_Planning/06_Resource/04_06_03_Resource_Breakdown_Structure_Example.md)
