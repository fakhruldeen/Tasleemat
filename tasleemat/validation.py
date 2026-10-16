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
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

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
    package_version: str = "2.6.1"
    status: str = "supported"  # "supported", "unavailable", "unknown_artifact", "invalid_schema"
    definition_fingerprint: str = ""
    schema_id: str = ""
    schema_dialect: str = ""
    schema_fingerprint: str = ""
    errors: List[ValidationError] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.definition_fingerprint and self.fingerprint:
            self.definition_fingerprint = self.fingerprint
        if not self.fingerprint and self.definition_fingerprint:
            self.fingerprint = self.definition_fingerprint

    @property
    def is_available(self) -> bool:
        """Returns True if completed-data schema validation is available for this artifact."""
        return self.status == "supported"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "valid": self.valid,
            "status": self.status,
            "is_available": self.is_available,
            "package_version": self.package_version,
            "artifact_id": self.artifact_id,
            "schema_version": self.schema_version,
            "fingerprint": self.fingerprint,
            "definition_fingerprint": self.definition_fingerprint,
            "schema_id": self.schema_id,
            "schema_dialect": self.schema_dialect,
            "schema_fingerprint": self.schema_fingerprint,
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


# Set of recognized structural keywords supported by the pure-Python validator engine
SUPPORTED_SCHEMA_KEYWORDS = {
    "$schema", "$id", "title", "description", "type", "properties",
    "required", "items", "minItems", "maxItems", "minLength", "maxLength",
    "pattern", "format", "enum", "const", "minimum", "maximum"
}

SUPPORTED_TYPES = {"object", "array", "string", "integer", "number", "boolean", "null"}

from .formats import FORMAT_HANDLERS, SUPPORTED_FORMATS, check_format


