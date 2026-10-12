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
                    "Bilingual (English & Arabic) PMO artifact library and structural data validation interface. "
                    "Provides 114 standardized deliverable templates, metadata, structural JSON validation, and HTML rendering."
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
                    "Supports filtering by project lifecycle phase and tailoring tier. "
                    "Exposes completed-data validation capability status."
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
                    "Retrieve deliverable metadata, English/Arabic titles, lifecycle phase, "
                    "tailoring applicability, and authoritative SHA-256 asset fingerprints."
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
                    "Retrieve the exact text content of a deliverable asset by role and language without filesystem parsing. "
                    "Roles: 'template' (document structure), 'guide' (practitioner instructions), 'prompt' (LLM drafting prompt), "
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
                    "referencing standard PMI PMBOK® and Saudi Digital Government Authority (DGA) glossaries."
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
                    "Verifies structural conformance only; does not constitute stage-gate approval or certification. "
                    "Supports 'strict' mode (all schema constraints required) and 'draft' mode (non-blocking warnings for WIP). "
                    "Supports optional definition_version reference (version tag, definition fingerprint, or schema fingerprint)."
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
                        "definition_version": {
                            "type": "string",
                            "description": "Optional definition version tag ('2.5.0', 'v2.5.0'), definition SHA-256 fingerprint, or schema SHA-256 fingerprint.",
                        },
                        "mode": {
                            "type": "string",
                            "enum": ["strict", "draft"],
                            "default": "strict",
                            "description": "'strict' enforces all constraints; 'draft' emits non-blocking warnings for WIP documents.",
                        },
                    },
                    "required": ["artifact_id", "data"],
                },
            },
            {
                "name": "tasleemat_render_artifact",
                "description": (
                    "Render a deliverable into a styled HTML reference document with Arabic RTL support, "
                    "typography, and document control blocks. Does not create legal signatures or audit attestations."
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
                        "fingerprint": a.fingerprint,
                        "completed_data_validation": a.completed_data_validation,
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
                definition_version = args.get("definition_version")
                report = validate_artifact_data(
                    artifact_id,
                    data,
                    definition_version=definition_version,
                    mode=mode,
                )
                report_dict = report.to_dict()
                # Maintain legacy helper counts for consumer convenience
                report_dict["errors_count"] = len(report.errors)
                report_dict["warnings_count"] = len(report.warnings)
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
                "description": "Standardized PMI & Saudi DGA Arabic-English project management terminology reference.",
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
                    "completed_data_validation": a.completed_data_validation,
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
                "description": "Draft an initial Project Charter (PMO-03.01) structure from raw notes. Requires human PM review.",
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
                "description": "Formulate an initial Risk Register (PMO-04.08.02) draft from workshop findings. Requires human PM review.",
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
            user_msg = (
                f"{system_prompt}\n\n"
                f"## Scope Note: This draft is for practitioner drafting only and requires formal PM and sponsor review.\n\n"
                f"## Project Input Notes:\n{notes}"
            )
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
            user_msg = (
                f"{system_prompt}\n\n"
                f"## Scope Note: This draft risk log requires qualitative and quantitative risk analysis by the project team.\n\n"
                f"## Risk Workshop Findings:\n{findings}"
            )
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

        # Validate that request is a JSON object per JSON-RPC 2.0 single request spec
        if not isinstance(req, dict):
            # If batch array was sent or scalar, return Invalid Request error
            return json.dumps({
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32600, "message": "Invalid Request: expected a JSON-RPC 2.0 object."},
            })

        # Validate jsonrpc version field: MUST be present and exactly "2.0"
        if "jsonrpc" not in req or req.get("jsonrpc") != "2.0":
            req_id = req.get("id") if isinstance(req.get("id"), (str, int)) and not isinstance(req.get("id"), bool) else None
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32600, "message": "Invalid Request: 'jsonrpc' must be present and exactly '2.0'."},
            })

        # Extract and validate message ID
        # In JSON-RPC 2.0: An identifier established by the Client that MUST contain a String, Number, or NULL value if included.
        # Numbers SHOULD NOT contain fractional parts. Booleans, Arrays, and Objects are invalid.
        # A Notification is a Request object without an "id" member.
        has_id = "id" in req
        msg_id = req.get("id") if has_id else None

        if has_id:
            # Note: bool is a subclass of int in Python, so isinstance(True, int) is True!
            if isinstance(msg_id, bool) or (msg_id is not None and not isinstance(msg_id, (str, int, float))):
                return json.dumps({
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32600, "message": "Invalid Request: 'id' must be a string, integer, or null."},
                })
            if isinstance(msg_id, float):
                if math.isnan(msg_id) or math.isinf(msg_id) or not msg_id.is_integer():
                    return json.dumps({
                        "jsonrpc": "2.0",
                        "id": None,
                        "error": {"code": -32600, "message": "Invalid Request: 'id' must not contain fractional or non-finite numbers."},
                    })
                msg_id = int(msg_id)

        # Validate method member
        method = req.get("method")
        if not isinstance(method, str) or not method:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32600, "message": "Invalid Request: 'method' must be a non-empty string."},
            })

        # Validate params member
        params = req.get("params")
        if params is None:
            params = {}
        elif isinstance(params, list):
            # MCP handlers and tools expect named parameter objects; positional array params are rejected explicitly
            if not has_id:
                return None
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32602, "message": "Invalid params: Positional array parameters are not supported; expected a named parameter object."},
            })
        elif not isinstance(params, dict):
            if not has_id:
                return None
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32602, "message": "Invalid params: 'params' must be an object dictionary."},
            })

        # Dispatch method
        if method not in self.handlers:
            if not has_id:
                # Unhandled notification is silently dropped per JSON-RPC 2.0 notification specification
                return None
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"},
            })

        try:
            result = self.handlers[method](params)
            if not has_id:
                # Notification - no response required
                return None
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": result}, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error handling method {method}: {e}\n{traceback.format_exc()}")
            if not has_id:
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
