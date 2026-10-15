"""tools/site_builder/pages_dev/sdk.py
Comprehensive Python SDK Reference, API Signatures, Tutorials & Production Recipes (English & Arabic).
"""

from tools.site_builder.theme import render_html_page
from tools.site_builder.pages_dev.nav import render_dev_subnav


def generate_dev_sdk_en(base_url: str = "/Tasleemat") -> str:
    subnav = render_dev_subnav("sdk", "en", base_url)
    
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/">Home</a> &gt; 
          <a href="{base_url}/developers/">Developers &amp; AI</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">Python SDK</span>
        </nav>
        <div class="hero-pill"><span>🐍 Pure Python Library</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">Python SDK &amp; API Reference</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto;">
          The authoritative Python API reference for programmatic catalog discovery, project tailoring, Draft 2020-12 schema validation, and headless deliverable compilation.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Section 1: Architectural Foundation -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">1. Architectural Foundation &amp; Zero-Dependency Design</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          The <code>tasleemat</code> Python library is built with a strict <strong>zero-external-dependency</strong> philosophy. 
          It relies exclusively on Python standard library modules (<code>json</code>, <code>pathlib</code>, <code>dataclasses</code>, <code>hashlib</code>, <code>re</code>, <code>csv</code>), 
          ensuring instant installation, zero dependency conflicts, and guaranteed execution in ultra-secure, air-gapped container runtimes.
        </p>
        <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1.25rem; border-radius: 0.5rem;">
          <div style="font-weight: 700; font-size: 0.9rem; margin-bottom: 0.5rem; color: var(--accent-blue);">Core Guarantees:</div>
          <ul style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7; margin: 0; padding-left: 1.25rem;">
            <li><strong>Thread-Safe In-Memory Caching:</strong> Catalog indexing and schema parsing are memoized on first load for microsecond retrieval times.</li>
            <li><strong>Source Immutability Protection:</strong> Internal filesystem resolvers block any write or modification operations targeting package data.</li>
            <li><strong>Cross-Platform Compatibility:</strong> Native POSIX and Windows filesystem support with UTF-8 encoding normalization.</li>
          </ul>
        </div>
      </div>

      <!-- Section 2: Detailed 9 API Functions -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text-main);">2. The 9 Verified Core API Functions</h2>

        <!-- Function 1 -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.5rem;">
            <code>tasleemat.list_artifacts(phase=None, tier=None, pack=None)</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Discovers deliverable metadata objects across the entire catalog or filtered by lifecycle phase, sizing tier, or methodology pack.
          </p>
          <pre><code>import tasleemat

# List all 114 deliverables
all_artifacts = tasleemat.list_artifacts()
print(f"Total deliverables: {{len(all_artifacts)}}")

# Discover deliverables for Phase 03 (Initiating) in Tier 2
phase_artifacts = tasleemat.list_artifacts(phase="03", tier=2)
for art in phase_artifacts:
    print(f"- [{{art.artifact_id}}] {{art.name_en}} / {{art.name_ar}}")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 2 -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">
            <code>tasleemat.get_artifact_definition(artifact_id: str) -&gt; dict</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Retrieves the canonical metadata dictionary for a specific deliverable code, including English/Arabic names, phase code, and supported tiers.
          </p>
          <pre><code>meta = tasleemat.get_artifact_definition("PMO-03.01")
print(f"Name (EN): {{meta['name_en']}}")
print(f"Name (AR): {{meta['name_ar']}}")
print(f"Allocated Tiers: {{meta['tiers']}}")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 3 & 4 -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-amber); margin-bottom: 0.5rem;">
            <code>tasleemat.get_artifact_assets(artifact_id: str, lang='en') -&gt; ArtifactAssets</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Returns a secure wrapper object providing access to the 5 companion files: template, guide, example, schema, and dictionary.
          </p>
          <pre><code>assets = tasleemat.get_artifact_assets("PMO-03.01", lang="ar")

# Direct content accessors
template_text = assets.get_template_content()
guide_text = assets.get_guide_content()
example_text = assets.get_example_content()
schema_dict = assets.get_schema_data()
dict_rows = assets.get_dictionary_rows()

# Or fetch directly by role string:
schema_raw = tasleemat.get_artifact_asset("PMO-03.01", role="schema", lang="en")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 5 -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: #8b5cf6; margin-bottom: 0.5rem;">
            <code>tasleemat.get_tailoring_profile(tier: Union[int, str], pack: str='general') -&gt; List[str]</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Computes the exact deterministic list of required deliverable codes matching a governance tier and delivery pack.
          </p>
          <pre><code># Resolve required deliverables for Tier 2 Agile Project