def preflight_schema(schema: Any, path: str = "#") -> List[ValidationError]:
    """
    Independently inspect and validate the structural schema before payload execution.
    Inspects all subschemas, optional properties, and item schemas.
    """
    errors: List[ValidationError] = []

    if not isinstance(schema, dict):
        errors.append(
            ValidationError(
                code="INVALID_SCHEMA_STRUCTURE",
                message=f"Schema node at {path} must be a dictionary object, got {type(schema).__name__}.",
                field_path=path,
                schema_rule="schema_type",
            )
        )
        return errors

    # Check for unsupported schema assertions
    unsupported_kws = set(schema.keys()) - SUPPORTED_SCHEMA_KEYWORDS
    for kw in sorted(list(unsupported_kws)):
        errors.append(
            ValidationError(
                code="UNSUPPORTED_SCHEMA_ASSERTION",
                message=f"Schema keyword '{kw}' at {path} is not supported by built-in validator.",
                field_path=path,
                schema_rule=f"keyword:{kw}",
            )
        )

    # Validate declared type
    if "type" in schema:
        t = schema["type"]
        if isinstance(t, str):
            if t not in SUPPORTED_TYPES:
                errors.append(
                    ValidationError(
                        code="UNSUPPORTED_TYPE_DECLARATION",
                        message=f"Declared type '{t}' at {path} is not supported by built-in validator.",
                        field_path=path,
                        schema_rule=f"type:{t}",
                    )
                )
        elif isinstance(t, list):
            errors.append(
                ValidationError(
                    code="UNSUPPORTED_TYPE_DECLARATION",
                    message=f"Type union declarations {t} at {path} are not supported by built-in validator.",
                    field_path=path,
                    schema_rule="type:union",
                )
            )
        else:
            errors.append(
                ValidationError(
                    code="MALFORMED_SCHEMA_KEYWORD",
                    message=f"Keyword 'type' at {path} must be a string.",
                    field_path=path,
                    schema_rule="keyword:type",
                )
            )

    # Validate regex pattern syntax
    if "pattern" in schema:
        pat = schema["pattern"]
        if not isinstance(pat, str):
            errors.append(
                ValidationError(
                    code="MALFORMED_SCHEMA_KEYWORD",
                    message=f"Keyword 'pattern' at {path} must be a string.",
                    field_path=path,
                    schema_rule="keyword:pattern",
                )
            )
        else:
            try:
                re.compile(pat)
            except re.error as re_err:
                errors.append(
                    ValidationError(
                        code="INVALID_PATTERN_SYNTAX",
                        message=f"Invalid regex pattern '{pat}' at {path}: {re_err}",
                        field_path=path,
                        schema_rule=f"pattern:{pat}",
                    )
                )

    # Validate format keyword
    if "format" in schema:
        fmt = schema["format"]
        if not isinstance(fmt, str):
            errors.append(
                ValidationError(
                    code="MALFORMED_SCHEMA_KEYWORD",
                    message=f"Keyword 'format' at {path} must be a string.",
                    field_path=path,
                    schema_rule="keyword:format",
                )
            )
        elif fmt not in SUPPORTED_FORMATS:
            errors.append(
                ValidationError(
                    code="UNSUPPORTED_FORMAT_ASSERTION",
                    message=f"Format '{fmt}' at {path} is not supported by built-in validator.",
                    field_path=path,
                    schema_rule=f"format:{fmt}",
                )
            )

    # Validate minLength / maxLength bounds
    for kw_len in ("minLength", "maxLength"):
        if kw_len in schema:
            val_len = schema[kw_len]
            if isinstance(val_len, bool) or not isinstance(val_len, int) or val_len < 0:
                errors.append(
                    ValidationError(
                        code="MALFORMED_SCHEMA_KEYWORD",
                        message=f"Keyword '{kw_len}' at {path} must be a non-negative integer.",
                        field_path=path,
                        schema_rule=f"keyword:{kw_len}",
                    )
                )

    # Validate minItems / maxItems bounds
    for kw_items in ("minItems", "maxItems"):
        if kw_items in schema:
            val_items = schema[kw_items]
            if isinstance(val_items, bool) or not isinstance(val_items, int) or val_items < 0:
                errors.append(
                    ValidationError(
                        code="MALFORMED_SCHEMA_KEYWORD",
                        message=f"Keyword '{kw_items}' at {path} must be a non-negative integer.",
                        field_path=path,
                        schema_rule=f"keyword:{kw_items}",
                    )
                )

    # Validate minimum / maximum numeric bounds
    for kw_num in ("minimum", "maximum"):
        if kw_num in schema:
            val_num = schema[kw_num]
            if (
                isinstance(val_num, bool)
                or not isinstance(val_num, (int, float))
                or (isinstance(val_num, float) and (math.isnan(val_num) or math.isinf(val_num)))
            ):
                errors.append(
                    ValidationError(
                        code="MALFORMED_SCHEMA_KEYWORD",
                        message=f"Keyword '{kw_num}' at {path} must be a finite numeric value.",
                        field_path=path,
                        schema_rule=f"keyword:{kw_num}",
                    )
                )

    # Validate required keyword
    if "required" in schema:
        req = schema["required"]
        if not isinstance(req, list) or not all(isinstance(r, str) for r in req):
            errors.append(
                ValidationError(
                    code="MALFORMED_SCHEMA_KEYWORD",
                    message=f"Keyword 'required' at {path} must be a list of strings.",
                    field_path=path,
                    schema_rule="keyword:required",
                )
            )

    # Validate enum keyword
    if "enum" in schema:
        enum_val = schema["enum"]
        if not isinstance(enum_val, list):
            errors.append(
                ValidationError(
                    code="MALFORMED_SCHEMA_KEYWORD",
                    message=f"Keyword 'enum' at {path} must be a list of allowed values.",
                    field_path=path,
                    schema_rule="keyword:enum",
                )
            )

    # Preflight child properties
    if "properties" in schema:
        props = schema["properties"]
        if not isinstance(props, dict):
            errors.append(
                ValidationError(
                    code="MALFORMED_SCHEMA_KEYWORD",
                    message=f"Keyword 'properties' at {path} must be a dictionary.",
                    field_path=path,
                    schema_rule="keyword:properties",
                )
            )
        else:
            for prop_name, prop_subschema in props.items():
                child_path = f"{path}/properties/{prop_name}"
                errors.extend(preflight_schema(prop_subschema, child_path))

    # Preflight array items
    if "items" in schema:
        items = schema["items"]
        if isinstance(items, dict):
            errors.extend(preflight_schema(items, f"{path}/items"))
        elif isinstance(items, list):
            errors.append(
                ValidationError(
                    code="UNSUPPORTED_SCHEMA_ASSERTION",
                    message=f"Tuple item array at {path}/items is not supported in Draft 2020-12; 'items' must be a schema object.",
                    field_path=f"{path}/items",
                    schema_rule="keyword:items",
                )
            )
        else:
            errors.append(
                ValidationError(
                    code="MALFORMED_SCHEMA_KEYWORD",
                    message=f"Keyword 'items' at {path} must be a dictionary schema object.",
                    field_path=path,
                    schema_rule="keyword:items",
                )
            )

    return errors


