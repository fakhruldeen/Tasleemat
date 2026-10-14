"""tools/site_builder/pages_developers.py
Comprehensive Developers, Engineering & AI Integration Guide for Tasleemat (English & Arabic).
Generates:
1. Developers Hub (/developers/ & /ar/developers/) with architecture map and sub-module navigation
2. CLI Tooling & Scaffolding Sub-Page (/developers/cli/ & /ar/developers/cli/)
3. Python SDK & Core Architecture Sub-Page (/developers/sdk/ & /ar/developers/sdk/)
4. Model Context Protocol (MCP) Server Sub-Page (/developers/mcp/ & /ar/developers/mcp/)
5. JSON Schemas & Autonomous Healing Sub-Page (/developers/schemas/ & /ar/developers/schemas/)
6. Agentic Swarms, CI/CD & Attested Math Sub-Page (/developers/agentic/ & /ar/developers/agentic/)
"""

from tools.site_builder.theme import render_html_page


def _render_dev_subnav(active_slug: str, lang: str, base_url: str) -> str:
    """Renders the top subnav bar or sidebar navigation across developer pages."""
    is_ar = lang == "ar"
    prefix = f"{base_url}/ar/developers" if is_ar else f"{base_url}/developers"

    pages = [
        {"slug": "hub", "en": "📖 Developers Hub", "ar": "📖 بوابة المطورين", "url": f"{prefix}/"},
        {"slug": "cli", "en": "⌨️ CLI Tooling", "ar": "⌨️ أداة الطرفية (CLI)", "url": f"{prefix}/cli/"},
        {"slug": "sdk", "en": "🐍 Python SDK", "ar": "🐍 مكتبة بايثون (SDK)", "url": f"{prefix}/sdk/"},
        {"slug": "mcp", "en": "🔌 MCP Server", "ar": "🔌 خادم بروتوكول MCP", "url": f"{prefix}/mcp/"},
        {"slug": "schemas", "en": "📐 Schemas & Validation", "ar": "📐 المخططات والتحقق", "url": f"{prefix}/schemas/"},
        {"slug": "agentic", "en": "🤖 Agentic Swarms & CI/CD", "ar": "🤖 أسراب الوكلاء و CI/CD", "url": f"{prefix}/agentic/"},
    ]

    links = []
    for p in pages:
        is_active = p["slug"] == active_slug
        active_class = "active" if is_active else ""
        title = p["ar" if is_ar else "en"]
        links.append(f'<a href="{p["url"]}" class="btn-utility {active_class}" style="font-size: 0.82rem; padding: 0.35rem 0.75rem; {"background: var(--accent-blue); color: #fff; border-color: var(--accent-blue);" if is_active else ""}">{title}</a>')

    return f"""
    <div style="background: var(--bg-card); border-bottom: 1px solid var(--border-color); padding: 0.75rem 0; margin-bottom: 2rem;">
      <div class="container" style="display: flex; gap: 0.5rem; flex-wrap: wrap; align-items: center;">
        <span style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted); margin-right: 0.5rem; text-transform: uppercase;">
          {"Sections:" if not is_ar else "الأقسام الفنية:"}
        </span>
        {"".join(links)}
      </div>
    </div>
    """


# ==============================================================================
# 1. DEVELOPERS HUB (EN & AR)
# ==============================================================================

