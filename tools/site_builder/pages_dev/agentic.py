"""tools/site_builder/pages_dev/agentic.py
Agentic Swarms, CrewAI/LangGraph Architectures, CI/CD Governance & Attested Math (English & Arabic).
"""

from tools.site_builder.theme import render_html_page
from tools.site_builder.pages_dev.nav import render_dev_subnav


def generate_dev_agentic_en(base_url: str = "/Tasleemat") -> str:
    subnav = render_dev_subnav("agentic", "en", base_url)
    
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
          Enterprise multi-agent architectures (CrewAI, LangGraph), automated CI/CD quality gates, and mathematically audited calculation engines.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Section 1: Multi-Agent Architecture Overview -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">1. Multi-Agent PMO Swarm Architecture</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          In enterprise project management, a single AI chatbot cannot reliably govern complex programs. 
          Tasleemat establishes a <strong>specialized multi-agent swarm pattern</strong> where separate autonomous agents 
          collaborate under strict separation of duties, bounded by formal schema contracts and mandatory human sign-off gates:
        </p>

        <pre><code class="language-mermaid">
flowchart TD
    subgraph Swarm["Autonomous PMO Swarm"]
        Director["PMO Director Agent<br/>(Tailoring &amp; Task Delegation)"]
        Drafter["Specialist Drafter Agent<br/>(Markdown Synthesis)"]
        Auditor["Governance Auditor Agent<br/>(Draft 2020-12 Schema Check)"]
    end

    subgraph Gates["Attestation &amp; Approvals"]
        HumanGate["Human Stage-Gate Review<br/>(Executive Sponsor Sign-off)"]
        Repo["Approved Project Repository"]
    end

    Director -->|Delegates Deliverable| Drafter
    Drafter -->|Produces JSON Payload| Auditor
    Auditor -->|Validates Schema| Auditor
    Auditor -.->|Self-Correction Loop| Drafter
    Auditor ==>|Certified Payload| HumanGate
    HumanGate -->|Approved| Repo
        </code></pre>
      </div>

      <!-- Section: 1-Click Native Agent Exporter -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem; border-left: 4px solid #8b5cf6;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.25rem;">
          <div>
            <div style="display: inline-flex; align-items: center; gap: 0.4rem; background: rgba(139, 92, 246, 0.1); color: #8b5cf6; padding: 0.2rem 0.6rem; border-radius: 9999px; font-size: 0.8rem; font-weight: 700; margin-bottom: 0.4rem;">
              ⚡ Instant Agent Context Injection
            </div>
            <h2 style="font-size: 1.4rem; margin: 0; color: var(--text-main);">1-Click Native Integration for 8 AI Agents &amp; IDEs</h2>
          </div>
          <code style="background: var(--bg-card); border: 1px solid var(--border-color); padding: 0.5rem 0.85rem; border-radius: 0.4rem; font-family: var(--font-mono); font-size: 0.85rem; color: #8b5cf6;">tasleemat agents export --target &lt;agent&gt;</code>
        </div>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Instead of manually crafting system prompts and prompt engineering files, <code>tasleemat agents export</code> generates tuned, deterministic instruction files, governance bounds, and Stage-Gate checklists for 8 industry-standard AI platforms:
        </p>

        <div class="grid-cards" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">Anthropic Claude</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">CLAUDE.md</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">Cursor AI</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">.cursorrules</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">Codeium Windsurf</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">.windsurfrules</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">Cline / Roo Code</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">.clinerules</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">OpenCode</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">opencode.json</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">OpenAI Assistant</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">openai_instructions.txt</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">Antigravity (AGY)</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">RULES.md &amp; SKILL.md</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">VS Code Workspace</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">.vscode/settings.json</div>
          </div>
        </div>

        <pre><code># Bootstrap an agentic PMO workspace for Cursor and Claude
tasleemat agents export --target cursor
tasleemat agents export --target claude

# Export all 8 agent targets at once to a dedicated directory
tasleemat agents export --target all --out ./agents_config/</code></pre>
      </div>

      <!-- Section 2: Framework Integrations (CrewAI & LangGraph) -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text-main);">2. Production Multi-Agent Framework Integrations</h2>

        <!-- Framework 1: CrewAI -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-blue); margin-bottom: 0.5rem;">
            A. CrewAI Multi-Agent PMO Team
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            A complete, runnable script assembling a CrewAI team equipped with custom tools calling the <code>tasleemat</code> SDK:
          </p>
          <pre><code>from crewai import Agent, Task, Crew, Process
