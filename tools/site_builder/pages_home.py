"""tools/site_builder/pages_home.py
Generates the Home pages in English and Arabic for the Tasleemat Portal.
Includes:
- Hero with accurate value proposition
- Interactive 8-Phase Lifecycle Map (00 to 07)
- Governance Sizing Tiers (1 Mega, 2 Standard, 3 Lean) with link to dedicated /tailoring/ page
- Methodology Archetype Packs (General, Agile, AI, Predictive, Hybrid)
- Honest Boundaries table (What Tasleemat Provides vs What It Does Not Do) placed before the footer
"""

from tools.site_builder.theme import render_html_page

PHASES_DATA = [
    {
        "code": "00",
        "name_en": "00. Program & Portfolio Management",
        "name_ar": "00. إدارة البرامج والمحافظ",
        "count": 6,
        "desc_en": "Strategic alignment, portfolio balancing, multi-project interdependencies, and PMO maturity assessments.",
        "desc_ar": "المواءمة الاستراتيجية، توازن المحفظة، إدارة الاعتماديات بين المشاريع، وتقييم نضج مكتب إدارة المشاريع.",
        "icon": "🏛️"
    },
    {
        "code": "01",
        "name_en": "01. Business & Value Delivery",
        "name_ar": "01. الأعمال وتسليم القيمة",
        "count": 4,
        "desc_en": "Business justification, benefits realization planning, value registers, and capability gap analysis.",
        "desc_ar": "دراسات الجدوى الاقتصادية، خطط إدارة المنافع، سجلات تحقيق القيمة، وتحليل الفجوات المؤسسية.",
        "icon": "💎"
    },
    {
        "code": "02",
        "name_en": "02. Project Approach & Tailoring",
        "name_ar": "02. منهجية المشروع والتخصيص",
        "count": 6,
        "desc_en": "Tailoring strategy, governance tiers, AI ethics evaluation, model cards, and agile/hybrid adoption.",
        "desc_ar": "استراتيجية التخصيص، مستويات الحوكمة، أخلاقيات الذكاء الاصطناعي، بطاقات النماذج، والتبني الهجين.",
        "icon": "⚖️"
    },
    {
        "code": "03",
        "name_en": "03. Initiating",
        "name_ar": "03. البدء والترخيص",
        "count": 5,
        "desc_en": "Formal project charter authorization, product vision canvas, initial assumption logs, and stakeholder registers.",
        "desc_ar": "الترخيص الرسمي لميثاق المشروع، رؤية المنتج، سجل الافتراضات الأولية، وسجل المعنيين.",
        "icon": "🚀"
    },
    {
        "code": "04",
        "name_en": "04. Planning",
        "name_ar": "04. التخطيط المتكامل",
        "count": 55,
        "desc_en": "Comprehensive baselines across Scope, Schedule, Cost, Quality, Resources, Risk, Procurement, and ESG.",
        "desc_ar": "الخطوط المرجعية الشاملة للنطاق، الجدول الزمني، التكلفة، الجودة، الموارد، المخاطر، والمشتريات.",
        "icon": "📐"
    },
    {
        "code": "05",
        "name_en": "05. Executing",
        "name_ar": "05. التنفيذ والتوجيه",
        "count": 15,
        "desc_en": "Directing deliverable work, issue and decision management, change request control, and team performance.",
        "desc_ar": "توجيه وإدارة أعمال التسليم، سجل القضايا، سجل القرارات، التحكم بطلبات التغيير، وأداء الفريق.",
        "icon": "⚡"
    },
    {
        "code": "06",
        "name_en": "06. Monitoring & Controlling",
        "name_ar": "06. المراقبة والتحكم",
        "count": 16,
        "desc_en": "Status reporting, Earned Value Analysis (EVA), variance tracking, risk audits, and user acceptance testing.",
        "desc_ar": "تقارير الأداء، تحليل القيمة المكتسبة (EVA)، مراقبة التباين، تدقيق المخاطر، واختبارات القبول النهائي.",
        "icon": "📊"
    },
    {
        "code": "07",
        "name_en": "07. Closing",
        "name_ar": "07. الإغلاق والتسليم النهائي",
        "count": 7,
        "desc_en": "Operational transition checklists, contract closeout, final lessons learned summaries, and post-implementation review.",
        "desc_ar": "قوائم انتقال العمليات التشغيلية، إغلاق العقود، خلاصة الدروس المستفادة، والمراجعة البعدية.",
        "icon": "🏁"
    }
]


