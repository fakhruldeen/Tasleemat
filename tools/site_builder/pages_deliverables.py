"""tools/site_builder/pages_deliverables.py
Generates the Deliverables Explorer and Individual Deliverable Detail Pages in English and Arabic.
Features:
- Instant client-side search across 114 deliverables
- Multi-faceted filters (Lifecycle Phase 00-07, Governance Tiers 1-3, Methodology Packs 1-5)
- Pre-rendered Detail Pages with 5 tabs:
  1. Overview & Metadata
  2. Template (Bilingual Markdown)
  3. Practitioner Guide
  4. Real-world Example
  5. Companion JSON Schema (Draft 2020-12)
"""

import re
import json
import html
import markdown
from tools.site_builder.theme import render_html_page

def _extract_meta_chips(md_text: str):
    """Extract metadata chips (e.g. Project Sponsor, PM, Date, Budget) from example document."""
    txt = md_text
    if txt.startswith("---"):
        parts = txt.split("---", 2)
        if len(parts) >= 3:
            txt = parts[2]
            
    lines = txt.splitlines()[:50]
    tbl_lines = [l.strip() for l in lines if l.strip().startswith("|") and l.strip().endswith("|")]
    chips = []
    if tbl_lines:
        for l in tbl_lines:
            if re.match(r"^\|[\s\-:|]+\|$", l):
                continue
            cells = [c.strip() for c in l.split("|")[1:-1] if c.strip()]
            for cell in cells:
                clean_cell = cell.replace("**", "").replace("__", "").strip()
                if ":" in clean_cell or "：" in clean_cell:
                    delim = ":" if ":" in clean_cell else "："
                    k, v = clean_cell.split(delim, 1)
                    if k.strip() and v.strip():
                        chips.append((k.strip(), v.strip()))
    return chips

def strip_yaml_frontmatter(md_text: str) -> str:
    """Strips YAML frontmatter and token pointers from markdown documents."""
    txt = md_text
    txt = re.sub(r"^\s*<!--\s*\n*---\s*\n.*?\n---\s*\n*-->\s*", "", txt, flags=re.DOTALL)
    txt = re.sub(r"^\s*---\s*\n.*?\n---\s*", "", txt, flags=re.DOTALL)
    txt = re.sub(r"(<div class=\"lang-switch-bar\">.*?</div>\s*)\n*---\s*\n.*?\n---\s*", r"\1\n", txt, flags=re.DOTALL)
    return txt

def clean_guide_content(md_text: str) -> str:
    """Clean markdown frontmatter and outer HTML wrappers from user guides."""
    txt = strip_yaml_frontmatter(md_text)
    txt = re.sub(r"^\s*<div[^>]*>\s*", "", txt)
    opens = len(re.findall(r"<div\b", txt))
    closes = len(re.findall(r"</div>", txt))
    if closes > opens:
        txt = re.sub(r"\s*</div>\s*$", "", txt)
    txt = re.sub(r"^\s*<div[^>]*>\s*$", "", txt, flags=re.MULTILINE)
    txt = re.sub(r"^\s*</div>\s*$", "", txt, flags=re.MULTILINE)
    return txt.strip()

def clean_prompt_content(md_text: str) -> str:
    """Clean markdown frontmatter, wrappers, and convert HTML comment instructions to rendered blockquotes."""
    txt = strip_yaml_frontmatter(md_text)
    txt = re.sub(r"^\s*<div[^>]*>\s*", "", txt)
    opens = len(re.findall(r"<div\b", txt))
    closes = len(re.findall(r"</div>", txt))
    if closes > opens:
        txt = re.sub(r"\s*</div>\s*$", "", txt)
    txt = re.sub(r"^\s*<div[^>]*>\s*$", "", txt, flags=re.MULTILINE)
    txt = re.sub(r"^\s*</div>\s*$", "", txt, flags=re.MULTILINE)
    
    def _comment_to_blockquote(match):
        inner = match.group(1).strip()
        lines = inner.splitlines()
        return "\n".join(["> " + l for l in lines]) + "\n"
        
    txt = re.sub(r"<!--\s*(.*?)\s*-->", _comment_to_blockquote, txt, flags=re.DOTALL)
    return txt.strip()

