"""
Tasleemat Canonical Artifact Catalog Interface
Provides structured, machine-readable discovery and asset retrieval.
"""

from __future__ import annotations

import copy
import json
import pathlib
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

# Resolve root directory containing forms/, docs/, etc.
PACKAGE_DIR = pathlib.Path(__file__).resolve().parent
CATALOG_PATH = PACKAGE_DIR / "data" / "catalog.json"

# Fallback root resolution if running inside installed site-packages or source tree
if (PACKAGE_DIR.parent / "forms").exists():
    REPO_ROOT = PACKAGE_DIR.parent
elif (PACKAGE_DIR / "forms").exists():
    REPO_ROOT = PACKAGE_DIR
else:
    REPO_ROOT = PACKAGE_DIR.parent


@dataclass(frozen=True)
class ArtifactSummary:
    artifact_id: str
    prefix: str
    name_en: str
    name_ar: str
    phase_code: str
    phase_name_en: str
    phase_name_ar: str
    tiers: List[str]
    fingerprint: str
    completed_data_validation: Optional[Dict[str, Any]] = None


@dataclass(frozen=True)
class ArtifactAssets:
    artifact_id: str
    lang: str
    template_path: str
    guide_path: str
    prompt_path: str
    schema_path: str
    dictionary_path: str
    example_path: Optional[str]

    def _resolve(self, rel_path: Optional[str]) -> Optional[pathlib.Path]:
        if not rel_path:
            return None
        # Defend against path traversal: relative paths must stay inside REPO_ROOT or PACKAGE_DIR
        for base in (REPO_ROOT, PACKAGE_DIR):
            candidate = (base / rel_path).resolve()
            try:
                candidate.relative_to(base.resolve())
            except ValueError:
                # Path escaped base directory
                continue
            if candidate.exists():
                return candidate

        fallback = (REPO_ROOT / rel_path).resolve()
        try:
            fallback.relative_to(REPO_ROOT.resolve())
        except ValueError:
            raise ValueError(f"Path traversal detected in asset path: {rel_path}")
        return fallback

    def get_template_content(self) -> str:
        p = self._resolve(self.template_path)
        if not p or not p.exists():
            raise FileNotFoundError(f"Template asset missing for {self.artifact_id}: {self.template_path}")
        return p.read_text(encoding="utf-8")

    def get_guide_content(self) -> str:
        p = self._resolve(self.guide_path)
        if not p or not p.exists():
            raise FileNotFoundError(f"Guide asset missing for {self.artifact_id}: {self.guide_path}")
        return p.read_text(encoding="utf-8")

    def get_prompt_content(self) -> str:
        p = self._resolve(self.prompt_path)
        if not p or not p.exists():
            raise FileNotFoundError(f"Prompt asset missing for {self.artifact_id}: {self.prompt_path}")
        return p.read_text(encoding="utf-8")

    def get_schema_data(self) -> Dict[str, Any]:
        p = self._resolve(self.schema_path)
        if not p or not p.exists():
            raise FileNotFoundError(f"Schema asset missing for {self.artifact_id}: {self.schema_path}")
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_dictionary_data(self) -> List[Dict[str, str]]:
        import csv
        p = self._resolve(self.dictionary_path)
        if not p or not p.exists():
            raise FileNotFoundError(f"Dictionary asset missing for {self.artifact_id}: {self.dictionary_path}")
        with open(p, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)

    def get_example_content(self) -> Optional[str]:
        p = self._resolve(self.example_path)
        if not p or not p.exists():
            return None
        return p.read_text(encoding="utf-8")


_CATALOG_CACHE: Optional[Dict[str, Any]] = None


def _get_catalog() -> Dict[str, Any]:
    global _CATALOG_CACHE
    if _CATALOG_CACHE is None:
        if not CATALOG_PATH.exists():
            raise FileNotFoundError(f"Catalog database not found at: {CATALOG_PATH}")
        with open(CATALOG_PATH, "r", encoding="utf-8") as f:
            _CATALOG_CACHE = json.load(f)
    return _CATALOG_CACHE


def list_artifacts(
    phase: Optional[str] = None,
    tier: Optional[str] = None,
    pack: Optional[str] = None,
) -> List[ArtifactSummary]:
    """List all artifacts matching the specified phase, tier, or pack filters."""
    catalog = _get_catalog()
    results = []

    for item in catalog.get("artifacts", []):
        if phase and item.get("phase_code") != phase and item.get("phase_name_en") != phase:
            continue
        tailoring = item.get("tailoring", {})
        packs_by_tier = tailoring.get("packs_by_tier", {})
        item_tiers = tailoring.get("tiers", [])

        if tier and tier not in item_tiers:
            continue

        if pack:
            if tier:
                # Strict intersection: pack must exist under the requested tier
                tier_packs = packs_by_tier.get(tier, [])
                if pack not in tier_packs:
                    continue
            else:
                # No specific tier requested: match if pack exists in any tier
                matched = False
                for t_packs in packs_by_tier.values():
                    if pack in t_packs:
                        matched = True
                        break
                if not matched:
                    continue

        results.append(
            ArtifactSummary(
                artifact_id=item["artifact_id"],
                prefix=item["prefix"],
                name_en=item["name_en"],
                name_ar=item["name_ar"],
                phase_code=item["phase_code"],
                phase_name_en=item["phase_name_en"],
                phase_name_ar=item["phase_name_ar"],
                tiers=list(item_tiers),
                fingerprint=item["fingerprint"],
                completed_data_validation=copy.deepcopy(item.get("completed_data_validation")),
            )
        )
    return results


