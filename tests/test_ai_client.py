import unittest
import os
import sys
import tempfile
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "sdk" / "python"))

from tasleemat.ai import AIClient, load_config, save_config

class TestAIClient(unittest.TestCase):

    def test_mock_generation(self):
        client = AIClient(provider="mock")
        res = client.generate("Create Project Charter for Cloud Migration", mock=True)
        self.assertIn("AI Generated Deliverable", res)
        self.assertIn("Cloud Migration", res)

    def test_provider_resolution(self):
        client = AIClient(provider="gemini", api_key="dummy_key")
        self.assertEqual(client.provider, "gemini")
        self.assertEqual(client.model, "gemini-2.5-flash")
        self.assertEqual(client.api_key, "dummy_key")

    def test_missing_api_key_raises_error(self):
        client = AIClient(provider="openai", api_key=None)
        old_val = os.environ.pop("OPENAI_API_KEY", None)
        try:
            with self.assertRaises(ValueError):
                client.generate("Test prompt")
        finally:
            if old_val:
                os.environ["OPENAI_API_KEY"] = old_val

    def test_config_save_load(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_path = os.path.join(tmpdir, "config.json")
            old_path = os.environ.get("TASLEEMAT_CONFIG_PATH")
            os.environ["TASLEEMAT_CONFIG_PATH"] = test_path
            try:
                save_config({"provider": "ollama", "model": "llama3.2"})
                cfg = load_config()
                self.assertIsInstance(cfg, dict)
            finally:
                if old_path:
                    os.environ["TASLEEMAT_CONFIG_PATH"] = old_path

if __name__ == "__main__":
    unittest.main()
