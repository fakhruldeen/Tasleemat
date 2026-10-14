"""tools/site_builder/pages_dev/cli.py
Comprehensive CLI Tooling, Scaffolding, Tutorials & Automation Manual (English & Arabic).
"""

from tools.site_builder.theme import render_html_page
from tools.site_builder.pages_dev.nav import render_dev_subnav


def generate_dev_cli_en(base_url: str = "/Tasleemat") -> str:
    subnav = render_dev_subnav("cli", "en", base_url)
    
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/">Home</a> &gt; 
          <a href="{base_url}/developers/">Developers &amp; AI</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">CLI Tooling &amp; Automation</span>
        </nav>
        <div class="hero-pill"><span>⌨️ Command Line Interface (CLI)</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">CLI Tooling, Scaffolding &amp; Automation Manual</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto;">
          The authoritative command-line executable (<code>tasleemat</code>) for terminal automation, interactive workspace scaffolding, catalog querying, LLM synthesis, and air-gapped CI/CD execution.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Section 1: Overview & Environment Architecture -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">1. CLI Architecture &amp; Environment Variables</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          The <code>tasleemat</code> command-line executable is compiled with zero external C-dependencies. It runs natively across Linux, macOS, and Windows.
          It operates in two distinct execution modes: an <strong>interactive terminal wizard</strong> for practitioners and human managers, 
          and a <strong>deterministic headless flag mode</strong> optimized for shell scripts, cron jobs, and CI/CD pipelines.
        </p>
        
        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.75rem;">Global Environment Variables</h3>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>Variable</th>
                <th>Default Value</th>
                <th>Description</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>TASLEEMAT_HOME</code></td>
                <td><code>~/.tasleemat</code></td>
                <td>Root directory for localized caches, project registry, and telemetry.</td>
              </tr>
              <tr>
                <td><code>TASLEEMAT_CONFIG_FILE</code></td>
                <td><code>~/.tasleemat/config.json</code></td>
                <td>Location of secure API keys and local LLM endpoints (file permissions <code>0600</code>).</td>
              </tr>
              <tr>
                <td><code>TASLEEMAT_DEFAULT_LANG</code></td>
                <td><code>en</code></td>
                <td>Fallback language for outputs and templates if <code>--lang</code> flag is omitted (<code>en</code> or <code>ar</code>).</td>
              </tr>
              <tr>
                <td><code>TASLEEMAT_NO_COLOR</code></td>
                <td><code>0</code></td>
                <td>Set to <code>1</code> to disable ANSI terminal colors for raw logging pipelines.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.75rem;">Standard Exit Codes Matrix</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 0.75rem;">
          The CLI produces strict POSIX exit codes to guarantee deterministic pipeline control:
        </p>
        <ul style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.8; padding-left: 1.5rem;">
          <li><code>0</code>: <strong>SUCCESS</strong> - Command completed successfully with all outputs written.</li>
          <li><code>1</code>: <strong>VALIDATION / RUNTIME ERROR</strong> - Schema validation failure, missing template, or LLM connection failure.</li>
          <li><code>2</code>: <strong>INVALID ARGUMENTS</strong> - Unrecognized flag, unsupported tier number, or illegal language code.</li>
          <li><code>127</code>: <strong>DELIVERABLE NOT FOUND</strong> - Specified artifact ID (e.g. <code>PMO-99.99</code>) does not exist in the 114 catalog.</li>
        </ul>
      </div>

      <!-- Section 2: Command Reference -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">2. Exhaustive Command Reference &amp; Flags</h2>

        <!-- Command 1: init -->
        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-blue); margin-bottom: 0.5rem;">A. <code>tasleemat init</code> (Workspace Scaffolding)</h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            Scaffolds an isolated project repository pre-tailored to your governance tier (1, 2, or 3) and delivery archetype pack. 
            For every required deliverable, the CLI generates the complete 5-asset bundle:
            <strong>Template (Markdown)</strong>, <strong>Practitioner Guide (Markdown)</strong>, <strong>Realistic Example (Markdown)</strong>, 
            <strong>Companion Schema (JSON Draft 2020-12)</strong>, and <strong>Data Dictionary (CSV)</strong>.
          </p>
          <pre><code># Interactive wizard mode (prompts for project metadata)
tasleemat init

# Full headless automation flags (e.g. Tier 2 Agile Project in Arabic)
tasleemat init \\
  --tier 2 \\
  --pack agile \\
  --lang ar \\
  --code "PRJ-2026-CLOUD" \\
  --name "منصة التحول الرقمي السحابي" \\
  --pm "سارة الأحمد" \\
  --sponsor "د. خالد المنصور" \\
  --out ./projects/PRJ-2026-CLOUD \\
  --force

