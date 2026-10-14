"""tools/site_builder/pages_developers.py
Developer Portal, Engineering Manual & AI Integration Hub for Tasleemat (English & Arabic).

Modularized into:
- tools/site_builder/pages_dev/hub.py      (Developers Hub)
- tools/site_builder/pages_dev/cli.py      (CLI Tooling & Automation)
- tools/site_builder/pages_dev/sdk.py      (Python SDK & API Reference)
- tools/site_builder/pages_dev/mcp.py      (Model Context Protocol Server)
- tools/site_builder/pages_dev/schemas.py  (JSON Schemas & Autonomous Healing)
- tools/site_builder/pages_dev/agentic.py  (Agentic Swarms, CI/CD & Attested Math)
"""

from tools.site_builder.pages_dev import (
    generate_developers_hub_en,
    generate_developers_hub_ar,
    generate_dev_cli_en,
    generate_dev_cli_ar,
    generate_dev_sdk_en,
    generate_dev_sdk_ar,
    generate_dev_mcp_en,
    generate_dev_mcp_ar,
    generate_dev_schemas_en,
    generate_dev_schemas_ar,
    generate_dev_agentic_en,
    generate_dev_agentic_ar,
)

# Backward compatibility aliases
generate_developers_en = generate_developers_hub_en
generate_developers_ar = generate_developers_hub_ar

__all__ = [
    "generate_developers_hub_en",
    "generate_developers_hub_ar",
    "generate_developers_en",
    "generate_developers_ar",
    "generate_dev_cli_en",
    "generate_dev_cli_ar",
    "generate_dev_sdk_en",
    "generate_dev_sdk_ar",
    "generate_dev_mcp_en",
    "generate_dev_mcp_ar",
    "generate_dev_schemas_en",
    "generate_dev_schemas_ar",
    "generate_dev_agentic_en",
    "generate_dev_agentic_ar",
]
