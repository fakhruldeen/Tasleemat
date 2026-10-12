"""
Tasleemat Structural Data Validation Engine
Validates completed artifact data payloads against companion schemas.
"""

from __future__ import annotations

import json
import pathlib
import re
import datetime
import copy
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

PACKAGE_DIR = pathlib.Path(__file__).resolve().parent
SCHEMAS_DIR = PACKAGE_DIR / "schemas" / "completed"

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


@dataclass(frozen=True)
class ValidationError:
    code: str
    message: str
    field_path: str
    schema_rule: str


@dataclass
class ValidationReport:
    valid: bool
    artifact_id: str
    schema_version: str
    fingerprint: str
    mode: str
    package_version: str = "2.5.0"
    definition_fingerprint: str = ""
    schema_id: str = ""
    schema_dialect: str = ""
    errors: List[ValidationError] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.definition_fingerprint and self.fingerprint:
            self.definition_fingerprint = self.fingerprint
        if not self.fingerprint and self.definition_fingerprint:
            self.fingerprint = self.definition_fingerprint

    def to_dict(self) -> Dict[str, Any]:
        return {
            "valid": self.valid,
            "package_version": self.package_version,
            "artifact_id": self.artifact_id,
            "schema_version": self.schema_version,
            "fingerprint": self.fingerprint,
            "definition_fingerprint": self.definition_fingerprint,
            "schema_id": self.schema_id,
            "schema_dialect": self.schema_dialect,
            "mode": self.mode,
            "errors": [
                {
                    "code": e.code,
                    "message": e.message,
                    "field_path": e.field_path,
                    "schema_rule": e.schema_rule,
                }
                for e in self.errors
            ],
            "warnings": self.warnings,
        }


def _load_schema(artifact_id: str) -> Dict[str, Any]:
    norm_id = artifact_id.upper().strip()
    schema_file = SCHEMAS_DIR / f"{norm_id}.schema.json"
    if not schema_file.exists():
        raise KeyError(
            f"No completed-data schema found for artifact ID '{artifact_id}'. "
            f"Expected schema at: {schema_file}"
        )
    with open(schema_file, "r", encoding="utf-8") as f:
        return json.load(f)


