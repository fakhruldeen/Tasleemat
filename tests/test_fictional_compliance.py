#!/usr/bin/env python3
"""
tests/test_fictional_compliance.py
Verifies that all 228 reference examples in Tasleemat are rich, realistic,
fully populated without unresolved placeholders, and contain proper fictional governance data.
"""

import unittest
import pathlib
import re

ROOT = pathlib.Path(__file__).parent.parent.resolve()
EXAMPLES_DIR = ROOT / "examples"

class TestFictionalCompliance(unittest.TestCase):

    def setUp(self):
        self.en_examples = list(EXAMPLES_DIR.glob("en/**/*_Example.md"))
        self.ar_examples = list(EXAMPLES_DIR.glob("ar/**/*_مثال.md"))

    def test_example_counts_and_symmetry(self):
        """Verify that exactly 114 EN examples and 114 AR examples exist."""
        self.assertEqual(len(self.en_examples), 114, f"Expected 114 EN examples, got {len(self.en_examples)}")
        self.assertEqual(len(self.ar_examples), 114, f"Expected 114 AR examples, got {len(self.ar_examples)}")

    def test_example_files_non_empty_and_substantive(self):
        """Verify that all example files contain substantive, realistic project content (> 400 chars)."""
        for ef in self.en_examples + self.ar_examples:
            content = ef.read_text(encoding="utf-8").strip()
            self.assertGreater(
                len(content),
                400,
                f"Example file {ef.relative_to(ROOT)} is too short ({len(content)} chars) to be a realistic example."
            )

    def test_no_unresolved_placeholders_in_examples(self):
        """Verify no unreplaced template placeholders remain in reference examples."""
        suspicious_patterns = [
            re.compile(r'\{\{[^}]+\}\}'),
            re.compile(r'\[\s*(?:Insert|TODO|TBD|Add|Specify|Enter)\b[^\]]*\]', re.IGNORECASE),
            re.compile(r'\[\s*(?:أدخل|حدد|أضف|اكتب|يرجى)\b[^\]]*\]')
        ]

        for ef in self.en_examples + self.ar_examples:
            content = ef.read_text(encoding="utf-8")
            for pat in suspicious_patterns:
                matches = pat.findall(content)
                self.assertEqual(
                    len(matches),
                    0,
                    f"Found unresolved placeholder(s) {matches} in example: {ef.relative_to(ROOT)}"
                )

    def test_governance_signoff_in_examples(self):
        """Verify that examples contain realistic document governance metadata (Author / Date / Sign-off)."""
        en_keywords = ["Author", "Date", "Version", "Status"]
        ar_keywords = ["المعد", "التاريخ", "الإصدار", "الحالة"]

        for ef in self.en_examples:
            content = ef.read_text(encoding="utf-8")
            has_gov = any(k in content for k in en_keywords)
            self.assertTrue(has_gov, f"EN example missing governance metadata: {ef.relative_to(ROOT)}")

        for ef in self.ar_examples:
            content = ef.read_text(encoding="utf-8")
            has_gov = any(k in content for k in ar_keywords)
            self.assertTrue(has_gov, f"AR example missing governance metadata: {ef.relative_to(ROOT)}")

if __name__ == "__main__":
    unittest.main()
