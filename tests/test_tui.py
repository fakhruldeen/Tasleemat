"""
tests/test_tui.py
Automated test suite for the Tasleemat Bilingual TUI, BiDi engine, and Agent Integrations.
"""

import json
import pathlib
import tempfile
import unittest
try:
    import textual
    import arabic_reshaper
    import bidi
    HAS_TUI_DEPS = True
except ImportError:
    HAS_TUI_DEPS = False

from tasleemat.tui.bidi import is_arabic, shape_text, align_bilingual
from tasleemat.tui.i18n import t
from tasleemat.tui.integrations.manager import (
    SUPPORTED_AGENTS,
    apply_selected_integrations,
    detect_existing_integrations,
)
if HAS_TUI_DEPS:
    from tasleemat.tui.app import TasleematApp
else:
    TasleematApp = None

class TestTUI(unittest.TestCase):

    def test_bidi_shaping(self):
        """Test Arabic character detection and BiDi shaping."""
        self.assertFalse(is_arabic("Project Charter"))
        self.assertTrue(is_arabic("ميثاق المشروع"))
        self.assertTrue(is_arabic("PMO-03.01 ميثاق"))

        # English text should return unchanged
        self.assertEqual(shape_text("Hello World"), "Hello World")

        # Arabic text should be shaped
        arabic_sample = "تسليمات"
        shaped = shape_text(arabic_sample)
        self.assertIsInstance(shaped, str)
        self.assertNotEqual(len(shaped), 0)

        # Bilingual alignment
        aligned = align_bilingual("Project Charter", "ميثاق المشروع", width=20)
        self.assertIn("Project Charter", aligned)
        self.assertIn("|", aligned)

    def test_i18n_translations(self):
        """Test bilingual dictionary lookups."""
        en_title = t("app_title", lang="en")
        ar_title = t("app_title", lang="ar", shape_ar=False)

        self.assertIn("Tasleemat", en_title)
        self.assertIn("تسليمات", ar_title)

        # Tab strings
        self.assertEqual(t("tab_scaffolder", lang="en"), "🚀 Scaffolder")
        self.assertIn("مُنشئ", t("tab_scaffolder", lang="ar", shape_ar=False))

        # Fallback for unknown key
        self.assertEqual(t("non_existent_key_xyz", lang="en"), "non_existent_key_xyz")

    def test_agent_integrations_in_workspace(self):
        """Test 1-click configuration for Cursor, AGY, Claude, and VS Code."""
        with tempfile.TemporaryDirectory() as tmpdir:
            ws_path = pathlib.Path(tmpdir) / "test_pmo_workspace"
            ws_path.mkdir(parents=True, exist_ok=True)

            # Initially no integrations
            initial_status = detect_existing_integrations(ws_path)
            self.assertFalse(initial_status["cursor"])
            self.assertFalse(initial_status["agy"])
            self.assertFalse(initial_status["vscode"])
            self.assertFalse(initial_status["opencode"])
            self.assertFalse(initial_status["cline"])
            self.assertFalse(initial_status["windsurf"])
            self.assertFalse(initial_status["openai_cli"])

            # Apply all supported agents
            agents = ["cursor", "agy", "claude", "vscode", "opencode", "cline", "windsurf", "openai_cli"]
            report = apply_selected_integrations(ws_path, agents)

            self.assertEqual(len(report), 8)

            # 1. Cursor verification
            cursor_mcp = ws_path / ".cursor" / "mcp.json"
            self.assertTrue(cursor_mcp.exists())
            with open(cursor_mcp, "r", encoding="utf-8") as f:
                cursor_data = json.load(f)
            self.assertIn("tasleemat", cursor_data["mcpServers"])
            self.assertTrue((ws_path / ".cursor" / "rules" / "tasleemat-pmo.mdc").exists())

            # 2. AGY verification
            self.assertTrue((ws_path / ".antigravityrules").exists())
            self.assertTrue((ws_path / "skills" / "pmo-governance" / "SKILL.md").exists())

            # 3. Claude verification
            self.assertTrue((ws_path / "CLAUDE.md").exists())

            # 4. VS Code verification
            vscode_mcp = ws_path / ".vscode" / "mcp.json"
            self.assertTrue(vscode_mcp.exists())
            with open(vscode_mcp, "r", encoding="utf-8") as f:
                vscode_data = json.load(f)
            self.assertIn("tasleemat", vscode_data["servers"])
            self.assertTrue((ws_path / "AGENT_GUIDE.md").exists())

            # 5. OpenCode verification
            opencode_mcp = ws_path / ".opencode" / "mcp.json"
            self.assertTrue(opencode_mcp.exists())
            self.assertTrue((ws_path / "OPENCODE.md").exists())

            # 6. Cline verification
            cline_mcp = ws_path / ".cline" / "mcp.json"
            self.assertTrue(cline_mcp.exists())
            self.assertTrue((ws_path / ".clinerules").exists())

            # 7. Windsurf verification
            windsurf_mcp = ws_path / ".windsurf" / "mcp.json"
            self.assertTrue(windsurf_mcp.exists())
            self.assertTrue((ws_path / ".windsurfrules").exists())

            # 8. OpenAI CLI verification
            openai_cfg = ws_path / ".openai" / "config.json"
            self.assertTrue(openai_cfg.exists())
            self.assertTrue((ws_path / ".openai" / "tools.json").exists())
            self.assertTrue((ws_path / ".openai" / "agent_runner.py").exists())

            # Verify detect_existing_integrations now reports all active
            updated_status = detect_existing_integrations(ws_path)
            self.assertTrue(updated_status["cursor"])
            self.assertTrue(updated_status["agy"])
            self.assertTrue(updated_status["claude"])
            self.assertTrue(updated_status["vscode"])
            self.assertTrue(updated_status["opencode"])
            self.assertTrue(updated_status["cline"])
            self.assertTrue(updated_status["windsurf"])
            self.assertTrue(updated_status["openai_cli"])

    @unittest.skipUnless(HAS_TUI_DEPS, "Textual optional dependency not installed")
    def test_tui_app_headless_execution(self):
        """Test Textual app instantiation, mounting, and language toggle in headless mode."""
        import asyncio
        async def _run():
            app = TasleematApp(lang="en")
            async with app.run_test() as pilot:
                # App should be running
                self.assertEqual(app.lang, "en")
                self.assertIsNotNone(app.query_one("#main_nav_tabs"))
                self.assertIsNotNone(app.query_one("#main_content_switcher"))

                # Toggle language to Arabic
                app.action_toggle_lang()
                self.assertEqual(app.lang, "ar")

                # Toggle back to English
                app.action_toggle_lang()
                self.assertEqual(app.lang, "en")

        asyncio.run(_run())

    @unittest.skipUnless(HAS_TUI_DEPS, "Textual optional dependency not installed")
    def test_wizard_scaffolding_execution(self):
        """Test wizard screen scaffolding execution with agent integrations."""
        from tasleemat.tui.screens.wizard import ScaffolderWizardScreen
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = pathlib.Path(tmpdir) / "Test_Wizard_Project"
            screen = ScaffolderWizardScreen(lang="en")

            # Emulate inputs
            class MockInput:
                def __init__(self, val):
                    self.value = val

            class MockSelect:
                def __init__(self, val):
                    self.value = val

            class MockCheckbox:
                def __init__(self, val):
                    self.value = val

            class MockStatic:
                def __init__(self):
                    self.text = ""
                def update(self, val):
                    self.text = str(val)

            screen_widgets = {
                "#inp_prj_name": MockInput("AI Health Tech"),
                "#inp_prj_code": MockInput("PRJ-AI-01"),
                "#inp_pm_name": MockInput("Dr. Nora"),
                "#inp_sponsor_name": MockInput("Eng. Tariq"),
                "#sel_tier": MockSelect("3"),
                "#sel_pack": MockSelect("ai"),
                "#sel_lang": MockSelect("both"),
                "#inp_out_dir": MockInput(str(out_path)),
                "#wiz_chk_cursor": MockCheckbox(True),
                "#wiz_chk_agy": MockCheckbox(True),
                "#wiz_chk_claude": MockCheckbox(False),
                "#wiz_chk_vscode": MockCheckbox(True),
                "#wiz_chk_opencode": MockCheckbox(True),
                "#wiz_chk_cline": MockCheckbox(True),
                "#wiz_chk_windsurf": MockCheckbox(True),
                "#wiz_chk_openai_cli": MockCheckbox(True),
                "#wizard_status": MockStatic()
            }

            screen.query_one = lambda selector, *args, **kwargs: screen_widgets.get(selector)
            screen.execute_scaffold()

            # Verify scaffolded workspace
            self.assertTrue(out_path.exists())
            self.assertTrue((out_path / "PROJECT_README.md").exists())
            self.assertTrue((out_path / ".cursor" / "mcp.json").exists())
            self.assertTrue((out_path / ".antigravityrules").exists())
            self.assertTrue((out_path / ".vscode" / "mcp.json").exists())
            self.assertTrue((out_path / ".opencode" / "mcp.json").exists())
            self.assertTrue((out_path / ".clinerules").exists())
            self.assertTrue((out_path / ".windsurfrules").exists())
            self.assertTrue((out_path / ".openai" / "agent_runner.py").exists())

            status_text = screen_widgets["#wizard_status"].text
            self.assertIn("Successfully scaffolded", status_text)

    def test_cli_tui_help(self):
        """Test that CLI help lists the tui command and its options."""
        import subprocess
        import sys
        ROOT = pathlib.Path(__file__).parent.parent.resolve()
        CLI_PATH = ROOT / "tools" / "tasleemat_cli.py"

        res = subprocess.run(
            [sys.executable, str(CLI_PATH), "help", "tui"],
            capture_output=True, text=True, cwd=str(ROOT)
        )
        self.assertEqual(res.returncode, 0)
        self.assertIn("tui", res.stdout)
        self.assertIn("--lang", res.stdout)

if __name__ == "__main__":
    unittest.main()