def generate_home_en(base_url: str = "/Tasleemat") -> str:
    """Generates the English home page."""
    stages_cards = "\n".join([
        f"""<a href="{base_url}/deliverables/?phase={p['code']}" class="stage-card">
          <div class="stage-badge">{p['icon']} Phase {p['code']}</div>
          <div class="stage-name">{p['name_en']}</div>
          <div class="stage-desc">{p['desc_en']}</div>
          <div class="stage-count">{p['count']} Deliverables &rarr;</div>
        </a>"""
        for p in PHASES_DATA
    ])

    content = f"""
    <section class="hero-section">
      <div class="container">
        <div class="hero-pill">
          <span>🛡️ Verified Project Deliverables &amp; Open Toolkit</span>
        </div>
        <h1 class="hero-title">Bilingual Project Management Deliverable Library &amp; Toolkit</h1>
        <p class="hero-subtitle">
          114 canonical project deliverables, practitioner guides, companion JSON schemas (Draft 2020-12),
          and automation tools for practitioners, PMOs, developers, and AI agents.
        </p>
        <div class="hero-actions">
          <a href="{base_url}/deliverables/" class="btn-primary">
            🔍 Explore 114 Deliverables
          </a>
          <a href="{base_url}/start/" class="btn-secondary">
            🚀 Start Here (3 Pathways)
          </a>
        </div>
        <div class="devhunt-badge-wrap">
          <a href="https://devhunt.org/tool/tasleemat" target="_blank" title="tasleemat on DevHunt" class="devhunt-badge devhunt-dark"><img src="https://devhunt.org/badge/tasleemat.svg" alt="tasleemat - Featured on DevHunt" width="220" height="54" /></a>
          <a href="https://devhunt.org/tool/tasleemat" target="_blank" title="tasleemat on DevHunt" class="devhunt-badge devhunt-light"><img src="https://devhunt.org/badge/tasleemat.svg?theme=light" alt="tasleemat - Featured on DevHunt" width="220" height="54" /></a>
        </div>
      </div>
    </section>

    <!-- Lifecycle Map -->
    <section class="boundaries-section" style="background-color: var(--bg-card); border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color);">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">8 Project Lifecycle Stages</h2>
          <p class="section-desc">From portfolio strategy through planning, execution, monitoring, and closing.</p>
        </div>
        <div class="stages-grid">
          {stages_cards}
        </div>
      </div>
    </section>

    <!-- Governance Tiers & Packs Summary -->
    <section class="boundaries-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">Governance Sizing Tiers &amp; Delivery Packs</h2>
          <p class="section-desc">Tailor governance rigor to project scale, complexity, and delivery methodology.</p>
        </div>
        <div class="grid-cards">
          <div class="card">
            <div class="card-title">🏢 Tier 1: Mega &amp; Strategic</div>
            <div class="card-desc">
              For investments &gt; $10M / &gt; 40M SAR, high organizational risk, or multi-year enterprise transformations.
            </div>
            <div class="tag-list">
              <span class="tag tier">35–50 Deliverables</span>
              <span class="tag">Steering Committee</span>
              <span class="tag">Formal Stage Gates</span>
            </div>
          </div>
          <div class="card">
            <div class="card-title">⚖️ Tier 2: Standard Projects</div>
            <div class="card-desc">
              For investments between $1M–$10M / 4M–40M SAR, cross-functional teams, and standard departmental initiatives.
            </div>
            <div class="tag-list">
              <span class="tag tier">18–25 Deliverables</span>
              <span class="tag">PMO Review</span>
              <span class="tag">Balanced Rigor</span>
            </div>
          </div>
          <div class="card">
            <div class="card-title">⚡ Tier 3: Lean Projects</div>
            <div class="card-desc">
              For investments &lt; $1M / &lt; 4M SAR, low risk, internal enhancements, or fast prototyping.
            </div>
            <div class="tag-list">
              <span class="tag tier">7–9 Deliverables</span>
              <span class="tag">Sponsor Sign-off</span>
              <span class="tag">Minimal Overhead</span>
            </div>
          </div>
        </div>

        <div style="margin-top: 2.5rem; text-align: center;">
          <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">Delivery Archetype Packs</h3>
          <div style="display: flex; gap: 0.75rem; justify-content: center; flex-wrap: wrap; margin-bottom: 1.75rem;">
            <span class="tag pack">General Delivery</span>
            <span class="tag pack">Agile &amp; Scrum</span>
            <span class="tag pack">AI &amp; Machine Learning</span>
            <span class="tag pack">Predictive / Waterfall</span>
            <span class="tag pack">Hybrid Framework</span>
          </div>
          <a href="{base_url}/tailoring/" class="btn-primary" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.75rem 1.75rem;">
            <span>Explore Governance Sizing Tiers &amp; Deliverable Lists &rarr;</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Honest Boundaries & Scope (Moved down before footer) -->
    <section class="boundaries-section" style="background-color: var(--bg-card); border-top: 1px solid var(--border-color);">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">Honest Boundaries &amp; Scope</h2>
          <p class="section-desc">Understand exactly what Tasleemat provides and what it does not do.</p>
        </div>
        <div class="boundaries-grid">
          <div class="boundary-card provides">
            <h3><span>✅</span> What Tasleemat Provides</h3>
            <ul class="boundary-list">
              <li><strong>114 Canonical Deliverables:</strong> Reusable markdown templates in English and Arabic so teams never start from blank sheets.</li>
              <li><strong>Practitioner Guidance &amp; Examples:</strong> Step-by-step authoring guides, completed realistic examples, and bilingual glossaries.</li>
              <li><strong>Governance Sizing &amp; Tailoring:</strong> Structured tailoring rules across 3 Sizing Tiers and 5 Delivery Archetype Packs.</li>
              <li><strong>Machine-Readable Contracts:</strong> 114 companion JSON Schemas (Draft 2020-12) for automated validation.</li>
              <li><strong>Developer &amp; AI Assistant Integration:</strong> Native Python SDK, CLI (<code>tasleemat</code>), and Model Context Protocol (MCP) server.</li>
            </ul>
          </div>
          <div class="boundary-card limits">
            <h3><span>❌</span> What Tasleemat Does Not Do</h3>
            <ul class="boundary-list">
              <li><strong>Not a Live PMO Application:</strong> Does not host or execute project tracking workflows, dashboards, or scheduling engines.</li>
              <li><strong>Not an Approval Authority:</strong> Does not replace project steering committees, sponsors, or governance gates.</li>
              <li><strong>Not a Certification Authority:</strong> Does not issue compliance seals, audits, or legal certifications.</li>
              <li><strong>Not an Autonomous Project Agent:</strong> Does not autonomously make executive or contractual decisions.</li>
              <li><strong>Not a Shared Database:</strong> Does not store your confidential project deliverables or sensitive operational data.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
    """

    return render_html_page(
        title="Bilingual Project Deliverable Library & Toolkit",
        content=content,
        lang="en",
        active_nav="home",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/",
        description="Tasleemat is an open bilingual library of 114 project management deliverables, practitioner guides, companion JSON schemas (Draft 2020-12), and developer automation tools (Python SDK, CLI, MCP).",
        canonical_url="https://fakhr.me/Tasleemat/",
    )


