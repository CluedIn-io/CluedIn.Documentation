/*
 * Agent mode switch in the top bar.
 *
 * Shows the page the way an AI agent should read it: the Markdown copy that
 * _plugins/agent_markdown.rb writes next to every article, with buttons to
 * copy it or open it. Pages without a copy (the home page) show /llms.txt, the
 * entry point for agents. The article is hidden while Agent mode is on.
 *
 * The data-agent-mode attribute is applied before paint by an inline script in
 * _includes/head_custom.html; this file builds the panel and remembers the
 * reader's choice.
 */
(function () {
  var KEY = "cluedin-docs-agent-mode";
  var panel = null;

  var LINKS = [
    { label: "Set up your AI assistant", href: "/get-started/ai-assistants",
      text: "point Claude, ChatGPT, Copilot or Cursor at this documentation" },
    { label: "REST API reference", href: "/api",
      text: "endpoints by category, with the OpenAPI documents" },
    { label: "CluedIn MCP server",
      href: "/govern/ai-agents/ai-agents-faqs#connecting-cluedin-mcp-to-claude-chatgpt-and-microsoft-copilot",
      text: "connect an assistant to your own CluedIn instance" }
  ];

  function isOn() {
    return document.documentElement.getAttribute("data-agent-mode") === "on";
  }

  function source() {
    var link = document.querySelector('link[rel="alternate"][type="text/markdown"]');
    if (link) return { url: link.href, label: "This page" };
    return { url: new URL("/llms.txt", location.href).href, label: "The documentation index" };
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function flash(button, text) {
    var original = button.textContent;
    button.textContent = text;
    setTimeout(function () { button.textContent = original; }, 1500);
  }

  function copy(button, text) {
    if (!navigator.clipboard) return flash(button, "Copy not available");
    navigator.clipboard.writeText(text).then(
      function () { flash(button, "Copied"); },
      function () { flash(button, "Copy failed"); }
    );
  }

  function build() {
    var host = document.getElementById("main-content");
    if (!host) return null;
    var src = source();
    var llms = new URL("/llms.txt", location.href).href;

    var section = el("section", "agent-panel");
    section.setAttribute("aria-label", "Agent mode");

    // "AI assistant", not "agent": in this documentation "AI agents" is a
    // CluedIn product feature (/govern/ai-agents), and this panel is about the
    // reader's own assistant.
    var intro = el("p", "agent-panel-intro");
    intro.appendChild(document.createTextNode(
      src.label + " as an AI assistant should read it: Markdown, without navigation or markup. " +
      "To point an assistant or an MCP fetch tool at the whole documentation, give it "));
    var llmsLink = el("a", null, llms);
    llmsLink.href = llms;
    intro.appendChild(llmsLink);
    intro.appendChild(document.createTextNode("."));
    section.appendChild(intro);

    var links = el("ul", "agent-panel-links");
    LINKS.forEach(function (item) {
      var li = el("li");
      var a = el("a", null, item.label);
      a.href = new URL(item.href, location.href).href;
      li.appendChild(a);
      li.appendChild(document.createTextNode(" — " + item.text));
      links.appendChild(li);
    });
    section.appendChild(links);

    var actions = el("div", "agent-panel-actions");
    var copyText = el("button", "agent-panel-button agent-panel-button-primary", "Copy Markdown");
    copyText.type = "button";
    copyText.disabled = true;
    var copyUrl = el("button", "agent-panel-button", "Copy URL");
    copyUrl.type = "button";
    copyUrl.addEventListener("click", function () { copy(copyUrl, src.url); });
    var open = el("a", "agent-panel-button", "Open raw");
    open.href = src.url;
    actions.appendChild(copyText);
    actions.appendChild(copyUrl);
    actions.appendChild(open);
    section.appendChild(actions);

    var pre = el("pre", "agent-panel-source");
    var code = el("code", null, "Loading " + src.url + " ...");
    pre.appendChild(code);
    section.appendChild(pre);

    fetch(src.url)
      .then(function (res) {
        if (!res.ok) throw new Error(res.status + " " + res.statusText);
        return res.text();
      })
      .then(function (text) {
        code.textContent = text;
        copyText.disabled = false;
        copyText.addEventListener("click", function () { copy(copyText, text); });
      })
      .catch(function (err) {
        code.textContent = "Could not load " + src.url + " (" + err.message + ").";
      });

    host.insertBefore(section, host.firstChild);
    return section;
  }

  function sync() {
    var on = isOn();
    if (on && !panel) panel = build();
    var toggles = document.querySelectorAll(".agent-toggle");
    for (var i = 0; i < toggles.length; i++) {
      toggles[i].setAttribute("aria-pressed", on ? "true" : "false");
    }
  }

  function init() {
    var toggle = document.getElementById("agent-toggle");
    if (toggle) {
      toggle.addEventListener("click", function () {
        var next = isOn() ? "off" : "on";
        if (next === "on") {
          document.documentElement.setAttribute("data-agent-mode", "on");
        } else {
          document.documentElement.removeAttribute("data-agent-mode");
        }
        try { localStorage.setItem(KEY, next); } catch (e) {}
        sync();
      });
    }
    sync();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
