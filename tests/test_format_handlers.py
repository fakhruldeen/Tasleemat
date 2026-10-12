"""
Tests for Centralized Format Registry, Assertion Handlers, and Preflight Enforcement.
"""

import copy
import pytest
from tasleemat.formats import (
    FORMAT_HANDLERS,
    SUPPORTED_FORMATS,
    check_format,
    validate_date,
    validate_date_time,
    validate_time,
    validate_uuid,
    validate_uri,
    validate_uri_reference,
    validate_email,
    validate_duration,
)
from tasleemat.validation import (
    preflight_schema,
    validate_artifact_data,
    _validate_with_builtin,
    _load_schema,
)


class TestFormatRegistryAndHandlers:
    """Verifies that format handlers adhere strictly to specifications and boundaries."""

    def test_supported_formats_registry_structure(self):
        expected_formats = {"date", "date-time", "time", "uuid", "uri", "uri-reference", "email", "duration"}
        assert SUPPORTED_FORMATS == expected_formats
        for fmt in expected_formats:
            assert fmt in FORMAT_HANDLERS
            handler, desc = FORMAT_HANDLERS[fmt]
            assert callable(handler)
            assert isinstance(desc, str) and len(desc) > 0

    def test_check_format_helper(self):
        is_valid, desc = check_format("date", "2026-10-12")
        assert is_valid is True
        assert "RFC 3339" in desc

        is_valid, _ = check_format("date", "not-a-date")
        assert is_valid is False

        with pytest.raises(KeyError, match="Unsupported format"):
            check_format("unsupported-fmt", "value")

    # --- Batch 1: Date and Timestamp Handling ---

    def test_date_handler_boundaries(self):
        # Valid cases
        assert validate_date("2026-10-12") is True
        assert validate_date("2024-02-29") is True  # 2024 is leap year
        assert validate_date("2000-02-29") is True  # 2000 is century leap year

        # Impossible dates / non-leap year
        assert validate_date("2026-02-29") is False
        assert validate_date("1900-02-29") is False  # 1900 not leap year
        assert validate_date("2026-04-31") is False  # April has 30 days
        assert validate_date("2026-13-01") is False  # Month > 12
        assert validate_date("2026-00-10") is False  # Month 0

        # Syntax violations
        assert validate_date("2026-2-5") is False    # Missing zero-padding
        assert validate_date("20260205") is False    # Compact date rejection
        assert validate_date("2026/02/05") is False  # Wrong separator
        assert validate_date("26-02-05") is False    # 2-digit year
        assert validate_date("") is False
        assert validate_date(12345) is False

    def test_date_time_handler_boundaries(self):
        # Valid cases: Z, positive and negative offsets, fractional seconds
        assert validate_date_time("2026-10-12T14:30:00Z") is True
        assert validate_date_time("2026-10-12t14:30:00z") is True
        assert validate_date_time("2026-10-12T14:30:00.123456Z") is True
        assert validate_date_time("2026-10-12T17:30:00+03:00") is True
        assert validate_date_time("2026-10-12T09:30:00-05:00") is True
        assert validate_date_time("2026-10-12T23:59:60Z") is True  # Leap second

        # Invalid cases
        assert validate_date_time("2026-10-12 14:30:00Z") is False       # Space instead of T
        assert validate_date_time("2026-10-12T14:30:00") is False         # Missing timezone offset
        assert validate_date_time("2026-02-29T14:30:00Z") is False        # Invalid calendar date (non-leap)
        assert validate_date_time("2026-10-12T25:00:00Z") is False        # Invalid hour > 23
        assert validate_date_time("2026-10-12T14:60:00Z") is False        # Invalid minute > 59
        assert validate_date_time("2026-10-12T14:30:61Z") is False        # Invalid second > 60
        assert validate_date_time("not-a-datetime") is False

    def test_time_handler_boundaries(self):
        # Valid cases
        assert validate_time("14:30:00") is True
        assert validate_time("14:30:00.999") is True
        assert validate_time("14:30:00Z") is True
        assert validate_time("14:30:00+03:00") is True
        assert validate_time("23:59:60") is True  # Leap second

        # Invalid cases
        assert validate_time("24:00:00") is False
        assert validate_time("14:60:00") is False
        assert validate_time("14:30") is False  # Missing seconds
        assert validate_time("2:30:00") is False  # Missing padding

    # --- Batch 2: Identifiers and Resource References ---

    def test_uuid_handler_boundaries(self):
        # Valid RFC 4122 UUID strings
        assert validate_uuid("123e4567-e89b-12d3-a456-426614174000") is True
        assert validate_uuid("c73bcdcc-2669-4bf6-81d3-e4ae73fb11ff") is True
        assert validate_uuid("C73BCDCC-2669-4BF6-81D3-E4AE73FB11FF") is True

        # Plain UUID required; URNs belong under URI validation
        assert validate_uuid("urn:uuid:123e4567-e89b-12d3-a456-426614174000") is False
        # Compact / unhyphenated
        assert validate_uuid("123e4567e89b12d3a456426614174000") is False
        # Malformed group lengths or invalid chars
        assert validate_uuid("123e4567-e89b-12d3-a456-42661417400") is False
        assert validate_uuid("123e4567-e89b-12d3-a456-42661417400g") is False
        assert validate_uuid("") is False

    def test_uri_handler_boundaries(self):
        # Absolute URIs with schemes
        assert validate_uri("https://example.com/api/v1") is True
        assert validate_uri("urn:isbn:0451450523") is True
        assert validate_uri("ftp://ftp.example.com/file.txt") is True
        assert validate_uri("mailto:user@example.com") is True
        assert validate_uri("urn:uuid:123e4567-e89b-12d3-a456-426614174000") is True

        # Missing scheme / relative references
        assert validate_uri("/relative/path") is False
        assert validate_uri("relative/path") is False
        assert validate_uri("example.com/api") is False
        # Whitespace
        assert validate_uri("https://example.com/path with spaces") is False
        assert validate_uri("") is False

    def test_uri_reference_handler_boundaries(self):
        # Absolute and relative references
        assert validate_uri_reference("https://example.com/api") is True
        assert validate_uri_reference("/relative/path") is True
        assert validate_uri_reference("relative/path#section") is True
        assert validate_uri_reference("#fragment-only") is True

        # Whitespace violations
        assert validate_uri_reference("path with space") is False

    # --- Batch 3: Contact and Duration Formats ---

    def test_email_handler_boundaries(self):
        # Valid standard emails
        assert validate_email("user@example.com") is True
        assert validate_email("first.last+tag@sub.domain.org") is True
        assert validate_email("support@tasleemat.dev") is True

        # Invalid emails
        assert validate_email("plainaddress") is False
        assert validate_email("@missinglocal.com") is False
        assert validate_email("missingdomain@") is False
        assert validate_email("user@domain") is False  # Must have domain label
        assert validate_email("user@.com") is False
        assert validate_email("user space@example.com") is False
        # Length check (> 254 chars)
        assert validate_email("a" * 250 + "@example.com") is False

    def test_duration_handler_boundaries(self):
        # Valid ISO 8601 durations
        assert validate_duration("P3Y6M4DT12H30M5S") is True
        assert validate_duration("P4W") is True
        assert validate_duration("PT15M") is True
        assert validate_duration("P1D") is True
        assert validate_duration("PT0.5S") is True

        # Invalid durations
        assert validate_duration("P") is False
        assert validate_duration("PT") is False
        assert validate_duration("P1Y2M3DT") is False  # Bare T at end
        assert validate_duration("3 days") is False    # English prose rejected
        assert validate_duration("2 weeks") is False
        assert validate_duration("10h") is False


