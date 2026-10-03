/**
 * Tasleemat Interactive Deliverables Explorer & Filter Engine
 * Client-side real-time filtering, phase tabs, tier selectors, and view switching.
 */
document.addEventListener("DOMContentLoaded", function () {
  const explorerContainer = document.getElementById("tasleemat-explorer");
  if (!explorerContainer) return;

  const searchInput = document.getElementById("explorer-search");
  const phaseButtons = document.querySelectorAll(".filter-phase-btn");
  const tierButtons = document.querySelectorAll(".filter-tier-btn");
  const viewButtons = document.querySelectorAll(".view-toggle-btn");
  const cardsContainer = document.getElementById("explorer-cards");
  const tableContainer = document.getElementById("explorer-table");
  const countDisplay = document.getElementById("results-count");

  let activePhase = "all";
  let activeTier = "all";
  let searchQuery = "";
  let currentView = "cards"; // 'cards' or 'table'

  function filterItems() {
    let visibleCount = 0;
    const cards = document.querySelectorAll(".explorer-card-item");
    const rows = document.querySelectorAll(".explorer-table-row");

    cards.forEach((card, index) => {
      const phase = card.getAttribute("data-phase") || "";
      const tier = card.getAttribute("data-tier") || "";
      const searchData = (card.getAttribute("data-search") || "").toLowerCase();

      const matchesPhase = activePhase === "all" || phase === activePhase;
      const matchesTier = activeTier === "all" || tier.includes(activeTier);
      const matchesSearch = !searchQuery || searchData.includes(searchQuery);

      const isVisible = matchesPhase && matchesTier && matchesSearch;

      if (isVisible) {
        card.style.display = "flex";
        if (rows[index]) rows[index].style.display = "";
        visibleCount++;
      } else {
        card.style.display = "none";
        if (rows[index]) rows[index].style.display = "none";
      }
    });

    if (countDisplay) {
      countDisplay.textContent = visibleCount;
    }
  }

  if (searchInput) {
    searchInput.addEventListener("input", function (e) {
      searchQuery = e.target.value.toLowerCase().trim();
      filterItems();
    });
  }

  phaseButtons.forEach((btn) => {
    btn.addEventListener("click", function () {
      phaseButtons.forEach((b) => b.classList.remove("active"));
      this.classList.add("active");
      activePhase = this.getAttribute("data-phase");
      filterItems();
    });
  });

  tierButtons.forEach((btn) => {
    btn.addEventListener("click", function () {
      tierButtons.forEach((b) => b.classList.remove("active"));
      this.classList.add("active");
      activeTier = this.getAttribute("data-tier");
      filterItems();
    });
  });

  viewButtons.forEach((btn) => {
    btn.addEventListener("click", function () {
      viewButtons.forEach((b) => b.classList.remove("active"));
      this.classList.add("active");
      currentView = this.getAttribute("data-view");

      if (currentView === "cards") {
        if (cardsContainer) cardsContainer.style.display = "grid";
        if (tableContainer) tableContainer.style.display = "none";
      } else {
        if (cardsContainer) cardsContainer.style.display = "none";
        if (tableContainer) tableContainer.style.display = "block";
      }
    });
  });
});