def generate_developers_hub_en(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("hub", "en", base_url)
    
    content = f"""
    <section class="hero-section" style="padding: 3.5rem 0 2.5rem;">
      <div class="container">
        <div class="hero-pill">
          <span>⚙️ Enterprise Engineering &amp; AI Automation Manual</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.35rem; margin-top: 0.75rem;">Developers &amp; AI Integration Hub</h1>
        <p class="hero-subtitle" style="max-width: 820px; margin: 0 auto; line-height: 1.7;">
          The authoritative technical portal for software engineers, AI architects, and DevOps leads.
          Integrate Tasleemat across Python applications, CLI automation pipelines, Model Context Protocol (MCP) servers,
          and autonomous multi-agent orchestration swarms.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-top: 1rem; margin-bottom: 5rem;">
      
      <!-- Modular Documentation Sub-Pages Grid -->
      <div style="margin-bottom: 3.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">
          📚 Dedicated Technical Guides &amp; Modules
        </h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
          
          <a href="{base_url}/developers/cli/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid var(--accent-blue); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⌨️</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">CLI Tooling &amp; Scaffolding</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">
                Deep dive into <code>tasleemat init</code>, <code>list</code>, <code>search</code>, <code>config</code>, <code>generate</code>, and <code>test</code>. Interactive wizards, flags, and bash automation recipes.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-blue); font-size: 0.85rem; margin-top: 1rem;">View CLI Manual &rarr;</div>
          </a>

          <a href="{base_url}/developers/sdk/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid var(--accent-emerald); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🐍</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">Python SDK &amp; Core Architecture</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">
                All 8 verified pure-Python functions, data models (<code>ArtifactSummary</code>, <code>ArtifactAssets</code>), exception hierarchy, and runtime document synthesis.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-emerald); font-size: 0.85rem; margin-top: 1rem;">View SDK Reference &rarr;</div>
          </a>

          <a href="{base_url}/developers/mcp/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid var(--accent-amber); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🔌</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">Model Context Protocol (MCP)</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">
                JSON-RPC 2.0 stdio server connecting Claude Desktop, Cursor, and Antigravity directly to the 114 deliverables, schemas, and tailoring engine.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-amber); font-size: 0.85rem; margin-top: 1rem;">View MCP Integration &rarr;</div>
          </a>

          <a href="{base_url}/developers/schemas/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid #8b5cf6; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📐</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">Draft 2020-12 &amp; Self-Correction</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">
                114 companion JSON schemas, RFC 3339/4122/3986 format validation, and the autonomous iterative feedback healing loop for LLMs.
              </p>
            </div>
            <div style="font-weight: 700; color: #8b5cf6; font-size: 0.85rem; margin-top: 1rem;">View Schemas &amp; Self-Correction &rarr;</div>
          </a>

          <a href="{base_url}/developers/agentic/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid #ec4899; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🤖</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">Agentic Swarms &amp; CI/CD</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">
                Multi-agent PMO personas (CrewAI, LangGraph), <code>tasleemat.ai.AIClient</code> synthesis, headless GitHub Actions quality gates, and EVA math contracts.
              </p>
            </div>
            <div style="font-weight: 700; color: #ec4899; font-size: 0.85rem; margin-top: 1rem;">View Agentic &amp; CI/CD Guide &rarr;</div>
          </a>

        </div>
      </div>

      <!-- Quick Installation & Architecture Overview -->
      <section id="quickstart" class="card" style="padding: 2.25rem; margin-bottom: 3rem;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
          <h2 style="font-size: 1.55rem; margin: 0;">1. Quick Installation &amp; Environment Prerequisites</h2>
          <span class="badge" style="background: var(--accent-blue-bg); color: var(--accent-blue); border: 1px solid var(--accent-blue-border); font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">PyPI: tasleemat</span>
        </div>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Tasleemat is distributed as a zero-dependency, pure-Python package on PyPI, supporting Python <strong>3.9, 3.10, 3.11, 3.12, and 3.13</strong>. 
          The core distribution packages all 114 bilingual deliverable templates, JSON companion schemas, CSV data dictionaries, 
          CLI commands, and the Model Context Protocol (MCP) server.
        </p>
        <pre><code># Install from PyPI
pip install tasleemat

# Verify both CLI and MCP executables
tasleemat --version
tasleemat-mcp --help</code></pre>
      </section>

      <!-- Architecture Flowchart -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 3rem;">
        <h3 style="font-size: 1.35rem; margin-bottom: 0.5rem; color: var(--text-main);">
          🏛️ Tasleemat Architectural Blueprint
        </h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 1.5rem;">
          How developer tools, MCP servers, and autonomous agents interact with the canonical forms catalog and validation contracts:
        </p>
        <pre><code class="language-mermaid">
flowchart TD
    subgraph Clients["Engineering &amp; AI Clients"]
        CLI["Terminal CLI (tasleemat)"]
        SDK["Python Application (tasleemat SDK)"]
        MCP["AI IDE (Claude Desktop, Cursor, Antigravity)"]
        Swarm["Autonomous Agent Swarm (LangGraph, CrewAI)"]
    end

    subgraph Core["Core Engine (tasleemat v2.5.0.post1)"]
        Catalog["Catalog &amp; Asset Resolver"]
        Tailoring["Tailoring Engine (Tiers 1-3, 5 Packs)"]
        Validator["Draft 2020-12 Schema Validator"]
        Attester["Attested Math Engine (EVA PMO-06.05)"]
    end

    subgraph Data["Canonical Immutability Core"]
        Forms["114 Deliverables (EN &amp; AR)"]
        Schemas["114 Draft 2020-12 Schemas"]
        Dicts["114 CSV Dictionaries"]
    end

    CLI --> Catalog
    SDK --> Catalog
    MCP --> Catalog
    Swarm --> Validator

    Catalog --> Tailoring
    Tailoring --> Forms
    Validator --> Schemas
    Attester --> Forms
        </code></pre>
      </div>

      <!-- Executive Summaries for Existing Anchor Links -->
      <div style="display: flex; flex-direction: column; gap: 2.5rem;">
        
        <section id="cli" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">2. CLI Command Reference</h3>
            <a href="{base_url}/developers/cli/" class="btn-utility" style="font-size: 0.85rem;">Dedicated CLI Page &rarr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">
            Scaffold customized workspaces (<code>tasleemat init</code>), search across English and Arabic deliverables (<code>tasleemat search</code>), 
            configure LLM credentials securely (<code>tasleemat config</code>), synthesize draft documents (<code>tasleemat generate</code>), 
            and run internal acceptance test suites (<code>tasleemat test</code>).
          </p>
          <pre><code>tasleemat init --tier 2 --pack agile --lang ar --code "PRJ-CLOUD" --name "مشروع السحابة" --out ./prj</code></pre>
        </section>

        <section id="sdk" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">3. Python SDK Core Architecture</h3>
            <a href="{base_url}/developers/sdk/" class="btn-utility" style="font-size: 0.85rem;">Dedicated SDK Page &rarr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">
            Pure-Python API exporting 8 verified functions: <code>list_artifacts</code>, <code>get_artifact_definition</code>, 
            <code>get_artifact_assets</code>, <code>get_artifact_asset</code>, <code>get_tailoring_profile</code>, 
            <code>validate_artifact_data</code>, <code>get_lexicon</code>, and <code>render_artifact</code>.
          </p>
          <pre><code>import tasleemat
profile = tasleemat.get_tailoring_profile(tier=2, pack="agile")
report = tasleemat.validate_artifact_data("PMO-03.01", {{"project_id": "PRJ-01"}}, mode="draft")</code></pre>
        </section>

        <section id="mcp" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">4. Model Context Protocol (MCP) Server</h3>
            <a href="{base_url}/developers/mcp/" class="btn-utility" style="font-size: 0.85rem;">Dedicated MCP Page &rarr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">
            Standard JSON-RPC 2.0 stdio server providing 6 specialized tools for Claude Desktop, Cursor, and AI agents:
            <code>tasleemat_list_forms</code>, <code>tasleemat_get_form</code>, <code>tasleemat_get_schema</code>, 
            <code>tasleemat_validate</code>, <code>tasleemat_tailor_project</code>, and <code>tasleemat_calculate_eva</code>.
          </p>
          <pre><code># Run standalone MCP server
tasleemat-mcp</code></pre>
        </section>

        <section id="schemas" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">5. JSON Schemas &amp; RFC Formats</h3>
            <a href="{base_url}/developers/schemas/" class="btn-utility" style="font-size: 0.85rem;">Dedicated Schemas Page &rarr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">
            All 114 deliverables feature companion JSON schemas conforming strictly to <strong>JSON Schema Draft 2020-12</strong>.
            Enforces strict format validations for RFC 3339 (dates/timestamps), RFC 4122 (UUIDs), RFC 3986 (URIs), and RFC 5322 (emails).
          </p>
        </section>

        <section id="self-correction" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">6. The Autonomous Agent Self-Correction Loop</h3>
            <a href="{base_url}/developers/schemas/#self-correction" class="btn-utility" style="font-size: 0.85rem;">Read Self-Correction Guide &rarr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">
            Autonomous agents don't guess: when LLMs generate invalid JSON or markdown tables, <code>tasleemat.validate_artifact_data</code> 
            returns exact JSON path errors. The agent incorporates the error message into its subsequent prompt to heal the output automatically.
          </p>
        </section>

        <section id="multi-agent" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">7. Multi-Agent PMO Swarm Architecture</h3>
            <a href="{base_url}/developers/agentic/#multi-agent" class="btn-utility" style="font-size: 0.85rem;">Read Multi-Agent Guide &rarr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">
            Orchestrate specialized AI personas (Project Manager, PMO Governance Auditor, Risk &amp; Ethics Lead, Executive Sponsor) 
            using CrewAI or LangGraph while maintaining strict human-in-the-loop review boundaries before formal stage gates.
          </p>
        </section>

        <section id="llm-client" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">8. Programmatic AI Synthesis with <code>tasleemat.ai.AIClient</code></h3>
            <a href="{base_url}/developers/agentic/#llm-client" class="btn-utility" style="font-size: 0.85rem;">Read AIClient Reference &rarr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">
            Use the unified <code>tasleemat.ai.AIClient</code> interface to synthesize deliverables across Google Gemini, OpenAI GPT-4o, 
            Anthropic Claude, and DeepSeek with standardized prompt assembly.
          </p>
        </section>

        <section id="cicd" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">9. Headless CI/CD Automation &amp; Quality Gates</h3>
            <a href="{base_url}/developers/agentic/#cicd" class="btn-utility" style="font-size: 0.85rem;">Read CI/CD Guide &rarr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">
            Integrate Tasleemat into GitHub Actions or GitLab CI to automatically enforce deliverable completeness, schema validity, 
            and bilingual consistency on every commit or pull request.
          </p>
        </section>

        <section id="attested-math" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">10. Attested Computations &amp; Deterministic Math Contracts (PMO-06.05)</h3>
            <a href="{base_url}/developers/agentic/#attested-math" class="btn-utility" style="font-size: 0.85rem;">Read Math Contracts &rarr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">
            AI models hallucinate mathematical figures. Tasleemat enforces deterministic calculation engines for Earned Value Analysis 
            (<code>PMO-06.05</code>) and Risk Severity matrices so project metrics remain mathematically attested.
          </p>
        </section>

      </div>

    </div>
    """

    return render_html_page(
        title="Developers & AI Integration Hub",
        content=content,
        lang="en",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/developers/",
        description="Comprehensive Developer & AI Engineering Portal for Tasleemat: CLI, Python SDK, MCP Server, Draft 2020-12 Schemas, and Agentic Swarms.",
        canonical_url="https://fakhr.me/Tasleemat/developers/",
    )


def generate_developers_hub_ar(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("hub", "ar", base_url)
    
    content = f"""
    <section class="hero-section" style="padding: 3.5rem 0 2.5rem;">
      <div class="container">
        <div class="hero-pill">
          <span>⚙️ الدليل الهندسي وتكامل الذكاء الاصطناعي المؤسسي</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.35rem; margin-top: 0.75rem;">بوابة المطورين وهندسة الذكاء الاصطناعي</h1>
        <p class="hero-subtitle" style="max-width: 820px; margin: 0 auto; line-height: 1.8;">
          المرجع التقني الشامل لمهندسي البرمجيات، معماريي الذكاء الاصطناعي، ومسؤولي عمليات DevOps.
          دليل برمجي متكامل لربط تسليمات عبر مكتبة بايثون، أدوات سطر الأوامر (CLI)، خادم بروتوكول سياق النماذج (MCP)،
          وأسراب الوكلاء الأذكياء متعددي المهام (Multi-Agent Swarms).
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-top: 1rem; margin-bottom: 5rem;">
      
      <!-- Modular Documentation Sub-Pages Grid AR -->
      <div style="margin-bottom: 3.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">
          📚 الأدلة الفنية المتخصصة والأقسام التفصيلية
        </h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
          
          <a href="{base_url}/ar/developers/cli/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid var(--accent-blue); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⌨️</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">أداة سطر الأوامر (CLI)</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
                شرح شامل لأوامر <code>tasleemat init</code> و <code>list</code> و <code>search</code> و <code>config</code> و <code>generate</code> و <code>test</code>. معالجات تفاعلية ونصوص أتمتة برمجية.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-blue); font-size: 0.85rem; margin-top: 1rem;">عرض دليل CLI التفصيلي &larr;</div>
          </a>

          <a href="{base_url}/ar/developers/sdk/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid var(--accent-emerald); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🐍</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">مكتبة بايثون والمعمارية البرمجية (SDK)</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
                كافة الدوال البرمجية الـ 8 المعتمدة، نماذج البيانات (<code>ArtifactSummary</code>, <code>ArtifactAssets</code>)، هيكل الاستثناءات، والتوليد البرمجي للوثائق.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-emerald); font-size: 0.85rem; margin-top: 1rem;">عرض مرجع SDK البرمجي &larr;</div>
          </a>

          <a href="{base_url}/ar/developers/mcp/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid var(--accent-amber); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🔌</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">خادم بروتوكول سياق النموذج (MCP)</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
                خادم JSON-RPC 2.0 stdio قياسي لربط Claude Desktop و Cursor و Antigravity مباشرة بكتالوج الـ 114 تسليمة ومخططاتها ومحرك التخصيص.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-amber); font-size: 0.85rem; margin-top: 1rem;">عرض دليل تكامل MCP &larr;</div>
          </a>

          <a href="{base_url}/ar/developers/schemas/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid #8b5cf6; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📐</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">المخططات والتصحيح الذاتي للوكلاء</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
                114 مخطط JSON متوافق مع Draft 2020-12، التحقق من معايير RFC، وحلقة التغذية الراجعة التلقائية لإصلاح أخطاء النماذج اللغوية.
              </p>
            </div>
            <div style="font-weight: 700; color: #8b5cf6; font-size: 0.85rem; margin-top: 1rem;">عرض المخططات والتصحيح الذاتي &larr;</div>
          </a>

          <a href="{base_url}/ar/developers/agentic/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid #ec4899; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🤖</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">أسراب الوكلاء وبوابات CI/CD</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
                شخصيات مكتب إدارة المشاريع (CrewAI, LangGraph)، محرك <code>tasleemat.ai.AIClient</code>، بوابات GitHub Actions، وعقود الحسابات الرياضية الموثقة لـ EVA.
              </p>
            </div>
            <div style="font-weight: 700; color: #ec4899; font-size: 0.85rem; margin-top: 1rem;">عرض دليل الوكلاء والأتمتة &larr;</div>
          </a>

        </div>
      </div>

      <!-- Quick Installation & Architecture Overview AR -->
      <section id="quickstart" class="card" style="padding: 2.25rem; margin-bottom: 3rem;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
          <h2 style="font-size: 1.55rem; margin: 0;">1. التثبيت السريع ومتطلبات البيئة</h2>
          <span class="badge" style="background: var(--accent-blue-bg); color: var(--accent-blue); border: 1px solid var(--accent-blue-border); font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">مستودع PyPI الرسمي</span>
        </div>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          حزمة <code>tasleemat</code> منشورة رسميًا عبر مستودع PyPI العام كحزمة بايثون نقية تدعم إصدارات بايثون <strong>3.9 و 3.10 و 3.11 و 3.12 و 3.13</strong>.
          تحتوي الحزمة الموزعة على كافة قوالب التسليمات الـ 114 باللغتين، مخططات JSON المرافقة، قواميس الحقول، أداة سطر الأوامر، وخادم بروتوكول MCP.
        </p>
        <pre style="direction: ltr; text-align: left;"><code># التثبيت المباشر عبر مدير الحزم pip
pip install tasleemat

# التحقق من جاهزية أداة الطرفية وخادم بروتوكول سياق النموذج (MCP):
tasleemat --version
tasleemat-mcp --help</code></pre>
      </section>

      <!-- Architecture Flowchart AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 3rem;">
        <h3 style="font-size: 1.35rem; margin-bottom: 0.5rem; color: var(--text-main);">
          🏛️ المخطط المعماري لمنظومة تسليمات
        </h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 1.5rem;">
          كيف تتكامل أدوات المطورين، وخوادم MCP، والوكلاء الأذكياء مع كتالوج التسليمات وعقود التحقق:
        </p>
        <pre><code class="language-mermaid">
flowchart TD
    subgraph Clients["أدوات وتطبيقات المطورين والذكاء الاصطناعي"]
        CLI["أداة سطر الأوامر (tasleemat CLI)"]
        SDK["تطبيق بايثون (tasleemat SDK)"]
        MCP["بيئات الذكاء الاصطناعي (Claude Desktop, Cursor)"]
        Swarm["أسراب الوكلاء الأذكياء (LangGraph, CrewAI)"]
    end

    subgraph Core["محرك تسليمات الأساسي (v2.5.0.post1)"]
        Catalog["مستكشف الكتالوج والأصول"]
        Tailoring["محرك التخصيص (3 مستويات و5 حزم)"]
        Validator["محرك التحقق من مخططات Draft 2020-12"]
        Attester["محرك الحسابات الرياضية الموثقة (EVA PMO-06.05)"]
    end

    subgraph Data["الأصول المعيارية المحمية"]
        Forms["114 تسليمة (عربي وإنجليزي)"]
        Schemas["114 مخطط JSON معتمد"]
        Dicts["114 قاموس حقول CSV"]
    end

    CLI --> Catalog
    SDK --> Catalog
    MCP --> Catalog
    Swarm --> Validator

    Catalog --> Tailoring
    Tailoring --> Forms
    Validator --> Schemas
    Attester --> Forms
        </code></pre>
      </div>

      <!-- Executive Summaries for Existing Anchor Links AR -->
      <div style="display: flex; flex-direction: column; gap: 2.5rem;">
        
        <section id="cli" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">2. مرجع أوامر الطرفية (CLI)</h3>
            <a href="{base_url}/ar/developers/cli/" class="btn-utility" style="font-size: 0.85rem;">الانتقال لدليل CLI الكامل &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            إنشاء مجلدات المشاريع المخصصة (<code>tasleemat init</code>)، البحث السريع في التسليمات باللغتين العربية والإنجليزية (<code>tasleemat search</code>)، 
            إعداد مفاتيح نماذج الذكاء الاصطناعي بأمان (<code>tasleemat config</code>)، توليد مسودات التسليمات (<code>tasleemat generate</code>)، 
            وتشغيل حزمة الاختبارات الآلية الداخلية (<code>tasleemat test</code>).
          </p>
          <pre style="direction: ltr; text-align: left;"><code>tasleemat init --tier 2 --pack agile --lang ar --code "PRJ-CLOUD" --name "منصة التحول الرقمي" --out ./prj</code></pre>
        </section>

        <section id="sdk" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">3. معمارية مكتبة بايثون (SDK)</h3>
            <a href="{base_url}/ar/developers/sdk/" class="btn-utility" style="font-size: 0.85rem;">الانتقال لمرجع SDK البرمجي &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            واجهة برمجية ناصعة بلغة بايثون تصدر 8 دوال معتمدة: <code>list_artifacts</code> و <code>get_artifact_definition</code> و 
            <code>get_artifact_assets</code> و <code>get_artifact_asset</code> و <code>get_tailoring_profile</code> و 
            <code>validate_artifact_data</code> و <code>get_lexicon</code> و <code>render_artifact</code>.
          </p>
          <pre style="direction: ltr; text-align: left;"><code>import tasleemat
profile = tasleemat.get_tailoring_profile(tier=2, pack="agile")
report = tasleemat.validate_artifact_data("PMO-03.01", {{"project_id": "PRJ-01"}}, mode="draft")</code></pre>
        </section>

        <section id="mcp" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">4. بروتوكول سياق النماذج (MCP)</h3>
            <a href="{base_url}/ar/developers/mcp/" class="btn-utility" style="font-size: 0.85rem;">الانتقال لدليل MCP &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            خادم JSON-RPC 2.0 stdio يوفر 6 أدوات متخصصة لمساعدي الذكاء الاصطناعي:
            <code>tasleemat_list_forms</code> و <code>tasleemat_get_form</code> و <code>tasleemat_get_schema</code> و 
            <code>tasleemat_validate</code> و <code>tasleemat_tailor_project</code> و <code>tasleemat_calculate_eva</code>.
          </p>
          <pre style="direction: ltr; text-align: left;"><code># تشغيل خادم MCP القياسي
tasleemat-mcp</code></pre>
        </section>

        <section id="schemas" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">5. مخططات JSON ومعايير RFC</h3>
            <a href="{base_url}/ar/developers/schemas/" class="btn-utility" style="font-size: 0.85rem;">الانتقال لدليل المخططات &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            تتضمن كافة التسليمات الـ 114 مخططات JSON مرافقة متوافقة تماماً مع معيار <strong>JSON Schema Draft 2020-12</strong>.
            وتفرض قيوداً صارمة على صيغ التواريخ (RFC 3339)، المعرفات الفريدة (RFC 4122)، الروابط (RFC 3986)، والبريد الإلكتروني (RFC 5322).
          </p>
        </section>

        <section id="self-correction" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">6. حلقة التصحيح الذاتي التلقائي للوكلاء</h3>
            <a href="{base_url}/ar/developers/schemas/#self-correction" class="btn-utility" style="font-size: 0.85rem;">قراءة دليل التصحيح الذاتي &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            لا يعتمد الوكلاء على التخمين: عند قيام النماذج بتوليد بيانات غير مطابقة للمخطط، تقوم دالة <code>tasleemat.validate_artifact_data</code> 
            بإرجاع تفاصيل الخطأ بدقة، ليقوم الوكيل بدمجه في سياق النموذج وإعادة التوليد تلقائياً حتى تصبح الوثيقة صالحة برمجياً.
          </p>
        </section>

        <section id="multi-agent" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">7. أسراب الوكلاء المتعددين لمكتب إدارة المشاريع</h3>
            <a href="{base_url}/ar/developers/agentic/#multi-agent" class="btn-utility" style="font-size: 0.85rem;">قراءة دليل أسراب الوكلاء &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            تنسيق شخصيات الذكاء الاصطناعي المتخصصة (مدير المشروع، مدقق الحوكمة، مسؤول المخاطر والأخلاقيات، الراعي التنفيذي) 
            باستخدام CrewAI أو LangGraph مع الحفاظ الصارم على حدود المراجعة والاعتماد البشري قبل بوابات المراحل.
          </p>
        </section>

        <section id="llm-client" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">8. التوليد البرمجي عبر <code>tasleemat.ai.AIClient</code></h3>
            <a href="{base_url}/ar/developers/agentic/#llm-client" class="btn-utility" style="font-size: 0.85rem;">قراءة مرجع AIClient &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            استخدام واجهة <code>tasleemat.ai.AIClient</code> الموحدة لتوليد مسودات الوثائق عبر Google Gemini و OpenAI GPT-4o 
            و Anthropic Claude و DeepSeek مع بناء وتجميع موحد للأوامر.
          </p>
        </section>

        <section id="cicd" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">9. خطوط CI/CD وبوابات الجودة الآلية</h3>
            <a href="{base_url}/ar/developers/agentic/#cicd" class="btn-utility" style="font-size: 0.85rem;">قراءة دليل CI/CD &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            دمج تسليمات في GitHub Actions أو GitLab CI لفرض اكتمال التسليمات وصحة المخططات والاتساق ثنائي اللغة آلياً مع كل إيداع برمجي (commit) أو طلب دمج (PR).
          </p>
        </section>

        <section id="attested-math" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">10. عقود الحسابات الرياضية الموثقة (PMO-06.05)</h3>
            <a href="{base_url}/ar/developers/agentic/#attested-math" class="btn-utility" style="font-size: 0.85rem;">قراءة عقود الحسابات &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            تتعرض النماذج اللغوية للهلوسة في الحسابات الدقيقة؛ لذلك يفرض إطار تسليمات محركات حسابية حتمية لتحليل القيمة المكتسبة (EVA في <code>PMO-06.05</code>) 
            ومصفوفات شدة المخاطر لضمان موثوقية المقاييس رياضياً.
          </p>
        </section>

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
        description="بوابة المطورين وهندسة الذكاء الاصطناعي لمنظومة تسليمات: أداة الطرفية CLI، مكتبة بايثون SDK، خادم MCP، مخططات JSON، وأسراب الوكلاء الأذكياء.",
        canonical_url="https://fakhr.me/Tasleemat/ar/developers/",
    )


# ==============================================================================
# 2. SUB-PAGE: CLI TOOLING & SCAFFOLDING
# ==============================================================================

def generate_dev_cli_en(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("cli", "en", base_url)
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/">Home</a> &gt; 
          <a href="{base_url}/developers/">Developers &amp; AI</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">CLI Tooling</span>
        </nav>
        <div class="hero-pill"><span>⌨️ Command Line Executable</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">CLI Tooling &amp; Scaffolding Reference</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto;">
          The authoritative command-line interface (<code>tasleemat</code>) for terminal automation, interactive workspace scaffolding, catalog querying, and test validation.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Command 1: init -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
          <h2 style="font-size: 1.5rem; margin: 0; color: var(--text-main);">A. Workspace Scaffolding (<code>tasleemat init</code>)</h2>
          <span class="badge" style="background: var(--accent-emerald-bg); color: var(--accent-emerald); font-weight: 700; font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">Primary Tool</span>
        </div>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          The <code>init</code> command creates a complete project folder tailored to your governance tier (Tier 1, 2, or 3) and delivery methodology pack (General, Agile, AI, Predictive, Hybrid). 
          Each deliverable in the profile is pre-scaffolded with its full 5-file bundle: template, authoring guide, realistic example, companion JSON schema, and CSV data dictionary.
        </p>

        <h3 style="font-size: 1.1rem; margin-top: 1.25rem; margin-bottom: 0.5rem;">Interactive Wizard Mode</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 0.5rem;">
          Running without arguments prompts interactively for project code, project name, project manager, sponsor, sizing tier, and language:
        </p>
        <pre><code>tasleemat init</code></pre>

        <h3 style="font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Headless Automation Mode (CLI Flags)</h3>
        <pre><code># Scaffold Tier 2 Agile Project in Arabic
tasleemat init \\
  --tier 2 \\
  --pack agile \\
  --lang ar \\
  --code "PRJ-2026-CLOUD-01" \\
  --name "منصة التحول الرقمي السحابي" \\
  --pm "سارة الأحمد" \\
  --sponsor "د. خالد المنصور" \\
  --out ./workspaces/PRJ-2026-CLOUD-01

# Enterprise Tier 1 Strategic Project in both English and Arabic
tasleemat init \\
  --tier 1 \\
  --pack hybrid \\
  --lang both \\
  --code "PRJ-2026-CORE" \\
  --name "Enterprise Core Banking Migration" \\
  --pm "Tariq Al-Harbi" \\
  --sponsor "Executive VP IT" \\
  --out ./enterprise_workspace</code></pre>

        <div style="margin-top: 1.5rem; background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
          <div style="font-size: 0.85rem; font-weight: 700; margin-bottom: 0.5rem;">Supported CLI Options:</div>
          <ul style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7; padding-left: 1.25rem;">
            <li><code>--tier &lt;1|2|3&gt;</code>: Governance sizing tier (1 = Mega/Strategic, 2 = Standard, 3 = Lean/Fast-track). Default: 2.</li>
            <li><code>--pack &lt;general|agile|ai|predictive|hybrid&gt;</code>: Delivery archetype pack. Default: general.</li>
            <li><code>--lang &lt;en|ar|both&gt;</code>: Target language generation mode. Default: en.</li>
            <li><code>--code &lt;string&gt;</code>: Project code identifier (e.g., PRJ-2026-001).</li>
            <li><code>--name &lt;string&gt;</code>: Formal project title.</li>
            <li><code>--pm &lt;string&gt;</code>: Project Manager name.</li>
            <li><code>--sponsor &lt;string&gt;</code>: Executive Project Sponsor name.</li>
            <li><code>--out &lt;dir&gt;</code>: Destination output directory path.</li>
          </ul>
        </div>
      </div>

      <!-- Command 2: list & search -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">B. Catalog Exploration &amp; Search (<code>tasleemat list</code> &amp; <code>search</code>)</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Query the canonical 114 deliverables catalog directly from the terminal with bilingual support and phase filters.
        </p>
        <pre><code># List all deliverables in English or Arabic
tasleemat list --lang en
tasleemat list --lang ar

# Search by English keyword, Arabic keyword, or deliverable ID
tasleemat search "Risk" --lang en
tasleemat search "ميثاق" --lang ar
tasleemat search "PMO-03.01" --lang en

# Filter deliverables by phase code (00 to 07)
tasleemat list --phase 04</code></pre>
      </div>

      <!-- Command 3: config -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">C. LLM AI Account Configuration (<code>tasleemat config</code>)</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Manage API keys and preferred LLM models for automated document synthesis. Configurations are stored locally in <code>~/.tasleemat/config.json</code> with restrictive file permissions.
        </p>
        <pre><code># Configure Google Gemini
tasleemat config set --provider gemini --model gemini-2.5-flash --key "AIzaSy..."

# Configure OpenAI GPT-4o
tasleemat config set --provider openai --model gpt-4o --key "sk-proj-..."

# Configure Anthropic Claude
tasleemat config set --provider anthropic --model claude-3-5-sonnet-20241022 --key "sk-ant-..."

# Configure local Ollama endpoint (Offline / Air-gapped)
tasleemat config set --provider ollama --model llama3.2 --endpoint "http://localhost:11434"

# Display active configuration (masks confidential tokens)
tasleemat config show</code></pre>
      </div>

      <!-- Command 4: generate -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">D. AI Deliverable Synthesis (<code>tasleemat generate</code>)</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Synthesize draft deliverable markdown files from kickoff meeting notes using configured LLM providers:
        </p>
        <pre><code># Generate Project Charter (PMO-03.01) from raw text notes
tasleemat generate \\
  --form PMO-03.01 \\
  --notes ./meeting_minutes.txt \\
  --lang en \\
  --out ./drafts/Project_Charter.md

# Offline mock mode for CI/CD test pipelines (zero token consumption)
tasleemat generate \\
  --form PMO-03.01 \\
  --notes "Mock project notes" \\
  --mock \\
  --out ./ci_output/Mock_Charter.md</code></pre>
      </div>

      <!-- Command 5: test & mcp -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">E. Automated Test Suite &amp; MCP Launcher (<code>test</code> &amp; <code>mcp</code>)</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Execute internal regression test suites or launch the stdio MCP server directly from the CLI:
        </p>
        <pre><code># Run full regression test suite (140+ unit &amp; integration tests)
tasleemat test -v

# Start the Model Context Protocol stdio server
tasleemat mcp</code></pre>
      </div>

    </div>
    """
    return render_html_page(
        title="CLI Tooling & Scaffolding Reference",
        content=content,
        lang="en",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/developers/cli/",
        description="Comprehensive CLI Tooling & Scaffolding Manual for Tasleemat: init, list, search, config, generate, test, and automated CI/CD recipes.",
        canonical_url="https://fakhr.me/Tasleemat/developers/cli/",
    )


def generate_dev_cli_ar(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("cli", "ar", base_url)
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/ar/">الرئيسية</a> &gt; 
          <a href="{base_url}/ar/developers/">المطورون والذكاء الاصطناعي</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">أداة سطر الأوامر (CLI)</span>
        </nav>
        <div class="hero-pill"><span>⌨️ أداة الطرفية وسطر الأوامر</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">مرجع أداة سطر الأوامر (CLI)</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
          المرجع الرسمي الشامل لأداة الطرفية (<code>tasleemat</code>) لأتمتة إنشاء بيئات عمل المشاريع المخصصة، استعلام الكتالوج، وتوليد الوثائق.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Command 1: init AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
          <h2 style="font-size: 1.5rem; margin: 0; color: var(--text-main);">أ. إنشاء بيئة عمل المشروع (<code>tasleemat init</code>)</h2>
          <span class="badge" style="background: var(--accent-emerald-bg); color: var(--accent-emerald); font-weight: 700; font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">الأداة الرئيسية</span>
        </div>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          يقوم أمر <code>init</code> بإنشاء مجلد متكامل للمشروع مخصص بدقة بحسب مستوى الحوكمة (المستوى 1 أو 2 أو 3) وحزمة المنهجية (العامة، الرشيقة، الذكاء الاصطناعي، التنبؤية، الهجينة).
          يتم تجهيز كل تسليمة معتمدة ضمن الحزمة بحزمتها الخماسية الكاملة: القالب، الدليل الإرشادي، المثال الواقعي، مخطط JSON، وقاموس البيانات CSV.
        </p>

        <h3 style="font-size: 1.1rem; margin-top: 1.25rem; margin-bottom: 0.5rem;">الوضع التفاعلي (Interactive Wizard)</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 0.5rem;">
          تشغيل الأمر بدون وسائط يبدأ معالجاً تفاعلياً يسأل عن رمز المشروع، اسمه، اسم مدير المشروع، الراعي، ومستوى الحوكمة:
        </p>
        <pre style="direction: ltr; text-align: left;"><code>tasleemat init</code></pre>

        <h3 style="font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">وضع الأتمتة المباشر (CLI Flags)</h3>
        <pre style="direction: ltr; text-align: left;"><code># إنشاء مشروع المستوى 2 بمنهجية رشيقة باللغة العربية
tasleemat init \\
  --tier 2 \\
  --pack agile \\
  --lang ar \\
  --code "PRJ-2026-CLOUD-01" \\
  --name "منصة التحول الرقمي السحابي" \\
  --pm "سارة الأحمد" \\
  --sponsor "د. خالد المنصور" \\
  --out ./workspaces/PRJ-2026-CLOUD-01

# مشروع استراتيجي كبير (المستوى 1) باللغتين العربية والإنجليزية
tasleemat init \\
  --tier 1 \\
  --pack hybrid \\
  --lang both \\
  --code "PRJ-2026-CORE" \\
  --name "Enterprise Core Banking Migration" \\
  --pm "Tariq Al-Harbi" \\
  --sponsor "Executive VP IT" \\
  --out ./enterprise_workspace</code></pre>

        <div style="margin-top: 1.5rem; background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
          <div style="font-size: 0.85rem; font-weight: 700; margin-bottom: 0.5rem;">الخيارات المدعومة في الأمر:</div>
          <ul style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.8; padding-right: 1.25rem;">
            <li><code>--tier &lt;1|2|3&gt;</code>: مستوى الحوكمة والحجم (1 = مشاريع كبرى، 2 = قياسية، 3 = رشيقة سريعة). القيمة الافتراضية: 2.</li>
            <li><code>--pack &lt;general|agile|ai|predictive|hybrid&gt;</code>: حزمة منهجية التسليم. القيمة الافتراضية: general.</li>
            <li><code>--lang &lt;en|ar|both&gt;</code>: لغة التسليمات المستهدفة (إنجليزية، عربية، أو كلاهما). القيمة الافتراضية: en.</li>
            <li><code>--code &lt;string&gt;</code>: رمز المشروع التعريفي (مثال: PRJ-2026-001).</li>
            <li><code>--name &lt;string&gt;</code>: الاسم الرسمي للمشروع.</li>
            <li><code>--pm &lt;string&gt;</code>: اسم مدير المشروع.</li>
            <li><code>--sponsor &lt;string&gt;</code>: اسم الراعي التنفيذي للمشروع.</li>
            <li><code>--out &lt;dir&gt;</code>: مسار مجلد الإخراج المستهدف.</li>
          </ul>
        </div>
      </div>

      <!-- Command 2: list & search AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">ب. استعراض والبحث في الكتالوج (<code>tasleemat list</code> &amp; <code>search</code>)</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          الاستعلام المباشر عن التسليمات الـ 114 من سطر الأوامر مع دعم كامل للغتين والفلترة بحسب المرحلة.
        </p>
        <pre style="direction: ltr; text-align: left;"><code># استعراض كافة التسليمات بالعربية أو الإنجليزية
tasleemat list --lang ar
tasleemat list --lang en

# البحث بكلمة مفتاحية بالعربية أو الإنجليزية أو برمز التسليمة
tasleemat search "ميثاق" --lang ar
tasleemat search "Risk" --lang en
tasleemat search "PMO-03.01" --lang en

# فلترة التسليمات بحسب رمز المرحلة (00 إلى 07)
tasleemat list --phase 04</code></pre>
      </div>

      <!-- Command 3: config AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">ج. إعداد حسابات ونماذج الذكاء الاصطناعي (<code>tasleemat config</code>)</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          إدارة مفاتيح API ونماذج الذكاء الاصطناعي المفضلة للتوليد الآلي. يتم حفظ الإعدادات بأمان في المسار المحلي <code>~/.tasleemat/config.json</code>.
        </p>
        <pre style="direction: ltr; text-align: left;"><code># ضبط نموذج Google Gemini
tasleemat config set --provider gemini --model gemini-2.5-flash --key "AIzaSy..."

# ضبط OpenAI GPT-4o
tasleemat config set --provider openai --model gpt-4o --key "sk-proj-..."

# ضبط Anthropic Claude
tasleemat config set --provider anthropic --model claude-3-5-sonnet-20241022 --key "sk-ant-..."

# ضبط خادم محلي منعزل عبر Ollama (دون اتصال بالإنترنت)
tasleemat config set --provider ollama --model llama3.2 --endpoint "http://localhost:11434"

# عرض الإعدادات النشطة الحالية (مع إخفاء المفاتيح السرية)
tasleemat config show</code></pre>
      </div>

      <!-- Command 4: generate AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">د. توليد مسودات التسليمات آلياً (<code>tasleemat generate</code>)</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          توليد مسودات التسليمات بتنسيق Markdown بالاعتماد على ملاحظات الاجتماعات ومخرجات النقاش الأولية:
        </p>
        <pre style="direction: ltr; text-align: left;"><code># توليد ميثاق المشروع (PMO-03.01) من ملف ملاحظات الاجتماع
tasleemat generate \\
  --form PMO-03.01 \\
  --notes ./meeting_minutes.txt \\
  --lang ar \\
  --out ./drafts/Project_Charter.md

# وضع الاختبار التجريبي لخطوط CI/CD دون استهلاك أي رصيد رموز API
tasleemat generate \\
  --form PMO-03.01 \\
  --notes "ملاحظات تجريبية" \\
  --mock \\
  --out ./ci_output/Mock_Charter.md</code></pre>
      </div>

      <!-- Command 5: test & mcp AR -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">هـ. حزمة الاختبارات وتشغيل خادم MCP (<code>test</code> &amp; <code>mcp</code>)</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          تنفيذ كافة الاختبارات الآلية الشاملة أو تشغيل خادم بروتوكول سياق النموذج القياسي:
        </p>
        <pre style="direction: ltr; text-align: left;"><code># تشغيل كامل حزمة الاختبارات الآلية (أكثر من 140 اختباراً)
tasleemat test -v

# تشغيل خادم بروتوكول سياق النموذج (MCP) عبر بروتوكول stdio
tasleemat mcp</code></pre>
      </div>

    </div>
    """
    return render_html_page(
        title="مرجع أداة سطر الأوامر (CLI)",
        content=content,
        lang="ar",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/developers/cli/",
        description="دليل أداة سطر الأوامر (CLI) الشامل لتسليمات: تهيئة المشاريع، استكشاف التسليمات، التوليد الآلي، وإدارة بيئات العمل في أسطر الأوامر.",
        canonical_url="https://fakhr.me/Tasleemat/ar/developers/cli/",
    )


# ==============================================================================
# 3. SUB-PAGE: PYTHON SDK & CORE ARCHITECTURE
# ==============================================================================

def generate_dev_sdk_en(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("sdk", "en", base_url)
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/">Home</a> &gt; 
          <a href="{base_url}/developers/">Developers &amp; AI</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">Python SDK</span>
        </nav>
        <div class="hero-pill"><span>🐍 Pure Python Library</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">Python SDK &amp; Core Architecture</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto;">
          Complete programmatic API reference for catalog discovery, tailored workspace generation, Draft 2020-12 validation, and report rendering.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- SDK Functions Table -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">The 8 Verified Core Functions</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.5rem;">
          The top-level <code>tasleemat</code> module exports 8 zero-dependency functions designed for production PMO automation pipelines:
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
                <td>Discovers summary objects for all 114 deliverables or tailored subsets with cryptographic SHA-256 fingerprints.</td>
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
                <td><code>tier: Union[int, str], pack: str='general'</code></td>
                <td><code>List[str]</code></td>
                <td>Returns the verified list of mandatory deliverable codes matching governance tier (1, 2, 3) and methodology pack.</td>
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
      </div>

      <!-- Data Models Card -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">Data Models &amp; Type Classes</h2>
        
        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;"><code>ArtifactSummary</code></h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 0.75rem;">Represents high-level deliverable metadata returned by <code>list_artifacts()</code>:</p>
        <pre><code>@dataclass(frozen=True)
class ArtifactSummary:
    artifact_id: str       # e.g. "PMO-03.01"
    prefix: str            # e.g. "03_01"
    name_en: str           # e.g. "Project Charter"
    name_ar: str           # e.g. "ميثاق المشروع"
    phase_code: str        # e.g. "03"
    phase_name_en: str     # e.g. "Initiating"
    phase_name_ar: str     # e.g. "البدء والترخيص"
    tiers: List[str]       # e.g. ["1", "2", "3"]
    fingerprint: str       # SHA-256 hash of immutable source form
    completed_data_validation: dict</code></pre>

        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;"><code>ValidationReport</code> &amp; <code>ValidationError</code></h3>
        <pre><code>@dataclass
class ValidationReport:
    valid: bool                         # True if payload satisfies all schema constraints
    errors: List[ValidationError]       # List of structured validation errors
    schema_id: str                      # Canonical URI of the schema
    schema_dialect: str                 # "https://json-schema.org/draft/2020-12/schema"
    fingerprint: str                    # SHA-256 fingerprint of the schema

@dataclass
class ValidationError:
    path: str                           # JSON Pointer / property path (e.g. "/budget/total")
    message: str                        # Human-readable failure explanation
    keyword: str                        # Violated keyword (e.g. "required", "format")
    schema_path: str                    # Path inside the schema where rule was defined</code></pre>
      </div>

      <!-- Real-World Python Script Card -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">Complete Working Python Example</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          The following script demonstrates discovering tailored deliverables, loading asset templates, validating structured data, and rendering HTML output:
        </p>
        <pre><code>import tasleemat

# 1. Resolve tailored deliverable bundle for a Tier 2 Agile Project
tailored_ids = tasleemat.get_tailoring_profile(tier=2, pack="agile")
print(f"Tailored deliverable count: {{len(tailored_ids)}}")

# 2. Inspect specific deliverable definition and assets
art_id = "PMO-03.01"  # Project Charter
meta = tasleemat.get_artifact_definition(art_id)
print(f"Deliverable: {{meta['name_en']}} / {{meta['name_ar']}}")

assets = tasleemat.get_artifact_assets(art_id, lang="en")
template_text = assets.get_template_content()
schema_data = assets.get_schema_data()

# 3. Validate a structured charter payload against Draft 2020-12 schema
payload = {{
    "project_id": "PRJ-2026-CLOUD",
    "project_name": "Cloud Transformation Platform",
    "sponsor": "Executive VP Operations",
    "project_manager": "Sarah Al-Ahmad",
    "authorization_date": "2026-10-15"
}}

report = tasleemat.validate_artifact_data(art_id, payload, mode="strict")
if report.valid:
    print("Payload conforms 100% to Draft 2020-12 schema!")
else:
    for err in report.errors:
        print(f"Schema Error at {{err.path}}: {{err.message}}")</code></pre>
      </div>

    </div>
    """
    return render_html_page(
        title="Python SDK & Core Architecture Reference",
        content=content,
        lang="en",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/developers/sdk/",
        description="Python SDK Reference for Tasleemat: 8 core API functions, ArtifactSummary models, Draft 2020-12 validation, and headless report rendering.",
        canonical_url="https://fakhr.me/Tasleemat/developers/sdk/",
    )


def generate_dev_sdk_ar(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("sdk", "ar", base_url)
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/ar/">الرئيسية</a> &gt; 
          <a href="{base_url}/ar/developers/">المطورون والذكاء الاصطناعي</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">مكتبة بايثون (SDK)</span>
        </nav>
        <div class="hero-pill"><span>🐍 مكتبة بايثون البرمجية</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">معمارية مكتبة بايثون والمرجع البرمجي</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
          المرجع البرمجي الكامل لاستكشاف الكتالوج، توليد بيئات العمل المخصصة، التحقق وفق Draft 2020-12، وتصيير الوثائق.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- SDK Functions Table AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">الدوال البرمجية الأساسية الثمانية (8 Core Functions)</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.5rem;">
          تصدر مكتبة <code>tasleemat</code> في المستوى الأعلى 8 دوال نقية بدون أي اعتماديات خارجية مخصصة لخطوط الإنتاج البرمجية:
        </p>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>الدالة البرمجية</th>
                <th>المعاملات</th>
                <th>النوع المُرجع</th>
                <th>الوصف الفني</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>list_artifacts()</code></td>
                <td><code>phase=None, tier=None, pack=None</code></td>
                <td><code>List[ArtifactSummary]</code></td>
                <td>استكشاف كائنات الملخص لكافة الـ 114 تسليمة أو الحزم المخصصة مع البصمات التشفيرية SHA-256.</td>
              </tr>
              <tr>
                <td><code>get_artifact_definition()</code></td>
                <td><code>artifact_id: str</code></td>
                <td><code>dict</code></td>
                <td>جلب قاموس البيانات الوصفية المعياري للتسليمة شاملاً رموز المراحل ومسارات الملفات.</td>
              </tr>
              <tr>
                <td><code>get_artifact_assets()</code></td>
                <td><code>artifact_id: str, lang='en'</code></td>
                <td><code>ArtifactAssets</code></td>
                <td>كائن يوفر مسارات آمنة ودوال وصول ميسرة لكافة أصول التسليمة.</td>
              </tr>
              <tr>
                <td><code>get_artifact_asset()</code></td>
                <td><code>artifact_id: str, role: str, lang='en'</code></td>
                <td><code>Union[str, dict, list]</code></td>
                <td>جلب محتوى الأصل مباشرة بحسب دوره: <code>template</code>, <code>guide</code>, <code>prompt</code>, <code>schema</code>, <code>dictionary</code>, <code>example</code>.</td>
              </tr>
              <tr>
                <td><code>get_tailoring_profile()</code></td>
                <td><code>tier: Union[int, str], pack: str='general'</code></td>
                <td><code>List[str]</code></td>
                <td>إرجاع قائمة معرّفات التسليمات الإلزامية المطابقة لمستوى الحوكمة (1, 2, 3) وحزمة المنهجية.</td>
              </tr>
              <tr>
                <td><code>get_lexicon()</code></td>
                <td><code>category: Optional[str]=None</code></td>
                <td><code>List[dict]</code></td>
                <td>إرجاع مصفوفة المصطلحات ثنائية اللغة المتوافقة مع دليل PMI ومواصفات هيئة الحكومة الرقمية السعودية (DGA).</td>
              </tr>
              <tr>
                <td><code>validate_artifact_data()</code></td>
                <td><code>artifact_id: str, data: dict, mode='strict'</code></td>
                <td><code>ValidationReport</code></td>
                <td>التحقق الآلي من مطابقة البيانات مع مخطط JSON Draft 2020-12 والتحقق الصارم من معايير RFC.</td>
              </tr>
              <tr>
                <td><code>render_artifact()</code></td>
                <td><code>artifact_id: str, lang='en', data=None, out_path=None</code></td>
                <td><code>str</code></td>
                <td>تصيير قالب التسليمة مع البيانات إلى وثيقة HTML منسقة جاهزة للطباعة مع دعم كامل للغة العربية.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Data Models Card AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">نماذج وفئات البيانات البرمجية</h2>
        
        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;"><code>ArtifactSummary</code></h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 0.75rem;">يمثل البيانات الوصفية الإجمالية للتسليمة المرجعة من <code>list_artifacts()</code>:</p>
        <pre style="direction: ltr; text-align: left;"><code>@dataclass(frozen=True)
class ArtifactSummary:
    artifact_id: str       # e.g. "PMO-03.01"
    prefix: str            # e.g. "03_01"
    name_en: str           # e.g. "Project Charter"
    name_ar: str           # e.g. "ميثاق المشروع"
    phase_code: str        # e.g. "03"
    phase_name_en: str     # e.g. "Initiating"
    phase_name_ar: str     # e.g. "البدء والترخيص"
    tiers: List[str]       # e.g. ["1", "2", "3"]
    fingerprint: str       # SHA-256 hash of immutable source form
    completed_data_validation: dict</code></pre>

        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;"><code>ValidationReport</code> &amp; <code>ValidationError</code></h3>
        <pre style="direction: ltr; text-align: left;"><code>@dataclass
class ValidationReport:
    valid: bool                         # True if payload satisfies all schema constraints
    errors: List[ValidationError]       # List of structured validation errors
    schema_id: str                      # Canonical URI of the schema
    schema_dialect: str                 # "https://json-schema.org/draft/2020-12/schema"
    fingerprint: str                    # SHA-256 fingerprint of the schema

@dataclass
class ValidationError:
    path: str                           # JSON Pointer / property path (e.g. "/budget/total")
    message: str                        # Human-readable failure explanation
    keyword: str                        # Violated keyword (e.g. "required", "format")
    schema_path: str                    # Path inside the schema where rule was defined</code></pre>
      </div>

      <!-- Real-World Python Script Card AR -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">مثال برمجي مكتمل بلغة بايثون</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          يوضح الكود التالي كيفية استعلام التسليمات المخصصة، قراءة محتوى القالب، التحقق من صحة البيانات، وإصدار التقرير:
        </p>
        <pre style="direction: ltr; text-align: left;"><code>import tasleemat

# 1. استخراج التسليمات المخصصة للمستوى 2 بمنهجية رشيقة
tailored_ids = tasleemat.get_tailoring_profile(tier=2, pack="agile")
print(f"عدد تسليمات الحزمة المخصصة: {{len(tailored_ids)}}")

# 2. فحص أصول تسليمة معينة (ميثاق المشروع PMO-03.01)
art_id = "PMO-03.01"
meta = tasleemat.get_artifact_definition(art_id)
print(f"التسليمة: {{meta['name_ar']}} / {{meta['name_en']}}")

assets = tasleemat.get_artifact_assets(art_id, lang="ar")
template_text = assets.get_template_content()
schema_data = assets.get_schema_data()

# 3. التحقق من بيانات الميثاق آلياً وفق معيار Draft 2020-12
payload = {{
    "project_id": "PRJ-2026-CLOUD",
    "project_name": "منصة التحول الرقمي السحابي",
    "sponsor": "النائب التنفيذي للعمليات",
    "project_manager": "سارة الأحمد",
    "authorization_date": "2026-10-15"
}}

report = tasleemat.validate_artifact_data(art_id, payload, mode="strict")
if report.valid:
    print("البيانات مطابقة تماماً للمخطط المعتمد!")
else:
    for err in report.errors:
        print(f"خطأ في الحقل {{err.path}}: {{err.message}}")</code></pre>
      </div>

    </div>
    """
    return render_html_page(
        title="معمارية مكتبة بايثون والمرجع البرمجي",
        content=content,
        lang="ar",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/developers/sdk/",
        description="المرجع البرمجي لمكتبة بايثون (SDK) لتسليمات: الدوال الثماني الأساسية، نماذج البيانات، والتحقق الصارم من مخططات الوثائق.",
        canonical_url="https://fakhr.me/Tasleemat/ar/developers/sdk/",
    )


# ==============================================================================
# 4. SUB-PAGE: MODEL CONTEXT PROTOCOL (MCP)
# ==============================================================================

def generate_dev_mcp_en(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("mcp", "en", base_url)
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/">Home</a> &gt; 
          <a href="{base_url}/developers/">Developers &amp; AI</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">MCP Server</span>
        </nav>
        <div class="hero-pill"><span>🔌 Model Context Protocol</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">Model Context Protocol (MCP) Server</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto;">
          Connect Claude Desktop, Cursor, and autonomous AI agents directly to the 114 project deliverables and Draft 2020-12 schemas via JSON-RPC 2.0.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- What is MCP Card -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">Standard Stdio Architecture</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          The Model Context Protocol (MCP) allows modern AI assistants to seamlessly read external tool definitions, fetch schemas, 
          and execute validated commands without hallucinating file contents. 
          Tasleemat packages an official standalone executable (<code>tasleemat-mcp</code>) that communicates over <code>stdio</code> via standard JSON-RPC 2.0 messages.
        </p>
        <pre><code># Test MCP Server execution in stdio mode
tasleemat-mcp</code></pre>
      </div>

      <!-- IDE Configurations Card -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">AI IDE &amp; Assistant Configurations</h2>
        
        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">1. Anthropic Claude Desktop</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 0.5rem;">
          Add to <code>claude_desktop_config.json</code> (macOS: <code>~/Library/Application Support/Claude/</code>, Windows: <code>%APPDATA%\\Claude\\</code>, Linux: <code>~/.config/Claude/</code>):
        </p>
        <pre><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat-mcp",
      "args": []
    }}
  }}
}}</code></pre>

        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">2. Cursor IDE</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 0.5rem;">
          Add to your project root or user config in <code>.cursor/mcp.json</code>:
        </p>
        <pre><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "python3",
      "args": ["-m", "tasleemat.mcp"]
    }}
  }}
}}</code></pre>
      </div>

      <!-- 6 Exposed Tools Card -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">The 6 Specialized MCP Tools</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.5rem;">
          The server advertises exactly 6 deterministic tools to the client:
        </p>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>MCP Tool Name</th>
                <th>Arguments</th>
                <th>Description</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>tasleemat_list_forms</code></td>
                <td><code>phase (optional), lang (optional)</code></td>
                <td>Returns catalog listings with IDs, bilingual titles, and phase categories.</td>
              </tr>
              <tr>
                <td><code>tasleemat_get_form</code></td>
                <td><code>artifact_id, asset_type, lang</code></td>
                <td>Fetches template, guide, example, prompt, schema, or dictionary content.</td>
              </tr>
              <tr>
                <td><code>tasleemat_get_schema</code></td>
                <td><code>artifact_id</code></td>
                <td>Returns complete JSON Schema Draft 2020-12 definition.</td>
              </tr>
              <tr>
                <td><code>tasleemat_validate</code></td>
                <td><code>artifact_id, data, mode</code></td>
                <td>Performs headless schema validation and returns exact JSON path errors.</td>
              </tr>
              <tr>
                <td><code>tasleemat_tailor_project</code></td>
                <td><code>tier (1, 2, 3), pack</code></td>
                <td>Returns tailored list of required deliverable IDs for the project.</td>
              </tr>
              <tr>
                <td><code>tasleemat_calculate_eva</code></td>
                <td><code>pv, ev, ac, bac</code></td>
                <td>Executes attested mathematical computations for PMO-06.05 metrics.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
    """
    return render_html_page(
        title="Model Context Protocol (MCP) Server Reference",
        content=content,
        lang="en",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/developers/mcp/",
        description="Model Context Protocol (MCP) Server for Tasleemat: Connect Claude Desktop, Cursor, and AI agents directly to 114 project deliverables via stdio.",
        canonical_url="https://fakhr.me/Tasleemat/developers/mcp/",
    )


def generate_dev_mcp_ar(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("mcp", "ar", base_url)
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/ar/">الرئيسية</a> &gt; 
          <a href="{base_url}/ar/developers/">المطورون والذكاء الاصطناعي</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">خادم بروتوكول MCP</span>
        </nav>
        <div class="hero-pill"><span>🔌 بروتوكول سياق النموذج (MCP)</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">خادم بروتوكول سياق النموذج (MCP)</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
          ربط بيئات Claude Desktop و Cursor والوكلاء الأذكياء مباشرة بتسليمات المشروع ومخططاتها عبر بروتوكول JSON-RPC 2.0.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- What is MCP Card AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">المعمارية القياسية لبروتوكول MCP</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          يسمح بروتوكول سياق النموذج (MCP) لمساعدي الذكاء الاصطناعي بقراءة الأدوات البرمجية، جلب المخططات، والتحقق من صحة البيانات دون أي هلوسة في المحتوى.
          توفر حزمة تسليمات أداة تشغيل رسمية مستقلة (<code>tasleemat-mcp</code>) تتواصل عبر قنوات <code>stdio</code> القياسية.
        </p>
        <pre style="direction: ltr; text-align: left;"><code># تجربة تشغيل خادم MCP في سطر الأوامر
tasleemat-mcp</code></pre>
      </div>

      <!-- IDE Configurations Card AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">إعدادات بيئات ومساعدي الذكاء الاصطناعي</h2>
        
        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">1. تطبيق Claude Desktop</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 0.5rem;">
          أضف الإعداد في ملف <code>claude_desktop_config.json</code>:
        </p>
        <pre style="direction: ltr; text-align: left;"><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat-mcp",
      "args": []
    }}
  }}
}}</code></pre>

        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">2. محرر Cursor IDE</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 0.5rem;">
          أضف في ملف <code>.cursor/mcp.json</code> داخل المجلد الرئيسي لمشروعك:
        </p>
        <pre style="direction: ltr; text-align: left;"><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "python3",
      "args": ["-m", "tasleemat.mcp"]
    }}
  }}
}}</code></pre>
      </div>

      <!-- 6 Exposed Tools Card AR -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">الأدوات الست المتخصصة لخادم MCP</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.5rem;">
          يعلن الخادم للعملاء عن 6 أدوات برمجية حتمية:
        </p>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>اسم الأداة</th>
                <th>المعاملات</th>
                <th>الوصف والوظيفة</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>tasleemat_list_forms</code></td>
                <td><code>phase (اختياري), lang (اختياري)</code></td>
                <td>إرجاع قائمة التسليمات بمعرفاتها وعناوينها الثنائية ومراحلها.</td>
              </tr>
              <tr>
                <td><code>tasleemat_get_form</code></td>
                <td><code>artifact_id, asset_type, lang</code></td>
                <td>جلب القالب أو الدليل أو المثال أو موجه الذكاء الاصطناعي أو المخطط أو القاموس.</td>
              </tr>
              <tr>
                <td><code>tasleemat_get_schema</code></td>
                <td><code>artifact_id</code></td>
                <td>جلب مخطط JSON Draft 2020-12 الكامل للتسليمة.</td>
              </tr>
              <tr>
                <td><code>tasleemat_validate</code></td>
                <td><code>artifact_id, data, mode</code></td>
                <td>التحقق الآلي من البيانات وإرجاع مسار الخطأ بدقة.</td>
              </tr>
              <tr>
                <td><code>tasleemat_tailor_project</code></td>
                <td><code>tier (1, 2, 3), pack</code></td>
                <td>إرجاع قائمة التسليمات المخصصة للمشروع بحسب الحجم والمنهجية.</td>
              </tr>
              <tr>
                <td><code>tasleemat_calculate_eva</code></td>
                <td><code>pv, ev, ac, bac</code></td>
                <td>تنفيذ الحسابات الرياضية الموثقة لمقاييس القيمة المكتسبة (PMO-06.05).</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
    """
    return render_html_page(
        title="مرجع خادم بروتوكول سياق النموذج (MCP)",
        content=content,
        lang="ar",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/developers/mcp/",
        description="خادم بروتوكول سياق النموذج (MCP) لتسليمات: دمج أدوات الحوكمة ومخططات الـ 114 تسليمة مباشرة مع بيئات Cursor و Claude Desktop.",
        canonical_url="https://fakhr.me/Tasleemat/ar/developers/mcp/",
    )


# ==============================================================================
# 5. SUB-PAGE: JSON SCHEMAS & AUTONOMOUS HEALING
# ==============================================================================

def generate_dev_schemas_en(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("schemas", "en", base_url)
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/">Home</a> &gt; 
          <a href="{base_url}/developers/">Developers &amp; AI</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">Schemas &amp; Validation</span>
        </nav>
        <div class="hero-pill"><span>📐 JSON Schema Draft 2020-12</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">JSON Schemas &amp; Autonomous Healing</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto;">
          Strict validation contracts across 114 deliverables, RFC format enforcement, and the autonomous self-correction loop for AI agents.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Draft 2020-12 Specification Card -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">Draft 2020-12 Dialect &amp; Specification</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Every canonical deliverable in Tasleemat is paired with a companion JSON schema declaring <code>"$schema": "https://json-schema.org/draft/2020-12/schema"</code>. 
          The schemas declare required metadata, nested objects, typed arrays, and strict format validation rules.
        </p>
        
        <h3 style="font-size: 1.15rem; margin-top: 1.25rem; margin-bottom: 0.5rem;">Enforced RFC Formats:</h3>
        <ul style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.8; padding-left: 1.5rem; margin-bottom: 1.5rem;">
          <li><strong>RFC 3339 (Date &amp; Timestamp):</strong> Formats <code>date</code> (<code>YYYY-MM-DD</code>) and <code>date-time</code> (<code>YYYY-MM-DDTHH:MM:SSZ</code>). Leap years and timezone offsets are strictly validated.</li>
          <li><strong>RFC 4122 (UUID):</strong> Format <code>uuid</code> verifying 128-bit identifiers (8-4-4-4-12 hexadecimal structure).</li>
          <li><strong>RFC 3986 (URI &amp; URI Reference):</strong> Formats <code>uri</code> and <code>uri-reference</code> ensuring compliant scheme, authority, and path syntax.</li>
          <li><strong>RFC 5322 (Email Address):</strong> Format <code>email</code> enforcing RFC-compliant user and domain structure.</li>
        </ul>

        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Validation Modes: Strict vs. Draft</h3>
        <p style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.7;">
          <code>mode="strict"</code> enforces all required fields, non-empty strings, and rejection of undeclared properties. 
          <code>mode="draft"</code> allows progressive elaboration during early project planning stages while verifying types and formats for populated fields.
        </p>
      </div>

      <!-- Autonomous Healing Loop Card -->
      <div id="self-correction" class="card" style="padding: 2.25rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
          <h2 style="font-size: 1.5rem; margin: 0; color: var(--text-main);">The Autonomous Agent Self-Correction Feedback Loop</h2>
          <span class="badge" style="background: var(--accent-blue-bg); color: var(--accent-blue); font-weight: 700; font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">Healing Engine</span>
        </div>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          When an LLM synthesizes structured project data, slight discrepancies can occur (e.g. missing required approval signatures or malformed ISO dates). 
          The agent self-correction feedback loop uses deterministic schema validation to teach the model how to heal its own output in a tight retry loop:
        </p>

        <pre><code class="language-mermaid">
sequenceDiagram
    autonumber
    actor User as Practitioner / User
    participant Agent as Autonomous PMO Agent
    participant Engine as Tasleemat Validator
    participant LLM as Frontier LLM Model

    User->>Agent: "Draft Risk Register for Cloud Project"
    Agent->>Engine: get_artifact_asset("PMO-04.08.02", "schema")
    Engine-->>Agent: Draft 2020-12 Schema
    Agent->>LLM: Prompt + Schema Constraints
    LLM-->>Agent: Raw JSON Payload (Draft 1)
    Agent->>Engine: validate_artifact_data("PMO-04.08.02", Draft 1, mode="strict")
    Engine-->>Agent: ValidationReport(valid=False, error="At /risks/0/score: missing required property")
    Note over Agent,LLM: Autonomous Healing Turn
    Agent->>LLM: "Previous output failed validation at /risks/0/score. Rectify schema error."
    LLM-->>Agent: Corrected JSON Payload (Draft 2)
    Agent->>Engine: validate_artifact_data("PMO-04.08.02", Draft 2, mode="strict")
    Engine-->>Agent: ValidationReport(valid=True)
    Agent->>User: "Risk Register Generated &amp; 100% Schema Validated"
        </code></pre>

        <h3 style="font-size: 1.15rem; margin-top: 1.75rem; margin-bottom: 0.5rem;">Autonomous Healing Python Script</h3>
        <pre><code>import tasleemat

def synthesize_with_self_correction(artifact_id: str, prompt_notes: str, max_retries: int = 3):
    schema = tasleemat.get_artifact_asset(artifact_id, "schema", lang="en")
    current_notes = prompt_notes
    
    for attempt in range(1, max_retries + 1):
        # 1. Call your configured LLM (e.g. Gemini, OpenAI, Claude)
        candidate_data = my_llm_call(notes=current_notes, schema=schema)
        
        # 2. Validate against Draft 2020-12 schema
        report = tasleemat.validate_artifact_data(artifact_id, candidate_data, mode="strict")
        if report.valid:
            print(f"Success on attempt {{attempt}}!")
            return candidate_data
            
        # 3. Formulate targeted healing prompt
        error_messages = [f"- {{e.path}}: {{e.message}}" for e in report.errors]
        current_notes = (
            f"{{prompt_notes}}\\n\\n"
            f"[CRITICAL: Previous attempt failed validation with errors:]\\n"
            + "\\n".join(error_messages)
            + "\\nFix these exact paths and return valid JSON."
        )
    raise RuntimeError("Failed to converge on valid schema payload within retry limit.")</code></pre>
      </div>

    </div>
    """
    return render_html_page(
        title="JSON Schemas & Autonomous Healing Reference",
        content=content,
        lang="en",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/developers/schemas/",
        description="JSON Schema Draft 2020-12 specifications, strict RFC format constraints, and autonomous agent self-correction feedback loop for Tasleemat.",
        canonical_url="https://fakhr.me/Tasleemat/developers/schemas/",
    )