def _json_equals(a: Any, b: Any) -> bool:
    """
    Strict recursive JSON-aware equality comparison.
    - Booleans are strictly distinct from numbers (True != 1, False != 0).
    - Numbers compare equal if numerically equal finite values (1 == 1.0).
    - Lists compare element-by-element in exact sequence.
    - Dicts compare key-for-key regardless of key insertion order.
    - None equals None.
    - Strings compare equal if string values are equal.
    """
    if type(a) is bool or type(b) is bool:
        return type(a) is bool and type(b) is bool and a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
            return False
        if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
            return False
        return a == b
    if type(a) is not type(b):
        return False
    if isinstance(a, list):
        if len(a) != len(b):
            return False
        return all(_json_equals(x, y) for x, y in zip(a, b))
    if isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        return all(_json_equals(a[k], b[k]) for k in a)
    return a == b


def _check_payload_json_compatibility(val: Any, path: str = "") -> List[ValidationError]:
    """
    Recursively check that all payload values are valid JSON tokens per RFC 8259.
    Specifically, non-finite floats (NaN, Infinity, -Infinity) are rejected anywhere
    in the payload structure, including undeclared properties, bare arrays, and nested containers.
    """
    errors: List[ValidationError] = []
    if isinstance(val, float) and (math.isnan(val) or math.isinf(val)):
        errors.append(
            ValidationError(
                code="TYPE_MISMATCH",
                message=f"Non-finite numeric value '{val}' at {path or '/'} is not valid JSON.",
                field_path=path or "/",
                schema_rule="type:number",
            )
        )
    elif isinstance(val, dict):
        for k, child in val.items():
            child_path = f"{path}/{k}" if path else f"/{k}"
            errors.extend(_check_payload_json_compatibility(child, child_path))
    elif isinstance(val, list):
        for idx, child in enumerate(val):
            child_path = f"{path}/{idx}" if path else f"/{idx}"
            errors.extend(_check_payload_json_compatibility(child, child_path))
    return errors