deliverable_ids = tasleemat.get_tailoring_profile(tier=2, pack="agile")
print(f"Allocated {{len(deliverable_ids)}} deliverables: {{deliverable_ids[:5]}}...")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 6 -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: #ec4899; margin-bottom: 0.5rem;">
            <code>tasleemat.validate_artifact_data(artifact_id: str, data: dict, mode='strict') -&gt; ValidationReport</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Executes pure-Python Draft 2020-12 schema validation on incoming JSON data payloads. Supports <code>strict</code> and <code>draft</code> modes.
          </p>
          <pre><code>payload = {{
    "project_id": "PRJ-2026-CLOUD",
    "project_name": "Cloud Transformation Platform",
    "sponsor": "Executive VP Operations",
    "project_manager": "Sarah Al-Ahmad",
    "authorization_date": "2026-10-15"
}}

report = tasleemat.validate_artifact_data("PMO-03.01", payload, mode="strict")
if report.valid:
    print("Payload conforms 100% to Draft 2020-12 schema!")
else:
    for err in report.errors:
        print(f"Error at {{err.path}}: {{err.message}} (Rule: {{err.keyword}})")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 7 & 8 -->
        <div>
          <h3 style="font-size: 1.2rem; color: #0284c7; margin-bottom: 0.5rem;">
            <code>tasleemat.get_lexicon()</code> &amp; <code>tasleemat.render_artifact()</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            <code>get_lexicon()</code> retrieves bilingual project management terminology mappings. 
            <code>render_artifact()</code> compiles markdown templates and structured data into standalone, print-ready HTML with Arabic RTL support.
          </p>
          <pre><code># Terminology lookup
terms = tasleemat.get_lexicon(category="governance")

# Headless HTML render
html_output = tasleemat.render_artifact(
    artifact_id="PMO-03.01",
    lang="ar",
    data=payload,
    out_path="./output_charter.html"
)</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 9 -->
        <div>
          <h3 style="font-size: 1.2rem; color: #10b981; margin-bottom: 0.5rem;">
            <code>tasleemat.audit_project(project_path, tier=None, pack=None, strict=False) -&gt; ProjectAuditReport</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Executes deterministic project workspace governance verification. Audits presence of required deliverables for Stage-Gates 0 through 5, validates JSON schemas (Draft 2020-12), and calculates governance compliance scores (0–100%).
          </p>
          <pre><code>import tasleemat

# Audit workspace against Tier 2 Agile requirements
report = tasleemat.audit_project("./PRJ-2026-CLOUD", tier=2, pack="agile", strict=True)
print(f"Overall Completion: {{report.overall_completion_pct}}%")
print(f"Governance Score: {{report.governance_score_pct}}%")

# Check Stage-Gate readiness
for gate in report.gate_kpis:
    print(f"[{{gate.status}}] Gate {{gate.gate_id}} ({{gate.gate_name_en}}): {{gate.percentage}}%")</code></pre>
        </div>

      </div>

      <!-- Section 3: Data Models & Classes -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">3. Data Models &amp; Type Classes</h2>
        
        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;"><code>ArtifactSummary</code> (Immutable Dataclass)</h3>
        <pre><code>@dataclass(frozen=True)
class ArtifactSummary:
    artifact_id: str                    # Unique code (e.g. "PMO-03.01")
    prefix: str                         # File prefix (e.g. "03_01")
    name_en: str                        # English name (e.g. "Project Charter")
    name_ar: str                        # Arabic name (e.g. "ميثاق المشروع")
    phase_code: str                     # Lifecycle phase code ("00" to "07")
    phase_name_en: str                  # Phase name in English
    phase_name_ar: str                  # Phase name in Arabic
    tiers: List[str]                    # Supported tiers: ["1", "2", "3"]
    fingerprint: str                    # SHA-256 fingerprint of canonical source
    completed_data_validation: dict     # Pre-validated baseline report</code></pre>

        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;"><code>ValidationReport</code> &amp; <code>ValidationError</code></h3>
        <pre><code>@dataclass
class ValidationReport:
    valid: bool                         # True if payload passes all schema rules
    errors: List[ValidationError]       # List of structured validation errors
    schema_id: str                      # Canonical URI of the companion schema
    schema_dialect: str                 # "https://json-schema.org/draft/2020-12/schema"
    fingerprint: str                    # Cryptographic hash of schema file

@dataclass
class ValidationError:
    path: str                           # JSON Pointer / property path (e.g. "/risks/0/score")
    message: str                        # Detailed failure explanation
    keyword: str                        # Violated schema keyword (e.g. "required", "format")
    schema_path: str                    # Path inside schema where constraint was declared</code></pre>
      </div>

      <!-- Section 4: Production Tutorials -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text-main);">4. Production Implementation Tutorials</h2>

        <!-- Tutorial 1: FastAPI -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-blue); margin-bottom: 0.5rem;">
            Tutorial 1: Building a Governance REST API with FastAPI
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            Wrap the <code>tasleemat</code> SDK into high-performance REST microservices for enterprise integration:
          </p>
          <pre><code>from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import tasleemat

