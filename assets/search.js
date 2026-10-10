/**
 * Tasleemat Global Executive Search Modal & Instant Search Engine
 */

(function () {
  let searchModal = null;
  let searchInput = null;
  let searchResults = null;

  function initSearchModal() {
    if (document.getElementById("tasleemat-search-modal")) return;

    const modalHtml = `
      <div id="tasleemat-search-modal" class="tasleemat-modal-backdrop hidden" style="position: fixed; inset: 0; background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(4px); z-index: 9999; display: flex; align-items: flex-start; justify-content: center; padding-top: 5rem;">
        <div class="tasleemat-modal-content" style="background: var(--bg-card, #ffffff); color: var(--text-primary, #0f172a); border: 1px solid var(--border-color, #e2e8f0); border-radius: 12px; width: 100%; max-width: 640px; margin: 0 1rem; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2); overflow: hidden;">
          <div style="display: flex; align-items: center; padding: 1rem; border-bottom: 1px solid var(--border-color, #e2e8f0);">
            <span style="font-size: 1.25rem; margin-right: 0.75rem;">🔍</span>
            <input id="tasleemat-search-input" type="text" placeholder="Search 102 deliverables, PMO manuals, codes (e.g. Risk, 04_08_02, EVA)..." style="width: 100%; background: transparent; border: none; outline: none; font-size: 1rem; color: var(--text-primary, #0f172a);" />
            <button id="tasleemat-search-close" style="background: transparent; border: none; cursor: pointer; font-size: 1.25rem; color: var(--text-muted, #64748b); padding: 0.25rem 0.5rem;">✕</button>
          </div>
          <div id="tasleemat-search-results" style="max-height: 400px; overflow-y: auto; padding: 0.5rem;">
            <div style="padding: 1.5rem; text-align: center; color: var(--text-muted, #64748b); font-size: 0.875rem;">Type to start searching deliverables, guides, and templates...</div>
          </div>
          <div style="padding: 0.75rem 1rem; background: var(--bg-dark, #f8fafc); border-top: 1px solid var(--border-color, #e2e8f0); display: flex; justify-content: space-between; font-size: 0.75rem; color: var(--text-muted, #64748b);">
            <span>Press <kbd style="background: var(--bg-card, #ffffff); border: 1px solid var(--border-color, #cbd5e1); border-radius: 4px; padding: 1px 5px;">ESC</kbd> to close</span>
            <span>⚡ Tasleemat Engine</span>
          </div>
        </div>
      </div>
    `;

    document.body.insertAdjacentHTML("beforeend", modalHtml);
    searchModal = document.getElementById("tasleemat-search-modal");
    searchInput = document.getElementById("tasleemat-search-input");
    searchResults = document.getElementById("tasleemat-search-results");

    document.getElementById("tasleemat-search-close").addEventListener("click", hideSearch);
    searchModal.addEventListener("click", function (e) {
      if (e.target === searchModal) hideSearch();
    });

    searchInput.addEventListener("input", handleSearchQuery);

    document.addEventListener("keydown", function (e) {
      if ((e.key === "k" && (e.metaKey || e.ctrlKey)) || (e.key === "/" && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "TEXTAREA")) {
        e.preventDefault();
        showSearch();
      } else if (e.key === "Escape" && searchModal && !searchModal.classList.contains("hidden")) {
        hideSearch();
      }
    });
  }

  function showSearch() {
    initSearchModal();
    if (searchModal) {
      searchModal.classList.remove("hidden");
      searchModal.style.display = "flex";
      setTimeout(() => searchInput.focus(), 50);
    }
  }

  function hideSearch() {
    if (searchModal) {
      searchModal.classList.add("hidden");
      searchModal.style.display = "none";
    }
  }

  function handleSearchQuery() {
    const q = searchInput.value.trim().toLowerCase();
    if (!q) {
      searchResults.innerHTML = `<div style="padding: 1.5rem; text-align: center; color: var(--text-muted, #64748b); font-size: 0.875rem;">Type to start searching deliverables, guides, and templates...</div>`;
      return;
    }

    const isArabicPage = document.documentElement.getAttribute("dir") === "rtl" || window.location.pathname.includes("/ar/") || window.location.pathname.includes("README_AR");
    const data = window.TASLEEMAT_DATA || [];
    const matches = data.filter(d => {
      const text = `${d.code} ${d.name_en} ${d.name_ar} ${d.phase_name_en} ${d.phase_name_ar} ${d.tier}`.toLowerCase();
      return text.includes(q);
    }).slice(0, 15);

    if (matches.length === 0) {
      searchResults.innerHTML = `<div style="padding: 1.5rem; text-align: center; color: var(--text-muted, #64748b); font-size: 0.875rem;">No deliverables found matching "${q}"</div>`;
      return;
    }

    let relRoot = getRelRootPath();

    searchResults.innerHTML = matches.map(d => {
      const name = isArabicPage ? (d.name_ar || d.name_en) : d.name_en;
      const phase = isArabicPage ? d.phase_name_ar : d.phase_name_en;
      const tplUrl = relRoot + d.url_tpl_en;
      const guideUrl = relRoot + d.url_guide_en;
      const exUrl = relRoot + d.url_ex_en;

      return `
        <div style="padding: 0.75rem 1rem; border-bottom: 1px solid var(--border-color, #e2e8f0); display: flex; flex-direction: column; gap: 0.25rem;">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <div style="font-weight: 600; font-size: 0.95rem; color: var(--color-primary-light, #2563eb);">
              <span style="background: var(--bg-dark, #f1f5f9); border: 1px solid var(--border-color, #cbd5e1); border-radius: 4px; padding: 2px 6px; font-size: 0.75rem; font-family: monospace; color: var(--text-primary, #0f172a); margin-right: 0.5rem;">${d.code}</span>
              ${name}
            </div>
            <span style="font-size: 0.75rem; color: var(--text-muted, #64748b);">${phase}</span>
          </div>
          <div style="display: flex; gap: 0.5rem; margin-top: 0.25rem;">
            <a href="${tplUrl}" style="font-size: 0.75rem; color: var(--color-primary-light, #2563eb); background: rgba(37, 99, 235, 0.08); padding: 2px 8px; border-radius: 4px; text-decoration: none;">📝 Template</a>
            <a href="${guideUrl}" style="font-size: 0.75rem; color: var(--color-accent, #0284c7); background: rgba(2, 132, 199, 0.08); padding: 2px 8px; border-radius: 4px; text-decoration: none;">📖 Guide</a>
            <a href="${exUrl}" style="font-size: 0.75rem; color: var(--color-success, #059669); background: rgba(5, 150, 105, 0.08); padding: 2px 8px; border-radius: 4px; text-decoration: none;">💡 Example</a>
          </div>
        </div>
      `;
    }).join("");
  }

  function getRelRootPath() {
    const depth = (window.location.pathname.split("/").length - 2);
    if (window.location.pathname.includes("/forms/") || window.location.pathname.includes("/guides/") || window.location.pathname.includes("/examples/") || window.location.pathname.includes("/catalog/")) {
      const parts = window.location.pathname.split("/").filter(p => p);
      let up = "";
      for (let i = 0; i < parts.length - 1; i++) {
        if (parts[i] === "site" || parts[i] === "Tasleemat") continue;
        up += "../";
      }
      return up || "./";
    }
    return "./";
  }

  // Attach search triggers on DOM ready
  document.addEventListener("DOMContentLoaded", function () {
    const searchBtns = document.querySelectorAll(".tasleemat-search-btn, #search-trigger");
    searchBtns.forEach(btn => btn.addEventListener("click", showSearch));
  });

  window.TasleematSearch = { show: showSearch, hide: hideSearch };
})();
