#!/usr/bin/env python3
"""
tests/test_consumer_interface.py
Comprehensive tests for the Tasleemat programmatic consumer contract:
- Canonical artifact discovery & asset retrieval
- Bilingual parity & content loaders
- Completed artifact data validation (valid, invalid, draft fixtures)
- Offline rendering with forms/ write protection
"""

import json
import os
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import tasleemat
from tasleemat.catalog import (
    ArtifactAssets,
    ArtifactSummary,
    get_artifact_assets,
    get_artifact_definition,
    get_tailoring_profile,
    list_artifacts,
)
from tasleemat.rendering import render_artifact
from tasleemat.validation import (
    ValidationError,
    ValidationReport,
    validate_artifact_data,
)

FIXTURES_DIR = ROOT / "tests" / "fixtures"


class TestConsumerInterface(unittest.TestCase):

    def test_package_exports(self):
        """Verify public package exports at root tasleemat namespace."""
        self.assertEqual(tasleemat.__version__, "2.6.0")
        self.assertTrue(callable(tasleemat.list_artifacts))
        self.assertTrue(callable(tasleemat.get_artifact_definition))
        self.assertTrue(callable(tasleemat.get_artifact_assets))
        self.assertTrue(callable(tasleemat.get_tailoring_profile))
        self.assertTrue(callable(tasleemat.validate_artifact_data))
        self.assertTrue(callable(tasleemat.render_artifact))

    def test_list_artifacts_all(self):
        """Verify listing returns all 114 canonical artifacts."""
        all_artifacts = list_artifacts()
        self.assertEqual(len(all_artifacts), 114)
        for a in all_artifacts:
            self.assertIsInstance(a, ArtifactSummary)
            self.assertTrue(a.artifact_id.startswith("PMO-"))
            self.assertTrue(len(a.name_en) > 0)
            self.assertTrue(len(a.name_ar) > 0)
            self.assertIn(a.phase_code, [f"{i:02d}" for i in range(8)])

    def test_list_artifacts_filtering(self):
        """Verify filtering by phase and tier."""
        init_artifacts = list_artifacts(phase="03")
        self.assertGreater(len(init_artifacts), 0)
        for a in init_artifacts:
            self.assertEqual(a.phase_code, "03")

        tier3_artifacts = list_artifacts(tier="3")
        self.assertGreater(len(tier3_artifacts), 0)
        for a in tier3_artifacts:
            self.assertIn("3", a.tiers)

    def test_get_artifact_definition_success_and_failure(self):
        """Verify artifact definition retrieval and unknown ID handling."""
        defn = get_artifact_definition("PMO-03.01")
        self.assertEqual(defn["artifact_id"], "PMO-03.01")
        self.assertEqual(defn["prefix"], "03_01")
        self.assertEqual(defn["name_en"], "PROJECT CHARTER")
        self.assertIn("en", defn["assets"])
        self.assertIn("ar", defn["assets"])

        with self.assertRaises(KeyError):
            get_artifact_definition("NONEXISTENT-99.99")

    def test_get_artifact_assets_and_content_loaders(self):
        """Verify asset path resolution and content loaders for English and Arabic."""
        assets_en = get_artifact_assets("PMO-03.01", lang="en")
        self.assertEqual(assets_en.lang, "en")
        tmpl_en = assets_en.get_template_content()
        self.assertIn("PROJECT CHARTER", tmpl_en)
        guide_en = assets_en.get_guide_content()
        self.assertIn("Project Artifact: Project Charter", guide_en)
        schema_en = assets_en.get_schema_data()
        self.assertIn("fields", schema_en)
        dict_en = assets_en.get_dictionary_data()
        self.assertGreater(len(dict_en), 0)
        ex_en = assets_en.get_example_content()
        self.assertIsNotNone(ex_en)
        self.assertIn("Apex", ex_en)

        assets_ar = get_artifact_assets("PMO-03.01", lang="ar")
        self.assertEqual(assets_ar.lang, "ar")
        tmpl_ar = assets_ar.get_template_content()
        self.assertIn("ميثاق المشروع", tmpl_ar)
        ex_ar = assets_ar.get_example_content()
        self.assertIsNotNone(ex_ar)
        self.assertIn("القمة", ex_ar)

        with self.assertRaises(ValueError):
            get_artifact_assets("PMO-03.01", lang="fr")

    def test_tailoring_profiles(self):
        """Verify tailoring profile query."""
        t2_agile = get_tailoring_profile("2", pack="agile")
        self.assertIn("PMO-03.01", t2_agile)
        self.assertIn("PMO-01.01", t2_agile)
        self.assertGreater(len(t2_agile), 5)

    def test_validate_pmo_03_01_valid_fixture(self):
        """Verify validation of valid PMO-03.01 fixture."""
        fixture_path = FIXTURES_DIR / "valid" / "PMO-03.01_valid.json"
        with open(fixture_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        report = validate_artifact_data("PMO-03.01", data)
        self.assertIsInstance(report, ValidationReport)
        self.assertTrue(report.valid)
        self.assertEqual(len(report.errors), 0)

    def test_validate_pmo_03_01_invalid_fixture(self):
        """Verify validation of invalid PMO-03.01 fixture flags missing required fields."""
        fixture_path = FIXTURES_DIR / "invalid" / "PMO-03.01_missing_required.json"
        with open(fixture_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        report = validate_artifact_data("PMO-03.01", data, mode="strict")
        self.assertFalse(report.valid)
        self.assertGreater(len(report.errors), 0)

        error_paths = [e.field_path for e in report.errors]
        self.assertTrue(any("project_objectives" in p for p in error_paths))

    def test_validate_pmo_03_01_draft_mode(self):
        """Verify draft mode accepts partial data and issues warnings rather than blocking errors."""
        fixture_path = FIXTURES_DIR / "draft" / "PMO-03.01_draft.json"
        with open(fixture_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        report = validate_artifact_data("PMO-03.01", data, mode="draft")
        self.assertTrue(report.valid)
        self.assertGreater(len(report.warnings), 0)

    def test_validate_pmo_04_08_02_fixtures(self):
        """Verify Risk Register valid and invalid fixtures."""
        valid_path = FIXTURES_DIR / "valid" / "PMO-04.08.02_valid.json"
        with open(valid_path, "r", encoding="utf-8") as f:
            valid_data = json.load(f)
        report_valid = validate_artifact_data("PMO-04.08.02", valid_data)
        self.assertTrue(report_valid.valid)

        invalid_path = FIXTURES_DIR / "invalid" / "PMO-04.08.02_invalid_types.json"
        with open(invalid_path, "r", encoding="utf-8") as f:
            invalid_data = json.load(f)
        report_invalid = validate_artifact_data("PMO-04.08.02", invalid_data)
        self.assertFalse(report_invalid.valid)
        self.assertGreater(len(report_invalid.errors), 0)

    def test_validate_pmo_06_01_valid_fixture(self):
        """Verify Project Status Report valid fixture."""
        valid_path = FIXTURES_DIR / "valid" / "PMO-06.01_valid.json"
        with open(valid_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        report = validate_artifact_data("PMO-06.01", data)
        self.assertTrue(report.valid)

    def test_rendering_html_strings(self):
        """Verify offline rendering for English and Arabic artifacts."""
        html_en = render_artifact("PMO-03.01", lang="en")
        self.assertIn("<!DOCTYPE html>", html_en)
        self.assertIn('dir="ltr"', html_en)
        self.assertIn("Inter", html_en)
        self.assertIn("PROJECT CHARTER", html_en)

        html_ar = render_artifact("PMO-03.01", lang="ar")
        self.assertIn("<!DOCTYPE html>", html_ar)
        self.assertIn('dir="rtl"', html_ar)
        self.assertIn("Cairo", html_ar)
        self.assertIn("ميثاق المشروع", html_ar)

    def test_rendering_forms_write_protection(self):
        """Verify that attempting to write rendered output inside forms/ is strictly blocked."""
        forms_target = ROOT / "forms" / "en" / "test_output.html"
        with self.assertRaises(ValueError):
            render_artifact("PMO-03.01", lang="en", out_path=forms_target)

    def test_rendering_safe_output_path(self):
        """Verify rendering writes safely to an external temporary directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = pathlib.Path(tmpdir) / "safe_charter.html"
            res = render_artifact("PMO-03.01", lang="en", out_path=out_file)
            self.assertTrue(out_file.exists())
            self.assertEqual(res, out_file.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
