#!/usr/bin/env python3
"""
tests/test_documentation.py
Validates the documentation portal, 24 comprehensive operational manuals (12 EN / 12 AR),
bilingual README files, Lexicon dictionaries, and mkdocs.yml navigation integrity.
"""

import unittest
import pathlib
import json
import yaml

ROOT = pathlib.Path(__file__).parent.parent.resolve()
DOCS_DIR = ROOT / "docs"

class CustomYamlLoader(yaml.SafeLoader):
    pass
CustomYamlLoader.add_multi_constructor('tag:yaml.org,2002:python/', lambda loader, suffix, node: None)

class TestDocumentation(unittest.TestCase):

    def setUp(self):
        self.en_docs = sorted(list((DOCS_DIR / "en").glob("*.md")))
        self.ar_docs = sorted(list((DOCS_DIR / "ar").glob("*.md")))

    def test_documentation_manuals_count_and_symmetry(self):
        """Verify exactly 12 English and 12 Arabic governance manuals exist."""
        self.assertEqual(len(self.en_docs), 12, f"Expected 12 EN guides, found {len(self.en_docs)}")
        self.assertEqual(len(self.ar_docs), 12, f"Expected 12 AR guides, found {len(self.ar_docs)}")

        en_prefixes = [p.stem.split("_")[0] for p in self.en_docs]
        ar_prefixes = [p.stem.split("_")[0] for p in self.ar_docs]
        self.assertEqual(en_prefixes, ar_prefixes, "EN and AR guide number prefixes must match 1:1")

    def test_documentation_manuals_substantive_content(self):
        """Verify each guide is substantive (> 1000 characters) and has standard governance headers."""
        for doc in self.en_docs:
            content = doc.read_text(encoding="utf-8").strip()
            self.assertGreater(
                len(content), 1000,
                f"English guide {doc.name} is too short ({len(content)} chars)."
            )
            has_ref = "Document Reference:" in content or "TASLEEMAT-GUIDE-" in content or "PMO-POL-MANUAL" in content
            self.assertTrue(has_ref, f"Guide {doc.name} missing standard Document Reference header.")

        for doc in self.ar_docs:
            content = doc.read_text(encoding="utf-8").strip()
            self.assertGreater(
                len(content), 1000,
                f"Arabic guide {doc.name} is too short ({len(content)} chars)."
            )
            has_ref = "مرجع الوثيقة:" in content or "TASLEEMAT-GUIDE-" in content or "PMO-POL-MANUAL" in content
            self.assertTrue(has_ref, f"Arabic guide {doc.name} missing standard مرجع الوثيقة header.")

    def test_lexicon_integrity(self):
        """Verify LEXICON.md and LEXICON.json exist and are well-formed."""
        lex_md = DOCS_DIR / "LEXICON.md"
        lex_json = DOCS_DIR / "LEXICON.json"

        self.assertTrue(lex_md.exists(), "docs/LEXICON.md must exist")
        self.assertTrue(lex_json.exists(), "docs/LEXICON.json must exist")

        with open(lex_json, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)
        self.assertEqual(data.get("total_forms"), 102)
        self.assertEqual(len(data.get("forms", [])), 102)

    def test_mkdocs_navigation_targets_exist(self):
        """Verify mkdocs.yml loads correctly and all referenced files exist on disk."""
        mkdocs_path = ROOT / "mkdocs.yml"
        self.assertTrue(mkdocs_path.exists(), "mkdocs.yml must exist at repo root")

        with open(mkdocs_path, "r", encoding="utf-8") as f:
            conf = yaml.load(f, Loader=CustomYamlLoader)

        self.assertIn("site_name", conf)
        nav = conf.get("nav", [])
        self.assertTrue(len(nav) > 0, "mkdocs.yml navigation must not be empty")

        missing_files = []
        def check_nav(item):
            if isinstance(item, dict):
                for k, v in item.items():
                    check_nav(v)
            elif isinstance(item, list):
                for sub in item:
                    check_nav(sub)
            elif isinstance(item, str):
                target = DOCS_DIR / item
                if not target.exists():
                    missing_files.append((item, str(target)))

        check_nav(nav)
        self.assertEqual(len(missing_files), 0, f"mkdocs.yml references missing files: {missing_files}")

    def test_repo_readmes(self):
        """Verify root README.md and README_AR.md are rich, present, and valid."""
        readme_en = ROOT / "README.md"
        readme_ar = ROOT / "README_AR.md"

        self.assertTrue(readme_en.exists(), "README.md must exist")
        self.assertTrue(readme_ar.exists(), "README_AR.md must exist")

        content_en = readme_en.read_text(encoding="utf-8")
        content_ar = readme_ar.read_text(encoding="utf-8")

        self.assertGreater(len(content_en), 2000, "README.md must be comprehensive")
        self.assertGreater(len(content_ar), 2000, "README_AR.md must be comprehensive")
        self.assertIn("Tasleemat", content_en)
        self.assertIn("تسليمات", content_ar)

if __name__ == "__main__":
    unittest.main()
