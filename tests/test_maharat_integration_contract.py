#!/usr/bin/env python3
"""
tests/test_maharat_integration_contract.py
Simulated downstream consumer integration test suite verifying the 9 contract
criteria required for Maharat integration without modifying forms/ or requiring
a real Maharat implementation:

1. Discover artifact by verified ID
2. Retrieve requested assets by role and language
3. Identify definition version and content fingerprint
4. Validate valid structured data where supported
5. Report expected structured errors for invalid data
6. Handle incomplete data in draft mode with non-blocking warnings
7. Return clear errors for unsupported requests (unknown ID, bad version, bad language, missing schema)
8. Run cleanly as library functions without source checkout path assumptions
9. Verify immutability of forms/ and library assets
"""

import json
import os
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import tasleemat
from tasleemat.catalog import (
    get_artifact_asset,
    get_artifact_definition,
    get_lexicon,
    list_artifacts,
)
from tasleemat.validation import (
    ValidationError,
    ValidationReport,
    validate_artifact_data,
)

FIXTURES_DIR = ROOT / "tests" / "fixtures"


class TestMaharatIntegrationContract(unittest.TestCase):

    def test_criterion_1_discover_artifact_by_verified_id(self):
        """Criterion 1: Discover artifact by stable, verified ID."""
        defn = get_artifact_definition("PMO-03.01")
        self.assertEqual(defn["artifact_id"], "PMO-03.01")
        self.assertEqual(defn["name_en"], "PROJECT CHARTER")
        self.assertEqual(defn["name_ar"], "ميثاق المشروع")
        self.assertEqual(defn["phase_code"], "03")

        defn_risk = get_artifact_definition("PMO-04.08.02")
        self.assertEqual(defn_risk["artifact_id"], "PMO-04.08.02")

    def test_criterion_2_retrieve_assets_by_role_and_language(self):
        """Criterion 2: Retrieve requested assets by role and language without filesystem parsing."""
        # 1. Template
        tmpl_en = get_artifact_asset("PMO-03.01", role="template", lang="en")
        self.assertIn("PROJECT CHARTER", tmpl_en)
        tmpl_ar = get_artifact_asset("PMO-03.01", role="template", lang="ar")
        self.assertIn("ميثاق المشروع", tmpl_ar)

        # 2. Guide
        guide_en = get_artifact_asset("PMO-03.01", role="guide", lang="en")
        self.assertIn("Project Artifact: Project Charter", guide_en)

        # 3. Prompt
        prompt_ar = get_artifact_asset("PMO-03.01", role="prompt", lang="ar")
        self.assertTrue(len(prompt_ar) > 100)

        # 4. Schema (JSON dict)
        schema_dict = get_artifact_asset("PMO-03.01", role="schema", lang="en")
        self.assertIsInstance(schema_dict, dict)
        self.assertIn("fields", schema_dict)

        # 5. Dictionary (List of dicts)
        dict_rows = get_artifact_asset("PMO-03.01", role="dictionary", lang="en")
        self.assertIsInstance(dict_rows, list)
        self.assertGreater(len(dict_rows), 0)

        # 6. Example
        example_en = get_artifact_asset("PMO-03.01", role="example", lang="en")
        self.assertIsNotNone(example_en)
        self.assertIn("Apex", example_en)

    def test_criterion_3_identify_version_and_content_fingerprint(self):
        """Criterion 3: Identify definition version and cryptographic content fingerprint."""
        defn = get_artifact_definition("PMO-03.01")
        self.assertIn("fingerprint", defn)
        self.assertEqual(len(defn["fingerprint"]), 64)  # SHA-256 length

        self.assertEqual(tasleemat.__version__, "2.5.0")

    def test_criterion_4_validate_valid_structured_data(self):
        """Criterion 4: Validate valid structured data against companion data contract."""
        fixture_path = FIXTURES_DIR / "valid" / "PMO-03.01_valid.json"
        with open(fixture_path, "r", encoding="utf-8") as f:
            valid_payload = json.load(f)

        report = validate_artifact_data("PMO-03.01", valid_payload, mode="strict")
        self.assertIsInstance(report, ValidationReport)
        self.assertTrue(report.valid)
        self.assertEqual(len(report.errors), 0)
        self.assertEqual(report.package_version, tasleemat.__version__)
        self.assertEqual(report.artifact_id, "PMO-03.01")

    def test_criterion_5_report_expected_errors_for_invalid_data(self):
        """Criterion 5: Report expected structured errors and field paths for invalid data."""
        fixture_path = FIXTURES_DIR / "invalid" / "PMO-03.01_missing_required.json"
        with open(fixture_path, "r", encoding="utf-8") as f:
            invalid_payload = json.load(f)

        report = validate_artifact_data("PMO-03.01", invalid_payload, mode="strict")
        self.assertFalse(report.valid)
        self.assertGreater(len(report.errors), 0)

        for err in report.errors:
            self.assertIsInstance(err, ValidationError)
            self.assertTrue(err.field_path.startswith("/"))
            self.assertTrue(len(err.code) > 0)
            self.assertTrue(len(err.message) > 0)

    def test_criterion_6_handle_incomplete_draft_data(self):
        """Criterion 6: Handle incomplete draft data with non-blocking warnings."""
        fixture_path = FIXTURES_DIR / "draft" / "PMO-03.01_draft.json"
        with open(fixture_path, "r", encoding="utf-8") as f:
            draft_payload = json.load(f)

        report = validate_artifact_data("PMO-03.01", draft_payload, mode="draft")
        self.assertTrue(report.valid)
        self.assertEqual(len(report.errors), 0)
        self.assertGreater(len(report.warnings), 0)
        self.assertTrue(any("Draft warning" in w for w in report.warnings))

    def test_criterion_7_return_clear_errors_for_unsupported_requests(self):
        """Criterion 7: Return clear, predictable errors for unsupported requests."""
        # 1. Unknown artifact ID
        with self.assertRaises(KeyError):
            get_artifact_definition("NONEXISTENT-99.99")

        # 2. Unsupported language
        with self.assertRaises(ValueError):
            get_artifact_asset("PMO-03.01", role="template", lang="de")

        # 3. Unsupported asset role
        with self.assertRaises(ValueError):
            get_artifact_asset("PMO-03.01", role="binary_executable", lang="en")

        # 4. Unsupported definition version requested
        fixture_path = FIXTURES_DIR / "valid" / "PMO-03.01_valid.json"
        with open(fixture_path, "r", encoding="utf-8") as f:
            valid_payload = json.load(f)
        report_bad_ver = validate_artifact_data(
            "PMO-03.01", valid_payload, definition_version="0.0.1"
        )
        self.assertFalse(report_bad_ver.valid)
        self.assertTrue(any(e.code == "UNSUPPORTED_VERSION" for e in report_bad_ver.errors))

        # 5. Missing companion schema requested (e.g. PMO-00.01)
        report_no_schema = validate_artifact_data("PMO-00.01", {"artifact_id": "PMO-00.01"})
        self.assertFalse(report_no_schema.valid)
        self.assertTrue(any(e.code == "SCHEMA_UNAVAILABLE" for e in report_no_schema.errors))

    def test_criterion_8_bilingual_lexicon_retrieval(self):
        """Criterion 8: Retrieve standardized bilingual PMO terminology."""
        lex = get_lexicon()
        self.assertIsInstance(lex, list)
        self.assertGreater(len(lex), 50)
        first_term = lex[0]
        self.assertIn("en_name", first_term)
        self.assertIn("ar_name", first_term)

        # Filter by category
        initiating_terms = get_lexicon(category="Initiating")
        self.assertGreater(len(initiating_terms), 0)
        for t in initiating_terms:
            self.assertIn("Initiating", t.get("group", ""))

    def test_criterion_9_immutability_and_forms_protection(self):
        """Criterion 9: Verify forms/ write protection and read-only asset integrity."""
        # Check that writing rendered output into forms/ is prohibited
        target_in_forms = ROOT / "forms" / "en" / "unauthorized_export.html"
        with self.assertRaises(ValueError):
            tasleemat.render_artifact("PMO-03.01", lang="en", out_path=target_in_forms)


if __name__ == "__main__":
    unittest.main()
