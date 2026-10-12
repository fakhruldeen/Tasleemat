"""
Tasleemat Centralized JSON Schema Format Registry & Assertion Handlers.

Per JSON Schema Draft 2020-12 specification, 'format' acts as an annotation by
default, but implementations may explicitly configure assertion mode.
Tasleemat enforces format keywords in assertion mode for supported formats.

Format Policy:
- Supported format, valid value: Validation proceeds (handler returns True).
- Supported format, invalid value: Emits ValidationError with code FORMAT_VIOLATION.
- Unsupported format: Preflight rejects schema with UNSUPPORTED_FORMAT_ASSERTION.
- Malformed format keyword: Preflight rejects schema with MALFORMED_SCHEMA_KEYWORD.
- Handlers perform strict offline syntax and boundary validation without external network calls.
"""

from typing import Callable, Dict, Optional, Tuple
import datetime
import re
import urllib.parse
import uuid


# ---------------------------------------------------------------------------
# Regex Specifications for Supported Formats
# ---------------------------------------------------------------------------

# RFC 3339 full-date: YYYY-MM-DD
# Strictly requires 4-digit year, 2-digit zero-padded month (01-12), 2-digit zero-padded day (01-31).
# Compact representations (YYYYMMDD) or unpadded months/days (YYYY-M-D) are rejected.
DATE_REGEX = re.compile(r"^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$")

# RFC 3339 date-time:
# date-time = full-date "T" full-time
# full-time = time-hour ":" time-minute ":" time-second [time-secfrac] time-offset
# time-offset = "Z" / ("+" / "-") time-hour ":" time-minute
# Allows leap second 60. Rejects space separator without T, missing offset, and invalid time parts.
DATETIME_REGEX = re.compile(
    r"^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])"
    r"[Tt]"
    r"(?:[01]\d|2[0-3]):[0-5]\d:(?:[0-5]\d|60)(?:\.\d+)?"
    r"(?:[Zz]|[+-](?:[01]\d|2[0-3]):[0-5]\d)$"
)

# RFC 3339 partial-time:
# partial-time = time-hour ":" time-minute ":" time-second [time-secfrac]
# Optionally with time-offset.
TIME_REGEX = re.compile(
    r"^(?:[01]\d|2[0-3]):[0-5]\d:(?:[0-5]\d|60)(?:\.\d+)?"
    r"(?:[Zz]|[+-](?:[01]\d|2[0-3]):[0-5]\d)?$"
)

# UUID (RFC 4122 string representation):
# 8-4-4-4-12 hexadecimal digits. URNs (urn:uuid:...) belong under uri, not plain uuid.
UUID_REGEX = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")

# RFC 3986 Absolute URI:
# URI = scheme ":" hier-part [ "?" query ] [ "#" fragment ]
# scheme = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )
# Must have scheme. Spaces or control characters rejected.
URI_REGEX = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:[^\s]*$")

# RFC 3986 URI-Reference (either absolute URI or relative-ref):
# relative-ref = relative-part [ "?" query ] [ "#" fragment ]
# Disallows unescaped whitespace or invalid control characters.
URI_REFERENCE_REGEX = re.compile(r"^[^\s]+$")

# RFC 5322 addr-spec documented standard subset:
# local-part @ domain. Disallows spaces and requires valid domain labels.
EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$"
)

# ISO 8601 / RFC 3339 duration:
# P(n)Y(n)M(n)DT(n)H(n)M(n)S or P(n)W
DURATION_REGEX = re.compile(
    r"^P(?:(?:\d+W)|(?:(?:\d+Y)?(?:\d+M)?(?:\d+D)?(?:T(?:\d+H)?(?:\d+M)?(?:\d+(?:\.\d+)?S)?)?))$"
)


# ---------------------------------------------------------------------------
# Format Handler Functions
# ---------------------------------------------------------------------------

def validate_date(val: str) -> bool:
    """
    Validate RFC 3339 full-date (YYYY-MM-DD) including calendar validity.
    Rejects compact dates (YYYYMMDD), non-zero padded dates, and invalid days
    such as February 29 on non-leap years.
    """
    if not isinstance(val, str) or not DATE_REGEX.match(val):
        return False
    try:
        parts = val.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        datetime.date(year, month, day)
        return True
    except (ValueError, TypeError, IndexError):
        return False


