"""
Executable entry point for Tasleemat MCP Server.
Usage:
    python -m tasleemat.mcp
"""

import sys
from tasleemat.mcp.server import main

if __name__ == "__main__":
    sys.exit(main())
