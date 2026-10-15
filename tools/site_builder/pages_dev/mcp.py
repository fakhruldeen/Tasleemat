"""tools/site_builder/pages_dev/mcp.py
Model Context Protocol (MCP) Server, JSON-RPC 2.0 Stdio Reference, IDE Integrations & Tutorials (English & Arabic).
"""

from tools.site_builder.theme import render_html_page
from tools.site_builder.pages_dev.nav import render_dev_subnav


def generate_dev_mcp_en(base_url: str = "/Tasleemat") -> str:
    subnav = render_dev_subnav("mcp", "en", base_url)
    
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/">Home</a> &gt; 
          <a href="{base_url}/developers/">Developers &amp; AI</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">MCP Server</span>
        </nav>
        <div class="hero-pill"><span>🔌 Model Context Protocol (MCP)</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">Model Context Protocol (MCP) Server Manual</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto;">
          Connect Anthropic Claude Desktop, Cursor, and autonomous AI agents directly to the 114 project deliverables and Draft 2020-12 schemas via standard JSON-RPC 2.0 stdio communication.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Section 1: Architecture & Protocol Handshake -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">1. Protocol Architecture &amp; Handshake Flow</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          The Model Context Protocol (MCP) is an open specification enabling AI assistants to securely connect to external data repositories and execution tools.
          Tasleemat packages an official standalone executable (<code>tasleemat-mcp</code>) that communicates via standard input/output (<code>stdio</code>) 
          using strict <strong>JSON-RPC 2.0</strong> framing. This design eliminates TCP port binding conflicts and allows seamless local sandboxing.
        </p>
        
        <pre><code class="language-mermaid">
sequenceDiagram
    autonumber
    actor User as Engineer / PM
    participant Host as AI Client (Cursor / Claude Desktop)
    participant Server as Tasleemat MCP (stdio)
    participant Engine as Tasleemat Core Engine

    Host->>Server: JSON-RPC "initialize" (capabilities, client info)
    Server-->>Host: Server capabilities (tools advertised)
    Host->>Server: JSON-RPC "notifications/initialized"
    User->>Host: "Tailor deliverables for Tier 2 Agile project"
    Host->>Server: "tools/call" (name: "tasleemat_tailor_project", args: {{tier: 2, pack: "agile"}})
    Server->>Engine: get_tailoring_profile(tier=2, pack="agile")
    Engine-->>Server: List of 34 Deliverable IDs
    Server-->>Host: JSON-RPC Result (structured deliverable manifest)
    Host->>User: "Here is your tailored governance manifest..."
        </code></pre>
      </div>

      <!-- Section 2: IDE Configurations -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <div style="background: linear-gradient(135deg, rgba(37, 99, 235, 0.08) 0%, rgba(139, 92, 246, 0.08) 100%); border: 1px solid rgba(37, 99, 235, 0.25); border-radius: 0.75rem; padding: 1.25rem; margin-bottom: 2rem;">
          <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem;">
            <div>
              <span class="brand-badge" style="background: #10b981; color: white; margin-bottom: 0.5rem; display: inline-block;">Official MCP Registry</span>
              <h3 style="font-size: 1.15rem; margin: 0.25rem 0; color: var(--text-main);">Registered ID: <code>io.github.fakhruldeen/tasleemat</code> (v2.6.0)</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); margin: 0;">Verified standard stdio Model Context Protocol server. Launch with zero setup using uvx or pip.</p>
            </div>
            <code style="background: var(--bg-card); border: 1px solid var(--border-color); padding: 0.5rem 0.85rem; border-radius: 0.4rem; font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent-blue);">uvx tasleemat-mcp</code>
          </div>
        </div>

        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">2. IDE &amp; Assistant Configuration Setup</h2>

        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.5rem;">A. Anthropic Claude Desktop</h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Add the following snippet to your <code>claude_desktop_config.json</code> file:
          </p>
          <ul style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.75rem;">
            <li><strong>macOS:</strong> <code>~/Library/Application Support/Claude/claude_desktop_config.json</code></li>
            <li><strong>Windows:</strong> <code>%APPDATA%\\Claude\\claude_desktop_config.json</code></li>
            <li><strong>Linux:</strong> <code>~/.config/Claude/claude_desktop_config.json</code></li>
          </ul>
          <pre><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat-mcp",
      "args": []
    }}
  }}
}}</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">B. Cursor AI IDE</h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Create or edit <code>.cursor/mcp.json</code> in your project root or user configuration:
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

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <div>
          <h3 style="font-size: 1.2rem; color: var(--accent-amber); margin-bottom: 0.5rem;">C. VS Code (Cline / Roo Code / Continue.dev)</h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            In your extension settings under MCP Servers, declare:
          </p>
          <pre><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat-mcp",
      "args": [],
      "disabled": false,
      "autoApprove": [
        "tasleemat_list_forms",
        "tasleemat_get_form",
        "tasleemat_get_schema",
        "tasleemat_validate",
        "tasleemat_tailor_project",
        "tasleemat_calculate_eva"
      ]
    }}
  }}
}}</code></pre>
        </div>
      </div>

      <!-- Section 3: The 6 Tools Reference & Payloads -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">3. Exhaustive 6 MCP Tools Reference &amp; Payloads</h2>

        <!-- Tool 1 -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.5rem;">1. <code>tasleemat_list_forms</code></h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Lists available deliverables filtered by phase, sizing tier, or methodology pack.
          </p>
          <pre><code>// Client Request
{{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {{
    "name": "tasleemat_list_forms",
    "arguments": {{
      "phase": "03",
      "lang": "en"
    }}
  }}
}}

