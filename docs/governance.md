<!--
---
type: Guide
---
-->

<div class="hero-wrapper">
  <div class="hero-tag">
    <span class="pulse-dot"></span> Stage-Gate Governance & Tailoring Architecture • PMI PMBOK® 6/7/8 & ISO 21500
  </div>
  <h1 class="hero-title">Tasleemat Stage-Gate Governance & Tailoring Profiles</h1>
  <div class="hero-title-ar">منظومة بوابات العبور الحوكمية ومستويات تخصيص المشاريع</div>
  <p class="hero-subtitle">
    Structured gatekeeper decision checkpoints (Gate 0 Idea to Gate 5 Closeout) paired with 4 scalable project sizing tiers to ensure auditability, rigorous fiscal control, and zero governance bloat.
  </p>
  <div class="hero-actions">
    <a href="#six-gates" class="btn-primary">🚪 Inspect 6 Stage-Gates</a>
    <a href="#tailoring-matrix" class="btn-secondary">⚖️ Tailoring Tiers Matrix</a>
    <a href="#calculator" class="btn-emerald">🧮 Launch Sizing Calculator</a>
  </div>
</div>

---

<h2 id="executive-framework">🏛️ 1. Executive Governance Framework</h2>

Every project passing through Tasleemat undergoes rigorous stage-gate governance. Each gate represents a formal review where a designated governing authority evaluates deliverables and decides between **Three Gate Outcomes**:

1. 🟢 **Proceed (Go):** Deliverables satisfy exit criteria. Authorized to release subsequent tranche and advance to the next lifecycle phase.
2. 🟡 **Conditional Approval (Go with Actions):** Minor non-critical deficiencies noted. Conditional approval granted subject to remedial actions completed within 14 calendar days.
3. 🔴 **Reject / Terminate (No-Go):** Critical variance or strategic misalignment. Project is halted, redirected for baseline replanning, or formally closed.

```mermaid
flowchart LR
    G0["<b>Gate 0</b><br/>Concept Review"] -->|Approved| G1["<b>Gate 1</b><br/>Charter & Auth"]
    G1 -->|Approved| G2["<b>Gate 2</b><br/>Baseline Approval"]
    G2 -->|Approved| G3["<b>Gate 3</b><br/>Execution Health"]
    G3 -->|Approved| G4["<b>Gate 4</b><br/>Operational UAT"]
    G4 -->|Approved| G5["<b>Gate 5</b><br/>Final Closeout"]
    
    style G0 fill:#f0fdf4,stroke:#10b981,stroke-width:2px
    style G1 fill:#eff6ff,stroke:#2563eb,stroke-width:2px
    style G2 fill:#eff6ff,stroke:#2563eb,stroke-width:2px
    style G3 fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style G4 fill:#f0fdf4,stroke:#10b981,stroke-width:2px
    style G5 fill:#f8fafc,stroke:#0b132b,stroke-width:2px
```

---

<h2 id="six-gates">🚪 2. Interactive 6 Stage-Gates Visual Inspector</h2>