class TestPreflightAndFormatAssertions:
    """Verifies schema preflight independent inspection and format assertion enforcement."""

    def test_preflight_detects_unsupported_format_in_absent_property(self):
        schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {
                "active_prop": {"type": "string"},
                "unexercised_prop": {
                    "type": "string",
                    "format": "unsupported-custom-format",
                },
            },
        }
        errors = preflight_schema(schema)
        assert len(errors) == 1
        assert errors[0].code == "UNSUPPORTED_FORMAT_ASSERTION"
        assert "unsupported-custom-format" in errors[0].message
        assert errors[0].field_path == "#/properties/unexercised_prop"

    def test_preflight_detects_malformed_format_keyword(self):
        schema = {
            "type": "object",
            "properties": {
                "field": {
                    "type": "string",
                    "format": 12345,  # Must be string
                }
            },
        }
        errors = preflight_schema(schema)
        assert len(errors) == 1
        assert errors[0].code == "MALFORMED_SCHEMA_KEYWORD"
        assert "must be a string" in errors[0].message

    def test_format_assertion_emits_format_violation_with_field_path(self):
        schema = {
            "type": "object",
            "required": ["uid", "target_date", "contact_email"],
            "properties": {
                "uid": {"type": "string", "format": "uuid"},
                "target_date": {"type": "string", "format": "date"},
                "contact_email": {"type": "string", "format": "email"},
            },
        }
        payload = {
            "uid": "not-a-uuid",
            "target_date": "2026-02-29",  # Invalid calendar date
            "contact_email": "invalid-email",
        }
        errors, warnings = _validate_with_builtin(payload, schema, mode="strict")
        assert len(errors) == 3
        codes = {e.code for e in errors}
        paths = {e.field_path for e in errors}
        assert codes == {"FORMAT_VIOLATION"}
        assert paths == {"/uid", "/target_date", "/contact_email"}

    def test_strict_and_draft_modes_reject_malformed_supplied_dates(self):
        schema = {
            "type": "object",
            "required": ["artifact_id", "metadata"],
            "properties": {
                "artifact_id": {"type": "string", "const": "PMO-05.01"},
                "metadata": {
                    "type": "object",
                    "properties": {
                        "date_prepared": {"type": "string", "format": "date"}
                    }
                },
                "issues": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "target_resolution_date": {"type": "string", "format": "date"}
                        }
                    }
                }
            }
        }
        # Incomplete payload (draft), but supplied date values are invalid
        payload = {
            "artifact_id": "PMO-05.01",
            "metadata": {
                "date_prepared": "2026-02-31"  # Invalid calendar date
            },
            "issues": [
                {
                    "target_resolution_date": "2026-2-5"  # Non-zero-padded date
                }
            ]
        }
        # Strict mode
        strict_errors, _ = _validate_with_builtin(payload, schema, mode="strict")
        # Draft mode
        draft_errors, _ = _validate_with_builtin(payload, schema, mode="draft")

        assert len(strict_errors) == 2
        assert len(draft_errors) == 2
        assert [e.code for e in strict_errors] == ["FORMAT_VIOLATION", "FORMAT_VIOLATION"]
        assert [e.code for e in draft_errors] == ["FORMAT_VIOLATION", "FORMAT_VIOLATION"]
        assert [e.field_path for e in strict_errors] == ["/metadata/date_prepared", "/issues/0/target_resolution_date"]
        assert [e.field_path for e in draft_errors] == ["/metadata/date_prepared", "/issues/0/target_resolution_date"]
