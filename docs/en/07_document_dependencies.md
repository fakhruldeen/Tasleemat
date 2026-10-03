<p align="center">
  <img src="docs/img/logo.png" alt="Tasleemat PMO Toolkit Logo" width="280">
</p>

# 🔗 Tasleemat Document Dependencies & Lifecycle Architecture
**Document Reference:** `TASLEEMAT-DOC-DEPENDENCIES-v2.0`  
**Standard:** PMI PMBOK® 6th, 7th & 8th Edition Standard  

---

## 🎯 Executive Overview

In the **Tasleemat PMO Operating System**, no document exists in isolation. Every form and artifact functions as a node in a connected **Directed Acyclic Graph (DAG)** of project inputs, baselines, operational logs, monitoring reports, and closeout assets.

```mermaid
flowchart TD
    subgraph G0["Gate 0: Strategic Alignment & Concept"]
        G0_1["PMO-00.06 OKR Alignment"] --> G0_2["PMO-01.01 Business Case"]
        G0_2 --> G0_3["PMO-01.02 Feasibility Study"]
        G0_2 --> G0_4["PMO-01.03 Benefits Realization"]
        G0_2 --> G0_5["PMO-00.01 Portfolio Roadmap"]
    end

    subgraph G1["Gate 1: Initiation & Authorization"]
        G0_2 --> G1_1["PMO-03.01 Project Charter"]
        G1_1 --> G1_2["PMO-03.03 Assumption Log"]
        G1_1 --> G1_3["PMO-03.04 Stakeholder Register"]
        G1_3 --> G1_4["PMO-03.05 Stakeholder Analysis"]
    end

    subgraph G2["Gate 2: Integrated Baseline Sign-off"]
        G1_1 --> G2_PMP["PMO-04.01.01 Project Mgmt Plan"]
        G2_PMP --> G2_SC["PMO-04.02.05 Scope Statement"]
        G2_SC --> G2_WBS["PMO-04.02.06 WBS & Dictionary"]
        G2_WBS --> G2_SCH["PMO-04.03.07 Schedule Baseline"]
        G2_WBS --> G2_CST["PMO-04.04.04 Cost Baseline"]
        G1_2 --> G2_RSK["PMO-04.08.02 Risk Register"]
        G2_PMP --> G2_RACI["PMO-04.06.04 RACI Matrix"]
    end

    subgraph G3["Gate 3: Execution & Control"]
        G2_PMP --> G3_ISS["PMO-05.01 Issue Log"]
        G2_PMP --> G3_DEC["PMO-05.02 Decision Log"]
        G3_ISS --> G3_CR["PMO-05.03 Change Request"]
        G3_CR --> G3_CHG["PMO-05.04 Change Log"]
        G2_SCH --> G3_EVM["PMO-06.05 Earned Value (EVM)"]
        G2_CST --> G3_EVM
        G3_EVM --> G3_PSR["PMO-06.01 Status Report"]
    end

    subgraph G4["Gate 4: Handover & Acceptance"]
        G2_WBS --> G4_UAT["PMO-06.10 UAT Sign-off"]
        G4_UAT --> G4_DEL["PMO-06.08 Deliverable Acceptance"]
        G4_DEL --> G4_OPS["PMO-07.04 Transition to Ops"]
    end

    subgraph G5["Gate 5: Closeout & Realization"]
        G4_OPS --> G5_CL["PMO-07.03 Project Closeout"]
        G3_ISS --> G5_LL["PMO-07.01 Lessons Learned"]
        G2_RSK --> G5_LL
        G5_CL --> G5_BEN["PMO-07.05 Post Implementation Review"]
        G0_4 --> G5_BEN
    end
```

---

## 📋 Comprehensive Dependency Index (Across All 102 Forms)

