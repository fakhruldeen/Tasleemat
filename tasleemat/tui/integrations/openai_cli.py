"""
tasleemat.tui.integrations.openai_cli
Configures OpenAI CLI and creates an interactive PMO Agent replica with tool calling.
"""

import os
import json
import pathlib

OPENAI_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "tasleemat_list_artifacts",
            "description": "List standardized PMO deliverables filtered by phase or tailoring tier.",
            "parameters": {
                "type": "object",
                "properties": {
                    "phase": {"type": "string", "description": "Optional phase code e.g. '03'"},
                    "tier": {"type": "string", "description": "Optional tailoring tier e.g. '1', '2', or '3'"}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "tasleemat_get_asset",
            "description": "Retrieve official template, practitioner guide, prompt, schema, or example for a PMO deliverable.",
            "parameters": {
                "type": "object",
                "properties": {
                    "artifact_id": {"type": "string", "description": "PMO Code e.g. 'PMO-03.01'"},
                    "role": {"type": "string", "enum": ["template", "guide", "prompt", "schema", "dictionary"], "description": "Asset role"},
                    "lang": {"type": "string", "enum": ["en", "ar"], "description": "Language"}
                },
                "required": ["artifact_id", "role"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "tasleemat_validate_data",
            "description": "Validate structured project data against formal JSON schema contracts.",
            "parameters": {
                "type": "object",
                "properties": {
                    "artifact_id": {"type": "string", "description": "PMO Code e.g. 'PMO-03.01'"},
                    "data": {"type": "object", "description": "Structured project data payload to validate"},
                    "mode": {"type": "string", "enum": ["strict", "draft"], "description": "Validation mode"}
                },
                "required": ["artifact_id", "data"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "tasleemat_get_lexicon",
            "description": "Search bilingual PMI PMBOK & Saudi DGA standardized terminology.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search keyword in English or Arabic"},
                    "category": {"type": "string", "description": "Lifecycle phase or category"}
                }
            }
        }
    }
]

SYSTEM_PROMPT = """You are the official Tasleemat PMO Director AI Agent.
You assist project managers, PMO leads, and executives with standard deliverable drafting, bilingual terminology (Arabic & English), and JSON schema validation.

When assisting users:
1. Always reference official Tasleemat form codes (e.g., PMO-03.01 for Project Charter, PMO-04.08.02 for Risk Register).
2. Maintain strict 1:1 bilingual parity.
3. Validate all structured data payloads using `tasleemat_validate_data`.
4. Ensure compliance with PMI PMBOK (6th, 7th & 8th Edition) and Saudi Digital Government Authority (DGA) standards.
"""

RUNNER_SCRIPT = '''#!/usr/bin/env python3
"""
Interactive OpenAI CLI PMO Director Agent Replica.
Run directly with: python .openai/agent_runner.py
"""

import os
import sys
import json
import urllib.request
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

def load_credentials():
    cfg_file = pathlib.Path.home() / ".tasleemat" / "config.json"
    key = os.getenv("OPENAI_API_KEY")
    model = "gpt-4o"
    if cfg_file.exists():
        try:
            with open(cfg_file, "r", encoding="utf-8") as f:
                d = json.load(f)
                key = d.get("api_key") or key
                model = d.get("model") or model
        except Exception:
            pass
    return key, model

def main():
    print("\\033[95m====================================================\\033[0m")
    print("\\033[95m   🤖 Tasleemat OpenAI PMO Director CLI Agent       \\033[0m")
    print("\\033[95m====================================================\\033[0m\\n")

    api_key, model = load_credentials()
    if not api_key:
        print("\\033[91m❌ No OpenAI API Key found. Configure via 'tasleemat config set --key YOUR_KEY' or OPENAI_API_KEY.\\033[0m")
        sys.exit(1)

    print(f"\\033[92mConnected using model: {model}\\033[0m")
    print("Type your project question, deliverable request, or 'exit' to quit.\\n")

    while True:
        try:
            user_input = input("\\033[94mUser > \\033[0m").strip()
            if not user_input or user_input.lower() in ["exit", "quit", "q"]:
                break
            
            # Simple direct completion request
            url = "https://api.openai.com/v1/chat/completions"
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": "You are the Tasleemat PMO Director Agent. Provide expert PMBOK & Saudi DGA guidance."},
                    {"role": "user", "content": user_input}
                ],
                "temperature": 0.4
            }
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }
            )
            with urllib.request.urlopen(req, timeout=45) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                reply = res_data["choices"][0]["message"]["content"]
                print(f"\\n\\033[92mPMO Director >\\033[0m\\n{reply}\\n")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\\033[91mError: {e}\\033[0m\\n")

if __name__ == "__main__":
    main()
'''

def configure_openai_cli(workspace_path: pathlib.Path) -> list[str]:
    """
    Configures OpenAI CLI & Agent Replica in the workspace:
    1. Creates .openai/config.json with model and system prompt.
    2. Writes .openai/tools.json containing the function calling schemas.
    3. Writes .openai/agent_runner.py ready-to-run interactive CLI.
    4. Writes SYSTEM_PROMPT.md.
    Returns list of modified/created file paths.
    """
    actions = []
    openai_dir = workspace_path / ".openai"
    openai_dir.mkdir(parents=True, exist_ok=True)

    # 1. .openai/config.json
    cfg_file = openai_dir / "config.json"
    cfg_data = {
        "model": "gpt-4o",
        "system_instruction_file": "instructions.md",
        "tools_file": "tools.json"
    }
    with open(cfg_file, "w", encoding="utf-8") as f:
        json.dump(cfg_data, f, indent=2, ensure_ascii=False)
    actions.append(str(cfg_file))

    # 2. .openai/tools.json
    tools_file = openai_dir / "tools.json"
    with open(tools_file, "w", encoding="utf-8") as f:
        json.dump(OPENAI_TOOLS, f, indent=2, ensure_ascii=False)
    actions.append(str(tools_file))

    # 3. .openai/instructions.md
    inst_file = openai_dir / "instructions.md"
    inst_file.write_text(SYSTEM_PROMPT, encoding="utf-8")
    actions.append(str(inst_file))

    # 4. .openai/agent_runner.py
    runner_file = openai_dir / "agent_runner.py"
    runner_file.write_text(RUNNER_SCRIPT, encoding="utf-8")
    try:
        runner_file.chmod(0o755)
    except Exception:
        pass
    actions.append(str(runner_file))

    return actions
