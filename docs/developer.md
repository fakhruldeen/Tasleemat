<!--
---
type: Guide
---
-->

<div class="hero-wrapper">
  <div class="hero-tag">
    <span class="pulse-dot"></span> Developer Manual, CLI Scaffolder & Python SDK • OKF Compliant
  </div>
  <h1 class="hero-title">Tasleemat Developer Tooling, Python SDK & Bilingual Lexicon</h1>
  <div class="hero-title-ar">دليل المطورين، أدوات سطر الأوامر (CLI)، وحزمة بايثون، والمعجم الموحد</div>
  <p class="hero-subtitle">
    Programmatic scaffolding, friction-free schema validation, AI agent integration via <code>tasleemat.ai</code>, and standardized bilingual project management terminology.
  </p>
  <div class="hero-actions">
    <span class="inline-flex items-center gap-2 px-3 py-2 bg-slate-900 text-slate-100 font-mono text-xs rounded-lg border border-slate-700 shadow-sm cursor-pointer" onclick="navigator.clipboard.writeText('pip install tasleemat'); alert('Copied: pip install tasleemat');">
      <span class="text-emerald-400">$</span> pip install tasleemat
      <span class="text-[10px] bg-slate-800 text-slate-400 px-1 py-0.5 rounded">📋 Copy</span>
    </span>
    <a href="https://pypi.org/project/tasleemat/" target="_blank" class="btn-secondary">📦 PyPI Release ↗</a>
    <a href="#cli-builder" class="btn-emerald">⚡ Interactive CLI Builder</a>
    <a href="#lexicon" class="btn-secondary">📖 Master Lexicon Glossary</a>
  </div>
</div>

---

<h2 id="installation">📦 1. Installation & Environment Verification</h2>

```bash
# Install the official global package
pip install --upgrade tasleemat

# Verify CLI version and environment readiness
tasleemat --version
tasleemat doctor
```

---

<h2 id="cli-builder">⚡ 2. Interactive CLI Command Generator</h2>

Use the interactive generator below to build customized scaffolding commands:

<div class="tailoring-calculator-card">
  <div class="calc-grid">
    <div class="calc-field">
      <label>Governance Tier:</label>
      <select id="cli-gen-tier" class="calc-select" onchange="updateCLICmd()">
        <option value="1">Tier 1: Micro / Small (5 Artifacts)</option>
        <option value="2" selected>Tier 2: Standard Core (18 Artifacts)</option>
        <option value="3">Tier 3: Enterprise Transformation (45+ Artifacts)</option>
        <option value="4">Tier 4: Agile / AI Iterative (25 Artifacts)</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Package Pack Type:</label>
      <select id="cli-gen-pack" class="calc-select" onchange="updateCLICmd()">
        <option value="standard" selected>Standard Predictive / PMBOK</option>
        <option value="agile">Agile / Scrum / Kanban</option>
        <option value="gov">Saudi Gov / DGA Digital Transformation</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Artifact Language:</label>
      <select id="cli-gen-lang" class="calc-select" onchange="updateCLICmd()">
        <option value="ar" selected>🇸🇦 Arabic Standardized (العربية)</option>
        <option value="en">🇬🇧 English Only</option>
        <option value="both">🌐 Bilingual Synchronized (Both)</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Project Directory Name:</label>
      <input type="text" id="cli-gen-name" class="calc-select" value="منصة_التحول_الرقمي" oninput="updateCLICmd()" />
    </div>
  </div>

  <div class="cli-terminal-window">
    <div class="terminal-header">
      <div class="terminal-dots">
        <span class="terminal-dot dot-red"></span>
        <span class="terminal-dot dot-yellow"></span>
        <span class="terminal-dot dot-green"></span>
      </div>
      <span class="terminal-title">bash — tasleemat cli scaffolder</span>
      <button class="card-btn" style="padding: 2px 8px; font-size: 11px;" onclick="copyLiveCLI()">📋 Copy Command</button>
    </div>
    <div class="terminal-body">
      <div class="flex items-center gap-2">
        <span class="terminal-prompt">$</span>
        <span id="live-cli-display" class="terminal-cmd">tasleemat init --tier 2 --pack standard --lang ar --name "منصة_التحول_الرقمي"</span>
      </div>
      <div class="terminal-output">
        <span class="text-slate-400">[INFO] Initializing Tasleemat project directory structure...</span><br>
        <span class="text-slate-400">[INFO] Generating 18 synchronized artifact bundles in Arabic (RTL)...</span><br>
        <span class="terminal-badge-ok">[OK] Successfully generated project scaffold! Ready for delivery.</span>
      </div>
    </div>
  </div>