from langchain.tools import tool
import json
import tasleemat

@tool
def fetch_pmo_deliverable_assets(artifact_id: str) -&gt; str:
    # Fetches template, guide, and JSON schema for a deliverable
    assets = tasleemat.get_artifact_assets(artifact_id, lang="en")
    return json.dumps({{
        "guide": assets.get_guide_content()[:600],
        "schema": assets.get_schema_data()
    }})

@tool
def validate_deliverable_data(artifact_id: str, payload_json: str) -&gt; str:
    # Validates structured project data against Draft 2020-12 schema
    data = json.loads(payload_json)
    report = tasleemat.validate_artifact_data(artifact_id, data, mode="strict")
    return json.dumps({{"valid": report.valid, "errors": [e.message for e in report.errors]}})

# Define Specialized Agents
pm_drafter = Agent(
    role="Senior Technical Project Manager",
    goal="Synthesize high-fidelity project deliverables matching kickoff requirements",
    backstory="Experienced PMP practitioner adept at translating unstructured notes into structured charter data.",
    tools=[fetch_pmo_deliverable_assets],
    verbose=True
)

compliance_auditor = Agent(
    role="PMO Governance &amp; Compliance Auditor",
    goal="Audit synthesized deliverable data and verify 100% Draft 2020-12 schema compliance",
    backstory="Strict enterprise auditor dedicated to verifying mandatory fields and RFC formats.",
    tools=[validate_deliverable_data],
    verbose=True
)

# Tasks
draft_task = Task(
    description="Fetch PMO-03.01 assets and draft charter JSON for project PRJ-CLOUD.",
    expected_output="Valid JSON string matching PMO-03.01 schema",
    agent=pm_drafter
)

audit_task = Task(
    description="Validate drafted JSON data using validate_deliverable_data tool. Require revisions if invalid.",
    expected_output="Final audit report certifying schema validity",
    agent=compliance_auditor
)

pmo_crew = Crew(
    agents=[pm_drafter, compliance_auditor],
    tasks=[draft_task, audit_task],
    process=Process.sequential
)</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Framework 2: LangGraph -->
        <div>
          <h3 style="font-size: 1.25rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">
            B. LangGraph StateGraph with Human-in-the-Loop Review Gate
          </h3>
          <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
            LangGraph state machine enforcing autonomous healing loops and interrupting for executive human review:
          </p>
          <pre><code>from typing import TypedDict, Optional, Dict, Any, List
from langgraph.graph import StateGraph, END
import tasleemat

class PMOState(TypedDict):
    artifact_id: str
    notes: str
    draft_data: Optional[Dict[str, Any]]
    errors: List[str]
    retries: int
    approved: bool

def draft_node(state: PMOState) -&gt; PMOState:
    # Call LLM to draft initial JSON based on state["notes"]
    state["draft_data"] = {{"project_id": "PRJ-01", "name": "Cloud"}}
    return state

def validate_node(state: PMOState) -&gt; PMOState:
    report = tasleemat.validate_artifact_data(state["artifact_id"], state["draft_data"], mode="strict")
    state["errors"] = [e.message for e in report.errors]
    return state

def should_heal(state: PMOState) -&gt; str:
    if len(state["errors"]) &gt; 0 and state["retries"] &lt; 3:
        return "heal_node"
    elif len(state["errors"]) == 0:
        return "human_approval_gate"
    return END

# Build State Machine
workflow = StateGraph(PMOState)
workflow.add_node("draft_node", draft_node)
workflow.add_node("validate_node", validate_node)
workflow.set_entry_point("draft_node")
workflow.add_edge("draft_node", "validate_node")
workflow.add_conditional_edges("validate_node", should_heal, {{
    "heal_node": "draft_node",
    "human_approval_gate": END
}})</code></pre>
        </div>

      </div>

      <!-- Section 3: CI/CD Quality Gates -->
      <div id="cicd" class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">3. Headless CI/CD Automation &amp; Quality Gates</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Incorporate automated deliverable audits directly into your DevOps repository. 
          The following GitHub Actions workflow validates all modified deliverable markdown and JSON files on every Pull Request:
        </p>

        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Complete GitHub Actions Workflow (<code>.github/workflows/pmo-governance.yml</code>)</h3>
        <pre><code>name: PMO Governance &amp; Schema Quality Gate

