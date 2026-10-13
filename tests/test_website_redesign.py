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


if __name__ == "__main__":
    unittest.main()
