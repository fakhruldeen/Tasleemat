"""tools/site_builder/build_site.py
Main static site compiler for the Tasleemat Public Portal (https://fakhr.me/Tasleemat/).
- Reads canonical metadata from `tasleemat.catalog` and source files immutably
- Compiles Home, Start Here, Deliverables Explorer, Guides, and Developers in EN and AR
- Compiles all 114 deliverable detail pages (228 total bilingual detail pages)
- Compiles the 12 Core Manuals and Dual-Track playbooks into `site/en/` and `site/ar/`
- Writes pre-rendered static files to `site/` ready for GitHub Pages deployment
"""

import os
import re
import sys
import json
import shutil
import pathlib
import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

import tasleemat
from tools.site_builder.theme import render_html_page
from tools.site_builder.pages_home import generate_home_en, generate_home_ar
from tools.site_builder.pages_start import generate_start_en, generate_start_ar
from tools.site_builder.pages_developers import generate_developers_en, generate_developers_ar
from tools.site_builder.pages_guides import generate_guides_en, generate_guides_ar
from tools.site_builder.pages_deliverables import generate_explorer_page, generate_detail_page


SITE_DIR = ROOT / "site"
DOCS_DIR = ROOT / "docs"
BASE_URL = "/Tasleemat"


def compile_manual_pages():
    """Compiles all markdown manuals and playbooks in docs/en and docs/ar into site/en and site/ar."""
    print("Compiling core manuals and playbooks...")
    for lang in ["en", "ar"]:
        src_dir = DOCS_DIR / lang
        out_dir = SITE_DIR / lang
        out_dir.mkdir(parents=True, exist_ok=True)
        
        for md_file in src_dir.glob("*.md"):
            with open(md_file, "r", encoding="utf-8") as f:
                raw_md = f.read()
                
            # Extract title if available from first H1
            title = md_file.stem.replace("_", " ").title()
            for line in raw_md.splitlines():
                if line.startswith("# "):
                    title = line[2:].strip()
            # Support callouts like > [!NOTE], > [!IMPORTANT], > [!WARNING]
            def repl_callout(m):
                kind = m.group(1).upper()
                body = m.group(2).strip()
                return f'<div class="admonition {kind.lower()}"><div class="admonition-title">{kind}</div><p>{body}</p></div>'

            processed_md = re.sub(r"^>\s*\[\!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*)$", repl_callout, raw_md, flags=re.MULTILINE | re.IGNORECASE)

            body_html = markdown.markdown(processed_md, extensions=['tables', 'fenced_code', 'toc', 'attr_list', 'admonition'])
            
            alt_lang = "ar" if lang == "en" else "en"
            alt_url = f"{BASE_URL}/{alt_lang}/{md_file.stem}.html"
            
            page_content = f"""
            <div class="container" style="margin-top: 2.5rem; margin-bottom: 4rem; max-width: 900px;">
              <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1.5rem;" aria-label="Breadcrumb">
                <a href="{BASE_URL}/" style="color: var(--text-muted);">{"Home" if lang == "en" else "الرئيسية"}</a> &gt; 
                <a href="{BASE_URL}/guides/" style="color: var(--text-muted);">{"Guides" if lang == "en" else "الأدلة"}</a> &gt; 
                <span style="color: var(--text-main); font-weight: 600;">{title}</span>
              </nav>

              <div class="card markdown-body" style="padding: 2.5rem; line-height: 1.8;">
                {body_html}
              </div>
            </div>
            """
            
            full_html = render_html_page(
                title=title,
                content=page_content,
                lang=lang,
                active_nav="guides",
                base_url=BASE_URL,
                alt_lang_url=alt_url,
            )
            
            out_file = out_dir / f"{md_file.stem}.html"
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(full_html)