app = FastAPI(title="Tasleemat PMO Governance API", version="2.6.0")

class TailorRequest(BaseModel):
    tier: int
    pack: str = "general"

class ValidateRequest(BaseModel):
    artifact_id: str
    data: Dict[str, Any]
    mode: str = "strict"

@app.get("/api/v1/artifacts")
def list_artifacts(phase: Optional[str] = None, tier: Optional[int] = None):
    results = tasleemat.list_artifacts(phase=phase, tier=tier)
    return [
        {{"id": a.artifact_id, "name_en": a.name_en, "name_ar": a.name_ar, "phase": a.phase_code}}
        for a in results
    ]

@app.post("/api/v1/tailor")
def tailor_project(req: TailorRequest):
    try:
        deliverable_ids = tasleemat.get_tailoring_profile(tier=req.tier, pack=req.pack)
        return {{"tier": req.tier, "pack": req.pack, "count": len(deliverable_ids), "deliverables": deliverable_ids}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/validate")
def validate_deliverable(req: ValidateRequest):
    report = tasleemat.validate_artifact_data(req.artifact_id, req.data, mode=req.mode)
    return {{
        "valid": report.valid,
        "errors": [{{"path": e.path, "message": e.message, "rule": e.keyword}} for e in report.errors],
        "schema_id": report.schema_id
    }}</code></pre>
        </div>

        <!-- Tutorial 2: Streamlit Dashboard -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">
            Tutorial 2: Interactive PMO Portal with Streamlit
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            Deploy an interactive internal web portal for project managers to tailor their projects and validate deliverables live:
          </p>
          <pre><code>import streamlit as st
import json
import tasleemat

st.set_page_config(page_title="Tasleemat PMO Portal", layout="wide")
st.title("🛡️ Enterprise PMO Deliverables Portal")

st.sidebar.header("Project Tailoring Parameters")
tier = st.sidebar.selectbox("Governance Sizing Tier", [1, 2, 3], index=1)
pack = st.sidebar.selectbox("Delivery Archetype Pack", ["general", "agile", "ai", "predictive", "hybrid"])

deliverables = tasleemat.get_tailoring_profile(tier=tier, pack=pack)
st.sidebar.success(f"Allocated Deliverables: {{len(deliverables)}}")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Required Deliverables Manifest")
    selected_id = st.selectbox("Select Deliverable to Inspect", deliverables)
    assets = tasleemat.get_artifact_assets(selected_id, lang="en")
    st.markdown(f"**Guide:**\\n{{assets.get_guide_content()[:500]}}...")

with col2:
    st.subheader(f"Validate Payload against Schema ({{selected_id}})")
    sample_json = json.dumps({{"project_id": "PRJ-01", "name": "Cloud App"}}, indent=2)
    user_input = st.text_area("JSON Payload", sample_json, height=220)
    
    if st.button("Run Schema Validation"):
        try:
            payload = json.loads(user_input)
            report = tasleemat.validate_artifact_data(selected_id, payload, mode="strict")
            if report.valid:
                st.success("✅ Payload passed all Draft 2020-12 schema assertions!")
            else:
                for err in report.errors:
                    st.error(f"❌ At {{err.path}}: {{err.message}}")
        except json.JSONDecodeError as e:
            st.warning(f"Invalid JSON format: {{e}}")</code></pre>
        </div>

        <!-- Tutorial 3: EVM Engine -->
        <div>
          <h3 style="font-size: 1.25rem; color: var(--accent-amber); margin-bottom: 0.5rem;">
            Tutorial 3: Attested Earned Value Management (EVM) Calculation Engine
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            Execute deterministic, mathematically audited computations for project metrics in <code>PMO-06.05</code> with zero-division handling:
          </p>
          <pre><code>def calculate_evm_metrics(pv: float, ev: float, ac: float, bac: float) -&gt; dict:
    # Computes PMI PMBOK standard Earned Value Management metrics with safe division
    # Variances
    cv = ev - ac                               # Cost Variance
    sv = ev - pv                               # Schedule Variance

    # Indices
    cpi = (ev / ac) if ac &gt; 0 else 1.0        # Cost Performance Index
    spi = (ev / pv) if pv &gt; 0 else 1.0        # Schedule Performance Index

    # Forecasting
    eac = (bac / cpi) if cpi &gt; 0 else bac      # Estimate At Completion
    etc = eac - ac                             # Estimate To Complete
    vac = bac - eac                            # Variance At Completion

    # To-Complete Performance Index (TCPI)
    remaining_work = bac - ev
    remaining_budget = bac - ac
    tcpi = (remaining_work / remaining_budget) if remaining_budget &gt; 0 else 1.0

    return {{
        "cost_variance": round(cv, 2),
        "schedule_variance": round(sv, 2),
        "cpi": round(cpi, 3),
        "spi": round(spi, 3),
        "eac": round(eac, 2),
        "etc": round(etc, 2),
        "vac": round(vac, 2),
        "tcpi": round(tcpi, 3),
        "status": "HEALTHY" if cpi &gt;= 1.0 and spi &gt;= 1.0 else "WARNING"
    }}

# Example calculation:
metrics = calculate_evm_metrics(pv=100000, ev=95000, ac=105000, bac=250000)
print(f"Project CPI: {{metrics['cpi']}}, SPI: {{metrics['spi']}}, EAC: ${{metrics['eac']:,}}")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Tutorial 4: Programmatic Project Governance Audit -->
        <div>
          <h3 style="font-size: 1.25rem; color: #10b981; margin-bottom: 0.5rem;">
            Tutorial 4: Programmatic Stage-Gate Governance Auditing
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            Integrate automated governance verification directly into your Python CI/CD pipelines, pre-commit hooks, or backend services:
          </p>
          <pre><code>import sys
import tasleemat

# Run deterministic audit against project directory
report = tasleemat.audit_project(
    project_path="./projects/PRJ-2026-CLOUD",
    tier=2,
    pack="agile",
    strict=True
)

print(f"Workspace: {{report.project_name}} ({{report.project_code}})")
print(f"Overall Governance Score: {{report.governance_score_pct}}%")
print(f"Completion Rate: {{report.overall_completion_pct}}%")

# Verify Gate 0 to 5 compliance
gate_failed = False
for gate in report.gate_kpis:
    status_icon = "✅" if gate.status == "PASS" else ("⚠️" if gate.status == "WARN" else "❌")
    print(f"{{status_icon}} Gate {{gate.gate_id}} - {{gate.gate_name_en}}: {{gate.percentage}}% ({{gate.completed_count}}/{{gate.required_count}})")
    if gate.status == "FAIL":
        gate_failed = True

# Block deployment if compliance is below threshold
if report.governance_score_pct &lt; 85.0 or gate_failed:
    print("❌ CI/CD Gate Failed: Project governance does not meet enterprise minimums.")
    sys.exit(1)

print("✅ Project approved for next stage gate!")</code></pre>
        </div>

      </div>

    </div>
    """

    return render_html_page(
        title="Python SDK & Core Architecture Reference",
        content=content,
        lang="en",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/developers/sdk/",
        description="Python SDK Reference for Tasleemat: 8 core API functions, ArtifactSummary models, Draft 2020-12 validation, and headless report rendering.",
        canonical_url="https://fakhr.me/Tasleemat/developers/sdk/",
    )


def generate_dev_sdk_ar(base_url: str = "/Tasleemat") -> str:
    subnav = render_dev_subnav("sdk", "ar", base_url)
    
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/ar/">الرئيسية</a> &gt; 
          <a href="{base_url}/ar/developers/">المطورون والذكاء الاصطناعي</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">مكتبة بايثون (SDK)</span>
        </nav>
        <div class="hero-pill"><span>🐍 مكتبة بايثون الخالصة</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">المرجع البرمجي لمكتبة بايثون (SDK)</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
          المرجع البرمجي المعتمد للتحكم الآلي في فهرس التسليمات، تحديد الحجم والتخصيص، التحقق من صحة البيانات وفق Draft 2020-12، وتوليد التقارير.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Section 1: Architectural Foundation AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">1. المعمارية البرمجية ومبدأ الاعتمادية الصفرية</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          تم تصميم مكتبة <code>tasleemat</code> وفق فلسفة صارمة قائمة على <strong>الاعتمادية الصفرية على المكتبات الخارجية (Zero-Dependency)</strong>؛ 
          حيث تعتمد بالكامل على حزم بايثون القياسية المدمجة (<code>json</code>, <code>pathlib</code>, <code>dataclasses</code>, <code>hashlib</code>, <code>re</code>, <code>csv</code>).
          يضمن هذا النهج التثبيت الفوري في بضع ثوانٍ، وانعدام تعارض إصدارات الحزم، وإمكانية التشغيل في البيئات الحكومية والمصرفية المعزولة أمنياً (Air-Gapped).
        </p>
        <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1.25rem; border-radius: 0.5rem;">
          <div style="font-weight: 700; font-size: 0.9rem; margin-bottom: 0.5rem; color: var(--accent-blue);">الضمانات الهندسية الأساسية:</div>
          <ul style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.8; margin: 0; padding-right: 1.25rem;">
            <li><strong>تخزين مؤقت آمن ومتزامن (Thread-Safe Caching):</strong> فهرسة الأصول وتحليل المخططات تتم مرة واحدة في الذاكرة لتوفير استجابة في أجزاء من الملي ثانية.</li>
            <li><strong>حماية النواة المصدرية من التعديل (Immutability):</strong> تمنع دوال الوصول أي عمليات كتابة أو تعديل على بيانات الحزمة المعتمدة.</li>
            <li><strong>توافق تام مع مختلف أنظمة التشغيل:</strong> دعم كامل لأنظمة Linux و macOS و Windows مع معالجة قياسية لترميز UTF-8.</li>
          </ul>
        </div>
      </div>

      <!-- Section 2: Detailed 9 API Functions AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text-main);">2. الدوال التسع المعتمدة في واجهة البرمجة (API)</h2>

        <!-- Function 1 AR -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.5rem; direction: ltr; text-align: right;">
            <code>tasleemat.list_artifacts(phase=None, tier=None, pack=None)</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            استكشاف كائنات التسليمات في الفهرس بالكامل أو مع تصفية محددة بحسب مرحلة المشروع أو مستوى الحجم أو حزمة المنهجية.
          </p>
          <pre style="direction: ltr; text-align: left;"><code>import tasleemat

# استعراض كافة الـ 114 تسليمة
all_artifacts = tasleemat.list_artifacts()
print(f"إجمالي التسليمات: {{len(all_artifacts)}}")

# استعراض تسليمات المرحلة 03 (البدء) للمستوى 2
phase_artifacts = tasleemat.list_artifacts(phase="03", tier=2)
for art in phase_artifacts:
    print(f"- [{{art.artifact_id}}] {{art.name_ar}} ({{art.name_en}})")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 2 AR -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.5rem; direction: ltr; text-align: right;">
            <code>tasleemat.get_artifact_definition(artifact_id: str) -&gt; dict</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            استرجاع قاموس البيانات الوصفية لتسليمة معينة يشمل الأسماء ثنائية اللغة، ورمز المرحلة، والمستويات المدعومة.
          </p>
          <pre style="direction: ltr; text-align: left;"><code>meta = tasleemat.get_artifact_definition("PMO-03.01")
print(f"الاسم بالعربية: {{meta['name_ar']}}")
print(f"الاسم بالإنجليزية: {{meta['name_en']}}")
print(f"المستويات المعتمدة: {{meta['tiers']}}")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 3 & 4 AR -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-amber); margin-bottom: 0.5rem; direction: ltr; text-align: right;">
            <code>tasleemat.get_artifact_assets(artifact_id: str, lang='ar') -&gt; ArtifactAssets</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            استرجاع كائن الأصول الذي يتيح الوصول الآمن للملفات الخمسة المرافقة للتسليمة.
          </p>
          <pre style="direction: ltr; text-align: left;"><code>assets = tasleemat.get_artifact_assets("PMO-03.01", lang="ar")

# دوال الوصول المباشر للمحتوى
template_text = assets.get_template_content()
guide_text = assets.get_guide_content()
example_text = assets.get_example_content()
schema_dict = assets.get_schema_data()
dict_rows = assets.get_dictionary_rows()

# أو جلب الأصل مباشرة بحسب نوعه
schema_raw = tasleemat.get_artifact_asset("PMO-03.01", role="schema", lang="ar")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 5 AR -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: #8b5cf6; margin-bottom: 0.5rem; direction: ltr; text-align: right;">
            <code>tasleemat.get_tailoring_profile(tier: Union[int, str], pack: str='general') -&gt; List[str]</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            تحديد القائمة الدقيقة والحتمية لرموز التسليمات المطلوبة وفق مستوى الحوكمة وحزمة المنهجية.
          </p>
          <pre style="direction: ltr; text-align: left;"><code># استخراج تسليمات مشروع رشيق من المستوى 2
deliverable_ids = tasleemat.get_tailoring_profile(tier=2, pack="agile")
print(f"عدد التسليمات المخصصة: {{len(deliverable_ids)}}")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 6 AR -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: #ec4899; margin-bottom: 0.5rem; direction: ltr; text-align: right;">
            <code>tasleemat.validate_artifact_data(artifact_id: str, data: dict, mode='strict') -&gt; ValidationReport</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            التحقق البرمجي الدقيق من بيانات JSON مقابل مخطط Draft 2020-12 المرافق للتسليمة.
          </p>
          <pre style="direction: ltr; text-align: left;"><code>payload = {{
    "project_id": "PRJ-2026-CLOUD",
    "project_name": "منصة التحول الرقمي السحابي",
    "sponsor": "نائب الرئيس التنفيذي للعمليات",
    "project_manager": "سارة الأحمد",
    "authorization_date": "2026-10-15"
}}

report = tasleemat.validate_artifact_data("PMO-03.01", payload, mode="strict")
if report.valid:
    print("البيانات مطابقة بنسبة 100% لمعايير المخطط المعياري!")
else:
    for err in report.errors:
        print(f"خطأ في الحقل {{err.path}}: {{err.message}} (القاعدة: {{err.keyword}})")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 7 & 8 AR -->
        <div>
          <h3 style="font-size: 1.2rem; color: #0284c7; margin-bottom: 0.5rem; direction: ltr; text-align: right;">
            <code>tasleemat.get_lexicon()</code> و <code>tasleemat.render_artifact()</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            دالة <code>get_lexicon()</code> لاسترجاع المصطلحات المهنية المعتمدة في إدارة المشاريع، ودالة <code>render_artifact()</code> لتوليد مخرجات HTML أنيقة وجاهزة للطباعة مع دعم اتجاه الكتابة العربي (RTL).
          </p>
          <pre style="direction: ltr; text-align: left;"><code># استرجاع المصطلحات المعتمدة
terms = tasleemat.get_lexicon(category="governance")

# توليد صفحة HTML منسقة باللغة العربية
html_output = tasleemat.render_artifact(
    artifact_id="PMO-03.01",
    lang="ar",
    data=payload,
    out_path="./output_charter.html"
)</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Function 9 AR -->
        <div>
          <h3 style="font-size: 1.2rem; color: #10b981; margin-bottom: 0.5rem; direction: ltr; text-align: right;">
            <code>tasleemat.audit_project(project_path, tier=None, pack=None, strict=False) -&gt; ProjectAuditReport</code>
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            تنفيذ تدقيق حوكمي هيكلي وحتمي على مجلد المشروع. يتحقق من اكتمال تسليمات بوابات المراحل (0 إلى 5)، ويفحص سلامة مخططات JSON، ويحسب نسب ومؤشرات الامتثال المئوية.
          </p>
          <pre style="direction: ltr; text-align: left;"><code>import tasleemat

# تدقيق المشروع وفق متطلبات المستوى 2 والمنهجية الرشيقة
report = tasleemat.audit_project("./PRJ-2026-CLOUD", tier=2, pack="agile", strict=True)
print(f"نسبة الإنجاز الكلية: {{report.overall_completion_pct}}%")
print(f"درجة الحوكمة: {{report.governance_score_pct}}%")

# فحص جاهزية بوابات المرحلة
for gate in report.gate_kpis:
    print(f"[{{gate.status}}] البوابة {{gate.gate_id}} ({{gate.gate_name_ar}}): {{gate.percentage}}%")</code></pre>
        </div>

      </div>

      <!-- Section 3: Data Models & Classes AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">3. نماذج البيانات وفئات الكائنات (Data Models)</h2>
        
        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">فئة <code>ArtifactSummary</code> (كائن غير قابل للتعديل)</h3>
        <pre style="direction: ltr; text-align: left;"><code>@dataclass(frozen=True)
class ArtifactSummary:
    artifact_id: str                    # الرمز الفريد للتسليمة (مثل "PMO-03.01")
    prefix: str                         # بادئة الملف (مثل "03_01")
    name_en: str                        # الاسم بالإنجليزية
    name_ar: str                        # الاسم بالعربية
    phase_code: str                     # رمز المرحلة ("00" إلى "07")
    phase_name_en: str                  # اسم المرحلة بالإنجليزية
    phase_name_ar: str                  # اسم المرحلة بالعربية
    tiers: List[str]                    # المستويات المعتمدة: ["1", "2", "3"]
    fingerprint: str                    # بصمة التجزئة SHA-256 للملف المصدري
    completed_data_validation: dict     # تقرير المطابقة المعياري المسبق</code></pre>

        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">فئتا <code>ValidationReport</code> و <code>ValidationError</code></h3>
        <pre style="direction: ltr; text-align: left;"><code>@dataclass
class ValidationReport:
    valid: bool                         # True إذا كانت البيانات مطابقة تماماً
    errors: List[ValidationError]       # قائمة بأخطاء عدم المطابقة المنظمة
    schema_id: str                      # الرابط المعياري للمخطط المرافق
    schema_dialect: str                 # لهجة المخطط Draft 2020-12
    fingerprint: str                    # بصمة التجزئة SHA-256 لملف المخطط

@dataclass
class ValidationError:
    path: str                           # مسار الحقل بنظام JSON Pointer (مثل "/risks/0/score")
    message: str                        # رسالة الخطأ وشرح المشكلة
    keyword: str                        # الكلمة المفتاحية في المخطط التي تم انتهاكها
    schema_path: str                    # مسار القاعدة داخل المخطط نفسه</code></pre>
      </div>

      <!-- Section 4: Production Tutorials AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text-main);">4. أدلة بناء التطبيقات والأنظمة المؤسسية (Tutorials)</h2>

        <!-- Tutorial 1: FastAPI AR -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-blue); margin-bottom: 0.5rem;">
            الدليل 1: بناء واجهة برمجة تطبيقات REST كاملة عبر إطار FastAPI
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            تضمين مكتبة <code>tasleemat</code> في خدمة سحابية عالية الأداء لربط أنظمة المؤسسة:
          </p>
          <pre style="direction: ltr; text-align: left;"><code>from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import tasleemat

app = FastAPI(title="Tasleemat PMO Governance API", version="2.6.0")

class TailorRequest(BaseModel):
    tier: int
    pack: str = "general"

class ValidateRequest(BaseModel):
    artifact_id: str
    data: Dict[str, Any]
    mode: str = "strict"

@app.get("/api/v1/artifacts")
def list_artifacts(phase: Optional[str] = None, tier: Optional[int] = None):
    results = tasleemat.list_artifacts(phase=phase, tier=tier)
    return [
        {{"id": a.artifact_id, "name_en": a.name_en, "name_ar": a.name_ar, "phase": a.phase_code}}
        for a in results
    ]

@app.post("/api/v1/tailor")
def tailor_project(req: TailorRequest):
    try:
        deliverable_ids = tasleemat.get_tailoring_profile(tier=req.tier, pack=req.pack)
        return {{"tier": req.tier, "pack": req.pack, "count": len(deliverable_ids), "deliverables": deliverable_ids}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/validate")
def validate_deliverable(req: ValidateRequest):
    report = tasleemat.validate_artifact_data(req.artifact_id, req.data, mode=req.mode)
    return {{
        "valid": report.valid,
        "errors": [{{"path": e.path, "message": e.message, "rule": e.keyword}} for e in report.errors],
        "schema_id": report.schema_id
    }}</code></pre>
        </div>

        <!-- Tutorial 2: Streamlit Dashboard AR -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">
            الدليل 2: بناء لوحة تحكم تفاعلية للممارسين عبر Streamlit
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            تطبيق ويب متكامل يتيح لمديري المشاريع اختيار مستوى وحزمة المشروع والتحقق من صحة الوثائق مباشرة:
          </p>
          <pre style="direction: ltr; text-align: left;"><code>import streamlit as st
import json
import tasleemat

st.set_page_config(page_title="بوابة تسليمات لإدارة المشاريع", layout="wide")
st.title("🛡️ بوابة الحوكمة وإدارة التسليمات المؤسسية")

st.sidebar.header("معايير تخصيص المشروع")
tier = st.sidebar.selectbox("مستوى الحجم والحوكمة", [1, 2, 3], index=1)
pack = st.sidebar.selectbox("حزمة المنهجية", ["general", "agile", "ai", "predictive", "hybrid"])

deliverables = tasleemat.get_tailoring_profile(tier=tier, pack=pack)
st.sidebar.success(f"عدد التسليمات المعتمدة: {{len(deliverables)}}")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("بيان التسليمات المطلوبة")
    selected_id = st.selectbox("اختر التسليمة للمعاينة", deliverables)
    assets = tasleemat.get_artifact_assets(selected_id, lang="ar")
    st.markdown(f"**دليل الممارس:**\\n{{assets.get_guide_content()[:500]}}...")

with col2:
    st.subheader(f"التحقق من البيانات مقابل المخطط ({{selected_id}})")
    sample_json = json.dumps({{"project_id": "PRJ-01", "name": "مشروع التحول السحابي"}}, indent=2, ensure_ascii=False)
    user_input = st.text_area("بيانات JSON", sample_json, height=220)
    
    if st.button("تشغيل فحص المطابقة"):
        try:
            payload = json.loads(user_input)
            report = tasleemat.validate_artifact_data(selected_id, payload, mode="strict")
            if report.valid:
                st.success("✅ البيانات مطابقة 100% لمعايير المخطط المعياري!")
            else:
                for err in report.errors:
                    st.error(f"❌ في المسار {{err.path}}: {{err.message}}")
        except json.JSONDecodeError as e:
            st.warning(f"صيغة JSON غير صحيحة: {{e}}")</code></pre>
        </div>

        <!-- Tutorial 3: EVM Engine AR -->
        <div>
          <h3 style="font-size: 1.25rem; color: var(--accent-amber); margin-bottom: 0.5rem;">
            الدليل 3: محرك الحسابات الرياضية الموثقة لإدارة القيمة المكتسبة (EVM)
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            كود برمجي حتمي لتنفيذ معادلات القيمة المكتسبة لتسليمة <code>PMO-06.05</code> بدقة ومنع أخطاء القسمة على صفر:
          </p>
          <pre style="direction: ltr; text-align: left;"><code>def calculate_evm_metrics(pv: float, ev: float, ac: float, bac: float) -&gt; dict:
    # حساب مقاييس إدارة القيمة المكتسبة وفق معايير PMI PMBOK مع معالجة آمنة للقسمة
    # التباينات (Variances)
    cv = ev - ac                               # تباين التكلفة (Cost Variance)
    sv = ev - pv                               # تباين الجدول الزمني (Schedule Variance)

    # المؤشرات (Indices)
    cpi = (ev / ac) if ac &gt; 0 else 1.0        # مؤشر أداء التكلفة
    spi = (ev / pv) if pv &gt; 0 else 1.0        # مؤشر أداء الجدول الزمني

    # التنبؤات (Forecasting)
    eac = (bac / cpi) if cpi &gt; 0 else bac      # التكلفة التقديرية عند الاكتمال
    etc = eac - ac                             # التكلفة التقديرية المتبقية للاكتمال
    vac = bac - eac                            # تباين التكلفة عند الاكتمال

    # مؤشر الأداء المطلوب للاكتمال (TCPI)
    remaining_work = bac - ev
    remaining_budget = bac - ac
    tcpi = (remaining_work / remaining_budget) if remaining_budget &gt; 0 else 1.0

    return {{
        "cost_variance": round(cv, 2),
        "schedule_variance": round(sv, 2),
        "cpi": round(cpi, 3),
        "spi": round(spi, 3),
        "eac": round(eac, 2),
        "etc": round(etc, 2),
        "vac": round(vac, 2),
        "tcpi": round(tcpi, 3),
        "status": "HEALTHY" if cpi &gt;= 1.0 and spi &gt;= 1.0 else "WARNING"
    }}

# تجربة حسابية للمشروع:
metrics = calculate_evm_metrics(pv=100000, ev=95000, ac=105000, bac=250000)
print(f"مؤشر التكلفة: {{metrics['cpi']}}، مؤشر الجدول: {{metrics['spi']}}، التكلفة المتوقعة: ${{metrics['eac']:,}}")</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Tutorial 4: Programmatic Project Governance Audit AR -->
        <div>
          <h3 style="font-size: 1.25rem; color: #10b981; margin-bottom: 0.5rem;">
            الدليل 4: التدقيق الحوكمي البرمجي لبوابات المرحلة عبر بايثون
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            دمج التدقيق الآلي المباشر ضمن خطوط أنابيب التكامل المستمر (CI/CD) أو كخطافات ما قبل الالتزام (Pre-commit hooks):
          </p>
          <pre style="direction: ltr; text-align: left;"><code>import sys
import tasleemat

# تدقيق مجلد المشروع تدقيقاً حتمياً
report = tasleemat.audit_project(
    project_path="./projects/PRJ-2026-CLOUD",
    tier=2,
    pack="agile",
    strict=True
)

print(f"المشروع: {{report.project_name}} ({{report.project_code}})")
print(f"درجة الحوكمة الكلية: {{report.governance_score_pct}}%")
print(f"نسبة إنجاز التسليمات: {{report.overall_completion_pct}}%")

# التحقق من امتثال البوابات 0 إلى 5
gate_failed = False
for gate in report.gate_kpis:
    status_icon = "✅" if gate.status == "PASS" else ("⚠️" if gate.status == "WARN" else "❌")
    print(f"{{status_icon}} البوابة {{gate.gate_id}} - {{gate.gate_name_ar}}: {{gate.percentage}}% ({{gate.completed_count}}/{{gate.required_count}})")
    if gate.status == "FAIL":
        gate_failed = True

# إيقاف النشر إذا كانت نسبة الامتثال أقل من الحد الأدنى للمؤسسة
if report.governance_score_pct &lt; 85.0 or gate_failed:
    print("❌ فشل اختبار الحوكمة: المشروع لا يستوفي الحد الأدنى لمعايير البوابة.")
    sys.exit(1)

print("✅ تم اجتياز متطلبات التدقيق واعتماد الانتقال للمرحلة التالية!")</code></pre>
        </div>

      </div>

    </div>
    """

    return render_html_page(
        title="معمارية مكتبة بايثون والمرجع البرمجي",
        content=content,
        lang="ar",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/developers/sdk/",
        description="المرجع البرمجي لمكتبة بايثون (SDK) لتسليمات: الدوال الثماني الأساسية، نماذج البيانات، والتحقق الصارم من مخططات الوثائق.",
        canonical_url="https://fakhr.me/Tasleemat/ar/developers/sdk/",
    )
