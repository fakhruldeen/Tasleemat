"""
Comprehensive Unit & Integration Test Suite for Tasleemat MCP Server.
Tests JSON-RPC 2.0 handshake, tools listing, tool dispatching, resources,
prompts, and error handling over simulated stdio messages.
"""

import json
import unittest
from unittest.mock import patch
from tasleemat.mcp.server import MCPServer
import tasleemat


class TestMCPServer(unittest.TestCase):

    def setUp(self):
        self.server = MCPServer()

    def send_request(self, method: str, params: dict = None, msg_id: int = 1) -> dict:
        req = {
            "jsonrpc": "2.0",
            "id": msg_id,
            "method": method,
            "params": params or {},
        }
        resp_raw = self.server.handle_message(json.dumps(req))
        self.assertIsNotNone(resp_raw)
        resp = json.loads(resp_raw)
        self.assertEqual(resp.get("jsonrpc"), "2.0")
        self.assertEqual(resp.get("id"), msg_id)
        return resp

    def test_initialize_handshake(self):
        """Verify initialize returns expected protocol version, capabilities, and server info."""
        resp = self.send_request("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "1.0"},
        })
        self.assertNotIn("error", resp)
        result = resp["result"]
        self.assertEqual(result["protocolVersion"], "2024-11-05")
        self.assertIn("tools", result["capabilities"])
        self.assertIn("resources", result["capabilities"])
        self.assertIn("prompts", result["capabilities"])
        self.assertEqual(result["serverInfo"]["name"], "tasleemat-mcp")
        self.assertEqual(result["serverInfo"]["version"], tasleemat.__version__)

    def test_tools_list(self):
        """Verify all 6 standard tools are registered with schemas."""
        resp = self.send_request("tools/list")
        self.assertNotIn("error", resp)
        tools = resp["result"]["tools"]
        tool_names = [t["name"] for t in tools]

        expected_tools = [
            "tasleemat_list_artifacts",
            "tasleemat_get_artifact",
            "tasleemat_get_asset",
            "tasleemat_get_lexicon",
            "tasleemat_validate_data",
            "tasleemat_render_artifact",
        ]
        for et in expected_tools:
            self.assertIn(et, tool_names)

    def test_tool_list_artifacts(self):
        """Verify tasleemat_list_artifacts returns deliverables catalog."""
        resp = self.send_request("tools/call", {
            "name": "tasleemat_list_artifacts",
            "arguments": {"phase": "Initiating"},
        })
        self.assertNotIn("error", resp)
        content_text = resp["result"]["content"][0]["text"]
        data = json.loads(content_text)
        self.assertEqual(data["total_found"], 5)
        self.assertTrue(any(a["artifact_id"] == "PMO-03.01" for a in data["artifacts"]))

    def test_tool_get_artifact(self):
        """Verify tasleemat_get_artifact returns rich deliverable metadata."""
        resp = self.send_request("tools/call", {
            "name": "tasleemat_get_artifact",
            "arguments": {"artifact_id": "PMO-03.01"},
        })
        self.assertNotIn("error", resp)
        defn = json.loads(resp["result"]["content"][0]["text"])
        self.assertEqual(defn["artifact_id"], "PMO-03.01")
        self.assertEqual(defn["name_en"], "PROJECT CHARTER")
        self.assertEqual(defn["name_ar"], "ميثاق المشروع")
        self.assertEqual(len(defn["fingerprint"]), 64)

    def test_tool_get_asset_en_and_ar(self):
        """Verify tasleemat_get_asset returns templates in English and Arabic."""
        # English Template
        resp_en = self.send_request("tools/call", {
            "name": "tasleemat_get_asset",
            "arguments": {"artifact_id": "PMO-03.01", "role": "template", "lang": "en"},
        })
        self.assertNotIn("error", resp_en)
        tmpl_en = resp_en["result"]["content"][0]["text"]
        self.assertIn("PROJECT CHARTER", tmpl_en)

        # Arabic Template
        resp_ar = self.send_request("tools/call", {
            "name": "tasleemat_get_asset",
            "arguments": {"artifact_id": "PMO-03.01", "role": "template", "lang": "ar"},
        })
        self.assertNotIn("error", resp_ar)
        tmpl_ar = resp_ar["result"]["content"][0]["text"]
        self.assertIn("ميثاق المشروع", tmpl_ar)

    def test_tool_get_lexicon(self):
        """Verify tasleemat_get_lexicon returns filtered terminology."""
        resp = self.send_request("tools/call", {
            "name": "tasleemat_get_lexicon",
            "arguments": {"category": "Initiating", "query": "charter"},
        })
        self.assertNotIn("error", resp)
        data = json.loads(resp["result"]["content"][0]["text"])
        self.assertGreater(data["total_terms"], 0)
        self.assertTrue(any("CHARTER" in t.get("en_name", "").upper() for t in data["terms"]))

    def test_tool_validate_data_strict_and_draft(self):
        """Verify tasleemat_validate_data executes strict and draft validation."""
        # 1. Invalid payload in strict mode
        resp_strict = self.send_request("tools/call", {
            "name": "tasleemat_validate_data",
            "arguments": {
                "artifact_id": "PMO-03.01",
                "data": {"artifact_id": "PMO-03.01"},
                "mode": "strict",
            },
        })
        self.assertNotIn("error", resp_strict)
        rep_strict = json.loads(resp_strict["result"]["content"][0]["text"])
        self.assertFalse(rep_strict["valid"])
        self.assertGreater(rep_strict["errors_count"], 0)

        # 2. Draft payload in draft mode
        draft_payload = {
            "artifact_id": "PMO-03.01",
            "metadata": {
                "project_name": "AI Draft",
                "project_code": "PRJ-01",
                "date_prepared": "2026-03-01",
                "prepared_by": "Agent",
                "sponsor": "Director",
                "status": "draft",
            },
            "fields": {
                "project_purpose": "Scoping AI assistant workflows",
            },
        }
        resp_draft = self.send_request("tools/call", {
            "name": "tasleemat_validate_data",
            "arguments": {
                "artifact_id": "PMO-03.01",
                "data": draft_payload,
                "mode": "draft",
            },
        })
        self.assertNotIn("error", resp_draft)
        rep_draft = json.loads(resp_draft["result"]["content"][0]["text"])
        self.assertTrue(rep_draft["valid"])
        self.assertGreater(rep_draft["warnings_count"], 0)

        # 3. Unsupported deliverable validation via MCP (simulated missing schema)
        with patch("tasleemat.validation._load_schema", side_effect=KeyError("Schema unavailable")):
            resp_unavail = self.send_request("tools/call", {
                "name": "tasleemat_validate_data",
                "arguments": {
                    "artifact_id": "PMO-00.01",
                    "data": {"artifact_id": "PMO-00.01"},
                },
            })
            self.assertNotIn("error", resp_unavail)
            rep_unavail = json.loads(resp_unavail["result"]["content"][0]["text"])
            self.assertFalse(rep_unavail["valid"])
            self.assertEqual(rep_unavail["status"], "unavailable")
            self.assertFalse(rep_unavail["is_available"])
            self.assertTrue(any(e["code"] == "SCHEMA_UNAVAILABLE" for e in rep_unavail["errors"]))

        # 4. Unknown artifact ID validation via MCP
        resp_unknown = self.send_request("tools/call", {
            "name": "tasleemat_validate_data",
            "arguments": {
                "artifact_id": "UNKNOWN-99.99",
                "data": {"artifact_id": "UNKNOWN-99.99"},
            },
        })
        self.assertNotIn("error", resp_unknown)
        rep_unknown = json.loads(resp_unknown["result"]["content"][0]["text"])
        self.assertFalse(rep_unknown["valid"])
        self.assertEqual(rep_unknown["status"], "unknown_artifact")
        self.assertFalse(rep_unknown["is_available"])
        self.assertTrue(any(e["code"] == "UNKNOWN_ARTIFACT" for e in rep_unknown["errors"]))

    def test_tool_render_artifact(self):
        """Verify tasleemat_render_artifact renders HTML."""
        resp = self.send_request("tools/call", {
            "name": "tasleemat_render_artifact",
            "arguments": {"artifact_id": "PMO-03.01", "lang": "en"},
        })
        self.assertNotIn("error", resp)
        html = resp["result"]["content"][0]["text"]
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("PROJECT CHARTER", html)

    def test_resources_list_and_read(self):
        """Verify resources/list and resources/read."""
        # List
        resp_list = self.send_request("resources/list")
        self.assertNotIn("error", resp_list)
        uris = [r["uri"] for r in resp_list["result"]["resources"]]
        self.assertIn("pmo://catalog", uris)
        self.assertIn("pmo://lexicon", uris)

        # Read Catalog
        resp_read = self.send_request("resources/read", {"uri": "pmo://catalog"})
        self.assertNotIn("error", resp_read)
        cat_json = resp_read["result"]["contents"][0]["text"]
        cat_data = json.loads(cat_json)
        self.assertEqual(len(cat_data), 114)

    def test_prompts_list_and_get(self):
        """Verify prompts/list and prompts/get."""
        resp_list = self.send_request("prompts/list")
        self.assertNotIn("error", resp_list)
        prompt_names = [p["name"] for p in resp_list["result"]["prompts"]]
        self.assertIn("draft_project_charter", prompt_names)

        # Get prompt
        resp_get = self.send_request("prompts/get", {
            "name": "draft_project_charter",
            "arguments": {"project_notes": "Project: Smart City Riyadh"},
        })
        self.assertNotIn("error", resp_get)
        msg_text = resp_get["result"]["messages"][0]["content"]["text"]
        self.assertIn("Smart City Riyadh", msg_text)
        self.assertIn("Project Charter", msg_text)

    def test_mcp_definition_version_forwarding_and_traceability(self):
        """Verify MCP tasleemat_validate_data exposes definition_version and returns complete canonical traceability."""
        from tasleemat.catalog import get_artifact_definition

        defn = get_artifact_definition("PMO-03.01")
        real_fp = defn["fingerprint"]
        schema_fp = defn["completed_data_validation"]["schema_fingerprint"]
        schema_id = defn["completed_data_validation"]["schema_id"]

        valid_payload = {
            "artifact_id": "PMO-03.01",
            "metadata": {
                "project_name": "MCP Project",
                "project_code": "PRJ-MCP",
                "date_prepared": "2026-03-15",
                "prepared_by": "MCP Author",
                "sponsor": "Sponsor",
                "status": "approved",
            },
            "fields": {
                "project_purpose": "Testing MCP definition version parameter.",
                "high_level_project_description": "Valid description.",
                "key_deliverables": ["Deliv 1"],
                "project_objectives_and_related_success_criteria": [
                    {"objective": "Obj 1", "success_criteria": "Crit 1"}
                ],
                "summary_milestone_schedule": [
                    {"milestone": "M1", "target_date": "2026-06-01"}
                ],
            },
        }

        # 1. Exact supported definition fingerprint
        resp_fp = self.send_request("tools/call", {
            "name": "tasleemat_validate_data",
            "arguments": {
                "artifact_id": "PMO-03.01",
                "data": valid_payload,
                "definition_version": real_fp,
            },
        })
        rep_fp = json.loads(resp_fp["result"]["content"][0]["text"])
        self.assertTrue(rep_fp["valid"])
        self.assertEqual(rep_fp["definition_fingerprint"], real_fp)
        self.assertEqual(rep_fp["schema_fingerprint"], schema_fp)
        self.assertEqual(rep_fp["schema_id"], schema_id)
        self.assertEqual(rep_fp["schema_dialect"], "https://json-schema.org/draft/2020-12/schema")
        self.assertEqual(rep_fp["mode"], "strict")

        # 2. Exact supported schema fingerprint
        resp_sfp = self.send_request("tools/call", {
            "name": "tasleemat_validate_data",
            "arguments": {
                "artifact_id": "PMO-03.01",
                "data": valid_payload,
                "definition_version": schema_fp,
            },
        })
        rep_sfp = json.loads(resp_sfp["result"]["content"][0]["text"])
        self.assertTrue(rep_sfp["valid"])

        # 3. Retained current-installed alias ('2.5.0' and 'v2.5.0')
        resp_alias = self.send_request("tools/call", {
            "name": "tasleemat_validate_data",
            "arguments": {
                "artifact_id": "PMO-03.01",
                "data": valid_payload,
                "definition_version": "2.5.0",
            },
        })
        rep_alias = json.loads(resp_alias["result"]["content"][0]["text"])
        self.assertTrue(rep_alias["valid"])

        # 4. Mismatched / unsupported version rejected
        resp_bad = self.send_request("tools/call", {
            "name": "tasleemat_validate_data",
            "arguments": {
                "artifact_id": "PMO-03.01",
                "data": valid_payload,
                "definition_version": "3.0.0-unsupported",
            },
        })
        rep_bad = json.loads(resp_bad["result"]["content"][0]["text"])
        self.assertFalse(rep_bad["valid"])
        self.assertTrue(any(e["code"] == "UNSUPPORTED_VERSION" for e in rep_bad["errors"]))

        # 5. Schema dialect URI rejected per contract
        resp_dialect = self.send_request("tools/call", {
            "name": "tasleemat_validate_data",
            "arguments": {
                "artifact_id": "PMO-03.01",
                "data": valid_payload,
                "definition_version": "https://json-schema.org/draft/2020-12/schema",
            },
        })
        rep_dialect = json.loads(resp_dialect["result"]["content"][0]["text"])
        self.assertFalse(rep_dialect["valid"])
        self.assertTrue(any(e["code"] == "UNSUPPORTED_VERSION" for e in rep_dialect["errors"]))

    def test_mcp_protocol_robustness_and_malformed_inputs(self):
        """Verify server robustly handles invalid JSON, scalars, arrays, bad jsonrpc versions, and falsey IDs."""
        # 1. Invalid JSON string
        raw_parse_err = self.server.handle_message("{invalid json")
        self.assertIsNotNone(raw_parse_err)
        resp_p = json.loads(raw_parse_err)
        self.assertEqual(resp_p["error"]["code"], -32700)
        self.assertIsNone(resp_p["id"])

        # 2. JSON scalar (number, string, bool)
        raw_scalar = self.server.handle_message("12345")
        resp_s = json.loads(raw_scalar)
        self.assertEqual(resp_s["error"]["code"], -32600)

        # 3. JSON array (batch input)
        raw_batch = self.server.handle_message('[{"jsonrpc": "2.0"}]')
        resp_b = json.loads(raw_batch)
        self.assertEqual(resp_b["error"]["code"], -32600)

        # 4. Invalid jsonrpc version field
        raw_bad_ver = self.server.handle_message(json.dumps({
            "jsonrpc": "1.0",
            "id": 10,
            "method": "ping",
        }))
        resp_bv = json.loads(raw_bad_ver)
        self.assertEqual(resp_bv["error"]["code"], -32600)
        self.assertEqual(resp_bv["id"], 10)

        # 5. Missing or invalid method type
        raw_no_method = self.server.handle_message(json.dumps({
            "jsonrpc": "2.0",
            "id": 11,
            "method": 123,
        }))
        resp_nm = json.loads(raw_no_method)
        self.assertEqual(resp_nm["error"]["code"], -32600)

        # 6. Invalid params type
        raw_bad_params = self.server.handle_message(json.dumps({
            "jsonrpc": "2.0",
            "id": 12,
            "method": "ping",
            "params": "not-an-object",
        }))
        resp_bp = json.loads(raw_bad_params)
        self.assertEqual(resp_bp["error"]["code"], -32600)

        # 7. Valid falsey ID (id = 0)
        raw_zero_id = self.server.handle_message(json.dumps({
            "jsonrpc": "2.0",
            "id": 0,
            "method": "ping",
        }))
        resp_zero = json.loads(raw_zero_id)
        self.assertEqual(resp_zero["id"], 0)
        self.assertEqual(resp_zero["result"], {})

        # 8. Unhandled notification drops silently
        raw_notif = self.server.handle_message(json.dumps({
            "jsonrpc": "2.0",
            "method": "custom/unhandled_notification",
        }))
        self.assertIsNone(raw_notif)


if __name__ == "__main__":
    unittest.main()
