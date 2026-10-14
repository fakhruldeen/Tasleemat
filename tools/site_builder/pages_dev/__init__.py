"""tools/site_builder/pages_dev/__init__.py
Developer Portal modular pages package.
"""

from tools.site_builder.pages_dev.hub import (
    generate_developers_hub_en,
    generate_developers_hub_ar,
)
from tools.site_builder.pages_dev.cli import (
    generate_dev_cli_en,
    generate_dev_cli_ar,
)
from tools.site_builder.pages_dev.sdk import (
    generate_dev_sdk_en,
    generate_dev_sdk_ar,
)
from tools.site_builder.pages_dev.mcp import (
    generate_dev_mcp_en,
    generate_dev_mcp_ar,
)
from tools.site_builder.pages_dev.schemas import (
    generate_dev_schemas_en,
    generate_dev_schemas_ar,
)
from tools.site_builder.pages_dev.agentic import (
    generate_dev_agentic_en,
    generate_dev_agentic_ar,
)

__all__ = [
    "generate_developers_hub_en",
    "generate_developers_hub_ar",
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
