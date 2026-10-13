"""tools/site_builder/pages_developers.py
Generates the Developers & AI documentation pages in English and Arabic.
Accurately covers:
- Python SDK API reference (the 8 verified functions in `tasleemat`)
- CLI command reference (`tasleemat list`, `tasleemat asset`, `tasleemat validate`, `tasleemat mcp`)
- Model Context Protocol (MCP) server integration & tool signatures
- Companion JSON Schemas (Draft 2020-12) & semantic validation loops
"""

from tools.site_builder.theme import render_html_page


def generate_developers_en(base_url: str = "/Tasleemat") -> str:
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <div class="hero-pill">
          <span>⚙️ Engineering &amp; Automation</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.25rem;">Developers &amp; AI Integration Guide</h1>
        <p class="hero-subtitle">
          Python SDK, CLI tooling, Model Context Protocol (MCP), and Draft 2020-12 JSON Schema validation.
        </p>
      </div>
    </section>

    <div class="container" style="margin-top: 2.5rem; margin-bottom: 4rem;">
      <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
        
        <!-- Sidebar Navigation -->
        <aside style="width: 240px; flex-shrink: 0;">
          <div style="position: sticky; top: 5.5rem; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 0.5rem; padding: 1.25rem;">
            <div style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 0.75rem;">Sections</div>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.5rem; font-size: 0.9rem;">
              <li><a href="#quickstart">Quick Installation</a></li>
              <li><a href="#cli">CLI Command Reference</a></li>
              <li><a href="#sdk">Python SDK Reference</a></li>
              <li><a href="#mcp">Model Context Protocol (MCP)</a></li>
              <li><a href="#schemas">Draft 2020-12 Schemas</a></li>
            </ul>
          </div>
        </aside>

        <!-- Main Guide Content -->
        <div style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 2.5rem;">
          
          <!-- Section 1: Quickstart -->
          <section id="quickstart" class="card" style="padding: 2rem;">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.75rem;">1. Quick Installation</h2>
            <p style="color: var(--text-muted); margin-bottom: 1rem;">
              The <code>tasleemat</code> package is distributed via PyPI and supports Python 3.10, 3.11, 3.12, and 3.13.
            </p>
            <pre><code>pip install tasleemat</code></pre>
            <p style="color: var(--text-muted); font-size: 0.9rem;">
              Verify installation:
            </p>
            <pre><code>tasleemat --version</code></pre>
          </section>

          <!-- Section 2: CLI -->
          <section id="cli" class="card" style="padding: 2rem;">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.75rem;">2. CLI Command Reference</h2>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              The <code>tasleemat</code> CLI enables instant catalog exploration, asset extraction, tailoring analysis, and schema validation.
            </p>
            
            <h3 style="font-size: 1.15rem; margin-top: 1rem; margin-bottom: 0.5rem;">List Deliverables (<code>tasleemat list</code>)</h3>
            <pre><code># List all 114 deliverables in JSON or table
tasleemat list

# Filter by governance sizing tier and methodology pack
tasleemat list --tier 2 --pack agile

# Filter by lifecycle phase
tasleemat list --phase 04</code></pre>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Extract Assets (<code>tasleemat asset</code>)</h3>
            <pre><code># Extract template in English or Arabic
tasleemat asset PMO-04.14 template --lang en > risk_plan_template.md
tasleemat asset PMO-04.14 template --lang ar > risk_plan_template_ar.md

# Extract authoring guide, completed example, or prompt
tasleemat asset PMO-04.14 guide --lang en
tasleemat asset PMO-04.14 example --lang en
tasleemat asset PMO-04.14 prompt --lang en</code></pre>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Validate Deliverable JSON (<code>tasleemat validate</code>)</h3>
            <pre><code># Validate completed JSON data against canonical Draft 2020-12 schema