# Enterprise Tier 1 Hybrid Project with Bilingual (both) Deliverables
tasleemat init \\
  --tier 1 \\
  --pack hybrid \\
  --lang both \\
  --code "PRJ-CORE-MIGRATE" \\
  --name "Core Banking Replacement Program" \\
  --pm "Fahad Al-Harbi" \\
  --sponsor "Chief Operating Officer" \\
  --out ./enterprise_workspace</code></pre>
          
          <div style="margin-top: 1rem; background: var(--bg-main); padding: 1rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
            <div style="font-size: 0.85rem; font-weight: 700; margin-bottom: 0.4rem;">Supported Flags:</div>
            <ul style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6; padding-left: 1.25rem; margin: 0;">
              <li><code>--tier &lt;1|2|3&gt;</code>: Governance tier (1 = Strategic/Mega, 2 = Standard Enterprise, 3 = Lean/Fast-track). Default: 2.</li>
              <li><code>--pack &lt;general|agile|ai|predictive|hybrid&gt;</code>: Delivery methodology pack. Default: general.</li>
              <li><code>--lang &lt;en|ar|both&gt;</code>: Language generation mode. Default: en.</li>
              <li><code>--code &lt;string&gt;</code>: Unique project identifier code.</li>
              <li><code>--name &lt;string&gt;</code>: Official project title.</li>
              <li><code>--pm &lt;string&gt;</code>: Name of assigned Project Manager.</li>
              <li><code>--sponsor &lt;string&gt;</code>: Name and title of Project Sponsor.</li>
              <li><code>--out &lt;path&gt;</code>: Target filesystem directory path.</li>
              <li><code>--force</code>: Overwrites existing destination directory without prompt.</li>
            </ul>
          </div>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Command 2: list & search -->
        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">B. <code>tasleemat list</code> &amp; <code>search</code> (Catalog Exploration)</h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            Inspect the 114 canonical deliverables directly from your terminal. Supports phase filtering, tier filtering, and JSON output formatting for piping into <code>jq</code>.
          </p>
          <pre><code># List all 114 deliverables in English or Arabic
tasleemat list --lang en
tasleemat list --lang ar

# Filter by project lifecycle phase code (00 to 07)
tasleemat list --phase 04 --lang en

# Filter by tier and pack
tasleemat list --tier 3 --pack agile

# Output catalog as machine-readable JSON array
tasleemat list --json | jq '.[0]'

# Full-text fuzzy search across deliverable titles, keywords, and IDs
tasleemat search "Charter"
tasleemat search "ميثاق" --lang ar
tasleemat search "PMO-04.08.02"</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Command 3: config -->
        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-amber); margin-bottom: 0.5rem;">C. <code>tasleemat config</code> (AI Model Credentials Management)</h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            Securely configure LLM provider API credentials and default models for automated document synthesis. 
            All tokens are stored locally in <code>~/.tasleemat/config.json</code> with POSIX permissions <code>0600</code>.
          </p>
          <pre><code># Configure Google Gemini
tasleemat config set --provider gemini --model gemini-2.5-flash --key "AIzaSy..."

# Configure OpenAI
tasleemat config set --provider openai --model gpt-4o --key "sk-proj-..."

# Configure Anthropic Claude
tasleemat config set --provider anthropic --model claude-3-5-sonnet-20241022 --key "sk-ant-..."

# Configure Local Ollama Endpoint (Air-Gapped / High-Security Setup)
tasleemat config set --provider ollama --model llama3.2 --endpoint "http://localhost:11434"

# Display configured providers (keys are automatically masked with asterisks)
tasleemat config show

# Reset credentials for a specific provider
tasleemat config reset --provider openai</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Command 4: generate -->
        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.25rem; color: #8b5cf6; margin-bottom: 0.5rem;">D. <code>tasleemat generate</code> (Automated Document Synthesis)</h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            Synthesize compliant markdown deliverables from raw meeting notes or text requirements using your configured LLM provider.
            Also features an offline <code>--mock</code> mode for test environments.
          </p>
          <pre><code># Generate Project Charter (PMO-03.01) from kick-off notes file
tasleemat generate \\
  --form PMO-03.01 \\
  --notes ./kickoff_notes.txt \\
  --lang en \\
  --out ./Project_Charter.md

