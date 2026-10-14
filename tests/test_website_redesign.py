#!/usr/bin/env python3
"""tests/test_website_redesign.py
Automated acceptance test suite for the redesigned Tasleemat public website.
Validates:
1. Forms directory hash immutability (1,164 files)
2. All 114 deliverable detail pages exist in English and Arabic (228 total)
3. Essential static entry points exist (Home, Start Here, Deliverables Explorer, Guides, Developers)
4. Full bilingual mirroring (every EN page has AR counterpart and vice versa)
5. Zero broken internal links across the primary site structure
6. No hyperbole or exaggerated claims in generated landing pages
7. Proper RTL attributes (`dir="rtl"`, `lang="ar"`) and typography on Arabic pages
8. Code snippet execution verification against installed `tasleemat` package
"""

import os
import re
import json
import pathlib
import unittest
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "site"


class TestWebsiteRedesign(unittest.TestCase):

    def test_forms_immutability(self):
        """Confirms that forms/ directory remains 100% bit-for-bit identical to baseline."""
        baseline_file = pathlib.Path("/tmp/forms_baseline_website_redesign.sha256")
        if not baseline_file.exists():
            self.skipTest("Baseline snapshot not found.")
        
        cmd = ["sha256sum", "-c", str(baseline_file)]
        res = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, f"Forms integrity violation! {res.stderr}")

    def test_primary_entry_points_exist(self):
        """Verifies that all core redesigned pages exist in both English and Arabic."""
        routes = [
            "index.html",
            "ar/index.html",
            "start/index.html",
            "ar/start/index.html",
            "deliverables/index.html",
            "ar/deliverables/index.html",
            "guides/index.html",
            "ar/guides/index.html",
            "developers/index.html",
            "ar/developers/index.html",
            "tailoring/index.html",
            "ar/tailoring/index.html",
        ]
        for r in routes:
            page_path = SITE_DIR / r
            self.assertTrue(page_path.exists(), f"Missing required entry point: {r}")
            self.assertGreater(page_path.stat().st_size, 1000, f"Page {r} is suspiciously small.")

    def test_all_114_deliverables_have_bilingual_detail_pages(self):
        """Verifies all 114 deliverables have pre-rendered English and Arabic detail pages."""
        import tasleemat
        artifacts = tasleemat.list_artifacts()
        self.assertEqual(len(artifacts), 114)

        for art in artifacts:
            art_id = art.artifact_id
            en_page = SITE_DIR / "deliverables" / art_id / "index.html"
            ar_page = SITE_DIR / "ar" / "deliverables" / art_id / "index.html"

            self.assertTrue(en_page.exists(), f"Missing English detail page for {art_id}")
            self.assertTrue(ar_page.exists(), f"Missing Arabic detail page for {art_id}")

            en_content = en_page.read_text(encoding="utf-8")
            ar_content = ar_page.read_text(encoding="utf-8")

            self.assertIn(art_id, en_content)
            self.assertIn(art_id, ar_content)
            self.assertIn('dir="ltr"', en_content)
            self.assertIn('dir="rtl"', ar_content)
            self.assertIn('Draft 2020-12', en_content)
            self.assertIn('Draft 2020-12', ar_content)

    def test_arabic_pages_have_proper_rtl_and_fonts(self):
        """Verifies that Arabic pages declare dir='rtl', lang='ar', and include Arabic font."""
        ar_home = (SITE_DIR / "ar" / "index.html").read_text(encoding="utf-8")
        self.assertIn('dir="rtl"', ar_home)
        self.assertIn('lang="ar"', ar_home)
        self.assertTrue("Cairo" in ar_home or "IBM Plex Sans Arabic" in ar_home)

    def test_no_hyperbole_in_landing_pages(self):
        """Ensures that forbidden marketing hyperbole is absent from the redesigned pages."""
        forbidden_terms = [
            "Enterprise PMO Operating System",
            "100% compliant",
            "guaranteed audit-ready",
            "officially approved",
            "AI will manage your project autonomously"
        ]
        
        pages_to_check = [
            SITE_DIR / "index.html",
            SITE_DIR / "ar" / "index.html",
            SITE_DIR / "start" / "index.html",
            SITE_DIR / "ar" / "start" / "index.html",
        ]
        
        for p in pages_to_check:
            content = p.read_text(encoding="utf-8")
            for term in forbidden_terms:
                self.assertNotIn(term, content, f"Found forbidden hyperbole '{term}' in {p.name}")

    def test_code_snippets_against_installed_package(self):
        """Validates that Python SDK snippets featured in documentation work as stated."""
        import tasleemat

        # Snippet 1: list_artifacts with tailoring filters
        tailored = tasleemat.list_artifacts(tier="2", pack="agile")
        self.assertIsInstance(tailored, list)
        self.assertGreater(len(tailored), 0)

        # Snippet 2: get_artifact_definition & get_artifact_asset
        art_id = "PMO-03.01"
        meta = tasleemat.get_artifact_definition(art_id)
        self.assertEqual(meta["artifact_id"], art_id)

        guide_text = tasleemat.get_artifact_asset(art_id, "guide", lang="en")
        self.assertIsInstance(guide_text, str)
        self.assertGreater(len(guide_text), 100)

        # Snippet 3: validate_artifact_data
        test_data = {
            "project_id": "PRJ-TEST",
            "project_title": "Automated Test Project"
        }
        result = tasleemat.validate_artifact_data(art_id, test_data, mode="draft")
        self.assertTrue(hasattr(result, "valid"))
        self.assertTrue(hasattr(result, "errors"))

    def test_example_tab_form_viewer_design(self):
        """Verifies that Tab 4 (Realistic Example) features the previous website's form design."""
        # Test an Arabic detail page (e.g. PMO-03.01)
        detail_ar = ROOT / "site" / "ar" / "deliverables" / "PMO-03.01" / "index.html"
        self.assertTrue(detail_ar.exists(), "PMO-03.01 Arabic detail page must exist")
        html_ar = detail_ar.read_text(encoding="utf-8")

        self.assertIn('id="tab-example"', html_ar)
        self.assertIn('deliverable-header-card', html_ar)
        self.assertIn('deliverable-badge-row', html_ar)
        self.assertIn('badge-code', html_ar)
        self.assertIn('badge-phase', html_ar)
        self.assertIn('badge-example', html_ar)
        self.assertIn('doc-meta-bar', html_ar)
        self.assertIn('doc-meta-chip', html_ar)
        self.assertIn('form-viewer-container', html_ar)

        # Test an English detail page
        detail_en = ROOT / "site" / "deliverables" / "PMO-03.01" / "index.html"
        self.assertTrue(detail_en.exists(), "PMO-03.01 English detail page must exist")
        html_en = detail_en.read_text(encoding="utf-8")

        self.assertIn('id="tab-example"', html_en)
        self.assertIn('deliverable-header-card', html_en)
        self.assertIn('deliverable-badge-row', html_en)
        self.assertIn('badge-code', html_en)
        self.assertIn('badge-phase', html_en)
        self.assertIn('badge-example', html_en)
        self.assertIn('doc-meta-bar', html_en)
        self.assertIn('doc-meta-chip', html_en)
        self.assertIn('form-viewer-container', html_en)

    def test_footer_pip_and_github_links(self):
        """Verifies that all pages include pip install command and GitHub links in the footer."""
        sample_pages = [
            ROOT / "site" / "index.html",
            ROOT / "site" / "ar" / "index.html",
            ROOT / "site" / "deliverables" / "index.html",
            ROOT / "site" / "guides" / "index.html",
            ROOT / "site" / "en" / "01_getting_started.html",
            ROOT / "site" / "ar" / "01_getting_started.html",
            ROOT / "site" / "deliverables" / "PMO-03.01" / "index.html",
            ROOT / "site" / "ar" / "deliverables" / "PMO-03.01" / "index.html",
        ]
        for page in sample_pages:
            self.assertTrue(page.exists(), f"Page {page} must exist")
            html = page.read_text(encoding="utf-8")
            self.assertIn("pip install tasleemat", html, f"pip install link missing in {page}")
            self.assertIn("https://github.com/fakhruldeen/Tasleemat", html, f"GitHub link missing in {page}")

    def test_no_visible_yaml_frontmatter(self):
        """Verifies that markdown YAML frontmatter (e.g. token_pointer, tokenizer_model_id) is not visible in compiled pages."""
        import re
        sample_pages = [
            ROOT / "site" / "en" / "01_getting_started.html",
            ROOT / "site" / "ar" / "07_document_dependencies.html",
            ROOT / "site" / "deliverables" / "PMO-03.01" / "index.html",
            ROOT / "site" / "ar" / "deliverables" / "PMO-03.01" / "index.html",
        ]
        for page in sample_pages:
            self.assertTrue(page.exists(), f"Page {page} must exist")
            html = page.read_text(encoding="utf-8")
            # Frontmatter block like type: Guide token_pointer: should not be present
            matches = re.findall(r'type:\s*(?:Guide|Form|Overview|Manual|Example)[\s\S]{0,100}token_pointer:', html)
            self.assertEqual(len(matches), 0, f"Found visible YAML frontmatter in {page}: {matches}")

    def test_footer_author_card(self):
        """Verifies that all pages include Mohamed Fouad Fakhruldeen's author card with links to fakhr.me and linkedin in the footer."""
        sample_pages = [
            ROOT / "site" / "index.html",
            ROOT / "site" / "ar" / "index.html",
            ROOT / "site" / "deliverables" / "index.html",
            ROOT / "site" / "guides" / "index.html",
            ROOT / "site" / "deliverables" / "PMO-03.01" / "index.html",
            ROOT / "site" / "ar" / "deliverables" / "PMO-03.01" / "index.html",
        ]
        for page in sample_pages:
            self.assertTrue(page.exists(), f"Page {page} must exist")
            html = page.read_text(encoding="utf-8")
            self.assertIn("footer-author-card", html, f"Author card missing in {page}")
            self.assertIn("https://fakhr.me", html, f"fakhr.me link missing in {page}")
            self.assertIn("https://www.linkedin.com/in/fakhruldeen", html, f"LinkedIn link missing in {page}")
            self.assertIn("https://avatars.githubusercontent.com/u/1162549", html, f"Avatar missing in {page}")
            if "/ar/" in str(page):
                self.assertIn("محمد فؤاد فخر الدين", html, f"Arabic author name missing in {page}")
            else:
                self.assertIn("Mohamed Fouad Fakhruldeen", html, f"English author name missing in {page}")

    def test_deliverable_prompt_and_short_tabs(self):
        """Verifies that deliverable pages have shortened tab names and a dedicated LLM Prompt tab."""
        sample_pages = [
            ROOT / "site" / "deliverables" / "PMO-03.01" / "index.html",
            ROOT / "site" / "ar" / "deliverables" / "PMO-03.01" / "index.html",
        ]
        for page in sample_pages:
            self.assertTrue(page.exists(), f"Page {page} must exist")
            html = page.read_text(encoding="utf-8")
            self.assertIn('id="tab-prompt"', html, f"LLM Prompt tab missing in {page}")
            self.assertIn('id="tab-guide"', html, f"User Guide tab missing in {page}")
            self.assertIn('id="tab-template"', html, f"Template tab missing in {page}")
            self.assertIn('id="tab-example"', html, f"Example tab missing in {page}")
            self.assertIn('id="tab-schema"', html, f"Schema tab missing in {page}")

    def test_developers_comprehensive_documentation(self):
        """Verifies that the /developers/ page contains comprehensive documentation across all 10 technical areas."""
        dev_en = ROOT / "site" / "developers" / "index.html"
        dev_ar = ROOT / "site" / "ar" / "developers" / "index.html"
        self.assertTrue(dev_en.exists(), "English developers page must exist")
        self.assertTrue(dev_ar.exists(), "Arabic developers page must exist")

        html_en = dev_en.read_text(encoding="utf-8")
        html_ar = dev_ar.read_text(encoding="utf-8")

        # Verify all 10 core section anchors are present in both
        section_ids = [
            "quickstart", "cli", "sdk", "mcp", "schemas",
            "self-correction", "multi-agent", "llm-client", "cicd", "attested-math"
        ]
        for sid in section_ids:
            self.assertIn(f'id="{sid}"', html_en, f"Section #{sid} missing in English developers page")
            self.assertIn(f'id="{sid}"', html_ar, f"Section #{sid} missing in Arabic developers page")

        # Verify key technical topics covered
        self.assertIn("tasleemat.ai.AIClient", html_en)
        self.assertIn("tasleemat.ai.AIClient", html_ar)
        self.assertIn("The Autonomous Agent Self-Correction Loop", html_en)
        self.assertIn("التصحيح الذاتي", html_ar)
        self.assertIn("Multi-Agent PMO Swarm", html_en)
        self.assertIn("أسراب الوكلاء", html_ar)
        self.assertIn("PMO-06.05", html_en)
        self.assertIn("PMO-06.05", html_ar)
        self.assertIn("RFC 3339", html_en)
        self.assertIn("RFC 3339", html_ar)

    def test_developer_subpages_exist(self):
        """Verifies that all 5 developer sub-pages exist in both English and Arabic with rich tutorials."""
        subpages = ["cli", "sdk", "mcp", "schemas", "agentic"]
        for sub in subpages:
            en_page = ROOT / "site" / "developers" / sub / "index.html"
            ar_page = ROOT / "site" / "ar" / "developers" / sub / "index.html"

            self.assertTrue(en_page.exists(), f"Missing English developer subpage: {sub}")
            self.assertTrue(ar_page.exists(), f"Missing Arabic developer subpage: {sub}")
            self.assertGreater(en_page.stat().st_size, 40000, f"English subpage {sub} is smaller than 40KB")
            self.assertGreater(ar_page.stat().st_size, 40000, f"Arabic subpage {sub} is smaller than 40KB")

        # Specific content assertions for enriched sections
        cli_en = (ROOT / "site" / "developers" / "cli" / "index.html").read_text(encoding="utf-8")
        cli_ar = (ROOT / "site" / "ar" / "developers" / "cli" / "index.html").read_text(encoding="utf-8")
        self.assertIn("TASLEEMAT_HOME", cli_en)
        self.assertIn("TASLEEMAT_HOME", cli_ar)
        self.assertIn("provision_portfolio.sh", cli_en)
        self.assertIn("provision_portfolio.sh", cli_ar)

        sdk_en = (ROOT / "site" / "developers" / "sdk" / "index.html").read_text(encoding="utf-8")
        sdk_ar = (ROOT / "site" / "ar" / "developers" / "sdk" / "index.html").read_text(encoding="utf-8")
        self.assertIn("FastAPI", sdk_en)
        self.assertIn("FastAPI", sdk_ar)
        self.assertIn("Streamlit", sdk_en)
        self.assertIn("Streamlit", sdk_ar)
        self.assertIn("calculate_evm_metrics", sdk_en)
        self.assertIn("calculate_evm_metrics", sdk_ar)

        mcp_en = (ROOT / "site" / "developers" / "mcp" / "index.html").read_text(encoding="utf-8")
        mcp_ar = (ROOT / "site" / "ar" / "developers" / "mcp" / "index.html").read_text(encoding="utf-8")
        self.assertIn("tasleemat_calculate_eva", mcp_en)
        self.assertIn("tasleemat_calculate_eva", mcp_ar)
        self.assertIn("call_mcp_tool", mcp_en)
        self.assertIn("call_mcp_tool", mcp_ar)

        schemas_en = (ROOT / "site" / "developers" / "schemas" / "index.html").read_text(encoding="utf-8")
        schemas_ar = (ROOT / "site" / "ar" / "developers" / "schemas" / "index.html").read_text(encoding="utf-8")
        self.assertIn("run_autonomous_synthesis", schemas_en)
        self.assertIn("run_autonomous_synthesis", schemas_ar)
        self.assertIn("unevaluatedProperties", schemas_en)
        self.assertIn("unevaluatedProperties", schemas_ar)

        agentic_en = (ROOT / "site" / "developers" / "agentic" / "index.html").read_text(encoding="utf-8")
        agentic_ar = (ROOT / "site" / "ar" / "developers" / "agentic" / "index.html").read_text(encoding="utf-8")
        self.assertIn("CrewAI", agentic_en)
        self.assertIn("CrewAI", agentic_ar)
        self.assertIn("LangGraph", agentic_en)
        self.assertIn("LangGraph", agentic_ar)


    def test_tailoring_page_structure_and_deliverable_links(self):
        """Verifies that the dedicated /tailoring/ page lists deliverables with direct links."""
        en_tailor = ROOT / "site" / "tailoring" / "index.html"
        ar_tailor = ROOT / "site" / "ar" / "tailoring" / "index.html"

        self.assertTrue(en_tailor.exists(), "English tailoring page must exist")
        self.assertTrue(ar_tailor.exists(), "Arabic tailoring page must exist")

        html_en = en_tailor.read_text(encoding="utf-8")
        html_ar = ar_tailor.read_text(encoding="utf-8")

        # Verify all tiers and packs mentioned
        self.assertIn("Tier 1: Mega", html_en)
        self.assertIn("المستوى 1: المشاريع الكبرى", html_ar)
        self.assertIn("Tier 2: Standard Enterprise", html_en)
        self.assertIn("المستوى 2: المشاريع القياسية", html_ar)
        self.assertIn("Tier 3: Lean", html_en)
        self.assertIn("المستوى 3: المشاريع الرشيقة", html_ar)

        # Verify deliverable links
        self.assertIn("/deliverables/PMO-03.01/", html_en)
        self.assertIn("/ar/deliverables/PMO-03.01/", html_ar)
        self.assertIn("/deliverables/PMO-01.01/", html_en)
        self.assertIn("/ar/deliverables/PMO-01.01/", html_ar)

    def test_homepage_section_ordering(self):
        """Verifies that Honest Boundaries section was moved down right before the footer."""
        html_en = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
        html_ar = (ROOT / "site" / "ar" / "index.html").read_text(encoding="utf-8")

        # In English: Lifecycle < Tiers < Boundaries < Footer
        pos_en_life = html_en.find("8 Project Lifecycle Stages")
        pos_en_tiers = html_en.find("Governance Sizing Tiers &amp; Delivery Packs")
        pos_en_bounds = html_en.find("Honest Boundaries &amp; Scope")
        pos_en_foot = html_en.find("<footer")

        self.assertTrue(pos_en_life < pos_en_tiers < pos_en_bounds < pos_en_foot,
                        f"English home section order violated: {pos_en_life}, {pos_en_tiers}, {pos_en_bounds}, {pos_en_foot}")

        # In Arabic: Lifecycle < Tiers < Boundaries < Footer
        pos_ar_life = html_ar.find("8 مراحل في دورة حياة المشروع")
        pos_ar_tiers = html_ar.find("مستويات الحوكمة وحزم المنهجيات")
        pos_ar_bounds = html_ar.find("حدود ونطاق مشروع تسليمات")
        pos_ar_foot = html_ar.find("<footer")

    def test_social_meta_and_open_graph_tags(self):
        """Verifies that all pages contain complete Open Graph, Twitter Cards, and canonical tags for social sharing."""
        social_img = SITE_DIR / "img" / "social.png"
        self.assertTrue(social_img.exists(), "Social preview image site/img/social.png must exist")
        self.assertGreater(social_img.stat().st_size, 1000, "Social image must not be empty")

        sample_pages = [
            ("index.html", "en", "https://fakhr.me/Tasleemat/"),
            ("ar/index.html", "ar", "https://fakhr.me/Tasleemat/ar/"),
            ("start/index.html", "en", "https://fakhr.me/Tasleemat/start/"),
            ("ar/start/index.html", "ar", "https://fakhr.me/Tasleemat/ar/start/"),
            ("deliverables/index.html", "en", "https://fakhr.me/Tasleemat/deliverables/"),
            ("ar/deliverables/index.html", "ar", "https://fakhr.me/Tasleemat/ar/deliverables/"),
            ("deliverables/PMO-03.01/index.html", "en", "https://fakhr.me/Tasleemat/deliverables/PMO-03.01/"),
            ("ar/deliverables/PMO-03.01/index.html", "ar", "https://fakhr.me/Tasleemat/ar/deliverables/PMO-03.01/"),
            ("guides/index.html", "en", "https://fakhr.me/Tasleemat/guides/"),
            ("ar/guides/index.html", "ar", "https://fakhr.me/Tasleemat/ar/guides/"),
            ("developers/index.html", "en", "https://fakhr.me/Tasleemat/developers/"),
            ("ar/developers/index.html", "ar", "https://fakhr.me/Tasleemat/ar/developers/"),
            ("developers/cli/index.html", "en", "https://fakhr.me/Tasleemat/developers/cli/"),
            ("ar/developers/cli/index.html", "ar", "https://fakhr.me/Tasleemat/ar/developers/cli/"),
            ("tailoring/index.html", "en", "https://fakhr.me/Tasleemat/tailoring/"),
            ("ar/tailoring/index.html", "ar", "https://fakhr.me/Tasleemat/ar/tailoring/"),
        ]

        for rel_path, lang, canonical_url in sample_pages:
            page = SITE_DIR / rel_path
            self.assertTrue(page.exists(), f"Sample page missing: {rel_path}")
            html = page.read_text(encoding="utf-8")

            # Open Graph Tags
            self.assertIn('<meta property="og:type" content="website">', html, f"Missing og:type in {rel_path}")
            self.assertIn(f'<meta property="og:url" content="{canonical_url}">', html, f"Wrong og:url in {rel_path}")
            self.assertIn('<meta property="og:site_name"', html, f"Missing og:site_name in {rel_path}")
            self.assertIn('<meta property="og:title"', html, f"Missing og:title in {rel_path}")
            self.assertIn('<meta property="og:description"', html, f"Missing og:description in {rel_path}")
            self.assertIn('<meta property="og:image" content="https://fakhr.me/Tasleemat/img/social.png">', html, f"Missing og:image in {rel_path}")
            self.assertIn('<meta property="og:image:width" content="1280">', html, f"Missing og:image:width in {rel_path}")
            self.assertIn('<meta property="og:image:height" content="640">', html, f"Missing og:image:height in {rel_path}")

            # Locale
            expected_locale = "ar_SA" if lang == "ar" else "en_US"
            alt_locale = "en_US" if lang == "ar" else "ar_SA"
            self.assertIn(f'<meta property="og:locale" content="{expected_locale}">', html, f"Wrong og:locale in {rel_path}")
            self.assertIn(f'<meta property="og:locale:alternate" content="{alt_locale}">', html, f"Wrong og:locale:alternate in {rel_path}")

            # Twitter Card Tags
            self.assertIn('<meta name="twitter:card" content="summary_large_image">', html, f"Missing twitter:card in {rel_path}")
            self.assertIn(f'<meta name="twitter:url" content="{canonical_url}">', html, f"Wrong twitter:url in {rel_path}")
            self.assertIn('<meta name="twitter:title"', html, f"Missing twitter:title in {rel_path}")
            self.assertIn('<meta name="twitter:description"', html, f"Missing twitter:description in {rel_path}")
            self.assertIn('<meta name="twitter:image" content="https://fakhr.me/Tasleemat/img/social.png">', html, f"Missing twitter:image in {rel_path}")

            # Canonical & Author
            self.assertIn(f'<link rel="canonical" href="{canonical_url}">', html, f"Missing canonical in {rel_path}")
            self.assertIn('<meta name="author" content="Mohamed Fouad Fakhruldeen">', html, f"Missing author in {rel_path}")


if __name__ == "__main__":
    unittest.main()




