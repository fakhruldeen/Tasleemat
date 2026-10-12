#!/usr/bin/env python3
"""
tests/test_wheel_clean_install.py
Verifies that building the Tasleemat wheel and installing it in a clean,
isolated virtual environment outside the source tree provides full library
and CLI functionality without source-checkout assumptions.
"""

import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SDK_DIR = ROOT / "sdk" / "python"


class TestWheelCleanInstall(unittest.TestCase):

    def test_wheel_build_and_clean_environment_execution(self):
        """Build wheel, install into isolated venv, and verify library imports & CLI outside repo."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = pathlib.Path(tmpdir)
            venv_dir = tmp_path / "clean_venv"
            dist_dir = tmp_path / "dist"
            dist_dir.mkdir(parents=True, exist_ok=True)

            # 1. Create clean virtual environment
            subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
            pip_bin = venv_dir / "bin" / "pip"
            py_bin = venv_dir / "bin" / "python"
            cli_bin = venv_dir / "bin" / "tasleemat"

            # 2. Stage SDK assets inside an isolated staging temp directory (outside source tree)
            stage_dir = tmp_path / "sdk_stage"
            stage_dir.mkdir(parents=True, exist_ok=True)
            pkg_dest = stage_dir / "tasleemat"
            pkg_dest.mkdir(parents=True, exist_ok=True)

            import shutil
            shutil.copytree(str(ROOT / "tasleemat"), str(pkg_dest), dirs_exist_ok=True)
            shutil.copytree(str(ROOT / "forms"), str(pkg_dest / "forms"), dirs_exist_ok=True)
            shutil.copytree(str(ROOT / "docs"), str(pkg_dest / "docs"), dirs_exist_ok=True)
            shutil.copytree(str(ROOT / "_tokens"), str(pkg_dest / "_tokens"), dirs_exist_ok=True)
            shutil.copytree(str(ROOT / "tools"), str(pkg_dest / "tools"), dirs_exist_ok=True)
            shutil.copytree(str(ROOT / "tools" / "ai"), str(pkg_dest / "ai"), dirs_exist_ok=True)
            shutil.copy(str(ROOT / "LICENSE"), str(stage_dir / "LICENSE"))
            shutil.copy(str(SDK_DIR / "setup.py"), str(stage_dir / "setup.py"))
            shutil.copy(str(SDK_DIR / "README.md"), str(stage_dir / "README.md"))

            (pkg_dest / "tools" / "__init__.py").touch()
            (pkg_dest / "tools" / "attested_computations" / "__init__.py").touch()

            # Build wheel directly in stage_dir into dist_dir
            subprocess.run(
                [sys.executable, "-m", "pip", "wheel", ".", "-w", str(dist_dir), "--no-deps"],
                cwd=str(stage_dir),
                check=True,
            )

            # Find built wheel in dist_dir
            wheels = sorted(dist_dir.glob("*.whl"), key=os.path.getmtime)
            self.assertTrue(len(wheels) > 0, "No built wheel found in isolated dist dir")
            latest_wheel = wheels[-1]

            # 3. Install wheel in isolated venv (using --no-deps for speed in offline/sandboxed test)
            subprocess.run([str(pip_bin), "install", "--no-deps", str(latest_wheel)], check=True)

            # 4. Verify programmatic library execution from outside the source checkout
            test_script = """
import sys
import tasleemat

# Verify version and exports
assert tasleemat.__version__ == "2.5.0", f"Unexpected version {tasleemat.__version__}"
artifacts = tasleemat.list_artifacts()
assert len(artifacts) == 114, f"Expected 114 artifacts, got {len(artifacts)}"

# Verify detail retrieval
defn = tasleemat.get_artifact_definition("PMO-03.01")
assert defn["name_en"] == "PROJECT CHARTER"

# Verify asset retrieval
assets = tasleemat.get_artifact_assets("PMO-03.01", lang="en")
tmpl = assets.get_template_content()
assert "PROJECT CHARTER" in tmpl

# Verify single-call role getter
tmpl_role = tasleemat.get_artifact_asset("PMO-03.01", role="template", lang="en")
assert tmpl == tmpl_role

# Verify lexicon access
lex = tasleemat.get_lexicon()
assert len(lex) > 50

# Verify validation
valid_payload = {
    "artifact_id": "PMO-03.01",
    "metadata": {
        "project_name": "Test Project",
        "project_code": "PRJ-01",
        "date_prepared": "2026-03-15",
        "prepared_by": "Test Author",
        "sponsor": "Test Sponsor",
        "status": "approved"
    },
    "fields": {
        "project_purpose": "Valid test purpose description for clean install test.",
        "high_level_project_description": "Valid high level description for verification.",
        "key_deliverables": ["Deliverable 1"],
        "project_objectives_and_related_success_criteria": [
            {"objective": "Obj 1", "success_criteria": "Crit 1"}
        ],
        "summary_milestone_schedule": [
            {"milestone": "M1", "target_date": "2026-05-01"}
        ]
    }
}
report = tasleemat.validate_artifact_data("PMO-03.01", valid_payload)
assert report.valid is True, f"Validation failed: {report.errors}"

print("SUCCESS: Programmatic library test passed in clean venv!")
"""
            res_py = subprocess.run(
                [str(py_bin), "-c", test_script],
                cwd=str(tmp_path),
                capture_output=True,
                text=True,
            )
            self.assertEqual(res_py.returncode, 0, f"Script failed: {res_py.stderr}")
            self.assertIn("SUCCESS", res_py.stdout)

            # 5. Verify CLI execution outside repo
            res_cli_list = subprocess.run(
                [str(cli_bin), "list", "--lang", "en"],
                cwd=str(tmp_path),
                capture_output=True,
                text=True,
            )
            self.assertEqual(res_cli_list.returncode, 0)
            self.assertIn("Total forms found: 114", res_cli_list.stdout)

            res_cli_search = subprocess.run(
                [str(cli_bin), "search", "Charter", "--lang", "en"],
                cwd=str(tmp_path),
                capture_output=True,
                text=True,
            )
            self.assertEqual(res_cli_search.returncode, 0)
            self.assertIn("MATCH", res_cli_search.stdout)

            res_cli_test = subprocess.run(
                [str(cli_bin), "test"],
                cwd=str(tmp_path),
                capture_output=True,
                text=True,
            )
            self.assertEqual(res_cli_test.returncode, 0)
            self.assertIn("Test directory not found", res_cli_test.stdout)


if __name__ == "__main__":
    unittest.main()
