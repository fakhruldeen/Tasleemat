<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Manual</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/docs/en/10_faq_and_troubleshooting.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="../ar/10_faq_and_troubleshooting.html">🇸🇦 الانتقال للنسخة العربية (Arabic Manual) →</a>
  </div>
</div>

</div>

</div>

</div>

<p align="center">
  <img src="../img/logo.png" alt="Tasleemat Logo" width="320" />
</p>

---

# ❓ Frequently Asked Questions & Troubleshooting Guide
**Document ID:** `TASLEEMAT-GUIDE-10-FAQ-TROUBLESHOOTING`  
**Version:** 2.0  
**Target Audience:** Project Managers, PMO Officers, Auditors, System Integrators  

---

## 💡 Top Frequently Asked Questions

### General Architecture & Standards
#### Q1: Do I have to fill out all 102 forms for every project?
**Answer:** Absolutely not. Tasleemat is strictly tailored based on project size and category. Consult [`05_tailoring_profiles.md`](05_tailoring_profiles.md). Tier 3 (Small/Agile) projects only require **12 core deliverables**, whereas Tier 1 (Strategic Enterprise) projects utilize up to 45 forms.

#### Q2: What international standards does Tasleemat align with?
**Answer:** Tasleemat aligns with:
- **PMI PMBOK® Guide:** 6th Edition (Process Groups & Knowledge Areas), 7th Edition (Performance Domains & Principles), and 8th Edition concepts.
- **NIST AI RMF 1.0 & ISO/IEC 42001:** For Artificial Intelligence governance.
- **SDAIA AI Ethics & Saudi PDPL:** For data privacy, ethics, and national regulatory compliance.
- **ISO 21500:** Project, programme, and portfolio management guidance.

#### Q3: How do the Markdown, JSON, and CSV files work together?
**Answer:** 
- The **`*_Template.md`** is the human-readable deliverable to be edited and signed.
- The **`*.json`** contains the schema definition and field constraints for programmatic validation and API integration.
- The **`*.csv`** provides standard table columns for direct import into Excel, Google Sheets, or PowerBI.

---

### Customization & Workflow
#### Q4: Can I modify the tables or add custom fields to a template?
**Answer:** Yes. You may add domain-specific columns or appendices. However, to maintain PMO audit compliance, **do not remove the Document Control & Sign-off table** at the bottom of the template.

#### Q5: Who has the legal/governance authority to sign off on baselines?
**Answer:** Refer to [`06_raci_authority_matrix.md`](06_raci_authority_matrix.md). The Project Manager is **Responsible (Author)**, while the Project Sponsor or Steering Committee is **Accountable (Sign-off Authority)**.

#### Q6: How do we handle project changes during execution?
**Answer:** Any deviation from the approved baseline (Scope, Schedule, Budget) exceeding threshold limits must go through [`PMO-05.03 Change Request`](../forms/en/05_Executing/05_03_Change_Request_Template.md) and be logged in [`PMO-05.04 Change Log`](../forms/en/05_Executing/05_04_Change_Log_Template.md) with formal Change Control Board (CCB) approval.

---

## 🔧 Practical Troubleshooting & Common Pitfalls

### Problem 1: "The project team complains about too much paperwork."
- **Root Cause:** The PM selected Tier 1 (Enterprise) forms for a small Tier 3 initiative.
- **Solution:** Re-run the project sizing assessment in [`05_tailoring_profiles.md`](05_tailoring_profiles.md). Strip out non-mandatory forms immediately. Consolidate status tracking into [`06_01 Project Status Report`](../forms/en/06_Monitoring_and_Controlling/06_01_Project_Status_Report_Template.md).

### Problem 2: "Earned Value Analysis numbers (CPI/SPI) do not match the status report."
- **Root Cause:** Discrepancy between Planned Value (PV) in the cost baseline and Actual Cost (AC) from accounting ledgers.
- **Solution:** Ensure that Earned Value (EV) is calculated strictly against completed WBS work packages as defined in [`PMO-04.02.07 WBS Dictionary`](../forms/en/04_Planning/02_Scope/04_02_07_WBS_Dictionary_Template.md).

### Problem 3: "Our AI model's accuracy dropped in production after deployment."
- **Root Cause:** Data drift or undetected distribution shifts in inference inputs.
- **Solution:** Check [`PMO-02.05 AI Model Card`](../forms/en/02_Project_Approach_and_Tailoring/02_05_AI_Model_Card_and_Fact_Sheet_Template.md) for baseline performance slices. Execute remediation protocols specified in [`PMO-02.02 AI Governance Plan`](../forms/en/02_Project_Approach_and_Tailoring/02_02_AI_Governance_Plan_Template.md).