</div>

<script>
function updateCLICmd() {
  const tier = document.getElementById("cli-gen-tier").value;
  const pack = document.getElementById("cli-gen-pack").value;
  const lang = document.getElementById("cli-gen-lang").value;
  const name = document.getElementById("cli-gen-name").value || "my_pmo_project";

  const cmd = `tasleemat init --tier ${tier} --pack ${pack} --lang ${lang} --name "${name}"`;
  document.getElementById("live-cli-display").textContent = cmd;
}

function copyLiveCLI() {
  const cmd = document.getElementById("live-cli-display").textContent;
  navigator.clipboard.writeText(cmd);
  alert("Copied to clipboard: " + cmd);
}
</script>

---

<h2 id="python-sdk">🤖 3. Programmatic Python SDK (`tasleemat.ai`)</h2>

Automate document drafting and LLM verification using the Python SDK:

```python
from tasleemat.ai import AIClient

# 1. Initialize client (supports Gemini, OpenAI, Claude, or local mock engines)
client = AIClient(provider="gemini", model="gemini-2.5-flash")

# 2. Automated artifact population using PMI PMBOK principle grounding
charter_md = client.generate_deliverable(
    code="FORM-03-01",
    lang="ar",
    project_context={
        "name": "منصة الحوكمة الرقمية",
        "sponsor": "معالي رئيس الهيئة",
        "budget": "4,500,000 SAR",
        "strategic_goal": "أتمتة مخرجات PMO وتحقيق مستهدفات التحول الرقمي 2030"
    }
)

print(charter_md)
```

---

<h2 id="lexicon">📖 4. Bilingual PMO Terminology Lexicon & Search</h2>

Searchable glossary of core project management terminology aligned with PMI PMBOK® Lexicon and Arab regional standards:

<div class="mb-4">
  <input type="text" id="lex-search-input" class="dash-search-box" placeholder="🔍 ابحث في المعجم (مثال: الخط الأساسي، WBS، EVA، المخاطر)..." oninput="filterLexicon()" />
</div>

