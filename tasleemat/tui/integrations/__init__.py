"""
tasleemat.tui.integrations
AI Agent integration utilities for Cursor, Antigravity, Claude, and VS Code.
"""

from tasleemat.tui.integrations.manager import (
    SUPPORTED_AGENTS,
    apply_selected_integrations,
    detect_existing_integrations,
)

__all__ = [
    "SUPPORTED_AGENTS",
    "apply_selected_integrations",
    "detect_existing_integrations",
]
