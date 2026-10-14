"""tools/site_builder/pages_dev/schemas.py
JSON Schema Draft 2020-12 Specifications, RFC Validation Rules, Autonomous Healing Loop & Tutorials (English & Arabic).
"""

from tools.site_builder.theme import render_html_page
from tools.site_builder.pages_dev.nav import render_dev_subnav


def generate_dev_schemas_en(base_url: str = "/Tasleemat") -> str:
    subnav = render_dev_subnav("schemas", "en", base_url)
    
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/">Home</a> &gt; 
          <a href="{base_url}/developers/">Developers &amp; AI</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">Schemas &amp; Validation</span>
        </nav>
        <div class="hero-pill"><span>📐 JSON Schema Draft 2020-12</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">JSON Schemas &amp; Autonomous Healing Engine</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto;">
          Strict validation contracts across 114 deliverables, RFC format enforcement, and the autonomous self-correction loop for AI agents.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Section 1: Philosophy & Dialect -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">1. Why JSON Schema Draft 2020-12?</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          In regulated enterprise environments, prompt-based LLM generation is inherently non-deterministic: models frequently hallucinate 
          undeclared properties, omit required approvals, or format ISO dates inconsistently. 
          Tasleemat enforces <strong>JSON Schema Draft 2020-12</strong> as the authoritative validation contract for every deliverable.
        </p>
        <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1.25rem; border-radius: 0.5rem;">
          <div style="font-weight: 700; font-size: 0.9rem; margin-bottom: 0.5rem; color: var(--accent-blue);">Draft 2020-12 Superpowers:</div>
          <ul style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7; margin: 0; padding-left: 1.25rem;">
            <li><code>unevaluatedProperties: false</code>: Strictly forbids any hallucinated keys not explicitly defined in the schema.</li>
            <li><code>dependentRequired</code>: Dynamic constraints (e.g. if <code>has_procurement_impact: true</code>, then <code>procurement_officer_signoff</code> is mandatory).</li>
            <li><code>prefixItems</code>: Tuple-style ordered array validation for chronological stage-gate signoffs.</li>
          </ul>
        </div>
      </div>

      <!-- Section 2: RFC Format Enforcement -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">2. Enforced RFC Formats &amp; Validation Modes</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          The pure-Python validator executes strict syntactic and semantic checking for the following RFC standards:
        </p>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>RFC Standard</th>
                <th>Format Keyword</th>
                <th>Validation Semantics</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>RFC 3339</strong></td>
                <td><code>date</code></td>
                <td>Full-date formatted as <code>YYYY-MM-DD</code>. Leap years and calendar days are mathematically verified.</td>
              </tr>
              <tr>
                <td><strong>RFC 3339</strong></td>
                <td><code>date-time</code></td>
                <td>Timestamp formatted as <code>YYYY-MM-DDTHH:MM:SSZ</code> with strict UTC offset validation.</td>
              </tr>
              <tr>
                <td><strong>RFC 4122</strong></td>
                <td><code>uuid</code></td>
                <td>128-bit hexadecimal identifier formatted in 8-4-4-4-12 structure.</td>
              </tr>
              <tr>
                <td><strong>RFC 3986</strong></td>
                <td><code>uri</code></td>
                <td>Compliant Uniform Resource Identifier with valid scheme, authority, and path syntax.</td>
              </tr>
              <tr>
                <td><strong>RFC 5322</strong></td>
                <td><code>email</code></td>
                <td>Standard mailbox address syntax with verified username and domain parts.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3 style="font-size: 1.15rem; margin-top: 1.75rem; margin-bottom: 0.5rem;">Strict vs. Draft Validation Modes</h3>
        <ul style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.8; padding-left: 1.5rem;">
          <li><code>mode="strict"</code>: Zero tolerance. Enforces all required properties, non-empty string values, and rejects any undeclared fields. Mandatory for formal stage-gate audits and executive reviews.</li>
          <li><code>mode="draft"</code>: Permissive progressive elaboration. Allows optional fields to remain null or empty while strictly validating types and RFC formats for any populated fields. Used during early sprint planning.</li>
        </ul>
      </div>

      <!-- Section 3: The Autonomous Healing Loop -->
      <div id="self-correction" class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
          <h2 style="font-size: 1.5rem; margin: 0; color: var(--text-main);">3. The Autonomous Agent Self-Correction Feedback Loop</h2>
          <span class="badge" style="background: var(--accent-blue-bg); color: var(--accent-blue); font-weight: 700; font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">Healing Engine</span>
        </div>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Frontier AI models (Gemini, Claude, GPT-4o) do not need humans to fix slight schema discrepancies. 
          When an LLM produces a payload that violates a constraint, <code>tasleemat.validate_artifact_data</code> returns 
          precise JSON Pointer paths. The agent feeds these exact errors back into the model to heal its output in a single retry turn:
        </p>

        <pre><code class="language-mermaid">
