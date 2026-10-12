"""
Standard Model Context Protocol (MCP) Server for Tasleemat.

Implements JSON-RPC 2.0 protocol over stdio to provide AI agents,
Claude Desktop, Cursor, OpenCode, and IDEs with native access to:
- 114 Bilingual PMO Artifacts & Metadata (list_artifacts, get_artifact)
- Templates, Practitioner Guides & LLM Prompts (get_asset)
- Standardized Bilingual PMO Terminology (get_lexicon)
- Structural JSON Data Validation in strict & draft modes (validate_data)
- Standalone Offline Document Rendering (render_artifact)
"""

import sys
import json
import logging
import traceback
from typing import Any, Dict, List, Optional

import tasleemat
from tasleemat.catalog import (
    list_artifacts,
    get_artifact_definition,
    get_artifact_asset,
    get_lexicon,
    get_tailoring_profile,
)
from tasleemat.validation import validate_artifact_data
from tasleemat.rendering import render_artifact

# Configure logging to stderr to prevent interference with stdio JSON-RPC transport
logging.basicConfig(
    level=logging.INFO,
    format="[Tasleemat-MCP] %(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger("tasleemat.mcp")


class MCPServer:
    """Zero-dependency JSON-RPC 2.0 Model Context Protocol Server for Tasleemat."""

    PROTOCOL_VERSION = "2024-11-05"
    SERVER_NAME = "tasleemat-mcp"
    SERVER_VERSION = tasleemat.__version__

    def __init__(self):
        self.handlers = {
            "initialize": self._handle_initialize,
            "notifications/initialized": self._handle_initialized,
            "tools/list": self._handle_tools_list,
            "tools/call": self._handle_tools_call,
            "resources/list": self._handle_resources_list,
            "resources/read": self._handle_resources_read,
            "prompts/list": self._handle_prompts_list,
            "prompts/get": self._handle_prompts_get,
            "ping": self._handle_ping,
        }

    def _handle_initialize(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handshake and protocol capability negotiation."""
        return {
            "protocolVersion": self.PROTOCOL_VERSION,
            "capabilities": {
                "tools": {"listChanged": False},
                "resources": {"subscribe": False, "listChanged": False},
                "prompts": {"listChanged": False},
            },
            "serverInfo": {
                "name": self.SERVER_NAME,
                "version": self.SERVER_VERSION,
                "description": (
                    "Enterprise Bilingual (English & Arabic) PMO Operating System. "
                    "Provides 114 standardized deliverables, templates, validation, and rendering."
                ),
            },
        }

    def _handle_initialized(self, params: Dict[str, Any]) -> None:
        """Client notification that initialization has completed."""
        logger.info("MCP Client connection initialized successfully.")
        return None

    def _handle_ping(self, params: Dict[str, Any]) -> Dict[str, Any]:
        return {}

    def _handle_tools_list(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Enumerate standard Tasleemat MCP tools."""
        tools = [
            {
                "name": "tasleemat_list_artifacts",
                "description": (
                    "Discover and list standardized PMO deliverables from the Tasleemat catalog. "
                    "Supports filtering by project lifecycle phase and tailoring tier."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "phase": {
                            "type": "string",
                            "description": "Optional lifecycle phase to filter by (e.g., 'Initiating', 'Planning', 'Executing', 'Monitoring & Controlling', 'Closing').",
                        },
                        "tier": {
                            "type": "string",
                            "description": "Optional tailoring tier to filter by ('1', '2', or '3').",
                        },
                    },
                },
            },
            {
                "name": "tasleemat_get_artifact",
                "description": (
                    "Retrieve comprehensive metadata, English/Arabic names, lifecycle phase, "
                    "tailoring applicability, and cryptographic SHA-256 fingerprint for a specific deliverable."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The canonical deliverable ID (e.g., 'PMO-03.01', 'PMO-04.08.02').",
                        }
                    },
                    "required": ["artifact_id"],
                },
            },
            {
                "name": "tasleemat_get_asset",
                "description": (
                    "Retrieve the exact content of a deliverable asset by role and language without filesystem parsing. "
                    "Roles: 'template' (document structure), 'guide' (practitioner instructions), 'prompt' (LLM generation prompt), "
                    "'schema' (data specification), 'dictionary' (tabular fields), 'example' (reference implementation)."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The canonical deliverable ID (e.g., 'PMO-03.01').",
                        },
                        "role": {
                            "type": "string",
                            "enum": ["template", "guide", "prompt", "schema", "dictionary", "example"],
                            "description": "The asset role to retrieve.",
                        },
                        "lang": {
                            "type": "string",
                            "enum": ["en", "ar"],
                            "default": "en",
                            "description": "The requested language ('en' for English, 'ar' for Arabic).",
                        },
                    },
                    "required": ["artifact_id", "role"],
                },
            },
            {
                "name": "tasleemat_get_lexicon",
                "description": (
                    "Search and retrieve standardized bilingual (English <-> Arabic) PMO terminology "
                    "conforming to official PMI PMBOK® and Saudi Digital Government Authority (DGA) standards."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Optional category to filter by (e.g. 'Initiating', 'Planning', 'Risk', 'General PMO').",
                        },
                        "query": {
                            "type": "string",
                            "description": "Optional text search query to filter terminology in English or Arabic.",
                        },
                    },
                },
            },
            {
                "name": "tasleemat_validate_data",
                "description": (
                    "Validate structured artifact data against formal companion JSON schemas. "
                    "Supports 'strict' mode (for formal stage-gate approval) and 'draft' mode (with non-blocking warnings). "
                    "Returns exact JSON Pointer error paths."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The canonical deliverable ID (e.g. 'PMO-03.01', 'PMO-04.08.02', 'PMO-06.01').",
                        },
                        "data": {
                            "type": "object",
                            "description": "The JSON payload representing the completed or draft artifact data.",
                        },
                        "mode": {
                            "type": "string",
                            "enum": ["strict", "draft"],
                            "default": "strict",
                            "description": "'strict' enforces all constraints; 'draft' emits non-blocking warnings.",
                        },
                    },
                    "required": ["artifact_id", "data"],
                },
            },
            {
                "name": "tasleemat_render_artifact",
                "description": (
                    "Render a deliverable into a publication-ready, styled HTML document with full Arabic RTL support, "
                    "responsive typography, status badges, and executive Document Control sign-off tables."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The canonical deliverable ID (e.g. 'PMO-03.01').",
                        },
                        "lang": {
                            "type": "string",
                            "enum": ["en", "ar"],
                            "default": "en",
                            "description": "Language of the template to render ('en' or 'ar').",
                        },
                        "data": {
                            "type": "object",
                            "description": "Optional JSON data dictionary to interpolate into template placeholders.",
                        },
                    },
                    "required": ["artifact_id"],
                },
            },
        ]
        return {"tools": tools}

    def _handle_tools_call(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Dispatch tool calls to the Tasleemat library."""
        tool_name = params.get("name")
        args = params.get("arguments", {})

        try:
            if tool_name == "tasleemat_list_artifacts":
                phase = args.get("phase")
                tier = args.get("tier")
                results = list_artifacts(phase=phase, tier=tier)
                summaries = [
                    {
                        "artifact_id": a.artifact_id,
                        "name_en": a.name_en,
                        "name_ar": a.name_ar,
                        "phase_code": a.phase_code,
                        "phase_name_en": a.phase_name_en,
                        "fingerprint": a.fingerprint[:16] + "...",
                    }
                    for a in results
                ]
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(
                                {"total_found": len(summaries), "artifacts": summaries},
                                indent=2,
                                ensure_ascii=False,
                            ),
                        }
                    ]
                }

            elif tool_name == "tasleemat_get_artifact":
                artifact_id = args["artifact_id"]
                defn = get_artifact_definition(artifact_id)
                return {
                    "content": [
                        {"type": "text", "text": json.dumps(defn, indent=2, ensure_ascii=False)}
                    ]
                }

            elif tool_name == "tasleemat_get_asset":
                artifact_id = args["artifact_id"]
                role = args["role"]
                lang = args.get("lang", "en")
                asset = get_artifact_asset(artifact_id, role=role, lang=lang)
                if isinstance(asset, (dict, list)):
                    content_str = json.dumps(asset, indent=2, ensure_ascii=False)
                else:
                    content_str = str(asset)
                return {
                    "content": [{"type": "text", "text": content_str}]
                }

            elif tool_name == "tasleemat_get_lexicon":
                category = args.get("category")
                query = args.get("query", "").strip().lower()
                terms = get_lexicon(category=category)
                if query:
                    terms = [
                        t for t in terms
                        if query in t.get("en_name", "").lower() or query in t.get("ar_name", "").lower()
                    ]
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(
                                {"total_terms": len(terms), "terms": terms},
                                indent=2,
                                ensure_ascii=False,
                            ),
                        }
                    ]
                }

            elif tool_name == "tasleemat_validate_data":
                artifact_id = args["artifact_id"]
                data = args["data"]
                mode = args.get("mode", "strict")
                report = validate_artifact_data(artifact_id, data, mode=mode)
                report_dict = {
                    "valid": report.valid,
                    "mode": report.mode,
                    "artifact_id": report.artifact_id,
                    "package_version": report.package_version,
                    "definition_fingerprint": report.definition_fingerprint,
                    "schema_id": report.schema_id,
                    "schema_dialect": report.schema_dialect,
                    "errors_count": len(report.errors),
                    "warnings_count": len(report.warnings),
                    "errors": [
                        {
                            "field_path": e.field_path,
                            "code": e.code,
                            "message": e.message,
                        }
                        for e in report.errors
                    ],
                    "warnings": report.warnings,
                }
                return {
                    "content": [
                        {"type": "text", "text": json.dumps(report_dict, indent=2, ensure_ascii=False)}
                    ]
                }

            elif tool_name == "tasleemat_render_artifact":
                artifact_id = args["artifact_id"]
                lang = args.get("lang", "en")
                data = args.get("data")
                html_output = render_artifact(artifact_id, lang=lang, data=data)
                return {
                    "content": [
                        {"type": "text", "text": html_output}
                    ]
                }

            else:
                raise ValueError(f"Unknown tool: {tool_name}")

        except Exception as e:
            logger.error(f"Error executing tool {tool_name}: {e}\n{traceback.format_exc()}")
            return {
                "isError": True,
                "content": [{"type": "text", "text": f"Error executing {tool_name}: {str(e)}"}],
            }

    def _handle_resources_list(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """List standard MCP resource URIs."""
        resources = [
            {
                "uri": "pmo://catalog",
                "name": "Tasleemat Artifact Catalog",
                "description": "Canonical inventory of all 114 bilingual deliverables, metadata, and fingerprints.",
                "mimeType": "application/json",
            },
            {
                "uri": "pmo://lexicon",
                "name": "Bilingual PMO Lexicon",
                "description": "Standardized PMI & Saudi DGA Arabic-English project management terminology.",
                "mimeType": "application/json",
            },
        ]
        return {"resources": resources}

    def _handle_resources_read(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Stream resource content by URI."""
        uri = params.get("uri", "")
        if uri == "pmo://catalog":
            artifacts = list_artifacts()
            data = [
                {
                    "artifact_id": a.artifact_id,
                    "name_en": a.name_en,
                    "name_ar": a.name_ar,
                    "phase_name_en": a.phase_name_en,
                    "phase_code": a.phase_code,
                    "fingerprint": a.fingerprint,
                }
                for a in artifacts
            ]
            return {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "application/json",
                        "text": json.dumps(data, indent=2, ensure_ascii=False),
                    }
                ]
            }
        elif uri == "pmo://lexicon":
            terms = get_lexicon()
            return {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "application/json",
                        "text": json.dumps(terms, indent=2, ensure_ascii=False),
                    }
                ]
            }
        else:
            raise ValueError(f"Resource not found: {uri}")

    def _handle_prompts_list(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Enumerate workflow prompts."""
        prompts = [
            {
                "name": "draft_project_charter",
                "description": "Draft a formal, audit-ready PMI Project Charter (PMO-03.01) from raw notes.",
                "arguments": [
                    {
                        "name": "project_notes",
                        "description": "Raw meeting notes, kickoff summary, or project requirements.",
                        "required": True,
                    },
                    {
                        "name": "lang",
                        "description": "Language for the draft ('en' or 'ar'). Default: 'en'.",
                        "required": False,
                    },
                ],
            },
            {
                "name": "conduct_risk_assessment",
                "description": "Formulate a PMI-compliant Risk Register (PMO-04.08.02) from workshop findings.",
                "arguments": [
                    {
                        "name": "risk_findings",
                        "description": "Identified project risks, severity, probability, or mitigations.",
                        "required": True,
                    },
                    {
                        "name": "lang",
                        "description": "Language for the register ('en' or 'ar'). Default: 'en'.",
                        "required": False,
                    },
                ],
            },
        ]
        return {"prompts": prompts}

    def _handle_prompts_get(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Fetch pre-engineered prompt workflows."""
        prompt_name = params.get("name")
        args = params.get("arguments", {})

        if prompt_name == "draft_project_charter":
            lang = args.get("lang", "en")
            notes = args.get("project_notes", "")
            system_prompt = get_artifact_asset("PMO-03.01", role="prompt", lang=lang)
            user_msg = f"{system_prompt}\n\n## Project Input Notes:\n{notes}"
            return {
                "description": "Draft Project Charter Prompt",
                "messages": [
                    {
                        "role": "user",
                        "content": {"type": "text", "text": user_msg},
                    }
                ],
            }
        elif prompt_name == "conduct_risk_assessment":
            lang = args.get("lang", "en")
            findings = args.get("risk_findings", "")
            system_prompt = get_artifact_asset("PMO-04.08.02", role="prompt", lang=lang)
            user_msg = f"{system_prompt}\n\n## Risk Workshop Findings:\n{findings}"
            return {
                "description": "Conduct Risk Assessment Prompt",
                "messages": [
                    {
                        "role": "user",
                        "content": {"type": "text", "text": user_msg},
                    }
                ],
            }
        else:
            raise ValueError(f"Unknown prompt: {prompt_name}")

    def handle_message(self, request_data: str) -> Optional[str]:
        """Process a single JSON-RPC 2.0 message string."""
        if not request_data.strip():
            return None

        try:
            req = json.loads(request_data)
        except json.JSONDecodeError as e:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {str(e)}"},
            })

        msg_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})

        if method not in self.handlers:
            if msg_id is None:
                # Notifications without handlers are ignored
                return None
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"},
            })

        try:
            result = self.handlers[method](params)
            if msg_id is None:
                # Notification - no response required
                return None
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": result}, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error handling method {method}: {e}\n{traceback.format_exc()}")
            if msg_id is None:
                return None
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32603, "message": f"Internal error: {str(e)}"},
            })

    def run_stdio(self) -> None:
        """Run the server reading from stdin and writing to stdout."""
        logger.info(f"Starting Tasleemat MCP Server v{self.SERVER_VERSION} on stdio...")
        for line in sys.stdin:
            response = self.handle_message(line)
            if response:
                sys.stdout.write(response + "\n")
                sys.stdout.flush()


def main() -> int:
    """Entrypoint function for CLI execution."""
    server = MCPServer()
    try:
        server.run_stdio()
        return 0
    except (KeyboardInterrupt, BrokenPipeError):
        return 0
    except Exception as e:
        logger.error(f"Fatal server crash: {e}\n{traceback.format_exc()}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
