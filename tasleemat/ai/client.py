import os
import json
import urllib.request
import urllib.error

def get_config_path():
    return os.getenv("TASLEEMAT_CONFIG_PATH", os.path.expanduser("~/.tasleemat/config.json"))

def load_config():
    path = get_config_path()
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_config(config_dict):
    path = get_config_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config_dict, f, indent=2, ensure_ascii=False)

class AIClient:
    """Unified LLM Client for Tasleemat PMO Artifact Auto-Generation with multi-provider & custom endpoint support."""

    DEFAULT_SUGGESTED_MODELS = {
        "gemini": "gemini-3.8-flash",
        "openai": "gpt-4o",
        "anthropic": "claude-3-5-sonnet-20241022",
        "openrouter": "anthropic/claude-3.5-sonnet",
        "custom": "default-model",
        "ollama": "llama3.2",
        "mock": "mock-v1"
    }

    def __init__(self, provider=None, model=None, api_key=None, endpoint=None):
        cfg = load_config()
        self.provider = (provider or cfg.get("provider") or os.getenv("TASLEEMAT_LLM_PROVIDER") or "gemini").lower()
        default_model = os.getenv("TASLEEMAT_LLM_MODEL") or os.getenv("GEMINI_MODEL") or "gemini-3.8-flash"
        self.model = model or cfg.get("model") or (default_model if self.provider == "gemini" else self.DEFAULT_SUGGESTED_MODELS.get(self.provider, "default-model"))
        self.api_key = api_key or cfg.get("api_key") or self._resolve_api_key(self.provider)
        self.endpoint = endpoint or cfg.get("endpoint") or self._resolve_endpoint(self.provider)

    def _resolve_api_key(self, provider):
        env_map = {
            "gemini": "GEMINI_API_KEY",
            "openai": "OPENAI_API_KEY",
            "anthropic": "ANTHROPIC_API_KEY",
            "openrouter": "OPENROUTER_API_KEY",
            "custom": "CUSTOM_LLM_API_KEY",
        }
        var_name = env_map.get(provider)
        return os.getenv(var_name) if var_name else os.getenv("LLM_API_KEY")

    def _resolve_endpoint(self, provider):
        if provider == "ollama":
            return os.getenv("OLLAMA_HOST", "http://localhost:11434")
        elif provider == "openrouter":
            return os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
        elif provider in ["custom", "openai-compatible"]:
            return os.getenv("CUSTOM_LLM_ENDPOINT")
        return None

    def generate(self, prompt, system_instruction=None, mock=False):
        if mock or self.provider == "mock":
            return self._generate_mock(prompt)
        
        if self.provider == "gemini":
            return self._generate_gemini(prompt, system_instruction)
        elif self.provider == "openai":
            return self._generate_openai(prompt, system_instruction)
        elif self.provider == "anthropic":
            return self._generate_anthropic(prompt, system_instruction)
        elif self.provider == "openrouter":
            return self._generate_openrouter(prompt, system_instruction)
        elif self.provider in ["custom", "openai-compatible"]:
            return self._generate_openai_compatible(prompt, system_instruction)
        elif self.provider == "ollama":
            return self._generate_ollama(prompt, system_instruction)
        else:
            # Fallback to generic OpenAI-compatible chat completion if custom provider specified
            return self._generate_openai_compatible(prompt, system_instruction)

    def _generate_mock(self, prompt):
        return (
            "<!-- UNVALIDATED TEST OUTPUT: NOT SUITABLE FOR PRODUCTION USE -->\n"
            "<!-- MOCK AI GENERATION: Structural test placeholder only (no LLM inference performed) -->\n"
            "# AI Generated Deliverable [MOCK TEST ONLY]\n\n"
            f"Generated from prompt summary: {prompt[:120]}...\n\n"
            "- Status: Mock Draft\n"
            "- Notice: UNVALIDATED TEST OUTPUT — No governance verification or project review has been performed.\n"
            "- Mock Engine: Tasleemat Offline Mock Provider\n"
        )

    def _generate_gemini(self, prompt, system_instruction=None):
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not set. Run 'tasleemat config set --provider gemini --key <KEY>' or export GEMINI_API_KEY.")
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        
        contents = []
        if system_instruction:
            contents.append({"role": "user", "parts": [{"text": f"System Instructions:\n{system_instruction}\n\nTask Prompt:\n{prompt}"}]})
        else:
            contents.append({"role": "user", "parts": [{"text": prompt}]})

        payload = json.dumps({"contents": contents}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        
        try:
            with urllib.request.urlopen(req) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                return res_data["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            raise RuntimeError(f"Gemini API Error ({e.code}): {err_body}")

    def _generate_openai(self, prompt, system_instruction=None):
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not set. Run 'tasleemat config set --provider openai --key <KEY>' or export OPENAI_API_KEY.")
        
        url = (self.endpoint.rstrip('/') + '/chat/completions') if self.endpoint else "https://api.openai.com/v1/chat/completions"
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        payload = json.dumps({"model": self.model, "messages": messages}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        })

        try:
            with urllib.request.urlopen(req) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                return res_data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            raise RuntimeError(f"OpenAI API Error ({e.code}): {err_body}")

    def _generate_openrouter(self, prompt, system_instruction=None):
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY is not set. Run 'tasleemat config set --provider openrouter --key <KEY>' or export OPENROUTER_API_KEY.")

        base_url = self.endpoint or "https://openrouter.ai/api/v1"
        url = f"{base_url.rstrip('/')}/chat/completions"

        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        payload = json.dumps({"model": self.model, "messages": messages}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://fakhr.me/Tasleemat/",
            "X-Title": "Tasleemat PMO Operating System"
        })

        try:
            with urllib.request.urlopen(req) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                return res_data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            raise RuntimeError(f"OpenRouter API Error ({e.code}): {err_body}")

    def _generate_openai_compatible(self, prompt, system_instruction=None):
        base_url = self.endpoint or "https://api.openai.com/v1"
        url = f"{base_url.rstrip('/')}/chat/completions"

        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        payload = json.dumps({"model": self.model, "messages": messages}).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        req = urllib.request.Request(url, data=payload, headers=headers)

        try:
            with urllib.request.urlopen(req) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                return res_data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            raise RuntimeError(f"Custom LLM API Error ({e.code}): {err_body}")

    def _generate_anthropic(self, prompt, system_instruction=None):
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY is not set. Run 'tasleemat config set --provider anthropic --key <KEY>' or export ANTHROPIC_API_KEY.")
        
        url = (self.endpoint.rstrip('/') + '/messages') if self.endpoint else "https://api.anthropic.com/v1/messages"
        payload_dict = {
            "model": self.model,
            "max_tokens": 4096,
            "messages": [{"role": "user", "content": prompt}]
        }
        if system_instruction:
            payload_dict["system"] = system_instruction

        payload = json.dumps(payload_dict).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01"
        })

        try:
            with urllib.request.urlopen(req) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                return res_data["content"][0]["text"]
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            raise RuntimeError(f"Anthropic API Error ({e.code}): {err_body}")

    def _generate_ollama(self, prompt, system_instruction=None):
        base_url = self.endpoint or "http://localhost:11434"
        url = f"{base_url.rstrip('/')}/api/generate"
        
        full_prompt = f"System: {system_instruction}\n\nPrompt: {prompt}" if system_instruction else prompt
        payload = json.dumps({"model": self.model, "prompt": full_prompt, "stream": False}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})

        try:
            with urllib.request.urlopen(req) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                return res_data["response"]
        except urllib.error.URLError as e:
            raise RuntimeError(f"Ollama Connection Error: {e}. Is Ollama running on {base_url}?")
