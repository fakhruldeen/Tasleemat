#!/usr/bin/env python3
"""Tests for 1:1 Bilingual Structural and Artifact Symmetry across Tasleemat.
"""

import unittest
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMS_EN = ROOT / "forms" / "en"
FORMS_AR = ROOT / "forms" / "ar"
EXAMPLES_EN = ROOT / "examples" / "en"
EXAMPLES_AR = ROOT / "examples" / "ar"

class TestBilingualParity(unittest.TestCase):

    def test_phase_directories_exist(self):
        """Verify all 8 lifecycle phases exist in both EN and AR."""
        en_phases = sorted([p.name for p in FORMS_EN.iterdir() if p.is_dir() and re.match(r'^\d{2}_', p.name)])
        ar_phases = sorted([p.name for p in FORMS_AR.iterdir() if p.is_dir() and re.match(r'^\d{2}_', p.name)])
        
        self.assertEqual(len(en_phases), 8, f"Expected 8 EN phases, found {len(en_phases)}")
        self.assertEqual(len(ar_phases), 8, f"Expected 8 AR phases, found {len(ar_phases)}")
        
        # Verify phase prefixes match (00 through 07)
        en_prefixes = [p[:2] for p in en_phases]
        ar_prefixes = [p[:2] for p in ar_phases]
        self.assertEqual(en_prefixes, ar_prefixes)

    def test_form_bundle_counts(self):
        """Verify exactly 114 form folders exist in both EN and AR."""
        en_templates = list(FORMS_EN.rglob("*_Template.md"))
        ar_templates = list(FORMS_AR.rglob("*_قالب.md"))
        
        self.assertEqual(len(en_templates), 114, f"Expected 114 EN templates, found {len(en_templates)}")
        self.assertEqual(len(ar_templates), 114, f"Expected 114 AR templates, found {len(ar_templates)}")

    def test_five_file_bundle_integrity(self):
        """Verify every form folder contains all 5 required files."""
        en_templates = list(FORMS_EN.rglob("*_Template.md"))
        
        for t in en_templates:
            folder = t.parent
            # Expect: *_Template.md, *_Guide.md, *.md, *.json, *.csv
            guides = list(folder.glob("*_Guide.md"))
            prompts = [p for p in folder.glob("*.md") if not p.name.endswith(("_Template.md", "_Guide.md"))]
            jsons = list(folder.glob("*.json"))
            csvs = list(folder.glob("*.csv"))
            
            self.assertEqual(len(guides), 1, f"Missing Guide in {folder}")
            self.assertEqual(len(prompts), 1, f"Missing Prompt in {folder}")
            self.assertEqual(len(jsons), 1, f"Missing JSON Schema in {folder}")
            self.assertEqual(len(csvs), 1, f"Missing CSV Dictionary in {folder}")

        ar_templates = list(FORMS_AR.rglob("*_قالب.md"))
        for t in ar_templates:
            folder = t.parent
            guides = list(folder.glob("*_دليل.md"))
            prompts = [p for p in folder.glob("*.md") if not p.name.endswith(("_قالب.md", "_دليل.md"))]
            jsons = list(folder.glob("*.json"))
            csvs = list(folder.glob("*.csv"))
            
            self.assertEqual(len(guides), 1, f"Missing Arabic Guide in {folder}")
            self.assertEqual(len(prompts), 1, f"Missing Arabic Prompt in {folder}")
            self.assertEqual(len(jsons), 1, f"Missing Arabic JSON Schema in {folder}")
            self.assertEqual(len(csvs), 1, f"Missing Arabic CSV Dictionary in {folder}")

    def test_examples_symmetry(self):
        """Verify 114 reference examples in EN match 114 in AR."""
        en_examples = list(EXAMPLES_EN.rglob("*_Example.md"))
        ar_examples = list(EXAMPLES_AR.rglob("*_مثال.md"))
        
        self.assertEqual(len(en_examples), 114, f"Expected 114 EN examples, found {len(en_examples)}")
        self.assertEqual(len(ar_examples), 114, f"Expected 114 AR examples, found {len(ar_examples)}")

if __name__ == "__main__":
    unittest.main()