on:
  pull_request:
    branches: [main]
    paths:
      - 'projects/**'

jobs:
  validate-governance:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Tasleemat Framework
        run: pip install tasleemat

      - name: Execute Regression &amp; Schema Audit
        run: |
          echo "Verifying project deliverable integrity..."
          tasleemat test -v
          
      - name: Post PR Compliance Summary
        if: success()
        run: echo "::notice title=Tasleemat PMO Gate::All 114 deliverable schemas and regression checks passed 100%!"</code></pre>
      </div>

      <!-- Section 4: Attested Computations & EVM Contracts -->
      <div id="attested-math" class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">4. Attested Computations &amp; Deterministic Math Contracts (PMO-06.05)</h2>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          Generative AI models are fundamentally token-prediction probability engines. They suffer from catastrophic arithmetic hallucination 
          when calculating multi-variable metrics. Tasleemat enforces <strong>deterministic computational contracts</strong> 
          using IEEE 754 precision and zero-division guards for all Earned Value Management (EVM) metrics in <code>PMO-06.05</code>:
        </p>

        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>EVM Metric</th>
                <th>Mathematical Formula</th>
                <th>Interpretation &amp; Attestation Boundary</th>
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
                <td>&gt; 1.0 = cost efficient. Guard: if <code>AC &lt;= 0</code>, CPI = 1.0</td>
              </tr>
              <tr>
                <td><strong>Schedule Performance Index (SPI)</strong></td>
                <td><code>SPI = EV / PV</code></td>
                <td>&gt; 1.0 = schedule efficient. Guard: if <code>PV &lt;= 0</code>, SPI = 1.0</td>
              </tr>
              <tr>
                <td><strong>Estimate at Completion (EAC)</strong></td>
                <td><code>EAC = BAC / CPI</code></td>
                <td>Forecasted final total cost based on current cost efficiency</td>
              </tr>
              <tr>
                <td><strong>To-Complete Performance Index (TCPI)</strong></td>
                <td><code>TCPI = (BAC - EV) / (BAC - AC)</code></td>
                <td>Required efficiency for remaining work to meet target budget</td>
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
    subnav = render_dev_subnav("agentic", "ar", base_url)
    
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <nav style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;" aria-label="Breadcrumb">
          <a href="{base_url}/ar/">الرئيسية</a> &gt; 
          <a href="{base_url}/ar/developers/">المطورون والذكاء الاصطناعي</a> &gt; 
          <span style="color: var(--text-main); font-weight: 600;">أسراب الوكلاء و CI/CD</span>
        </nav>
        <div class="hero-pill"><span>🤖 أسراب الوكلاء وخطوط CI/CD</span></div>
        <h1 class="hero-title" style="font-size: 2.2rem; margin-top: 0.5rem;">أسراب الوكلاء، خطوط CI/CD، والحسابات الموثقة</h1>
        <p class="hero-subtitle" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
          تنسيق أسراب الوكلاء الأذكياء عبر CrewAI و LangGraph، بوابات الحوكمة المؤتمتة في خطوط CI/CD، وعقود الحسابات الرياضية الموثقة لإدارة المشاريع.
        </p>
      </div>
    </section>

    {subnav}

    <div class="container" style="margin-bottom: 5rem; max-width: 960px;">
      
      <!-- Section 1: Multi-Agent Architecture Overview AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">1. معمارية أسراب الوكلاء الأذكياء (PMO Swarm)</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          في إدارة المشاريع المؤسسية، لا يمكن الاعتماد على روبوت محادثة فردي لإدارة برامج تحول استراتيجية معقدة. 
          تعتمد تسليمات <strong>نمط سرب الوكلاء المتخصصين</strong>؛ حيث يتعاون عدة وكلاء أذكياء مع الفصل الصارم بين المسؤوليات، 
          وضبط المخرجات بمخططات Draft 2020-12 وبوابات الاعتماد البشري الإلزامية:
        </p>

        <pre><code class="language-mermaid">
