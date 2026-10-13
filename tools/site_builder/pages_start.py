"""tools/site_builder/pages_start.py
Generates the 'Start Here' onboarding pathway pages in English and Arabic.
Highlights 3 clear, tailored user pathways:
1. Pathway 1: Project Practitioners & PMO Directors (manuals, templates, tailoring)
2. Pathway 2: Technical Teams & Automation Engineers (CLI, Python SDK, validation)
3. Pathway 3: AI Assistants, LLMs & Multi-Agent Systems (MCP, prompts, self-correction loops)
"""

from tools.site_builder.theme import render_html_page


def generate_start_en(base_url: str = "/Tasleemat") -> str:
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <div class="hero-pill">
          <span>🧭 Onboarding &amp; Pathways</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.25rem;">Start Here: Three Delivery Pathways</h1>
        <p class="hero-subtitle">
          Choose the right starting path based on how your team delivers projects.
        </p>
      </div>
    </section>

    <section class="boundaries-section">
      <div class="container">
        <div style="display: flex; flex-direction: column; gap: 2.5rem; max-width: 960px; margin: 0 auto;">
          
          <!-- Pathway 1 -->
          <div class="card" style="padding: 2rem; border-left: 5px solid var(--accent-emerald);">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
              <h2 style="font-size: 1.4rem;">Pathway 1: Project Practitioners &amp; PMO Directors</h2>
              <span class="tag" style="background: var(--accent-emerald-bg); color: var(--accent-emerald);">Templates &amp; Governance</span>
            </div>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              For Project Managers, PMO Leaders, and Delivery Directors looking to establish structured governance, avoid blank-document paralysis, and tailor deliverables to organizational risk.
            </p>
            <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem;">
              <li><strong>Step 1 — Assess Project Sizing Tier:</strong> Classify your project into Tier 1 (&gt; $10M / Mega), Tier 2 ($1M–$10M / Standard), or Tier 3 (&lt; $1M / Lean). See the <a href="{base_url}/guides/#tailoring">Tailoring Profiles Manual</a>.</li>
              <li><strong>Step 2 — Select Initiation Deliverables:</strong> Download foundational templates starting with <a href="{base_url}/deliverables/PMO-03.01/">PMO-03.01 Project Charter</a>, <a href="{base_url}/deliverables/PMO-03.03/">PMO-03.03 Assumption Log</a>, and <a href="{base_url}/deliverables/PMO-03.04/">PMO-03.04 Stakeholder Register</a>.</li>
              <li><strong>Step 3 — Review the 12 Core Lifecycle Manuals:</strong> Align stage gates and RACI authority before proceeding to detailed baseline planning in Stage 04.</li>
            </ol>
            <div>
              <a href="{base_url}/guides/" class="btn-primary" style="font-size: 0.9rem; padding: 0.6rem 1.25rem;">
                Browse Core Manuals &rarr;
              </a>
            </div>
          </div>

          <!-- Pathway 2 -->
          <div class="card" style="padding: 2rem; border-left: 5px solid var(--accent-blue);">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
              <h2 style="font-size: 1.4rem;">Pathway 2: Technical Teams &amp; Automation Engineers</h2>
              <span class="tag" style="background: var(--accent-blue-bg); color: var(--accent-blue);">CLI &amp; Python SDK</span>
            </div>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              For software engineers, DevOps practitioners, and automation leads integrating Tasleemat deliverables directly into GitOps pipelines, CI/CD validations, or internal portals.
            </p>
            <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem;">
              <li>
                <strong>Step 1 — Install the Verified Python Package:</strong>
                <pre><code>pip install tasleemat</code></pre>
              </li>
              <li>
                <strong>Step 2 — List Tailored Deliverables via CLI:</strong>
                <pre><code>tasleemat list --tier 2 --pack agile</code></pre>
              </li>
              <li>
                <strong>Step 3 — Export Templates &amp; Validate Data:</strong>
                <pre><code>tasleemat asset PMO-04.14 template --lang en > risk_plan.md