def _validate_with_builtin(
    data: Dict[str, Any], schema: Dict[str, Any], mode: str
) -> tuple[list[ValidationError], list[str]]:
    """Pure-Python structural validator ensuring zero mandatory third-party requirements."""
    errors: list[ValidationError] = []
    warnings: list[str] = []

    def check_node(val: Any, rule: Dict[str, Any], path: str):
        expected_type = rule.get("type")
        if expected_type == "object":
            if not isinstance(val, dict):
                errors.append(
                    ValidationError(
                        code="TYPE_MISMATCH",
                        message=f"Expected object at {path or '/'}, got {type(val).__name__}",
                        field_path=path or "/",
                        schema_rule="type:object",
                    )
                )
                return

            req = rule.get("required", [])
            for r in req:
                if r not in val:
                    err = ValidationError(
                        code="REQUIRED_FIELD_MISSING",
                        message=f"Missing required field '{r}' at {path or '/'}",
                        field_path=f"{path}/{r}",
                        schema_rule="required",
                    )
                    if mode == "draft" and path != "":
                        warnings.append(f"Draft warning: {err.message}")
                    else:
                        errors.append(err)

            props = rule.get("properties", {})
            for k, child_val in val.items():
                if k in props:
                    check_node(child_val, props[k], f"{path}/{k}")

        elif expected_type == "array":
            if not isinstance(val, list):
                errors.append(
                    ValidationError(
                        code="TYPE_MISMATCH",
                        message=f"Expected array at {path}, got {type(val).__name__}",
                        field_path=path,
                        schema_rule="type:array",
                    )
                )
                return

            min_items = rule.get("minItems")
            if min_items is not None and len(val) < min_items:
                err = ValidationError(
                    code="MIN_ITEMS_VIOLATION",
                    message=f"Array at {path} must contain at least {min_items} items, got {len(val)}",
                    field_path=path,
                    schema_rule=f"minItems:{min_items}",
                )
                if mode == "draft":
                    warnings.append(f"Draft warning: {err.message}")
                else:
                    errors.append(err)

            max_items = rule.get("maxItems")
            if max_items is not None and len(val) > max_items:
                errors.append(
                    ValidationError(
                        code="MAX_ITEMS_VIOLATION",
                        message=f"Array at {path} must contain at most {max_items} items, got {len(val)}",
                        field_path=path,
                        schema_rule=f"maxItems:{max_items}",
                    )
                )

            item_rule = rule.get("items")
            if item_rule:
                for idx, item in enumerate(val):
                    check_node(item, item_rule, f"{path}/{idx}")

        elif expected_type == "string":
            if not isinstance(val, str):
                errors.append(
                    ValidationError(
                        code="TYPE_MISMATCH",
                        message=f"Expected string at {path}, got {type(val).__name__}",
                        field_path=path,
                        schema_rule="type:string",
                    )
                )
                return
            min_len = rule.get("minLength")
            if min_len is not None and len(val) < min_len:
                errors.append(
                    ValidationError(
                        code="MIN_LENGTH_VIOLATION",
                        message=f"String at {path} is shorter than minimum length {min_len}",
                        field_path=path,
                        schema_rule=f"minLength:{min_len}",
                    )
                )
            max_len = rule.get("maxLength")
            if max_len is not None and len(val) > max_len:
                errors.append(
                    ValidationError(
                        code="MAX_LENGTH_VIOLATION",
                        message=f"String at {path} exceeds maximum length {max_len}",
                        field_path=path,
                        schema_rule=f"maxLength:{max_len}",
                    )
                )
            pattern = rule.get("pattern")
            if pattern is not None:
                if not re.search(pattern, val):
                    errors.append(
                        ValidationError(
                            code="PATTERN_VIOLATION",
                            message=f"String '{val}' at {path} does not match required pattern '{pattern}'",
                            field_path=path,
                            schema_rule=f"pattern:{pattern}",
                        )
                    )
            fmt = rule.get("format")
            if fmt == "date":
                # Validate standard YYYY-MM-DD
                try:
                    datetime.date.fromisoformat(val)
                except (ValueError, TypeError):
                    errors.append(
                        ValidationError(
                            code="FORMAT_VIOLATION",
                            message=f"String '{val}' at {path} does not match required format 'date' (YYYY-MM-DD)",
                            field_path=path,
                            schema_rule="format:date",
                        )
                    )
            enum_vals = rule.get("enum")
            if enum_vals and val not in enum_vals:
                errors.append(
                    ValidationError(
                        code="ENUM_VIOLATION",
                        message=f"Value '{val}' at {path} not in allowed options {enum_vals}",
                        field_path=path,
                        schema_rule="enum",
                    )
                )
            const_val = rule.get("const")
            if const_val is not None and val != const_val:
                errors.append(
                    ValidationError(
                        code="CONST_VIOLATION",
                        message=f"Value '{val}' at {path} does not match constant '{const_val}'",
                        field_path=path,
                        schema_rule="const",
                    )
                )

        elif expected_type in ("integer", "number"):
            # Avoid Python bool trap: bool is a subclass of int in Python
            if isinstance(val, bool) or not isinstance(val, (int, float)) or (expected_type == "integer" and not isinstance(val, int)):
                errors.append(
                    ValidationError(
                        code="TYPE_MISMATCH",
                        message=f"Expected {expected_type} at {path}, got {type(val).__name__}",
                        field_path=path,
                        schema_rule=f"type:{expected_type}",
                    )
                )
                return
            minimum = rule.get("minimum")
            if minimum is not None and val < minimum:
                errors.append(
                    ValidationError(
                        code="MINIMUM_VIOLATION",
                        message=f"Value {val} at {path} is less than minimum {minimum}",
                        field_path=path,
                        schema_rule=f"minimum:{minimum}",
                    )
                )
            maximum = rule.get("maximum")
            if maximum is not None and val > maximum:
                errors.append(
                    ValidationError(
                        code="MAXIMUM_VIOLATION",
                        message=f"Value {val} at {path} is greater than maximum {maximum}",
                        field_path=path,
                        schema_rule=f"maximum:{maximum}",
                    )
                )

    check_node(data, schema, "")
    return errors, warnings


