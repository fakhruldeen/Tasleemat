import unittest
import os
import sys
import tempfile
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.ai import AIClient, load_config, save_config

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

    def test_openrouter_and_custom_models(self):
        # OpenRouter with custom model
        client_or = AIClient(provider="openrouter", model="anthropic/claude-3.7-sonnet", api_key="sk-or-test")
        self.assertEqual(client_or.provider, "openrouter")
        self.assertEqual(client_or.model, "anthropic/claude-3.7-sonnet")
        self.assertEqual(client_or.endpoint, "https://openrouter.ai/api/v1")

        # Custom OpenAI-compatible provider with DeepSeek R1
        client_custom = AIClient(provider="custom", model="deepseek/deepseek-r1", endpoint="https://api.deepseek.com/v1", api_key="sk-test")
        self.assertEqual(client_custom.provider, "custom")
        self.assertEqual(client_custom.model, "deepseek/deepseek-r1")
        self.assertEqual(client_custom.endpoint, "https://api.deepseek.com/v1")

    def test_arbitrary_unrestricted_model_strings(self):
        # User can set ANY model identifier
        any_model = "my-custom-fine-tuned-qwen-2.5-72b:v2"
        client = AIClient(provider="openai", model=any_model, api_key="sk-test")
        self.assertEqual(client.model, any_model)

if __name__ == "__main__":
    unittest.main()
