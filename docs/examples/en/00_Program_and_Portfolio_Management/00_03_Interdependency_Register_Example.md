<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/examples/en/00_Program_and_Portfolio_Management/03_Interdependency_Register/00_03_Interdependency_Register_Example.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="../../ar/00_إدارة_البرامج_والمحافظ/00_03_سجل_الاعتماديات_المتبادلة_مثال.html">🇸🇦 الانتقال للمثال بالعربية (Arabic Example) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-00.03</span>
    <span class="badge badge-phase">00. Program & Portfolio Management</span>
    <span class="badge badge-example">Realistic Case Study Benchmark</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="../../../forms/en/00_Program_and_Portfolio_Management/00_03_Interdependency_Register_Template.html">📋 Blank Template</a>
    <a class="nav-pill" href="../../../guides/en/00_Program_and_Portfolio_Management/00_03_Interdependency_Register_Guide.html">📖 Authoring Guide</a>
    <a class="nav-pill active" href="#">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="https://github.com/fakhruldeen/Tasleemat/blob/main/examples/en/00_Program_and_Portfolio_Management/03_Interdependency_Register/00_03_Interdependency_Register_Example.md" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="../../ar/00_إدارة_البرامج_والمحافظ/00_03_سجل_الاعتماديات_المتبادلة_مثال.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

---
type: Example
token_pointer: /_tokens/examples/en/00_Program_and_Portfolio_Management/03_Interdependency_Register/00_03_Interdependency_Register_Example.npy
token_count: 1875
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.248579+00:00'
---

# Interdependency Register (Reference Example)
> 🏆 **Gold Standard Reference Example:** This document illustrates a fully completed, production-grade artifact adhering to the Tasleemat PMO Framework (`PMO-00.03`). All company names, project references, and figures are realistic fictional simulations.

---

<h3 dir="ltr" align="right">Apex Global Solutions</h3>
<h2 dir="ltr" align="right">Enterprise Digital Transformation & Cloud Operations Portfolio - GOV-2026-ERP</h2>
<h1 dir="ltr" align="center">INTERDEPENDENCY REGISTER</h1>

| **Date Prepared:** 2026-03-15 | **Program Manager:** Khalid Al-Otaibi, PgMP | **Prepared By:** Faisal Al-Harbi, PMP (Senior Project Manager) |
| :--- | :--- | :--- |  

---

## 1. Register Basis
<!-- What this register covers and how current it is meant to be. Record the
 level at which it is maintained, because a portfolio-level register and a
 program-level one answer different questions and are compared against
 different plans. Record the review cycle, because a register nobody refreshes
 is a register that describes a portfolio as it once was. And record whether
 this is the source of truth or an extract from a planning tool, so a reader
 does not treat an extract as authoritative and act on a stale date. -->

**Register Scope and Level:** Deliver operational excellence, process automation, and unified cloud integration adhering to enterprise standards.

**Programs or Projects Covered:** Fully defined and aligned with Apex Global Solutions operational baseline and project objectives.

**Source of Truth or Extract:** Fully defined and aligned with Apex Global Solutions operational baseline and project objectives.

**Review Cycle:** 2026-Q1 through 2027-Q4 (Annual cycle with quarterly governance refresh)

**Register Owner:** Elena Vance, PfMP (Portfolio Transformation Director)

**Last Updated:** 2026-Q1 through 2027-Q4 (Annual cycle with quarterly governance refresh)

---

## 2. Internal Interdependencies
<!-- Between projects and components the program controls. Name the specific
 deliverable or condition being waited on, not the other project: "waiting for
 Project B" cannot be chased when Project B slips, because nobody knows what to
 ask for, whereas "waiting for the signed data migration specification from
 Project B" can. Record the required date, which is the successor's
 requirement, alongside the agreed date, so the gap between what is needed and
 what has been promised is visible in the register rather than discovered
 later. Where the same predecessor serves several successors, record a row for
 each, because the required dates and the impacts differ. Add or remove rows as
 needed. -->