# Pipe notes directly from stdin (ideal for shell automation)
cat &lt;&lt; 'EOF' | tasleemat generate --form PMO-04.08.02 --lang ar --out ./Risk_Register.md -
المشروع يواجه احتمالية تأخر وصول الخوادم بنسبة 40%، مما قد يعطل الإطلاق أسبوعين.
المسؤول عن المتابعة هو مهندس البنية التحتية.
EOF

# Offline mock mode for CI/CD test runs (zero tokens consumed, runs in 50ms)
tasleemat generate \\
  --form PMO-03.01 \\
  --notes "Mock input data" \\
  --mock \\
  --out ./mock_charter.md</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Command 5: test & mcp -->
        <div>
          <h3 style="font-size: 1.25rem; color: #ec4899; margin-bottom: 0.5rem;">E. <code>tasleemat test</code> &amp; <code>tasleemat mcp</code></h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            Execute internal verification suites or launch the stdio Model Context Protocol (MCP) server for IDE integration:
          </p>
          <pre><code># Run complete automated test suite (140+ unit and integration checks)
tasleemat test -v

# Run tests with fail-fast mode
tasleemat test -v --failfast

# Start the Model Context Protocol stdio server for Claude Desktop / Cursor
tasleemat mcp</code></pre>
        </div>

      </div>

      <!-- Section 3: Step-by-Step Tutorials -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">3. Practical Step-by-Step Tutorials</h2>

        <!-- Tutorial 1 -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.75rem;">
            Tutorial 1: Zero-to-Production Enterprise Workspace Scaffolding
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            Follow this end-to-end walkthrough to create an audited project directory for a strategic healthcare transformation initiative:
          </p>
          <ol style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.8; padding-left: 1.5rem; margin-bottom: 1rem;">
            <li><strong>Discover Required Deliverables:</strong> Run <code>tasleemat list --tier 1 --pack hybrid</code> to inspect the required 42 deliverables.</li>
            <li><strong>Scaffold the Workspace:</strong> Execute the headless initialization command:
              <pre><code>tasleemat init \\
  --tier 1 \\
  --pack hybrid \\
  --lang en \\
  --code "PRJ-2026-MED" \\
  --name "National Health EHR Integration" \\
  --pm "Dr. Mariam Al-Ghamdi" \\
  --sponsor "Ministerial Steering Committee" \\
  --out ./PRJ-2026-MED</code></pre>
            </li>
            <li><strong>Inspect Directory Structure:</strong> Navigate into <code>./PRJ-2026-MED</code>. You will find:
              <pre><code>PRJ-2026-MED/
├── manifest.json                  # Machine-readable workspace catalog &amp; SHA-256 hashes
├── 01_Initiation/
│   ├── PMO-03.01_Project_Charter/
│   │   ├── template.md            # Pure Markdown template with placeholder brackets
│   │   ├── guide.md               # Practitioner authoring instructions &amp; RACI tips
│   │   ├── example.md             # Fully filled realistic enterprise example
│   │   ├── schema.json            # Companion JSON Schema Draft 2020-12
│   │   └── dictionary.csv         # Standardized field dictionary &amp; data types
│   └── PMO-03.02_Stakeholder_Register/
└── ...</code></pre>
            </li>
            <li><strong>Synthesize Charter from Raw Notes:</strong> Feed your kickoff meeting notes directly into the synthesizer:
              <pre><code>tasleemat generate \\
  --form PMO-03.01 \\
  --notes ./meeting_minutes.txt \\
  --out ./PRJ-2026-MED/01_Initiation/PMO-03.01_Project_Charter/template.md</code></pre>
            </li>
          </ol>
        </div>

        <!-- Tutorial 2 -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.75rem;">
            Tutorial 2: Air-Gapped High-Security Enterprise Setup
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            For defense, banking, and government environments with zero outbound internet connectivity:
          </p>
          <ol style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.8; padding-left: 1.5rem;">
            <li><strong>Transfer Wheel Package:</strong> Copy the pre-built <code>tasleemat-2.5.0.post1-py3-none-any.whl</code> to your air-gapped bastion host via verified removable media.</li>
            <li><strong>Offline Installation:</strong>
              <pre><code>pip install --no-index --find-links . tasleemat-2.5.0.post1-py3-none-any.whl</code></pre>
            </li>
            <li><strong>Configure Local Ollama Instance:</strong> Point Tasleemat to an on-premises air-gapped LLM instance:
              <pre><code>tasleemat config set --provider ollama --model llama3.2 --endpoint "http://10.0.50.12:11434"</code></pre>
            </li>
            <li><strong>Verify Zero Telemetry:</strong> Run <code>tasleemat test -v</code>. All 146 internal tests execute in memory without emitting any outbound HTTP requests.</li>
          </ol>
        </div>

        <!-- Tutorial 3 -->
        <div>
          <h3 style="font-size: 1.2rem; color: var(--accent-amber); margin-bottom: 0.75rem;">
            Tutorial 3: Multi-Project Enterprise Portfolio Batch Provisioning
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            Use this bash automation recipe to batch-scaffold multiple project workspaces from a centralized portfolio CSV registry:
          </p>
          <pre><code>#!/usr/bin/env bash
