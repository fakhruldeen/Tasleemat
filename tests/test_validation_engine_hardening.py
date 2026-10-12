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


if __name__ == "__main__":
    unittest.main()