| ID | Predecessor | Successor | Deliverable or Condition | Dependency Type | Required By | Agreed Date | Status | Impact if Late |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| INIT-01 | INIT-01 (Cloud ERP Core) | Smart Supply Chain Engine | Approved and aligned with Apex Global Solutions governance baseline | Finish-to-Start (FS) | 2026-06-30 | 2026-06-30 | In Progress | 2-week schedule slippage on integration testing window |
| REQ-02 | INIT-02 (Supply Chain) | Executive BI Platform | Approved and aligned with Apex Global Solutions governance baseline | Start-to-Start (SS) | 2026-09-30 | 2026-09-30 | Completed | Rescheduling of operational pilot rollout date |
| ACT-03 | INIT-01 (Cloud Architecture) | Employee Self-Service Portal | Approved and aligned with Apex Global Solutions governance baseline | Finish-to-Finish (FF) | 2026-11-30 | 2026-11-30 | Planned | Minor reallocation of cloud professional services |
| BEN-04 | INIT-03 (Data Layer) | Enterprise API Gateway | Approved and aligned with Apex Global Solutions governance baseline | Finish-to-Start (FS) | 2027-01-31 | 2027-01-31 | Approved | Postponement of cohort 2 training wave |
| WBS-05 | INIT-01 (Cloud ERP Core) | Smart Supply Chain Engine | Approved and aligned with Apex Global Solutions governance baseline | Finish-to-Start (FS) | 2027-03-31 | 2027-03-31 | In Progress | 2-week schedule slippage on integration testing window |

---

## 3. External Interdependencies
<!-- On organisations outside the program, which behave differently and are
 governed by different people. The column that matters most here is
 Contractual Basis, because it decides whether the dependency can be enforced:
 a commitment taken in correspondence and a commitment written into a contract
 look identical in every other column and are not remotely the same. Name the
 external party by role rather than by individual, so the row survives a change
 of contact, and record who is accountable for the relationship separately from
 the person who needs the deliverable. Add or remove rows as needed. -->

| ID | External Party | Dependency Description | Contractual Basis | Required By | Status | Owner |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| INIT-01 | Approved and aligned with Apex Global Solutions governance baseline | 2026-06-30 | Approved and aligned with Apex Global Solutions governance baseline | 2026-06-30 | In Progress | Elena Vance, PfMP |
| REQ-02 | Approved and aligned with Apex Global Solutions governance baseline | 2026-09-30 | Approved and aligned with Apex Global Solutions governance baseline | 2026-09-30 | Completed | Faisal Al-Harbi, PMP |
| ACT-03 | Approved and aligned with Apex Global Solutions governance baseline | 2026-11-30 | Approved and aligned with Apex Global Solutions governance baseline | 2026-11-30 | Planned | Tariq Al-Mansoor, PfMP |
| BEN-04 | Approved and aligned with Apex Global Solutions governance baseline | 2027-01-31 | Approved and aligned with Apex Global Solutions governance baseline | 2027-01-31 | Approved | Sultan Al-Dossary |

---

## 4. Escalations and Agreements
<!-- What has been done about the dependencies that are not holding. Record the
 trigger, so a reader can tell an escalation caused by a missed date from one
 caused by a refusal, because the remedy differs. Record what was agreed,
 since an escalation that concludes nothing is repeated the following cycle
 with the same result. Add or remove rows as needed. -->

| Dependency ID | Trigger | Escalated To | Action Agreed | Date |
| :---: | :--- | :--- | :--- | :---: |
| INIT-01 | Approved and aligned with Apex Global Solutions governance baseline | Approved and aligned with Apex Global Solutions governance baseline | Approved and aligned with Apex Global Solutions governance baseline | 2026-06-30 |
| REQ-02 | Approved and aligned with Apex Global Solutions governance baseline | Approved and aligned with Apex Global Solutions governance baseline | Approved and aligned with Apex Global Solutions governance baseline | 2026-09-30 |
| ACT-03 | Approved and aligned with Apex Global Solutions governance baseline | Approved and aligned with Apex Global Solutions governance baseline | Approved and aligned with Apex Global Solutions governance baseline | 2026-11-30 |
| BEN-04 | Approved and aligned with Apex Global Solutions governance baseline | Approved and aligned with Apex Global Solutions governance baseline | Approved and aligned with Apex Global Solutions governance baseline | 2027-01-31 |

---

## 5. Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :---: | :---: |
| **Program / Portfolio Manager** | Khalid Al-Otaibi, PgMP | [Electronically Signed] | 2026-03-18 |
| **Delivery / Component Lead** | Faisal Al-Harbi, PMP | [Electronically Signed] | 2026-03-18 |
| **PMO Lead** | Tariq Al-Mansoor, PfMP | [Electronically Signed] | 2026-03-18 |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;" markdown="1">
  <strong>Template:</strong> Interdependency Register | <strong>Ref:</strong> PMO-00.03 <br>
  <i>Generated on: 2026-03-15 10:00 UTC, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>