tasleemat validate PMO-04.14 ./my_project_risk_data.json</code></pre>
          </section>

          <!-- Section 3: SDK -->
          <section id="sdk" class="card" style="padding: 2rem;">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.75rem;">3. Python SDK API Reference</h2>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              The <code>tasleemat</code> module exports 8 primary functions for programmatic access:
            </p>

            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Function</th>
                    <th>Parameters</th>
                    <th>Returns</th>
                    <th>Description</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>list_artifacts()</code></td>
                    <td><code>tier=None, pack=None, phase=None</code></td>
                    <td><code>List[ArtifactSummary]</code></td>
                    <td>Returns summary objects for all 114 deliverables or tailored subset.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_definition()</code></td>
                    <td><code>artifact_id: str</code></td>
                    <td><code>dict</code></td>
                    <td>Full metadata dictionary including phase, tiers, and asset paths.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_assets()</code></td>
                    <td><code>artifact_id: str, lang='en'</code></td>
                    <td><code>ArtifactAssets</code></td>
                    <td>Structured paths to template, guide, prompt, schema, and example.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_asset()</code></td>
                    <td><code>artifact_id: str, asset_type: str, lang='en'</code></td>
                    <td><code>str</code></td>
                    <td>Raw text content of the requested asset file.</td>
                  </tr>
                  <tr>
                    <td><code>get_tailoring_profile()</code></td>
                    <td><code>tier: str, pack: str</code></td>
                    <td><code>List[str]</code></td>
                    <td>List of deliverable IDs required for the given tier and pack.</td>
                  </tr>
                  <tr>
                    <td><code>get_lexicon()</code></td>
                    <td><code>search=None</code></td>
                    <td><code>List[dict]</code></td>
                    <td>Bilingual project management terminology mappings.</td>
                  </tr>
                  <tr>
                    <td><code>validate_artifact_data()</code></td>
                    <td><code>artifact_id: str, data: dict, mode='strict'</code></td>
                    <td><code>ValidationResult</code></td>
                    <td>Validates JSON payload against Draft 2020-12 companion schema.</td>
                  </tr>
                  <tr>
                    <td><code>render_artifact()</code></td>
                    <td><code>artifact_id: str, data: dict, lang='en'</code></td>
                    <td><code>str</code></td>
                    <td>Renders filled markdown document by merging data with template.</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">SDK Example</h3>
            <pre><code>import tasleemat

# 1. Fetch tailored list for Tier 2 Agile
artifacts = tasleemat.list_artifacts(tier="2", pack="agile")
print(f"Found {{len(artifacts)}} required deliverables.")

# 2. Get English Guide text for PMO-03.01 Project Charter
guide_text = tasleemat.get_artifact_asset("PMO-03.01", "guide", lang="en")

# 3. Validate completed project charter data
charter_data = {{
    "project_id": "PRJ-2026-001",
    "project_title": "Enterprise Cloud Migration",
    "sponsor": "Executive VP Operations",
    "budget": 2500000.00
}}
result = tasleemat.validate_artifact_data("PMO-03.01", charter_data)
if result.valid:
    print("Charter data is schema-compliant!")
