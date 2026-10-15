/*
 * Sidebar grouping for the restructured CluedIn documentation.
 *
 * just-the-docs v0.7 renders one flat list of top-level sections. This script
 * makes the information architecture visible in it:
 *
 *   - a Home link at the top;
 *   - a labelled heading in front of the first section of each group — the
 *     data lifecycle, the platform around it, learning material, reference;
 *   - an icon on every top-level section, from the sprite in
 *     _includes/icons/cluedin.html.
 *
 * It is purely presentational — if the script does not run, the navigation
 * still works, it is simply ungrouped and without icons.
 */
(function () {
  var GROUPS = [
    { before: "/ingest", label: "Data lifecycle" },
    { before: "/administer", label: "Platform" },
    { before: "/solutions", label: "Learn" },
    { before: "/troubleshooting", label: "Reference" },
    { before: "/archive", label: "Archive" },
  ];

  var ICONS = {
    "/get-started": "rocket",
    "/ingest": "database",
    "/model": "model",
    "/master": "layers",
    "/govern": "shield",
    "/publish": "share",
    "/administer": "users",
    "/operate": "server",
    "/develop": "code",
    "/solutions": "plug",
    "/learning-paths": "cap",
    "/playbooks": "clipboard",
    "/troubleshooting": "lifebuoy",
    "/release-notes": "file",
    "/archive": "archive",
  };

  // Suffix match, so this works whether the site is served from a domain root
  // or from under a baseurl, with or without a trailing slash.
  function topLink(list, path) {
    return list.querySelector(
      ':scope > li > a[href$="' + path + '"], :scope > li > a[href$="' + path + '/"]'
    );
  }

  function icon(name) {
    var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("class", "ci nav-icon");
    svg.setAttribute("aria-hidden", "true");
    var use = document.createElementNS("http://www.w3.org/2000/svg", "use");
    use.setAttribute("href", "#ci-" + name);
    svg.appendChild(use);
    return svg;
  }

  function enhance() {
    var list = document.querySelector(".site-nav > ul.nav-list");
    if (!list) return;

    Object.keys(ICONS).forEach(function (path) {
      var link = topLink(list, path);
      if (link && !link.querySelector(".nav-icon")) link.prepend(icon(ICONS[path]));
    });

    GROUPS.forEach(function (group) {
      var link = topLink(list, group.before);
      if (!link) return;

      var item = link.closest("li");
      if (!item || item.previousElementSibling?.classList.contains("nav-group-label")) return;

      var label = document.createElement("li");
      label.className = "nav-group-label";
      label.textContent = group.label;
      item.parentNode.insertBefore(label, item);
    });

    if (!list.querySelector(".nav-home")) {
      var home = document.createElement("li");
      home.className = "nav-list-item nav-home";
      var a = document.createElement("a");
      a.className = "nav-list-link";
      a.href = document.querySelector(".site-title")?.getAttribute("href") || "/";
      a.appendChild(icon("home"));
      a.appendChild(document.createTextNode("Home"));
      if (document.querySelector(".home-hero")) a.classList.add("active");
      home.appendChild(a);
      list.prepend(home);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enhance);
  } else {
    enhance();
  }
})();
