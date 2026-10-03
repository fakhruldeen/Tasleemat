# AI Model Card and Fact Sheet (Reference Example)
> 🏆 **Gold Standard Reference Example:** This document illustrates a fully completed, production-grade artifact adhering to the Tasleemat PMO Framework (`PMO-02.05`). All company names, project references, and figures are realistic fictional simulations.

---

<h3 dir="ltr" align="right">Apex Global Solutions</h3>
<h2 dir="ltr" align="right">Enterprise-Wide Cloud Migration - GOV-FRM-2026-01</h2>
<h1 dir="ltr" align="center">AI MODEL CARD AND FACT SHEET</h1>

| **Date Prepared:** 2026-03-15 | **Compliance Officer:** Abdulaziz Al-Zahrani (Compliance Director) | **Prepared By:** Faisal Al-Harbi, PMP (Senior Project Manager) |
| :--- | :--- | :--- |

---

## 1. Model Identification and Provenance


**Model Name and Version:** Apex Enterprise Cognitive Assistant Engine (AECA Engine v2.4)

**Developer and Provenance:** Apex Global Solutions AI & Data Engineering Squad in partnership with Certified Cloud Partner

**Architecture and Configuration:** Transformer architecture augmented with Vector Retrieval (RAG) and private vector embeddings

**Training Method and Compute:** Supervised Fine-Tuning (SFT) & DPO hosted on secured private cloud GPU clusters (8x H100)

**Licence and Usage Terms:** Proprietary Enterprise Commercial License restricted to Apex Global Solutions internal operations

**Related Artefacts:** Secured Cloud Model Registry Artifacts (v2.4 Production Baseline)

---

## 2. Intended Use and Out-of-Scope Use
<!-- The task as an input and an output, what else it may be used for, what it must not be used for, who operates it and who it acts upon, and the conditions under which its metrics hold. -->

**Primary Use:** Automated procurement purchase order matching, invoice data parsing, and predictive replenishment

**Secondary Use:** Operational synthesis reporting and preliminary compliance audit logs for operations management

**Out-of-Scope Use:** Autonomous HR hiring/termination decisions, customer credit scoring, or unsupervised fund disbursements

**User and Audience:** Operations directors, supply chain analysts, procurement specialists, and financial auditors

**Operating Conditions:** Secured enterprise virtual private cloud (VPC) with latency SLA < 800ms and 99.95% uptime

**Human Oversight Requirement:** Mandatory human-in-the-loop review for all financial transactions exceeding $15,000 USD or model confidence < 90%

---

## 3. Training Data
<!-- One row per dataset: what it is and who owns it, where it came from, whom and where it represents, when it covers, on what basis it may be used, what was done to it, and what it cannot represent. -->

| Dataset | Provenance and Collection | Demographic and Geographic Coverage | Time Period Covered | Licence and Consent Basis | Preprocessing and Filtering | Known Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Historical Purchase Orders & Inventory Logs | Automated database ETL pipeline extraction | Enterprise-wide regional logistics hubs | 2026-Q2 | Proprietary enterprise internal asset | PII de-identification and masking protocols | Restricted to USD and SAR transaction types |
| Vendor Invoices & RFQ Quotation Records | Secure electronic archiving with compliance audit | Central and regional procurement units | 2026-Q3 | Authorized operational telemetry under policy | Deduplication and anomaly detection cleaning | Excludes legacy manual offline paper cash slips |
| User Operational Interaction & Ticket Logs | API ingestion streams with tokenized logging | Tier-1 and Tier-2 commercial vendors | 2026-Q4 | Formal CFO & Compliance authorization sign-off | Standardized ISO datetime and currency normalization | Requires human-in-the-loop review on multi-line POs |

---

## 4. Evaluation and Performance
<!-- One row per metric: what it is measured on, its value with the sample size behind it, the same figure for each affected group, the baseline it beats, the threshold in force, and what the method does not establish. -->

| Metric | Evaluation Data and Disjointness | Value and Sample Size | Performance by Subgroup | Baseline Comparison | Threshold in Force | Method Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model inference accuracy & data reconciliation >= 95% | Isolated test holdout partition (15% dataset) | 94.2% accuracy (Sample Size: 50,000 records) | Approved and aligned with Apex Global Solutions governance baseline | +28% throughput increase over legacy manual flow | Minimum acceptable accuracy >= 90% | Restricted to USD and SAR transaction types |
| Annual recurring operational savings >= $950K USD | Fresh Q1-2026 transaction batch | F1-Score: 0.91 (Sample Size: 25,000 invoices) | Approved and aligned with Apex Global Solutions governance baseline | 65% error reduction compared to legacy baseline | Maximum error tolerance <= 2% | Excludes legacy manual offline paper cash slips |
| Sub-second transaction response latency (< 800ms) | Independent manually annotated validation set | Latency: 620ms (10,000 concurrent requests) | Approved and aligned with Apex Global Solutions governance baseline | +18% speedup over existing ERP workflow | Maximum latency SLA <= 800ms | Requires human-in-the-loop review on multi-line POs |

---

## 5. Ethical, Fairness and Safety Considerations
<!-- One row per consideration: which group is affected, the specific way this model is unfair, the harm it could cause and its severity, how it could be misused, what it can reveal, and its resource cost. -->

| Consideration | Groups Affected | Specific Finding | Severity | What Was Done |
| :--- | :--- | :--- | :--- | :--- |
| INIT-01 | Approved and aligned with Apex Global Solutions governance baseline | Approved and aligned with Apex Global Solutions governance baseline | Medium (Subject to quarterly audit) | Approved and aligned with Apex Global Solutions governance baseline |
| REQ-02 | Approved and aligned with Apex Global Solutions governance baseline | Approved and aligned with Apex Global Solutions governance baseline | Low (Within acceptable operating bounds) | Approved and aligned with Apex Global Solutions governance baseline |
| ACT-03 | Approved and aligned with Apex Global Solutions governance baseline | Approved and aligned with Apex Global Solutions governance baseline | High (Requires mandatory human approval) | Approved and aligned with Apex Global Solutions governance baseline |

---

## 6. Limitations, Monitoring and Change Control


**Known Limitations:** Restricted to digital documents and invoices with minimum 300 DPI resolution in USD and SAR.

**Out-of-Distribution Behaviour:** Automatic safe fallback routing out-of-distribution inputs directly to human verification queues.

**Production Monitoring:** Real-time telemetry tracking inference latency, accuracy rates, and error anomalies via Grafana dashboards.

**Monitoring Thresholds:** Variance threshold of ±5% on CPI or SPI triggers mandatory corrective action plan within 48 hours.

**Retraining and Update Policy:** Quarterly scheduled retraining on curated new operational datasets subject to regression gate verification.

**Version Change Record:** Version 2.4: Enhanced multi-page invoice entity extraction accuracy by 12% and optimized RAG embedding layer.

**Decommissioning Plan:** Maintain previous model release in warm standby for 6 months prior to permanent secure archival.

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Model Developer / ML Lead** | Dr. Rayan Al-Sulaiman (Lead ML Scientist) | [Electronically Signed] | 2026-03-18 |
| **AI Ethics / QA Reviewer** | Approved - QA Reviewer Name | [Electronically Signed] | 2026-03-18 |
| **Product Owner** | Mariam Al-Khatib (Principal Product Owner) | [Electronically Signed] | 2026-03-18 |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> AI MODEL CARD AND FACT SHEET | <strong>Ref:</strong> PMO-02.05 <br>
  <i>Generated on: 2026-03-15 10:00 UTC, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>