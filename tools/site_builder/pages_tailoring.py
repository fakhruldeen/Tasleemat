"""tools/site_builder/pages_tailoring.py
Dedicated Governance Sizing Tiers & Delivery Archetype Packs page for Tasleemat (English & Arabic).
Provides comprehensive lists of deliverables for Tier 1, Tier 2, and Tier 3 across
General, Agile, AI, Predictive, and Hybrid delivery packs, with direct links to deliverable detail pages.
"""

import html
import tasleemat
from tools.tasleemat_cli import TIER_PACKS
from tools.site_builder.theme import render_html_page

TIER_METADATA = {
    "1": {
        "title_en": "Tier 1: Mega & Strategic Projects",
        "title_ar": "المستوى 1: المشاريع الكبرى والاستراتيجية",
        "icon": "🏢",
        "budget_en": "> $10M USD / > 40M SAR",
        "budget_ar": "> 40 مليون ريال / > 10 ملايين دولار",
        "risk_en": "High / Critical Organizational Risk",
        "risk_ar": "مخاطر استراتيجية وتنظيمية حرجة وعالية",
        "governance_en": "Steering Committee, C-Suite Sponsor, Formal Stage Gates",
        "governance_ar": "لجنة توجيهية، راعٍ تنفيذي، بوابات مرحلية رسمية صارمة",
        "desc_en": "Designed for multi-year enterprise transformations, high-scrutiny government programs, and mission-critical investments.",
        "desc_ar": "مصمم لمشاريع التحول المؤسسي الكبرى متعددة السنوات، والبرامج الحكومية عالية الحساسية، والاستثمارات الحيوية."
    },
    "2": {
        "title_en": "Tier 2: Standard Enterprise Projects",
        "title_ar": "المستوى 2: المشاريع القياسية للمؤسسات",
        "icon": "⚖️",
        "budget_en": "$1M – $10M USD / 4M – 40M SAR",
        "budget_ar": "4 – 40 مليون ريال / 1 – 10 ملايين دولار",
        "risk_en": "Moderate / Departmental & Cross-Functional Risk",
        "risk_ar": "مخاطر متوسطة، مبادرات مشتركة بين الإدارات",
        "governance_en": "PMO Director, Department Head, Balanced Stage Gates",
        "governance_ar": "مدير مكتب إدارة المشاريع، رئيس قطاع، بوابات مراجعة متوازنة",
        "desc_en": "The default balanced operating model for standard departmental and multi-functional initiatives requiring structured governance without undue overhead.",
        "desc_ar": "النموذج المتوازن الافتراضي للمشاريع الإدارية والمبادرات الوظيفية المشتركة التي تتطلب انضباطاً دون هدر إداري."
    },
    "3": {
        "title_en": "Tier 3: Lean & Fast-Track Projects",
        "title_ar": "المستوى 3: المشاريع الرشيقة والمصغرة السريعة",
        "icon": "⚡",
        "budget_en": "< $1M USD / < 4M SAR",
        "budget_ar": "< 4 ملايين ريال / < 1 مليون دولار",
        "risk_en": "Low / Well-Understood Operational Scope",
        "risk_ar": "مخاطر محدودة، نطاق عمل واضح ومعروف تشغيلياً",
        "governance_en": "Direct Project Sponsor Sign-Off, Lightweight Reviews",
        "governance_ar": "اعتماد مباشر من راعي المشروع، مراجعات موجزة وسريعة",
        "desc_en": "Optimized for internal improvements, proof-of-concept prototypes, and fast operational enhancements where speed of execution is paramount.",
        "desc_ar": "مخصص للمشاريع الداخلية السريعة، وتجارب إثبات المفهوم، والتحسينات التشغيلية التي تتطلب سرعة الإنجاز."
    }
}