| Ref ID | Form Name | Primary Stage / Gate | Direct Predecessors (Inputs) | Direct Successors (Outputs) |
| :--- | :--- | :--- | :--- | :--- |
| **`PMO-00.01`** | Portfolio Roadmap | Gate 0: Strategy & Portfolio Alignment | `PMO-00.06 OKR Alignment`, `PMO-01.01 Business Case` | `PMO-00.02 Program Charter`, `PMO-03.01 Project Charter`, `PMO-00.04 Capacity Matrix` |
| **`PMO-00.02`** | Program Charter | Gate 0: Strategy & Portfolio Alignment | `PMO-00.01 Portfolio Roadmap`, `PMO-01.01 Business Case` | `PMO-00.03 Interdependency Register`, `PMO-03.01 Project Charter` |
| **`PMO-00.03`** | Interdependency Register | Continuous Governance across Program Lifecycle | `PMO-00.02 Program Charter`, `PMO-04.03.08 Project Schedule` | `PMO-04.08.02 Risk Register`, `PMO-06.01 Project Status Report` |
| **`PMO-00.04`** | Resource Capacity Matrix | Gate 0 & Continuous Portfolio Planning | `PMO-00.01 Portfolio Roadmap`, `PMO-04.06.02 Resource Requirements` | `PMO-04.06.01 Resource Management Plan`, `PMO-04.03.08 Project Schedule` |
| **`PMO-00.05`** | PMO Maturity Assessment | Annual / Semi-Annual PMO Strategic Review | `Organizational Strategic Mandate` | `PMO-02.01 Tailoring Framework`, `PMO Policy Manual` |
| **`PMO-00.06`** | OKR Alignment Matrix | Gate 0: Strategic Alignment | `Enterprise Strategic Goals / Vision 2030` | `PMO-00.01 Portfolio Roadmap`, `PMO-01.01 Business Case` |
| **`PMO-01.01`** | Business Case | Gate 0: Justification & Funding | `PMO-00.06 OKR Alignment`, `PMO-01.04 Value Proposition` | `PMO-01.02 Feasibility Study`, `PMO-01.03 Benefits Realization`, `PMO-03.01 Project Charter` |
| **`PMO-01.02`** | Feasibility Study | Gate 0: Justification & Funding | `PMO-01.01 Business Case` | `PMO-03.01 Project Charter` |
| **`PMO-01.03`** | Benefits Realization Plan | Gate 0 through Gate 5 (Lifecycle Long) | `PMO-01.01 Business Case` | `PMO-07.05 Post Implementation Review` |
| **`PMO-01.04`** | Value Proposition Canvas | Gate 0: Product & Service Definition | `Market Research / User Need Analysis` | `PMO-01.01 Business Case`, `PMO-03.02 Product Vision` |
| **`PMO-02.01`** | Development Approach Assessment | Gate 1: Initiation | `PMO-01.01 Business Case`, `PMO-02.02 Complexity Model` | `PMO-03.01 Project Charter`, `PMO-04.01.01 Project Management Plan` |
| **`PMO-02.02`** | Complexity Assessment Model | Gate 1: Initiation & Tier Sizing | `PMO-01.01 Business Case` | `PMO-02.01 Development Approach`, `Project Sizing Tier Assignment` |
| **`PMO-02.03`** | AI Ethics and Governance Checklist | Gate 1 & Continuous AI Verification | `PMO-02.04 AI Use Case Canvas` | `PMO-04.08.02 Risk Register (AI Ethical Risks)` |
| **`PMO-02.04`** | AI Canvas and Use Case Card | Gate 0 / Gate 1: AI Scoping | `PMO-01.01 Business Case` | `PMO-02.03 AI Ethics Checklist`, `PMO-03.01 Project Charter` |
| **`PMO-02.05`** | Governance and Compliance Matrix | Gate 1 & Gate 2: Planning Baseline | `PMO-03.01 Project Charter` | `PMO-04.05.01 Quality Plan`, `PMO-06.07 Procurement/Compliance Audit` |
| **`PMO-03.01`** | Project Charter | Gate 1: Project Authorization | `PMO-01.01 Business Case`, `PMO-02.01 Development Approach` | `PMO-03.03 Assumption Log`, `PMO-03.04 Stakeholder Register`, `PMO-04.01.01 Project Management Plan` |
| **`PMO-03.02`** | Product Vision | Gate 1: Agile / Product Initiation | `PMO-01.04 Value Proposition Canvas` | `PMO-04.02.08 Product Backlog`, `PMO-04.02.09 Story Mapping` |
| **`PMO-03.03`** | Assumption Log | Gate 1 & Continuous Planning | `PMO-03.01 Project Charter`, `PMO-01.01 Business Case` | `PMO-04.08.02 Risk Register`, `PMO-04.02.05 Project Scope Statement` |
| **`PMO-03.04`** | Stakeholder Register | Gate 1 & Continuous Stakeholder Mgmt | `PMO-03.01 Project Charter` | `PMO-03.05 Stakeholder Analysis`, `PMO-04.10.01 Stakeholder Plan`, `PMO-04.07.01 Communications Plan` |
| **`PMO-03.05`** | Stakeholder Analysis | Gate 1 & Gate 2: Planning | `PMO-03.04 Stakeholder Register` | `PMO-04.10.01 Stakeholder Engagement Plan` |

---
*Note: For the remaining standard domain plans (Communications, Procurement, Quality, Risk, ESG), each plan depends directly on `PMO-04.01.01 Project Management Plan` and `PMO-03.01 Project Charter`, and produces operational logs in Phase 05/06.*