def generate_home_ar(base_url: str = "/Tasleemat") -> str:
    """Generates the Arabic home page."""
    stages_cards = "\n".join([
        f"""<a href="{base_url}/ar/deliverables/?phase={p['code']}" class="stage-card">
          <div class="stage-badge">{p['icon']} المرحلة {p['code']}</div>
          <div class="stage-name">{p['name_ar']}</div>
          <div class="stage-desc">{p['desc_ar']}</div>
          <div class="stage-count">{p['count']} تسليمة &larr;</div>
        </a>"""
        for p in PHASES_DATA
    ])

    content = f"""
    <section class="hero-section">
      <div class="container">
        <div class="hero-pill">
          <span>🛡️ تسليمات معتمدة ثنائية اللغة وأدوات مساندة</span>
        </div>
        <h1 class="hero-title">مكتبة تسليمات إدارة المشاريع ثنائية اللغة ومجموعة الأدوات</h1>
        <p class="hero-subtitle">
          114 تسليمة معيارية للمشاريع، أدلة تطبيق عملية، مخططات JSON متوافقة (Draft 2020-12)،
          وأدوات أتمتة للممارسين، ومكاتب إدارة المشاريع (PMO)، والمطورين، ونماذج الذكاء الاصطناعي.
        </p>
        <div class="hero-actions">
          <a href="{base_url}/ar/deliverables/" class="btn-primary">
            🔍 استكشف 114 تسليمة
          </a>
          <a href="{base_url}/ar/start/" class="btn-secondary">
            🚀 ابدأ هنا (3 مسارات تطبيق)
          </a>
        </div>
        <div class="devhunt-badge-wrap">
          <a href="https://devhunt.org/tool/tasleemat" target="_blank" title="tasleemat on DevHunt" class="devhunt-badge devhunt-dark"><img src="https://devhunt.org/badge/tasleemat.svg" alt="tasleemat - Featured on DevHunt" width="220" height="54" /></a>
          <a href="https://devhunt.org/tool/tasleemat" target="_blank" title="tasleemat on DevHunt" class="devhunt-badge devhunt-light"><img src="https://devhunt.org/badge/tasleemat.svg?theme=light" alt="tasleemat - Featured on DevHunt" width="220" height="54" /></a>
        </div>
      </div>
    </section>

    <!-- Lifecycle Map in Arabic -->
    <section class="boundaries-section" style="background-color: var(--bg-card); border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color);">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">8 مراحل في دورة حياة المشروع</h2>
          <p class="section-desc">من مواءمة المحفظة الاستراتيجية وحتى التخطيط والتنفيذ والمراقبة والإغلاق النهائي.</p>
        </div>
        <div class="stages-grid">
          {stages_cards}
        </div>
      </div>
    </section>

    <!-- Governance Tiers & Packs in Arabic -->
    <section class="boundaries-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">مستويات الحوكمة وحزم المنهجيات</h2>
          <p class="section-desc">مواءمة دقة الحوكمة مع حجم المشروع، مستوى المخاطر، ومنهجية التنفيذ.</p>
        </div>
        <div class="grid-cards">
          <div class="card">
            <div class="card-title">🏢 المستوى 1: المشاريع الكبرى والاستراتيجية</div>
            <div class="card-desc">
              للمشاريع التي تتجاوز قيمتها 40 مليون ريال / 10 ملايين دولار، أو ذات المخاطر التنظيمية العالية والتحولات المؤسسية.
            </div>
            <div class="tag-list">
              <span class="tag tier">35–50 تسليمة</span>
              <span class="tag">لجنة توجيهية</span>
              <span class="tag">بوابات مرحلية صارمة</span>
            </div>
          </div>
          <div class="card">
            <div class="card-title">⚖️ المستوى 2: المشاريع القياسية</div>
            <div class="card-desc">
              للمشاريع بين 4 إلى 40 مليون ريال / 1 إلى 10 ملايين دولار، والفرق متعددة الوظائف، والمبادرات الإدارية المستقرة.
            </div>
            <div class="tag-list">
              <span class="tag tier">18–25 تسليمة</span>
              <span class="tag">مراجعة مكتب إدارة المشاريع</span>
              <span class="tag">حوكمة متوازنة</span>
            </div>
          </div>
          <div class="card">
            <div class="card-title">⚡ المستوى 3: المشاريع الرشيقة والمصغرة</div>
            <div class="card-desc">
              للمشاريع الأقل من 4 ملايين ريال / 1 مليون دولار، ذات المخاطر المحدودة، والتحسينات الداخلية السريعة.
            </div>
            <div class="tag-list">
              <span class="tag tier">7–9 تسليمات</span>
              <span class="tag">اعتماد الراعي</span>
              <span class="tag">أقل قدر من الهدر الإداري</span>
            </div>
          </div>
        </div>

        <div style="margin-top: 2.5rem; text-align: center;">
          <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">حزم المنهجيات المعيارية</h3>
          <div style="display: flex; gap: 0.75rem; justify-content: center; flex-wrap: wrap; margin-bottom: 1.75rem;">
            <span class="tag pack">التسليم العام (General)</span>
            <span class="tag pack">المنهجيات الرشيقة (Agile)</span>
            <span class="tag pack">الذكاء الاصطناعي (AI)</span>
            <span class="tag pack">المنهجية التنبؤية (Predictive)</span>
            <span class="tag pack">المنهجية الهجينة (Hybrid)</span>
          </div>
          <a href="{base_url}/ar/tailoring/" class="btn-primary" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.75rem 1.75rem;">
            <span>استعراض مستويات الحوكمة وقوائم التسليمات التفصيلية &larr;</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Honest Boundaries & Scope in Arabic (Moved down before footer) -->
    <section class="boundaries-section" style="background-color: var(--bg-card); border-top: 1px solid var(--border-color);">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">حدود ونطاق مشروع تسليمات</h2>
          <p class="section-desc">تعرّف بدقة على ما توفره مكتبة تسليمات وما تخرج عن نطاقه.</p>
        </div>
        <div class="boundaries-grid">
          <div class="boundary-card provides">
            <h3><span>✅</span> ما توفره مكتبة تسليمات</h3>
            <ul class="boundary-list">
              <li><strong>114 تسليمة معيارية:</strong> قوالب بتنسيق Markdown باللغتين العربية والإنجليزية لإنهاء مشكلة البدء من صفحات فارغة.</li>
              <li><strong>أدلة توجيهية وأمثلة واقعية:</strong> أدلة إرشادية لكل تسليمة، أمثلة مكتملة واقعية، ومعاجم مصطلحات ثنائية متخصصة.</li>
              <li><strong>تحديد الحجم وتخصيص الحوكمة:</strong> قواعد تخصيص واضحة عبر 3 مستويات حوكمة و5 حزم منهجية للتسليم.</li>
              <li><strong>عقود بيانات رقمية منضبطة:</strong> 114 مخطط JSON متوافق مع معيار Draft 2020-12 للتحقق الآلي من جودة البيانات.</li>
              <li><strong>تكامل المطورين ومساعدي الذكاء الاصطناعي:</strong> مكتبة بايثون رسمية، أمر تشغيل (<code>tasleemat</code>)، وخادم MCP قياسي.</li>
            </ul>
          </div>
          <div class="boundary-card limits">
            <h3><span>❌</span> ما لا تقدمه مكتبة تسليمات</h3>
            <ul class="boundary-list">
              <li><strong>ليست نظاماً إلكترونياً حياً لإدارة المشاريع:</strong> لا تستضيف مهام المشاريع ولا تحتوي لوحات تحكم تفاعلية للمتابعة اليومية.</li>
              <li><strong>ليست سلطة اعتماد أو موافقة:</strong> لا تغني عن اللجان التوجيهية، والرعاة، وبوابات المراجعة المؤسسية.</li>
              <li><strong>ليست جهة تدقيق أو شهادات:</strong> لا تصدر أختام امتثال قانوني أو شهادات تدقيق إلزامية.</li>
              <li><strong>ليست وكيلاً ذكياً ذاتي القرار:</strong> لا تتخذ قرارات تعاقدية أو تنفيذية نيابة عن مدير المشروع أو المنظمة.</li>
              <li><strong>ليست قاعدة بيانات مشتركة:</strong> لا تقوم بحفظ أو استضافة وثائق مشاريعك السرية أو بياناتك الحساسة.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
    """

    return render_html_page(
        title="مكتبة تسليمات إدارة المشاريع ومجموعة الأدوات",
        content=content,
        lang="ar",
        active_nav="home",
        base_url=base_url,
        alt_lang_url=f"{base_url}/",
        description="تسليمات: مكتبة معيارية مفتوحة ثنائية اللغة تضم 114 تسليمة لإدارة المشاريع، أدلة تطبيق عملية، قوالب Markdown، مخططات JSON متوافقة، ومجموعة أدوات للمطورين وخادم MCP.",
        canonical_url="https://fakhr.me/Tasleemat/ar/",
    )