# provision_portfolio.sh - Batch PMO Workspace Initializer
set -euo pipefail

CSV_FILE="portfolio_registry.csv"
OUTPUT_ROOT="./enterprise_pmo_workspaces"

mkdir -p "$OUTPUT_ROOT"

echo "Reading projects from $CSV_FILE..."
# CSV Format: code,name,tier,pack,lang,pm,sponsor
tail -n +2 "$CSV_FILE" | while IFS=',' read -r code name tier pack lang pm sponsor; do
    echo "=========================================================="
    echo "Scaffolding: [$code] $name (Tier $tier, Pack $pack)..."
    
    tasleemat init \\
      --code "$code" \\
      --name "$name" \\
      --tier "$tier" \\
      --pack "$pack" \\
      --lang "$lang" \\
      --pm "$pm" \\
      --sponsor "$sponsor" \\
      --out "$OUTPUT_ROOT/$code" \\
      --force
      
    echo "Successfully created: $OUTPUT_ROOT/$code"
done

echo "Portfolio provisioning complete! All workspaces verified."</code></pre>
        </div>

      </div>

      <!-- Section 4: CI/CD & Shell Recipes -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">4. Enterprise DevOps &amp; Shell Recipes</h2>
        
        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">A. Git Pre-Commit Hook</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-bottom: 0.75rem;">
          Place this script in <code>.git/hooks/pre-commit</code> to prevent committing corrupted workspaces or invalid deliverable schemas:
        </p>
        <pre><code>#!/usr/bin/env bash
# .git/hooks/pre-commit
echo "[Tasleemat Hook] Verifying project integrity..."

# 1. Run internal unit tests
if ! tasleemat test &gt; /dev/null 2&gt;&amp;1; then
    echo "ERROR: Tasleemat regression tests failed! Aborting commit."
    exit 1
fi

echo "[Tasleemat Hook] Pre-commit checks passed successfully."
exit 0</code></pre>

        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">B. Parsing Catalog via <code>jq</code></h3>
        <pre><code># Extract deliverable codes and English names for Phase 03
tasleemat list --phase 03 --json | jq -r '.[] | "\\(.id): \\(.name_en)"'