def _clean_example_content(md_text: str) -> str:
    """Clean markdown frontmatter, wrappers, and remove redundant metadata table to render inside styled form container."""
    txt = strip_yaml_frontmatter(md_text)
            
    txt = re.sub(r"^\s*<div[^>]*>\s*", "", txt)
    opens = len(re.findall(r"<div\b", txt))
    closes = len(re.findall(r"</div>", txt))
    if closes > opens:
        txt = re.sub(r"\s*</div>\s*$", "", txt)
    
    lines = txt.splitlines()
    new_lines = []
    in_meta_table = False
    table_removed = False
    
    for idx, l in enumerate(lines):
        if idx < 45 and not table_removed:
            if l.strip().startswith("|") and l.strip().endswith("|"):
                in_meta_table = True
                continue
            elif in_meta_table:
                in_meta_table = False
                table_removed = True
                if l.strip() == "---":
                    continue
        new_lines.append(l)
    return "\n".join(new_lines).strip()



PHASES_NAME_MAP = {
    "00": ("00. Program & Portfolio Management", "00. إدارة البرامج والمحافظ"),
    "01": ("01. Business & Value Delivery", "01. الأعمال وتسليم القيمة"),
    "02": ("02. Project Approach & Tailoring", "02. منهجية المشروع والتخصيص"),
    "03": ("03. Initiating", "03. البدء والترخيص"),
    "04": ("04. Planning", "04. التخطيط المتكامل"),
    "05": ("05. Executing", "05. التنفيذ والتوجيه"),
    "06": ("06. Monitoring & Controlling", "06. المراقبة والتحكم"),
    "07": ("07. Closing", "07. الإغلاق والتسليم النهائي"),
}


