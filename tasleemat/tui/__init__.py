"""
tasleemat.tui
Bilingual Terminal User Interface (TUI) for the Tasleemat PMO Operating System.
"""

import sys

def launch_tui(lang: str = "en"):
    """Launch the Tasleemat visual TUI, verifying dependencies first."""
    try:
        import textual
    except ImportError:
        print("\n\033[93m⚠️  The Tasleemat visual TUI requires optional dependencies.\033[0m")
        print("Please install them using:\n")
        print("    \033[92mpip install 'tasleemat[tui]'\033[0m")
        print("Or:\n")
        print("    \033[92mpip install textual arabic-reshaper python-bidi\033[0m\n")
        sys.exit(1)

    from tasleemat.tui.app import run_tui
    run_tui(lang=lang)

__all__ = ["launch_tui"]