// Server Response
{{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {{
    "content": [
      {{
        "type": "text",
        "text": "[{{\\"id\\": \\"PMO-03.01\\", \\"name\\": \\"Project Charter\\", \\"phase\\": \\"03\\"}}, ...]"
      }}
    ]
  }}
}}</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Tool 2 -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">2. <code>tasleemat_get_form</code></h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Fetches specific asset contents for a deliverable: <code>template</code>, <code>guide</code>, <code>example</code>, <code>prompt</code>, <code>schema</code>, or <code>dictionary</code>.
          </p>
          <pre><code>// Client Request
{{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {{
    "name": "tasleemat_get_form",
    "arguments": {{
      "artifact_id": "PMO-03.01",
      "asset_type": "template",
      "lang": "en"
    }}
  }}
}}</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Tool 3 -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-amber); margin-bottom: 0.5rem;">3. <code>tasleemat_get_schema</code></h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Retrieves the complete JSON Schema Draft 2020-12 definition to enable client-side schema inspection or agent prompt injection.
          </p>
          <pre><code>// Client Request
{{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {{
    "name": "tasleemat_get_schema",
    "arguments": {{
      "artifact_id": "PMO-04.08.02"
    }}
  }}
}}</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Tool 4 -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: #8b5cf6; margin-bottom: 0.5rem;">4. <code>tasleemat_validate</code></h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            Validates a structured JSON payload against the companion schema and returns exact JSON path errors.
          </p>
          <pre><code>// Client Request
{{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {{
    "name": "tasleemat_validate",
    "arguments": {{
      "artifact_id": "PMO-03.01",
      "data": {{
        "project_id": "PRJ-01",
        "project_name": "Cloud Platform",
        "sponsor": "Sarah Al-Ahmad"
      }},
      "mode": "strict"
    }}
  }}
}}