def generate_explorer_page(artifacts_data: list, lang: str = "en", base_url: str = "/Tasleemat") -> str:
    is_ar = lang == "ar"
    title = "Deliverables Explorer (114)" if not is_ar else "مستكشف التسليمات (114)"
    
    # Pre-render deliverable cards into HTML for fast, accessible initial rendering
    cards_html = []
    for art in artifacts_data:
        art_id = art["artifact_id"]
        phase = art["phase_code"]
        name = art["name_ar"] if is_ar else art["name_en"]
        alt_name = art["name_en"] if is_ar else art["name_ar"]
        tiers = art.get("tiers", [])
        tier_str = ", ".join([f"Tier {t}" for t in tiers])
        
        detail_url = f"{base_url}/deliverables/{art_id}/" if not is_ar else f"{base_url}/ar/deliverables/{art_id}/"
        
        # Tags
        tags = []
        for t in tiers:
            tags.append(f'<span class="tag tier">{"المستوى" if is_ar else "Tier"} {t}</span>')
        
        packs = art.get("packs", [])
        for p in packs:
            tags.append(f'<span class="tag pack">{p}</span>')
            
        tags_rendered = " ".join(tags)
        
        card = f"""
        <div class="deliverable-card" data-id="{art_id}" data-phase="{phase}" data-tiers='{json.dumps(tiers)}' data-packs='{json.dumps(packs)}' data-name="{html.escape(name.lower())}" data-alt="{html.escape(alt_name.lower())}">
          <div class="deliverable-top">
            <span class="deliverable-id">{art_id}</span>
            <span style="font-size: 0.75rem; color: var(--text-muted);">{"مرحلة" if is_ar else "Phase"} {phase}</span>
          </div>
          <h3 class="deliverable-title"><a href="{detail_url}">{name}</a></h3>
          <div class="deliverable-title-alt">{alt_name}</div>
          <div class="tag-list">
            {tags_rendered}
          </div>
          <div class="deliverable-actions">
            <a href="{detail_url}" style="font-weight: 600; font-size: 0.85rem;">{"عرض التفاصيل" if is_ar else "View Details"} &rarr;</a>
            <span style="font-size: 0.75rem; color: var(--accent-emerald); font-weight: 600;">Draft 2020-12 Schema</span>
          </div>
        </div>
        """
        cards_html.append(card)
        
    cards_rendered = "\n".join(cards_html)

    # Explorer client-side script for instant filtering and search
    extra_scripts = """
    <script>
    (function() {
      const searchInput = document.getElementById('explorer-search');
      const phaseSelect = document.getElementById('filter-phase');
      const tierSelect = document.getElementById('filter-tier');
      const packSelect = document.getElementById('filter-pack');
      const countEl = document.getElementById('results-count');
      const cards = Array.from(document.querySelectorAll('.deliverable-card'));

      // Check URL search parameters on load (e.g. ?phase=04)
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.has('phase')) {
        phaseSelect.value = urlParams.get('phase');
      }
      if (urlParams.has('tier')) {
        tierSelect.value = urlParams.get('tier');
      }
      if (urlParams.has('pack')) {
        packSelect.value = urlParams.get('pack');
      }

      function filterCards() {
        const query = searchInput.value.trim().toLowerCase();
        const selectedPhase = phaseSelect.value;
        const selectedTier = tierSelect.value;
        const selectedPack = packSelect.value;

        let visibleCount = 0;

        cards.forEach(card => {
          const id = card.getAttribute('data-id').toLowerCase();
          const name = card.getAttribute('data-name');
          const alt = card.getAttribute('data-alt');
          const phase = card.getAttribute('data-phase');
          const tiers = JSON.parse(card.getAttribute('data-tiers') || '[]');
          const packs = JSON.parse(card.getAttribute('data-packs') || '[]');

          const matchesQuery = !query || id.includes(query) || name.includes(query) || alt.includes(query);
          const matchesPhase = !selectedPhase || phase === selectedPhase;
          const matchesTier = !selectedTier || tiers.includes(selectedTier);
          const matchesPack = !selectedPack || packs.includes(selectedPack);

          if (matchesQuery && matchesPhase && matchesTier && matchesPack) {
            card.style.display = 'flex';
            visibleCount++;
          } else {
            card.style.display = 'none';
          }
        });

        countEl.innerText = visibleCount;
      }

      searchInput.addEventListener('input', filterCards);
      phaseSelect.addEventListener('change', filterCards);
      tierSelect.addEventListener('change', filterCards);
      packSelect.addEventListener('change', filterCards);

      filterCards();
    })();
    </script>
    """

    content = f"""
    <section class="hero-section" style="padding: 2.5rem 0 1.5rem;">
      <div class="container">
        <h1 class="hero-title" style="font-size: 2.25rem;">{title}</h1>
        <p class="hero-subtitle" style="margin-bottom: 0;">
          {"Search, filter, and inspect templates, guides, examples, and schemas across all 114 project deliverables." if not is_ar else "ابحث وفلتر واستعرض القوالب والأدلة والأمثلة والمخططات لكافة تسليمات المشروع الـ 114."}
        </p>
      </div>
    </section>

    <div class="container" style="margin-top: 2rem; margin-bottom: 4rem;">
      <!-- Explorer Controls -->
      <div class="explorer-controls">
        <div class="search-input-wrapper">
          <input type="text" id="explorer-search" class="search-input" placeholder='{"Find by ID (e.g. PMO-04.14), title, or keyword..." if not is_ar else "ابحث برقم التسليمة (مثال: PMO-04.14) أو العنوان أو كلمة مفتاحية..."}' aria-label="Search Deliverables">
        </div>
        <div class="filters-row">
          <div class="filter-group">
            <label class="filter-label" for="filter-phase">{"Lifecycle Phase" if not is_ar else "مرحلة المشروع"}</label>
            <select id="filter-phase" class="filter-select">
              <option value="">{"All Phases (00-07)" if not is_ar else "كافة المراحل (00-07)"}</option>
              <option value="00">00. {"Program & Portfolio" if not is_ar else "إدارة البرامج والمحافظ"}</option>
              <option value="01">01. {"Business & Value" if not is_ar else "الأعمال والقيمة"}</option>
              <option value="02">02. {"Tailoring & Approach" if not is_ar else "التخصيص والمنهجية"}</option>
              <option value="03">03. {"Initiating" if not is_ar else "البدء والترخيص"}</option>
              <option value="04">04. {"Planning" if not is_ar else "التخطيط"}</option>
              <option value="05">05. {"Executing" if not is_ar else "التنفيذ"}</option>
              <option value="06">06. {"Monitoring & Controlling" if not is_ar else "المراقبة والتحكم"}</option>
              <option value="07">07. {"Closing" if not is_ar else "الإغلاق النهائي"}</option>
            </select>
          </div>

          <div class="filter-group">
            <label class="filter-label" for="filter-tier">{"Governance Tier" if not is_ar else "مستوى الحوكمة"}</label>
            <select id="filter-tier" class="filter-select">
              <option value="">{"All Tiers (1-3)" if not is_ar else "كافة المستويات (1-3)"}</option>
              <option value="1">{"Tier 1 (Mega > $10M / 40M SAR)" if not is_ar else "المستوى 1 (المشاريع الكبرى > 40 مليون ريال)"}</option>
              <option value="2">{"Tier 2 (Standard $1M-$10M)" if not is_ar else "المستوى 2 (القياسية 4-40 مليون ريال)"}</option>
              <option value="3">{"Tier 3 (Lean < $1M)" if not is_ar else "المستوى 3 (المشاريع الرشيقة < 4 ملايين ريال)"}</option>
            </select>
          </div>

          <div class="filter-group">
            <label class="filter-label" for="filter-pack">{"Delivery Pack" if not is_ar else "حزمة المنهجية"}</label>
            <select id="filter-pack" class="filter-select">
              <option value="">{"All Delivery Packs" if not is_ar else "كافة حزم المنهجيات"}</option>
              <option value="general">general</option>
              <option value="agile">agile</option>
              <option value="ai">ai</option>
              <option value="predictive">predictive</option>
              <option value="hybrid">hybrid</option>
            </select>
          </div>
        </div>

        <div class="explorer-status">
          <div>{"Showing" if not is_ar else "عرض"} <strong id="results-count">114</strong> {"of 114 deliverables" if not is_ar else "من أصل 114 تسليمة"}</div>
          <div style="font-size: 0.8rem;">{"All deliverables include EN & AR Markdown + Draft 2020-12 Schema" if not is_ar else "كافة التسليمات تتضمن قوالب ثنائية ومخطط Draft 2020-12"}</div>
        </div>
      </div>

      <!-- Deliverables Grid -->
      <div class="grid-cards" id="deliverables-grid">
        {cards_rendered}
      </div>
    </div>
    """

    desc = (
        "Interactive explorer across 114 canonical project management deliverables with multi-faceted filtering by lifecycle phase, sizing tier, and methodology pack."
        if not is_ar
        else "مستكشف تفاعلي لكافة الـ 114 تسليمة معيارية لإدارة المشاريع مع إمكانية الفلترة والبحث بحسب مرحلة دورة الحياة ومستوى الحوكمة وحزمة المنهجية."
    )
    canonical = f"https://fakhr.me{base_url}/deliverables/" if not is_ar else f"https://fakhr.me{base_url}/ar/deliverables/"

    return render_html_page(
        title=title,
        content=content,
        lang=lang,
        active_nav="deliverables",
        base_url=base_url,
        extra_scripts=extra_scripts,
        alt_lang_url=f"{base_url}/ar/deliverables/" if not is_ar else f"{base_url}/deliverables/",
        description=desc,
        canonical_url=canonical,
    )


