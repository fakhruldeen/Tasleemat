"""
tasleemat.tui.bidi
Arabic text shaping and bidirectional (BiDi) algorithm handling for terminal display.
Ensures Arabic characters are properly connected and RTL-ordered across terminal emulators.
"""

import re
import os

_HAS_BIDI = False
try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    _HAS_BIDI = True
except ImportError:
    _HAS_BIDI = False

# Arabic unicode range regex
ARABIC_REGEX = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]')

def is_arabic(text: str) -> bool:
    """Check if the text contains any Arabic characters."""
    if not text:
        return False
    return bool(ARABIC_REGEX.search(text))

def shape_text(text: str, force_bidi: bool = False) -> str:
    """
    Reshape Arabic characters to their cursive forms and apply BiDi reordering.
    If the terminal natively handles BiDi and force_bidi is False,
    shaping without reversing may be preferred, but for most standard terminal
    cells, get_display(reshaped) produces the correct visual output.
    """
    if not text or not _HAS_BIDI:
        return text

    if not is_arabic(text):
        return text

    try:
        # Configuration to handle ligature and numbers gracefully
        reshaper = arabic_reshaper.ArabicReshaper(
            configuration={
                'delete_harakat': False,
                'support_ligatures': True,
                'format': 'Default'
            }
        )
        reshaped = reshaper.reshape(text)
        visual = get_display(reshaped)
        return visual
    except Exception:
        return text

def align_bilingual(en_text: str, ar_text: str, width: int = 40) -> str:
    """Format a bilingual label: English on the left, reshaped Arabic on the right."""
    shaped_ar = shape_text(ar_text)
    return f"{en_text:<{width}} | {shaped_ar}"