<div class="space-y-6">

  <!-- Gate 0 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 0: Strategic Concept & Portfolio Alignment</span>
      <span class="badge badge-code">Phase 00 & 01</span>
      <span class="badge" style="background:#f0fdf4;color:#166534;">Authority: Investment Review Board / CFO</span>
    </div>
    <h3 class="dash-card-title">بوابة 0: دراسة الفكرة والمواءمة الاستراتيجية</h3>
    <p class="dash-card-desc">
      Validates strategic alignment, OKR linkage, high-level feasibility, and preliminary ROI before allocating capital or assigning project teams.
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Initiative directly aligns with corporate OKRs or Vision 2030 strategic objectives.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Business Case contains quantified cost of inaction and preliminary NPV/IRR analysis.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Initial feasibility study verifies technical and legal compliance.</span></label>
    </div>
    <div class="dash-card-actions">
      <span class="badge badge-code">FORM-00-06: OKR Alignment</span>
      <span class="badge badge-code">FORM-01-01: Business Case</span>
      <span class="badge badge-code">FORM-01-02: Feasibility Study</span>
    </div>
  </div>

  <!-- Gate 1 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 1: Project Charter & Authorization</span>
      <span class="badge badge-code">Phase 02 & 03</span>
      <span class="badge" style="background:#eff6ff;color:#1e3a8a;">Authority: Executive Sponsor & PMO Director</span>
    </div>
    <h3 class="dash-card-title">بوابة 1: ميثاق المشروع والترخيص الرسمي</h3>
    <p class="dash-card-desc">
      Formally authorizes project existence, assigns the Project Manager, establishes high-level scope boundaries, and defines the initial budget envelope.
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Signed Project Charter by Executive Sponsor and PMO Director.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Governance tier selected (Tier 1-4) with tailored deliverable bundle.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Initial stakeholder register and assumption log established.</span></label>
    </div>
    <div class="dash-card-actions">
      <a href="forms/ar/form-viewer.html" class="card-btn" style="background:#0d9488;color:#fff!important;">🎯 معاينة تفاعلية (FORM-03-01)</a>
      <span class="badge badge-code">FORM-03-01: Project Charter</span>
      <span class="badge badge-code">FORM-03-04: Stakeholder Register</span>
      <span class="badge badge-code">FORM-02-01: Tailoring Plan</span>
    </div>
  </div>

  <!-- Gate 2 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 2: Integrated Baselines Approval</span>
      <span class="badge badge-code">Phase 04</span>
      <span class="badge" style="background:#eff6ff;color:#1e3a8a;">Authority: PMO Steering Committee</span>
    </div>
    <h3 class="dash-card-title">بوابة 2: اعتماد خطوط الأساس المتكاملة</h3>
    <p class="dash-card-desc">
      Rigorous lock-in of Scope Baseline (WBS), Critical Path Schedule, Cost Baseline, and Risk Response Plans before major expenditure.
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>100% WBS Work Package coverage matching agreed scope dictionary.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Cost baseline includes validated contingency and management reserves.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Risk Register contains proactive response plans for all High/Critical risks.</span></label>
    </div>
    <div class="dash-card-actions">
      <span class="badge badge-code">FORM-04-03: Scope & WBS</span>
      <span class="badge badge-code">FORM-04-12: Schedule Baseline</span>
      <span class="badge badge-code">FORM-04-15: Cost Baseline</span>
      <span class="badge badge-code">FORM-04-18: Risk Register</span>
    </div>
  </div>

  <!-- Gate 3 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 3: Execution Mid-Stage Health Check</span>
      <span class="badge badge-code">Phase 05 & 06</span>
      <span class="badge" style="background:#fef3c7;color:#92400e;">Authority: PMO Performance Board</span>
    </div>
    <h3 class="dash-card-title">بوابة 3: مراقبة الأداء وتحليل القيمة المكتسبة</h3>
    <p class="dash-card-desc">
      Continuous monitoring using Earned Value Analysis (EVA): verifies Cost Performance Index (CPI >= 0.95) and Schedule Performance Index (SPI >= 0.95).
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>SPI and CPI within acceptable control thresholds (>= 0.95).</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>All major issues have assigned owners and active remediation dates.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Change requests vetted through formal Change Control Board (CCB).</span></label>
    </div>
    <div class="dash-card-actions">
      <span class="badge badge-code">FORM-06-03: Earned Value Report</span>
      <span class="badge badge-code">FORM-05-03: Issue Log</span>
      <span class="badge badge-code">FORM-05-04: Change Request</span>
    </div>
  </div>

  <!-- Gate 4 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 4: Operational Handover & UAT</span>
      <span class="badge badge-code">Phase 06 & 07</span>
      <span class="badge" style="background:#f0fdf4;color:#166534;">Authority: Operations Director & End-User Sponsor</span>
    </div>
    <h3 class="dash-card-title">بوابة 4: القبول والتسليم التشغيلي</h3>
    <p class="dash-card-desc">
      Formal transition of project deliverables into business-as-usual (BAU) operations, warranty signoffs, and training sign-off.
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>100% user acceptance testing (UAT) test cases verified and signed off.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Operational handover protocols and SLA agreements executed.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Operations team fully trained with operational manuals delivered.</span></label>
    </div>
    <div class="dash-card-actions">
      <span class="badge badge-code">FORM-06-05: Quality Acceptance</span>
      <span class="badge badge-code">FORM-07-02: Operational Handover</span>
    </div>
  </div>

  <!-- Gate 5 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 5: Contract Closeout & Value Realization</span>
      <span class="badge badge-code">Phase 07</span>
      <span class="badge" style="background:#f8fafc;color:#0b132b;">Authority: Executive Sponsor & Audit Committee</span>
    </div>
    <h3 class="dash-card-title">بوابة 5: الإغلاق النهائي وتقييم الفوائد</h3>
    <p class="dash-card-desc">
      Final contract reconciliation, vendor evaluations, lessons learned archive, and post-implementation review (PIR) schedule.
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>All procurement contracts closed with final settlements executed.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Comprehensive Lessons Learned Register archived in organizational repository.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Post-Implementation Review (PIR) calendar established with Value Lead.</span></label>
    </div>
    <div class="dash-card-actions">
      <span class="badge badge-code">FORM-07-01: Lessons Learned</span>
      <span class="badge badge-code">FORM-07-03: Contract Closeout</span>
      <span class="badge badge-code">FORM-07-05: Post-Implementation Review</span>
    </div>
  </div>

</div>

---

<h2 id="tailoring-matrix">⚖️ 3. Tailoring Profiles Matrix (4 Project Sizing Tiers)</h2>

| Tier | Project Profile | Artifact Bundle | Governance Cadence | Required Approvals |
| :--- | :--- | :---: | :--- | :--- |
| **Tier 1: Micro / Small** | Budget < $100K, Duration < 3 mo, Low Risk | **5 Core Artifacts** | Bi-weekly flash report | Project Sponsor only |
| **Tier 2: Standard Core** | Budget $100K–$1M, 3–12 mo, Medium Risk | **18 Artifacts** | Monthly PMO review | Sponsor & PMO Lead |
| **Tier 3: Enterprise Transformation** | Budget > $1M, Multi-vendor, High Impact | **45+ Artifacts** | Formal Steering Committee | Sponsor, PMO, CFO, SteerCo |
| **Tier 4: Agile / AI Iterative** | Machine learning, SaaS, Fast sprints | **25 Artifacts** | Sprint review & Model audit | Product Owner & AI Ethics Lead |