else:
    for err in result.errors:
        print(f"Validation error at {{err.field_path}}: {{err.message}}")</code></pre>
          </section>

          <!-- Section 4: MCP -->
          <section id="mcp" class="card" style="padding: 2rem;">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.75rem;">4. Model Context Protocol (MCP) Server</h2>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              Tasleemat includes a standard stdio MCP server for direct integration with AI developer tools (Claude Desktop, Cursor, Antigravity, OpenCode).
            </p>
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Configuration (claude_desktop_config.json)</h3>
            <pre><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat",
      "args": ["mcp"]
    }}
  }}
}}</code></pre>
            <p style="color: var(--text-muted); margin-top: 1rem; margin-bottom: 0.5rem;">
              Alternatively, invoke via the standalone binary <code>tasleemat-mcp</code>:
            </p>
            <pre><code>tasleemat-mcp</code></pre>
            
            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Exposed MCP Tools</h3>
            <ul style="margin-left: 1.5rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-muted);">
              <li><code>list_artifacts(tier, pack, phase)</code>: List available deliverables.</li>
              <li><code>get_artifact_definition(artifact_id)</code>: Retrieve deliverable metadata.</li>
              <li><code>get_artifact_asset(artifact_id, asset_type, lang)</code>: Fetch template, guide, prompt, schema, or example.</li>
              <li><code>get_tailoring_profile(tier, pack)</code>: Get recommended deliverable bundle.</li>
              <li><code>validate_artifact_data(artifact_id, data, mode)</code>: Validate deliverable JSON against schema.</li>
            </ul>
          </section>

          <!-- Section 5: Schemas -->
          <section id="schemas" class="card" style="padding: 2rem;">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.75rem;">5. Draft 2020-12 Companion Schemas</h2>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              Every one of the 114 deliverables is paired with a companion JSON Schema conforming to the <strong>JSON Schema Draft 2020-12</strong> specification with strict RFC format validation (dates, currencies, URIs, emails).
            </p>
            <p style="color: var(--text-muted); margin-bottom: 1rem;">
              These schemas turn unstructured project documentation into machine-verifiable data contracts. When pairing with LLMs, schemas provide explicit feedback for deterministic autonomous self-correction loops.
            </p>
            <pre><code># Example: Check companion schema location
tasleemat asset PMO-04.14 schema --lang en</code></pre>
          </section>

        </div>
      </div>
    </div>
    """

    return render_html_page(
        title="Developers & AI Integration Guide",
        content=content,
        lang="en",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/ar/developers/",
    )


def generate_developers_ar(base_url: str = "/Tasleemat") -> str:
    content = f"""
    <section class="hero-section" style="padding: 3rem 0 2rem;">
      <div class="container">
        <div class="hero-pill">
          <span>⚙️ الهندسة والأتمتة التقنية</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.25rem;">دليل المطورين وتكامل الذكاء الاصطناعي</h1>
        <p class="hero-subtitle">
          مكتبة بايثون، أمر التشغيل (CLI)، بروتوكول سياق النماذج (MCP)، والتحقق من مخططات Draft 2020-12.
        </p>
      </div>
    </section>

    <div class="container" style="margin-top: 2.5rem; margin-bottom: 4rem;">
      <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
        
        <!-- Sidebar Navigation AR -->
        <aside style="width: 240px; flex-shrink: 0;">
          <div style="position: sticky; top: 5.5rem; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 0.5rem; padding: 1.25rem;">
            <div style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 0.75rem;">فهرس الدليل</div>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.5rem; font-size: 0.9rem;">
              <li><a href="#quickstart">التثبيت السريع</a></li>
              <li><a href="#cli">مرجع أوامر الطرفية (CLI)</a></li>
              <li><a href="#sdk">مرجع مكتبة بايثون (SDK)</a></li>
              <li><a href="#mcp">بروتوكول سياق النماذج (MCP)</a></li>
              <li><a href="#schemas">مخططات Draft 2020-12</a></li>
            </ul>
          </div>
        </aside>

        <!-- Main Guide Content AR -->
        <div style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 2.5rem;">
          
          <!-- Section 1: Quickstart AR -->
          <section id="quickstart" class="card" style="padding: 2rem;">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.75rem;">1. التثبيت السريع</h2>
            <p style="color: var(--text-muted); margin-bottom: 1rem;">
              حزمة <code>tasleemat</code> منشورة رسمياً عبر مستودع PyPI وتدعم إصدارات بايثون 3.10، 3.11، 3.12، و3.13.
            </p>
            <pre><code>pip install tasleemat</code></pre>
            <p style="color: var(--text-muted); font-size: 0.9rem;">
              التحقق من نجاح التثبيت ورقم الإصدار:
            </p>
            <pre><code>tasleemat --version</code></pre>
          </section>

          <!-- Section 2: CLI AR -->
          <section id="cli" class="card" style="padding: 2rem;">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.75rem;">2. مرجع أوامر الطرفية (CLI)</h2>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              تتيح أداة <code>tasleemat</code> في سطر الأوامر استكشاف الفهرس، واستخراج الأصول، وتحليل التخصيص، والتحقق من صحة البيانات.
            </p>
            
            <h3 style="font-size: 1.15rem; margin-top: 1rem; margin-bottom: 0.5rem;">استعراض التسليمات (<code>tasleemat list</code>)</h3>
            <pre><code># استعراض كافة التسليمات الـ 114