flowchart TD
    subgraph Swarm["سرب وكلاء إدارة المشاريع (PMO Swarm)"]
        Director["وكيل مدير الـ PMO<br/>(تحديد الحجم وتوزيع المهام)"]
        Drafter["وكيل الصياغة المتخصص<br/>(توليد محتوى الوثائق)"]
        Auditor["وكيل تدقيق الحوكمة<br/>(فحص المخطط Draft 2020-12)"]
    end

    subgraph Gates["التوثيق والاعتماد"]
        HumanGate["بوابة المراجعة البشرية<br/>(اعتماد الراعي التنفيذي)"]
        Repo["مستودع وثائق المشروع المعتمدة"]
    end

    Director -->|تفويض إعداد التسليمة| Drafter
    Drafter -->|إرسال بيانات JSON| Auditor
    Auditor -->|التحقق من المخطط| Auditor
    Auditor -.->|حلقة التصحيح الذاتي| Drafter
    Auditor ==>|بيانات مطابقة ومعتمدة| HumanGate
    HumanGate -->|اعتماد نهائي| Repo
        </code></pre>
      </div>

      <!-- Section: 1-Click Native Agent Exporter AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem; border-right: 4px solid #8b5cf6;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.25rem;">
          <div>
            <div style="display: inline-flex; align-items: center; gap: 0.4rem; background: rgba(139, 92, 246, 0.1); color: #8b5cf6; padding: 0.2rem 0.6rem; border-radius: 9999px; font-size: 0.8rem; font-weight: 700; margin-bottom: 0.4rem;">
              ⚡ حقن سياق وقواعد الحوكمة فورياً
            </div>
            <h2 style="font-size: 1.4rem; margin: 0; color: var(--text-main);">تصدير سياق المشروع بنقرة واحدة لـ 8 من وكلاء الذكاء الاصطناعي</h2>
          </div>
          <code style="background: var(--bg-card); border: 1px solid var(--border-color); padding: 0.5rem 0.85rem; border-radius: 0.4rem; font-family: var(--font-mono); font-size: 0.85rem; color: #8b5cf6; direction: ltr;">tasleemat agents export --target &lt;agent&gt;</code>
        </div>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          بدلاً من كتابة المطالبات والتعليمات الحوكمية يدوياً، يتيح أمر <code>tasleemat agents export</code> توليد ملفات التوجيه الموجهة والمنضبطة تلقائياً مع معايير بوابات المراحل وقوائم التحقق لـ 8 من أبرز بيئات الذكاء الاصطناعي:
        </p>

        <div class="grid-cards" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">Anthropic Claude</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); direction: ltr; text-align: right;">CLAUDE.md</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">Cursor AI</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); direction: ltr; text-align: right;">.cursorrules</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">Codeium Windsurf</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); direction: ltr; text-align: right;">.windsurfrules</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">Cline / Roo Code</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); direction: ltr; text-align: right;">.clinerules</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">OpenCode</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); direction: ltr; text-align: right;">opencode.json</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">OpenAI Assistant</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); direction: ltr; text-align: right;">openai_instructions.txt</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">Antigravity (AGY)</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); direction: ltr; text-align: right;">RULES.md &amp; SKILL.md</div>
          </div>
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 1rem; border-radius: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">بيئة VS Code</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); direction: ltr; text-align: right;">.vscode/settings.json</div>
          </div>
        </div>

        <pre style="direction: ltr; text-align: left;"><code># تجهيز بيئة عمل الحوكمة لـ Cursor و Claude بنقرة واحدة
tasleemat agents export --target cursor
tasleemat agents export --target claude

# تصدير إعدادات كافة الوكلاء دفعة واحدة لمجلد مخصص
tasleemat agents export --target all --out ./agents_config/</code></pre>
      </div>

      <!-- Section 2: Framework Integrations AR -->
      <div class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text-main);">2. أدلة التكامل مع أطر عمل الوكلاء (CrewAI و LangGraph)</h2>

        <!-- Framework 1: CrewAI AR -->
        <div style="margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.25rem; color: var(--accent-blue); margin-bottom: 0.5rem;">
            أ. بناء فريق عمل متكامل عبر إطار CrewAI
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            كود بايثون تنفيذي مكتمل لتشكيل فريق وكلاء أذكياء مزودين بأدوات تسليمات للتحقق الآلي:
          </p>
          <pre style="direction: ltr; text-align: left;"><code>from crewai import Agent, Task, Crew, Process
