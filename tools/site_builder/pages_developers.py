"""tools/site_builder/pages_developers.py
Comprehensive Developers, Engineering & AI Integration Guide for Tasleemat (English & Arabic).
Covers:
- Quick installation & environment prerequisites (PyPI, Python 3.9-3.13)
- CLI Command Reference (`init`, `list`, `search`, `config`, `generate`, `mcp`, `test`, `help`)
- Python SDK Core Architecture (All 8 verified functions, data models, exception handling)
- Model Context Protocol (MCP) Server (JSON-RPC 2.0 stdio, Claude Desktop, Cursor, OpenCode, Antigravity)
- Draft 2020-12 Companion Schemas & RFC Formats (RFC 3339, RFC 4122, RFC 3986, RFC 5322, strict/draft modes)
- Autonomous Agent Self-Correction Feedback Loop (Autonomous LLM healing)
- Multi-Agent Orchestration Swarm Architecture (CrewAI / LangGraph PMO personas)
- Programmatic LLM Document Synthesis (`tasleemat.ai.AIClient`, providers, prompt assembly)
- Headless CI/CD Automation & Quality Gates (GitHub Actions, GitLab CI, pre-commit)
- Attested Computations & Deterministic Math Contracts (PMO-06.05 Earned Value Analysis)
"""

from tools.site_builder.theme import render_html_page