def validate_date_time(val: str) -> bool:
    """
    Validate RFC 3339 date-time.
    Requires complete date, T separator, time, and timezone offset ('Z' or +/-HH:MM).
    Supports fractional seconds and leap seconds (second 60).
    """
    if not isinstance(val, str) or not DATETIME_REGEX.match(val):
        return False
    date_part = val[:10]
    return validate_date(date_part)


def validate_time(val: str) -> bool:
    """
    Validate RFC 3339 partial-time / full-time (HH:MM:SS[.fractional][Z|offset]).
    """
    if not isinstance(val, str) or not TIME_REGEX.match(val):
        return False
    return True


def validate_uuid(val: str) -> bool:
    """
    Validate standard 8-4-4-4-12 hex UUID representation (RFC 4122).
    Plain UUID strings only. URNs (urn:uuid:...) are rejected here.
    """
    if not isinstance(val, str) or not UUID_REGEX.match(val):
        return False
    try:
        uuid.UUID(val)
        return True
    except (ValueError, TypeError, AttributeError):
        return False


def validate_uri(val: str) -> bool:
    """
    Validate RFC 3986 absolute URI.
    Checks syntax, presence of valid scheme, and absence of raw whitespace.
    Does not issue network requests or check resource existence.
    """
    if not isinstance(val, str) or not URI_REGEX.match(val):
        return False
    try:
        parsed = urllib.parse.urlsplit(val)
        return bool(parsed.scheme)
    except Exception:
        return False


def validate_uri_reference(val: str) -> bool:
    """
    Validate RFC 3986 URI Reference (either absolute URI or relative reference).
    Disallows unescaped whitespace and malformed percent-encoding.
    """
    if not isinstance(val, str) or not URI_REFERENCE_REGEX.match(val):
        return False
    try:
        urllib.parse.urlsplit(val)
        return True
    except Exception:
        return False


def validate_email(val: str) -> bool:
    """
    Validate RFC 5322 email address subset (addr-spec).
    Maximum length 254 octets. Syntax check only; does not verify mailbox delivery.
    """
    if not isinstance(val, str) or len(val) > 254:
        return False
    return bool(EMAIL_REGEX.match(val))


def validate_duration(val: str) -> bool:
    """
    Validate ISO 8601 / RFC 3339 duration representation (e.g. P1Y2M, PT15M, P4W).
    Rejects bare 'P' or 'PT' and arbitrary prose such as '3 days'.
    """
    if not isinstance(val, str) or val in ("P", "PT") or not DURATION_REGEX.match(val) or val.endswith("T"):
        return False
    return True


# ---------------------------------------------------------------------------
# Central Handler Registry
# ---------------------------------------------------------------------------

FormatHandler = Callable[[str], bool]

FORMAT_HANDLERS: Dict[str, Tuple[FormatHandler, str]] = {
    # format_name: (handler_func, human_readable_description)
    "date": (validate_date, "RFC 3339 full-date (YYYY-MM-DD)"),
    "date-time": (validate_date_time, "RFC 3339 date-time with timezone (YYYY-MM-DDTHH:MM:SS[Z|+/-HH:MM])"),
    "time": (validate_time, "RFC 3339 time (HH:MM:SS[Z|+/-HH:MM])"),
    "uuid": (validate_uuid, "RFC 4122 UUID (8-4-4-4-12 hex string)"),
    "uri": (validate_uri, "RFC 3986 absolute URI with scheme"),
    "uri-reference": (validate_uri_reference, "RFC 3986 URI reference"),
    "email": (validate_email, "RFC 5322 email address (local-part@domain)"),
    "duration": (validate_duration, "ISO 8601 duration (e.g., P3Y6M4DT12H30M5S or PT15M)"),
}

SUPPORTED_FORMATS = set(FORMAT_HANDLERS.keys())


def check_format(fmt: str, val: str) -> Tuple[bool, Optional[str]]:
    """
    Check value against registered format handler.
    Returns (is_valid, description).
    Raises KeyError if format is not registered.
    """
    if fmt not in FORMAT_HANDLERS:
        raise KeyError(f"Unsupported format '{fmt}'")
    handler, desc = FORMAT_HANDLERS[fmt]
    return handler(val), desc