sequenceDiagram
    autonumber
    actor User as Project Manager
    participant Agent as Autonomous PMO Agent
    participant Engine as Tasleemat Validator
    participant LLM as Frontier LLM Model

    User->>Agent: "Draft Risk Register for Cloud Project"
    Agent->>Engine: get_artifact_asset("PMO-04.08.02", "schema")
    Engine-->>Agent: Draft 2020-12 Schema Definition
    Agent->>LLM: Prompt + Schema Constraints
    LLM-->>Agent: Raw JSON Payload (Draft 1)
    Agent->>Engine: validate_artifact_data("PMO-04.08.02", Draft 1, mode="strict")
    Engine-->>Agent: ValidationReport(valid=False, error="At /risks/0/score: missing required property")
    Note over Agent,LLM: Autonomous Healing Turn
    Agent->>LLM: "Previous output failed validation at /risks/0/score. Rectify schema error."
    LLM-->>Agent: Corrected JSON Payload (Draft 2)
    Agent->>Engine: validate_artifact_data("PMO-04.08.02", Draft 2, mode="strict")
    Engine-->>Agent: ValidationReport(valid=True)
    Agent->>User: "Risk Register Generated &amp; 100% Schema Validated"
        </code></pre>
      </div>

      <!-- Section 4: Production Tutorials -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">4. Practical Step-by-Step Tutorials</h2>

        <!-- Tutorial 1 -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.5rem;">
            Tutorial 1: Complete Production Autonomous Healing Loop Implementation
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 0.75rem;">
            A complete, runnable script implementing the retry loop with convergence telemetry:
          </p>
          <pre><code>import json
import tasleemat