def generate_developers_en(base_url: str = "/Tasleemat") -> str:
    content = f"""
    <section class="hero-section" style="padding: 3.5rem 0 2.5rem;">
      <div class="container">
        <div class="hero-pill">
          <span>⚙️ Enterprise Engineering &amp; AI Automation Manual</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.35rem; margin-top: 0.75rem;">Developers &amp; AI Integration Reference</h1>
        <p class="hero-subtitle" style="max-width: 820px; margin: 0 auto; line-height: 1.7;">
          The authoritative technical manual for software engineers, AI system architects, and DevOps leads.
          Integrate Tasleemat across Python applications, terminal automation pipelines, Model Context Protocol (MCP) servers,
          and autonomous multi-agent orchestration swarms.
        </p>
      </div>
    </section>

    <div class="container" style="margin-top: 2.5rem; margin-bottom: 5rem;">
      <div style="display: flex; gap: 2.5rem; flex-wrap: wrap;">
        
        <!-- Sticky Sidebar Navigation -->
        <aside style="width: 260px; flex-shrink: 0;">
          <div style="position: sticky; top: 5.5rem; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 0.75rem; padding: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            <div style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); margin-bottom: 0.85rem;">Table of Contents</div>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.45rem; font-size: 0.86rem; padding: 0; margin: 0;">
              <li><a href="#quickstart" style="color: var(--text-main); text-decoration: none; font-weight: 500;">1. Quick Installation</a></li>
              <li><a href="#cli" style="color: var(--text-main); text-decoration: none; font-weight: 500;">2. CLI Command Reference</a></li>
              <li><a href="#sdk" style="color: var(--text-main); text-decoration: none; font-weight: 500;">3. Python SDK Architecture</a></li>
              <li><a href="#mcp" style="color: var(--text-main); text-decoration: none; font-weight: 500;">4. Model Context Protocol (MCP)</a></li>
              <li><a href="#schemas" style="color: var(--text-main); text-decoration: none; font-weight: 500;">5. Schemas &amp; RFC Formats</a></li>
              <li><a href="#self-correction" style="color: var(--text-main); text-decoration: none; font-weight: 500;">6. Agent Self-Correction Loop</a></li>
              <li><a href="#multi-agent" style="color: var(--text-main); text-decoration: none; font-weight: 500;">7. Multi-Agent PMO Swarms</a></li>
              <li><a href="#llm-client" style="color: var(--text-main); text-decoration: none; font-weight: 500;">8. AI Synthesis &amp; Prompting</a></li>
              <li><a href="#cicd" style="color: var(--text-main); text-decoration: none; font-weight: 500;">9. CI/CD &amp; DevOps Pipelines</a></li>
              <li><a href="#attested-math" style="color: var(--text-main); text-decoration: none; font-weight: 500;">10. Attested Math Contracts</a></li>
            </ul>
          </div>
        </aside>

        <!-- Main Technical Content -->
        <div style="flex: 1; min-width: 320px; display: flex; flex-direction: column; gap: 3rem;">
          
          <!-- Section 1: Quick Installation -->
          <section id="quickstart" class="card" style="padding: 2.25rem;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
              <h2 style="font-size: 1.55rem; margin: 0;">1. Installation &amp; Environment Prerequisites</h2>
              <span class="badge" style="background: var(--accent-blue-bg); color: var(--accent-blue); border: 1px solid var(--accent-blue-border); font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">PyPI: tasleemat</span>
            </div>
            <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
              Tasleemat is distributed as a zero-dependency, pure-Python package on PyPI, supporting Python <strong>3.9, 3.10, 3.11, 3.12, and 3.13</strong>. 
              The core distribution packages all 114 bilingual deliverable templates, JSON companion schemas, CSV data dictionaries, 
              CLI commands, and the Model Context Protocol (MCP) server.
            </p>
            <pre><code># Install from PyPI
pip install tasleemat

# Or install within isolated virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install tasleemat</code></pre>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 1rem; margin-bottom: 0.5rem;">
              Verify that both the core CLI tool and the standalone MCP executable are registered on your <code>PATH</code>:
            </p>
            <pre><code>tasleemat --version
tasleemat-mcp --help</code></pre>
          </section>

          <!-- Section 2: CLI Command Reference -->
          <section id="cli" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">2. Complete CLI Command Reference</h2>
            <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.5rem;">
              The <code>tasleemat</code> command-line executable provides first-class scaffolding, catalog inspection, 
              LLM generation, automated test execution, and MCP runtime support.
            </p>
            
            <h3 style="font-size: 1.2rem; margin-top: 1.5rem; margin-bottom: 0.5rem; color: var(--text-main);">A. Project Workspace Scaffolding (<code>tasleemat init</code>)</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 0.75rem;">
              Generates a tailored project directory pre-populated with required 5-file deliverable bundles according to governance sizing tier and methodology pack:
            </p>
            <pre><code># Interactive wizard mode (prompts for project code, name, PM, sponsor)
tasleemat init

# Non-interactive headless mode: Tier 2 (Standard Enterprise) with Agile Pack in Arabic
tasleemat init \
  --tier 2 \
  --pack agile \
  --lang ar \
  --code "PRJ-2026-CLOUD-01" \
  --name "منصة التحول الرقمي السحابي" \
  --pm "سارة الأحمد" \
  --sponsor "د. خالد المنصور" \
  --out ./workspaces/PRJ-2026-CLOUD-01

# Enterprise Tier 1 Project in both English and Arabic
tasleemat init \
  --tier 1 \
  --pack hybrid \
  --lang both \
  --code "PRJ-2026-CORE" \
  --name "Enterprise Core Banking Migration" \
  --pm "Tariq Al-Harbi" \
  --sponsor "Executive VP IT" \
  --out ./enterprise_workspace</code></pre>

            <h3 style="font-size: 1.2rem; margin-top: 2rem; margin-bottom: 0.5rem; color: var(--text-main);">B. Catalog Exploration &amp; Search (<code>tasleemat list</code> &amp; <code>search</code>)</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 0.75rem;">
              Inspect the 114 deliverables or search across English and Arabic artifact titles:
            </p>
            <pre><code># List all forms in English or Arabic
tasleemat list --lang en
tasleemat list --lang ar

# Search by keyword or deliverable code
tasleemat search "Risk" --lang en
tasleemat search "ميثاق" --lang ar
tasleemat search "PMO-03.01" --lang en</code></pre>

            <h3 style="font-size: 1.2rem; margin-top: 2rem; margin-bottom: 0.5rem; color: var(--text-main);">C. LLM AI Account Configuration (<code>tasleemat config</code>)</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 0.75rem;">
              Securely store credentials in <code>~/.tasleemat/config.json</code> without environment variable collision:
            </p>
            <pre><code># Configure Google Gemini
tasleemat config set --provider gemini --model gemini-2.5-flash --key "AIzaSy..."

# Configure OpenAI or Anthropic
tasleemat config set --provider openai --model gpt-4o --key "sk-proj-..."
tasleemat config set --provider anthropic --model claude-3-5-sonnet-20241022 --key "sk-ant-..."

# Configure local Ollama endpoint
tasleemat config set --provider ollama --model llama3.2 --endpoint "http://localhost:11434"

# Display active configuration (hides secret keys)
tasleemat config show</code></pre>

            <h3 style="font-size: 1.2rem; margin-top: 2rem; margin-bottom: 0.5rem; color: var(--text-main);">D. Automated AI Document Generation (<code>tasleemat generate</code>)</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 0.75rem;">
              Draft formal deliverables from unstructured kickoff notes using configured AI providers:
            </p>
            <pre><code># Generate Project Charter (PMO-03.01) from raw text notes
tasleemat generate \
  --form PMO-03.01 \
  --notes ./meeting_minutes.txt \
  --lang en \
  --out ./drafts/Project_Charter.md

# Offline mock mode for continuous integration (zero API token cost)
tasleemat generate \
  --form PMO-03.01 \
  --notes "Mock project notes" \
  --mock \
  --out ./ci_output/Mock_Charter.md</code></pre>

            <h3 style="font-size: 1.2rem; margin-top: 2rem; margin-bottom: 0.5rem; color: var(--text-main);">E. Automated Test Suite (<code>tasleemat test</code>)</h3>
            <pre><code># Run complete internal test suite (140+ unit and integration tests)
tasleemat test -v</code></pre>
          </section>

          <!-- Section 3: Python SDK Architecture -->
          <section id="sdk" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">3. Python SDK Architecture &amp; API Reference</h2>
            <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.5rem;">
              The <code>tasleemat</code> library exports 8 pure-Python functions for catalog discovery, asset loading, 
              tailoring resolution, RFC format validation, and offline document rendering.
            </p>

            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Function</th>
                    <th>Parameters</th>
                    <th>Return Type</th>
                    <th>Description</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>list_artifacts()</code></td>
                    <td><code>phase=None, tier=None, pack=None</code></td>
                    <td><code>List[ArtifactSummary]</code></td>
                    <td>Discovers summary objects for all 114 deliverables or tailored subset with SHA-256 fingerprints.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_definition()</code></td>
                    <td><code>artifact_id: str</code></td>
                    <td><code>dict</code></td>
                    <td>Retrieves canonical metadata dictionary including phase codes, tier mappings, and asset file paths.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_assets()</code></td>
                    <td><code>artifact_id: str, lang='en'</code></td>
                    <td><code>ArtifactAssets</code></td>
                    <td>Object containing safe file path resolvers and convenience content accessors.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_asset()</code></td>
                    <td><code>artifact_id: str, role: str, lang='en'</code></td>
                    <td><code>Union[str, dict, list]</code></td>
                    <td>Fetches parsed content directly by role: <code>template</code>, <code>guide</code>, <code>prompt</code>, <code>schema</code>, <code>dictionary</code>, <code>example</code>.</td>
                  </tr>
                  <tr>
                    <td><code>get_tailoring_profile()</code></td>
                    <td><code>tier: str, pack: str='general'</code></td>
                    <td><code>List[str]</code></td>
                    <td>Returns the list of mandatory deliverable codes matching governance tier (1, 2, 3) and methodology pack.</td>
                  </tr>
                  <tr>
                    <td><code>get_lexicon()</code></td>
                    <td><code>category: Optional[str]=None</code></td>
                    <td><code>List[dict]</code></td>
                    <td>Returns bilingual PMI PMBOK® and Saudi DGA project management terminology mappings.</td>
                  </tr>
                  <tr>
                    <td><code>validate_artifact_data()</code></td>
                    <td><code>artifact_id: str, data: dict, mode='strict'</code></td>
                    <td><code>ValidationReport</code></td>
                    <td>Validates structured payload against Draft 2020-12 companion schema with strict RFC format checking.</td>
                  </tr>
                  <tr>
                    <td><code>render_artifact()</code></td>
                    <td><code>artifact_id: str, lang='en', data=None, out_path=None</code></td>
                    <td><code>str</code></td>
                    <td>Compiles deliverable template and data dictionary into styled, print-ready HTML with Arabic RTL support.</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="font-size: 1.2rem; margin-top: 2rem; margin-bottom: 0.5rem; color: var(--text-main);">Comprehensive Python SDK Example</h3>
            <pre><code>import tasleemat

# 1. Resolve tailored deliverable bundle for a Tier 2 Agile Project
required_ids = tasleemat.get_tailoring_profile(tier="2", pack="agile")
print(f"Mandatory deliverables count: {{len(required_ids)}}")

# 2. Extract bilingual prompt instructions for Project Charter (PMO-03.01)
prompt_en = tasleemat.get_artifact_asset("PMO-03.01", role="prompt", lang="en")
prompt_ar = tasleemat.get_artifact_asset("PMO-03.01", role="prompt", lang="ar")

# 3. Inspect companion JSON Schema
schema_def = tasleemat.get_artifact_asset("PMO-03.01", role="schema", lang="en")
print(f"Root schema ID: {{schema_def.get('$id')}}")

# 4. Programmatic Data Validation (Strict Mode)
charter_payload = {{
    "project_code": "PRJ-2026-CLOUD",
    "project_name": "Unified Cloud Transformation",
    "start_date": "2026-11-01",              # Valid RFC 3339 full-date
    "sponsor_name": "Dr. Khalid Al-Mansour",
    "estimated_budget": 3500000.00
}}

report = tasleemat.validate_artifact_data("PMO-03.01", charter_payload, mode="strict")
if report.valid:
    print(f"✅ Schema valid! Fingerprint: {{report.fingerprint}}")
else:
    print(f"❌ Validation failed with {{len(report.errors)}} error(s):")
    for err in report.errors:
        print(f"   • {{err.field_path}}: {{err.message}} (Code: {{err.code}})")

# 5. Render to styled print-ready HTML
html_output = tasleemat.render_artifact(
    artifact_id="PMO-03.01",
    lang="ar",
    data={{"Project_Name": "مشروع التحول السحابي", "Project_Code": "PRJ-2026-CLOUD"}},
    out_path="./exports/charter_rendered.html"
)</code></pre>
          </section>

          <!-- Section 4: Model Context Protocol (MCP) -->
          <section id="mcp" class="card" style="padding: 2.25rem;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
              <h2 style="font-size: 1.55rem; margin: 0;">4. Model Context Protocol (MCP) Integration</h2>
              <span class="badge" style="background: var(--accent-emerald-bg); color: var(--accent-emerald); border: 1px solid var(--accent-emerald-border); font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">Stdio JSON-RPC 2.0</span>
            </div>
            <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
              Tasleemat includes an official zero-dependency Model Context Protocol (MCP) server conforming to protocol version 
              <code>2024-11-05</code>. It exposes 6 specialized tools that allow AI assistants (Claude Desktop, Cursor, OpenCode, Antigravity) 
              to discover deliverables, retrieve prompts and templates, query bilingual terminology, validate structured payloads, and render HTML.
            </p>

            <h3 style="font-size: 1.15rem; margin-top: 1rem; margin-bottom: 0.5rem;">Client Configuration Setup</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 0.75rem;">
              Add the Tasleemat server block to your client configuration file:
            </p>
            <ul style="margin-left: 1.5rem; color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1rem;">
              <li><strong>Claude Desktop:</strong> <code>~/.config/Claude/claude_desktop_config.json</code> (Linux) or <code>~/Library/Application Support/Claude/claude_desktop_config.json</code> (macOS)</li>
              <li><strong>Cursor IDE:</strong> <code>.cursor/mcp.json</code> or Settings &rarr; Features &rarr; MCP</li>
              <li><strong>OpenCode / Antigravity:</strong> Stdio process command <code>tasleemat mcp</code> or <code>tasleemat-mcp</code></li>
            </ul>

            <pre><code>// claude_desktop_config.json or .cursor/mcp.json
{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat",
      "args": ["mcp"]
    }}
  }}
}}</code></pre>

            <h3 style="font-size: 1.2rem; margin-top: 1.75rem; margin-bottom: 0.75rem; color: var(--text-main);">The 6 Core MCP Tools</h3>
            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>MCP Tool Name</th>
                    <th>Parameters</th>
                    <th>Autonomous Agent Purpose</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>tasleemat_list_artifacts</code></td>
                    <td><code>phase?: string, tier?: string</code></td>
                    <td>Allows the agent to dynamically inspect required deliverables across the 8 project phases.</td>
                  </tr>
                  <tr>
                    <td><code>tasleemat_get_artifact</code></td>
                    <td><code>artifact_id: string</code></td>
                    <td>Returns canonical deliverable metadata, English/Arabic names, and authoritative SHA-256 fingerprints.</td>
                  </tr>
                  <tr>
                    <td><code>tasleemat_get_asset</code></td>
                    <td><code>artifact_id: string, role: string, lang?: "en"|"ar"</code></td>
                    <td>Retrieves raw text for <code>template</code>, <code>guide</code>, <code>prompt</code>, <code>schema</code>, <code>dictionary</code>, or <code>example</code>.</td>
                  </tr>
                  <tr>
                    <td><code>tasleemat_get_lexicon</code></td>
                    <td><code>category?: string, query?: string</code></td>
                    <td>Prevents semantic translation drift by returning verified PMI PMBOK® and Saudi DGA terminology.</td>
                  </tr>
                  <tr>
                    <td><code>tasleemat_validate_data</code></td>
                    <td><code>artifact_id: string, data: object, mode?: "strict"|"draft"</code></td>
                    <td>Validates structured payload against Draft 2020-12 schema; returns machine-parseable error lists on failure.</td>
                  </tr>
                  <tr>
                    <td><code>tasleemat_render_artifact</code></td>
                    <td><code>artifact_id: string, lang?: "en"|"ar", data?: object</code></td>
                    <td>Renders the validated deliverable to standalone HTML for human gatekeeper review and executive sign-off.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </section>

          <!-- Section 5: Schemas & RFC Formats -->
          <section id="schemas" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">5. Draft 2020-12 Schemas &amp; Strict RFC Format Validation</h2>
            <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
              Every one of the 114 deliverables in Tasleemat is paired with a companion JSON Schema conforming to the 
              <strong>JSON Schema Draft 2020-12</strong> specification. Per Draft 2020-12, format annotations are optional by default; 
              however, Tasleemat’s pure-Python validation engine explicitly operates in <strong>assertion mode</strong> to guarantee semantic data contracts.
            </p>

            <h3 style="font-size: 1.15rem; margin-top: 1rem; margin-bottom: 0.5rem;">Registered RFC Format Handlers</h3>
            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Format Keyword</th>
                    <th>Standard Specification</th>
                    <th>Validation Rules &amp; Edge Cases Handled</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>date</code></td>
                    <td>RFC 3339 full-date</td>
                    <td>Strict <code>YYYY-MM-DD</code>. Validates calendar boundaries (rejects Feb 29 on non-leap years, invalid months, unpadded days).</td>
                  </tr>
                  <tr>
                    <td><code>date-time</code></td>
                    <td>RFC 3339 date-time</td>
                    <td>Requires date, <code>T</code> separator, time, and timezone offset (<code>Z</code> or <code>+/-HH:MM</code>). Supports leap second 60.</td>
                  </tr>
                  <tr>
                    <td><code>time</code></td>
                    <td>RFC 3339 partial-time</td>
                    <td><code>HH:MM:SS[.fractional][Z|offset]</code> syntax check.</td>
                  </tr>
                  <tr>
                    <td><code>uuid</code></td>
                    <td>RFC 4122 UUID</td>
                    <td>Exact 8-4-4-4-12 hex representation (36 chars). Bare UUIDs only; URN schemes belong under <code>uri</code>.</td>
                  </tr>
                  <tr>
                    <td><code>uri</code></td>
                    <td>RFC 3986 URI</td>
                    <td>Absolute URI requiring scheme (e.g. <code>https://</code>). Disallows raw whitespace or unescaped characters.</td>
                  </tr>
                  <tr>
                    <td><code>uri-reference</code></td>
                    <td>RFC 3986 URI Reference</td>
                    <td>Allows either absolute URI or valid relative reference without whitespace.</td>
                  </tr>
                  <tr>
                    <td><code>email</code></td>
                    <td>RFC 5322 addr-spec</td>
                    <td>Standard <code>local-part@domain</code>. Max length 254 octets. Rejects whitespace and invalid domain labels.</td>
                  </tr>
                  <tr>
                    <td><code>duration</code></td>
                    <td>ISO 8601 / RFC 3339</td>
                    <td>Duration strings (e.g. <code>P1Y2M</code>, <code>PT15M</code>, <code>P4W</code>). Rejects bare <code>P</code> or <code>PT</code> and prose.</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Strict Mode vs. Draft Mode</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-top: 0.75rem;">
              <div style="background: var(--bg-card-hover); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
                <h4 style="margin-top: 0; color: var(--accent-blue); font-size: 1rem;">🔒 Strict Mode (Stage-Gate Enforcement)</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 0;">
                  Enforces all mandatory keys (<code>required</code>), type safety, numerical bounds, regex patterns, and RFC formats. 
                  Returns <code>valid=False</code> on any discrepancy. Used at formal stage-gate approvals and CI/CD quality gates.
                </p>
              </div>
              <div style="background: var(--bg-card-hover); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
                <h4 style="margin-top: 0; color: var(--accent-emerald); font-size: 1rem;">📝 Draft Mode (Agent Work-in-Progress)</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 0;">
                  Permits incomplete payloads and missing required fields while surfacing non-blocking warnings. 
                  Allows AI agents to draft preliminary sections incrementally across conversational turns before final packaging.
                </p>
              </div>
            </div>
          </section>

          <!-- Section 6: Agent Self-Correction Loop -->
          <section id="self-correction" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">6. The Autonomous Agent Self-Correction Loop</h2>
            <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
              When LLM agents generate structured deliverables, subtle syntax discrepancies (such as dates formatted as <code>MM/DD/YYYY</code>, 
              boolean fields written as strings <code>"true"</code>, or negative budget figures) are common.
              Tasleemat's deterministic validation engine acts as a <strong>surgical compiler error reporter</strong>, enabling autonomous self-healing.
            </p>

            <div class="mermaid">
flowchart TD
    RAW["Raw Project Context & Notes"] --> LLM["LLM Agent (Gemini / Claude / GPT)"]
    LLM --> JSON["Draft JSON Payload"]
    JSON --> VALIDATE{{"tasleemat.validate_artifact_data(strict=True)"}}
    
    VALIDATE -->|valid == True| RENDER["tasleemat.render_artifact()"]
    RENDER --> HUMAN["Human Gatekeeper Approval"]
    
    VALIDATE -->|valid == False| SURGICAL["Extract Structured Error List:<br/>- field_path: start_date<br/>- code: FORMAT_VIOLATION<br/>- rule: RFC 3339 (YYYY-MM-DD)"]
    SURGICAL --> REPROMPT["Automated Re-Prompt Feedback Context"]
    REPROMPT --> LLM
            </div>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Self-Correction Python Implementation</h3>
            <pre><code>import tasleemat
from tasleemat.ai import AIClient

def generate_and_heal_deliverable(artifact_id: str, raw_notes: str, max_attempts: int = 3) -> dict:
    client = AIClient(provider="gemini", model="gemini-2.5-flash")
    schema_def = tasleemat.get_artifact_asset(artifact_id, role="schema", lang="en")
    prompt_instructions = tasleemat.get_artifact_asset(artifact_id, role="prompt", lang="en")
    
    system_prompt = (
        f"You are an AI PMO Engineer. Generate a valid JSON object matching the JSON Schema Draft 2020-12.\\n"
        f"Schema ID: {{schema_def.get('$id')}}\\n"
        f"Strict RFC formatting is enforced: dates must be YYYY-MM-DD, numbers must be non-negative."
    )
    
    current_prompt = f"{{prompt_instructions}}\\n\\nPROJECT NOTES:\\n{{raw_notes}}"
    
    for attempt in range(1, max_attempts + 1):
        raw_response = client.generate(prompt=current_prompt, system_instruction=system_prompt)
        # Parse generated JSON
        payload = extract_json_block(raw_response)
        
        # Execute pure-Python schema verification
        report = tasleemat.validate_artifact_data(artifact_id, payload, mode="strict")
        if report.valid:
            print(f"✅ Deliverable {{artifact_id}} successfully validated on attempt {{attempt}}!")
            return payload
            
        print(f"⚠️ Attempt {{attempt}} failed schema checks. Assembling surgical feedback...")
        error_context = "\\n".join([f"- Field '{{e.field_path}}': {{e.message}} (Rule: {{e.schema_rule}})" for e in report.errors])
        
        # In-context surgical re-prompting
        current_prompt = (
            f"Your previous JSON output contained schema validation errors:\\n{{error_context}}\\n\\n"
            f"Fix ONLY these fields and return the updated valid JSON object without commentary."
        )
        
    raise RuntimeError(f"Deliverable {{artifact_id}} could not be validated after {{max_attempts}} attempts.")</code></pre>
          </section>

          <!-- Section 7: Multi-Agent PMO Swarms -->
          <section id="multi-agent" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">7. Multi-Agent PMO Swarm Architecture</h2>
            <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
              In enterprise ecosystems utilizing <strong>CrewAI</strong>, <strong>LangGraph</strong>, <strong>AutoGen</strong>, or <strong>OpenAI Swarm</strong>, 
              PMO responsibilities are distributed among specialized personas rather than handled by a single monolithic prompt.
            </p>

            <div class="mermaid">
flowchart LR
    SPONSOR["Project Sponsor / PM"] --> ORCH["<b>PMO Orchestrator Agent</b><br/>Resolves Tailoring & Sequences DAG"]
    
    subgraph Swarm["Specialized PMO Agent Swarm"]
        ORCH --> BA["<b>Business Analyst</b><br/>PMO-01.01 Business Case<br/>PMO-03.01 Project Charter"]
        ORCH --> SCHED["<b>Schedule Engineer</b><br/>PMO-04.02.06 WBS<br/>PMO-04.03.08 Project Schedule"]
        ORCH --> RISK["<b>Risk Specialist</b><br/>PMO-04.08.02 Risk Register<br/>PMO-04.08.04 Probability Matrix"]
    end
    
    BA --> AUDIT["<b>Gatekeeper QA Agent</b><br/>tasleemat_validate_data"]
    SCHED --> AUDIT
    RISK --> AUDIT
    
    AUDIT -->|Pass| HTML["<b>Offline Renderer</b><br/>tasleemat_render_artifact"]
    HTML --> HUMAN["Human Stage-Gate Sign-off"]
            </div>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Recommended Agent Persona Blueprints</h3>
            <div style="display: flex; flex-direction: column; gap: 1rem; margin-top: 0.75rem;">
              <div style="background: var(--bg-card-hover); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
                <h4 style="margin: 0 0 0.5rem 0; font-size: 1.05rem; color: var(--accent-blue);">1. PMO Lead Orchestrator (Virtual PMO Director)</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 0.5rem;">
                  <strong>Responsibility:</strong> Invokes <code>get_tailoring_profile(tier, pack)</code> to establish the governance deliverable baseline. 
                  Enforces the Directed Acyclic Graph (DAG) dependencies (e.g., ensuring PMO-03.01 Charter is approved before PMO-04.02.06 WBS is drafted).
                </p>
                <code style="font-size: 0.82rem;">Tool Access: tasleemat_list_artifacts, tasleemat_get_artifact, get_tailoring_profile</code>
              </div>

              <div style="background: var(--bg-card-hover); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
                <h4 style="margin: 0 0 0.5rem 0; font-size: 1.05rem; color: var(--accent-blue);">2. Authoring Agents (Business Analyst, Schedule Engineer, Risk Specialist)</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 0.5rem;">
                  <strong>Responsibility:</strong> Synthesizes specific deliverable sections using <code>get_artifact_asset(role="prompt")</code> and 
                  references the 228 verified real-world examples in <code>examples/en/</code> and <code>examples/ar/</code>.
                </p>
                <code style="font-size: 0.82rem;">Tool Access: tasleemat_get_asset, tasleemat_get_lexicon</code>
              </div>

              <div style="background: var(--bg-card-hover); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
                <h4 style="margin: 0 0 0.5rem 0; font-size: 1.05rem; color: var(--accent-blue);">3. Gatekeeper QA Agent (Audit &amp; Compliance Lead)</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 0.5rem;">
                  <strong>Responsibility:</strong> Executes <code>validate_artifact_data(mode="strict")</code> on all completed JSON artifacts. 
                  Blocks progression to subsequent lifecycle phases if any required fields or RFC constraints fail.
                </p>
                <code style="font-size: 0.82rem;">Tool Access: tasleemat_validate_data, tasleemat_render_artifact</code>
              </div>
            </div>
          </section>

          <!-- Section 8: AI Synthesis & Prompting -->
          <section id="llm-client" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">8. Programmatic LLM Document Synthesis (<code>tasleemat.ai</code>)</h2>
            <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
              The <code>tasleemat.ai.AIClient</code> class offers a unified Python interface supporting Google Gemini, OpenAI, Anthropic, 
              local Ollama instances, and deterministic mock runners for unit testing.
            </p>

            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Provider Code</th>
                    <th>Default Model</th>
                    <th>Supported Endpoint Types</th>
                    <th>Environment Variable</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>gemini</code></td>
                    <td><code>gemini-2.5-flash</code></td>
                    <td>Google AI Studio Cloud REST API</td>
                    <td><code>GEMINI_API_KEY</code></td>
                  </tr>
                  <tr>
                    <td><code>openai</code></td>
                    <td><code>gpt-4o</code></td>
                    <td>OpenAI API or custom proxy (<code>api_base</code>)</td>
                    <td><code>OPENAI_API_KEY</code></td>
                  </tr>
                  <tr>
                    <td><code>anthropic</code></td>
                    <td><code>claude-3-5-sonnet-20241022</code></td>
                    <td>Anthropic Messages API</td>
                    <td><code>ANTHROPIC_API_KEY</code></td>
                  </tr>
                  <tr>
                    <td><code>ollama</code></td>
                    <td><code>llama3.2</code></td>
                    <td>Local offline endpoint (<code>http://localhost:11434</code>)</td>
                    <td><code>OLLAMA_HOST</code></td>
                  </tr>
                  <tr>
                    <td><code>mock</code></td>
                    <td><code>mock-v1</code></td>
                    <td>In-memory deterministic synthesis for CI</td>
                    <td>None (zero API calls)</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">AI Client Python Usage</h3>
            <pre><code>from tasleemat.ai import AIClient
import tasleemat

# Initialize client (automatically reads configured key or environment)
client = AIClient(provider="gemini", model="gemini-2.5-flash")

# Load verified system prompt for Scope Statement (PMO-04.02.05)
prompt_text = tasleemat.get_artifact_asset("PMO-04.02.05", role="prompt", lang="en")

notes = '''
Project: Data Platform Revamp
Deliverables: Data ingestion engine, Kafka streaming cluster, Snowfake data warehouse, PowerBI dashboards.
Exclusions: Legacy mainframe hardware decommissioning.
Acceptance Criteria: 99.9% uptime, end-to-end ingestion latency under 5 seconds.
'''

# Synthesize markdown deliverable
deliverable_md = client.generate(
    prompt=f"{{prompt_text}}\\n\\nPROJECT NOTES:\\n{{notes}}",
    system_instruction="You are an enterprise PMO Director. Generate a formal Scope Statement matching the template structure."
)

print(deliverable_md)</code></pre>
          </section>

          <!-- Section 9: CI/CD & DevOps Pipelines -->
          <section id="cicd" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">9. CI/CD Pipelines &amp; Headless Quality Gates</h2>
            <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
              Enforce a strict <strong>Docs-as-Code</strong> philosophy by integrating Tasleemat validation gates into your Git pipelines. 
              Prevent broken schemas, unverified templates, or missing translations from merging into protected branches.
            </p>

            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">GitHub Actions Workflow Example (<code>.github/workflows/pmo-governance.yml</code>)</h3>
            <pre><code>name: PMO Governance &amp; Schema Quality Gates

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  validate-governance:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Install Tasleemat &amp; Dependencies
        run: |
          pip install --upgrade pip
          pip install tasleemat

      - name: Validate Completed Artifact JSON Files
        run: |
          # Recursively validate all project deliverable JSON files against companion schemas
          python3 -c "
          import pathlib, sys, json, tasleemat
          errors = 0
          for p in pathlib.Path('workspaces').rglob('*.json'):
              art_id = p.stem.split('.')[0] # e.g. PMO-03.01
              if art_id.startswith('PMO-'):
                  data = json.loads(p.read_text(encoding='utf-8'))
                  report = tasleemat.validate_artifact_data(art_id, data, mode='strict')
                  if not report.valid:
                      print(f'❌ Validation failed for {{p}}: {{report.errors}}')
                      errors += 1
          if errors > 0:
              sys.exit(1)
          print('✅ All project deliverables passed strict schema quality gates!')
          "

      - name: Run Test Suite
        run: |
          tasleemat test -v</code></pre>
          </section>

          <!-- Section 10: Attested Math Contracts -->
          <section id="attested-math" class="card" style="padding: 2.25rem;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
              <h2 style="font-size: 1.55rem; margin: 0;">10. Attested Computations &amp; Deterministic Math Contracts</h2>
              <span class="badge" style="background: var(--accent-purple-bg); color: var(--accent-purple); border: 1px solid var(--accent-purple-border); font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">PMO-06.05 EVA</span>
            </div>
            <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
              LLMs are notorious for mathematical hallucination when calculating financial and earned-value progress metrics. 
              Tasleemat establishes strict <strong>Attested Computation Contracts</strong> where financial metrics are calculated 
              deterministically by dedicated offline tools and verified cryptographically before publication.
            </p>

            <h3 style="font-size: 1.15rem; margin-top: 1rem; margin-bottom: 0.5rem;">Earned Value Analysis Computation Contract (<code>PMO-06.05</code>)</h3>
            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Metric</th>
                    <th>Standard Formula</th>
                    <th>Deterministic Rounding Rule</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Schedule Variance (SV)</strong></td>
                    <td><code>SV = EV - PV</code></td>
                    <td>Exact decimal currency match (± 0.01 tolerance)</td>
                  </tr>
                  <tr>
                    <td><strong>Cost Variance (CV)</strong></td>
                    <td><code>CV = EV - AC</code></td>
                    <td>Exact decimal currency match (± 0.01 tolerance)</td>
                  </tr>
                  <tr>
                    <td><strong>Schedule Performance Index (SPI)</strong></td>
                    <td><code>SPI = EV / PV</code></td>
                    <td>Half-up to 2 decimal places (handles PV=0 as 0.0)</td>
                  </tr>
                  <tr>
                    <td><strong>Cost Performance Index (CPI)</strong></td>
                    <td><code>CPI = EV / AC</code></td>
                    <td>Half-up to 2 decimal places (handles AC=0 as 0.0)</td>
                  </tr>
                  <tr>
                    <td><strong>Estimate at Completion (EAC)</strong></td>
                    <td><code>EAC = BAC / CPI</code></td>
                    <td>Half-up to 2 decimal places</td>
                  </tr>
                  <tr>
                    <td><strong>To-Complete Performance Index (TCPI)</strong></td>
                    <td><code>TCPI = (BAC - EV) / (BAC - AC)</code></td>
                    <td>Half-up to 2 decimal places</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 1rem; line-height: 1.6;">
              When autonomous agents synthesize Earned Value Reports (<code>PMO-06.05</code>), the pipeline invokes 
              <code>tools/attested_computations/eva_calculator.py</code> to produce verifiable ground truth and 
              <code>eva_attester.py</code> to verify that the table presented in the markdown document matches mathematical reality 
              prior to stage-gate approval.
            </p>
          </section>

        </div>
      </div>
    </div>
    """

    return render_html_page(
        title="Developers & AI Integration Reference",
        content=content,
        lang="en",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/developers/",
    )


