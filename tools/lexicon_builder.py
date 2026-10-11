"""tools/lexicon_builder.py
Generates the dedicated, comprehensive Bilingual PMO Terminology Lexicon page
with 164+ standardized deliverables, core PMI terms, AI governance, and RACI roles.
"""

import json
import html as pyhtml
import pathlib

def get_standalone_lexicon_html(docs_dir: pathlib.Path, rel_root: str = "./") -> str:
    docs_dir = pathlib.Path(docs_dir)
    lex_json_path = docs_dir / "LEXICON.json"
    forms_raw = []
    if lex_json_path.exists():
        with open(lex_json_path, "r", encoding="utf-8") as f:
            forms_raw = json.load(f).get("forms", [])

    lex_md_path = docs_dir / "LEXICON.md"
    tables = []
    if lex_md_path.exists():
        with open(lex_md_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        curr = []
        for line in lines:
            if line.strip().startswith("|"):
                curr.append(line.strip())
            else:
                if curr:
                    tables.append(curr)
                    curr = []
        if curr:
            tables.append(curr)

    def parse_md_table(rows):
        if len(rows) < 3:
            return []
        header = [c.strip() for c in rows[0].split("|")[1:-1]]
        data = []
        for r in rows[2:]:
            cols = [c.strip() for c in r.split("|")[1:-1]]
            if cols:
                data.append(dict(zip(header, cols)))
        return data

    t_pmi = parse_md_table(tables[1]) if len(tables) > 1 else []
    t_ai = parse_md_table(tables[2]) if len(tables) > 2 else []
    t_roles = parse_md_table(tables[3]) if len(tables) > 3 else []

    lex_entries = []

    # 1. 114 Deliverables
    for item in forms_raw:
        code = item.get("code", "")
        en_name = item.get("en_name") or item.get("english_name", "")
        ar_name = item.get("ar_name") or item.get("arabic_name", "")
        en_path = item.get("en_dir") or item.get("en_path", "")
        group = item.get("group")
        if not group and en_path:
            parts = en_path.split("/")
            if len(parts) >= 3:
                group = parts[2]
        group = group or "00_Program_and_Portfolio_Management"
        phase_prefix = group[:2]
        group_clean = group.replace("_", " ")

        lex_entries.append({
            "type": "deliverable",
            "code": code,
            "term_en": en_name,
            "term_ar": ar_name,
            "definition": f"Standard institutional PMO deliverable bundle in {group_clean}. Includes Markdown template, OKF schema, and authoring practice guide.",
            "phase": phase_prefix,
            "category": "Deliverables (114)",
            "standard": "PMBOK 6/7/8 • ISO 21500 • DGA",
            "github": f"https://github.com/fakhruldeen/Tasleemat/tree/main/{en_path}" if en_path else "https://github.com/fakhruldeen/Tasleemat"
        })

    # 2. Core PMI Terms
    for item in t_pmi:
        term_en = item.get("English Term", "").replace("**", "").strip()
        term_ar = item.get("Official Arabic (PMI Standard)", "").strip()
        defin = item.get("Definition & Context", "").strip()
        lex_entries.append({
            "type": "pmi",
            "code": item.get("Acronym / Note", "-").replace("**", "").strip(),
            "term_en": term_en,
            "term_ar": term_ar,
            "definition": defin,
            "phase": "Core PMI",
            "category": "Core PMI / PMBOK",
            "standard": "PMI PMBOK® Standard",
            "github": "https://github.com/fakhruldeen/Tasleemat/blob/main/docs/LEXICON.md#3-core-pmi--pmbok-lexicon"
        })

    # 3. AI Governance Terms
    for item in t_ai:
        term_en = item.get("English Term", "").replace("**", "").strip()
        term_ar = item.get("Official Arabic Translation", "").strip()
        defin = item.get("Definition & Context", "").strip()
        lex_entries.append({
            "type": "ai",
            "code": "AI-GOV",
            "term_en": term_en,
            "term_ar": term_ar,
            "definition": defin,
            "phase": "02 (AI Ethics)",
            "category": "AI & Digital Governance",
            "standard": "NIST AI RMF / ISO 42001",
            "github": "https://github.com/fakhruldeen/Tasleemat/blob/main/docs/LEXICON.md#4-ai--digital-governance-terminology"
        })

    # 4. Roles & RACI
    for item in t_roles:
        term_en = item.get("Role (EN)", "").replace("**", "").strip()
        term_ar = item.get("المسمى الوظيفي بالعربية", "").strip()
        defin = item.get("Governance Responsibility & Templates Signed", "").strip()
        lex_entries.append({
            "type": "role",
            "code": "RACI",
            "term_en": term_en,
            "term_ar": term_ar,
            "definition": f"Sign-off responsibilities: {defin}",
            "phase": "Governance",
            "category": "Roles & Governance RACI",
            "standard": "RACI Matrix / PMO Governance",
            "github": "https://github.com/fakhruldeen/Tasleemat/blob/main/docs/LEXICON.md#5-governance-roles--sign-off-responsibilities"
        })

    rows_html = []
    for e in lex_entries:
        cat_badge_cls = {
            "Deliverables (114)": "bg-secondary/15 text-secondary border border-secondary/30",
            "Core PMI / PMBOK": "bg-primary-container text-on-primary",
            "AI & Digital Governance": "bg-tertiary-fixed-dim/20 text-tertiary-fixed-dim border border-tertiary-fixed-dim/40",
            "Roles & Governance RACI": "bg-surface-container-high text-on-surface"
        }.get(e["category"], "bg-surface-container text-on-surface-variant")

        search_text = f"{e['code']} {e['term_en']} {e['term_ar']} {e['definition']} {e['phase']} {e['category']} {e['standard']}".lower()

        r = f"""<tr class="hover:bg-surface-container/50 transition-colors lexicon-row" data-category="{pyhtml.escape(e['category'])}" data-phase="{pyhtml.escape(e['phase'])}" data-search="{pyhtml.escape(search_text)}">
  <td class="py-space-md px-space-md">
    <div class="font-semibold text-on-surface">{pyhtml.escape(e['term_en'])}</div>
    <div class="flex items-center gap-1.5 mt-0.5">
      <span class="font-label-code text-badge-caps px-1.5 py-0.5 rounded bg-surface-container-high text-on-surface font-bold">{pyhtml.escape(e['code'])}</span>
      <span class="font-label-code text-badge-caps px-1.5 py-0.5 rounded {cat_badge_cls}">{pyhtml.escape(e['category'])}</span>
    </div>
  </td>
  <td class="py-space-md px-space-md text-right" dir="rtl">
    <div class="font-headline-sm text-on-surface font-bold">{pyhtml.escape(e['term_ar'])}</div>
    <span class="block font-label-code text-badge-caps text-on-surface-variant font-normal mt-0.5">{pyhtml.escape(e['standard'])}</span>
  </td>
  <td class="py-space-md px-space-md text-on-surface-variant max-w-md text-body-sm leading-relaxed">
    {pyhtml.escape(e['definition'])}
  </td>
  <td class="py-space-md px-space-md whitespace-nowrap">
    <span class="px-2 py-1 rounded bg-surface-container text-on-surface-variant font-label-code text-xs font-semibold">{pyhtml.escape(e['phase'])}</span>
  </td>
  <td class="py-space-md px-space-md whitespace-nowrap font-label-code text-xs text-right">
    <a class="inline-flex items-center gap-1 px-2.5 py-1 rounded bg-surface-container text-secondary hover:bg-surface-container-high hover:underline transition" href="{pyhtml.escape(e['github'])}" target="_blank" rel="noreferrer" title="Source Specification">
      <span>Spec</span>
      <span class="material-symbols-outlined text-[13px]">open_in_new</span>
    </a>
  </td>
</tr>"""
        rows_html.append(r)

    rendered_rows = "\n".join(rows_html)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>Bilingual PMO Terminology Lexicon (المعجم الثنائي الموحد) | Tasleemat</title>
  <link rel="icon" type="image/png" href="{rel_root}img/logo.png"/>
  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            primary: "#1b2a4a",
            "on-primary": "#f8f9fa",
            "primary-container": "#2c3e66",
            secondary: "#006a61",
            "on-secondary": "#ffffff",
            "secondary-container": "#86f2e4",
            background: "#f8f9fa",
            "on-background": "#2c3e66",
            surface: "#f8f9fa",
            "on-surface": "#2c3e66",
            "surface-container-lowest": "#ffffff",
            "surface-container-low": "#edf2f7",
            "surface-container": "#e2e8f0",
            "surface-container-high": "#cbd5e1",
            "outline-variant": "#94a3b8",
            "tertiary-fixed-dim": "#a25b00"
          }},
          spacing: {{
            "space-xs": "4px", "space-sm": "8px", "space-md": "16px",
            "space-lg": "24px", "space-xl": "32px", "space-2xl": "48px"
          }}
        }}
      }}
    }};
  </script>