tasleemat validate PMO-04.14 completed_data.json</code></pre>
              </li>
            </ol>
            <div>
              <a href="{base_url}/developers/" class="btn-primary" style="font-size: 0.9rem; padding: 0.6rem 1.25rem;">
                View Python &amp; CLI Reference &rarr;
              </a>
            </div>
          </div>

          <!-- Pathway 3 -->
          <div class="card" style="padding: 2rem; border-left: 5px solid var(--accent-amber);">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
              <h2 style="font-size: 1.4rem;">Pathway 3: AI Assistants, LLMs &amp; Multi-Agent Systems</h2>
              <span class="tag" style="background: var(--accent-amber-bg); color: var(--accent-amber);">Model Context Protocol (MCP)</span>
            </div>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              For teams pairing with AI assistants (Claude Desktop, Cursor, Antigravity) or building multi-agent systems that draft, audit, and validate project governance documents deterministically.
            </p>
            <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem;">
              <li>
                <strong>Step 1 — Configure the Stdio MCP Server:</strong>
                Add the Tasleemat MCP tool server to your client configuration:
                <pre><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat",
      "args": ["mcp"]
    }}
  }}
}}</code></pre>
              </li>
              <li>
                <strong>Step 2 — Deterministic Artifact Fetching:</strong>
                Instruct your LLM to fetch the official prompt, guide, and Draft 2020-12 schema using <code>get_artifact_asset</code> rather than hallucinating deliverable structures.
              </li>
              <li>
                <strong>Step 3 — Closed Self-Correction Validation Loop:</strong>
                Pass drafted JSON data to <code>validate_artifact_data</code>. If errors occur, provide schema error paths back to the LLM for autonomous self-correction before human sign-off.
              </li>
            </ol>
            <div>
              <a href="{base_url}/developers/#mcp" class="btn-primary" style="font-size: 0.9rem; padding: 0.6rem 1.25rem;">
                Explore MCP Integration Guide &rarr;
              </a>
            </div>
          </div>

        </div>
      </div>
    </section>
    """

    return render_html_page(
        title="Start Here — Three Delivery Pathways",
        content=content,
        lang="en",
        active_nav="start",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/start/",
    )


def generate_start_ar(base_url: str = "/Tasleemat") -> str:
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <div class="hero-pill">
          <span>🧭 مسارات العمل والتطبيق</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.25rem;">ابدأ هنا: ثلاثة مسارات تطبيقية متكاملة</h1>
        <p class="hero-subtitle">
          اختر المسار الأنسب لطبيعة فريقك وكيفية تسليم المشاريع في منظمتك.
        </p>
      </div>
    </section>

    <section class="boundaries-section">
      <div class="container">
        <div style="display: flex; flex-direction: column; gap: 2.5rem; max-width: 960px; margin: 0 auto;">
          
          <!-- Pathway 1 AR -->
          <div class="card" style="padding: 2rem; border-right: 5px solid var(--accent-emerald);">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
              <h2 style="font-size: 1.4rem;">المسار الأول: ممارسو إدارة المشاريع ومديرو مكاتب الـ PMO</h2>
              <span class="tag" style="background: var(--accent-emerald-bg); color: var(--accent-emerald);">القوالب والحوكمة</span>
            </div>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              لمديري المشاريع، وقادة مكاتب إدارة المشاريع، ومديري التسليم الراغبين في ضبط الحوكمة وتجنب البدء من وثائق فارغة ومواءمة التسليمات مع حجم مخاطر المنظمة.
            </p>
            <ol style="margin-right: 1.5rem; margin-bottom: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem;">
              <li><strong>الخطوة 1 — تحديد مستوى الحوكمة:</strong> صنف مشروعك ضمن المستوى 1 (المشاريع الكبرى &gt; 40 مليون ريال)، المستوى 2 (القياسية 4-40 مليون ريال)، أو المستوى 3 (المشاريع الرشيقة &lt; 4 ملايين ريال). راجع <a href="{base_url}/ar/guides/#tailoring">دليل تخصيص الحوكمة</a>.</li>
              <li><strong>الخطوة 2 — استخراج تسليمات مرحلة البدء:</strong> حمّل القوالب التأسيسية بدءاً من <a href="{base_url}/ar/deliverables/PMO-03.01/">PMO-03.01 ميثاق المشروع</a>، و<a href="{base_url}/ar/deliverables/PMO-03.03/">PMO-03.03 سجل الافتراضات</a>، و<a href="{base_url}/ar/deliverables/PMO-03.04/">PMO-03.04 سجل المعنيين</a>.</li>
              <li><strong>الخطوة 3 — مراجعة الأدلة التنظيمية الـ 12:</strong> اضبط بوابات المراجعة وصلاحيات RACI قبل الانتقال إلى التخطيط التفصيلي في المرحلة 04.</li>
            </ol>
            <div>
              <a href="{base_url}/ar/guides/" class="btn-primary" style="font-size: 0.9rem; padding: 0.6rem 1.25rem;">
                تصفح الأدلة التشغيلية الـ 12 &larr;
              </a>
            </div>
          </div>

          <!-- Pathway 2 AR -->
          <div class="card" style="padding: 2rem; border-right: 5px solid var(--accent-blue);">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
              <h2 style="font-size: 1.4rem;">المسار الثاني: الفرق التقنية ومهندسو الأتمتة</h2>
              <span class="tag" style="background: var(--accent-blue-bg); color: var(--accent-blue);">مكتبة بايثون وأمر التشغيل CLI</span>
            </div>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              لمطوري البرمجيات، ومهندسي DevOps، ومسؤولي الأتمتة الساعين لدمج تسليمات المشاريع مباشرة ضمن خطوط الـ CI/CD، والتحقق الآلي من جودة البيانات.
            </p>
            <ol style="margin-right: 1.5rem; margin-bottom: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem;">
              <li>
                <strong>الخطوة 1 — تثبيت حزمة بايثون المعتمدة:</strong>
                <pre><code>pip install tasleemat</code></pre>
              </li>
              <li>
                <strong>الخطوة 2 — استعراض التسليمات المخصصة عبر الطرفية:</strong>
                <pre><code>tasleemat list --tier 2 --pack agile</code></pre>
              </li>
              <li>
                <strong>الخطوة 3 — تصدير القوالب والتحقق من البيانات:</strong>
                <pre><code>tasleemat asset PMO-04.14 template --lang ar > risk_plan_ar.md
tasleemat validate PMO-04.14 completed_data.json</code></pre>
              </li>
            </ol>
            <div>
              <a href="{base_url}/ar/developers/" class="btn-primary" style="font-size: 0.9rem; padding: 0.6rem 1.25rem;">
                دليل المطورين وأمر التشغيل &larr;
              </a>
            </div>
          </div>

          <!-- Pathway 3 AR -->
          <div class="card" style="padding: 2rem; border-right: 5px solid var(--accent-amber);">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
              <h2 style="font-size: 1.4rem;">المسار الثالث: مساعدو الذكاء الاصطناعي والأنظمة متعددة الوكلاء</h2>
              <span class="tag" style="background: var(--accent-amber-bg); color: var(--accent-amber);">بروتوكول سياق النماذج (MCP)</span>
            </div>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              للفرق التي تستخدم مساعدي الذكاء الاصطناعي (Claude Desktop، Cursor، Antigravity) أو تبني أنظمة وكلاء متعددة لصياغة وتدقيق وثائق الحوكمة بدقة متناهية.
            </p>
            <ol style="margin-right: 1.5rem; margin-bottom: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem;">
              <li>
                <strong>الخطوة 1 — ضبط إعدادات خادم MCP:</strong>
                أضف خادم Tasleemat MCP إلى إعدادات العميل لديك:
                <pre><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat",
      "args": ["mcp"]
    }}
  }}
}}</code></pre>
              </li>
              <li>
                <strong>الخطوة 2 — جلب الأصول المرجعية بدقة:</strong>
                وجّه نموذج الذكاء الاصطناعي لاسترجاع الموجه (Prompt) والدليل ومخطط Draft 2020-12 عبر أداة <code>get_artifact_asset</code> لمنع الهلوسة في هيكلة الوثائق.
              </li>
              <li>
                <strong>الخطوة 3 — حلقة التصحيح الذاتي المغلقة:</strong>
                أرسل البيانات المصوغة لأداة <code>validate_artifact_data</code>، وفي حال وجود أخطاء بنوية يتم إرجاع مسار الخطأ للنموذج لتصحيحه ذاتياً قبل التوقيع البشري.
              </li>
            </ol>
            <div>
              <a href="{base_url}/ar/developers/#mcp" class="btn-primary" style="font-size: 0.9rem; padding: 0.6rem 1.25rem;">
                دليل تكامل الذكاء الاصطناعي وMCP &larr;
              </a>
            </div>
          </div>

        </div>
      </div>
    </section>
    """

    return render_html_page(
        title="ابدأ هنا — ثلاثة مسارات تطبيقية",
        content=content,
        lang="ar",
        active_nav="start",
        base_url=base_url,
        alt_lang_url=f"{base_url}/start/",
    )