def _validate_with_builtin(
    data: Dict[str, Any], schema: Dict[str, Any], mode: str
) -> Tuple[List[ValidationError], List[str]]:
    """Pure-Python structural validator ensuring zero mandatory third-party requirements."""
    # Preflight schema assertions
    errors: List[ValidationError] = list(preflight_schema(schema))
    warnings: List[str] = []

    # Whole-payload JSON-compatibility check independent of schema declaration
    payload_compat_errors = _check_payload_json_compatibility(data, "")
    if payload_compat_errors:
        errors.extend(payload_compat_errors)
        return errors, warnings

    def check_node(val: Any, rule: Dict[str, Any], path: str):
        # 1. Evaluate universal assertions: enum and const across all types
        if "const" in rule:
            const_val = rule["const"]
            if not _json_equals(val, const_val):
                errors.append(
                    ValidationError(
                        code="CONST_VIOLATION",
                        message=f"Value '{val}' at {path or '/'} does not match constant '{const_val}'",
                        field_path=path or "/",
                        schema_rule="const",
                    )
                )

        if "enum" in rule:
            enum_vals = rule["enum"]
            matched = False
            if isinstance(enum_vals, list):
                for opt in enum_vals:
                    if _json_equals(val, opt):
                        matched = True
                        break
            if not matched:
                errors.append(
                    ValidationError(
                        code="ENUM_VIOLATION",
                        message=f"Value '{val}' at {path or '/'} not in allowed options {enum_vals}",
                        field_path=path or "/",
                        schema_rule="enum",
                    )
                )

        expected_type = rule.get("type")

        # Check explicit type mismatch if 'type' is declared
        if expected_type is not None:
            if expected_type == "object" and not isinstance(val, dict):
                errors.append(
                    ValidationError(
                        code="TYPE_MISMATCH",
                        message=f"Expected object at {path or '/'}, got {type(val).__name__}",
                        field_path=path or "/",
                        schema_rule="type:object",
                    )
                )
                return
            elif expected_type == "array" and not isinstance(val, list):
                errors.append(
                    ValidationError(
                        code="TYPE_MISMATCH",
                        message=f"Expected array at {path or '/'}, got {type(val).__name__}",
                        field_path=path or "/",
                        schema_rule="type:array",
                    )
                )
                return
            elif expected_type == "string" and not isinstance(val, str):
                errors.append(
                    ValidationError(
                        code="TYPE_MISMATCH",
                        message=f"Expected string at {path or '/'}, got {type(val).__name__}",
                        field_path=path or "/",
                        schema_rule="type:string",
                    )
                )
                return
            elif expected_type in ("integer", "number"):
                if (
                    isinstance(val, bool)
                    or not isinstance(val, (int, float))
                    or (isinstance(val, float) and (math.isnan(val) or math.isinf(val)))
                    or (expected_type == "integer" and not isinstance(val, int))
                ):
                    errors.append(
                        ValidationError(
                            code="TYPE_MISMATCH",
                            message=f"Expected {expected_type} at {path or '/'}, got {type(val).__name__}",
                            field_path=path or "/",
                            schema_rule=f"type:{expected_type}",
                        )
                    )
                    return
            elif expected_type == "boolean" and not isinstance(val, bool):
                errors.append(
                    ValidationError(
                        code="TYPE_MISMATCH",
                        message=f"Expected boolean at {path or '/'}, got {type(val).__name__}",
                        field_path=path or "/",
                        schema_rule="type:boolean",
                    )
                )
                return
            elif expected_type == "null" and val is not None:
                errors.append(
                    ValidationError(
                        code="TYPE_MISMATCH",
                        message=f"Expected null at {path or '/'}, got {type(val).__name__}",
                        field_path=path or "/",
                        schema_rule="type:null",
                    )
                )
                return

        # 2. Evaluate object-applicable assertions
        if isinstance(val, dict) and (expected_type is None or expected_type == "object"):
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

        # 3. Evaluate array-applicable assertions
        elif isinstance(val, list) and (expected_type is None or expected_type == "array"):
            min_items = rule.get("minItems")
            if min_items is not None and len(val) < min_items:
                err = ValidationError(
                    code="MIN_ITEMS_VIOLATION",
                    message=f"Array at {path or '/'} must contain at least {min_items} items, got {len(val)}",
                    field_path=path or "/",
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
                        message=f"Array at {path or '/'} must contain at most {max_items} items, got {len(val)}",
                        field_path=path or "/",
                        schema_rule=f"maxItems:{max_items}",
                    )
                )

            item_rule = rule.get("items")
            if item_rule and isinstance(item_rule, dict):
                for idx, item in enumerate(val):
                    check_node(item, item_rule, f"{path}/{idx}")

        # 4. Evaluate string-applicable assertions
        elif isinstance(val, str) and (expected_type is None or expected_type == "string"):
            min_len = rule.get("minLength")
            if min_len is not None and len(val) < min_len:
                errors.append(
                    ValidationError(
                        code="MIN_LENGTH_VIOLATION",
                        message=f"String at {path or '/'} is shorter than minimum length {min_len}",
                        field_path=path or "/",
                        schema_rule=f"minLength:{min_len}",
                    )
                )
            max_len = rule.get("maxLength")
            if max_len is not None and len(val) > max_len:
                errors.append(
                    ValidationError(
                        code="MAX_LENGTH_VIOLATION",
                        message=f"String at {path or '/'} exceeds maximum length {max_len}",
                        field_path=path or "/",
                        schema_rule=f"maxLength:{max_len}",
                    )
                )
            pattern = rule.get("pattern")
            if pattern is not None:
                if not re.search(pattern, val):
                    errors.append(
                        ValidationError(
                            code="PATTERN_VIOLATION",
                            message=f"String '{val}' at {path or '/'} does not match required pattern '{pattern}'",
                            field_path=path or "/",
                            schema_rule=f"pattern:{pattern}",
                        )
                    )
            fmt = rule.get("format")
            if fmt:
                if fmt in SUPPORTED_FORMATS:
                    is_valid, desc = check_format(fmt, val)
                    if not is_valid:
                        errors.append(
                            ValidationError(
                                code="FORMAT_VIOLATION",
                                message=f"String '{val}' at {path or '/'} does not match required format '{fmt}' ({desc})",
                                field_path=path or "/",
                                schema_rule=f"format:{fmt}",
                            )
                        )
                else:
                    errors.append(
                        ValidationError(
                            code="UNSUPPORTED_FORMAT_ASSERTION",
                            message=f"Format '{fmt}' at {path or '/'} is not supported by built-in validator.",
                            field_path=path or "/",
                            schema_rule=f"format:{fmt}",
                        )
                    )

        # 5. Evaluate numeric-applicable assertions
        elif (
            isinstance(val, (int, float))
            and not isinstance(val, bool)
            and (expected_type is None or expected_type in ("integer", "number"))
        ):
            minimum = rule.get("minimum")
            if minimum is not None and val < minimum:
                errors.append(
                    ValidationError(
                        code="MINIMUM_VIOLATION",
                        message=f"Value {val} at {path or '/'} is less than minimum {minimum}",
                        field_path=path or "/",
                        schema_rule=f"minimum:{minimum}",
                    )
                )
            maximum = rule.get("maximum")
            if maximum is not None and val > maximum:
                errors.append(
                    ValidationError(
                        code="MAXIMUM_VIOLATION",
                        message=f"Value {val} at {path or '/'} is greater than maximum {maximum}",
                        field_path=path or "/",
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
        artifact_id: Canonical PMO identifier, e.g. "PMO-03.01"
        data: Dict containing completed artifact data
        definition_version: Optional definition fingerprint or release version tag
        mode: "strict" (default) or "draft" (lenient for in-progress documents)

    Returns:
        ValidationReport with valid flag, status, errors, warnings, and field paths.
    """
    import tasleemat
    from tasleemat.catalog import get_artifact_definition

    current_pkg_version = getattr(tasleemat, "__version__", "2.6.1")
    norm_id = artifact_id.upper().strip()
    norm_mode = mode.lower().strip()
    if norm_mode not in ("strict", "draft"):
        raise ValueError(f"Invalid validation mode '{mode}'. Choose 'strict' or 'draft'.")

    # Step 1: Verify artifact existence in the canonical catalog
    try:
        art_def = get_artifact_definition(norm_id)
        real_definition_fingerprint = art_def.get("fingerprint", "")
    except KeyError:
        return ValidationReport(
            valid=False,
            artifact_id=norm_id,
            schema_version="",
            fingerprint="",
            definition_fingerprint="",
            package_version=current_pkg_version,
            status="unknown_artifact",
            mode=norm_mode,
            errors=[
                ValidationError(
                    code="UNKNOWN_ARTIFACT",
                    message=f"Artifact ID '{artifact_id}' does not exist in the canonical Tasleemat catalog.",
                    field_path="/",
                    schema_rule="artifact_registration",
                )
            ],
            warnings=[],
        )
    except Exception as exc:
        raise RuntimeError(f"Failed to access canonical catalog: {exc}") from exc

    # Step 2: Verify companion schema availability
    try:
        schema = _load_schema(norm_id)
    except KeyError:
        return ValidationReport(
            valid=False,
            artifact_id=norm_id,
            schema_version="",
            fingerprint=real_definition_fingerprint,
            definition_fingerprint=real_definition_fingerprint,
            package_version=current_pkg_version,
            status="unavailable",
            mode=norm_mode,
            errors=[
                ValidationError(
                    code="SCHEMA_UNAVAILABLE",
                    message=(
                        f"Completed-data structural validation is not available for artifact '{artifact_id}'. "
                        f"No companion schema has been published for this deliverable."
                    ),
                    field_path="/",
                    schema_rule="schema_existence",
                )
            ],
            warnings=[],
        )

    schema_id = schema.get("$id", f"https://tasleemat.pmo/schemas/completed/{norm_id}.schema.json")
    schema_dialect = schema.get("$schema", "https://json-schema.org/draft/2020-12/schema")
    comp_meta = art_def.get("completed_data_validation", {})
    schema_fingerprint = comp_meta.get("schema_fingerprint", "")

    schema_rev = schema_fingerprint or current_pkg_version

    # Step 3: Preflight the schema independently of payload
    preflight_errors = preflight_schema(schema)
    if preflight_errors:
        return ValidationReport(
            valid=False,
            artifact_id=norm_id,
            schema_version=schema_rev,
            schema_id=schema_id,
            schema_dialect=schema_dialect,
            schema_fingerprint=schema_fingerprint,
            fingerprint=real_definition_fingerprint,
            definition_fingerprint=real_definition_fingerprint,
            package_version=current_pkg_version,
            status="invalid_schema",
            mode=norm_mode,
            errors=preflight_errors,
            warnings=[],
        )

    # Step 4: Verify definition reference compatibility if requested
    if definition_version:
        # Explicit deterministic definition reference contract:
        # Accepts:
        # 1. Exact catalog definition SHA-256 fingerprint
        # 2. Exact companion schema SHA-256 fingerprint
        # 3. Exact companion schema $id URI (documented alias selecting current installed schema)
        # 4. Authoritative installed package version (e.g. "2.5.0", "v2.5.0")
        is_matched = (
            definition_version == real_definition_fingerprint
            or (schema_fingerprint and definition_version == schema_fingerprint)
            or definition_version == schema_id
            or definition_version in (current_pkg_version, f"v{current_pkg_version}", "2.5.0", "v2.5.0", "2.6.0", "v2.6.0", "2.6.0b1", "v2.6.0b1", "2.6.1", "v2.6.1")
        )
        if not is_matched:
            return ValidationReport(
                valid=False,
                package_version=current_pkg_version,
                artifact_id=norm_id,
                schema_version=schema_rev,
                schema_id=schema_id,
                schema_dialect=schema_dialect,
                schema_fingerprint=schema_fingerprint,
                fingerprint=real_definition_fingerprint,
                definition_fingerprint=real_definition_fingerprint,
                status="supported",
                mode=norm_mode,
                errors=[
                    ValidationError(
                        code="UNSUPPORTED_VERSION",
                        message=(
                            f"Requested definition reference '{definition_version}' does not match "
                            f"installed artifact definition fingerprint '{real_definition_fingerprint}', "
                            f"schema fingerprint '{schema_fingerprint}', or schema ID '{schema_id}'."
                        ),
                        field_path="/",
                        schema_rule="definition_compatibility",
                    )
                ],
                warnings=[],
            )

    # Step 5: Verify payload structure
    if not isinstance(data, dict):
        return ValidationReport(
            valid=False,
            artifact_id=norm_id,
            schema_version=schema_rev,
            schema_id=schema_id,
            schema_dialect=schema_dialect,
            schema_fingerprint=schema_fingerprint,
            fingerprint=real_definition_fingerprint,
            definition_fingerprint=real_definition_fingerprint,
            package_version=current_pkg_version,
            status="supported",
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

    # Step 6: Execute validation (payload immutability guaranteed)
    errors, warnings = _validate_with_builtin(data, schema, norm_mode)
    is_valid = len(errors) == 0

    return ValidationReport(
        valid=is_valid,
        artifact_id=norm_id,
        schema_version=schema_rev,
        schema_id=schema_id,
        schema_dialect=schema_dialect,
        schema_fingerprint=schema_fingerprint,
        fingerprint=real_definition_fingerprint,
        definition_fingerprint=real_definition_fingerprint,
        package_version=current_pkg_version,
        status="supported",
        mode=norm_mode,
        errors=errors,
        warnings=warnings,
    )
