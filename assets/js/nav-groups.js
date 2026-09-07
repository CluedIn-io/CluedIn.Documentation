/*
 * Sidebar grouping for the restructured CluedIn documentation.
 *
 * The information architecture has two tiers: eight lifecycle areas that
 * answer "what am I trying to do with my data", and supporting material that
 * sits outside that workflow. just-the-docs v0.7 renders one flat list of
 * top-level sections, so this script inserts a labelled separator in front of
 * the first item of each later tier. It is purely presentational — if the
 * script does not run, the navigation still works, it is simply ungrouped.
 */
(function () {
  var GROUPS = [
    { before: "/solutions", label: "Resources" },
    { before: "/archive", label: "Archive" },
  ];

  function insertLabels() {
    var list = document.querySelector(".site-nav > ul.nav-list");
    if (!list) return;

    GROUPS.forEach(function (group) {
      // Suffix match, so the separators land in the right place whether the
      // site is served from a domain root or from under a baseurl.
      var link = list.querySelector(
        ':scope > li > a[href$="' + group.before + '"], :scope > li > a[href$="' + group.before + '/"]'
      );
      if (!link) return;

      var item = link.closest("li");
      if (!item || item.previousElementSibling?.classList.contains("nav-group-label")) return;

      var label = document.createElement("li");
      label.className = "nav-group-label";
      label.textContent = group.label;
      item.parentNode.insertBefore(label, item);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", insertLabels);
  } else {
    insertLabels();
  }
})();