# Count deliverables allocated to Tier 3
tasleemat list --tier 3 --json | jq 'length'</code></pre>
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
    subnav = render_dev_subnav("cli", "ar", base_url)
    
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/ar/">الرئيسية</a> &gt; 
          <a href="{base_url}/ar/developers/">المطورون والذكاء الاصطناعي</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">أداة الطرفية والأتمتة (CLI)</span>
        </nav>
        <div class="hero-pill"><span>⌨️ أداة سطر الأوامر (CLI)</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">دليل أداة الطرفية وسطر الأوامر والأتمتة</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
          المرجع الشامل لأداة التشغيل عبر سطر الأوامر (<code>tasleemat</code>) لأتمتة بيئات العمل، تهيئة مجلدات المشاريع، البحث في الفهرس المعياري، التوليد الآلي عبر الذكاء الاصطناعي، والتشغيل في البيئات المعزولة.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Section 1: Overview & Environment Architecture AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">1. معمارية الأداة ومتغيرات البيئة البرمجية</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          تم بناء أداة <code>tasleemat</code> كأداة طرفية بلغة بايثون الخالصة بدون أي مكتبات خارجية ثقيلة، وهي تعمل مباشرة على أنظمة Linux و macOS و Windows.
          توفر الأداة نمطين للتشغيل: <strong>نمط المعالج التفاعلي</strong> الموجه لمديري المشاريع والممارسين، و <strong>نمط المعاملات المؤتمتة (Flags Mode)</strong> الموجه لسكربتات Bash وأنظمة CI/CD.
        </p>
        
        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.75rem;">متغيرات البيئة العامة (Environment Variables)</h3>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>المتغير</th>
                <th>القيمة الافتراضية</th>
                <th>الوصف والوظيفة</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>TASLEEMAT_HOME</code></td>
                <td><code>~/.tasleemat</code></td>
                <td>المجلد الرئيسي للبيانات المحلية المؤقتة وسجلات المشاريع.</td>
              </tr>
              <tr>
                <td><code>TASLEEMAT_CONFIG_FILE</code></td>
                <td><code>~/.tasleemat/config.json</code></td>
                <td>ملف حفظ مفاتيح واجهات الذكاء الاصطناعي المشفر بصلاحيات أمان <code>0600</code>.</td>
              </tr>
              <tr>
                <td><code>TASLEEMAT_DEFAULT_LANG</code></td>
                <td><code>ar</code></td>
                <td>اللغة الافتراضية للتوليد في حال عدم تمرير خيار <code>--lang</code>.</td>
              </tr>
              <tr>
                <td><code>TASLEEMAT_NO_COLOR</code></td>
                <td><code>0</code></td>
                <td>تعيينه إلى <code>1</code> لتعطيل ألوان ANSI في سجلات التشغيل النصية.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.75rem;">مصفوفة رموز الخروج القياسية (Exit Codes)</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 0.75rem;">
          تلتزم الأداة بمعايير POSIX لرموز الخروج لتمكين خطوط الأتمتة من اتخاذ القرارات بدقة:
        </p>
        <ul style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.8; padding-right: 1.5rem;">
          <li><code>0</code>: <strong>نجاح كامل (SUCCESS)</strong> - تم تنفيذ الأمر بنجاح وحفظ كافة المخرجات.</li>
          <li><code>1</code>: <strong>خطأ تشغيلي أو فشل تحقق (ERROR)</strong> - عدم تطابق البيانات مع مخطط JSON أو تعذر الاتصال بالنموذج.</li>
          <li><code>2</code>: <strong>معاملات غير صالحة (INVALID ARGS)</strong> - خيار غير معروف أو مستوى حوكمة غير مسجل.</li>
          <li><code>127</code>: <strong>تسليمة غير موجودة (NOT FOUND)</strong> - رمز التسليمة المحدد غير موجود في الفهرس المعياري.</li>
        </ul>
      </div>

      <!-- Section 2: Command Reference AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">2. المرجع الشامل لكافة الأوامر والمعاملات</h2>

        <!-- Command 1: init -->
        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-blue); margin-bottom: 0.5rem;">أ. <code>tasleemat init</code> (تهيئة وتجهيز بيئات عمل المشاريع)</h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            يقوم أمر <code>init</code> ببناء بيئة عمل متكاملة للمشروع مخصصة وفق مستوى الحوكمة (المستوى 1 أو 2 أو 3) وحزمة المنهجية المتبعة.
            ينشئ الأمر لكل تسليمة حزمة متكاملة من 5 ملفات:
            <strong>القالب الأساسي (Markdown)</strong>، <strong>دليل الممارس (Markdown)</strong>، <strong>مثال واقعي مكتمل (Markdown)</strong>، 
            <strong>مخطط التحقق الآلي (JSON Draft 2020-12)</strong>، و <strong>قاموس الحقول والبيانات (CSV)</strong>.
          </p>
          <pre style="direction: ltr; text-align: left;"><code># نمط المعالج التفاعلي (يسألك خطوة بخطوة عن بيانات المشروع)
tasleemat init

# نمط الأتمتة الكامل عبر المعاملات (مشروع رشيق من المستوى 2 باللغة العربية)
tasleemat init \\
  --tier 2 \\
  --pack agile \\
  --lang ar \\
  --code "PRJ-2026-CLOUD" \\
  --name "منصة التحول الرقمي السحابي" \\
  --pm "سارة الأحمد" \\
  --sponsor "د. خالد المنصور" \\
  --out ./projects/PRJ-2026-CLOUD \\
  --force