</head>
<body class="bg-background text-on-surface font-sans antialiased">
  <!-- Top Navigation Header -->
  <header class="fixed top-0 left-0 right-0 z-50 bg-surface-container-lowest/90 backdrop-blur-md border-b border-surface-container-high/80">
    <div class="max-w-7xl mx-auto px-4 md:px-6 h-16 flex items-center justify-between gap-4">
      <div class="flex items-center gap-3 cursor-pointer" onclick="window.location.href='{rel_root}index.html'">
        <img alt="Tasleemat Logo" class="h-8 w-auto object-contain" src="{rel_root}img/logo.png"/>
        <div class="flex flex-col">
          <span class="font-bold text-on-surface text-base leading-tight">Tasleemat PMO</span>
          <span class="text-xs text-secondary font-medium" dir="rtl">المعجم الموحد لإدارة المشاريع</span>
        </div>
      </div>
      <nav class="hidden md:flex items-center gap-6 text-sm font-medium text-on-surface-variant">
        <a class="hover:text-on-surface transition-colors" href="{rel_root}index.html">Overview</a>
        <a class="hover:text-on-surface transition-colors" href="{rel_root}catalog/en/index.html">114 Templates</a>
        <a class="hover:text-on-surface transition-colors" href="{rel_root}governance.html">Stage-Gates & RACI</a>
        <a class="hover:text-on-surface transition-colors" href="{rel_root}developer.html">Developer & CLI</a>
        <a class="text-secondary font-bold" href="{rel_root}LEXICON.html">Bilingual Lexicon</a>
      </nav>
      <div class="flex items-center gap-2">
        <a href="{rel_root}README_AR.html" class="inline-flex items-center gap-1 px-3 py-1.5 rounded-lg border border-outline-variant/60 bg-surface-container-low text-xs font-semibold text-on-surface hover:bg-surface-container transition-colors">
          <span>🇸🇦</span><span>العربية</span>
        </a>
        <a class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant text-xs font-semibold border border-outline-variant/40 hover:bg-surface-container-high hover:text-on-surface transition-colors" href="https://github.com/fakhruldeen/Tasleemat" target="_blank" rel="noreferrer">
          <span>★</span><span>Star 2</span>
        </a>
        <a href="https://github.com/fakhruldeen" target="_blank" rel="noreferrer" title="Mohamed Fakhruldeen (GitHub / LinkedIn / Website)">
          <img alt="Mohamed Fakhruldeen" class="w-8 h-8 rounded-full object-cover border border-outline-variant/40" src="https://avatars.githubusercontent.com/u/1162549?v=4"/>
        </a>
      </div>
    </div>
  </header>

  <main class="w-full pt-16 min-h-screen">
    <!-- Hero Banner -->
    <section class="w-full bg-surface-container-low border-b border-surface-container-high py-12">
      <div class="max-w-7xl mx-auto px-4 md:px-6 space-y-4">
        <div class="flex flex-wrap items-center gap-2">
          <span class="px-2.5 py-0.5 rounded-full bg-secondary text-on-secondary font-mono text-xs font-bold uppercase tracking-wider">PMI PMBOK® 6/7/8 • ISO 21500 • DGA</span>
          <span class="px-2.5 py-0.5 rounded-full bg-surface-container text-on-surface-variant font-mono text-xs font-semibold">164+ Standard Terms</span>
          <span class="px-2.5 py-0.5 rounded-full bg-surface-container text-on-surface-variant font-mono text-xs font-semibold">Full Bilingual Parity</span>
        </div>
        <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6">
          <div class="space-y-2 max-w-3xl">
            <h1 class="text-3xl md:text-4xl font-extrabold text-on-surface tracking-tight">
              Bilingual PMO Terminology Lexicon
              <span class="block text-secondary text-2xl font-bold mt-1" dir="rtl">المعجم الثنائي الموحد لمصطلحات وتسليمات إدارة المشاريع</span>
            </h1>
            <p class="text-on-surface-variant text-sm md:text-base leading-relaxed">
              Standardized Arabic and English vocabulary across all 114 project deliverable bundles, Earned Value Analysis (EVA) equations, NIST AI Risk Management Framework, and RACI governance authorities.
            </p>
          </div>
          <div class="flex items-center gap-2 shrink-0">
            <a href="{rel_root}catalog/en/index.html" class="px-4 py-2.5 rounded-xl bg-secondary text-on-secondary font-mono text-xs font-bold hover:opacity-95 transition shadow-sm flex items-center gap-1.5">
              <span class="material-symbols-outlined text-sm">grid_view</span>
              <span>Explore 114 Deliverables</span>
            </a>
            <a href="https://github.com/fakhruldeen/Tasleemat/blob/main/docs/LEXICON.md" target="_blank" rel="noreferrer" class="px-4 py-2.5 rounded-xl bg-surface-container text-on-surface font-mono text-xs font-bold hover:bg-surface-container-high transition border border-outline-variant/40 flex items-center gap-1.5">
              <span class="material-symbols-outlined text-sm">code</span>
              <span>Markdown Source</span>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Filter & Search Controls Section -->
    <section class="max-w-7xl mx-auto px-4 md:px-6 py-8 space-y-6">
      <div class="bg-surface-container-lowest rounded-2xl p-6 border border-outline-variant/30 shadow-sm space-y-4">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <!-- Search Bar -->
          <div class="relative flex-1">
            <span class="material-symbols-outlined absolute left-3.5 top-3 text-outline-variant text-lg">search</span>
            <input id="lexicon-search" oninput="filterLexicon()" type="text" placeholder="Search EN / عربي (e.g. WBS, ميثاق, EVA, Risk, Sponsor, AI)..." class="w-full bg-surface-container-low text-on-surface placeholder:text-outline-variant border border-outline-variant/50 rounded-xl pl-10 pr-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-secondary focus:bg-white transition-all"/>
          </div>
          <div class="flex items-center gap-2 text-xs font-mono text-on-surface-variant">
            <span>Showing:</span>
            <span id="active-count-label" class="px-2 py-1 rounded bg-surface-container font-bold text-secondary">164 Terms</span>
          </div>
        </div>

        <!-- Filter Pills by Category -->
        <div class="flex flex-wrap items-center gap-2 pt-2 border-t border-surface-container-high/60">
          <span class="text-xs font-mono text-on-surface-variant mr-1">Category:</span>
          <button class="cat-btn px-3 py-1.5 rounded-lg bg-secondary text-on-secondary text-xs font-mono font-bold transition-all shadow-xs" data-category="all" onclick="setCategoryFilter('all')">All Categories (164)</button>
          <button class="cat-btn px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant text-xs font-mono font-medium hover:bg-surface-container-high transition-all" data-category="Deliverables (114)" onclick="setCategoryFilter('Deliverables (114)')">Deliverables (114)</button>
          <button class="cat-btn px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant text-xs font-mono font-medium hover:bg-surface-container-high transition-all" data-category="Core PMI / PMBOK" onclick="setCategoryFilter('Core PMI / PMBOK')">Core PMI / PMBOK (33)</button>
          <button class="cat-btn px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant text-xs font-mono font-medium hover:bg-surface-container-high transition-all" data-category="AI & Digital Governance" onclick="setCategoryFilter('AI & Digital Governance')">AI Governance (6)</button>
          <button class="cat-btn px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant text-xs font-mono font-medium hover:bg-surface-container-high transition-all" data-category="Roles & Governance RACI" onclick="setCategoryFilter('Roles & Governance RACI')">Roles & RACI (11)</button>
        </div>
      </div>

      <!-- Lexicon Table Container -->
      <div class="w-full overflow-x-auto bg-surface-container-lowest rounded-2xl border border-outline-variant/30 shadow-sm">
        <table class="w-full text-left border-collapse" id="lexicon-table">
          <thead>
            <tr class="bg-surface-container border-b border-surface-container-high font-mono text-xs uppercase tracking-wider text-on-surface-variant">
              <th class="py-4 px-4 font-bold">English Standard Term & Code</th>
              <th class="py-4 px-4 text-right font-bold" dir="rtl">المصطلح العربي المعتمد</th>
              <th class="py-4 px-4 font-bold">Standard Definition & Application</th>
              <th class="py-4 px-4 font-bold">Phase</th>
              <th class="py-4 px-4 text-right font-bold">Reference</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-surface-container-high text-sm font-sans" id="lexicon-tbody">
            {rendered_rows}
          </tbody>
        </table>
        <!-- Empty State -->
        <div id="lexicon-empty" class="hidden p-12 text-center space-y-2">
          <span class="material-symbols-outlined text-outline-variant text-4xl">search_off</span>
          <p class="font-bold text-on-surface text-base">No matching terminology found</p>
          <p class="text-xs text-on-surface-variant">Try typing acronyms (e.g., WBS, EVA, SPI, CPI), Arabic roots, or reset filters.</p>
          <button onclick="resetFilters()" class="mt-2 px-3 py-1.5 rounded-lg bg-surface-container text-xs font-mono text-secondary hover:bg-surface-container-high font-bold transition">Reset Search & Filters</button>
        </div>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="w-full bg-surface-container-low border-t border-surface-container-high py-12 mt-16">
    <div class="max-w-7xl mx-auto px-4 md:px-6 flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="flex items-center gap-3">
        <img alt="Tasleemat Logo" class="h-8 w-auto object-contain" src="{rel_root}img/logo.png"/>
        <div>
          <span class="font-bold text-on-surface text-sm">Tasleemat PMO Framework</span>
          <p class="text-xs text-on-surface-variant">Bilingual Project Management Operating System (MIT Licensed)</p>
        </div>
      </div>
      <div class="flex items-center gap-6 text-xs text-on-surface-variant font-mono">
        <a href="{rel_root}index.html" class="hover:underline">Home</a>
        <a href="{rel_root}catalog/en/index.html" class="hover:underline">Catalog</a>
        <a href="{rel_root}governance.html" class="hover:underline">Stage-Gates</a>
        <a href="{rel_root}developer.html" class="hover:underline">Developer</a>
        <a href="https://github.com/fakhruldeen/Tasleemat" target="_blank" rel="noreferrer" class="hover:underline">GitHub</a>
      </div>
    </div>
  </footer>

  <script>
    let activeCategory = 'all';

    function setCategoryFilter(cat) {{
      activeCategory = cat;
      document.querySelectorAll('.cat-btn').forEach(btn => {{
        if (btn.getAttribute('data-category') === cat) {{
          btn.className = 'cat-btn px-3 py-1.5 rounded-lg bg-secondary text-on-secondary text-xs font-mono font-bold transition-all shadow-xs';
        }} else {{
          btn.className = 'cat-btn px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant text-xs font-mono font-medium hover:bg-surface-container-high transition-all';
        }}
      }});
      filterLexicon();
    }}

    function normalizeText(txt) {{
      if (!txt) return '';
      return txt
        .replace(/[إأآا]/g, 'ا')
        .replace(/ة/g, 'ه')
        .replace(/ي/g, 'ي')
        .replace(/ى/g, 'ي')
        .toLowerCase()
        .trim();
    }}

    function filterLexicon() {{
      const searchInput = document.getElementById('lexicon-search');
      const query = normalizeText(searchInput ? searchInput.value : '');
      const rows = document.querySelectorAll('.lexicon-row');
      let visibleCount = 0;

      rows.forEach(r => {{
        const rowSearch = normalizeText(r.getAttribute('data-search') || '');
        const rowCategory = r.getAttribute('data-category') || '';

        const matchesCat = (activeCategory === 'all' || rowCategory === activeCategory);
        const matchesQuery = (!query || rowSearch.includes(query));

        if (matchesCat && matchesQuery) {{
          r.style.display = '';
          visibleCount++;
        }} else {{
          r.style.display = 'none';
        }}
      }});

      const counter = document.getElementById('active-count-label');
      if (counter) {{
        counter.innerText = visibleCount + ' Terms';
      }}

      const empty = document.getElementById('lexicon-empty');
      if (empty) {{
        if (visibleCount === 0) {{
          empty.classList.remove('hidden');
        }} else {{
          empty.classList.add('hidden');
        }}
      }}
    }}

    function resetFilters() {{
      document.getElementById('lexicon-search').value = '';
      setCategoryFilter('all');
    }}
  </script>
</body>
</html>"""
