"""tools/site_builder/pages_dev/nav.py
Shared subnavigation bar for all Developer Portal pages (English and Arabic).
"""

def render_dev_subnav(active_slug: str, lang: str, base_url: str) -> str:
    """Renders the top subnav bar across developer pages."""
    is_ar = lang == "ar"
    prefix = f"{base_url}/ar/developers" if is_ar else f"{base_url}/developers"

    pages = [
        {"slug": "hub", "en": "📖 Developers Hub", "ar": "📖 بوابة المطورين", "url": f"{prefix}/"},
        {"slug": "cli", "en": "⌨️ CLI Tooling & Automation", "ar": "⌨️ أداة الطرفية والأتمتة", "url": f"{prefix}/cli/"},
        {"slug": "sdk", "en": "🐍 Python SDK & API", "ar": "🐍 مكتبة بايثون (SDK)", "url": f"{prefix}/sdk/"},
        {"slug": "mcp", "en": "🔌 MCP Server & IDEs", "ar": "🔌 خادم بروتوكول MCP", "url": f"{prefix}/mcp/"},
        {"slug": "schemas", "en": "📐 Schemas & Validation", "ar": "📐 المخططات والتحقق", "url": f"{prefix}/schemas/"},
        {"slug": "agentic", "en": "🤖 Agentic Swarms & CI/CD", "ar": "🤖 أسراب الوكلاء و CI/CD", "url": f"{prefix}/agentic/"},
    ]

    links = []
    for p in pages:
        is_active = p["slug"] == active_slug
        active_class = "active" if is_active else ""
        title = p["ar" if is_ar else "en"]
        active_style = "background: var(--accent-blue); color: #fff; border-color: var(--accent-blue);" if is_active else ""
        links.append(f'<a href="{p["url"]}" class="btn-utility {active_class}" style="font-size: 0.82rem; padding: 0.38rem 0.85rem; font-weight: 600; {active_style}">{title}</a>')

    label = "الأقسام الفنية:" if is_ar else "Sections:"
    return f"""
    <div style="background: var(--bg-card); border-bottom: 1px solid var(--border-color); padding: 0.75rem 0; margin-bottom: 2rem;">
      <div class="container" style="display: flex; gap: 0.5rem; flex-wrap: wrap; align-items: center;">
        <span style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted); margin-right: 0.5rem; text-transform: uppercase;">
          {label}
        </span>
        {"".join(links)}
      </div>
    </div>
    """