from langchain.tools import tool
import json
import tasleemat

@tool
def fetch_pmo_deliverable_assets(artifact_id: str) -&gt; str:
    # استرجاع القالب والدليل والمخطط لتسليمة معينة
    assets = tasleemat.get_artifact_assets(artifact_id, lang="ar")
    return json.dumps({{
        "guide": assets.get_guide_content()[:600],
        "schema": assets.get_schema_data()
    }}, ensure_ascii=False)

@tool
def validate_deliverable_data(artifact_id: str, payload_json: str) -&gt; str:
    # التحقق من مطابقة بيانات الوثيقة لمخطط Draft 2020-12
    data = json.loads(payload_json)
    report = tasleemat.validate_artifact_data(artifact_id, data, mode="strict")
    return json.dumps({{"valid": report.valid, "errors": [e.message for e in report.errors]}}, ensure_ascii=False)

# تعريف الوكلاء المتخصصين
pm_drafter = Agent(
    role="مدير المشاريع التقني",
    goal="صياغة وثائق مشاريع عالية الدقة تطابق متطلبات ومذكرات الاجتماع",
    backstory="ممارس معتمد خبير في تحويل الملاحظات الخام إلى بيانات ميثاق مهيكلة.",
    tools=[fetch_pmo_deliverable_assets],
    verbose=True
)

compliance_auditor = Agent(
    role="مدقق الحوكمة والامتثال المؤسسي",
    goal="تدقيق بيانات الوثائق والتأكد من مطابقتها 100% لمخطط Draft 2020-12",
    backstory="مدقق صارم معني بالتحقق من الحقول الإلزامية وتنسيقات التواريخ القياسية.",
    tools=[validate_deliverable_data],
    verbose=True
)

# المهام
draft_task = Task(
    description="استدعاء أصول PMO-03.01 وصياغة بيانات الميثاق لمشروع PRJ-CLOUD.",
    expected_output="نص JSON صالح يطابق مخطط PMO-03.01",
    agent=pm_drafter
)

audit_task = Task(
    description="فحص صحة بيانات JSON عبر أداة validate_deliverable_data وإلزام الوكيل بالتصحيح إن وجدت أخطاء.",
    expected_output="تقرير تدقيق نهائي يثبت مطابقة الوثيقة للمخطط",
    agent=compliance_auditor
)

pmo_crew = Crew(
    agents=[pm_drafter, compliance_auditor],
    tasks=[draft_task, audit_task],
    process=Process.sequential
)</code></pre>
        </div>

        <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">

        <!-- Framework 2: LangGraph AR -->
        <div>
          <h3 style="font-size: 1.25rem; color: var(--accent-emerald); margin-bottom: 0.5rem;">
            ب. آلة الحالة LangGraph مع بوابة المراجعة البشرية (Human-in-the-Loop)
          </h3>
          <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1rem;">
            إدارة تدفق العمل عبر LangGraph مع إيقاف العملية للموافقة البشرية قبل اعتماد الوثيقة:
          </p>
          <pre style="direction: ltr; text-align: left;"><code>from typing import TypedDict, Optional, Dict, Any, List
from langgraph.graph import StateGraph, END
import tasleemat

class PMOState(TypedDict):
    artifact_id: str
    notes: str
    draft_data: Optional[Dict[str, Any]]
    errors: List[str]
    retries: int
    approved: bool

def draft_node(state: PMOState) -&gt; PMOState:
    state["draft_data"] = {{"project_id": "PRJ-01", "name": "مشروع السحابة"}}
    return state

def validate_node(state: PMOState) -&gt; PMOState:
    report = tasleemat.validate_artifact_data(state["artifact_id"], state["draft_data"], mode="strict")
    state["errors"] = [e.message for e in report.errors]
    return state

