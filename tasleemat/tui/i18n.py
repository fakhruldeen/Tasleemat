"""
tasleemat.tui.i18n
Bilingual translation and localization engine for the Tasleemat TUI.
"""

import json
import pathlib
from tasleemat.tui.bidi import shape_text

LOCALES_DIR = pathlib.Path(__file__).parent / "locales"

_STRINGS = {
    "en": {},
    "ar": {}
}

def load_translations():
    global _STRINGS
    en_file = LOCALES_DIR / "en.json"
    ar_file = LOCALES_DIR / "ar.json"
    if en_file.exists():
        with open(en_file, "r", encoding="utf-8") as f:
            _STRINGS["en"] = json.load(f)
    if ar_file.exists():
        with open(ar_file, "r", encoding="utf-8") as f:
            _STRINGS["ar"] = json.load(f)

load_translations()

def t(key: str, lang: str = "en", shape_ar: bool = True) -> str:
    """
    Retrieve localized string by key and language ('en' or 'ar').
    If lang is 'ar' and shape_ar is True, applies Arabic BiDi shaping.
    """
    dict_to_use = _STRINGS.get(lang, _STRINGS.get("en", {}))
    val = dict_to_use.get(key)
    if not val:
        val = _STRINGS.get("en", {}).get(key, key)
    
    if lang == "ar" and shape_ar:
        return shape_text(val)
    return val
