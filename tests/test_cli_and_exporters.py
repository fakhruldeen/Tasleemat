#!/usr/bin/env python3
"""
tests/test_cli_and_exporters.py
Tests the Tasleemat CLI (`tools/tasleemat_cli.py`) and Batch Exporter (`tools/export_deliverables.py`)
ensuring robust scaffolding, variable replacement, catalog search, and HTML export.
"""

import unittest
import pathlib
import tempfile
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).parent.parent.resolve()
CLI_PATH = ROOT / "tools" / "tasleemat_cli.py"
EXPORTER_PATH = ROOT / "tools" / "export_deliverables.py"

class TestCliAndExporters(unittest.TestCase):

    def test_cli_list_commands(self):
        """Test listing English and Arabic forms via CLI."""
        res_en = subprocess.run(
            [sys.executable, str(CLI_PATH), "list", "-l", "en"],
            capture_output=True, text=True, cwd=str(ROOT)
        )
        self.assertEqual(res_en.returncode, 0)
        self.assertIn("Tasleemat Master Forms Catalog (EN)", res_en.stdout)
        self.assertIn("Total forms found: 114", res_en.stdout)

        res_ar = subprocess.run(
            [sys.executable, str(CLI_PATH), "list", "-l", "ar"],
            capture_output=True, text=True, cwd=str(ROOT)
        )
        self.assertEqual(res_ar.returncode, 0)
        self.assertIn("Tasleemat Master Forms Catalog (AR)", res_ar.stdout)
        self.assertIn("Total forms found: 114", res_ar.stdout)

    def test_cli_search_commands(self):
        """Test searching for deliverable forms via CLI."""
        res = subprocess.run(
            [sys.executable, str(CLI_PATH), "search", "charter", "-l", "en"],
            capture_output=True, text=True, cwd=str(ROOT)
        )
        self.assertEqual(res.returncode, 0)
        self.assertIn("MATCH", res.stdout)
        self.assertIn("03_01", res.stdout)

        res_ar = subprocess.run(
            [sys.executable, str(CLI_PATH), "search", "ميثاق", "-l", "ar"],
            capture_output=True, text=True, cwd=str(ROOT)
        )
        self.assertEqual(res_ar.returncode, 0)
        self.assertIn("MATCH", res_ar.stdout)

    def test_cli_scaffold_tier3_lean(self):
        """Test scaffolding a Tier 3 Lean project and verifying variable substitution."""
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = pathlib.Path(tmpdir) / "Test_Lean_Project"
            res = subprocess.run(
                [
                    sys.executable, str(CLI_PATH), "init",
                    "-n", "Autonomous Drone Delivery",
                    "-c", "PRJ-DRONE-99",
                    "--pm", "Sarah Al-Rashid",
                    "--sponsor", "Eng. Khalid",
                    "-t", "3",
                    "-p", "agile",
                    "-l", "both",
                    "-o", str(out_path)
                ],
                capture_output=True, text=True, cwd=str(ROOT)
            )
            self.assertEqual(res.returncode, 0)
            self.assertTrue(out_path.exists())
            self.assertTrue((out_path / "PROJECT_README.md").exists())
            
            # Check variable substitutions in files
            readme = (out_path / "PROJECT_README.md").read_text(encoding="utf-8")
            self.assertIn("Autonomous Drone Delivery", readme)
            self.assertIn("PRJ-DRONE-99", readme)
            self.assertIn("Sarah Al-Rashid", readme)

            # Check that files were copied
            ar_files = list((out_path / "ar").rglob("*.md"))
            en_files = list((out_path / "en").rglob("*.md"))
            self.assertGreater(len(ar_files), 5)
            self.assertGreater(len(en_files), 5)

            # Check header variable replacement in a scaffolded template
            for f in ar_files:
                content = f.read_text(encoding="utf-8")
                self.assertNotIn("{{اسم_المشروع}}", content)
                self.assertNotIn("{{معرف_المشروع}}", content)

    def test_exporter_markdown_to_html(self):
        """Test exporting Markdown deliverable to HTML."""
        sample_md = ROOT / "forms" / "en" / "03_Initiating" / "01_Project_Charter" / "03_01_Project_Charter_Template.md"
        with tempfile.TemporaryDirectory() as tmpdir:
            out_html = pathlib.Path(tmpdir) / "charter.html"
            res = subprocess.run(
                [
                    sys.executable, str(EXPORTER_PATH),
                    str(sample_md),
                    "-o", str(out_html)
                ],
                capture_output=True, text=True, cwd=str(ROOT)
            )
            self.assertEqual(res.returncode, 0)
            self.assertTrue(out_html.exists())
            html_text = out_html.read_text(encoding="utf-8")
            self.assertIn("<!DOCTYPE html>", html_text)
            self.assertIn("project charter", html_text.lower())

    def test_exporter_batch_directory(self):
        """Test batch exporting an entire folder to HTML."""
        input_dir = ROOT / "forms" / "ar" / "03_البدء" / "01_ميثاق_المشروع"
        with tempfile.TemporaryDirectory() as tmpdir:
            # copy folder to tmpdir so exported html files go into tmpdir
            test_sub = pathlib.Path(tmpdir) / "test_folder"
            shutil.copytree(input_dir, test_sub)
            res = subprocess.run(
                [
                    sys.executable, str(EXPORTER_PATH),
                    str(test_sub)
                ],
                capture_output=True, text=True, cwd=str(ROOT)
            )
            self.assertEqual(res.returncode, 0)
            html_files = list(test_sub.glob("*.html"))
            self.assertGreater(len(html_files), 0)

if __name__ == "__main__":
    unittest.main()