PACK_METADATA = {
    "general": {
        "title_en": "General Delivery Pack",
        "title_ar": "حزمة التسليم العام",
        "icon": "📦",
        "desc_en": "Comprehensive baseline delivery deliverables covering all standard PMO knowledge areas.",
        "desc_ar": "الحزمة الشاملة الأساسية التي تغطي كافة مجالات المعرفة المعتادة لمكتب إدارة المشاريع."
    },
    "agile": {
        "title_en": "Agile & Scrum Delivery Pack",
        "title_ar": "حزمة المنهجيات الرشيقة (Agile)",
        "icon": "🔄",
        "desc_en": "Iterative delivery deliverables emphasizing sprint backlogs, burn-up/down tracking, and retrospective improvements.",
        "desc_ar": "تسليمات العمل التكراري التي تركز على سجلات السبرنت، تتبع معدل الإنجاز، ومخرجات المراجعات الدورية."
    },
    "ai": {
        "title_en": "AI & Machine Learning Delivery Pack",
        "title_ar": "حزمة مشاريع الذكاء الاصطناعي (AI)",
        "icon": "🤖",
        "desc_en": "Specialized deliverables for AI ethics impact, model governance cards, dataset cards, and technical debt registers.",
        "desc_ar": "تسليمات متخصصة لأخلاقيات الذكاء الاصطناعي، بطاقات حوكمة النماذج، بطاقات مجموعات البيانات، والديون التقنية."
    },
    "predictive": {
        "title_en": "Predictive / Waterfall Delivery Pack",
        "title_ar": "حزمة المنهجية التنبؤية (Waterfall)",
        "icon": "📐",
        "desc_en": "Sequential delivery deliverables emphasizing baseline scope, schedule, earned value analysis, and formal change control.",
        "desc_ar": "تسليمات المسار التتابعي التي تركز على ضبط خطوط الأساس، تحليل القيمة المكتسبة (EVA)، وإدارة التغيير الصارمة."
    },
    "hybrid": {
        "title_en": "Hybrid Framework Delivery Pack",
        "title_ar": "حزمة المنهجية الهجينة (Hybrid)",
        "icon": "🔀",
        "desc_en": "Blended governance combining executive stage-gate milestone oversight with agile sprint team execution.",
        "desc_ar": "مزيج حوكمة يجمع بين رقابة البوابات المرحلية للإدارة العليا والتنفيذ الرشيق المرن لفرق العمل."
    }
}


def _render_deliverable_card(art_id: str, art_dict: dict, lang: str, base_url: str) -> str:
    is_ar = lang == "ar"
    detail_url = f"{base_url}/deliverables/{art_id}/" if not is_ar else f"{base_url}/ar/deliverables/{art_id}/"
    name = art_dict.get("name_ar" if is_ar else "name_en", art_id)
    phase_code = art_dict.get("phase_code", "")
    phase_name = art_dict.get("phase_name_ar" if is_ar else "phase_name_en", "")

    return f"""
    <a href="{detail_url}" class="card" style="text-decoration: none; display: flex; flex-direction: column; justify-content: space-between; padding: 1.25rem; transition: transform 0.15s ease, box-shadow 0.15s ease; border-left: 4px solid var(--accent-blue);">
      <div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
          <span style="font-family: var(--font-mono); font-size: 0.8rem; font-weight: 700; color: var(--accent-blue); background: var(--accent-blue-bg); padding: 0.2rem 0.5rem; border-radius: 4px; border: 1px solid var(--accent-blue-border);">
            {html.escape(art_id)}
          </span>
          <span style="font-size: 0.75rem; color: var(--text-muted);">
            {"Phase" if not is_ar else "المرحلة"} {html.escape(phase_code)}
          </span>
        </div>
        <div style="font-weight: 700; font-size: 1rem; color: var(--text-main); margin-bottom: 0.35rem; line-height: 1.4;">
          {html.escape(name)}
        </div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">
          {html.escape(phase_name)}
        </div>
      </div>
      <div style="margin-top: 1rem; font-size: 0.82rem; font-weight: 600; color: var(--accent-blue); display: flex; align-items: center; gap: 0.35rem;">
        <span>{"View Deliverable &rarr;" if not is_ar else "عرض التسليمة &larr;"}</span>
      </div>
    </a>
    """