# مشروع استراتيجي كبير (المستوى 1) بكامل الوثائق ثنائية اللغة (عربي وإنجليزي)
tasleemat init \\
  --tier 1 \\
  --pack hybrid \\
  --lang both \\
  --code "PRJ-CORE-MIGRATE" \\
  --name "برنامج استبدال الأنظمة المصرفية الأساسية" \\
  --pm "فهد الحربي" \\
  --sponsor "الرئيس التنفيذي للعمليات" \\
  --out ./enterprise_workspace</code></pre>
          
          <div style="margin-top: 1rem; background: var(--bg-main); padding: 1rem; border-radius: 0.5rem; border: 1px solid var(--border-color);">
            <div style="font-size: 0.85rem; font-weight: 700; margin-bottom: 0.4rem;">المعاملات والخيارات المدعومة:</div>
            <ul style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.7; padding-right: 1.25rem; margin: 0;">
              <li><code>--tier &lt;1|2|3&gt;</code>: مستوى حجم وحوكمة المشروع (1 = مشاريع كبرى/استراتيجية، 2 = مشاريع قياسية، 3 = مشاريع رشيقة سريعة). القيمة الافتراضية: 2.</li>
              <li><code>--pack &lt;general|agile|ai|predictive|hybrid&gt;</code>: حزمة منهجية التسليم. القيمة الافتراضية: general.</li>
              <li><code>--lang &lt;en|ar|both&gt;</code>: لغة توليد الملفات (عربي، إنجليزي، أو كلتا اللغتين). القيمة الافتراضية: ar.</li>
              <li><code>--code &lt;string&gt;</code>: الرمز التعريفي للمشروع (مثل: PRJ-2026-001).</li>
              <li><code>--name &lt;string&gt;</code>: الاسم الرسمي المعتمد للمشروع.</li>
              <li><code>--pm &lt;string&gt;</code>: اسم مدير المشروع المسؤول.</li>
              <li><code>--sponsor &lt;string&gt;</code>: اسم الراعي التنفيذي للمشروع.</li>
              <li><code>--out &lt;path&gt;</code>: مسار مجلد الإخراج في نظام الملفات.</li>
              <li><code>--force</code>: استبدال المجلد الحالي في حال وجوده دون توقف.</li>
            </ul>
          </div>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Command 2: list & search AR -->
        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">ب. <code>tasleemat list</code> و <code>search</code> (استعراض الفهرس والبحث)</h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            استعراض الـ 114 تسليمة معيارية مباشرة من الطرفية مع إمكانية التصفية بحسب مراحل المشروع، مستويات الحوكمة، واستخراج المخرجات بصيغة JSON.
          </p>
          <pre style="direction: ltr; text-align: left;"><code># استعراض كافة التسليمات باللغة العربية أو الإنجليزية
tasleemat list --lang ar
tasleemat list --lang en

# تصفية التسليمات بحسب مرحلة دورة حياة المشروع (المراحل من 00 إلى 07)
tasleemat list --phase 04 --lang ar

# تصفية التسليمات بحسب المستوى والمنهجية
tasleemat list --tier 3 --pack agile

# تصدير التسليمات بصيغة JSON المعيارية للمعالجة البرمجية
tasleemat list --json | jq '.[0]'

# البحث الذكي الشامل بالعناوين والكلمات المفتاحية والرموز
tasleemat search "ميثاق" --lang ar
tasleemat search "Charter" --lang en
tasleemat search "PMO-04.08.02"</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Command 3: config AR -->
        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-amber); margin-bottom: 0.5rem;">ج. <code>tasleemat config</code> (إدارة مفاتيح وبيئات الذكاء الاصطناعي)</h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            إدارة مفاتيح الربط مع نماذج الذكاء الاصطناعي والنماذج المحلية بشكل آمن في الملف المحلي <code>~/.tasleemat/config.json</code> بصلاحيات مقيدة.
          </p>
          <pre style="direction: ltr; text-align: left;"><code># إعداد وتفعيل Google Gemini
tasleemat config set --provider gemini --model gemini-2.5-flash --key "AIzaSy..."

# إعداد وتفعيل OpenAI GPT-4o
tasleemat config set --provider openai --model gpt-4o --key "sk-proj-..."

# إعداد وتفعيل Anthropic Claude
tasleemat config set --provider anthropic --model claude-3-5-sonnet-20241022 --key "sk-ant-..."

# إعداد خادم محلي Ollama (للبيئات المعزولة وعالية الأمان بدون إنترنت)
tasleemat config set --provider ollama --model llama3.2 --endpoint "http://localhost:11434"

# عرض الإعدادات الحالية (يتم حجب المفاتيح السرية تلقائياً بنجوم)
tasleemat config show

# إعادة تعيين مفاتيح مزود معين
tasleemat config reset --provider openai</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Command 4: generate AR -->
        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.25rem; color: #8b5cf6; margin-bottom: 0.5rem;">د. <code>tasleemat generate</code> (التوليد الذكي للوثائق)</h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            توليد مسودات الوثائق بصيغة Markdown من مذكرات الاجتماعات الخام باستخدام النماذج اللغوية، مع خيار المحاكاة بدون إنترنت (<code>--mock</code>).
          </p>
          <pre style="direction: ltr; text-align: left;"><code># توليد ميثاق المشروع (PMO-03.01) من ملف مذكرات الاجتماع