def generate_dev_schemas_ar(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("schemas", "ar", base_url)
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/ar/">الرئيسية</a> &gt; 
          <a href="{base_url}/ar/developers/">المطورون والذكاء الاصطناعي</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">المخططات والتحقق</span>
        </nav>
        <div class="hero-pill"><span>📐 معيار JSON Schema Draft 2020-12</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">مخططات JSON وحلقة التصحيح الذاتي</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
          عقود التحقق الصارمة لكافة الـ 114 تسليمة، معايير RFC، وحلقة التغذية الراجعة التلقائية لإصلاح أخطاء الوكلاء الأذكياء.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Draft 2020-12 Specification Card AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">مواصفات ولهجة Draft 2020-12</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          تقترن كل تسليمة معيارية في إطار تسليمات بمخطط JSON مخصص يعلن عن المعيار الدولي: 
          <code>"$schema": "https://json-schema.org/draft/2020-12/schema"</code>.
          تحدد المخططات الحقول الإلزامية، الكائنات المتداخلة، مصفوفات البيانات المنضبطة، والتحقق الصارم من التنسيقات.
        </p>
        
        <h3 style="font-size: 1.15rem; margin-top: 1.25rem; margin-bottom: 0.5rem;">تنسيقات RFC الإلزامية المفروضة:</h3>
        <ul style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.8; padding-right: 1.5rem; margin-bottom: 1.5rem;">
          <li><strong>RFC 3339 (التواريخ والوقت):</strong> صيغة التاريخ <code>date</code> (<code>YYYY-MM-DD</code>) وصيغة الوقت الكامل <code>date-time</code> (<code>YYYY-MM-DDTHH:MM:SSZ</code>) مع التحقق من السنوات الكبيسة وفروق التوقيت.</li>
          <li><strong>RFC 4122 (المعرفات الفريدة UUID):</strong> صيغة <code>uuid</code> للتحقق من المعرفات الفريدة بطول 128 بت (بنية 8-4-4-4-12).</li>
          <li><strong>RFC 3986 (الروابط URIs):</strong> صيغ <code>uri</code> و <code>uri-reference</code> للتحقق من صحة بروتوكول ومسار الروابط.</li>
          <li><strong>RFC 5322 (البريد الإلكتروني):</strong> صيغة <code>email</code> للتحقق من صحة أسماء المستخدمين والنطاقات.</li>
        </ul>

        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">أوضاع التحقق: الصارم (Strict) مقابل المسودة (Draft)</h3>
        <p style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.8;">
          يفرض الوضع الصارم (<code>mode="strict"</code>) كافة الحقول المطلوبة والنصوص غير الفارغة ويرفض الحقول غير المصرح بها.
          بينما يسمح وضع المسودة (<code>mode="draft"</code>) بالتدرج في إكمال الحقول خلال مراحل التخطيط الأولى مع التأكد من صحة أنواع الحقول المعبأة.
        </p>
      </div>

      <!-- Autonomous Healing Loop Card AR -->
      <div id="self-correction" class="card" style="padding: 2.25rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
          <h2 style="font-size: 1.5rem; margin: 0; color: var(--text-main);">حلقة التصحيح الذاتي التلقائي للوكلاء الأذكياء</h2>
          <span class="badge" style="background: var(--accent-blue-bg); color: var(--accent-blue); font-weight: 700; font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">محرك المعالجة الذاتية</span>
        </div>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          عندما تقوم النماذج اللغوية بتوليد بيانات المشاريع، قد تحدث أخطاء في البنية (كنقص حقل إلزامي أو صيغة تاريخ غير قياسية).
          تعتمد حلقة التصحيح الذاتي على التحقق الحتمي لإرجاع مسار الخطأ بدقة إلى النموذج اللغوي ليعيد تصحيح نفسه تلقائياً:
        </p>

        <pre><code class="language-mermaid">
sequenceDiagram
    autonumber
    actor User as الممارس / مدير المشروع
    participant Agent as الوكيل الذكي (PMO Agent)
    participant Engine as محرك التحقق في تسليمات
    participant LLM as نموذج الذكاء الاصطناعي (LLM)

    User->>Agent: "قم بإعداد سجل المخاطر لمشروع السحابة"
    Agent->>Engine: get_artifact_asset("PMO-04.08.02", "schema")
    Engine-->>Agent: مخطط Draft 2020-12
    Agent->>LLM: الأمر + قيود المخطط البرمجي
    LLM-->>Agent: بيانات JSON الأولية (المسودة 1)
    Agent->>Engine: validate_artifact_data("PMO-04.08.02", المسودة 1, mode="strict")
    Engine-->>Agent: ValidationReport(valid=False, error="نقص حقل إلزامي في /risks/0/score")
    Note over Agent,LLM: جولة التصحيح الذاتي التلقائي
    Agent->>LLM: "فشل التحقق في المسار /risks/0/score. أصلح الخطأ فوراً."
    LLM-->>Agent: بيانات JSON المصححة (المسودة 2)
    Agent->>Engine: validate_artifact_data("PMO-04.08.02", المسودة 2, mode="strict")
    Engine-->>Agent: ValidationReport(valid=True)
    Agent->>User: "تم توليد سجل المخاطر بنجاح وتأكيد صحته وفق المخطط 100%"
        </code></pre>

        <h3 style="font-size: 1.15rem; margin-top: 1.75rem; margin-bottom: 0.5rem;">كود التصحيح الذاتي بلغة بايثون</h3>
        <pre style="direction: ltr; text-align: left;"><code>import tasleemat

def synthesize_with_self_correction(artifact_id: str, prompt_notes: str, max_retries: int = 3):
    schema = tasleemat.get_artifact_asset(artifact_id, "schema", lang="ar")
    current_notes = prompt_notes
    
    for attempt in range(1, max_retries + 1):
        candidate_data = my_llm_call(notes=current_notes, schema=schema)
        
        report = tasleemat.validate_artifact_data(artifact_id, candidate_data, mode="strict")
        if report.valid:
            print(f"تم التحقق بنجاح في المحاولة رقم {{attempt}}!")
            return candidate_data
            
        error_messages = [f"- {{e.path}}: {{e.message}}" for e in report.errors]
        current_notes = (
            f"{{prompt_notes}}\\n\\n"
            f"[تنبيه: فشلت المحاولة السابقة في التحقق للأسباب التالية:]\\n"
            + "\\n".join(error_messages)
            + "\\nقم بتصحيح هذه المسارات بدقة وأعد إرسال JSON صالح."
        )
    raise RuntimeError("تعذر تصحيح البيانات ضمن الحد الأقصى للمحاولات.")</code></pre>
      </div>

    </div>
    """
    return render_html_page(
        title="مخططات JSON وحلقة التصحيح الذاتي",
        content=content,
        lang="ar",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/developers/schemas/",
        description="مواصفات مخططات JSON المعيارية Draft 2020-12، قيود RFC الإلزامية، ومحرك التصحيح الذاتي التلقائي لأسراب الوكلاء الأذكياء.",
        canonical_url="https://fakhr.me/Tasleemat/ar/developers/schemas/",
    )


# ==============================================================================
# 6. SUB-PAGE: AGENTIC SWARMS, CI/CD & ATTESTED MATH
# ==============================================================================

def generate_dev_agentic_en(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("agentic", "en", base_url)
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/">Home</a> &gt; 
          <a href="{base_url}/developers/">Developers &amp; AI</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">Agentic Swarms &amp; CI/CD</span>
        </nav>
        <div class="hero-pill"><span>🤖 Multi-Agent Swarms &amp; DevOps</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">Agentic Swarms, CI/CD &amp; Attested Math</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto;">
          Enterprise multi-agent architectures (CrewAI, LangGraph), unified LLM synthesis, automated CI/CD quality gates, and attested math contracts.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Multi-Agent PMO Swarm Card -->
      <div id="multi-agent" class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">Multi-Agent PMO Swarm Architecture</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          In high-governance organizations, a single generic AI agent cannot adequately draft, audit, and approve project deliverables. 
          Tasleemat establishes a 4-agent persona architecture with explicit checks and balances:
        </p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
          <div style="background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.35rem;">1. Project Manager Agent</div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">Retrieves templates and drafts initial deliverables from kickoff notes and stakeholder transcripts.</div>
          </div>
          <div style="background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.35rem;">2. PMO Auditor Agent</div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">Enforces Draft 2020-12 schema conformance, checks required stage gates, and flags missing sections.</div>
          </div>
          <div style="background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.35rem;">3. Risk &amp; Ethics Lead Agent</div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">Audits AI ethics cards, technical debt registers, and evaluates severity probability scores.</div>
          </div>
          <div style="background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.35rem;">4. Human Sponsor Boundary</div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">AI swarms NEVER self-approve. Deliverables are packaged for human executive sponsor sign-off.</div>
          </div>
        </div>
      </div>

      <!-- LLM Client Card -->
      <div id="llm-client" class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">Programmatic AI Synthesis with <code>tasleemat.ai.AIClient</code></h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          The <code>tasleemat.ai</code> submodule provides a provider-agnostic client abstraction across Google Gemini, OpenAI GPT-4o, Anthropic Claude, and local Ollama endpoints:
        </p>
        <pre><code>from tasleemat.ai import AIClient

# Initializes client using ~/.tasleemat/config.json or environment variables
client = AIClient.from_config()

# Synthesize charter with automatic prompt and schema injection
result = client.generate_deliverable(
    artifact_id="PMO-03.01",
    notes="Kickoff meeting transcript: Target completion Q3 2026, budget $2.4M...",
    lang="en",
    validate=True  # Automatically runs self-correction if invalid
)

print(result.markdown_content)</code></pre>
      </div>

      <!-- CI/CD Card -->
      <div id="cicd" class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">Headless CI/CD Automation &amp; Quality Gates</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Embed Tasleemat into GitHub Actions or GitLab CI to ensure every pull request adheres to deliverable completeness and schema integrity:
        </p>
        <pre><code># .github/workflows/tasleemat-quality-gate.yml
name: Tasleemat PMO Quality Gate

on: [push, pull_request]

jobs:
  validate-deliverables:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          
      - name: Install Tasleemat
        run: pip install tasleemat
        
      - name: Verify Forms Integrity Baseline
        run: tasleemat test -v</code></pre>
      </div>

      <!-- Attested Math Card -->
      <div id="attested-math" class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">Attested Computations &amp; Deterministic Math Contracts (PMO-06.05)</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Large language models are probabilistic token predictors and are notoriously prone to math hallucinations. 
          When managing project investments, financial and schedule metrics must be backed by attested deterministic code. 
          Tasleemat enforces mathematically verified formulas for Earned Value Analysis (<code>PMO-06.05</code>):
        </p>

        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>Earned Value Metric</th>
                <th>Standard Formula</th>
                <th>Interpretation &amp; Attestation</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Cost Variance (CV)</strong></td>
                <td><code>CV = EV - AC</code></td>
                <td>Positive = under budget, Negative = over budget</td>
              </tr>
              <tr>
                <td><strong>Schedule Variance (SV)</strong></td>
                <td><code>SV = EV - PV</code></td>
                <td>Positive = ahead of schedule, Negative = behind schedule</td>
              </tr>
              <tr>
                <td><strong>Cost Performance Index (CPI)</strong></td>
                <td><code>CPI = EV / AC</code></td>
                <td>&gt; 1.0 = cost efficient, &lt; 1.0 = cost overrun</td>
              </tr>
              <tr>
                <td><strong>Schedule Performance Index (SPI)</strong></td>
                <td><code>SPI = EV / PV</code></td>
                <td>&gt; 1.0 = progressing faster than planned</td>
              </tr>
              <tr>
                <td><strong>Estimate at Completion (EAC)</strong></td>
                <td><code>EAC = BAC / CPI</code></td>
                <td>Projected total cost based on current performance</td>
              </tr>
              <tr>
                <td><strong>To-Complete Performance Index (TCPI)</strong></td>
                <td><code>TCPI = (BAC - EV) / (BAC - AC)</code></td>
                <td>Efficiency required to finish within remaining budget</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
    """
    return render_html_page(
        title="Agentic Swarms, CI/CD & Attested Math",
        content=content,
        lang="en",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/developers/agentic/",
        description="Multi-Agent Architectures (CrewAI, LangGraph), LLM Prompt Synthesis, CI/CD Automated Governance Gates, and Attested Math Contracts for Tasleemat.",
        canonical_url="https://fakhr.me/Tasleemat/developers/agentic/",
    )


def generate_dev_agentic_ar(base_url: str = "/Tasleemat") -> str:
    subnav = _render_dev_subnav("agentic", "ar", base_url)
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/ar/">الرئيسية</a> &gt; 
          <a href="{base_url}/ar/developers/">المطورون والذكاء الاصطناعي</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">أسراب الوكلاء و CI/CD</span>
        </nav>
        <div class="hero-pill"><span>🤖 أسراب الوكلاء وبوابات DevOps</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">أسراب الوكلاء، CI/CD، والحسابات الموثقة</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
          معمارية الوكلاء المتعددين (CrewAI, LangGraph)، التوليد الموحد عبر الذكاء الاصطناعي، بوابات CI/CD، وعقود الحسابات الرياضية الموثقة.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Multi-Agent PMO Swarm Card AR -->
      <div id="multi-agent" class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">معمارية أسراب الوكلاء الأذكياء المتعددين (Multi-Agent Swarm)</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          في المؤسسات ذات الحوكمة العالية، لا يمكن لوكيل ذكي واحد أن يقوم بصياغة التسليمة وتدقيقها واعتمادها بمفرده.
          يؤسس إطار تسليمات بنية مكونة من 4 شخصيات متخصصة مع ضوابط وتوازنات واضحة:
        </p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
          <div style="background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.35rem;">1. وكيل مدير المشروع (PM Agent)</div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">جلب القوالب وصياغة المسودات الأولية للتسليمات من نصوص الاجتماعات ومخرجات النقاش.</div>
          </div>
          <div style="background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.35rem;">2. وكيل مدقق الحوكمة (PMO Auditor)</div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">فرض مطابقة المخططات Draft 2020-12 وفحص بوابات المراجعة وتنبيه الفريق للأقسام المفقودة.</div>
          </div>
          <div style="background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.35rem;">3. وكيل المخاطر والأخلاقيات (Risk Lead)</div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">تدقيق بطاقات أخلاقيات النماذج، وسجلات الديون التقنية، وتقييم احتمالية وشدة المخاطر.</div>
          </div>
          <div style="background: var(--bg-main); padding: 1.25rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.35rem;">4. حدود الاعتماد البشري (Human Sponsor)</div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">لا تعتمد النماذج الذكية نفسها أبداً. يتم تسليم الوثائق الجاهزة للمسؤولين البشر للاعتماد الرسمي.</div>
          </div>
        </div>
      </div>

      <!-- LLM Client Card AR -->
      <div id="llm-client" class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">التوليد البرمجي عبر <code>tasleemat.ai.AIClient</code></h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          يوفر الموديول <code>tasleemat.ai</code> عميلاً موحداً متوافقاً مع Google Gemini و OpenAI GPT-4o و Anthropic Claude والخوادم المحلية المنعزلة:
        </p>
        <pre style="direction: ltr; text-align: left;"><code>from tasleemat.ai import AIClient

# تهيئة العميل من ملف ~/.tasleemat/config.json أو متغيرات البيئة
client = AIClient.from_config()

# توليد مسودة ميثاق المشروع مع التحقق الذاتي التلقائي
result = client.generate_deliverable(
    artifact_id="PMO-03.01",
    notes="مخرجات اجتماع إطلاق المشروع: الميزانية 9 مليون ريال، تاريخ التسليم النهائي الربع الثالث 2026...",
    lang="ar",
    validate=True  # إجراء التصحيح الذاتي تلقائياً عند أي مخالفة للمخطط
)

print(result.markdown_content)</code></pre>
      </div>

      <!-- CI/CD Card AR -->
      <div id="cicd" class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">بوابات الجودة الآلية في خطوط CI/CD</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          دمج تسليمات في GitHub Actions لضمان سلامة كافة الوثائق وصحة المخططات مع كل إيداع برمجي (Commit):
        </p>
        <pre style="direction: ltr; text-align: left;"><code># .github/workflows/tasleemat-quality-gate.yml
name: Tasleemat PMO Quality Gate

on: [push, pull_request]

jobs:
  validate-deliverables:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          
      - name: Install Tasleemat
        run: pip install tasleemat
        
      - name: Verify Forms Integrity Baseline
        run: tasleemat test -v</code></pre>
      </div>

      <!-- Attested Math Card AR -->
      <div id="attested-math" class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">عقود الحسابات الرياضية الموثقة (PMO-06.05)</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          تتعرض النماذج اللغوية للهلوسة في الحسابات الدقيقة؛ لذلك يفرض إطار تسليمات محركات حسابية حتمية لتحليل القيمة المكتسبة (EVA في <code>PMO-06.05</code>):
        </p>

        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>مقياس القيمة المكتسبة</th>
                <th>المعادلة القياسية</th>
                <th>المعنى والتفسير الرياضي</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>تباين التكلفة (Cost Variance - CV)</strong></td>
                <td><code>CV = EV - AC</code></td>
                <td>الموجب = توفير في الميزانية، السالب = تجاوز الميزانية</td>
              </tr>
              <tr>
                <td><strong>تباين الجدول الزمني (Schedule Variance - SV)</strong></td>
                <td><code>SV = EV - PV</code></td>
                <td>الموجب = متقدم عن الجدول، السالب = متأخر زمنياً</td>
              </tr>
              <tr>
                <td><strong>مؤشر أداء التكلفة (Cost Performance Index - CPI)</strong></td>
                <td><code>CPI = EV / AC</code></td>
                <td>أكبر من 1.0 = كفاءة تكلفة، أقل من 1.0 = تجاوز التكلفة</td>
              </tr>
              <tr>
                <td><strong>مؤشر أداء الجدول (Schedule Performance Index - SPI)</strong></td>
                <td><code>SPI = EV / PV</code></td>
                <td>أكبر من 1.0 = سرعة إنجاز أعلى من المخطط</td>
              </tr>
              <tr>
                <td><strong>التقدير عند الاكتمال (Estimate at Completion - EAC)</strong></td>
                <td><code>EAC = BAC / CPI</code></td>
                <td>التكلفة الإجمالية المتوقعة بناءً على الأداء الحالي</td>
              </tr>
              <tr>
                <td><strong>مؤشر الأداء المطلوب للاكتمال (TCPI)</strong></td>
                <td><code>TCPI = (BAC - EV) / (BAC - AC)</code></td>
                <td>الكفاءة المطلوبة في المتبقي من المشروع لإنهاء الميزانية كما خطط لها</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
    """
    return render_html_page(
        title="أسراب الوكلاء، CI/CD، والحسابات الموثقة",
        content=content,
        lang="ar",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/developers/agentic/",
        description="معمارية أسراب الوكلاء المتعددين (CrewAI و LangGraph)، هندسة موجهات LLM، بوابات الحوكمة المؤتمتة، وعقود الحسابات الرياضية الموثقة.",
        canonical_url="https://fakhr.me/Tasleemat/ar/developers/agentic/",
    )


# Backward compatibility aliases
generate_developers_en = generate_developers_hub_en
generate_developers_ar = generate_developers_hub_ar
