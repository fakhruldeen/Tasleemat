<!--
---
type: Roadmap
---
-->

# 🗺️ Tasleemat Future Strategic Plans & Roadmap

This document outlines the multi-phase evolution of the **Tasleemat (تسليمات)** PMO Operating System beyond version `v2.6.1`. It establishes concrete milestones, architectural objectives, and deliverable specifications to expand management coverage from 114 to 126 standardized bilingual deliverables.

---

## 🌊 Wave 2: Strategic Governance, Portfolio Stage-Gates & Cloud/AI FinOps
**Target Version:** `v2.7.0`  
**Deliverable Expansion:** +4 Deliverables (114 &rarr; 118 Deliverables / 236 Form Bundles)

### Management Scope & Deliverables
1. **`PMO-00.07` — Portfolio Prioritization, Scoring & Investment Matrix (`مصفوفة أولويات المحفظة والتقييم الاستثماري`)**
   - *Phase:* `00` (Program and Portfolio Management)
   - *Purpose:* Quantified project selection framework combining ROI, strategic alignment weights, risk exposure, and resource feasibility into an objective scoring index.
2. **`PMO-00.08` — Executive Stage-Gate Authorization Dossier (`ملف تفويض بوابات المرحلة التنفيذي`)**
   - *Phase:* `00` (Program and Portfolio Management)
   - *Purpose:* Unified executive briefing pack formalizing Gate 0 through Gate 5 transition reviews, capturing sponsor sign-offs, variance allowances, and conditional go/no-go waivers.
3. **`PMO-01.05` — Project Intake & Demand Management Brief (`موجز استيعاب وإدارة الطلب للمشاريع`)**
   - *Phase:* `01` (Business and Value Delivery)
   - *Purpose:* Standardized intake document bridging operational business ideas with formal PMO review prior to Business Case initiation.
4. **`PMO-04.04.05` — Cloud FinOps & AI Compute Capacity Financial Plan (`خطة الإدارة المالية للسحابة وحوسبة الذكاء الاصطناعي FinOps`)**
   - *Phase:* `04.04` (Cost Management)
   - *Purpose:* Dedicated financial planning template for token consumption, GPU provisioning, cloud infrastructure commitments, and cloud unit economics.

---

## 🌊 Wave 3: Enterprise Architecture, NDMO Data Sovereignty & Agentic AI Safety
**Target Version:** `v2.8.0`  
**Deliverable Expansion:** +4 Deliverables (118 &rarr; 122 Deliverables / 244 Form Bundles)

### Management Scope & Deliverables
1. **`PMO-02.07` — AI Red-Teaming, Alignment & Safety Evaluation Report (`تقرير الاختبار الأمني التنافسي وسلامة نماذج الذكاء الاصطناعي`)**
   - *Phase:* `02` (Project Approach and Tailoring)
   - *Purpose:* Systematic safety verification evaluating jailbreak resilience, hallucination rates, toxic output suppression, and adversarial prompt injections.
2. **`PMO-02.08` — Agentic Workflow & Human-in-the-Loop (HITL) Governance Matrix (`مصفوفة حوكمة وكلاء الذكاء الاصطناعي والإشراف البشري`)**
   - *Phase:* `02` (Project Approach and Tailoring)
   - *Purpose:* Operational boundaries, autonomy tiers (autonomous vs. supervised vs. human-confirmed), and failover procedures for agentic coding and automation workflows.
3. **`PMO-04.13.02` — Data Governance, Classification & Sovereign Data Residency Plan (`خطة حوكمة وتصنيف وحصانة البيانات والسيادة الرقمية`)**
   - *Phase:* `04.13` (Security & Governance)
   - *Purpose:* Compliance blueprints aligned with Saudi National Data Management Office (NDMO) policies, personal data protection laws (PDPL), and sovereign cloud hosting regulations.