def generate_detail_page(
    art_meta: dict,
    template_content: str,
    guide_content: str,
    example_content: str,
    schema_content: Any,
    prompt_content: str = "",
    fields_content: Any = None,
    lang: str = "en",
    base_url: str = "/Tasleemat"
) -> str:
    is_ar = lang == "ar"
    art_id = art_meta["artifact_id"]
    name = art_meta["name_ar"] if is_ar else art_meta["name_en"]
    alt_name = art_meta["name_en"] if is_ar else art_meta["name_ar"]
    phase_code = art_meta["phase_code"]
    phase_title = art_meta["phase_name_ar"] if is_ar else art_meta["phase_name_en"]
    
    tiers = art_meta.get("tailoring", {}).get("tiers", [])
    tier_badges = " ".join([f'<span class="tag tier">{"المستوى" if is_ar else "Tier"} {t}</span>' for t in tiers])
    
    packs_list = []
    for t, pks in art_meta.get("tailoring", {}).get("packs_by_tier", {}).items():
        packs_list.extend(pks)
    unique_packs = sorted(list(set(packs_list)))
    pack_badges = " ".join([f'<span class="tag pack">{p}</span>' for p in unique_packs])

    # Clean frontmatter and outer wrappers from template, guide, and prompt
    cleaned_template_content = strip_yaml_frontmatter(template_content)
    cleaned_guide_content = clean_guide_content(guide_content)
    cleaned_prompt_content = clean_prompt_content(prompt_content)

    # Convert markdown contents safely to rich HTML
    rendered_guide_html = markdown.markdown(cleaned_guide_content, extensions=['tables', 'fenced_code', 'toc', 'attr_list', 'admonition'])
    rendered_prompt_html = markdown.markdown(cleaned_prompt_content, extensions=['tables', 'fenced_code', 'toc', 'attr_list', 'admonition'])


    # Extract metadata chips and clean example markdown for rich form-viewer display
    example_chips = _extract_meta_chips(example_content)
    cleaned_example_md = _clean_example_content(example_content)
    rendered_example_html = markdown.markdown(cleaned_example_md, extensions=['tables', 'fenced_code', 'toc', 'attr_list', 'admonition'])

    # Render metadata chips block if available
    chips_html = ""
    if example_chips:
        chips_inner = "\n".join([
            f'<div class="doc-meta-chip"><div class="meta-chip-label">{html.escape(k)}</div><div class="meta-chip-val">{html.escape(v)}</div></div>'
            for k, v in example_chips
        ])
        chips_html = f'<div class="doc-meta-bar">\n{chips_inner}\n</div>'

    # Format Draft 2020-12 JSON schema cleanly
    if isinstance(schema_content, dict):
        formatted_schema_json = json.dumps(schema_content, indent=2, ensure_ascii=False)
    else:
        try:
            parsed_schema = json.loads(schema_content)
            formatted_schema_json = json.dumps(parsed_schema, indent=2, ensure_ascii=False)
        except Exception:
            formatted_schema_json = str(schema_content)

    formatted_fields_json = ""
    if fields_content and fields_content != schema_content:
        if isinstance(fields_content, dict):
            formatted_fields_json = json.dumps(fields_content, indent=2, ensure_ascii=False)
        else:
            try:
                parsed_f = json.loads(fields_content)
                formatted_fields_json = json.dumps(parsed_f, indent=2, ensure_ascii=False)
            except Exception:
                formatted_fields_json = str(fields_content)


    content = f"""
    <div class="container" style="margin-top: 2rem; margin-bottom: 4rem;">
      <!-- Breadcrumb -->
      <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1.5rem;" aria-label="Breadcrumb">
        <a href="{base_url}/" style="color: var(--text-muted);">{"Home" if not is_ar else "الرئيسية"}</a> &gt; 
        <a href="{base_url}/deliverables/" style="color: var(--text-muted);">{"Deliverables" if not is_ar else "التسليمات"}</a> &gt; 
        <span style="color: var(--text-main); font-weight: 600;">{art_id}</span>
      </nav>

      <!-- Deliverable Header Card -->
      <div class="card" style="padding: 2rem; margin-bottom: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem;">
          <div>
            <span class="deliverable-id" style="font-size: 1rem; padding: 0.25rem 0.6rem;">{art_id}</span>
            <span style="font-size: 0.9rem; color: var(--text-muted); margin-left: 0.75rem; margin-right: 0.75rem;">
              {"Phase" if not is_ar else "المرحلة"} {phase_code}: {phase_title}
            </span>
          </div>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            {tier_badges}
            {pack_badges}
          </div>
        </div>

        <h1 style="font-size: 2.25rem; font-weight: 800; margin-bottom: 0.5rem;">{name}</h1>
        <div style="font-size: 1.25rem; color: var(--text-muted); margin-bottom: 1.5rem;">{alt_name}</div>

        <!-- CLI Quick Command Bar -->
        <div style="background: var(--bg-main); border: 1px solid var(--border-color); border-radius: 0.375rem; padding: 0.75rem 1rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
          <code style="font-size: 0.85rem;">tasleemat asset {art_id} template --lang {'ar' if is_ar else 'en'}</code>
          <button class="btn-utility" onclick="navigator.clipboard.writeText('tasleemat asset {art_id} template --lang {'ar' if is_ar else 'en'}'); this.innerText='Copied!'; setTimeout(() => this.innerText='Copy Command', 2000);">
            {"Copy Command" if not is_ar else "نسخ الأمر"}
          </button>
        </div>
      </div>

      <!-- Tabbed Views -->
      <div class="tabs-container">
        <div class="tabs-nav" role="tablist">
          <button class="tab-btn active" onclick="switchTab(event, 'tab-overview')" role="tab" aria-selected="true">
            📋 {"Overview" if not is_ar else "نظرة عامة"}
          </button>
          <button class="tab-btn" onclick="switchTab(event, 'tab-template')" role="tab" aria-selected="false">
            📄 {"Template" if not is_ar else "القالب"}
          </button>
          <button class="tab-btn" onclick="switchTab(event, 'tab-guide')" role="tab" aria-selected="false">
            📖 {"User Guide" if not is_ar else "دليل المستخدم"}
          </button>
          <button class="tab-btn" onclick="switchTab(event, 'tab-prompt')" role="tab" aria-selected="false">
            🤖 {"LLM Prompt" if not is_ar else "مطالبة التوليد"}
          </button>
          <button class="tab-btn" onclick="switchTab(event, 'tab-example')" role="tab" aria-selected="false">
            💡 {"Example" if not is_ar else "مثال واقعي"}
          </button>
          <button class="tab-btn" onclick="switchTab(event, 'tab-schema')" role="tab" aria-selected="false">
            ⚙️ {"Schema" if not is_ar else "المخطط"}
          </button>
        </div>


        <!-- Tab 1: Overview -->
        <div id="tab-overview" class="tab-pane active" role="tabpanel">
          <h2 style="font-size: 1.4rem; margin-bottom: 1rem;">{"Deliverable Summary & Governance Boundaries" if not is_ar else "ملخص التسليمة وحدود الحوكمة"}</h2>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 2rem;">
            <div>
              <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">{"Lifecycle Phase Alignment" if not is_ar else "المرحلة في دورة حياة المشروع"}</h3>
              <p style="color: var(--text-muted); font-size: 0.95rem;">
                <strong>{"Phase" if not is_ar else "المرحلة"} {phase_code}:</strong> {phase_title}
              </p>
            </div>
            <div>
              <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">{"Sizing Tier Requirements" if not is_ar else "متطلبات مستوى الحجم"}</h3>
              <p style="color: var(--text-muted); font-size: 0.95rem;">
                {tier_badges}
              </p>
            </div>
          </div>

          <div style="border-top: 1px solid var(--border-color); padding-top: 1.5rem;">
            <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">{"Validation Contract" if not is_ar else "عقد التحقق الآلي"}</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1rem;">
              {"This deliverable conforms to a strict companion Draft 2020-12 JSON Schema for automated structural and semantic validation." if not is_ar else "ترتبط هذه التسليمة بمخطط JSON Schema متوافق مع معيار Draft 2020-12 لتمكين التحقق البنيوي والدلالي الآلي."}
            </p>
            <pre><code>tasleemat validate {art_id} ./completed_data.json</code></pre>
          </div>
        </div>

        <!-- Tab 2: Template -->
        <div id="tab-template" class="tab-pane" role="tabpanel">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <h2 style="font-size: 1.3rem;">{"Template Markdown (Bilingual)" if not is_ar else "قالب التسليمة بتنسيق Markdown"}</h2>
            <button class="btn-utility" id="btn-copy-template" onclick="copySnippet(this, 'code-template')">
              {"Copy Markdown" if not is_ar else "نسخ القالب"}
            </button>
          </div>
          <pre id="code-template"><code>{html.escape(cleaned_template_content)}</code></pre>
        </div>

        <!-- Tab 3: Guide -->
        <div id="tab-guide" class="tab-pane" role="tabpanel">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <h2 style="font-size: 1.3rem;">{"User Guide & Practitioner Instructions" if not is_ar else "دليل المستخدم وإرشادات الممارس"}</h2>
            <button class="btn-utility" onclick="window.print()">
              🖨️ {"Print Guide" if not is_ar else "طباعة الدليل"}
            </button>
          </div>
          <div class="markdown-body" style="line-height: 1.8;">
            {rendered_guide_html}
          </div>
        </div>

        <!-- Tab: LLM Prompt -->
        <div id="tab-prompt" class="tab-pane" role="tabpanel">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <h2 style="font-size: 1.3rem;">{"LLM Generation Prompt & Agent Instructions" if not is_ar else "مطالبة التوليد للذكاء الاصطناعي وتعليمات الوكيل"}</h2>
            <button class="btn-utility" onclick="navigator.clipboard.writeText(document.getElementById('code-prompt').innerText); this.innerText='{'Copied!' if not is_ar else 'تم النسخ!'}'; setTimeout(() => this.innerText='{'Copy Prompt' if not is_ar else 'نسخ المطالبة'}', 2000);">
              📋 {"Copy Prompt" if not is_ar else "نسخ المطالبة"}
            </button>
          </div>
          <div class="markdown-body" id="code-prompt" style="line-height: 1.8;">
            {rendered_prompt_html if rendered_prompt_html.strip() else f'<pre><code>{html.escape(cleaned_prompt_content)}</code></pre>'}
          </div>
        </div>

        <!-- Tab 4: Example -->
        <div id="tab-example" class="tab-pane" role="tabpanel">

          <!-- Deliverable Header Card & Badge Row -->
          <div class="deliverable-header-card">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
              <div class="deliverable-badge-row">
                <span class="badge badge-code">{art_id}</span>
                <span class="badge badge-phase">{"Phase" if not is_ar else "المرحلة"} {phase_code}: {phase_title}</span>
                <span class="badge badge-example">{"Realistic Case Study Benchmark" if not is_ar else "دراسة حالة واقعية مكتملة"}</span>
              </div>
              <div style="display: flex; gap: 0.5rem; align-items: center;">
                <button class="btn-utility" onclick="window.print()">
                  🖨️ {"Print / PDF" if not is_ar else "طباعة / PDF"}
                </button>
                <button class="btn-utility" onclick="navigator.clipboard.writeText(document.getElementById('example-prose').innerText); this.innerText='{'Copied!' if not is_ar else 'تم النسخ!'}'; setTimeout(() => this.innerText='{'Copy Text' if not is_ar else 'نسخ النص'}', 2000);">
                  📋 {"Copy Text" if not is_ar else "نسخ النص"}
                </button>
              </div>
            </div>
          </div>

          <!-- Document Control Meta Strip -->
          {chips_html}

          <!-- Form Sheet & Rendered Document Prose -->
          <div class="form-viewer-container markdown-body" id="example-prose" style="line-height: 1.85;">
            {rendered_example_html}
          </div>
        </div>


        <!-- Tab 5: Schema -->
        <div id="tab-schema" class="tab-pane" role="tabpanel">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
            <div>
              <h2 style="font-size: 1.3rem; margin-bottom: 0.25rem;">{"Draft 2020-12 JSON Schema" if not is_ar else "مخطط JSON Schema (معيار Draft 2020-12)"}</h2>
              <div style="font-size: 0.85rem; color: var(--text-muted);">
                {"Canonical machine-readable data contract for automated payload validation with tasleemat CLI." if not is_ar else "العقد الرقمي المعياري لتمكين التحقق الآلي من بيانات التسليمة بواسطة أداة tasleemat."}
              </div>
            </div>
            <div style="display: flex; gap: 0.5rem;">
              <button class="btn-utility" id="btn-copy-schema" onclick="copySnippet(this, 'code-schema')">
                {"Copy JSON Schema" if not is_ar else "نسخ المخطط"}
              </button>
            </div>
          </div>
          <pre id="code-schema"><code>{html.escape(formatted_schema_json)}</code></pre>
          {f'''
          <details style="margin-top: 1.5rem; background: var(--bg-main); border: 1px solid var(--border-color); border-radius: 0.5rem; padding: 1rem;">
            <summary style="font-size: 0.95rem; font-weight: 600; cursor: pointer; color: var(--accent-blue);">
              {"📋 Form Field Definitions Dictionary (Legacy Specification)" if not is_ar else "📋 قاموس تعريفات حقول النموذج (المواصفة التفصيلية)"}
            </summary>
            <div style="display: flex; justify-content: flex-end; margin-top: 0.75rem; margin-bottom: 0.5rem;">
              <button class="btn-utility" onclick="copySnippet(this, 'code-fields')">
                {"Copy Field Definitions" if not is_ar else "نسخ تعريفات الحقول"}
              </button>
            </div>
            <pre id="code-fields"><code>{html.escape(formatted_fields_json)}</code></pre>
          </details>
          ''' if formatted_fields_json else ''}
        </div>

      </div>
    </div>
    """

    # Generate tailored description for social sharing
    art_summary = (
        f"{art_id}: {name} - Comprehensive project deliverable template, practitioner guide, completed realistic example, and companion Draft 2020-12 JSON schema."
        if not is_ar
        else f"{art_id}: {name} - تسليمة معيارية للمشروع، دليل تطبيقي للممارس، مثال واقعي متكامل، ومخطط JSON للتحقق الآلي."
    )
    canonical = (
        f"https://fakhr.me{base_url}/deliverables/{art_id}/"
        if not is_ar
        else f"https://fakhr.me{base_url}/ar/deliverables/{art_id}/"
    )

    return render_html_page(
        title=f"{art_id} {name}",
        content=content,
        lang=lang,
        active_nav="deliverables",
        base_url=base_url,
        alt_lang_url=f"{base_url}/deliverables/{art_id}/" if is_ar else f"{base_url}/ar/deliverables/{art_id}/",
        description=art_summary,
        canonical_url=canonical,
    )