tasleemat generate \\
  --form PMO-03.01 \\
  --notes ./kickoff_notes.txt \\
  --lang ar \\
  --out ./Project_Charter.md

# التمرير المباشر للنصوص عبر مجرى الإدخال القياسي (stdin piping)
cat &lt;&lt; 'EOF' | tasleemat generate --form PMO-04.08.02 --lang ar --out ./Risk_Register.md -
المشروع يواجه احتمالية تأخر وصول الخوادم بنسبة 40%، مما قد يعطل الإطلاق أسبوعين.
المسؤول عن المتابعة هو مهندس البنية التحتية.
EOF

# نمط المحاكاة بدون استهلاك أي رموز (mock mode) لاختبارات خطوط CI/CD
tasleemat generate \\
  --form PMO-03.01 \\
  --notes "بيانات وهمية للاختبار" \\
  --mock \\
  --out ./mock_charter.md</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Command 5: test & mcp AR -->
        <div>
          <h3 style="font-size: 1.25rem; color: #ec4899; margin-bottom: 0.5rem;">هـ. <code>tasleemat test</code> و <code>tasleemat mcp</code></h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            تشغيل حزم الاختبارات الداخلية والتحقق من صحة البيئة، أو إطلاق خادم بروتوكول سياق النموذج (MCP):
          </p>
          <pre style="direction: ltr; text-align: left;"><code># تشغيل كامل حزمة الاختبارات الآلية (أكثر من 140 اختباراً)
tasleemat test -v

# تشغيل الاختبارات مع التوقف عند أول خطأ
tasleemat test -v --failfast

# تشغيل خادم بروتوكول MCP عبر بروتوكول stdio للتكامل مع Cursor و Claude
tasleemat mcp</code></pre>
        </div>

      </div>

      <!-- Section 3: Step-by-Step Tutorials AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">3. أدلة تطبيقية عملية خطوة بخطوة (Tutorials)</h2>

        <!-- Tutorial 1 AR -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.75rem;">
            الدليل 1: تجهيز بيئة عمل متكاملة لمشروع مؤسسي من الصفر
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            خطوات عملية لبناء بيئة عمل معتمدة لمشروع رعاية صحية رقمي استراتيجي:
          </p>
          <ol style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.9; padding-right: 1.5rem; margin-bottom: 1rem;">
            <li><strong>استكشاف التسليمات المطلوبة:</strong> نفذ أمر <code>tasleemat list --tier 1 --pack hybrid</code> لمعاينة الـ 42 تسليمة المقررة.</li>
            <li><strong>تهيئة مجلد المشروع:</strong> نفذ أمر التهيئة الآلي:
              <pre style="direction: ltr; text-align: left;"><code>tasleemat init \\
  --tier 1 \\
  --pack hybrid \\
  --lang ar \\
  --code "PRJ-2026-MED" \\
  --name "منصة السجلات الطبية الوطنية الموحدة" \\
  --pm "د. مريم الغامدي" \\
  --sponsor "اللجنة التوجيهية للتحول الرقمي" \\
  --out ./PRJ-2026-MED</code></pre>
            </li>
            <li><strong>معاينة هيكلية المجلدات المولدة:</strong> ادخل إلى مجلد <code>./PRJ-2026-MED</code> وستجد:
              <pre style="direction: ltr; text-align: left;"><code>PRJ-2026-MED/