def compile_all_deliverables(artifacts_summary):
    """Compiles all 114 deliverable detail pages in both English and Arabic."""
    print("Compiling 114 deliverable detail pages (228 bilingual variants)...")
    for summary in artifacts_summary:
        art_id = summary.artifact_id
        def_dict = tasleemat.get_artifact_definition(art_id)
        
        # Load asset contents
        template_en = tasleemat.get_artifact_asset(art_id, "template", lang="en")
        guide_en = tasleemat.get_artifact_asset(art_id, "guide", lang="en")
        example_en = tasleemat.get_artifact_asset(art_id, "example", lang="en")
        schema_text = tasleemat.get_artifact_asset(art_id, "schema", lang="en")
        
        template_ar = tasleemat.get_artifact_asset(art_id, "template", lang="ar")
        guide_ar = tasleemat.get_artifact_asset(art_id, "guide", lang="ar")
        example_ar = tasleemat.get_artifact_asset(art_id, "example", lang="ar")
        
        # English Detail Page
        en_out_dir = SITE_DIR / "deliverables" / art_id
        en_out_dir.mkdir(parents=True, exist_ok=True)
        html_en = generate_detail_page(
            art_meta=def_dict,
            template_content=template_en,
            guide_content=guide_en,
            example_content=example_en,
            schema_content=schema_text,
            lang="en",
            base_url=BASE_URL
        )
        with open(en_out_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(html_en)
            
        # Arabic Detail Page
        ar_out_dir = SITE_DIR / "ar" / "deliverables" / art_id
        ar_out_dir.mkdir(parents=True, exist_ok=True)
        html_ar = generate_detail_page(
            art_meta=def_dict,
            template_content=template_ar,
            guide_content=guide_ar,
            example_content=example_ar,
            schema_content=schema_text,
            lang="ar",
            base_url=BASE_URL
        )
        with open(ar_out_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(html_ar)


def build_site():
    print(f"--- Starting Tasleemat Public Website Build (Target: {SITE_DIR}) ---")
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Fetch catalog data
    artifacts_summary = tasleemat.list_artifacts()
    print(f"Loaded {len(artifacts_summary)} canonical deliverables from tasleemat.catalog.")
    
    # Prepare normalized list for the Explorer
    artifacts_data = []
    for s in artifacts_summary:
        def_dict = tasleemat.get_artifact_definition(s.artifact_id)
        packs_set = set()
        for t, pks in def_dict.get("tailoring", {}).get("packs_by_tier", {}).items():
            packs_set.update(pks)
        artifacts_data.append({
            "artifact_id": s.artifact_id,
            "prefix": s.prefix,
            "phase_code": s.phase_code,
            "phase_name_en": s.phase_name_en,
            "phase_name_ar": s.phase_name_ar,
            "name_en": s.name_en,
            "name_ar": s.name_ar,
            "tiers": s.tiers,
            "packs": sorted(list(packs_set))
        })
        
    # Save search index
    assets_dir = SITE_DIR / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    with open(assets_dir / "catalog-index.json", "w", encoding="utf-8") as f:
        json.dump(artifacts_data, f, indent=2, ensure_ascii=False)
        
    # 2. Compile Home Pages
    print("Generating Home pages (EN & AR)...")
    with open(SITE_DIR / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_home_en(BASE_URL))
    
    ar_dir = SITE_DIR / "ar"
    ar_dir.mkdir(parents=True, exist_ok=True)
    with open(ar_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_home_ar(BASE_URL))

    # 3. Compile Start Here Pages
    print("Generating Start Here pages (EN & AR)...")
    start_en_dir = SITE_DIR / "start"
    start_en_dir.mkdir(parents=True, exist_ok=True)
    with open(start_en_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_start_en(BASE_URL))
        
    start_ar_dir = SITE_DIR / "ar" / "start"
    start_ar_dir.mkdir(parents=True, exist_ok=True)
    with open(start_ar_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_start_ar(BASE_URL))

    # 4. Compile Deliverables Explorer Pages
    print("Generating Deliverables Explorer pages (EN & AR)...")
    deliv_en_dir = SITE_DIR / "deliverables"
    deliv_en_dir.mkdir(parents=True, exist_ok=True)
    with open(deliv_en_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_explorer_page(artifacts_data, lang="en", base_url=BASE_URL))
        
    deliv_ar_dir = SITE_DIR / "ar" / "deliverables"
    deliv_ar_dir.mkdir(parents=True, exist_ok=True)
    with open(deliv_ar_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_explorer_page(artifacts_data, lang="ar", base_url=BASE_URL))

    # 5. Compile Developers & AI Pages
    print("Generating Developers & AI pages (EN & AR)...")
    dev_en_dir = SITE_DIR / "developers"
    dev_en_dir.mkdir(parents=True, exist_ok=True)
    with open(dev_en_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_developers_en(BASE_URL))
        
    dev_ar_dir = SITE_DIR / "ar" / "developers"
    dev_ar_dir.mkdir(parents=True, exist_ok=True)
    with open(dev_ar_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_developers_ar(BASE_URL))

    # 6. Compile Guides & Governance Pages
    print("Generating Guides & Governance landing pages (EN & AR)...")
    guides_en_dir = SITE_DIR / "guides"
    guides_en_dir.mkdir(parents=True, exist_ok=True)
    with open(guides_en_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_guides_en(BASE_URL))
        
    guides_ar_dir = SITE_DIR / "ar" / "guides"
    guides_ar_dir.mkdir(parents=True, exist_ok=True)
    with open(guides_ar_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_guides_ar(BASE_URL))

    # 7. Compile Manuals & Playbooks
    compile_manual_pages()

    # 8. Compile All 114 Deliverable Detail Pages
    compile_all_deliverables(artifacts_summary)

    print("--- Build Finished Successfully! ---")


if __name__ == "__main__":
    build_site()
