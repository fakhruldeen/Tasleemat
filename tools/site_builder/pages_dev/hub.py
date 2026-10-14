"""tools/site_builder/pages_dev/hub.py
Developer & AI Integration Hub landing pages (English & Arabic).
"""

from tools.site_builder.theme import render_html_page
from tools.site_builder.pages_dev.nav import render_dev_subnav


def generate_developers_hub_en(base_url: str = "/Tasleemat") -> str:
    subnav = render_dev_subnav("hub", "en", base_url)
    
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
                Deep dive into <code>tasleemat init</code>, <code>list</code>, <code>search</code>, <code>config</code>, <code>generate</code>, and <code>test</code>. Interactive wizards, flags, air-gapped setups, and bash automation recipes.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-blue); font-size: 0.85rem; margin-top: 1rem;">View CLI Manual &rarr;</div>
          </a>

          <a href="{base_url}/developers/sdk/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid var(--accent-emerald); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🐍</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">Python SDK &amp; Core Architecture</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">
                All 8 verified pure-Python functions, FastAPI integration, custom Streamlit dashboards, data models (<code>ArtifactSummary</code>, <code>ArtifactAssets</code>), and EVM calculation engine.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-emerald); font-size: 0.85rem; margin-top: 1rem;">View SDK Reference &rarr;</div>
          </a>

          <a href="{base_url}/developers/mcp/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid var(--accent-amber); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🔌</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">Model Context Protocol (MCP)</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">
                JSON-RPC 2.0 stdio server connecting Claude Desktop, Cursor, and AI agents directly to the 114 deliverables, schemas, and tailoring engine. Includes Python MCP client tutorials.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-amber); font-size: 0.85rem; margin-top: 1rem;">View MCP Integration &rarr;</div>
          </a>

          <a href="{base_url}/developers/schemas/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid #8b5cf6; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📐</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">Draft 2020-12 &amp; Self-Correction</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">
                114 companion JSON schemas, RFC 3339/4122/3986 format validation, and the autonomous iterative feedback healing loop for frontier LLMs with runnable retry scripts.
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
    subnav = render_dev_subnav("hub", "ar", base_url)
    
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
          📚 الأدلة التقنية المتخصصة والوحدات البرمجية
        </h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
          
          <a href="{base_url}/ar/developers/cli/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid var(--accent-blue); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⌨️</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">أداة الطرفية وسطر الأوامر (CLI)</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
                شرح تفصيلي لأوامر <code>tasleemat init</code> و <code>list</code> و <code>search</code> و <code>config</code> و <code>generate</code> و <code>test</code> مع معالجات التهيئة والأتمتة في بيئات العمل المعزولة.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-blue); font-size: 0.85rem; margin-top: 1rem;">عرض دليل أداة الطرفية &larr;</div>
          </a>

          <a href="{base_url}/ar/developers/sdk/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid var(--accent-emerald); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🐍</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">مكتبة بايثون والمعمارية البرمجية (SDK)</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
                شرح الدوال الثماني الأساسية الخالية من التبعيات، تكامل FastAPI، لوحات تحكم Streamlit، ونماذج البيانات (<code>ArtifactSummary</code> و <code>ArtifactAssets</code>) وحسابات EVM.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-emerald); font-size: 0.85rem; margin-top: 1rem;">عرض مرجع مكتبة بايثون &larr;</div>
          </a>

          <a href="{base_url}/ar/developers/mcp/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid var(--accent-amber); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🔌</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">خادم بروتوكول سياق النموذج (MCP)</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
                خادم stdio ببروتوكول JSON-RPC 2.0 لربط Claude Desktop و Cursor والوكلاء الأذكياء بالـ 114 تسليمة والمخططات وحزم التخصيص، مع عميل بايثون مخصص.
              </p>
            </div>
            <div style="font-weight: 700; color: var(--accent-amber); font-size: 0.85rem; margin-top: 1rem;">عرض دليل بروتوكول MCP &larr;</div>
          </a>

          <a href="{base_url}/ar/developers/schemas/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid #8b5cf6; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📐</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">مخططات JSON وحلقة التصحيح الذاتي</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
                114 مخططاً معيارياً متوافقاً مع Draft 2020-12، قيود صيغ RFC الصارمة، ومحرك التغذية الراجعة التلقائي لمعالجة أخطاء نماذج الذكاء الاصطناعي مع كود الإعادة التلقائي.
              </p>
            </div>
            <div style="font-weight: 700; color: #8b5cf6; font-size: 0.85rem; margin-top: 1rem;">عرض المخططات والتصحيح الذاتي &larr;</div>
          </a>

          <a href="{base_url}/ar/developers/agentic/" class="card" style="text-decoration: none; padding: 1.75rem; border-top: 4px solid #ec4899; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🤖</div>
              <h3 style="font-size: 1.2rem; color: var(--text-main); margin-bottom: 0.5rem;">أسراب الوكلاء وخطوط CI/CD</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
                تنسيق أدوار الوكلاء في مكاتب إدارة المشاريع عبر CrewAI و LangGraph، التوليد عبر <code>AIClient</code>، بوابات جودة GitHub Actions، وعقود EVA الرياضية.
              </p>
            </div>
            <div style="font-weight: 700; color: #ec4899; font-size: 0.85rem; margin-top: 1rem;">عرض دليل الوكلاء و CI/CD &larr;</div>
          </a>

        </div>
      </div>

      <!-- Quick Installation & Architecture Overview AR -->
      <section id="quickstart" class="card" style="padding: 2.25rem; margin-bottom: 3rem;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
          <h2 style="font-size: 1.55rem; margin: 0;">1. التثبيت السريع ومتطلبات بيئة العمل</h2>
          <span class="badge" style="background: var(--accent-blue-bg); color: var(--accent-blue); border: 1px solid var(--accent-blue-border); font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 9999px;">PyPI: tasleemat</span>
        </div>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          حزمة تسليمات منشورة عبر مستودع PyPI الرسمي كحزمة بايثون خالصة (zero-dependency) تدعم إصدارات بايثون <strong>3.9 و 3.10 و 3.11 و 3.12 و 3.13</strong>.
          تتضمن التوزيعة كافة قوالب التسليمات الـ 114 ثنائية اللغة، ومخططات JSON المرافقة، وقواميس CSV، وأداة سطر الأوامر (CLI)، وخادم بروتوكول سياق النماذج (MCP).
        </p>
        <pre style="direction: ltr; text-align: left;"><code># التثبيت المباشر عبر مدير الحزم pip