// Server Response
{{
  "jsonrpc": "2.0",
  "id": 4,
  "result": {{
    "content": [
      {{
        "type": "text",
        "text": "{{\\"valid\\": true, \\"errors\\": [], \\"schema_id\\": \\"https://fakhr.me/schemas/pmo-03-01.json\\"}}"
      }}
    ]
  }}
}}</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Tool 5 & 6 -->
        <div>
          <h3 style="font-size: 1.2rem; color: #ec4899; margin-bottom: 0.5rem;">5. <code>tasleemat_tailor_project</code> &amp; 6. <code>tasleemat_calculate_eva</code></h3>
          <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">
            <code>tasleemat_tailor_project</code> returns required deliverables for a tier/pack. 
            <code>tasleemat_calculate_eva</code> computes attested EVM math metrics for PMO-06.05.
          </p>
          <pre><code>// Calculate EVA Metrics Request
{{
  "jsonrpc": "2.0",
  "id": 6,
  "method": "tools/call",
  "params": {{
    "name": "tasleemat_calculate_eva",
    "arguments": {{
      "pv": 500000,
      "ev": 475000,
      "ac": 520000,
      "bac": 1200000
    }}
  }}
}}</code></pre>
        </div>
      </div>

      <!-- Section 4: Practical Tutorials -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">4. Step-by-Step Tutorials</h2>

        <!-- Tutorial 1 -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.5rem;">
            Tutorial 1: Autonomous PMO Deliverable Drafting in Cursor Agent Mode
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 0.75rem;">
            Once <code>.cursor/mcp.json</code> is saved, switch Cursor Composer to <strong>Agent Mode</strong> and prompt:
          </p>
          <div style="background: var(--bg-main); border-left: 4px solid var(--accent-blue); padding: 1rem; margin-bottom: 1rem; font-style: italic;">
            "We are initiating project PRJ-CLOUD. Using Tasleemat MCP tools, fetch the template and schema for PMO-03.01 (Project Charter), draft a compliant charter based on our kickoff notes in docs/notes.txt, and validate the JSON data before writing the file."
          </div>
          <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7;">
            Cursor will autonomously execute <code>tasleemat_get_form</code>, inspect constraints via <code>tasleemat_get_schema</code>, 
            run <code>tasleemat_validate</code> to confirm schema conformance, and write the finalized markdown file.
          </p>
        </div>

        <!-- Tutorial 2 -->
        <div>
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">
            Tutorial 2: Building a Standalone Python MCP Client
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 0.75rem;">
            You can interact with <code>tasleemat-mcp</code> from any Python application via standard subprocessing:
          </p>
          <pre><code>import subprocess
import json