def run_autonomous_synthesis(artifact_id: str, prompt_notes: str, llm_callable, max_retries: int = 3):
    # Synthesizes structured deliverable data with autonomous schema self-healing
    schema = tasleemat.get_artifact_asset(artifact_id, "schema", lang="en")
    current_prompt = prompt_notes
    telemetry = {{"attempts": 0, "healed": False}}

    for attempt in range(1, max_retries + 1):
        telemetry["attempts"] = attempt
        print(f"Synthesis attempt {{attempt}} for {{artifact_id}}...")
        
        # 1. Call your configured LLM
        candidate_json_str = llm_callable(prompt=current_prompt, schema=schema)
        candidate_data = json.loads(candidate_json_str)

        # 2. Validate against Draft 2020-12 companion schema
        report = tasleemat.validate_artifact_data(artifact_id, candidate_data, mode="strict")
        if report.valid:
            print(f"✅ Success! Converged on valid schema payload in {{attempt}} attempt(s).")
            telemetry["healed"] = attempt &gt; 1
            return candidate_data, telemetry

        # 3. Formulate targeted remediation instructions
        error_lines = [f"- Path '{{e.path}}': {{e.message}} (Violated: {{e.keyword}})" for e in report.errors]
        current_prompt = (
            f"{{prompt_notes}}\\n\\n"
            f"[CRITICAL VALIDATION FEEDBACK - ATTEMPT {{attempt}} FAILED]:\\n"
            + "\\n".join(error_lines)
            + "\\nFix these exact JSON paths and return the corrected JSON object."
        )

    raise RuntimeError(f"Failed to converge on valid schema payload after {{max_retries}} retries.")</code></pre>
        </div>

        <!-- Tutorial 2 -->
        <div>
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">
            Tutorial 2: Authoring a Custom Deliverable Schema
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 0.75rem;">
            Design a custom Draft 2020-12 schema for enterprise deliverables (e.g. Security Audit Sign-off):
          </p>
          <pre><code>custom_schema = {{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://company.org/schemas/pmo-sec-01.json",
    "title": "Cloud Security Sign-off",
    "type": "object",
    "required": ["project_id", "security_officer", "signoff_date", "vulnerability_count"],
    "properties": {{
        "project_id": {{"type": "string", "pattern": "^PRJ-[0-9]{{4}}-[A-Z]+$"}},
        "security_officer": {{"type": "string", "minLength": 3}},
        "signoff_date": {{"type": "string", "format": "date"}},
        "vulnerability_count": {{"type": "integer", "minimum": 0, "maximum": 0}},
        "audit_passed": {{"type": "boolean", "const": True}}
    }},
    "unevaluatedProperties": False
}}</code></pre>
        </div>

      </div>

    </div>
    """

    return render_html_page(
        title="JSON Schemas & Autonomous Healing Reference",
        content=content,
        lang="en",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/developers/schemas/",
        description="JSON Schema Draft 2020-12 specifications, strict RFC format constraints, and autonomous agent self-correction feedback loop for Tasleemat.",
        canonical_url="https://fakhr.me/Tasleemat/developers/schemas/",
    )


def generate_dev_schemas_ar(base_url: str = "/Tasleemat") -> str:
    subnav = render_dev_subnav("schemas", "ar", base_url)
    
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/ar/">الرئيسية</a> &gt; 
          <a href="{base_url}/ar/developers/">المطورون والذكاء الاصطناعي</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">المخططات والتحقق</span>
        </nav>
        <div class="hero-pill"><span>📐 معيار JSON Schema Draft 2020-12</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">مخططات JSON ومحرك التصحيح الذاتي التلقائي</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
          عقود التحقق الصارمة لكافة الـ 114 تسليمة، معايير وتنسيقات RFC الإلزامية، ومحرك التغذية الراجعة التلقائية لإصلاح أخطاء نماذج الذكاء الاصطناعي.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Section 1: Philosophy AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">1. لماذا اعتمدنا معيار JSON Schema Draft 2020-12؟</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          في البيئات المؤسسية والحكومية الخاضعة للتدقيق الصارم، لا يمكن الاعتماد على التوليد النصي الحر لنماذج الذكاء الاصطناعي؛ 
          إذ تعاني النماذج من الهلوسة بابتكار حقول غير معتمدة، أو إغفال التوقيعات الإلزامية، أو كتابة التواريخ بصيغ عشوائية.
          لذلك، تفرض منظومة تسليمات مخطط <strong>JSON Schema Draft 2020-12</strong> كعقد إلزامي لكل تسليمة.
        </p>
        <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1.25rem; border-radius: 0.5rem;">
          <div style="font-weight: 700; font-size: 0.9rem; margin-bottom: 0.5rem; color: var(--accent-blue);">مزايا معيار Draft 2020-12:</div>
          <ul style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.8; margin: 0; padding-right: 1.25rem;">
            <li><code>unevaluatedProperties: false</code>: حظر أي حقول إضافية غير معلنة في المخطط منعاً تاماً للهلوسة.</li>
            <li><code>dependentRequired</code>: قواعد الارتباط الشرطي (مثال: إذا كان للمشروع أثر تعاقدي، يصبح توقيع مسؤول المشتريات إلزامياً).</li>
            <li><code>prefixItems</code>: التحقق من الترتيب الزمني لمصفوفات الموافقات وبوابات المراجعة.</li>
          </ul>
        </div>
      </div>

      <!-- Section 2: RFC Formats AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">2. معايير RFC الإلزامية وأوضاع التحقق</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          يتحقق محرك الفحص الآلي من صحة التنسيقات وفق المعايير الدولية التالية:
        </p>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>معيار RFC</th>
                <th>الكلمة المفتاحية</th>
                <th>قواعد ودلالات التحقق</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>RFC 3339</strong></td>
                <td><code>date</code></td>
                <td>صيغة التاريخ الكامل <code>YYYY-MM-DD</code> مع التحقق الحسابي من السنوات الكبيسة وأيام الأشهر.</td>
              </tr>
              <tr>
                <td><strong>RFC 3339</strong></td>
                <td><code>date-time</code></td>
                <td>التوقيت الكامل <code>YYYY-MM-DDTHH:MM:SSZ</code> مع التحقق من دقة المنطقة الزمنية UTC.</td>
              </tr>
              <tr>
                <td><strong>RFC 4122</strong></td>
                <td><code>uuid</code></td>
                <td>المعرف الفريد بطول 128 بت بصيغة الستة عشري القياسية (8-4-4-4-12).</td>
              </tr>
              <tr>
                <td><strong>RFC 3986</strong></td>
                <td><code>uri</code></td>
                <td>صحة هيكلية الروابط ومطابقتها لبروتوكولات ومسارات الويب المعتمدة.</td>
              </tr>
              <tr>
                <td><strong>RFC 5322</strong></td>
                <td><code>email</code></td>
                <td>الصيغة القياسية لصناديق البريد الإلكتروني مع التحقق من صحة النطاق واسم المستخدم.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3 style="font-size: 1.15rem; margin-top: 1.75rem; margin-bottom: 0.5rem;">أوضاع التحقق: الصارم (Strict) مقابل المسودة (Draft)</h3>
        <ul style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.8; padding-right: 1.5rem;">
          <li><code>mode="strict"</code>: التدقيق الصارم بدون تساهل. يفرض وجود كافة الحقول الإلزامية، ويرفض النصوص الفارغة والحقول غير المعلنة. إلزامي لبوابات المراجعة واعتمادات اللجان التوجيهية.</li>
          <li><code>mode="draft"</code>: التدقيق المرن للتطوير التدريجي. يسمح بترك الحقول الاختيارية فارغة مع التحقق من صحة أنواع وتنسيقات الحقول المعبأة. يُستخدم أثناء التخطيط المبكر وسبرنتات العمل الأولى.</li>
        </ul>
      </div>

      <!-- Section 3: The Autonomous Healing Loop AR -->
      <div id="self-correction" class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
          <h2 style="font-size: 1.5rem; margin: 0; color: var(--text-main);">3. حلقة التصحيح الذاتي التلقائي للوكلاء الأذكياء</h2>
          <span class="badge" style="background: var(--accent-blue-bg); color: var(--accent-blue); font-weight: 700; font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">محرك المعالجة الذاتية</span>
        </div>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          النماذج اللغوية الرائدة (مثل Gemini و Claude و GPT-4o) لا تحتاج إلى تدخل بشري لتعديل الأخطاء الطفيفة؛ 
          فعندما ينتج النموذج بيانات تخالف المخطط، ترجع دالة <code>tasleemat.validate_artifact_data</code> مسار الخطأ بدقة 
          (عبر JSON Pointer). يقوم الوكيل بإعادة توجيه الخطأ للنموذج ليصلح نفسه تلقائياً في جولة واحدة:
        </p>

        <pre><code class="language-mermaid">
sequenceDiagram
    autonumber
    actor User as الممارس / مدير المشروع
    participant Agent as الوكيل الذكي (PMO Agent)
    participant Engine as محرك التحقق في تسليمات
    participant LLM as نموذج الذكاء الاصطناعي (LLM)

    User->>Agent: "قم بإعداد سجل المخاطر لمشروع السحابة"
    Agent->>Engine: get_artifact_asset("PMO-04.08.02", "schema")
    Engine-->>Agent: مخطط Draft 2020-12
    Agent->>LLM: الأمر + قيود المخطط البرمجي
    LLM-->>Agent: بيانات JSON الأولية (المسودة 1)
    Agent->>Engine: validate_artifact_data("PMO-04.08.02", المسودة 1, mode="strict")
    Engine-->>Agent: ValidationReport(valid=False, error="نقص حقل إلزامي في /risks/0/score")
    Note over Agent,LLM: جولة التصحيح الذاتي التلقائي
    Agent->>LLM: "فشل التحقق في المسار /risks/0/score. أصلح الخطأ فوراً."
    LLM-->>Agent: بيانات JSON المصححة (المسودة 2)
    Agent->>Engine: validate_artifact_data("PMO-04.08.02", المسودة 2, mode="strict")
    Engine-->>Agent: ValidationReport(valid=True)
    Agent->>User: "تم توليد سجل المخاطر بنجاح وتأكيد صحته وفق المخطط 100%"
        </code></pre>
      </div>

      <!-- Section 4: Production Tutorials AR -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">4. أدلة تطبيقية عملية (Tutorials)</h2>

        <!-- Tutorial 1 AR -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.5rem;">
            الدليل 1: كود برمجي متكامل لحلقة التصحيح الذاتي التلقائي
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            سكربت بايثون تنفيذي مكتمل لتطبيق حلقة التصحيح الذاتي مع قياس أداء التعافي:
          </p>
          <pre style="direction: ltr; text-align: left;"><code>import json
import tasleemat

def run_autonomous_synthesis(artifact_id: str, prompt_notes: str, llm_callable, max_retries: int = 3):
    # توليد بيانات الوثائق مع المعالجة الذاتية التلقائية للأخطاء
    schema = tasleemat.get_artifact_asset(artifact_id, "schema", lang="ar")
    current_prompt = prompt_notes
    telemetry = {{"attempts": 0, "healed": False}}

    for attempt in range(1, max_retries + 1):
        telemetry["attempts"] = attempt
        print(f"محاولة التوليد رقم {{attempt}} للتسليمة {{artifact_id}}...")
        
        # 1. استدعاء نموذج الذكاء الاصطناعي
        candidate_json_str = llm_callable(prompt=current_prompt, schema=schema)
        candidate_data = json.loads(candidate_json_str)

        # 2. التحقق الآلي من المخطط المعياري
        report = tasleemat.validate_artifact_data(artifact_id, candidate_data, mode="strict")
        if report.valid:
            print(f"✅ نجاح كامل! تم التوافق التام مع المخطط في المحاولة رقم {{attempt}}.")
            telemetry["healed"] = attempt &gt; 1
            return candidate_data, telemetry

        # 3. صياغة توجيه التصحيح المركز للنموذج
        error_lines = [f"- في المسار '{{e.path}}': {{e.message}} (القاعدة: {{e.keyword}})" for e in report.errors]
        current_prompt = (
            f"{{prompt_notes}}\\n\\n"
            f"[تنبيه: فشلت المحاولة رقم {{attempt}} في التحقق للأسباب التالية:]\\n"
            + "\\n".join(error_lines)
            + "\\nقم بتصحيح مسارات JSON هذه بدقة وأعد إرسال الكائن النهائي الصحيح."
        )

    raise RuntimeError(f"تعذر الوصول لبيانات مطابقة بعد {{max_retries}} محاولات.")</code></pre>
        </div>

        <!-- Tutorial 2 AR -->
        <div>
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">
            الدليل 2: كتابة وتصميم مخطط تسليمة مؤسسية مخصصة
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            تصميم مخطط Draft 2020-12 لتسليمة اعتماد أمان السحابة المؤسسي:
          </p>
          <pre style="direction: ltr; text-align: left;"><code>custom_schema = {{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://company.org/schemas/pmo-sec-01.json",
    "title": "اعتماد أمان السحابة",
    "type": "object",
    "required": ["project_id", "security_officer", "signoff_date", "vulnerability_count"],
    "properties": {{
        "project_id": {{"type": "string", "pattern": "^PRJ-[0-9]{{4}}-[A-Z]+$"}},
        "security_officer": {{"type": "string", "minLength": 3}},
        "signoff_date": {{"type": "string", "format": "date"}},
        "vulnerability_count": {{"type": "integer", "minimum": 0, "maximum": 0}},
        "audit_passed": {{"type": "boolean", "const": True}}
    }},
    "unevaluatedProperties": False
}}</code></pre>
        </div>

      </div>

    </div>
    """

    return render_html_page(
        title="مخططات JSON وحلقة التصحيح الذاتي",
        content=content,
        lang="ar",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/developers/schemas/",
        description="مواصفات مخططات JSON المعيارية Draft 2020-12، قيود RFC الإلزامية، ومحرك التصحيح الذاتي التلقائي لأسراب الوكلاء الأذكياء.",
        canonical_url="https://fakhr.me/Tasleemat/ar/developers/schemas/",
    )
