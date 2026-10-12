"""
Tasleemat (تسليمات) — Enterprise Bilingual PMO Framework & Automation Library
"""

__version__ = "2.4.1"

from tasleemat.catalog import (
    ArtifactAssets,
    ArtifactSummary,
    get_artifact_asset,
    get_artifact_assets,
    get_artifact_definition,
    get_lexicon,
    get_tailoring_profile,
    list_artifacts,
)
from tasleemat.rendering import render_artifact
from tasleemat.validation import (
    ValidationError,
    ValidationReport,
    validate_artifact_data,
)

__all__ = [
    "__version__",
    "list_artifacts",
    "get_artifact_definition",
    "get_artifact_assets",
    "get_artifact_asset",
    "get_tailoring_profile",
    "get_lexicon",
    "validate_artifact_data",
    "render_artifact",
    "ArtifactSummary",
    "ArtifactAssets",
    "ValidationReport",
    "ValidationError",
]