pip install tasleemat

# التحقق من نجاح التثبيت وأدوات التشغيل
tasleemat --version
tasleemat-mcp --help</code></pre>
      </section>

      <!-- Architecture Flowchart AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 3rem;">
        <h3 style="font-size: 1.35rem; margin-bottom: 0.5rem; color: var(--text-main);">
          🏛️ المعمارية الهندسية لمنظومة تسليمات
        </h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 1.5rem;">
          مخطط تدفق العمليات والتكامل بين أدوات المطورين وخوادم MCP وأسراب الوكلاء مع النواة المعيارية الثابتة:
        </p>
        <pre><code class="language-mermaid">
flowchart TD
    subgraph Clients["واجهات المهندسين والذكاء الاصطناعي"]
        CLI["أداة سطر الأوامر (tasleemat)"]
        SDK["تطبيقات بايثون (tasleemat SDK)"]
        MCP["بيئات التطوير الذكية (Cursor, Claude)"]
        Swarm["أسراب الوكلاء الأذكياء (CrewAI, LangGraph)"]
    end

    subgraph Core["محرك المنظومة (tasleemat v2.5.0.post1)"]
        Catalog["محرك الفهرسة واستدعاء الأصول"]
        Tailoring["محرك التخصيص وتحديد الحجم"]
        Validator["محرك التحقق من المخططات 2020-12"]
        Attester["محرك الحسابات الموثقة (EVA PMO-06.05)"]
    end

    subgraph Data["النواة المعيارية الثابتة"]
        Forms["114 تسليمة (عربي وإنجليزي)"]
        Schemas["114 مخطط JSON معتمد"]
        Dicts["114 قاموس بيانات CSV"]
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
            <a href="{base_url}/ar/developers/cli/" class="btn-utility" style="font-size: 0.85rem;">الصفحة المخصصة لأداة الطرفية &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            تهيئة بيئات العمل المخصصة (<code>tasleemat init</code>)، البحث في فهرس التسليمات باللغتين العربية والإنجليزية (<code>tasleemat search</code>)، 
            إدارة مفاتيح النماذج اللغوية بأمان (<code>tasleemat config</code>)، توليد الوثائق آلياً (<code>tasleemat generate</code>)، 
            وتشغيل حزم الاختبارات الداخلية (<code>tasleemat test</code>).
          </p>
          <pre style="direction: ltr; text-align: left;"><code>tasleemat init --tier 2 --pack agile --lang ar --code "PRJ-CLOUD" --name "مشروع السحابة" --out ./prj</code></pre>
        </section>

        <section id="sdk" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">3. معمارية مكتبة بايثون (SDK)</h3>
            <a href="{base_url}/ar/developers/sdk/" class="btn-utility" style="font-size: 0.85rem;">الصفحة المخصصة لمكتبة بايثون &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            مكتبة بايثون خالصة تصدّر 8 دوال معتمدة: <code>list_artifacts</code> و <code>get_artifact_definition</code> و 
            <code>get_artifact_assets</code> و <code>get_artifact_asset</code> و <code>get_tailoring_profile</code> و 
            <code>validate_artifact_data</code> و <code>get_lexicon</code> و <code>render_artifact</code>.
          </p>
          <pre style="direction: ltr; text-align: left;"><code>import tasleemat