def generate_developers_ar(base_url: str = "/Tasleemat") -> str:
    content = f"""
    <section class="hero-section" style="padding: 3.5rem 0 2.5rem;">
      <div class="container">
        <div class="hero-pill">
          <span>⚙️ الدليل الهندسي وتكامل الذكاء الاصطناعي المؤسسي</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.35rem; margin-top: 0.75rem;">مرجع المطورين وهندسة الذكاء الاصطناعي</h1>
        <p class="hero-subtitle" style="max-width: 820px; margin: 0 auto; line-height: 1.8;">
          المرجع التقني الشامل لمهندسي البرمجيات، معماريي الذكاء الاصطناعي، ومسؤولي عمليات DevOps.
          دليل برمجي متكامل لربط تسليمات عبر مكتبة بايثون، أدوات سطر الأوامر (CLI)، خادم بروتوكول سياق النماذج (MCP)،
          وأسراب الوكلاء الأذكياء متعددي المهام (Multi-Agent Swarms).
        </p>
      </div>
    </section>

    <div class="container" style="margin-top: 2.5rem; margin-bottom: 5rem;">
      <div style="display: flex; gap: 2.5rem; flex-wrap: wrap;">
        
        <!-- Sticky Sidebar Navigation AR -->
        <aside style="width: 260px; flex-shrink: 0;">
          <div style="position: sticky; top: 5.5rem; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 0.75rem; padding: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            <div style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); margin-bottom: 0.85rem;">فهرس الدليل التقني</div>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.45rem; font-size: 0.86rem; padding: 0; margin: 0;">
              <li><a href="#quickstart" style="color: var(--text-main); text-decoration: none; font-weight: 500;">1. التثبيت السريع والبيئة</a></li>
              <li><a href="#cli" style="color: var(--text-main); text-decoration: none; font-weight: 500;">2. مرجع أوامر الطرفية (CLI)</a></li>
              <li><a href="#sdk" style="color: var(--text-main); text-decoration: none; font-weight: 500;">3. معمارية مكتبة بايثون (SDK)</a></li>
              <li><a href="#mcp" style="color: var(--text-main); text-decoration: none; font-weight: 500;">4. بروتوكول سياق النماذج (MCP)</a></li>
              <li><a href="#schemas" style="color: var(--text-main); text-decoration: none; font-weight: 500;">5. مخططات Draft 2020-12 و RFC</a></li>
              <li><a href="#self-correction" style="color: var(--text-main); text-decoration: none; font-weight: 500;">6. حلقة التصحيح الذاتي للوكلاء</a></li>
              <li><a href="#multi-agent" style="color: var(--text-main); text-decoration: none; font-weight: 500;">7. أسراب الوكلاء المتعددين</a></li>
              <li><a href="#llm-client" style="color: var(--text-main); text-decoration: none; font-weight: 500;">8. توليد وتأصيل الوثائق بالذكاء الاصطناعي</a></li>
              <li><a href="#cicd" style="color: var(--text-main); text-decoration: none; font-weight: 500;">9. خطوط CI/CD وبوابات الجودة</a></li>
              <li><a href="#attested-math" style="color: var(--text-main); text-decoration: none; font-weight: 500;">10. عقود الحسابات الرياضية الموثقة</a></li>
            </ul>
          </div>
        </aside>

        <!-- Main Technical Content AR -->
        <div style="flex: 1; min-width: 320px; display: flex; flex-direction: column; gap: 3rem;">
          
          <!-- Section 1: Quick Installation AR -->
          <section id="quickstart" class="card" style="padding: 2.25rem;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
              <h2 style="font-size: 1.55rem; margin: 0;">1. التثبيت السريع ومتطلبات البيئة</h2>
              <span class="badge" style="background: var(--accent-blue-bg); color: var(--accent-blue); border: 1px solid var(--accent-blue-border); font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">مستودع PyPI الرسمي</span>
            </div>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
              حزمة <code>tasleemat</code> منشورة رسميًا عبر مستودع PyPI العام كحزمة بايثون نقية تدعم إصدارات بايثون <strong>3.9 و 3.10 و 3.11 و 3.12 و 3.13</strong>.
              تحتوي الحزمة الموزعة على كافة قوالب التسليمات الـ 114 باللغتين، مخططات JSON المرافقة، قواميس الحقول، أداة سطر الأوامر، وخادم بروتوكول MCP.
            </p>
            <pre><code># التثبيت المباشر عبر مدير الحزم pip
pip install tasleemat

# أو التثبيت داخل بيئة افتراضية منعزلة
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install tasleemat</code></pre>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 1rem; margin-bottom: 0.5rem;">
              التحقق من جاهزية أداة الطرفية وخادم بروتوكول سياق النموذج (MCP):
            </p>
            <pre><code>tasleemat --version
tasleemat-mcp --help</code></pre>
          </section>

          <!-- Section 2: CLI Command Reference AR -->
          <section id="cli" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">2. مرجع أوامر الطرفية الكامل (CLI Reference)</h2>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.5rem;">
              توفر أداة <code>tasleemat</code> في سطر الأوامر إمكانيات متطورة لتأسيس مساحات العمل، واستعراض الفهرس،
              وتوليد الوثائق بنماذج الذكاء الاصطناعي، وتنفيذ الاختبارات، وتشغيل خوادم الوكلاء الأذكياء.
            </p>
            
            <h3 style="font-size: 1.2rem; margin-top: 1.5rem; margin-bottom: 0.5rem; color: var(--text-main);">أ. تأسيس مساحة عمل المشروع المخصصة (<code>tasleemat init</code>)</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 0.75rem;">
              بناء هيكل مجلدات متكامل منسوخ مسبقاً بالتسليمات الإلزامية حسب فئة الحوكمة وباقة المنهجية:
            </p>
            <pre><code># النمط التفاعلي (يطرح أسئلة الإعداد خطوة بخطوة)
tasleemat init

# النمط المباشر للسكربتات: الفئة 2 (متوسطة) مع باقة أجايل بالعربية
tasleemat init \
  --tier 2 \
  --pack agile \
  --lang ar \
  --code "PRJ-2026-CLOUD-01" \
  --name "مشروع التحول السحابي المؤسسي" \
  --pm "سارة الأحمد" \
  --sponsor "د. خالد المنصور" \
  --out ./workspaces/PRJ-2026-CLOUD-01

# مشروع الفئة 1 الكبرى باللغتين العربية والإنجليزية
tasleemat init \
  --tier 1 \
  --pack hybrid \
  --lang both \
  --code "PRJ-2026-CORE" \
  --name "Enterprise Core Banking Migration" \
  --pm "Tariq Al-Harbi" \
  --sponsor "Executive VP IT" \
  --out ./enterprise_workspace</code></pre>

            <h3 style="font-size: 1.2rem; margin-top: 2rem; margin-bottom: 0.5rem; color: var(--text-main);">ب. استعراض الفهرس والبحث المتقدم (<code>tasleemat list</code> &amp; <code>search</code>)</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 0.75rem;">
              استعراض المخرجات الـ 114 باللغتين العربية والإنجليزية أو البحث السريع بالكلمات المفتاحية:
            </p>
            <pre><code># استعراض كافة التسليمات بالعربية أو الإنجليزية
tasleemat list --lang ar
tasleemat list --lang en

# البحث السريع في الفهرس
tasleemat search "مخاطر" --lang ar
tasleemat search "ميثاق" --lang ar
tasleemat search "PMO-03.01" --lang en</code></pre>

            <h3 style="font-size: 1.2rem; margin-top: 2rem; margin-bottom: 0.5rem; color: var(--text-main);">ج. إدارة حسابات الذكاء الاصطناعي (<code>tasleemat config</code>)</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 0.75rem;">
              حفظ المفاتيح في المسار الآمن <code>~/.tasleemat/config.json</code>:
            </p>
            <pre><code># ضبط مزود Google Gemini
tasleemat config set --provider gemini --model gemini-2.5-flash --key "AIzaSy..."

# ضبط مزودي OpenAI أو Anthropic
tasleemat config set --provider openai --model gpt-4o --key "sk-proj-..."
tasleemat config set --provider anthropic --model claude-3-5-sonnet-20241022 --key "sk-ant-..."

# ضبط خادم Ollama المحلي المستقل
tasleemat config set --provider ollama --model llama3.2 --endpoint "http://localhost:11434"

# استعراض الإعدادات الحالية بأمان
tasleemat config show</code></pre>

            <h3 style="font-size: 1.2rem; margin-top: 2rem; margin-bottom: 0.5rem; color: var(--text-main);">د. التوليد الآلي للوثائق (<code>tasleemat generate</code>)</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 0.75rem;">
              توليد مسودات احترافية من ملاحظات الاجتماعات باستخدام الذكاء الاصطناعي:
            </p>
            <pre><code># توليد ميثاق المشروع (PMO-03.01) من ملف ملاحظات الاجتماع
tasleemat generate \
  --form PMO-03.01 \
  --notes ./meeting_minutes.txt \
  --lang ar \
  --out ./drafts/ميثاق_المشروع.md

# نمط المحاكاة المحلي (Mock) لخطوط CI دون استهلاك رموز API
tasleemat generate \
  --form PMO-03.01 \
  --notes "ملاحظات تجريبية" \
  --mock \
  --out ./ci_output/Mock_Charter.md</code></pre>

            <h3 style="font-size: 1.2rem; margin-top: 2rem; margin-bottom: 0.5rem; color: var(--text-main);">هـ. حزمة الاختبارات الآلية (<code>tasleemat test</code>)</h3>
            <pre><code># تنفيذ كافة اختبارات الوحدة والتكامل (أكثر من 140 اختباراً)
tasleemat test -v</code></pre>
          </section>

          <!-- Section 3: Python SDK Architecture AR -->
          <section id="sdk" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">3. معمارية مكتبة بايثون البرمجية (SDK Reference)</h2>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.5rem;">
              تصدّر مكتبة <code>tasleemat</code> ثماني دوال برمجية محورية لاستكشاف الفهرس، واستخراج الأصول، 
              وتحليل التخصيص، والتحقق الصارم من التنسيقات، وتصيير الوثائق إلى صفحات HTML مستقلة.
            </p>

            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>الدالة البرمجية</th>
                    <th>المعاملات المدخلة</th>
                    <th>نوع المخرجات</th>
                    <th>الوصف الوظيفي</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>list_artifacts()</code></td>
                    <td><code>phase=None, tier=None, pack=None</code></td>
                    <td><code>List[ArtifactSummary]</code></td>
                    <td>استرجاع كائنات ملخصة لكافة الـ 114 تسليمة أو باقة مخصصة مع بصمات SHA-256 الرقمية.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_definition()</code></td>
                    <td><code>artifact_id: str</code></td>
                    <td><code>dict</code></td>
                    <td>قاموس البيانات الوصفية المعتمد متضمناً المرحلة وفئات الحوكمة ومسارات الأصول.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_assets()</code></td>
                    <td><code>artifact_id: str, lang='en'</code></td>
                    <td><code>ArtifactAssets</code></td>
                    <td>كائن برمجي لإدارة مسارات الملفات واسترجاع المحتويات بأمان دون اختراق المسارات.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_asset()</code></td>
                    <td><code>artifact_id: str, role: str, lang='en'</code></td>
                    <td><code>Union[str, dict, list]</code></td>
                    <td>استخراج محتوى الأصل مباشرة بحسب دوره: <code>template</code>، <code>guide</code>، <code>prompt</code>، <code>schema</code>، <code>dictionary</code>، <code>example</code>.</td>
                  </tr>
                  <tr>
                    <td><code>get_tailoring_profile()</code></td>
                    <td><code>tier: str, pack: str='general'</code></td>
                    <td><code>List[str]</code></td>
                    <td>تحديد قائمة معرفات التسليمات الإلزامية لمستوى الحوكمة (1, 2, 3) وباقة المنهجية.</td>
                  </tr>
                  <tr>
                    <td><code>get_lexicon()</code></td>
                    <td><code>category: Optional[str]=None</code></td>
                    <td><code>List[dict]</code></td>
                    <td>استرجاع المصطلحات المعتمدة المترجمة بين العربية والإنجليزية وفق معايير PMI وهيئة الحكومة الرقمية (DGA).</td>
                  </tr>
                  <tr>
                    <td><code>validate_artifact_data()</code></td>
                    <td><code>artifact_id: str, data: dict, mode='strict'</code></td>
                    <td><code>ValidationReport</code></td>
                    <td>التحقق الصارم من كائن البيانات مقابل مخطط Draft 2020-12 وتنسيقات RFC المعتمدة.</td>
                  </tr>
                  <tr>
                    <td><code>render_artifact()</code></td>
                    <td><code>artifact_id: str, lang='en', data=None, out_path=None</code></td>
                    <td><code>str</code></td>
                    <td>تصيير قالب التسليمة وبياناتها إلى صفحة HTML أنيقة جاهزة للطباعة مع دعم الاتجاه العربي (RTL).</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="font-size: 1.2rem; margin-top: 2rem; margin-bottom: 0.5rem; color: var(--text-main);">مثال تطبيقي متكامل في بايثون</h3>
            <pre><code>import tasleemat

# 1. استخراج التسليمات الإلزامية لمشروع قياسي (فئة 2) يتبع المنهجية الرشيقة
required_ids = tasleemat.get_tailoring_profile(tier="2", pack="agile")
print(f"عدد التسليمات الإلزامية: {{len(required_ids)}}")

# 2. استخراج موجه الذكاء الاصطناعي المعتمد لميثاق المشروع (PMO-03.01) بالعربية
prompt_ar = tasleemat.get_artifact_asset("PMO-03.01", role="prompt", lang="ar")

# 3. قراءة مخطط JSON الهيكلي
schema_def = tasleemat.get_artifact_asset("PMO-03.01", role="schema", lang="ar")
print(f"معرف المخطط: {{schema_def.get('$id')}}")

# 4. التدقيق البرمجي في بيانات الميثاق (النمط الصارم)
charter_payload = {{
    "project_code": "PRJ-2026-CLOUD",
    "project_name": "مشروع التحول السحابي الموحد",
    "start_date": "2026-11-01",              # تاريخ صالح وفق مواصفة RFC 3339
    "sponsor_name": "د. خالد المنصور",
    "estimated_budget": 3500000.00
}}

report = tasleemat.validate_artifact_data("PMO-03.01", charter_payload, mode="strict")
if report.valid:
    print(f"✅ البيانات مطابقة للمخطط! بصمة التحقق: {{report.fingerprint}}")
else:
    print(f"❌ فشل التدقيق لوجود {{len(report.errors)}} أخطاء:")
    for err in report.errors:
        print(f"   • {{err.field_path}}: {{err.message}} (الرمز: {{err.code}})")

# 5. تصيير الوثيقة المعتمدة إلى صفحة HTML مطبوعة بالعربية
html_output = tasleemat.render_artifact(
    artifact_id="PMO-03.01",
    lang="ar",
    data={{"Project_Name": "مشروع التحول السحابي", "Project_Code": "PRJ-2026-CLOUD"}},
    out_path="./exports/charter_rendered.html"
)</code></pre>
          </section>

          <!-- Section 4: Model Context Protocol (MCP) AR -->
          <section id="mcp" class="card" style="padding: 2.25rem;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
              <h2 style="font-size: 1.55rem; margin: 0;">4. بروتوكول سياق النماذج (MCP) للذكاء الاصطناعي</h2>
              <span class="badge" style="background: var(--accent-emerald-bg); color: var(--accent-emerald); border: 1px solid var(--accent-emerald-border); font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">قنوات Stdio JSON-RPC 2.0</span>
            </div>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
              تتضمن تسليمات خادم بروتوكول Model Context Protocol قياسي متوافق مع مواصفة <code>2024-11-05</code>.
              يتيح الخادم لعملاء الذكاء الاصطناعي (مثل Claude Desktop، Cursor، OpenCode، و Antigravity) استكشاف الفهرس،
              وجلب القوالب والموجهات، والبحث في المصطلحات، والتحقق الصارم من مخططات JSON، وتصيير صفحات HTML برمجياً.
            </p>

            <h3 style="font-size: 1.15rem; margin-top: 1rem; margin-bottom: 0.5rem;">ملفات إعدادات العملاء الذكية</h3>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 0.75rem;">
              أضف خادم تسليمات إلى ملف إعدادات العميل الخاص بك:
            </p>
            <ul style="margin-right: 1.5rem; color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1rem;">
              <li><strong>Claude Desktop:</strong> <code>~/.config/Claude/claude_desktop_config.json</code> (لينكس) أو المسار الموازي في ماك وويندوز</li>
              <li><strong>محرر Cursor:</strong> الملف <code>.cursor/mcp.json</code> في جذر مساحة العمل</li>
              <li><strong>مساعدات OpenCode و Antigravity:</strong> تشغيل الأمر المباشر <code>tasleemat mcp</code> أو <code>tasleemat-mcp</code></li>
            </ul>

            <pre><code>// claude_desktop_config.json أو .cursor/mcp.json
{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat",
      "args": ["mcp"]
    }}
  }}
}}</code></pre>

            <h3 style="font-size: 1.2rem; margin-top: 1.75rem; margin-bottom: 0.75rem; color: var(--text-main);">أدوات MCP الست الأساسية المتاحة للوكلاء</h3>
            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>اسم الأداة في MCP</th>
                    <th>المعاملات المدخلة</th>
                    <th>وظيفة الأداة للوكيل الذكي</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>tasleemat_list_artifacts</code></td>
                    <td><code>phase?: string, tier?: string</code></td>
                    <td>استكشاف التسليمات الإلزامية المتاحة عبر مراحل المشروع الثماني.</td>
                  </tr>
                  <tr>
                    <td><code>tasleemat_get_artifact</code></td>
                    <td><code>artifact_id: string</code></td>
                    <td>استرجاع البيانات الوصفية وبصمات SHA-256 للمخرج المحدد.</td>
                  </tr>
                  <tr>
                    <td><code>tasleemat_get_asset</code></td>
                    <td><code>artifact_id: string, role: string, lang?: "en"|"ar"</code></td>
                    <td>جلب نصوص <code>template</code> أو <code>guide</code> أو <code>prompt</code> أو <code>schema</code> أو <code>dictionary</code> أو <code>example</code>.</td>
                  </tr>
                  <tr>
                    <td><code>tasleemat_get_lexicon</code></td>
                    <td><code>category?: string, query?: string</code></td>
                    <td>منع الانحراف الدلالي في الترجمة عبر استرجاع المصطلحات الرسمية المعتمدة من PMI و DGA.</td>
                  </tr>
                  <tr>
                    <td><code>tasleemat_validate_data</code></td>
                    <td><code>artifact_id: string, data: object, mode?: "strict"|"draft"</code></td>
                    <td>التحقق الهيكلي من صحة كائن البيانات؛ وإرجاع قائمة أخطاء برمجية دقيقة في حال عدم المطابقة.</td>
                  </tr>
                  <tr>
                    <td><code>tasleemat_render_artifact</code></td>
                    <td><code>artifact_id: string, lang?: "en"|"ar", data?: object</code></td>
                    <td>تصيير الوثيقة المعتمدة كصفحة HTML مستقلة للعرض على لجان التوجيه والرعاة التنفيذيين.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </section>

          <!-- Section 5: Schemas & RFC Formats AR -->
          <section id="schemas" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">5. مخططات Draft 2020-12 والتحقق الصارم من معايير RFC</h2>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
              كل تسليمة من الـ 114 تسليمة مقترنة بمخطط JSON رسمي متوافق مع مواصفة <strong>JSON Schema Draft 2020-12</strong>.
              وبينما تعد قيود التنسيق اختيارية في المواصفة العامة، يفرض محرك التدقيق في تسليمات التحقق الصارم في <strong>نمط التوكيد (Assertion Mode)</strong> 
              لضمان عقود بيانات لا تقبل الشك أو التخمين.
            </p>

            <h3 style="font-size: 1.15rem; margin-top: 1rem; margin-bottom: 0.5rem;">تنسيقات RFC المعتمدة في محرك التحقق</h3>
            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>محدد التنسيق</th>
                    <th>المعيار القياسي</th>
                    <th>شروط التحقق والحالات المستثناة</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>date</code></td>
                    <td>RFC 3339 full-date</td>
                    <td>الصيغة الصارمة <code>YYYY-MM-DD</code>. التحقق من سلامة الأيام والشهور وسنوات الكبيس (رفض 29 فبراير في السنوات البسيطة).</td>
                  </tr>
                  <tr>
                    <td><code>date-time</code></td>
                    <td>RFC 3339 date-time</td>
                    <td>يشترط التاريخ وفاصل <code>T</code> والوقت وتحديد النطاق الزمني (<code>Z</code> أو <code>+/-HH:MM</code>). يدعم ثانية الكبيس 60.</td>
                  </tr>
                  <tr>
                    <td><code>time</code></td>
                    <td>RFC 3339 partial-time</td>
                    <td>صيغة الوقت القياسية <code>HH:MM:SS[.fractional][Z|offset]</code>.</td>
                  </tr>
                  <tr>
                    <td><code>uuid</code></td>
                    <td>RFC 4122 UUID</td>
                    <td>الصيغة السداسية العشرية 8-4-4-4-12 (36 حرفاً). المعرفات المجردة فقط؛ بادئات URN تنتمي لـ <code>uri</code>.</td>
                  </tr>
                  <tr>
                    <td><code>uri</code></td>
                    <td>RFC 3986 URI</td>
                    <td>عنوان مطلق يشترط وجود المخطط (مثل <code>https://</code>). يمنع المسافات والمحارف غير المرمزة.</td>
                  </tr>
                  <tr>
                    <td><code>uri-reference</code></td>
                    <td>RFC 3986 URI Reference</td>
                    <td>يقبل العنوان المطلق أو المسار النسبي المنضبط دون مسافات فارغة.</td>
                  </tr>
                  <tr>
                    <td><code>email</code></td>
                    <td>RFC 5322 addr-spec</td>
                    <td>الصيغة القياسية <code>user@domain</code> بحد أقصى 254 بايت مع فحص النطاقات.</td>
                  </tr>
                  <tr>
                    <td><code>duration</code></td>
                    <td>ISO 8601 / RFC 3339</td>
                    <td>نصوص المدة الزمنية القياسية (مثل <code>P1Y2M</code>، <code>PT15M</code>). يرفض الرموز المجردة أو النصوص الوصفية.</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">النمط الصارم (Strict) مقابل نمط المسودة (Draft)</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-top: 0.75rem;">
              <div style="background: var(--bg-card-hover); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
                <h4 style="margin-top: 0; color: var(--accent-blue); font-size: 1rem;">🔒 النمط الصارم (Strict Mode)</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 0;">
                  يفرض كافة الحقول الإلزامية، أمان الأنواع (التفريق بين True و 1)، الحدود الرقمية، وتنسيقات RFC. 
                  يُرجع <code>valid=False</code> عند أي مخالفة، ويُستخدم في بوابات العبور واختبارات CI/CD.
                </p>
              </div>
              <div style="background: var(--bg-card-hover); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
                <h4 style="margin-top: 0; color: var(--accent-emerald); font-size: 1rem;">📝 نمط المسودة (Draft Mode)</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 0;">
                  يسمح بالملفات غير المكتملة والحقول الناقصة مع إطلاق تحذيرات برمجية غير حاجبة. 
                  مخصص لمساعدة الوكلاء الأذكياء على صياغة الأقسام تدريجياً عبر حوارات متعددة.
                </p>
              </div>
            </div>
          </section>

          <!-- Section 6: Agent Self-Correction Loop AR -->
          <section id="self-correction" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">6. حلقة التصحيح الذاتي التلقائي للوكلاء الأذكياء</h2>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
              عند توليد كائنات البيانات بواسطة النماذج اللغوية، تقع أخطاء شائعة (مثل صياغة التواريخ بصيغة غير قياسية، أو تمرير القيم المنطقية كنصوص).
              يعمل محرك الفحص في تسليمات كـ <strong>مترجم برمجي عالي الدقة</strong> يُعيد تفاصيل الخطأ الدقيقة للنموذج ليعيد صياغته ذاتياً حتى المطابقة التامة.
            </p>

            <div class="mermaid">
flowchart TD
    RAW["مدخلات المشروع: ملاحظات الاجتماعات"] --> LLM["وكيل الذكاء الاصطناعي (Gemini / Claude / GPT)"]
    LLM --> JSON["مسودة كائن البيانات JSON"]
    JSON --> VALIDATE{{"tasleemat.validate_artifact_data(strict=True)"}}
    
    VALIDATE -->|مطابق: valid == True| RENDER["tasleemat.render_artifact()"]
    RENDER --> HUMAN["اعتماد بوابة العبور من راعي المشروع"]
    
    VALIDATE -->|غير مطابق: valid == False| SURGICAL["استخراج مصفوفة الأخطاء الهيكلية:<br/>- مسار الحقل: start_date<br/>- رمز الخطأ: FORMAT_VIOLATION<br/>- القاعدة: معيار RFC 3339 (YYYY-MM-DD)"]
    SURGICAL --> REPROMPT["إعادة توجيه النموذج بالأخطاء المحددة فقط"]
    REPROMPT --> LLM
            </div>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">شيفرة حلقة التصحيح الذاتي في بايثون</h3>
            <pre><code>import tasleemat
from tasleemat.ai import AIClient

def generate_and_heal_deliverable(artifact_id: str, raw_notes: str, max_attempts: int = 3) -> dict:
    client = AIClient(provider="gemini", model="gemini-2.5-flash")
    schema_def = tasleemat.get_artifact_asset(artifact_id, role="schema", lang="ar")
    prompt_instructions = tasleemat.get_artifact_asset(artifact_id, role="prompt", lang="ar")
    
    system_prompt = (
        f"أنت مهندس ذكاء اصطناعي متخصص في PMO. قم بتوليد كائن JSON صالح يطابق مخطط Draft 2020-12 تماماً.\\n"
        f"معرف المخطط: {{schema_def.get('$id')}}\\n"
        f"يتم فرض قيود RFC الصارمة: التواريخ بصيغة YYYY-MM-DD والأرقام موجبة."
    )
    
    current_prompt = f"{{prompt_instructions}}\\n\\nملاحظات المشروع:\\n{{raw_notes}}"
    
    for attempt in range(1, max_attempts + 1):
        raw_response = client.generate(prompt=current_prompt, system_instruction=system_prompt)
        payload = extract_json_block(raw_response)
        
        # الفحص البرمجي الصارم
        report = tasleemat.validate_artifact_data(artifact_id, payload, mode="strict")
        if report.valid:
            print(f"✅ تم اجتياز الفحص بنجاح في المحاولة {{attempt}}!")
            return payload
            
        print(f"⚠️ المحاولة {{attempt}} غير مطابقة. تجميع التغذية العكسية الدقيقة...")
        error_context = "\\n".join([f"- الحقل '{{e.field_path}}': {{e.message}} (القاعدة: {{e.schema_rule}})" for e in report.errors])
        
        # إعادة التوجيه الدقيق بالأخطاء فقط
        current_prompt = (
            f"مخرجات JSON السابقة احتوت على أخطاء هيكلية محددة:\\n{{error_context}}\\n\\n"
            f"قم بتصحيح هذه الحقول فقط وأعد توليد كائن JSON صالح بدون مقدمات أو تعليقات."
        )
        
    raise RuntimeError(f"تعذر استيفاء المخطط للتسليمة {{artifact_id}} بعد {{max_attempts}} محاولات.")</code></pre>
          </section>

          <!-- Section 7: Multi-Agent PMO Swarms AR -->
          <section id="multi-agent" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">7. معمارية أسراب الوكلاء المتعددين (Multi-Agent PMO Swarms)</h2>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
              في بيئات المؤسسات المتقدمة التي تستخدم أطر <strong>CrewAI</strong> أو <strong>LangGraph</strong> أو <strong>AutoGen</strong>،
              يتم توزيع مهام التوثيق والحوكمة على وكلاء متخصصين متعددي المهام بدلاً من الاعتماد على وكيل أحادي.
            </p>

            <div class="mermaid">
flowchart LR
    SPONSOR["راعي المشروع / مدير PMO"] --> ORCH["<b>الوكيل المنسق العام</b><br/>يحدد الفئة ويرتب اعتماديات DAG"]
    
    subgraph Swarm["سرب الوكلاء المتخصصين"]
        ORCH --> BA["<b>محلل الأعمال</b><br/>PMO-01.01 دراسة الجدوى<br/>PMO-03.01 ميثاق المشروع"]
        ORCH --> SCHED["<b>مهندس الجدولة</b><br/>PMO-04.02.06 هيكل WBS<br/>PMO-04.03.08 الجدول الزمني"]
        ORCH --> RISK["<b>أخصائي المخاطر</b><br/>PMO-04.08.02 سجل المخاطر<br/>PMO-04.08.04 مصفوفة الاحتمالية"]
    end
    
    BA --> AUDIT["<b>وكيل التدقيق الحوكمي</b><br/>tasleemat_validate_data"]
    SCHED --> AUDIT
    RISK --> AUDIT
    
    AUDIT -->|مطابق| HTML["<b>محرك التصيير المستقل</b><br/>tasleemat_render_artifact"]
    HTML --> HUMAN["الاعتماد البشري في بوابة العبور"]
            </div>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">الأدوار التخصصية في السرب الذكي</h3>
            <div style="display: flex; flex-direction: column; gap: 1rem; margin-top: 0.75rem;">
              <div style="background: var(--bg-card-hover); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
                <h4 style="margin: 0 0 0.5rem 0; font-size: 1.05rem; color: var(--accent-blue);">1. الوكيل المنسق العام (مدير PMO الافتراضي)</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 0.5rem;">
                  <strong>المسؤولية:</strong> استدعاء <code>get_tailoring_profile(tier, pack)</code> لتحديد المخرجات المطلوبة، وفرض مخطط الاعتماديات (DAG) بحيث لا يبدأ إعداد WBS قبل اعتماد الميثاق.
                </p>
                <code style="font-size: 0.82rem;">صلاحيات الأدوات: tasleemat_list_artifacts, tasleemat_get_artifact, get_tailoring_profile</code>
              </div>

              <div style="background: var(--bg-card-hover); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
                <h4 style="margin: 0 0 0.5rem 0; font-size: 1.05rem; color: var(--accent-blue);">2. وكلاء الصياغة التخصصية (تحليل الأعمال، الجدولة، المخاطر)</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 0.5rem;">
                  <strong>المسؤولية:</strong> صياغة الأقسام بالاستناد إلى موجهات <code>get_artifact_asset(role="prompt")</code> والاسترشاد بالأمثلة الواقعية الـ 228 في <code>examples/ar/</code>.
                </p>
                <code style="font-size: 0.82rem;">صلاحيات الأدوات: tasleemat_get_asset, tasleemat_get_lexicon</code>
              </div>

              <div style="background: var(--bg-card-hover); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
                <h4 style="margin: 0 0 0.5rem 0; font-size: 1.05rem; color: var(--accent-blue);">3. وكيل التدقيق الحوكمي (QA &amp; Governance Gatekeeper)</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 0.5rem;">
                  <strong>المسؤولية:</strong> تشغيل <code>validate_artifact_data(mode="strict")</code> والتأكد من استيفاء كافة الحقول وقيود RFC قبل السماح برفع الوثيقة للاعتماد البشري.
                </p>
                <code style="font-size: 0.82rem;">صلاحيات الأدوات: tasleemat_validate_data, tasleemat_render_artifact</code>
              </div>
            </div>
          </section>

          <!-- Section 8: AI Synthesis & Prompting AR -->
          <section id="llm-client" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">8. عميل الذكاء الاصطناعي الموحد في بايثون (<code>tasleemat.ai</code>)</h2>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
              توفر فئة <code>tasleemat.ai.AIClient</code> واجهة بايثون موحدة تدعم نماذج Google Gemini، OpenAI، Anthropic،
              خوادم Ollama المحلية، ونمط المحاكاة المكتبي (Mock) لاختبارات التكامل.
            </p>

            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>رمز المزود</th>
                    <th>النموذج الافتراضي</th>
                    <th>نوع نقطة الاتصال المدعومة</th>
                    <th>متغير البيئة القياسي</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>gemini</code></td>
                    <td><code>gemini-2.5-flash</code></td>
                    <td>Google AI Studio Cloud REST API</td>
                    <td><code>GEMINI_API_KEY</code></td>
                  </tr>
                  <tr>
                    <td><code>openai</code></td>
                    <td><code>gpt-4o</code></td>
                    <td>OpenAI API أو وكيل مخصص (<code>api_base</code>)</td>
                    <td><code>OPENAI_API_KEY</code></td>
                  </tr>
                  <tr>
                    <td><code>anthropic</code></td>
                    <td><code>claude-3-5-sonnet-20241022</code></td>
                    <td>Anthropic Messages API</td>
                    <td><code>ANTHROPIC_API_KEY</code></td>
                  </tr>
                  <tr>
                    <td><code>ollama</code></td>
                    <td><code>llama3.2</code></td>
                    <td>نقطة اتصال محلية مستقلة (<code>http://localhost:11434</code>)</td>
                    <td><code>OLLAMA_HOST</code></td>
                  </tr>
                  <tr>
                    <td><code>mock</code></td>
                    <td><code>mock-v1</code></td>
                    <td>محاكاة حتمية داخل الذاكرة لخطوط CI</td>
                    <td>بدون (صفر استهلاك)</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">نموذج استخدام عميل الذكاء الاصطناعي في بايثون</h3>
            <pre><code>from tasleemat.ai import AIClient
import tasleemat

# تهيئة العميل البرمجي (يقرأ المفتاح تلقائياً من الإعدادات أو البيئة)
client = AIClient(provider="gemini", model="gemini-2.5-flash")

# جلب موجه بيان النطاق المعتمد (PMO-04.02.05)
prompt_text = tasleemat.get_artifact_asset("PMO-04.02.05", role="prompt", lang="ar")

notes = '''
المشروع: منصة معالجة البيانات المركزية
المخرجات الأساسية: محرك استيعاب البيانات، عنقود كافكا للبث اللحظي، مستودع البيانات السحابي، لوحات PowerBI.
الاستثناءات: تفكيك الأجهزة القديمة غير مشمول في هذا النطاق.
معايير القبول: جاهزية بنسبة 99.9%، وزمن استجابة الاستيعاب أقل من 5 ثوانٍ.
'''

# توليد مسودة الوثيقة بصيغة ماركداون
deliverable_md = client.generate(
    prompt=f"{{prompt_text}}\\n\\nملاحظات المشروع:\\n{{notes}}",
    system_instruction="أنت مدير مكتب إدارة مشاريع محترف. قم بصياغة بيان نطاق متكامل ومطابق لهيكل النموذج."
)

print(deliverable_md)</code></pre>
          </section>

          <!-- Section 9: CI/CD & DevOps Pipelines AR -->
          <section id="cicd" class="card" style="padding: 2.25rem;">
            <h2 style="font-size: 1.55rem; margin-bottom: 0.75rem;">9. خطوط أنابيب CI/CD وبوابات الجودة المؤتمتة</h2>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
              تطبيق فلسفة <strong>الوثائق كشيفرة برمجية (Docs-as-Code)</strong> عبر دمج بوابات فحص تسليمات داخل خطوط الأنابيب في Git، 
              لمنع دمج أي وثائق غير مطابقة للمخططات في الفروع الرئيسية.
            </p>

            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">ملف إعدادات GitHub Actions (<code>.github/workflows/pmo-governance.yml</code>)</h3>
            <pre><code>name: PMO Governance &amp; Schema Quality Gates

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  validate-governance:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Install Tasleemat
        run: |
          pip install --upgrade pip
          pip install tasleemat

      - name: Validate Completed Artifact JSON Files
        run: |
          # فحص كافة ملفات JSON للمشروع مقابل مخططات Draft 2020-12
          python3 -c "
          import pathlib, sys, json, tasleemat
          errors = 0
          for p in pathlib.Path('workspaces').rglob('*.json'):
              art_id = p.stem.split('.')[0]
              if art_id.startswith('PMO-'):
                  data = json.loads(p.read_text(encoding='utf-8'))
                  report = tasleemat.validate_artifact_data(art_id, data, mode='strict')
                  if not report.valid:
                      print(f'❌ فشل التدقيق للملف {{p}}: {{report.errors}}')
                      errors += 1
          if errors > 0:
              sys.exit(1)
          print('✅ اجتازت كافة وثائق المشروع بوابات الجودة الصارمة بنجاح!')
          "

      - name: Run Test Suite
        run: |
          tasleemat test -v</code></pre>
          </section>

          <!-- Section 10: Attested Math Contracts AR -->
          <section id="attested-math" class="card" style="padding: 2.25rem;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
              <h2 style="font-size: 1.55rem; margin: 0;">10. عقود الحسابات الرياضية الموثقة (Attested Math Contracts)</h2>
              <span class="badge" style="background: var(--accent-purple-bg); color: var(--accent-purple); border: 1px solid var(--accent-purple-border); font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">تحليل القيمة المكتسبة PMO-06.05</span>
            </div>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
              تتعرض النماذج اللغوية للهلوسة عند إجراء العمليات الحسابية والمالية التراكمية.
              تؤسس تسليمات <strong>عقود حسابات رياضية موثقة وحتمية</strong> بحيث تُحسب مؤشرات الأداء المالي برمجياً دون تدخل الوكلاء،
              ويتم التحقق منها قبل تقديمها لبوابة الاعتماد.
            </p>

            <h3 style="font-size: 1.15rem; margin-top: 1rem; margin-bottom: 0.5rem;">عقد حسابات تحليل القيمة المكتسبة (PMO-06.05 EVA)</h3>
            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>المؤشر المالي</th>
                    <th>المعادلة القياسية</th>
                    <th>قاعدة التقريب الحتمية المعتمدة</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>تباين الجدول الزمني (SV)</strong></td>
                    <td><code>SV = EV - PV</code></td>
                    <td>تطابق عشري دقيق للعملة (نسبة تفاوت ± 0.01)</td>
                  </tr>
                  <tr>
                    <td><strong>تباين التكلفة (CV)</strong></td>
                    <td><code>CV = EV - AC</code></td>
                    <td>تطابق عشري دقيق للعملة (نسبة تفاوت ± 0.01)</td>
                  </tr>
                  <tr>
                    <td><strong>مؤشر أداء الجدول (SPI)</strong></td>
                    <td><code>SPI = EV / PV</code></td>
                    <td>تقريب نصف لأعلى إلى خانتين عشريتين (قيمة 0.0 عند انعدام PV)</td>
                  </tr>
                  <tr>
                    <td><strong>مؤشر أداء التكلفة (CPI)</strong></td>
                    <td><code>CPI = EV / AC</code></td>
                    <td>تقريب نصف لأعلى إلى خانتين عشريتين (قيمة 0.0 عند انعدام AC)</td>
                  </tr>
                  <tr>
                    <td><strong>التقدير عند الاكتمال (EAC)</strong></td>
                    <td><code>EAC = BAC / CPI</code></td>
                    <td>تقريب نصف لأعلى إلى خانتين عشريتين</td>
                  </tr>
                  <tr>
                    <td><strong>مؤشر الأداء المتبقي (TCPI)</strong></td>
                    <td><code>TCPI = (BAC - EV) / (BAC - AC)</code></td>
                    <td>تقريب نصف لأعلى إلى خانتين عشريتين</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 1rem; line-height: 1.7;">
              عند توليد تقارير القيمة المكتسبة عبر الوكلاء الأذكياء، يستدعي خط الأنابيب الأداة المعتمدة 
              <code>tools/attested_computations/eva_calculator.py</code> لإنتاج الحقائق الرياضية بدقة متناهية، 
              وتقوم أداة التدقيق <code>eva_attester.py</code> بالتحقق التام من مطابقة الأرقام في المستند للحقائق الرياضية قبل الاعتماد المؤسسي.
            </p>
          </section>

        </div>
      </div>
    </div>
    """

    return render_html_page(
        title="مرجع المطورين وهندسة الذكاء الاصطناعي",
        content=content,
        lang="ar",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/developers/",
    )