def get_artifact_definition(artifact_id: str) -> Dict[str, Any]:
    """Retrieve full catalog definition for a specific artifact ID (e.g. 'PMO-03.01')."""
    catalog = _get_catalog()
    norm_id = artifact_id.upper().strip()
    for item in catalog.get("artifacts", []):
        if item["artifact_id"] == norm_id:
            return copy.deepcopy(item)
    raise KeyError(f"Artifact ID '{artifact_id}' not found in Tasleemat catalog.")


def get_artifact_assets(artifact_id: str, lang: str = "en") -> ArtifactAssets:
    """Retrieve bilingual asset paths and loaders for an artifact."""
    norm_lang = lang.lower().strip()
    if norm_lang not in ("en", "ar"):
        raise ValueError(f"Unsupported language '{lang}'. Supported: 'en', 'ar'.")

    definition = get_artifact_definition(artifact_id)
    lang_assets = definition["assets"].get(norm_lang)
    if not lang_assets:
        raise KeyError(f"Language assets for '{lang}' not found for artifact '{artifact_id}'.")

    return ArtifactAssets(
        artifact_id=definition["artifact_id"],
        lang=norm_lang,
        template_path=lang_assets["template"],
        guide_path=lang_assets["guide"],
        prompt_path=lang_assets["prompt"],
        schema_path=lang_assets["schema"],
        dictionary_path=lang_assets["dictionary"],
        example_path=lang_assets.get("example"),
    )


VALID_TIERS = {"1", "2", "3"}
VALID_PACKS = {"general", "predictive", "agile", "hybrid", "ai"}


def get_tailoring_profile(tier: str, pack: str = "general") -> List[str]:
    """Retrieve the list of required artifact IDs for a given governance tier and methodology pack."""
    norm_tier = str(tier).strip()
    norm_pack = pack.lower().strip()

    if norm_tier not in VALID_TIERS:
        raise ValueError(f"Invalid tailoring tier '{tier}'. Supported tiers: {sorted(list(VALID_TIERS))}")
    if norm_pack not in VALID_PACKS:
        raise ValueError(f"Invalid tailoring pack '{pack}'. Supported packs: {sorted(list(VALID_PACKS))}")

    catalog = _get_catalog()
    matched_ids = []

    for item in catalog.get("artifacts", []):
        tailoring = item.get("tailoring", {})
        packs_by_tier = tailoring.get("packs_by_tier", {})
        if norm_tier in packs_by_tier:
            if norm_pack in packs_by_tier[norm_tier]:
                matched_ids.append(item["artifact_id"])

    return matched_ids


def get_artifact_asset(artifact_id: str, role: str, lang: str = "en") -> Any:
    """
    Retrieve specific asset content for an artifact by role and language.

    Parameters:
        artifact_id: PMO code (e.g. "PMO-03.01")
        role: "template", "guide", "prompt", "schema", "dictionary", or "example"
        lang: "en" or "ar"

    Returns:
        Content string, dict, or list depending on the asset role.
    """
    norm_role = role.lower().strip()
    valid_roles = ("template", "guide", "prompt", "schema", "dictionary", "example")
    if norm_role not in valid_roles:
        raise ValueError(
            f"Invalid asset role '{role}'. Supported roles: {', '.join(valid_roles)}."
        )

    assets = get_artifact_assets(artifact_id, lang=lang)
    if norm_role == "template":
        return assets.get_template_content()
    elif norm_role == "guide":
        return assets.get_guide_content()
    elif norm_role == "prompt":
        return assets.get_prompt_content()
    elif norm_role == "schema":
        return assets.get_schema_data()
    elif norm_role == "dictionary":
        return assets.get_dictionary_data()
    elif norm_role == "example":
        return assets.get_example_content()


_LEXICON_CACHE: Optional[Dict[str, Any]] = None


def get_lexicon(category: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Retrieve standardized bilingual terminology and form registry definitions.

    Parameters:
        category: Optional lifecycle phase or group filter (e.g. "03_Initiating")

    Returns:
        List of terminology dictionaries with English and Arabic names.
    """
    global _LEXICON_CACHE
    if _LEXICON_CACHE is None:
        lex_path = REPO_ROOT / "docs" / "LEXICON.json"
        if not lex_path.exists():
            lex_path = PACKAGE_DIR / "docs" / "LEXICON.json"
        if not lex_path.exists():
            return []
        with open(lex_path, "r", encoding="utf-8") as f:
            _LEXICON_CACHE = json.load(f)

    forms = _LEXICON_CACHE.get("forms", []) if _LEXICON_CACHE else []
    if category:
        norm_cat = category.strip().lower()
        return [
            copy.deepcopy(f)
            for f in forms
            if f.get("group", "") and norm_cat in f.get("group", "").lower()
        ]
    return [copy.deepcopy(f) for f in forms]