4. **`PMO-04.14.01` — Architecture Decision Record (ADR) & Tech Debt Register (`سجل قرارات البنية المعمارية والديون التقنية`)**
   - *Phase:* `04.14` (Technical Architecture Management)
   - *Purpose:* Formal ledger documenting structural architecture decisions, trade-offs, rationale, status (proposed/accepted/superseded), and tracked technical debt.

---

## 🌊 Wave 4: Post-Award Procurement, Contract Disputes, BCP & Service Level Operations
**Target Version:** `v2.9.0`  
**Deliverable Expansion:** +4 Deliverables (122 &rarr; 126 Deliverables / 252 Form Bundles)

### Management Scope & Deliverables
1. **`PMO-04.08.08` — Business Continuity, Disaster Recovery & Crisis Management Plan (`خطة استمرارية الأعمال والتعافي من الكوارث وإدارة الأزمات`)**
   - *Phase:* `04.08` (Risk Management)
   - *Purpose:* Recovery Point Objectives (RPO), Recovery Time Objectives (RTO), failover protocols, emergency contact rosters, and operational resilience checklists.
2. **`PMO-04.09.06` — Vendor Bid Evaluation, Scoring & Award Recommendation Report (`تقرير تقييم العروض والترسية والمفاضلة الفنية والمالية`)**
   - *Phase:* `04.09` (Procurement Management)
   - *Purpose:* Rigorous technical and commercial bid comparison matrix, evaluation committee scores, and formal award recommendation justifications.
3. **`PMO-06.17` — Service Level Agreement (SLA) & Operational KPI Scorecard (`بطاقة أداء اتفاقية مستوى الخدمة والمؤشرات التشغيلية SLA`)**
   - *Phase:* `06` (Monitoring and Controlling)
   - *Purpose:* Post-implementation tracking of operational uptime, incident response times, latency SLAs, and contractual vendor performance penalty tracking.
4. **`PMO-06.18` — Contract Variation, Claims & Dispute Resolution Log (`سجل أوامر التغيير التعاقدية والمطالبات وفض النزاعات`)**
   - *Phase:* `06` (Monitoring and Controlling)
   - *Purpose:* Systematic tracking of contractor scope variation requests, financial claims, schedule extensions, and dispute escalation stages.

---

## 🌊 Wave 5: Next-Gen Tooling, Semantic DAG Auditor & Executive Multi-Format Exporter
**Target Version:** `v3.0.0`  
**Focus:** Developer Experience, Deep Inter-Artifact Reasoning, and Production Executive Exporting

### Technical Innovations
1. **Cross-Artifact Semantic DAG Auditor (`tasleemat audit --semantic`)**:
   - Parses inter-deliverable data dependencies across files:
     - Verifies whether milestone dates in `PMO-04.03.04` match milestones in `PMO-03.01` and `PMO-04.03.08`.
     - Validates that total cost estimates in `PMO-04.04.04` reconcile with `PMO-01.01` business case budgets.
     - Confirms risks highlighted in `PMO-06.01` weekly status reports originate from active risks in `PMO-04.08.02`.
   - Generates Mermaid dependency graphs and flags data discrepancies across the project lifecycle.

2. **Native Multi-Format Executive Exporter**:
   - `tasleemat export [artifact_id] --format docx`: Corporate Word deliverable export with institutional typography, RTL Arabic styles, and header document controls.
   - `tasleemat export [artifact_id] --format pdf`: Print-ready vector PDF via headless rendering engine.
   - `tasleemat export [artifact_id] --format xlsx`: Formatted Excel registers with built-in formulas for EVA (`PMO-06.05`), Risk Scoring (`PMO-04.08.02`), and WBS Dictionary (`PMO-04.02.07`).
   - `tasleemat export [artifact_id] --format marp`: Executive slide deck presentation generation for steering committee reporting (`PMO-06.13`).

3. **Autonomous Agent Tool Calling Expansion**:
   - MCP multi-turn workflow sessions with built-in checkpoint rollback.
   - Real-time schema autofix engine capable of automatically formatting and repairing missing JSON schema fields.
