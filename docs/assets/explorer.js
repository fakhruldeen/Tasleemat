/**
 * Tasleemat PMO Interactive Deliverables Explorer & Multi-Artifact Drawer
 * Aligned with PMOSkills Obsidian Dark Aesthetic, Full Bilingual EN/AR & LTR/RTL Precision
 */

(function () {
  // Lightweight markdown-to-HTML parser for fast, client-side artifact rendering
  function renderMarkdown(md) {
    if (!md) return '<div class="empty-state">No content available.</div>';

    // Strip internal HTML comments and metadata wrappers
    let text = md.replace(/<!--[\s\S]*?-->/g, "").trim();

    // Escape raw HTML entities except supported tags
    text = text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    text = text.replace(/&lt;(\/?)div(.*?)&gt;/g, "<$1div$2>");
    text = text.replace(/&lt;(\/?)span(.*?)&gt;/g, "<$1span$2>");
    text = text.replace(/&lt;(\/?)strong(.*?)&gt;/g, "<$1strong$2>");
    text = text.replace(/&lt;(\/?)em(.*?)&gt;/g, "<$1em$2>");
    text = text.replace(/&lt;(\/?)i(.*?)&gt;/g, "<$1i$2>");
    text = text.replace(/&lt;(\/?)b(.*?)&gt;/g, "<$1b$2>");
    text = text.replace(/&lt;(\/?)p(.*?)&gt;/g, "<$1p$2>");
    text = text.replace(/&lt;(\/?)br&gt;/g, "<br>");
    text = text.replace(/&lt;a href="(.*?)"(.*?)&gt;(.*?)&lt;\/a&gt;/g, '<a href="$1"$2 target="_blank">$3</a>');

    // Code blocks (fenced ```)
    text = text.replace(/```([a-z]*)\n([\s\S]*?)```/g, function (_, lang, code) {
      return '<pre class="code-block"><code class="language-' + (lang || "text") + '">' + code.trim() + "</code></pre>";
    });

    // Inline code `code`
    text = text.replace(/`([^`]+)`/g, '<code class="inline-code">$1</code>');

    // Headers
    text = text.replace(/^###### (.*$)/gim, '<h6 class="md-h6">$1</h6>');
    text = text.replace(/^##### (.*$)/gim, '<h5 class="md-h5">$1</h5>');
    text = text.replace(/^#### (.*$)/gim, '<h4 class="md-h4">$1</h4>');
    text = text.replace(/^### (.*$)/gim, '<h3 class="md-h3">$1</h3>');
    text = text.replace(/^## (.*$)/gim, '<h2 class="md-h2">$1</h2>');
    text = text.replace(/^# (.*$)/gim, '<h1 class="md-h1">$1</h1>');

    // Horizontal Rule
    text = text.replace(/^---$/gim, '<hr class="md-hr" />');

    // Bold & Italic
    text = text.replace(/\*\*\*([^*]+)\*\*\*/g, "<strong><em>$1</em></strong>");
    text = text.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    text = text.replace(/\*([^*]+)\*/g, "<em>$1</em>");

    // Blockquotes
    text = text.replace(/^\> (.*$)/gim, '<blockquote class="md-blockquote">$1</blockquote>');

    // Tables
    const lines = text.split("\n");
    let inTable = false;
    let tableHtml = "";
    let processedLines = [];

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      if (line.startsWith("|") && line.endsWith("|")) {
        const cells = line.split("|").slice(1, -1).map(c => c.trim());
        if (!inTable) {
          inTable = true;
          tableHtml = '<div class="table-responsive"><table class="md-table"><thead><tr>';
          cells.forEach(c => {
            tableHtml += `<th>${c}</th>`;
          });
          tableHtml += "</tr></thead><tbody>";
        } else if (line.includes("---")) {
          // Separator row, skip
          continue;
        } else {
          tableHtml += "<tr>";
          cells.forEach(c => {
            tableHtml += `<td>${c}</td>`;
          });
          tableHtml += "</tr>";
        }
      } else {
        if (inTable) {
          inTable = false;
          tableHtml += "</tbody></table></div>";
          processedLines.push(tableHtml);
          tableHtml = "";
        }
        processedLines.push(line);
      }
    }
    if (inTable) {
      tableHtml += "</tbody></table></div>";
      processedLines.push(tableHtml);
    }

    text = processedLines.join("\n");

    // Unordered Lists
    text = text.replace(/^\s*[-*]\s+(.*$)/gim, '<li class="md-li">$1</li>');
    text = text.replace(/(<li class="md-li">[\s\S]*?<\/li>)/gim, '<ul class="md-ul">$1</ul>');

    // Paragraphs
    const blocks = text.split(/\n\n+/);
    text = blocks.map(b => {
      b = b.trim();
      if (!b) return "";
      if (b.startsWith("<h") || b.startsWith("<ul") || b.startsWith("<ol") || b.startsWith("<div") || b.startsWith("<pre") || b.startsWith("<blockquote") || b.startsWith("<hr")) {
        return b;
      }
      return '<p class="md-p">' + b.replace(/\n/g, "<br />") + '</p>';
    }).join("\n");

    return text;
  }

  document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("tasleemat-explorer");
    if (!container) return;

    const data = window.TASLEEMAT_DATA || [];
    const isArabic = document.documentElement.lang === "ar" || container.getAttribute("dir") === "rtl" || window.location.pathname.includes("/ar/");

    let activePhase = "all";
    let activeTier = "all";
    let searchQuery = "";
    let activeDeliverable = null;
    let activeTab = "template";
    let modalLang = isArabic ? "ar" : "en";

    // Build the complete interactive UI inside container
    container.innerHTML = `
      <div class="explorer-dashboard ${isArabic ? 'rtl-dashboard' : ''}" dir="${isArabic ? 'rtl' : 'ltr'}">
        <!-- Explorer Header Control Bar -->
        <div class="explorer-header-bar">
          <div class="explorer-search-wrapper">
            <span class="search-icon">🔍</span>
            <input 
              type="text" 
              id="dash-search-input" 
              class="dash-search-box" 
              placeholder="${isArabic ? 'بحث فوري برمز النموذج (مثل PMO-03.01) أو الاسم أو المرحلة أو المتطلبات...' : 'Search by code (e.g. PMO-03.01), deliverable name, phase, tier, or keyword...'}"
            />
            <button id="dash-clear-search" class="dash-clear-btn" style="display: none;">✕</button>
          </div>
          <div class="explorer-stat-summary">
            <span class="stat-pill"><strong id="dash-visible-count">${data.length}</strong> / ${data.length} ${isArabic ? 'مخرجاً إدارياً' : 'Deliverables'}</span>
          </div>
        </div>

        <!-- Filter Chips: Lifecycle Phases -->
        <div class="explorer-filter-section">
          <div class="filter-label-title">${isArabic ? 'مراحل دورة حياة المشروع:' : 'Lifecycle Phases:'}</div>
          <div class="phase-chip-group">
            <button class="phase-chip active" data-phase="all">${isArabic ? 'الكل (102)' : 'All (102)'}</button>
            <button class="phase-chip" data-phase="00">🏛️ ${isArabic ? '00. المحافظ (6)' : '00. Portfolio (6)'}</button>
            <button class="phase-chip" data-phase="01">💎 ${isArabic ? '01. القيمة (4)' : '01. Value (4)'}</button>
            <button class="phase-chip" data-phase="02">⚖️ ${isArabic ? '02. التخصيص (6)' : '02. Approach (6)'}</button>
            <button class="phase-chip" data-phase="03">🚀 ${isArabic ? '03. البدء (5)' : '03. Initiating (5)'}</button>
            <button class="phase-chip" data-phase="04">📐 ${isArabic ? '04. التخطيط (47)' : '04. Planning (47)'}</button>
            <button class="phase-chip" data-phase="05">⚡ ${isArabic ? '05. التنفيذ (12)' : '05. Executing (12)'}</button>
            <button class="phase-chip" data-phase="06">📊 ${isArabic ? '06. المراقبة (12)' : '06. Monitoring (12)'}</button>
            <button class="phase-chip" data-phase="07">🏁 ${isArabic ? '07. الإغلاق (5)' : '07. Closing (5)'}</button>
          </div>
        </div>

        <!-- Filter Chips: Project Sizing Tiers -->
        <div class="explorer-tier-section">
          <div class="tier-chip-group">
            <button class="tier-chip active" data-tier="all">${isArabic ? 'كافة المستويات' : 'All Tiers'}</button>
            <button class="tier-chip" data-tier="Tier 1">${isArabic ? 'المستوى 1 (المشاريع الكبرى)' : 'Tier 1 (Major)'}</button>
            <button class="tier-chip" data-tier="Tier 2">${isArabic ? 'المستوى 2 (المتوسطة)' : 'Tier 2 (Medium)'}</button>
            <button class="tier-chip" data-tier="Tier 3">${isArabic ? 'المستوى 3 (الرشيقة / السريعة)' : 'Tier 3 (Lean/Agile)'}</button>
            <button class="tier-chip tier-chip-ai" data-tier="Tier 4">${isArabic ? 'المستوى 4 (الذكاء الاصطناعي 🤖)' : 'Tier 4 (AI Governance 🤖)'}</button>
          </div>
        </div>

        <!-- Deliverables Grid Container -->
        <div id="dash-deliverables-grid" class="dash-grid"></div>

        <!-- Empty State Message -->
        <div id="dash-empty-message" class="dash-empty-box" style="display: none;">
          <div class="empty-icon">🔍</div>
          <h3>${isArabic ? 'لم يتم العثور على مخرجات مطابقة' : 'No matching deliverables found'}</h3>
          <p>${isArabic ? 'يرجى تجربة كلمات بحث أخرى أو إلغاء تفعيل الفلاتر.' : 'Try adjusting your search query or removing active filters.'}</p>
        </div>
      </div>

      <!-- Slide-Over Multi-Artifact Interactive Modal -->
      <div id="tasleemat-modal-backdrop" class="tasleemat-modal-overlay" style="display: none;">
        <div class="tasleemat-modal-container" role="dialog" aria-modal="true">
          <!-- Modal Header -->
          <div class="modal-top-header">
            <div class="modal-title-area">
              <div class="modal-badges">
                <span id="modal-code-badge" class="badge badge-code">PMO-00.01</span>
                <span id="modal-phase-badge" class="badge badge-phase">Phase</span>
                <span id="modal-tier-badge" class="badge badge-tier">Tier</span>
              </div>
              <h2 id="modal-doc-title" class="modal-heading">Deliverable Title</h2>
            </div>
            <div class="modal-header-actions">
              <button id="modal-lang-toggle" class="btn-modal-lang">🇸🇦 النسخة العربية</button>
              <button id="modal-close-btn" class="btn-modal-close" title="Close (Esc)">✕</button>
            </div>
          </div>

          <!-- Modal Tabs Bar -->
          <div class="modal-tabs-bar">
            <button class="modal-tab-btn active" data-tab="template">📋 ${isArabic ? 'القالب القياسي' : 'Blank Template'}</button>
            <button class="modal-tab-btn" data-tab="guide">📖 ${isArabic ? 'الدليل الإرشادي' : 'Authoring Guide'}</button>
            <button class="modal-tab-btn" data-tab="example">💡 ${isArabic ? 'مثال واقعي مكتمل' : 'Reference Example'}</button>
            <button class="modal-tab-btn" data-tab="prompt">🤖 ${isArabic ? 'أمر التوليد الذكي (Prompt)' : 'AI Agent Prompt'}</button>
            <button class="modal-tab-btn" data-tab="schema">📊 ${isArabic ? 'مخطط البيانات (JSON/CSV)' : 'Data Schema'}</button>
          </div>

          <!-- Modal Action Bar (Copy / Download / GitHub) -->
          <div class="modal-action-bar">
            <button id="modal-copy-btn" class="modal-act-btn">📋 ${isArabic ? 'نسخ المحتوى' : 'Copy Content'}</button>
            <button id="modal-download-btn" class="modal-act-btn">⬇️ ${isArabic ? 'تحميل الملف' : 'Download File'}</button>
            <a id="modal-github-btn" class="modal-act-btn modal-gh-btn" href="#" target="_blank" rel="noopener noreferrer">🐙 ${isArabic ? 'عرض على GitHub' : 'View on GitHub'} ↗</a>
            <span id="modal-toast" class="modal-toast-msg" style="display: none;">✓ ${isArabic ? 'تم النسخ إلى الحافظة بنجاح!' : 'Copied to clipboard!'}</span>
          </div>

          <!-- Modal Content Body -->
          <div id="modal-content-body" class="modal-body-scroll markdown-body"></div>
        </div>
      </div>
    `;

    const searchInput = document.getElementById("dash-search-input");
    const clearSearchBtn = document.getElementById("dash-clear-search");
    const visibleCountEl = document.getElementById("dash-visible-count");
    const grid = document.getElementById("dash-deliverables-grid");
    const emptyMsg = document.getElementById("dash-empty-message");
    const phaseChips = document.querySelectorAll(".phase-chip");
    const tierChips = document.querySelectorAll(".tier-chip");

    const modalBackdrop = document.getElementById("tasleemat-modal-backdrop");
    const modalCloseBtn = document.getElementById("modal-close-btn");
    const modalLangBtn = document.getElementById("modal-lang-toggle");
    const modalCopyBtn = document.getElementById("modal-copy-btn");
    const modalDownloadBtn = document.getElementById("modal-download-btn");
    const modalGithubBtn = document.getElementById("modal-github-btn");
    const modalToast = document.getElementById("modal-toast");
    const modalTabBtns = document.querySelectorAll(".modal-tab-btn");
    const modalBody = document.getElementById("modal-content-body");

    const modalCodeBadge = document.getElementById("modal-code-badge");
    const modalPhaseBadge = document.getElementById("modal-phase-badge");
    const modalTierBadge = document.getElementById("modal-tier-badge");
    const modalDocTitle = document.getElementById("modal-doc-title");

    function renderGrid() {
      grid.innerHTML = "";
      let visible = 0;

      data.forEach((item) => {
        const matchesPhase = activePhase === "all" || item.phase === activePhase;
        const matchesTier = activeTier === "all" || item.tier.includes(activeTier);
        const searchTarget = (item.code + " " + item.name_en + " " + item.name_ar + " " + item.phase_name_en + " " + item.phase_name_ar + " " + item.tier).toLowerCase();
        const matchesSearch = !searchQuery || searchTarget.includes(searchQuery);

        if (matchesPhase && matchesTier && matchesSearch) {
          visible++;
          const card = document.createElement("div");
          card.className = "dash-card glass-card " + (item.tier.includes("Tier 4") ? "glow-skill" : "glow-ref");

          const title = isArabic ? item.name_ar : item.name_en;
          const altTitle = isArabic ? item.name_en : item.name_ar;

          card.innerHTML = `
            <div class="dash-card-header">
              <span class="badge badge-code">${item.code}</span>
              <span class="badge badge-phase">${item.phase_icon} ${isArabic ? item.phase_name_ar : item.phase_name_en}</span>
              <span class="badge ${item.tier.includes('Tier 4') ? 'badge-skill' : 'badge-ref'}">${item.tier.split('|')[0].trim()}</span>
            </div>
            <h3 class="dash-card-title">${title}</h3>
            <div class="dash-card-sub">${altTitle}</div>
            <div class="dash-card-actions">
              <button class="card-btn btn-primary-act" data-code="${item.code}" data-tab="template">📋 ${isArabic ? 'القالب' : 'Template'}</button>
              <button class="card-btn btn-sec-act" data-code="${item.code}" data-tab="guide">📖 ${isArabic ? 'الدليل' : 'Guide'}</button>
              <button class="card-btn btn-sec-act" data-code="${item.code}" data-tab="example">💡 ${isArabic ? 'المثال' : 'Example'}</button>
              <button class="card-btn btn-sec-act" data-code="${item.code}" data-tab="prompt">🤖 ${isArabic ? 'الأمر' : 'Prompt'}</button>
            </div>
          `;

          // Clicking buttons opens specific tabs
          card.querySelectorAll(".card-btn").forEach((b) => {
            b.addEventListener("click", function (e) {
              e.stopPropagation();
              const tab = this.getAttribute("data-tab");
              openModal(item, tab);
            });
          });

          // Clicking card opens template
          card.addEventListener("click", function () {
            openModal(item, "template");
          });

          grid.appendChild(card);
        }
      });

      visibleCountEl.textContent = visible;
      emptyMsg.style.display = visible === 0 ? "block" : "none";
    }

    function openModal(item, tab) {
      activeDeliverable = item;
      activeTab = tab || "template";
      modalLang = isArabic ? "ar" : "en";

      updateModalUI();
      modalBackdrop.style.display = "flex";
      document.body.style.overflow = "hidden";
    }

    function closeModal() {
      modalBackdrop.style.display = "none";
      document.body.style.overflow = "";
      activeDeliverable = null;
    }

    function getActiveContent() {
      if (!activeDeliverable) return "";
      const isAr = modalLang === "ar";
      switch (activeTab) {
        case "template":
          return isAr ? activeDeliverable.template_ar : activeDeliverable.template_en;
        case "guide":
          return isAr ? activeDeliverable.guide_ar : activeDeliverable.guide_en;
        case "example":
          return isAr ? activeDeliverable.example_ar : activeDeliverable.example_en;
        case "prompt":
          return isAr ? activeDeliverable.prompt_ar : activeDeliverable.prompt_en;
        case "schema":
          return isAr ? activeDeliverable.json_ar : activeDeliverable.json_en;
        default:
          return "";
      }
    }

    function updateModalUI() {
      if (!activeDeliverable) return;
      const isAr = modalLang === "ar";

      modalCodeBadge.textContent = activeDeliverable.code;
      modalPhaseBadge.textContent = activeDeliverable.phase_icon + " " + (isAr ? activeDeliverable.phase_name_ar : activeDeliverable.phase_name_en);
      modalTierBadge.textContent = activeDeliverable.tier;
      modalDocTitle.textContent = isAr ? activeDeliverable.name_ar : activeDeliverable.name_en;

      modalLangBtn.textContent = isAr ? "🇬🇧 English Version" : "🇸🇦 النسخة العربية";

      modalTabBtns.forEach((b) => {
        b.classList.toggle("active", b.getAttribute("data-tab") === activeTab);
      });

      const rawContent = getActiveContent();

      if (activeTab === "schema") {
        try {
          const parsed = JSON.parse(rawContent);
          modalBody.innerHTML = '<pre class="code-block"><code class="language-json">' + JSON.stringify(parsed, null, 2) + '</code></pre>';
        } catch (_) {
          modalBody.innerHTML = '<pre class="code-block"><code>' + rawContent + '</code></pre>';
        }
      } else {
        modalBody.innerHTML = renderMarkdown(rawContent);
      }

      modalBody.setAttribute("dir", isAr ? "rtl" : "ltr");

      // Update GitHub Source URL
      let ghUrl = "";
      if (activeTab === "template") ghUrl = isAr ? activeDeliverable.gh_tpl_ar : activeDeliverable.gh_tpl_en;
      else if (activeTab === "guide") ghUrl = isAr ? activeDeliverable.gh_guide_ar : activeDeliverable.gh_guide_en;
      else if (activeTab === "example") ghUrl = isAr ? activeDeliverable.gh_ex_ar : activeDeliverable.gh_ex_en;
      else if (activeTab === "prompt") ghUrl = isAr ? activeDeliverable.gh_prompt_ar : activeDeliverable.gh_prompt_en;
      else if (activeTab === "schema") ghUrl = isAr ? activeDeliverable.gh_json_ar : activeDeliverable.gh_json_en;

      if (ghUrl) {
        modalGithubBtn.href = ghUrl;
        modalGithubBtn.style.display = "inline-flex";
      } else {
        modalGithubBtn.style.display = "none";
      }
      modalGithubBtn.innerHTML = `🐙 ${isAr ? 'عرض على GitHub' : 'View on GitHub'} ↗`;
    }

    // Search Box Listener
    searchInput.addEventListener("input", function (e) {
      searchQuery = e.target.value.toLowerCase().trim();
      clearSearchBtn.style.display = searchQuery ? "block" : "none";
      renderGrid();
    });

    clearSearchBtn.addEventListener("click", function () {
      searchInput.value = "";
      searchQuery = "";
      clearSearchBtn.style.display = "none";
      renderGrid();
      searchInput.focus();
    });

    // Phase Chips Listener
    phaseChips.forEach((btn) => {
      btn.addEventListener("click", function () {
        phaseChips.forEach((b) => b.classList.remove("active"));
        this.classList.add("active");
        activePhase = this.getAttribute("data-phase");
        renderGrid();
      });
    });

    // Tier Chips Listener
    tierChips.forEach((btn) => {
      btn.addEventListener("click", function () {
        tierChips.forEach((b) => b.classList.remove("active"));
        this.classList.add("active");
        activeTier = this.getAttribute("data-tier");
        renderGrid();
      });
    });

    // Modal Tab Buttons Listener
    modalTabBtns.forEach((b) => {
      b.addEventListener("click", function () {
        activeTab = this.getAttribute("data-tab");
        updateModalUI();
      });
    });

    // Language Toggle inside Modal
    modalLangBtn.addEventListener("click", function () {
      modalLang = modalLang === "ar" ? "en" : "ar";
      updateModalUI();
    });

    // Copy Button
    modalCopyBtn.addEventListener("click", function () {
      const content = getActiveContent();
      if (!content) return;
      navigator.clipboard.writeText(content).then(() => {
        modalToast.style.display = "inline-block";
        setTimeout(() => {
          modalToast.style.display = "none";
        }, 2500);
      });
    });

    // Download Button
    modalDownloadBtn.addEventListener("click", function () {
      const content = getActiveContent();
      if (!content || !activeDeliverable) return;
      const isAr = modalLang === "ar";
      const ext = activeTab === "schema" ? "json" : "md";
      const filename = `${activeDeliverable.code_raw}_${activeTab}_${isAr ? 'ar' : 'en'}.${ext}`;

      const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });

    // Modal Close
    modalCloseBtn.addEventListener("click", closeModal);
    modalBackdrop.addEventListener("click", function (e) {
      if (e.target === modalBackdrop) closeModal();
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && modalBackdrop.style.display !== "none") {
        closeModal();
      }
    });

    // Initial render
    renderGrid();
  });
})();