def generate_tailoring_en(base_url: str = "/Tasleemat") -> str:
    """Generates the English Governance Sizing Tiers & Delivery Packs page."""
    artifacts_map = {a.artifact_id: a for a in tasleemat.list_artifacts()}
    
    # Build Overview Matrix
    matrix_rows = []
    for tier_num in ["1", "2", "3"]:
        t_meta = TIER_METADATA[tier_num]
        counts = [len(TIER_PACKS[tier_num][p]) for p in ["general", "agile", "ai", "predictive", "hybrid"]]
        matrix_rows.append(f"""
        <tr>
          <td style="font-weight: 700; white-space: nowrap;">
            <a href="#tier-{tier_num}" style="color: var(--text-main); text-decoration: none;">
              {t_meta['icon']} {t_meta['title_en'].split(':')[0]}
            </a>
          </td>
          <td style="font-size: 0.85rem; color: var(--text-muted);">{t_meta['budget_en']}</td>
          <td style="text-align: center; font-weight: 600;">{counts[0]}</td>
          <td style="text-align: center; font-weight: 600;">{counts[1]}</td>
          <td style="text-align: center; font-weight: 600;">{counts[2]}</td>
          <td style="text-align: center; font-weight: 600;">{counts[3]}</td>
          <td style="text-align: center; font-weight: 600;">{counts[4]}</td>
          <td style="text-align: center;">
            <a href="#tier-{tier_num}" class="btn-utility" style="padding: 0.25rem 0.6rem; font-size: 0.8rem;">View Lists &rarr;</a>
          </td>
        </tr>
        """)
    matrix_html = "\n".join(matrix_rows)

    # Build Tier Sections
    tier_sections_html = []
    for tier_num in ["1", "2", "3"]:
        t_meta = TIER_METADATA[tier_num]
        
        # Build packs cards
        packs_html = []
        for pack_key in ["general", "agile", "ai", "predictive", "hybrid"]:
            p_meta = PACK_METADATA[pack_key]
            deliv_ids = TIER_PACKS[tier_num][pack_key]
            
            cards_html = "".join([
                _render_deliverable_card(art_id, vars(artifacts_map[art_id]) if art_id in artifacts_map else {}, "en", base_url)
                for art_id in deliv_ids
            ])
            
            packs_html.append(f"""
            <div id="tier-{tier_num}-{pack_key}" style="margin-top: 2rem; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 0.75rem; padding: 1.75rem;">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
                <div>
                  <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="font-size: 1.3rem;">{p_meta['icon']}</span>
                    <h4 style="font-size: 1.25rem; font-weight: 700; margin: 0; color: var(--text-main);">{p_meta['title_en']}</h4>
                    <span class="badge" style="background: var(--tag-bg); color: var(--tag-text); font-weight: 700; font-size: 0.8rem; padding: 0.2rem 0.6rem; border-radius: 9999px;">
                      {len(deliv_ids)} Deliverables
                    </span>
                  </div>
                  <p style="font-size: 0.9rem; color: var(--text-muted); margin-top: 0.35rem; margin-bottom: 0;">{p_meta['desc_en']}</p>
                </div>
                <div style="font-family: var(--font-mono); font-size: 0.8rem; background: var(--bg-main); padding: 0.35rem 0.75rem; border-radius: 6px; border: 1px solid var(--border-color);">
                  <code>tasleemat init --tier {tier_num} --pack {pack_key}</code>
                </div>
              </div>
              <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1rem;">
                {cards_html}
              </div>
            </div>
            """)

        tier_sections_html.append(f"""
        <section id="tier-{tier_num}" style="margin-top: 3.5rem; scroll-margin-top: 5rem;">
          <div class="card" style="padding: 2.25rem; border-top: 4px solid var(--accent-emerald);">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1.25rem; margin-bottom: 1.5rem;">
              <div>
                <div style="display: flex; align-items: center; gap: 0.6rem;">
                  <span style="font-size: 1.6rem;">{t_meta['icon']}</span>
                  <h2 style="font-size: 1.7rem; font-weight: 800; margin: 0; color: var(--text-main);">{t_meta['title_en']}</h2>
                </div>
                <p style="font-size: 1rem; color: var(--text-muted); margin-top: 0.5rem; max-width: 850px; line-height: 1.6;">
                  {t_meta['desc_en']}
                </p>
              </div>
            </div>

            <!-- Tier Governance Badges -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-bottom: 2rem; background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
              <div>
                <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.05em;">Budget Threshold</div>
                <div style="font-weight: 700; color: var(--text-main); font-size: 0.95rem; margin-top: 0.2rem;">{t_meta['budget_en']}</div>
              </div>
              <div>
                <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.05em;">Risk Profile</div>
                <div style="font-weight: 700; color: var(--text-main); font-size: 0.95rem; margin-top: 0.2rem;">{t_meta['risk_en']}</div>
              </div>
              <div>
                <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.05em;">Governance Body</div>
                <div style="font-weight: 700; color: var(--text-main); font-size: 0.95rem; margin-top: 0.2rem;">{t_meta['governance_en']}</div>
              </div>
            </div>

            <!-- Jump to Pack Nav Pills -->
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
              <span style="font-size: 0.85rem; font-weight: 700; align-self: center; margin-right: 0.5rem; color: var(--text-muted);">Quick Jump:</span>
              <a href="#tier-{tier_num}-general" class="btn-utility" style="font-size: 0.82rem; padding: 0.25rem 0.65rem;">📦 General ({len(TIER_PACKS[tier_num]['general'])})</a>
              <a href="#tier-{tier_num}-agile" class="btn-utility" style="font-size: 0.82rem; padding: 0.25rem 0.65rem;">🔄 Agile ({len(TIER_PACKS[tier_num]['agile'])})</a>
              <a href="#tier-{tier_num}-ai" class="btn-utility" style="font-size: 0.82rem; padding: 0.25rem 0.65rem;">🤖 AI ({len(TIER_PACKS[tier_num]['ai'])})</a>
              <a href="#tier-{tier_num}-predictive" class="btn-utility" style="font-size: 0.82rem; padding: 0.25rem 0.65rem;">📐 Predictive ({len(TIER_PACKS[tier_num]['predictive'])})</a>
              <a href="#tier-{tier_num}-hybrid" class="btn-utility" style="font-size: 0.82rem; padding: 0.25rem 0.65rem;">🔀 Hybrid ({len(TIER_PACKS[tier_num]['hybrid'])})</a>
            </div>

            <!-- Packs lists -->
            {"".join(packs_html)}
          </div>
        </section>
        """)

    all_tier_content = "\n".join(tier_sections_html)

    content = f"""
    <section class="hero-section" style="padding: 3.5rem 0 2.5rem;">
      <div class="container">
        <div class="hero-pill">
          <span>⚖️ Tailored Governance &amp; Methodology Packs</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.35rem; margin-top: 0.75rem;">
          Governance Sizing Tiers &amp; Delivery Packs
        </h1>
        <p class="hero-subtitle" style="max-width: 820px; margin: 0 auto; line-height: 1.7;">
          Not every project needs all 114 deliverables. Tasleemat provides structured tailoring profiles
          that balance governance rigor with operational speed according to project investment scale, risk, and delivery archetype.
        </p>
      </div>
    </section>

    <div class="container" style="margin-top: 2.5rem; margin-bottom: 5rem;">
      
      <!-- Sizing Matrix Card -->
      <div class="card" style="padding: 2rem; margin-bottom: 2.5rem;">
        <h3 style="font-size: 1.35rem; margin-bottom: 0.5rem; color: var(--text-main);">
          📊 Governance Sizing Matrix &amp; Deliverable Counts
        </h3>
        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">
          Compare deliverable counts across tiers and methodology packs. Click any tier to jump directly to its complete deliverable inventory.
        </p>
        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.92rem;">
            <thead>
              <tr style="border-bottom: 2px solid var(--border-color); background: var(--bg-main);">
                <th style="padding: 0.75rem 1rem;">Sizing Tier</th>
                <th style="padding: 0.75rem 1rem;">Budget Threshold</th>
                <th style="padding: 0.75rem 0.5rem; text-align: center;">📦 General</th>
                <th style="padding: 0.75rem 0.5rem; text-align: center;">🔄 Agile</th>
                <th style="padding: 0.75rem 0.5rem; text-align: center;">🤖 AI</th>
                <th style="padding: 0.75rem 0.5rem; text-align: center;">📐 Predictive</th>
                <th style="padding: 0.75rem 0.5rem; text-align: center;">🔀 Hybrid</th>
                <th style="padding: 0.75rem 1rem; text-align: center;">Explore</th>
              </tr>
            </thead>
            <tbody>
              {matrix_html}
            </tbody>
          </table>
        </div>
      </div>

      <!-- CLI & SDK Code Reference Card -->
      <div class="card" style="padding: 2rem; margin-bottom: 2.5rem; background: var(--bg-card); border-left: 4px solid var(--accent-blue);">
        <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--text-main);">
          ⚡ Programmatic Tailoring &amp; Scaffolding
        </h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 1rem;">
          Generate pre-populated project folders with tailored deliverables in one command or query them directly in Python:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem;">
          <div>
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted); margin-bottom: 0.35rem; text-transform: uppercase;">CLI Scaffolding Command</div>
            <pre style="margin: 0;"><code># Scaffold Tier 2 Agile Project
tasleemat init \\
  --tier 2 \\
  --pack agile \\
  --lang en \\
  --name "Customer Portal v2" \\
  --code "PRJ-2026-PORTAL" \\
  --out ./portal_project</code></pre>
          </div>
          <div>
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted); margin-bottom: 0.35rem; text-transform: uppercase;">Python SDK Function</div>
            <pre style="margin: 0;"><code>import tasleemat

# Query tailored deliverable IDs
deliverables = tasleemat.get_tailoring_profile(
    tier=2,
    pack="agile"
)
print(f"Tailored count: {{len(deliverables)}}")</code></pre>
          </div>
        </div>
      </div>

      <!-- Detailed Tiers Sections -->
      {all_tier_content}

    </div>
    """

    return render_html_page(
        title="Governance Sizing Tiers & Delivery Packs",
        content=content,
        lang="en",
        active_nav="tailoring",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/tailoring/",
        description="Governance Sizing Tiers (Tier 1 Mega, Tier 2 Standard, Tier 3 Lean) and Delivery Packs (General, Agile, AI, Predictive, Hybrid) with complete lists of deliverables.",
        canonical_url="https://fakhr.me/Tasleemat/tailoring/",
    )


