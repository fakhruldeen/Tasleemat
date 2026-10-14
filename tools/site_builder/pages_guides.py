"""tools/site_builder/pages_guides.py
Generates the Guides & Governance documentation pages in English and Arabic.
Features:
- Track A: Executive & Governance Guidance (Tailoring, Sizing, Stage Gates, RACI, Audits)
- Track B: Technical & Integration Architecture (Schemas, Prompts, LLM synthesis, Multi-Agent)
- 12 Core PMO Lifecycle Manuals directory with direct links to both English and Arabic versions
"""

from tools.site_builder.theme import render_html_page

CORE_MANUALS = [
    {
        "id": "01",
        "file": "01_getting_started.html",
        "title_en": "01. Getting Started & Architecture",
        "title_ar": "01. دليل البدء والهيكلية",
        "desc_en": "Foundational guide on directory structure, asset types, and project lifecycle alignment.",
        "desc_ar": "الدليل التأسيسي لهيكلية المجلدات، أنواع الأصول، ومواءمة دورة حياة المشروع."
    },
    {
        "id": "02",
        "file": "02_usage_guide.html",
        "title_en": "02. Practitioner Usage Guide",
        "title_ar": "02. دليل الاستخدام للممارسين",
        "desc_en": "How to select, adapt, fill, and maintain deliverables throughout project execution.",
        "desc_ar": "كيفية اختيار القوالب وتكييفها وتعبئتها وصيانتها خلال تنفيذ المشروع."
    },
    {
        "id": "03",
        "file": "03_pmo_policy_manual.html",
        "title_en": "03. PMO Policy & Operating Framework",
        "title_ar": "03. دليل سياسات وإجراءات مكتب إدارة المشاريع",
        "desc_en": "Governance charter, compliance guidelines, and organizational operational standards.",
        "desc_ar": "ميثاق الحوكمة، إرشادات الامتثال، والمعايير التشغيلية المعتمدة للمنظمة."
    },
    {
        "id": "04",
        "file": "04_stage_gates_and_governance.html",
        "title_en": "04. Stage Gates & Governance Reviews",
        "title_ar": "04. بوابات المراحل والمراجعات الحوكمية",
        "desc_en": "Stage-gate checklists, sign-off criteria, and escalation workflows across Phases 00 to 07.",
        "desc_ar": "قوائم مراجعة بوابات المراحل، معايير الاعتماد، ومسارات التصعيد عبر المراحل 00 إلى 07."
    },
    {
        "id": "05",
        "file": "05_tailoring_profiles.html",
        "title_en": "05. Tailoring Profiles & Sizing Matrices",
        "title_ar": "05. مصفوفات التخصيص وتحديد الحجم",
        "desc_en": "Comprehensive deliverable requirements for Tiers 1–3 and delivery archetype packs.",
        "desc_ar": "المتطلبات الإلزامية والموصى بها للمستويات 1–3 وحزم المنهجيات المختلفة."
    },
    {
        "id": "06",
        "file": "06_raci_authority_matrix.html",
        "title_en": "06. RACI & Authority Delegation Matrix",
        "title_ar": "06. مصفوفة الصلاحيات والمسؤوليات (RACI)",
        "desc_en": "Role delegations, approval rights, and accountability boundaries for all 114 deliverables.",
        "desc_ar": "تفويض الصلاحيات وحقوق الاعتماد والمسؤوليات لكافة الـ 114 تسليمة."
    },
    {
        "id": "07",
        "file": "07_document_dependencies.html",
        "title_en": "07. Document Dependencies & Information Flow",
        "title_ar": "07. شجرة الاعتماديات وتدفق البيانات",
        "desc_en": "Upstream feeder documents and downstream consuming deliverables across all phases.",
        "desc_ar": "وثائق المدخلات المغذية والتسليمات المعتمدة عليها عبر دورة حياة المشروع."
    },
    {
        "id": "08",
        "file": "08_ai_governance_framework.html",
        "title_en": "08. AI Governance & Ethics Framework",
        "title_ar": "08. إطار حوكمة وأخلاقيات الذكاء الاصطناعي",
        "desc_en": "Model cards, bias auditing, data privacy, and ethical risk mitigation for AI projects.",
        "desc_ar": "بطاقات النماذج، تدقيق الانحياز، خصوصية البيانات، وتخفيف المخاطر الأخلاقية لمشاريع الذكاء الاصطناعي."
    },
    {
        "id": "09",
        "file": "09_agile_hybrid_integration.html",
        "title_en": "09. Agile & Hybrid Delivery Integration",
        "title_ar": "09. التكامل مع المنهجيات الرشيقة والهجينة",
        "desc_en": "Integrating sprints, backlogs, user stories, and flow metrics with enterprise governance.",
        "desc_ar": "دمج دورات السبرنت، سجلات المتطلبات، وقصص المستخدم مع متطلبات الحوكمة المؤسسية."
    },
    {
        "id": "10",
        "file": "10_faq_and_troubleshooting.html",
        "title_en": "10. FAQ & Troubleshooting Guide",
        "title_ar": "10. الأسئلة الشائعة وحل المشكلات",
        "desc_en": "Practitioner answers on artifact conflicts, scope changes, and fast-track projects.",
        "desc_ar": "إجابات عملية حول تعارض الوثائق، تغييرات النطاق، والمشاريع ذات المسار السريع."
    },
    {
        "id": "11",
        "file": "11_tools_and_automation.html",
        "title_en": "11. Tools & Automation Playbook",
        "title_ar": "11. دليل الأدوات والأتمتة",
        "desc_en": "Automating deliverable generation, schema validation, and tool integration.",
        "desc_ar": "أتمتة توليد الوثائق، التحقق من المخططات، والربط مع أدوات إدارة المشاريع."
    },
    {
        "id": "12",
        "file": "12_open_knowledge_framework.html",
        "title_en": "12. Open Knowledge Framework (OKF)",
        "title_ar": "12. إطار المعرفة المفتوحة (OKF)",
        "desc_en": "Open-source governance standards, contribution protocols, and licensing compliance.",
        "desc_ar": "معايير الحوكمة المفتوحة، بروتوكولات المساهمة، والامتثال للرخص المفتوحة."
    }
]