def validate_artifact_data(
    artifact_id: str,
    data: Dict[str, Any],
    definition_version: Optional[str] = None,
    mode: str = "strict",
) -> ValidationReport:
    """
    Validate a completed artifact data payload against the artifact's companion schema.

    Parameters:
        artifact_id: PMO identifier, e.g. "PMO-03.01"
        data: Dict containing completed artifact data
        definition_version: Optional schema version tag
        mode: "strict" (default) or "draft" (lenient for in-progress documents)

    Returns:
        ValidationReport with valid flag, errors, warnings, and field paths.
    """
    import tasleemat
    from tasleemat.catalog import get_artifact_definition

    current_pkg_version = getattr(tasleemat, "__version__", "2.4.2")
    norm_id = artifact_id.upper().strip()
    norm_mode = mode.lower().strip()
    if norm_mode not in ("strict", "draft"):
        raise ValueError(f"Invalid validation mode '{mode}'. Choose 'strict' or 'draft'.")

    # Resolve deliverable SHA-256 fingerprint from catalog
    real_fingerprint = ""
    try:
        art_def = get_artifact_definition(norm_id)
        real_fingerprint = art_def.get("fingerprint", "")
    except Exception:
        pass

    # Check payload type
    if not isinstance(data, dict):
        return ValidationReport(
            valid=False,
            artifact_id=norm_id,
            schema_version="",
            fingerprint=real_fingerprint,
            definition_fingerprint=real_fingerprint,
            package_version=current_pkg_version,
            mode=norm_mode,
            errors=[
                ValidationError(
                    code="INVALID_PAYLOAD",
                    message=f"Data payload must be a dictionary object, got {type(data).__name__}.",
                    field_path="/",
                    schema_rule="type:object",
                )
            ],
            warnings=[],
        )

    # Check companion schema availability
    try:
        schema = _load_schema(norm_id)
    except KeyError as exc:
        return ValidationReport(
            valid=False,
            artifact_id=norm_id,
            schema_version="",
            fingerprint=real_fingerprint,
            definition_fingerprint=real_fingerprint,
            package_version=current_pkg_version,
            mode=norm_mode,
            errors=[
                ValidationError(
                    code="SCHEMA_UNAVAILABLE",
                    message=f"Companion completed-data schema not available for artifact '{artifact_id}'.",
                    field_path="/",
                    schema_rule="schema_existence",
                )
            ],
            warnings=[],
        )

    schema_id = schema.get("$id", f"https://tasleemat.pmo/schemas/completed/{norm_id}.schema.json")
    schema_dialect = schema.get("$schema", "https://json-schema.org/draft/2020-12/schema")

    # Verify version compatibility if requested
    # Strict deterministic whitelist of supported versions
    if definition_version:
        supported_versions = {
            "2.5.0", "v2.5.0",
            "2.4.2", "v2.4.2",
            "2.4.1", "v2.4.1",
            "2.4.0", "v2.4.0",
            "2.3.1", "v2.3.1",
        }
        if definition_version not in supported_versions:
            return ValidationReport(
                valid=False,
                package_version=current_pkg_version,
                artifact_id=norm_id,
                schema_version=schema_dialect,
                schema_id=schema_id,
                schema_dialect=schema_dialect,
                fingerprint=real_fingerprint,
                definition_fingerprint=real_fingerprint,
                mode=norm_mode,
                errors=[
                    ValidationError(
                        code="UNSUPPORTED_VERSION",
                        message=(
                            f"Requested definition version '{definition_version}' is not supported "
                            f"by installed Tasleemat package (v{current_pkg_version})."
                        ),
                        field_path="/",
                        schema_rule="version_compatibility",
                    )
                ],
                warnings=[],
            )

    errors, warnings = _validate_with_builtin(data, schema, norm_mode)
    is_valid = len(errors) == 0

    return ValidationReport(
        valid=is_valid,
        artifact_id=norm_id,
        schema_version=schema_dialect,
        schema_id=schema_id,
        schema_dialect=schema_dialect,
        fingerprint=real_fingerprint,
        definition_fingerprint=real_fingerprint,
        package_version=current_pkg_version,
        mode=norm_mode,
        errors=errors,
        warnings=warnings,
    )
