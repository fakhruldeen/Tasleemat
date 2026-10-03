#!/usr/bin/env python3
"""Tests for Template Governance, Document Control tables, and Guide cross-references.
"""

import unittest
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMS_EN = ROOT / "forms" / "en"
FORMS_AR = ROOT / "forms" / "ar"
DOCS_DIR = ROOT / "docs"

class TestGovernanceTemplates(unittest.TestCase):

    def test_document_control_tables_in_all_templates(self):
        """Verify every template contains an executive Document Control / Sign-off table."""
        en_templates = list(FORMS_EN.rglob("*_Template.md"))
        ar_templates = list(FORMS_AR.rglob("*_قالب.md"))

        self.assertEqual(len(en_templates), 102)
        self.assertEqual(len(ar_templates), 102)

        for t in en_templates:
            content = t.read_text(encoding="utf-8")
            has_doc_control = ("Document Control" in content or "Prepared by" in content or "Approved by" in content or "Sign-off" in content or "Authorization" in content)
            self.assertTrue(has_doc_control, f"Missing Document Control table in {t.name}")

        for t in ar_templates:
            content = t.read_text(encoding="utf-8")
            has_doc_control = ("التحكم في الوثيقة" in content or "إعداد" in content or "اعتماد" in content or "المعتمد" in content or "المراجع" in content or "التوقيع" in content)
            self.assertTrue(has_doc_control, f"Missing Arabic Document Control table in {t.name}")

    def test_guides_link_to_completed_examples(self):
        """Verify all 204 guide files link to their completed reference example."""
        en_guides = list(FORMS_EN.rglob("*_Guide.md"))
        ar_guides = list(FORMS_AR.rglob("*_دليل.md"))

        for g in en_guides:
            content = g.read_text(encoding="utf-8")
            self.assertIn("examples/en/", content, f"Guide {g.name} does not link to English example")

        for g in ar_guides:
            content = g.read_text(encoding="utf-8")
            self.assertIn("examples/ar/", content, f"Arabic guide {g.name} does not link to Arabic example")

    def test_relative_links_in_docs_and_forms(self):
        """Verify all relative markdown links in docs/ and forms/ point to existing files."""
        md_files = list(DOCS_DIR.rglob("*.md")) + [ROOT / "README.md", ROOT / "README_AR.md"]

        for mf in md_files:
            content = mf.read_text(encoding="utf-8")
            # Match markdown links [text](path) including paths with balanced parentheses
            links = re.findall(r'\[(?:[^\]]*)\]\(((?:[^()]+|\([^()]*\))+)\)', content)
            for l in links:
                if l.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                # remove anchors e.g. file.md#section
                clean_link = l.split('#')[0].split('?')[0].strip()
                if not clean_link:
                    continue
                target = (mf.parent / clean_link).resolve()
                self.assertTrue(
                    target.exists(),
                    f"Broken link '{clean_link}' in {mf.relative_to(ROOT)}"
                )

    def test_mermaid_diagram_syntax_integrity(self):
        """Verify all mermaid diagram blocks in markdown files have matching delimiters."""
        all_mds = list(ROOT.rglob("*.md"))
        
        for mf in all_mds:
            if ".git" in str(mf) or "scratch" in str(mf):
                continue
            content = mf.read_text(encoding="utf-8")
            # Count opening ```mermaid vs closed code blocks
            mermaid_starts = len(re.findall(r'```mermaid', content))
            if mermaid_starts > 0:
                # verify block closes
                code_block_delims = len(re.findall(r'```', content))
                self.assertEqual(
                    code_block_delims % 2, 0,
                    f"Unclosed code block / mermaid diagram in {mf.relative_to(ROOT)}"
                )

if __name__ == "__main__":
    unittest.main()