---

<h2 id="calculator">🧮 4. Interactive Project Tailoring Calculator</h2>

<div class="tailoring-calculator-card">
  <div class="calc-grid">
    <div class="calc-field">
      <label>Project Budget Envelope:</label>
      <select id="calc-budget" class="calc-select" onchange="runTailoringCalc()">
        <option value="1">Small (Under $100K / 400K SAR)</option>
        <option value="2" selected>Medium ($100K – $1M / 400K - 4M SAR)</option>
        <option value="3">Enterprise (Over $1M / 4M+ SAR)</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Estimated Project Duration:</label>
      <select id="calc-duration" class="calc-select" onchange="runTailoringCalc()">
        <option value="1">Under 3 Months</option>
        <option value="2" selected>3 to 12 Months</option>
        <option value="3">Over 1 Year (Multi-Year)</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Delivery Methodology:</label>
      <select id="calc-method" class="calc-select" onchange="runTailoringCalc()">
        <option value="predictive" selected>Traditional / Predictive (Waterfall)</option>
        <option value="agile">Agile / Scrum / Kanban</option>
        <option value="ai">AI / Machine Learning / Data Science</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Regulatory & Compliance Level:</label>
      <select id="calc-reg" class="calc-select" onchange="runTailoringCalc()">
        <option value="standard" selected>Standard Enterprise Compliance</option>
        <option value="high">High Regulatory (Gov / Financial / DGA)</option>
      </select>
    </div>
  </div>

  <div id="calc-result" class="calc-result-box">
    <div>
      <div class="text-xs text-emerald-800 font-bold uppercase tracking-wider">Recommended Governance Profile:</div>
      <div id="calc-tier-title" class="text-lg font-bold text-emerald-950 mt-1">Tier 2: Standard Core Pack (18 Artifacts)</div>
      <div id="calc-tier-desc" class="text-xs text-emerald-800 mt-1">Full Baselines (Scope, Schedule, Cost, Risk, Communications) with formal stage-gate approval at Gates 1, 2, and 4.</div>
    </div>
    <div>
      <span id="calc-cli-btn" class="inline-flex items-center gap-2 px-3 py-2 bg-slate-900 text-slate-100 font-mono text-xs rounded-lg border border-slate-700 shadow-sm cursor-pointer" onclick="copyCalcCLI()">
        <span class="text-emerald-400">$</span> <span id="calc-cli-cmd">tasleemat init --tier 2 --pack standard --lang both</span>
        <span class="text-[10px] bg-slate-800 text-slate-400 px-1 py-0.5 rounded">📋 Copy</span>
      </span>
    </div>
  </div>
</div>

<script>
function runTailoringCalc() {
  const budget = parseInt(document.getElementById("calc-budget").value);
  const duration = parseInt(document.getElementById("calc-duration").value);
  const method = document.getElementById("calc-method").value;
  const reg = document.getElementById("calc-reg").value;

  let tier = 2;
  let pack = "standard";
  let title = "Tier 2: Standard Core Pack (18 Artifacts)";
  let desc = "Full Baselines (Scope, Schedule, Cost, Risk, Communications) with formal stage-gate approval at Gates 1, 2, and 4.";

  if (method === "ai") {
    tier = 4;
    pack = "ai";
    title = "Tier 4: AI & Machine Learning Governance (25 Artifacts)";
    desc = "AI Canvas, Model Cards, Bias Assessment, NIST AI RMF compliance, and iterative MLOps monitoring.";
  } else if (method === "agile" && budget < 3) {
    tier = 4;
    pack = "agile";
    title = "Tier 4: Agile / Lean Iterative Pack (25 Artifacts)";
    desc = "Sprint Backlog, Retrospectives, Flow Metrics, Product Vision, and Definition of Done checklists.";
  } else if (budget === 3 || reg === "high") {
    tier = 3;
    pack = "enterprise";
    title = "Tier 3: Enterprise Transformation Pack (45+ Artifacts)";
    desc = "Full institutional governance: Multi-vendor procurement, ESG compliance, steering committee signoffs, and independent audit trails.";
  } else if (budget === 1 && duration === 1) {
    tier = 1;
    pack = "lean";
    title = "Tier 1: Micro / Small Fast-Track (5 Core Artifacts)";
    desc = "Charter, Action Log, Milestones Schedule, Status Report, and Operational Closeout.";
  }

  document.getElementById("calc-tier-title").textContent = title;
  document.getElementById("calc-tier-desc").textContent = desc;
  document.getElementById("calc-cli-cmd").textContent = `tasleemat init --tier ${tier} --pack ${pack} --lang both`;
}

function copyCalcCLI() {
  const cmd = document.getElementById("calc-cli-cmd").textContent;
  navigator.clipboard.writeText(cmd);
  alert("Copied to clipboard: " + cmd);
}
</script>