tasleemat list

# التصفية بحسب مستوى الحوكمة وحزمة المنهجية
tasleemat list --tier 2 --pack agile

# التصفية بحسب المرحلة
tasleemat list --phase 04</code></pre>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">استخراج الأصول والقوالب (<code>tasleemat asset</code>)</h3>
            <pre><code># تصدير قالب التسليمة بالعربية أو الإنجليزية
tasleemat asset PMO-04.14 template --lang ar > risk_plan_ar.md
tasleemat asset PMO-04.14 template --lang en > risk_plan_en.md

# تصدير الدليل الإرشادي، أو المثال الواقعي، أو موجه الذكاء الاصطناعي
tasleemat asset PMO-04.14 guide --lang ar
tasleemat asset PMO-04.14 example --lang ar
tasleemat asset PMO-04.14 prompt --lang ar</code></pre>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">التحقق من صحة ملفات JSON (<code>tasleemat validate</code>)</h3>
            <pre><code># التحقق من بيانات التسليمة مقابل مخطط Draft 2020-12 المعتمد
tasleemat validate PMO-04.14 ./my_project_risk_data.json</code></pre>
          </section>

          <!-- Section 3: SDK AR -->
          <section id="sdk" class="card" style="padding: 2rem;">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.75rem;">3. مرجع مكتبة بايثون البرمجية (SDK)</h2>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              تصدّر مكتبة <code>tasleemat</code> ثماني دوال برمجية أساسية للاستخدام في تطبيقات بايثون:
            </p>

            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>الدالة</th>
                    <th>المعاملات</th>
                    <th>المخرجات</th>
                    <th>الوصف</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>list_artifacts()</code></td>
                    <td><code>tier, pack, phase</code></td>
                    <td><code>List[ArtifactSummary]</code></td>
                    <td>استرجاع كائنات ملخصة لكافة الـ 114 تسليمة أو جزء مخصص منها.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_definition()</code></td>
                    <td><code>artifact_id: str</code></td>
                    <td><code>dict</code></td>
                    <td>قاموس البيانات الوصفية الكامل متضمناً المرحلة والمستويات ومسارات الأصول.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_assets()</code></td>
                    <td><code>artifact_id: str, lang='en'</code></td>
                    <td><code>ArtifactAssets</code></td>
                    <td>مسارات القالب والدليل والموجه والمخطط والمثال الواقعي.</td>
                  </tr>
                  <tr>
                    <td><code>get_artifact_asset()</code></td>
                    <td><code>artifact_id, asset_type, lang</code></td>
                    <td><code>str</code></td>
                    <td>المحتوى النصي الخام للأصل المطلوب باللغة المحددة.</td>
                  </tr>
                  <tr>
                    <td><code>get_tailoring_profile()</code></td>
                    <td><code>tier: str, pack: str</code></td>
                    <td><code>List[str]</code></td>
                    <td>قائمة معرفات التسليمات المطلوبة للمستوى والحزمة المحددة.</td>
                  </tr>
                  <tr>
                    <td><code>get_lexicon()</code></td>
                    <td><code>search=None</code></td>
                    <td><code>List[dict]</code></td>
                    <td>مصطلحات إدارة المشاريع المعيارية المترجمة بين اللغتين.</td>
                  </tr>
                  <tr>
                    <td><code>validate_artifact_data()</code></td>
                    <td><code>artifact_id, data, mode</code></td>
                    <td><code>ValidationResult</code></td>
                    <td>التحقق من صحة بيانات JSON مقابل مخطط Draft 2020-12.</td>
                  </tr>
                  <tr>
                    <td><code>render_artifact()</code></td>
                    <td><code>artifact_id, data, lang</code></td>
                    <td><code>str</code></td>
                    <td>توليد مستند Markdown مكتمل عبر دمج البيانات في القالب المعتمد.</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">مثال تطبيقي في بايثون</h3>
            <pre><code>import tasleemat