def call_mcp_tool(tool_name: str, arguments: dict) -&gt; dict:
    # Invokes a tool on the Tasleemat MCP server via stdio JSON-RPC
    proc = subprocess.Popen(
        ["tasleemat-mcp"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # 1. Initialize Handshake
    init_req = {{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {{"capabilities": {{}}}}}}
    proc.stdin.write(json.dumps(init_req) + "\\n")
    proc.stdin.flush()
    proc.stdout.readline()  # consume init response
    
    # 2. Call Tool
    call_req = {{
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {{"name": tool_name, "arguments": arguments}}
    }}
    proc.stdin.write(json.dumps(call_req) + "\\n")
    proc.stdin.flush()
    
    response_line = proc.stdout.readline()
    proc.terminate()
    return json.loads(response_line)

# Example: tailor project for Tier 2 Agile
result = call_mcp_tool("tasleemat_tailor_project", {{"tier": 2, "pack": "agile"}})
print("Tailored Result:", result)</code></pre>
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
    subnav = render_dev_subnav("mcp", "ar", base_url)
    
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/ar/">الرئيسية</a> &gt; 
          <a href="{base_url}/ar/developers/">المطورون والذكاء الاصطناعي</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">خادم بروتوكول MCP</span>
        </nav>
        <div class="hero-pill"><span>🔌 بروتوكول سياق النموذج (MCP)</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">دليل خادم بروتوكول سياق النموذج (MCP)</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
          ربط بيئات التطوير الذكية مثل Cursor و Claude Desktop والوكلاء الأذكياء مباشرة بالـ 114 تسليمة ومخططاتها المعيارية عبر بروتوكول JSON-RPC 2.0 stdio الموحد.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Section 1: Architecture AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">1. معمارية البروتوكول ومسار المصافحة (Handshake)</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          يُعد بروتوكول سياق النماذج (Model Context Protocol - MCP) المعيار الدولي المفتوح لربط مساعدي الذكاء الاصطناعي بمستودعات البيانات وأدوات التشغيل الخارجية.
          توفر منظومة تسليمات خادماً مستقلاً (<code>tasleemat-mcp</code>) يتواصل عبر مجاري الإدخال والإخراج القياسية (<code>stdio</code>) 
          باستخدام رسائل <strong>JSON-RPC 2.0</strong> الصارمة، مما يمنع تعارض المنافذ الشبكية ويتيح التشغيل في بيئات معزولة وآمنة تماماً.
        </p>
        
        <pre><code class="language-mermaid">
sequenceDiagram
    autonumber
    actor User as المهندس / مدير المشروع
    participant Host as المساعد الذكي (Cursor / Claude)
    participant Server as خادم Tasleemat MCP (stdio)
    participant Engine as محرك تسليمات الأساسي

    Host->>Server: رسالة المصافحة "initialize"
    Server-->>Host: تأكيد الإمكانات وعرض الأدوات المتاحة
    Host->>Server: إشعار الاكتمال "notifications/initialized"
    User->>Host: "خصص لي تسليمات مشروع رشيق من المستوى 2"
    Host->>Server: استدعاء الأداة (name: "tasleemat_tailor_project", args: {{tier: 2, pack: "agile"}})
    Server->>Engine: get_tailoring_profile(tier=2, pack="agile")
    Engine-->>Server: قائمة بـ 34 تسليمة معتمدة
    Server-->>Host: نتيجة JSON-RPC (بيان التسليمات)
    Host->>User: "إليك قائمة التسليمات المعتمدة لمشروعك..."
        </code></pre>
      </div>

      <!-- Section 2: IDE Configurations AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <div style="background: linear-gradient(135deg, rgba(37, 99, 235, 0.08) 0%, rgba(139, 92, 246, 0.08) 100%); border: 1px solid rgba(37, 99, 235, 0.25); border-radius: 0.75rem; padding: 1.25rem; margin-bottom: 2rem;">
          <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem;">
            <div>
              <span class="brand-badge" style="background: #10b981; color: white; margin-bottom: 0.5rem; display: inline-block;">سجل MCP الرسمي المعتمد</span>
              <h3 style="font-size: 1.15rem; margin: 0.25rem 0; color: var(--text-main);">المعرّف المعتمد: <code>io.github.fakhruldeen/tasleemat</code> (v2.6.0)</h3>
              <p style="font-size: 0.88rem; color: var(--text-muted); margin: 0;">خادم بروتوكول سياق النماذج معتمد عبر قنوات stdio القياسية بدون الحاجة لفتح منافذ شبكية.</p>
            </div>
            <code style="background: var(--bg-card); border: 1px solid var(--border-color); padding: 0.5rem 0.85rem; border-radius: 0.4rem; font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent-blue); direction: ltr;">uvx tasleemat-mcp</code>
          </div>
        </div>

        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">2. إعدادات التكامل مع بيئات التطوير الذكية</h2>

        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.5rem;">أ. تطبيق Anthropic Claude Desktop</h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            أضف المقطع التالي إلى ملف التكوين <code>claude_desktop_config.json</code>:
          </p>
          <ul style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.75rem; padding-right: 1.25rem;">
            <li><strong>نظام macOS:</strong> <code>~/Library/Application Support/Claude/claude_desktop_config.json</code></li>
            <li><strong>نظام Windows:</strong> <code>%APPDATA%\\Claude\\claude_desktop_config.json</code></li>
            <li><strong>نظام Linux:</strong> <code>~/.config/Claude/claude_desktop_config.json</code></li>
          </ul>
          <pre style="direction: ltr; text-align: left;"><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat-mcp",
      "args": []
    }}
  }}
}}</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <div style="margin-bottom: 2rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">ب. بيئة Cursor الذكية</h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            أنشئ ملف <code>.cursor/mcp.json</code> في المجلد الرئيسي للمشروع:
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

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <div>
          <h3 style="font-size: 1.2rem; color: var(--accent-amber); margin-bottom: 0.5rem;">ج. محررات VS Code (Cline و Continue.dev)</h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            في إعدادات إضافة MCP داخل المحرر، أضف التكوين التالي مع تفعيل الموافقة التلقائية على الأدوات:
          </p>
          <pre style="direction: ltr; text-align: left;"><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat-mcp",
      "args": [],
      "disabled": false,
      "autoApprove": [
        "tasleemat_list_forms",
        "tasleemat_get_form",
        "tasleemat_get_schema",
        "tasleemat_validate",
        "tasleemat_tailor_project",
        "tasleemat_calculate_eva"
      ]
    }}
  }}
}}</code></pre>
        </div>
      </div>

      <!-- Section 3: The 6 Tools Reference AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">3. المرجع التفصيلي لأدوات MCP الست وحمولات البيانات</h2>

        <!-- Tool 1 AR -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.5rem; direction: ltr; text-align: right;">1. <code>tasleemat_list_forms</code></h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            استعراض التسليمات المتاحة مع تصفية محددة بالمرحلة، مستوى الحجم، أو اللغة.
          </p>
          <pre style="direction: ltr; text-align: left;"><code>// طلب العميل (Client Request)
{{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {{
    "name": "tasleemat_list_forms",
    "arguments": {{
      "phase": "03",
      "lang": "ar"
    }}
  }}
}}</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Tool 2 AR -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.5rem; direction: ltr; text-align: right;">2. <code>tasleemat_get_form</code></h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            جلب أصول التسليمة: <code>template</code> (القالب)، <code>guide</code> (الدليل)، <code>example</code> (المثال)، <code>schema</code> (المخطط).
          </p>
          <pre style="direction: ltr; text-align: left;"><code>// طلب العميل
{{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {{
    "name": "tasleemat_get_form",
    "arguments": {{
      "artifact_id": "PMO-03.01",
      "asset_type": "template",
      "lang": "ar"
    }}
  }}
}}</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Tool 3 AR -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-amber); margin-bottom: 0.5rem; direction: ltr; text-align: right;">3. <code>tasleemat_get_schema</code></h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            استرجاع مخطط JSON الكامل لتمكين نموذج الذكاء الاصطناعي من فهم قيود الحقول قبل الصياغة.
          </p>
          <pre style="direction: ltr; text-align: left;"><code>// طلب العميل
{{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {{
    "name": "tasleemat_get_schema",
    "arguments": {{
      "artifact_id": "PMO-04.08.02"
    }}
  }}
}}</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Tool 4 AR -->
        <div style="margin-bottom: 2.25rem;">
          <h3 style="font-size: 1.2rem; color: #8b5cf6; margin-bottom: 0.5rem; direction: ltr; text-align: right;">4. <code>tasleemat_validate</code></h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            التحقق من بيانات JSON المصاغة مقابل المخطط وإرجاع مسار الخطأ بدقة إلى المساعد الذكي.
          </p>
          <pre style="direction: ltr; text-align: left;"><code>// طلب التحقق
{{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {{
    "name": "tasleemat_validate",
    "arguments": {{
      "artifact_id": "PMO-03.01",
      "data": {{
        "project_id": "PRJ-01",
        "project_name": "منصة التحول السحابي",
        "sponsor": "سارة الأحمد"
      }},
      "mode": "strict"
    }}
  }}
}}</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Tool 5 & 6 AR -->
        <div>
          <h3 style="font-size: 1.2rem; color: #ec4899; margin-bottom: 0.5rem; direction: ltr; text-align: right;">5. <code>tasleemat_tailor_project</code> و 6. <code>tasleemat_calculate_eva</code></h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            أداة <code>tasleemat_tailor_project</code> لتخصيص التسليمات المطلوبة، وأداة <code>tasleemat_calculate_eva</code> لحساب مقاييس القيمة المكتسبة حتمياً لتسليمة PMO-06.05.
          </p>
          <pre style="direction: ltr; text-align: left;"><code>// طلب حساب مقاييس القيمة المكتسبة
{{
  "jsonrpc": "2.0",
  "id": 6,
  "method": "tools/call",
  "params": {{
    "name": "tasleemat_calculate_eva",
    "arguments": {{
      "pv": 500000,
      "ev": 475000,
      "ac": 520000,
      "bac": 1200000
    }}
  }}
}}</code></pre>
        </div>
      </div>

      <!-- Section 4: Practical Tutorials AR -->
      <div class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; color: var(--text-main);">4. أدلة تطبيقية عملية (Tutorials)</h2>

        <!-- Tutorial 1 AR -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.2rem; color: var(--accent-blue); margin-bottom: 0.5rem;">
            الدليل 1: صياغة تسليمات المشاريع ذاتياً داخل نمط الوكيل في Cursor (Agent Mode)
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            بعد حفظ ملف التكوين <code>.cursor/mcp.json</code>، فعّل نمط Agent في Cursor وأرسل التوجيه التالي:
          </p>
          <div style="background: var(--bg-main); border-right: 4px solid var(--accent-blue); padding: 1rem; margin-bottom: 1rem; font-style: italic;">
            "نحن نبدأ مشروع منصة التحول الرقمي PRJ-CLOUD. باستخدام أدوات خادم Tasleemat MCP، اجلب قالب ومخطط ميثاق المشروع PMO-03.01، وصغ ميثاقاً مطابقاً للمواصفات استناداً لمذكرات الاجتماع في docs/notes.txt، مع التحقق من صحة بيانات JSON قبل إنشاء الملف النهائي."
          </div>
          <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.8;">
            سيقوم Cursor تلقائياً باستدعاء <code>tasleemat_get_form</code>، وفحص الشروط عبر <code>tasleemat_get_schema</code>، 
            ثم استدعاء <code>tasleemat_validate</code> لتأكيد سلامة البيانات 100% وكتابة الملف النهائي.
          </p>
        </div>

        <!-- Tutorial 2 AR -->
        <div>
          <h3 style="font-size: 1.2rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">
            الدليل 2: بناء عميل بايثون مخصص للتواصل مع خادم MCP
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem;">
            يمكن استدعاء أدوات خادم MCP من أي تطبيق بايثون خارجي عبر مجاري الإدخال والإخراج:
          </p>
          <pre style="direction: ltr; text-align: left;"><code>import subprocess
import json

def call_mcp_tool(tool_name: str, arguments: dict) -&gt; dict:
    # استدعاء أدوات خادم تسليمات MCP عبر بروتوكول stdio JSON-RPC
    proc = subprocess.Popen(
        ["tasleemat-mcp"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # 1. إرسال مصافحة التهيئة
    init_req = {{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {{"capabilities": {{}}}}}}
    proc.stdin.write(json.dumps(init_req) + "\\n")
    proc.stdin.flush()
    proc.stdout.readline()  # قراءة رد التهيئة
    
    # 2. استدعاء الأداة المطلوبة
    call_req = {{
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {{"name": tool_name, "arguments": arguments}}
    }}
    proc.stdin.write(json.dumps(call_req) + "\\n")
    proc.stdin.flush()
    
    response_line = proc.stdout.readline()
    proc.terminate()
    return json.loads(response_line)

# تجربة تخصيص تسليمات المشروع:
result = call_mcp_tool("tasleemat_tailor_project", {{"tier": 2, "pack": "agile"}})
print("نتيجة التخصيص:", result)</code></pre>
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
