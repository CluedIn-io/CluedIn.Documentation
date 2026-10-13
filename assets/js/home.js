/*
 * Home page behaviour.
 *
 * The hero search box is the theme's own search (#search-input and its results
 * list), moved out of the top bar, so it keeps the index, keyboard navigation
 * and result previews. Without this script the search simply stays in the top
 * bar.
 */
(function () {
  function init() {
    var slot = document.getElementById("home-search");
    var search = document.querySelector(".main-header .search");
    var input = document.getElementById("search-input");
    if (!slot || !search || !input) return;

    slot.appendChild(search);
    document.documentElement.classList.add("home-search-moved");

    var mac = /Mac|iPhone|iPad/.test(navigator.platform || navigator.userAgent);
    var hint = document.createElement("kbd");
    hint.className = "home-search-kbd";
    hint.textContent = mac ? "⌘ K" : "Ctrl K";
    search.querySelector(".search-input-wrap").appendChild(hint);

    document.addEventListener("keydown", function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        input.focus();
        input.select();
      }
    });

    document.querySelectorAll(".home-chip").forEach(function (chip) {
      chip.addEventListener("click", function () {
        input.value = chip.getAttribute("data-q");
        input.focus();
        // The theme re-runs the search on keyup; focus alone only shows the
        // results for an input that was already filled in.
        input.dispatchEvent(new KeyboardEvent("keyup", { bubbles: true }));
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
