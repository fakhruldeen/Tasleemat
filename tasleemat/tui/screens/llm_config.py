"""
tasleemat.tui.screens.llm_config
Screen for configuring LLM provider, API credentials, custom base endpoints, and unrestricted model selection.
Supports OpenRouter, Google Gemini, OpenAI, Claude, Ollama, and generic OpenAI-compatible APIs (Groq, Together, DeepSeek, etc.).
"""

import time
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, ScrollableContainer
from textual.widgets import Static, Input, Select, Button, Label
from tasleemat.tui.i18n import t
from tasleemat.ai import AIClient, load_config, save_config

PROVIDERS = [
    ("Google Gemini", "gemini"),
    ("OpenAI", "openai"),
    ("Anthropic Claude", "anthropic"),
    ("OpenRouter (Universal Multi-Model Hub)", "openrouter"),
    ("Custom / OpenAI-Compatible (Groq, DeepSeek, Together, vLLM, LM Studio)", "custom"),
    ("Ollama (Local Offline Models)", "ollama"),
    ("Mock Engine (Offline Test)", "mock"),
]

DEFAULT_SUGGESTIONS = {
    "gemini": ("gemini-2.5-flash", ""),
    "openai": ("gpt-4o", ""),
    "anthropic": ("claude-3-5-sonnet-20241022", ""),
    "openrouter": ("anthropic/claude-3.5-sonnet", "https://openrouter.ai/api/v1"),
    "custom": ("deepseek-chat", "https://api.deepseek.com/v1"),
    "ollama": ("llama3.2", "http://localhost:11434"),
    "mock": ("mock-v1", ""),
}

class LLMConfigScreen(ScrollableContainer):
    """Screen for managing LLM API credentials & testing connection with flexible provider and model choices."""

    def __init__(self, lang: str = "en", **kwargs):
        super().__init__(**kwargs)
        self.lang = lang
        self.cfg = load_config()

    def compose(self) -> ComposeResult:
        with Vertical(classes="panel-container"):
            yield Static(f"### {t('tab_llm_config', self.lang)}", classes="card-title")
            yield Static("Configure any LLM provider, custom API gateway (OpenRouter, Groq, DeepSeek, etc.), and choose any model without restrictions.", classes="card-subtitle")

            with Vertical(classes="card"):
                yield Label(t("lbl_provider", self.lang), classes="form-label")
                current_provider = self.cfg.get("provider", "gemini")
                yield Select(
                    [(name, pid) for name, pid in PROVIDERS],
                    value=current_provider,
                    id="sel_provider"
                )

                yield Label(t("lbl_api_key", self.lang), classes="form-label")
                current_key = self.cfg.get("api_key", "")
                yield Input(
                    value=current_key,
                    placeholder="Enter API Key (e.g. sk-or-v1-... or AIzaSy... or sk-...)",
                    password=True,
                    id="inp_api_key"
                )

                yield Label("Model ID (Type any preferred model):", classes="form-label")
                current_model = self.cfg.get("model", DEFAULT_SUGGESTIONS.get(current_provider, ("gemini-2.5-flash", ""))[0])
                yield Input(
                    value=current_model,
                    placeholder="e.g. anthropic/claude-3.7-sonnet, deepseek/deepseek-r1, qwen/qwen-2.5-72b, gpt-4o, llama3.3:70b",
                    id="inp_model"
                )
                yield Static(
                    "[dim]💡 Tip: Models are fast-growing and completely unrestricted. Type any exact model ID from OpenRouter, OpenAI, Google, Anthropic, or Hugging Face.[/dim]",
                    classes="card-subtitle"
                )

                yield Label("Custom API Base URL / Endpoint (Optional):", classes="form-label")
                current_endpoint = self.cfg.get("endpoint", "")
                yield Input(
                    value=current_endpoint or "",
                    placeholder="e.g. https://openrouter.ai/api/v1 or https://api.groq.com/openai/v1 or http://localhost:11434",
                    id="inp_endpoint"
                )

                with Horizontal():
                    yield Button(t("btn_test_conn", self.lang), id="btn_test", variant="primary")
                    yield Button(t("btn_save_config", self.lang), id="btn_save", variant="success")
                    yield Button(t("btn_reset", self.lang), id="btn_reset", classes="-secondary")

                yield Static("", id="status_message")

    def on_select_changed(self, event: Select.Changed) -> None:
        """When provider changes, update suggested model and endpoint defaults if applicable."""
        if event.select.id == "sel_provider":
            prov = str(event.value)
            model_inp = self.query_one("#inp_model", Input)
            endpoint_inp = self.query_one("#inp_endpoint", Input)

            suggested_model, suggested_endpoint = DEFAULT_SUGGESTIONS.get(prov, ("", ""))
            if suggested_model and not model_inp.value:
                model_inp.value = suggested_model
            elif suggested_model:
                # Update placeholder to inspire the user
                model_inp.placeholder = f"e.g. {suggested_model}"

            if suggested_endpoint and not endpoint_inp.value:
                endpoint_inp.value = suggested_endpoint

    def on_button_pressed(self, event: Button.Pressed) -> None:
        status = self.query_one("#status_message", Static)
        prov_select = self.query_one("#sel_provider", Select)
        key_inp = self.query_one("#inp_api_key", Input)
        model_inp = self.query_one("#inp_model", Input)
        endpoint_inp = self.query_one("#inp_endpoint", Input)

        provider = str(prov_select.value)
        api_key = key_inp.value.strip()
        model = model_inp.value.strip() or DEFAULT_SUGGESTIONS.get(provider, ("default", ""))[0]
        endpoint = endpoint_inp.value.strip() or None

        if event.button.id == "btn_save":
            self.cfg["provider"] = provider
            self.cfg["api_key"] = api_key
            self.cfg["model"] = model
            self.cfg["endpoint"] = endpoint
            save_config(self.cfg)
            status.update(f"✅ Configuration saved to ~/.tasleemat/config.json ({provider} / {model})")

        elif event.button.id == "btn_reset":
            self.cfg = {}
            save_config({})
            key_inp.value = ""
            endpoint_inp.value = ""
            model_inp.value = DEFAULT_SUGGESTIONS.get("gemini", ("gemini-2.5-flash", ""))[0]
            prov_select.value = "gemini"
            status.update("🔄 Configuration reset to defaults.")

        elif event.button.id == "btn_test":
            status.update(f"⏳ Testing connection to {provider} (Model: {model})...")
            self.app.call_later(self._run_test_connection, provider, model, api_key, endpoint)

    def _run_test_connection(self, provider, model, api_key, endpoint):
        status = self.query_one("#status_message", Static)
        t0 = time.time()
        try:
            client = AIClient(provider=provider, model=model, api_key=api_key, endpoint=endpoint)
            if provider == "mock":
                reply = client.generate("Ping test", mock=True)
            else:
                reply = client.generate("Respond with the word OK.", system_instruction="You are a health check agent.")
            dt = int((time.time() - t0) * 1000)
            status.update(f"🟢 Connected successfully! Response time: {dt}ms | Provider: {provider} | Model: {model}")
        except Exception as e:
            dt = int((time.time() - t0) * 1000)
            status.update(f"🔴 Connection failed after {dt}ms: {e}")