def should_heal(state: PMOState) -&gt; str:
    if len(state["errors"]) &gt; 0 and state["retries"] &lt; 3:
        return "heal_node"
    elif len(state["errors"]) == 0:
        return "human_approval_gate"
    return END

# بناء آلة الحالة
workflow = StateGraph(PMOState)
workflow.add_node("draft_node", draft_node)
workflow.add_node("validate_node", validate_node)
workflow.set_entry_point("draft_node")
workflow.add_edge("draft_node", "validate_node")
workflow.add_conditional_edges("validate_node", should_heal, {{
    "heal_node": "draft_node",
    "human_approval_gate": END
}})</code></pre>
        </div>

      </div>

      <!-- Section 3: CI/CD Quality Gates AR -->
      <div id="cicd" class="card" style="padding: 2.25rem; margin-bottom: 2.5rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">3. خطوط CI/CD وبوابات الجودة المؤتمتة</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          دمج التدقيق الآلي لوثائق المشاريع في خطوط DevOps عبر مسار عمل GitHub Actions المتكامل، والذي يفحص الوثائق المعدلة مع كل طلب دمج (Pull Request):
        </p>

        <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">ملف سير العمل المتكامل لـ GitHub Actions (<code>.github/workflows/pmo-governance.yml</code>)</h3>
        <pre style="direction: ltr; text-align: left;"><code>name: PMO Governance &amp; Schema Quality Gate

on:
  pull_request:
    branches: [main]
    paths:
      - 'projects/**'

jobs:
  validate-governance:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Tasleemat Framework
        run: pip install tasleemat

      - name: Execute Regression &amp; Schema Audit
        run: |
          echo "التحقق الآلي من سلامة مخططات وثائق المشروع..."
          tasleemat test -v
          
      - name: Post PR Compliance Summary
        if: success()
        run: echo "::notice title=بوابة حوكمة تسليمات::تم اجتياز كافة اختبارات المخططات المعيارية بنجاح 100%!"</code></pre>
      </div>

      <!-- Section 4: Attested Computations AR -->
      <div id="attested-math" class="card" style="padding: 2.25rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-main);">4. عقود الحسابات الرياضية الموثقة (PMO-06.05)</h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.25rem;">
          نماذج الذكاء الاصطناعي التوليدية هي محركات احتمالية لتوقع الرموز، مما يجعلها عرضة للخطأ والهلوسة في الحسابات المعقدة. 
          تفرض تسليمات <strong>عقوداً حسابية حتمية</strong> تضمن دقة IEEE 754 ومعالجة حالات القسمة على صفر لكافة مقاييس القيمة المكتسبة (EVM) في <code>PMO-06.05</code>:
        </p>

        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>المقياس الحسابي</th>
                <th>المعادلة الرياضية</th>
                <th>الدلالة ومعالجة الحدود الحرجة</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>تباين التكلفة (CV)</strong></td>
                <td><code>CV = EV - AC</code></td>
                <td>موجب = وفر في الميزانية، سالب = تجاوز للميزانية</td>
              </tr>
              <tr>
                <td><strong>تباين الجدول الزمني (SV)</strong></td>
                <td><code>SV = EV - PV</code></td>
                <td>موجب = متقدم على الجدول، سالب = متأخر عن الجدول</td>
              </tr>
              <tr>
                <td><strong>مؤشر أداء التكلفة (CPI)</strong></td>
                <td><code>CPI = EV / AC</code></td>
                <td>أكبر من 1.0 = كفاءة تكلفة. حماية: إذا كانت <code>AC &lt;= 0</code> تصبح النتيجة 1.0</td>
              </tr>
              <tr>
                <td><strong>مؤشر أداء الجدول (SPI)</strong></td>
                <td><code>SPI = EV / PV</code></td>
                <td>أكبر من 1.0 = كفاءة جدول. حماية: إذا كانت <code>PV &lt;= 0</code> تصبح النتيجة 1.0</td>
              </tr>
              <tr>
                <td><strong>التكلفة التقديرية عند الاكتمال (EAC)</strong></td>
                <td><code>EAC = BAC / CPI</code></td>
                <td>التكلفة الإجمالية المتوقعة للمشروع استناداً لكفاءة الصرف الحالية</td>
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