# 1. استخراج التسليمات المطلوبة لمشروع قياسي يتبع المنهجية الرشيقة
artifacts = tasleemat.list_artifacts(tier="2", pack="agile")
print(f"عدد التسليمات الإلزامية: {{len(artifacts)}}")

# 2. قراءة الدليل العربي لميثاق المشروع PMO-03.01
guide_ar = tasleemat.get_artifact_asset("PMO-03.01", "guide", lang="ar")

# 3. التحقق من بيانات ميثاق المشروع
charter_data = {{
    "project_id": "PRJ-2026-001",
    "project_title": "التحول الرقمي السحابي",
    "sponsor": "نائب الرئيس التنفيذي للعمليات",
    "budget": 2500000.00
}}
result = tasleemat.validate_artifact_data("PMO-03.01", charter_data)
if result.valid:
    print("البيانات متوافقة مع المخطط!")
else:
    for err in result.errors:
        print(f"خطأ في الحقل {{err.field_path}}: {{err.message}}")</code></pre>
          </section>

          <!-- Section 4: MCP AR -->
          <section id="mcp" class="card" style="padding: 2rem;">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.75rem;">4. بروتوكول سياق النماذج (MCP) للذكاء الاصطناعي</h2>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              تتضمن تسليمات خادم MCP قياسي يعمل عبر قنوات الإدخال والإخراج المعيارية (stdio) للربط المباشر مع أدوات التطوير المدعومة بالذكاء الاصطناعي.
            </p>
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">ملف إعدادات العميل (claude_desktop_config.json)</h3>
            <pre><code>{{
  "mcpServers": {{
    "tasleemat": {{
      "command": "tasleemat",
      "args": ["mcp"]
    }}
  }}
}}</code></pre>
            <p style="color: var(--text-muted); margin-top: 1rem; margin-bottom: 0.5rem;">
              أو تشغيل الخادم المستقل مباشرة عبر الطرفية:
            </p>
            <pre><code>tasleemat-mcp</code></pre>
          </section>

          <!-- Section 5: Schemas AR -->
          <section id="schemas" class="card" style="padding: 2rem;">
            <h2 style="font-size: 1.5rem; margin-bottom: 0.75rem;">5. مخططات JSON المرافقة (Draft 2020-12)</h2>
            <p style="color: var(--text-muted); margin-bottom: 1.25rem;">
              كل تسليمة من الـ 114 مقترنة بمخطط JSON رسمي متوافق مع معيار <strong>Draft 2020-12</strong> مع التحقق الصارم من التنسيقات (التواريخ، العملات، الروابط، البريد).
            </p>
            <p style="color: var(--text-muted); margin-bottom: 1rem;">
              تحول هذه المخططات وثائق المشاريع غير المنظمة إلى عقود رقمية منضبطة تتيح لنماذج الذكاء الاصطناعي إجراء تصحيح ذاتي آلي قبل الاعتماد البشري.
            </p>
            <pre><code>tasleemat asset PMO-04.14 schema --lang ar</code></pre>
          </section>

        </div>
      </div>
    </div>
    """

    return render_html_page(
        title="دليل المطورين وتكامل الذكاء الاصطناعي",
        content=content,
        lang="ar",
        active_nav="developers",
        base_url=base_url,
        alt_lang_url=f"{base_url}/developers/",
    )