├── manifest.json                  # فهرس المشروع وقيم بصمات SHA-256 للملفات
├── 01_Initiation/
│   ├── PMO-03.01_Project_Charter/
│   │   ├── template.md            # قالب Markdown مع وسوم الأقواس الحاصرة
│   │   ├── guide.md               # دليل الممارس وإرشادات المسؤوليات RACI
│   │   ├── example.md             # مثال واقعي متكامل ومكتمل البيانات
│   │   ├── schema.json            # مخطط JSON Draft 2020-12 للتحقق الآلي
│   │   └── dictionary.csv         # قاموس الحقول المعياري وأنواع البيانات
│   └── PMO-03.02_Stakeholder_Register/
└── ...</code></pre>
            </li>
            <li><strong>توليد مسودة ميثاق المشروع من محضر الاجتماع:</strong>
              <pre style="direction: ltr; text-align: left;"><code>tasleemat generate \\
  --form PMO-03.01 \\
  --notes ./meeting_minutes.txt \\
  --lang ar \\
  --out ./PRJ-2026-MED/01_Initiation/PMO-03.01_Project_Charter/template.md</code></pre>
            </li>
          </ol>
        </div>

        <!-- Tutorial 2 AR -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.75rem;">
            الدليل 2: التشغيل في البيئات الحكومية والمصرفية المعزولة (Air-Gapped)
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            للبيئات فائقة الأمان التي تمنع الاتصال بالإنترنت الخارجي منعاً باتاً:
          </p>
          <ol style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.9; padding-right: 1.5rem;">
            <li><strong>نقل حزمة التثبيت:</strong> انسخ ملف <code>tasleemat-2.5.0.post1-py3-none-any.whl</code> إلى الخادم المعزول عبر وسائط آمنة ومعتمدة.</li>
            <li><strong>التثبيت دون اتصال بالإنترنت:</strong>
              <pre style="direction: ltr; text-align: left;"><code>pip install --no-index --find-links . tasleemat-2.5.0.post1-py3-none-any.whl</code></pre>
            </li>
            <li><strong>توجيه الأداة لخادم ذكاء اصطناعي محلي:</strong>
              <pre style="direction: ltr; text-align: left;"><code>tasleemat config set --provider ollama --model llama3.2 --endpoint "http://10.0.50.12:11434"</code></pre>
            </li>
            <li><strong>التحقق من انعدام حركة البيانات الخارجية:</strong> نفذ <code>tasleemat test -v</code> لتأكيد نجاح كافة الاختبارات بدون أي اتصال بالإنترنت.</li>
          </ol>
        </div>

        <!-- Tutorial 3 AR -->
        <div>
          <h3 style="font-size: 1.2rem; color: var(--accent-amber); margin-bottom: 0.75rem;">
            الدليل 3: أتمتة تهيئة محفظة مشاريع كاملة عبر سكربت Bash
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            سكربت متقدم لقراءة سجل محفظة المشاريع من ملف CSV وإنشاء كافة بيئات العمل دفعة واحدة:
          </p>
          <pre style="direction: ltr; text-align: left;"><code>#!/usr/bin/env bash
# provision_portfolio.sh - سكربت تهيئة محفظة المشاريع المؤسسية
set -euo pipefail

CSV_FILE="portfolio_registry.csv"
OUTPUT_ROOT="./enterprise_pmo_workspaces"

mkdir -p "$OUTPUT_ROOT"

echo "جاري قراءة المشاريع من ملف $CSV_FILE..."
# تنسيق الملف: code,name,tier,pack,lang,pm,sponsor
tail -n +2 "$CSV_FILE" | while IFS=',' read -r code name tier pack lang pm sponsor; do
    echo "=========================================================="
    echo "جاري إنشاء مشروع: [$code] $name (المستوى $tier، الحزمة $pack)..."
    
    tasleemat init \\
      --code "$code" \\
      --name "$name" \\
      --tier "$tier" \\
      --pack "$pack" \\
      --lang "$lang" \\
      --pm "$pm" \\
      --sponsor "$sponsor" \\
      --out "$OUTPUT_ROOT/$code" \\
      --force
      
    echo "تم بنجاح إنشاء مجلد: $OUTPUT_ROOT/$code"
done

echo "اكتملت تهيئة المحفظة بالكامل بنجاح!"</code></pre>
        </div>

      </div>

      <!-- Section 4: CI/CD & Shell Recipes AR -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">4. خطوط الأتمتة وأدوات Git</h2>
        
        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">أ. خطاف التحقق التلقائي قبل الالتزام (Git Pre-Commit Hook)</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.8; margin-bottom: 0.75rem;">
          ضع هذا السكربت في <code>.git/hooks/pre-commit</code> لمنع إيداع أي تسليمات معطوبة أو غير مطابقة:
        </p>
        <pre style="direction: ltr; text-align: left;"><code>#!/usr/bin/env bash
# .git/hooks/pre-commit
echo "[Tasleemat Hook] التحقق من سلامة وثائق المشروع..."

# تشغيل الاختبارات الآلية
if ! tasleemat test &gt; /dev/null 2&gt;&amp;1; then
    echo "خطأ: فشلت اختبارات التحقق من الوثائق! تم إيقاف الالتزام."
    exit 1
fi

echo "[Tasleemat Hook] تم التحقق بنجاح، يمكنك المتابعة."
exit 0</code></pre>

        <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">ب. استخراج وتحليل الفهرس عبر <code>jq</code></h3>
        <pre style="direction: ltr; text-align: left;"><code># استخراج رموز وأسماء تسليمات المرحلة 03 باللغة العربية
tasleemat list --phase 03 --json | jq -r '.[] | "\\(.id): \\(.name_ar)"'

# عد التسليمات المخصصة للمستوى 3
tasleemat list --tier 3 --json | jq 'length'</code></pre>
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
