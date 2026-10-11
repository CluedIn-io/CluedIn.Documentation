/*
 * Light / dark switch in the top bar.
 *
 * The initial scheme is applied by an inline script in _includes/head_custom.html
 * so the page does not flash; this file only wires up the toggle and remembers
 * the reader's choice.
 */
(function () {
  var KEY = "cluedin-docs-theme";

  function current() {
    return document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
  }

  function apply(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    // "default" is just-the-docs-default.css, compiled from the `clue` scheme.
    window.ciSetScheme(theme === "dark" ? "clue-dark" : "default");
    sync();
  }

  function sync() {
    var toggles = document.querySelectorAll(".theme-toggle");
    for (var i = 0; i < toggles.length; i++) {
      toggles[i].setAttribute("aria-checked", current() === "dark" ? "true" : "false");
    }
  }

  function wire(toggle) {
    toggle.addEventListener("click", function () {
      var next = current() === "dark" ? "light" : "dark";
      apply(next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
    });
  }

  function init() {
    var toggle = document.getElementById("theme-toggle");
    if (!toggle) return;
    wire(toggle);

    // On narrow screens the top bar is folded into the menu, so the CSS shows
    // this copy beside the menu button instead.
    var menuButton = document.getElementById("menu-button");
    if (menuButton) {
      var copy = toggle.cloneNode(true);
      copy.removeAttribute("id");
      menuButton.parentNode.insertBefore(copy, menuButton);
      wire(copy);
    }
    sync();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
