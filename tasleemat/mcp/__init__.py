"""
Tasleemat Model Context Protocol (MCP) Package
Exposes standardized MCP tools, resources, and prompts for AI agents,
Claude Desktop, Cursor, OpenCode, and automated workflows.
"""

from tasleemat.mcp.server import MCPServer, main

__all__ = ["MCPServer", "main"]