def generate_tailoring_ar(base_url: str = "/Tasleemat") -> str:
    """Generates the Arabic Governance Sizing Tiers & Delivery Packs page."""
    artifacts_map = {a.artifact_id: a for a in tasleemat.list_artifacts()}
    
    # Build Overview Matrix
    matrix_rows = []
    for tier_num in ["1", "2", "3"]:
        t_meta = TIER_METADATA[tier_num]
        counts = [len(TIER_PACKS[tier_num][p]) for p in ["general", "agile", "ai", "predictive", "hybrid"]]
        matrix_rows.append(f"""
        <tr>
          <td style="font-weight: 700; white-space: nowrap;">
            <a href="#tier-{tier_num}" style="color: var(--text-main); text-decoration: none;">
              {t_meta['icon']} {t_meta['title_ar'].split(':')[0]}
            </a>
          </td>
          <td style="font-size: 0.85rem; color: var(--text-muted);">{t_meta['budget_ar']}</td>
          <td style="text-align: center; font-weight: 600;">{counts[0]}</td>
          <td style="text-align: center; font-weight: 600;">{counts[1]}</td>
          <td style="text-align: center; font-weight: 600;">{counts[2]}</td>
          <td style="text-align: center; font-weight: 600;">{counts[3]}</td>
          <td style="text-align: center; font-weight: 600;">{counts[4]}</td>
          <td style="text-align: center;">
            <a href="#tier-{tier_num}" class="btn-utility" style="padding: 0.25rem 0.6rem; font-size: 0.8rem;">عرض القوائم &larr;</a>
          </td>
        </tr>
        """)
    matrix_html = "\n".join(matrix_rows)

    # Build Tier Sections
    tier_sections_html = []
    for tier_num in ["1", "2", "3"]:
        t_meta = TIER_METADATA[tier_num]
        
        # Build packs cards
        packs_html = []
        for pack_key in ["general", "agile", "ai", "predictive", "hybrid"]:
            p_meta = PACK_METADATA[pack_key]
            deliv_ids = TIER_PACKS[tier_num][pack_key]
            
            cards_html = "".join([
                _render_deliverable_card(art_id, vars(artifacts_map[art_id]) if art_id in artifacts_map else {}, "ar", base_url)
                for art_id in deliv_ids
            ])
            
            packs_html.append(f"""
            <div id="tier-{tier_num}-{pack_key}" style="margin-top: 2rem; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 0.75rem; padding: 1.75rem;">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
                <div>
                  <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="font-size: 1.3rem;">{p_meta['icon']}</span>
                    <h4 style="font-size: 1.25rem; font-weight: 700; margin: 0; color: var(--text-main);">{p_meta['title_ar']}</h4>
                    <span class="badge" style="background: var(--tag-bg); color: var(--tag-text); font-weight: 700; font-size: 0.8rem; padding: 0.2rem 0.6rem; border-radius: 9999px;">
                      {len(deliv_ids)} تسليمة
                    </span>
                  </div>
                  <p style="font-size: 0.9rem; color: var(--text-muted); margin-top: 0.35rem; margin-bottom: 0;">{p_meta['desc_ar']}</p>
                </div>
                <div style="font-family: var(--font-mono); font-size: 0.8rem; background: var(--bg-main); padding: 0.35rem 0.75rem; border-radius: 6px; border: 1px solid var(--border-color); direction: ltr;">
                  <code>tasleemat init --tier {tier_num} --pack {pack_key} --lang ar</code>
                </div>
              </div>
              <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1rem;">
                {cards_html}
              </div>
            </div>
            """)

        tier_sections_html.append(f"""
        <section id="tier-{tier_num}" style="margin-top: 3.5rem; scroll-margin-top: 5rem;">
          <div class="card" style="padding: 2.25rem; border-top: 4px solid var(--accent-emerald);">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1.25rem; margin-bottom: 1.5rem;">
              <div>
                <div style="display: flex; align-items: center; gap: 0.6rem;">
                  <span style="font-size: 1.6rem;">{t_meta['icon']}</span>
                  <h2 style="font-size: 1.7rem; font-weight: 800; margin: 0; color: var(--text-main);">{t_meta['title_ar']}</h2>
                </div>
                <p style="font-size: 1rem; color: var(--text-muted); margin-top: 0.5rem; max-width: 850px; line-height: 1.6;">
                  {t_meta['desc_ar']}
                </p>
              </div>
            </div>

            <!-- Tier Governance Badges -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-bottom: 2rem; background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
              <div>
                <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.05em;">سقف الميزانية التقديرية</div>
                <div style="font-weight: 700; color: var(--text-main); font-size: 0.95rem; margin-top: 0.2rem;">{t_meta['budget_ar']}</div>
              </div>
              <div>
                <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.05em;">مستوى المخاطر</div>
                <div style="font-weight: 700; color: var(--text-main); font-size: 0.95rem; margin-top: 0.2rem;">{t_meta['risk_ar']}</div>
              </div>
              <div>
                <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.05em;">جهة الحوكمة والاعتماد</div>
                <div style="font-weight: 700; color: var(--text-main); font-size: 0.95rem; margin-top: 0.2rem;">{t_meta['governance_ar']}</div>
              </div>
            </div>

            <!-- Jump to Pack Nav Pills -->
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
              <span style="font-size: 0.85rem; font-weight: 700; align-self: center; margin-left: 0.5rem; color: var(--text-muted);">انتقال سريع للحزم:</span>
              <a href="#tier-{tier_num}-general" class="btn-utility" style="font-size: 0.82rem; padding: 0.25rem 0.65rem;">📦 التسليم العام ({len(TIER_PACKS[tier_num]['general'])})</a>
              <a href="#tier-{tier_num}-agile" class="btn-utility" style="font-size: 0.82rem; padding: 0.25rem 0.65rem;">🔄 الرشيقة ({len(TIER_PACKS[tier_num]['agile'])})</a>
              <a href="#tier-{tier_num}-ai" class="btn-utility" style="font-size: 0.82rem; padding: 0.25rem 0.65rem;">🤖 الذكاء الاصطناعي ({len(TIER_PACKS[tier_num]['ai'])})</a>
              <a href="#tier-{tier_num}-predictive" class="btn-utility" style="font-size: 0.82rem; padding: 0.25rem 0.65rem;">📐 التنبؤية ({len(TIER_PACKS[tier_num]['predictive'])})</a>
              <a href="#tier-{tier_num}-hybrid" class="btn-utility" style="font-size: 0.82rem; padding: 0.25rem 0.65rem;">🔀 الهجينة ({len(TIER_PACKS[tier_num]['hybrid'])})</a>
            </div>

            <!-- Packs lists -->
            {"".join(packs_html)}
          </div>
        </section>
        """)

    all_tier_content = "\n".join(tier_sections_html)

    content = f"""
    <section class="hero-section" style="padding: 3.5rem 0 2.5rem;">
      <div class="container">
        <div class="hero-pill">
          <span>⚖️ مصفوفة الحوكمة وحزم المنهجيات المعيارية</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.35rem; margin-top: 0.75rem;">
          مستويات الحوكمة وحزم المنهجيات
        </h1>
        <p class="hero-subtitle" style="max-width: 820px; margin: 0 auto; line-height: 1.7;">
          لا يحتاج كل مشروع إلى إعداد كافة الـ 114 تسليمة. يوفر إطار تسليمات مصفوفة تخصيص علمية منضبطة
          توازن بين متطلبات الرقابة وسرعة الإنجاز التشغيلي بحسب حجم استثمار المشروع، مستوى مخاطره، ومنهجية التسليم المعتمدة.
        </p>
      </div>
    </section>

    <div class="container" style="margin-top: 2.5rem; margin-bottom: 5rem;">
      
      <!-- Sizing Matrix Card -->
      <div class="card" style="padding: 2rem; margin-bottom: 2.5rem;">
        <h3 style="font-size: 1.35rem; margin-bottom: 0.5rem; color: var(--text-main);">
          📊 مصفوفة الحوكمة وأعداد التسليمات المعيارية
        </h3>
        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">
          قارن أعداد التسليمات المطلوبة عبر المستويات والحزم المنهجية المختلفة. انقر على أي مستوى للانتقال المباشر إلى قوائم تسليماته التفصيلية.
        </p>
        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; text-align: right; font-size: 0.92rem;">
            <thead>
              <tr style="border-bottom: 2px solid var(--border-color); background: var(--bg-main);">
                <th style="padding: 0.75rem 1rem;">مستوى الحوكمة</th>
                <th style="padding: 0.75rem 1rem;">سقف الميزانية</th>
                <th style="padding: 0.75rem 0.5rem; text-align: center;">📦 العام</th>
                <th style="padding: 0.75rem 0.5rem; text-align: center;">🔄 الرشيقة</th>
                <th style="padding: 0.75rem 0.5rem; text-align: center;">🤖 الذكاء الاصطناعي</th>
                <th style="padding: 0.75rem 0.5rem; text-align: center;">📐 التنبؤية</th>
                <th style="padding: 0.75rem 0.5rem; text-align: center;">🔀 الهجينة</th>
                <th style="padding: 0.75rem 1rem; text-align: center;">استعراض</th>
              </tr>
            </thead>
            <tbody>
              {matrix_html}
            </tbody>
          </table>
        </div>
      </div>

      <!-- CLI & SDK Code Reference Card -->
      <div class="card" style="padding: 2rem; margin-bottom: 2.5rem; background: var(--bg-card); border-right: 4px solid var(--accent-blue);">
        <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--text-main);">
          ⚡ التخصيص التلقائي وإنشاء بيئات العمل البرمجية
        </h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 1rem;">
          يمكن إنشاء بيئة عمل كاملة للمشروع تحتوي حصرياً على التسليمات المطلوبة بأمر واحد عبر الطرفية أو الاستعلام عنها برمجياً عبر بايثون:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem;">
          <div>
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted); margin-bottom: 0.35rem; text-transform: uppercase;">أمر إنشاء مجلد المشروع عبر الطرفية</div>
            <pre style="margin: 0; direction: ltr; text-align: left;"><code># إنشاء مجلد مشروع للمستوى 2 بمنهجية رشيقة باللغة العربية
tasleemat init \\
  --tier 2 \\
  --pack agile \\
  --lang ar \\
  --name "بوابة المستفيدين السحابية" \\
  --code "PRJ-2026-PORTAL" \\
  --out ./portal_project</code></pre>
          </div>
          <div>
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted); margin-bottom: 0.35rem; text-transform: uppercase;">استعلام برمجياً عبر مكتبة بايثون</div>
            <pre style="margin: 0; direction: ltr; text-align: left;"><code>import tasleemat

# جلب قائمة معرّفات التسليمات المخصصة
deliverables = tasleemat.get_tailoring_profile(
    tier=2,
    pack="agile"
)
print(f"عدد تسليمات الحزمة: {{len(deliverables)}}")</code></pre>
          </div>
        </div>
      </div>

      <!-- Detailed Tiers Sections -->
      {all_tier_content}

    </div>
    """

    return render_html_page(
        title="مستويات الحوكمة وحزم المنهجيات",
        content=content,
        lang="ar",
        active_nav="tailoring",
        base_url=base_url,
        alt_lang_url=f"{base_url}/tailoring/",
        description="مستويات الحوكمة وتحديد الحجم (المشاريع الكبرى، القياسية، الرشيقة) وحزم المنهجيات المعيارية مع قوائم التسليمات التفصيلية وروابطها المباشرة.",
        canonical_url="https://fakhr.me/Tasleemat/ar/tailoring/",
    )