def generate_guides_en(base_url: str = "/Tasleemat") -> str:
    manuals_cards = "\n".join([
        f"""<div class="card" style="padding: 1.25rem;">
          <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-blue); margin-bottom: 0.35rem;">Manual {m['id']}</div>
          <div style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;"><a href="{base_url}/en/{m['file']}">{m['title_en']}</a></div>
          <div style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 0.75rem;">{m['desc_en']}</div>
          <div style="display: flex; gap: 0.75rem; font-size: 0.85rem; font-weight: 600;">
            <a href="{base_url}/en/{m['file']}">Read English &rarr;</a>
            <a href="{base_url}/ar/{m['file']}">العربية &larr;</a>
          </div>
        </div>"""
        for m in CORE_MANUALS
    ])

    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <div class="hero-pill">
          <span>📚 Practitioner &amp; Executive Knowledge</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.25rem;">Guides &amp; PMO Governance Library</h1>
        <p class="hero-subtitle">
          Comprehensive dual-track playbooks and 12 core lifecycle operational manuals.
        </p>
      </div>
    </section>

    <div class="container" style="margin-top: 3rem; margin-bottom: 4rem;">
      
      <!-- Dual-Track Playbooks -->
      <div style="margin-bottom: 3.5rem;">
        <h2 style="font-size: 1.6rem; margin-bottom: 0.75rem;">Dual-Track Audience Guides</h2>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
          Specialized guidance authored specifically for managerial leadership vs. technical engineering teams.
        </p>
        
        <div class="boundaries-grid">
          <div class="card" style="border-top: 4px solid var(--accent-emerald);">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">👔 Track A: Managerial &amp; PMO Leadership</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1rem;">
              Executive oversight, investment thresholds, stage-gate gating, RACI accountability, and risk mitigation.
            </p>
            <ul style="margin-left: 1.25rem; font-size: 0.9rem; color: var(--text-muted); display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.25rem;">
              <li><a href="{base_url}/en/managerial_stage_gates_playbook.html">Executive Stage-Gates Playbook</a></li>
              <li><a href="{base_url}/en/managerial_tailoring_and_sizing.html">Organizational Sizing &amp; Tailoring Rules</a></li>
              <li><a href="{base_url}/en/managerial_audit_and_benefits.html">Audit Readiness &amp; Benefit Realization</a></li>
              <li><a href="{base_url}/en/managerial_ai_risk_and_ethics.html">AI Risk &amp; Algorithmic Governance for Leaders</a></li>
            </ul>
          </div>

          <div class="card" style="border-top: 4px solid var(--accent-blue);">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">💻 Track B: Technical &amp; Systems Engineers</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1rem;">
              Schema contracts, CI/CD validation loops, LLM prompt engineering, and multi-agent system orchestration.
            </p>
            <ul style="margin-left: 1.25rem; font-size: 0.9rem; color: var(--text-muted); display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.25rem;">
              <li><a href="{base_url}/en/tech_schemas_and_validation_loops.html">JSON Schema Contracts &amp; Validation Loops</a></li>
              <li><a href="{base_url}/en/tech_cli_and_devops_automation.html">CLI DevOps Automation &amp; CI/CD Pipelines</a></li>
              <li><a href="{base_url}/en/tech_llm_synthesis_and_prompting.html">Deterministic LLM Prompting &amp; Synthesis</a></li>
              <li><a href="{base_url}/en/tech_agentic_and_multiagent_orchestration.html">Multi-Agent Systems &amp; MCP Orchestration</a></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 12 Core Manuals Grid -->
      <div>
        <h2 style="font-size: 1.6rem; margin-bottom: 0.75rem;">The 12 Core PMO Lifecycle Manuals</h2>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
          Complete bilingual manuals providing end-to-end guidance across all project management domains.
        </p>
        <div class="grid-cards">
          {manuals_cards}
        </div>
      </div>

    </div>
    """

    return render_html_page(
        title="Guides & PMO Governance Library",
        content=content,
        lang="en",
        active_nav="guides",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/guides/",
        description="The 12 Core PMO Lifecycle Manuals, Frameworks, Dual-Track Playbooks, and Governance Guides for Tasleemat in English and Arabic.",
        canonical_url="https://fakhr.me/Tasleemat/guides/",
    )


def generate_guides_ar(base_url: str = "/Tasleemat") -> str:
    manuals_cards = "\n".join([
        f"""<div class="card" style="padding: 1.25rem;">
          <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-blue); margin-bottom: 0.35rem;">الدليل {m['id']}</div>
          <div style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;"><a href="{base_url}/ar/{m['file']}">{m['title_ar']}</a></div>
          <div style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 0.75rem;">{m['desc_ar']}</div>
          <div style="display: flex; gap: 0.75rem; font-size: 0.85rem; font-weight: 600;">
            <a href="{base_url}/ar/{m['file']}">قراءة بالعربية &rarr;</a>
            <a href="{base_url}/en/{m['file']}">English &larr;</a>
          </div>
        </div>"""
        for m in CORE_MANUALS
    ])

    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <div class="hero-pill">
          <span>📚 مكتبة المعرفة والحوكمة المؤسسية</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.25rem;">الأدلة وحوكمة مكاتب إدارة المشاريع</h1>
        <p class="hero-subtitle">
          أدلة المسار المزدوج المتخصصة، والأدلة التشغيلية الـ 12 المعتمدة لدورة حياة المشروع.
        </p>
      </div>
    </section>

    <div class="container" style="margin-top: 3rem; margin-bottom: 4rem;">
      
      <!-- Dual-Track Playbooks AR -->
      <div style="margin-bottom: 3.5rem;">
        <h2 style="font-size: 1.6rem; margin-bottom: 0.75rem;">أدلة المسار المزدوج المتخصص</h2>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
          أدلة تخصصية موجهة للقيادات الإدارية وفرق الهندسة التقنية بلغة تلائم أهداف كل فئة.
        </p>
        
        <div class="boundaries-grid">
          <div class="card" style="border-top: 4px solid var(--accent-emerald);">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">👔 المسار الإداري: قيادات الـ PMO والإدارة العليا</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1rem;">
              الإشراف الاستراتيجي، عتبات الاستثمار، بوابات المراجعة، مصفوفة صلاحيات RACI، وتخفيف المخاطر.
            </p>
            <ul style="margin-right: 1.25rem; font-size: 0.9rem; color: var(--text-muted); display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.25rem;">
              <li><a href="{base_url}/ar/managerial_stage_gates_playbook.html">دليل بوابات المراحل التنفيذية</a></li>
              <li><a href="{base_url}/ar/managerial_tailoring_and_sizing.html">قواعد تخصيص الحوكمة وحجم المشاريع</a></li>
              <li><a href="{base_url}/ar/managerial_audit_and_benefits.html">الجاهزية للتدقيق وتحقيق المنافع</a></li>
              <li><a href="{base_url}/ar/managerial_ai_risk_and_ethics.html">حوكمة مخاطر وأخلاقيات الذكاء الاصطناعي للقيادات</a></li>
            </ul>
          </div>

          <div class="card" style="border-top: 4px solid var(--accent-blue);">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">💻 المسار التقني: المطورون ومهندسو النظم</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1rem;">
              عقود المخططات، حلقات التحقق في CI/CD، هندسة موجهات الذكاء الاصطناعي، وتنسيق الوكلاء المتعددين.
            </p>
            <ul style="margin-right: 1.25rem; font-size: 0.9rem; color: var(--text-muted); display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.25rem;">
              <li><a href="{base_url}/ar/tech_schemas_and_validation_loops.html">عقود مخططات JSON وحلقات التحقق الذاتي</a></li>
              <li><a href="{base_url}/ar/tech_cli_and_devops_automation.html">أتمتة DevOps وأمر التشغيل في خطوط CI/CD</a></li>
              <li><a href="{base_url}/ar/tech_llm_synthesis_and_prompting.html">توجيه النماذج اللغوية وصياغة الوثائق بدقة</a></li>
              <li><a href="{base_url}/ar/tech_agentic_and_multiagent_orchestration.html">الأنظمة متعددة الوكلاء وتنسيق خادم MCP</a></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 12 Core Manuals Grid AR -->
      <div>
        <h2 style="font-size: 1.6rem; margin-bottom: 0.75rem;">الأدلة التشغيلية الـ 12 المعتمدة</h2>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
          أدلة ثنائية اللغة متكاملة توفر توجيهاً شاملاً عبر كافة مجالات إدارة المشاريع.
        </p>
        <div class="grid-cards">
          {manuals_cards}
        </div>
      </div>

    </div>
    """

    return render_html_page(
        title="الأدلة وحوكمة مكاتب إدارة المشاريع",
        content=content,
        lang="ar",
        active_nav="guides",
        base_url=base_url,
        alt_lang_url=f"{base_url}/guides/",
        description="الأدلة الرئيسية الـ 12 لمكتب إدارة المشاريع، أطر الحوكمة، وأدلة الممارس باللغتين العربية والإنجليزية.",
        canonical_url="https://fakhr.me/Tasleemat/ar/guides/",
    )
