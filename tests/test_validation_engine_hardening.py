#!/usr/bin/env python3
"""
tests/test_validation_engine_hardening.py
Verification suite for Tasleemat Validation & Interface Hardening:
- Task A: Pattern enforcement, ISO date format, maxLength, maxItems, and bool-type traps.
- Task B: Strict version compatibility contract whitelist.
- Task C: ValidationReport metadata, definition_fingerprint, schema_id, schema_dialect.
- Task D: Catalog defensive copy, strict tailoring profile validation, path traversal defense.
- Task G: Rendering path traversal and directory containment protection.
- Task H: Mock output prominent unvalidated disclaimer.
"""

import copy
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import tasleemat
from tasleemat.catalog import (
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
from tasleemat.ai import AIClient


class TestValidationEngineHardening(unittest.TestCase):

    def setUp(self):
        self.charter_base = {
            "artifact_id": "PMO-03.01",
            "metadata": {
                "project_name": "Cloud Transformation",
                "project_code": "PRJ-999",
                "date_prepared": "2026-03-15",
                "prepared_by": "Dr. Sarah",
                "sponsor": "Executive VP",
                "version": "1.0",
                "status": "approved",
            },
            "fields": {
                "project_purpose": "Detailed objective for the enterprise cloud modernization.",
                "high_level_project_description": "Migrating on-premise compute nodes to hybrid cloud architecture.",
                "key_deliverables": ["Cloud Architecture Plan", "Security Framework"],
                "project_objectives_and_related_success_criteria": [
                    {"objective": "Zero downtime", "success_criteria": "99.99% SLA"}
                ],
                "summary_milestone_schedule": [
                    {"milestone": "Phase 1 Gate", "target_date": "2026-06-30"}
                ],
            },
        }

    # ==================== TASK A: CONSTRAINT VALIDATION ====================

    def test_pattern_constraint_enforcement(self):
        """Verify that regex pattern constraint is enforced on project_code."""
        payload = copy.deepcopy(self.charter_base)
        # Invalid characters in project_code according to ^[A-Z0-9_-]+$
        payload["metadata"]["project_code"] = "PRJ 999 with spaces!"
        report = validate_artifact_data("PMO-03.01", payload)
        self.assertFalse(report.valid)
        error_codes = [e.code for e in report.errors]
        self.assertIn("PATTERN_VIOLATION", error_codes)

    def test_date_format_constraint_enforcement(self):
        """Verify that date format is enforced as valid ISO YYYY-MM-DD."""
        payload = copy.deepcopy(self.charter_base)
        # Invalid date format
        payload["metadata"]["date_prepared"] = "15/03/2026"
        report = validate_artifact_data("PMO-03.01", payload)
        self.assertFalse(report.valid)
        error_codes = [e.code for e in report.errors]
        self.assertIn("FORMAT_VIOLATION", error_codes)

        # Invalid date value
        payload["metadata"]["date_prepared"] = "2026-02-31"
        report2 = validate_artifact_data("PMO-03.01", payload)
        self.assertFalse(report2.valid)
        self.assertIn("FORMAT_VIOLATION", [e.code for e in report2.errors])

    def test_python_boolean_type_trap(self):
        """Verify that Python bool (True/False) is rejected for integer and number types."""
        risk_payload = {
            "artifact_id": "PMO-04.08.02",
            "metadata": {
                "project_name": "Test Project",
                "project_code": "PRJ-01",
                "last_updated": "2026-03-15",
            },
            "risks": [
                {
                    "risk_id": "RSK-001",
                    "category": "Technical",
                    "event_narrative": "Latency issue during cloud sync",
                    "probability_score": True,  # Boolean passed where integer is expected
                    "impact_score": 4,
                    "response_strategy": "Mitigate",
                    "owner": "Network Lead",
                    "status": "Identified",
                }
            ],
        }
        report = validate_artifact_data("PMO-04.08.02", risk_payload)
        self.assertFalse(report.valid)
        error_codes = [e.code for e in report.errors]
        self.assertIn("TYPE_MISMATCH", error_codes)

    # ==================== TASK B: VERSION CONTRACT ====================

    def test_version_compatibility_strict_whitelist(self):
        """Verify version compatibility strictly accepts valid versions and rejects unknown/dialect URIs."""
        # Valid supported versions
        for v in ["2.5.0", "v2.5.0", "2.4.2", "v2.4.2", "2.4.1", "2.4.0"]:
            rep = validate_artifact_data("PMO-03.01", self.charter_base, definition_version=v)
            self.assertTrue(rep.valid, f"Expected {v} to be supported")

        # Invalid arbitrary strings or dialect URIs must be rejected
        for bad_v in [
            "https://json-schema.org/draft/2020-12/schema",
            "custom_PMO-03.01",
            "3.0.0",
            "invalid_version",
        ]:
            rep_bad = validate_artifact_data("PMO-03.01", self.charter_base, definition_version=bad_v)
            self.assertFalse(rep_bad.valid, f"Expected {bad_v} to be rejected")
            self.assertIn("UNSUPPORTED_VERSION", [e.code for e in rep_bad.errors])

    # ==================== TASK C: TRACEABILITY METADATA ====================

    def test_validation_report_traceability_metadata(self):
        """Verify report returns real SHA-256 fingerprint, schema_id, and schema_dialect."""
        rep = validate_artifact_data("PMO-03.01", self.charter_base)
        self.assertTrue(rep.valid)
        # Definition fingerprint must be a 64-char SHA-256 hash matching catalog
        defn = get_artifact_definition("PMO-03.01")
        self.assertEqual(rep.definition_fingerprint, defn["fingerprint"])
        self.assertEqual(len(rep.definition_fingerprint), 64)
        self.assertEqual(rep.schema_id, "https://tasleemat.pmo/schemas/completed/PMO-03.01.schema.json")
        self.assertEqual(rep.schema_dialect, "https://json-schema.org/draft/2020-12/schema")

        d = rep.to_dict()
        self.assertIn("definition_fingerprint", d)
        self.assertIn("schema_id", d)
        self.assertIn("schema_dialect", d)

    # ==================== TASK D: CATALOG & PROFILE HARDENING ====================

    def test_get_artifact_definition_defensive_deepcopy(self):
        """Verify mutating returned definition does not mutate catalog cache."""
        defn1 = get_artifact_definition("PMO-03.01")
        defn1["name_en"] = "MUTATED NAME"
        defn2 = get_artifact_definition("PMO-03.01")
        self.assertEqual(defn2["name_en"], "PROJECT CHARTER")

    def test_tailoring_profile_validation_errors(self):
        """Verify get_tailoring_profile raises ValueError on invalid tier or pack."""
        with self.assertRaises(ValueError):
            get_tailoring_profile(tier="99")

        with self.assertRaises(ValueError):
            get_tailoring_profile(tier="2", pack="unknown_pack")

        # Valid calls
        t1 = get_tailoring_profile(tier="1", pack="general")
        self.assertGreater(len(t1), 0)

    def test_asset_path_traversal_containment(self):
        """Verify ArtifactAssets._resolve rejects paths escaping repository/package root."""
        assets = get_artifact_assets("PMO-03.01", lang="en")
        with self.assertRaises(ValueError):
            assets._resolve("../../etc/passwd")

    # ==================== TASK G: RENDERING IMMUTABILITY ====================

    def test_rendering_protected_directories(self):
        """Verify render_artifact blocks writing to forms/ and package directory."""
        with self.assertRaises(ValueError):
            render_artifact("PMO-03.01", lang="en", out_path=ROOT / "forms" / "illegal.html")

        with self.assertRaises(ValueError):
            render_artifact("PMO-03.01", lang="en", out_path=ROOT / "tasleemat" / "illegal.html")

    # ==================== TASK H: MOCK DISCLAIMER ====================

    def test_mock_generation_unvalidated_notice(self):
        """Verify mock AI generation emits prominent unvalidated test output disclaimer."""
        client = AIClient(provider="mock")
        res = client.generate("Draft Project Charter for testing", mock=True)
        self.assertIn("UNVALIDATED TEST OUTPUT: NOT SUITABLE FOR PRODUCTION USE", res)
        self.assertIn("MOCK AI GENERATION", res)
        self.assertIn("[MOCK TEST ONLY]", res)

    # ==================== STAGE B TESTS ====================

    def test_unsupported_schema_keyword_detection(self):
        """Verify pure-Python validator flags unsupported JSON schema assertions."""
        schema_with_unsupported = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {
                "name": {"type": "string", "unsupportedAssertion": True}
            }
        }
        from tasleemat.validation import _validate_with_builtin
        errors, warnings = _validate_with_builtin({"name": "test"}, schema_with_unsupported, "strict")
        self.assertTrue(any(e.code == "UNSUPPORTED_SCHEMA_ASSERTION" for e in errors))

    def test_unsupported_artifact_explicit_status(self):
        """Verify validation of deliverable without companion schema returns status='unavailable'."""
        report = validate_artifact_data("PMO-00.01", {"some": "data"})
        self.assertFalse(report.valid)
        self.assertEqual(report.status, "unavailable")
        self.assertFalse(report.is_available)
        self.assertEqual(len(report.errors), 1)
        self.assertEqual(report.errors[0].code, "SCHEMA_UNAVAILABLE")

    def test_artifact_summary_and_lexicon_cache_isolation(self):
        """Verify mutating ArtifactSummary.tiers or get_lexicon() does not pollute cache."""
        from tasleemat.catalog import get_lexicon
        arts1 = list_artifacts()
        arts1[0].tiers.append("DIRTY_TIER")
        arts2 = list_artifacts()
        self.assertNotIn("DIRTY_TIER", arts2[0].tiers)

        lex1 = get_lexicon()
        lex1[0]["dirty_key"] = "DIRTY_VALUE"
        lex2 = get_lexicon()
        self.assertNotIn("dirty_key", lex2[0])

    def test_combined_tier_and_pack_filter_intersection(self):
        """Verify list_artifacts with tier and pack enforces strict intersection."""
        # PMO-02.01 has agile under tier 1, but NOT under tier 2
        arts = list_artifacts(tier="2", pack="agile")
        ids = [a.artifact_id for a in arts]
        self.assertNotIn("PMO-02.01", ids)

    def test_batch_1_pmo_01_01_business_case_validation(self):
        """Verify PMO-01.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-01.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-01.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-01.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-01.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-01.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-01.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_1_pmo_07_03_closeout_validation(self):
        """Verify PMO-07.03 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-07.03_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-07.03_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-07.03_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-07.03", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-07.03", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-07.03", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    # ==================== BATCH 2 COMPANION SCHEMAS ====================

    def test_batch_2_pmo_04_01_01_project_management_plan_validation(self):
        """Verify PMO-04.01.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.01.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.01.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.01.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.01.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)
        self.assertEqual(rep_v.schema_id, "https://tasleemat.pmo/schemas/completed/PMO-04.01.01.schema.json")

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.01.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.01.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_2_pmo_04_02_05_scope_statement_validation(self):
        """Verify PMO-04.02.05 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.02.05_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.02.05_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.02.05_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.02.05", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.02.05", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.02.05", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_2_pmo_04_04_01_cost_management_plan_validation(self):
        """Verify PMO-04.04.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.04.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.04.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.04.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.04.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.04.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.04.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)


if __name__ == "__main__":
    unittest.main()