<div class="overflow-x-auto">
  <table id="lex-table">
    <thead>
      <tr>
        <th>English Term</th>
        <th>المصطلح العربي المعتمد</th>
        <th>Definition & Context (التعريف والسياق)</th>
        <th>Lifecycle Domain</th>
        <th>PMBOK Reference</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="font-bold">Baseline</td>
        <td class="font-bold text-blue-700">الخط الأساسي</td>
        <td>The approved version of a work product, schedule, or cost envelope that can only be changed through formal change control.</td>
        <td><span class="badge badge-phase">Planning</span></td>
        <td>PMBOK® 6/7/8</td>
      </tr>
      <tr>
        <td class="font-bold">Work Breakdown Structure (WBS)</td>
        <td class="font-bold text-blue-700">هيكل تجزئة العمل</td>
        <td>A hierarchical decomposition of the total scope of work to be carried out by the project team.</td>
        <td><span class="badge badge-phase">Scope (04.02)</span></td>
        <td>ISO 21502 / PMBOK®</td>
      </tr>
      <tr>
        <td class="font-bold">Earned Value Analysis (EVA)</td>
        <td class="font-bold text-blue-700">تحليل القيمة المكتسبة</td>
        <td>Methodology that combines scope, schedule, and resource measurements to assess project performance and progress.</td>
        <td><span class="badge badge-phase">Monitoring (06)</span></td>
        <td>ANSI/EIA-748</td>
      </tr>
      <tr>
        <td class="font-bold">Stage-Gate Review</td>
        <td class="font-bold text-blue-700">مراجعة بوابة المرحلة</td>
        <td>A formal checkpoint at the end of a phase where a decision is made to continue, conditionally proceed, or terminate.</td>
        <td><span class="badge badge-phase">Governance (00-07)</span></td>
        <td>PMI Standard</td>
      </tr>
      <tr>
        <td class="font-bold">Deliverable</td>
        <td class="font-bold text-blue-700">المُسلَّم / التسليمة القياسية</td>
        <td>Any unique and verifiable product, result, or capability to perform a service that is required to be produced to complete a phase.</td>
        <td><span class="badge badge-phase">All Lifecycle</span></td>
        <td>OKF / PMBOK®</td>
      </tr>
      <tr>
        <td class="font-bold">Stakeholder Engagement</td>
        <td class="font-bold text-blue-700">إشراك أصحاب المصلحة</td>
        <td>Strategies and actions to involve individuals and groups in project decisions and execution based on interests and influence.</td>
        <td><span class="badge badge-phase">Initiating (03)</span></td>
        <td>PMBOK® Principle 3</td>
      </tr>
      <tr>
        <td class="font-bold">Risk Appetite</td>
        <td class="font-bold text-blue-700">القابلية للمخاطر</td>
        <td>The degree of uncertainty an organization or individual is willing to accept in anticipation of a reward.</td>
        <td><span class="badge badge-phase">Risk (04.08)</span></td>
        <td>ISO 31000</td>
      </tr>
      <tr>
        <td class="font-bold">Contingency Reserve</td>
        <td class="font-bold text-blue-700">احتياطي الطوارئ</td>
        <td>Time or budget allocated within the cost baseline for known-unknown risks managed by the Project Manager.</td>
        <td><span class="badge badge-phase">Cost (04.04)</span></td>
        <td>PMBOK® 6th/7th</td>
      </tr>
    </tbody>
  </table>
</div>

<script>
function filterLexicon() {
  const query = document.getElementById("lex-search-input").value.toLowerCase();
  const rows = document.querySelectorAll("#lex-table tbody tr");
  rows.forEach(r => {
    const text = r.textContent.toLowerCase();
    r.style.display = text.includes(query) ? "" : "none";
  });
}
</script>

---

<h2 id="citation">📚 5. Academic Citation & Zenodo DOI</h2>

If you utilize the Tasleemat framework or dataset in enterprise research, audit manuals, or academia, please cite:

<div class="dash-card">
  <div class="flex items-center justify-between mb-3">
    <div class="flex items-center gap-2">
      <span class="badge badge-code">DOI: 10.5281/zenodo.23193523</span>
      <span class="badge" style="background:#f0fdf4;color:#166534;">Open Access • MIT License</span>
    </div>
    <div class="flex gap-2">
      <button class="card-btn" onclick="copyBibTeX()">📋 Copy BibTeX</button>
      <button class="card-btn" onclick="copyAPA()">📋 Copy APA</button>
    </div>
  </div>
  <pre class="bg-slate-900 text-slate-100 p-4 rounded-lg text-xs font-mono overflow-x-auto"><code id="bibtex-code">@software{fakhruldeen_tasleemat_2026,
  author       = {Fakhruldeen, Mohamed (Fouad)},
  title        = {Tasleemat: The Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Governance Framework},
  year         = {2026},
  version      = {v2.0.2},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23193523},
  url          = {https://doi.org/10.5281/zenodo.23193523}
}</code></pre>
</div>

<script>
function copyBibTeX() {
  const code = document.getElementById("bibtex-code").textContent;
  navigator.clipboard.writeText(code);
  alert("BibTeX citation copied to clipboard!");
}
function copyAPA() {
  const apa = "Fakhruldeen, M. (F.). (2026). Tasleemat: The Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Governance Framework (Version v2.0.2) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23193523";
  navigator.clipboard.writeText(apa);
  alert("APA citation copied to clipboard!");
}
</script>
