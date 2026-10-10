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
    jtd.setTheme(theme === "dark" ? "clue-dark" : "default");
    var toggle = document.getElementById("theme-toggle");
    if (toggle) toggle.setAttribute("aria-checked", theme === "dark" ? "true" : "false");
  }

  function init() {
    var toggle = document.getElementById("theme-toggle");
    if (!toggle) return;
    toggle.setAttribute("aria-checked", current() === "dark" ? "true" : "false");
    toggle.addEventListener("click", function () {
      var next = current() === "dark" ? "light" : "dark";
      apply(next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