profile = tasleemat.get_tailoring_profile(tier=2, pack="agile")
report = tasleemat.validate_artifact_data("PMO-03.01", {{"project_id": "PRJ-01"}}, mode="draft")</code></pre>
        </section>

        <section id="mcp" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">4. خادم بروتوكول سياق النماذج (MCP)</h3>
            <a href="{base_url}/ar/developers/mcp/" class="btn-utility" style="font-size: 0.85rem;">الصفحة المخصصة لخادم MCP &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            خادم stdio قياسي ببروتوكول JSON-RPC 2.0 يتيح 6 أدوات متخصصة لبيئات Claude Desktop و Cursor والوكلاء الأذكياء:
            <code>tasleemat_list_forms</code> و <code>tasleemat_get_form</code> و <code>tasleemat_get_schema</code> و 
            <code>tasleemat_validate</code> و <code>tasleemat_tailor_project</code> و <code>tasleemat_calculate_eva</code>.
          </p>
          <pre style="direction: ltr; text-align: left;"><code># تشغيل خادم بروتوكول MCP
tasleemat-mcp</code></pre>
        </section>

        <section id="schemas" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">5. مخططات JSON وتنسيقات RFC المعيارية</h3>
            <a href="{base_url}/ar/developers/schemas/" class="btn-utility" style="font-size: 0.85rem;">الصفحة المخصصة للمخططات والتحقق &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            تقترن كافة الـ 114 تسليمة بمخططات JSON متوافقة بدقة مع معيار <strong>JSON Schema Draft 2020-12</strong>.
            يتم فرض قيود التنسيق الصارمة لـ RFC 3339 (التواريخ والأوقات)، RFC 4122 (معرفات UUID)، RFC 3986 (الروابط)، و RFC 5322 (البريد الإلكتروني).
          </p>
        </section>

        <section id="self-correction" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">6. حلقة التصحيح الذاتي التلقائي للوكلاء الأذكياء</h3>
            <a href="{base_url}/ar/developers/schemas/#self-correction" class="btn-utility" style="font-size: 0.85rem;">قراءة دليل التصحيح الذاتي &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            الوكلاء الأذكياء لا يخمنون: عندما تولد النماذج اللغوية بيانات JSON غير صحيحة، ترجع دالة <code>tasleemat.validate_artifact_data</code> 
            مسار الخطأ المحدد بدقة (JSON Pointer). يقوم الوكيل بدمج رسالة الخطأ في أمره التالي لإصلاح البيانات تلقائياً.
          </p>
        </section>

        <section id="multi-agent" class="card" style="padding: 2rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; margin: 0;">7. أسراب الوكلاء متعددي المهام (Multi-Agent Swarm)</h3>
            <a href="{base_url}/ar/developers/agentic/#multi-agent" class="btn-utility" style="font-size: 0.85rem;">قراءة دليل أسراب الوكلاء &larr;</a>
          </div>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 1rem;">
            تنسيق أدوار الذكاء الاصطناعي المتخصصة (مدير المشروع، مدقق الحوكمة، مسؤول المخاطر والأخلاقيات، الراعي التنفيذي) 
            باستخدام أطر مثل CrewAI و LangGraph مع الحفاظ على الحدود الصارمة لمراجعة واعتماد العنصر البشري قبل بوابات المراحل.
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
