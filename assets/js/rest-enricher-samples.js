/*
 * Interactive parts of the REST API enricher samples section
 * (/govern/rest-api-enricher-samples). Loaded only on those pages.
 *
 * 1. Index page: a search box and an API key filter for the
 *    "Company registry lookups" table.
 * 2. Sample pages: a "Customize the script" panel above the process script.
 *    It lists the settings constants at the top of the script (vocabulary
 *    keys, URLs, cache duration) and updates the script, and the
 *    "Vocabulary and Properties" block, as you type, so the copy button
 *    copies a script that is ready to paste into the enricher.
 *
 * Everything is progressive enhancement: without JavaScript (and in the
 * Markdown copy for AI agents) the pages are unchanged.
 */
(function () {
  "use strict";

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (name) {
      if (name === "text") {
        node.textContent = attrs[name];
      } else {
        node.setAttribute(name, attrs[name]);
      }
    });
    (children || []).forEach(function (child) {
      node.appendChild(typeof child === "string" ? document.createTextNode(child) : child);
    });
    return node;
  }

  // The first element after `heading` (in document order, not only siblings)
  // that matches `selector`, stopping at the next h2.
  function nextAfterHeading(heading, selector) {
    var node = heading.nextElementSibling;
    while (node && node.tagName !== "H2") {
      if (node.matches(selector)) {
        return node;
      }
      var inner = node.querySelector(selector);
      if (inner) {
        return inner;
      }
      node = node.nextElementSibling;
    }
    return null;
  }

  // ---- 1. Registry table filter ------------------------------------------------

  function setUpRegistryFilter() {
    var heading = document.getElementById("company-registry-lookups");
    var table = heading && nextAfterHeading(heading, "table");
    if (!table || !table.tBodies.length) {
      return;
    }

    var rows = Array.prototype.slice.call(table.tBodies[0].rows);
    var keyColumn = -1;
    Array.prototype.forEach.call(table.tHead ? table.tHead.rows[0].cells : [], function (cell, i) {
      if (/api key/i.test(cell.textContent)) {
        keyColumn = i;
      }
    });

    var search = el("input", {
      type: "search",
      id: "registry-filter-search",
      class: "ci-sample-input",
      placeholder: "Country, register or identifier",
      autocomplete: "off",
    });
    var keySelect = el("select", { id: "registry-filter-key", class: "ci-sample-input" }, [
      el("option", { value: "any", text: "Any" }),
      el("option", { value: "none", text: "No key needed" }),
      el("option", { value: "needed", text: "Key needed" }),
    ]);
    var status = el("p", { class: "ci-sample-status", "aria-live": "polite" });
    var empty = el("tr", { class: "ci-sample-empty", hidden: "" }, [
      el("td", { colspan: String(table.tBodies[0].rows[0].cells.length), text: "No registry matches. Clear the filter to see them all." }),
    ]);
    table.tBodies[0].appendChild(empty);

    var controls = el("div", { class: "ci-sample-controls", role: "search", "aria-label": "Filter company registries" }, [
      el("div", { class: "ci-sample-field" }, [el("label", { for: "registry-filter-search", text: "Filter" }), search]),
      el("div", { class: "ci-sample-field" }, [el("label", { for: "registry-filter-key", text: "API key" }), keySelect]),
    ]);
    table.parentNode.insertBefore(controls, table);
    table.parentNode.insertBefore(status, table);

    function needsKey(row) {
      var text = keyColumn >= 0 ? row.cells[keyColumn].textContent.toLowerCase() : "";
      return !(/not needed|optional/.test(text));
    }

    function apply() {
      var words = search.value.toLowerCase().split(/\s+/).filter(Boolean);
      var key = keySelect.value;
      var shown = 0;
      rows.forEach(function (row) {
        var text = row.textContent.toLowerCase();
        var match = words.every(function (word) { return text.indexOf(word) >= 0; }) &&
          (key === "any" || (key === "needed") === needsKey(row));
        row.hidden = !match;
        if (match) {
          shown++;
        }
      });
      empty.hidden = shown > 0;
      status.textContent = shown === rows.length
        ? rows.length + " registries"
        : "Showing " + shown + " of " + rows.length + " registries";
    }

    search.addEventListener("input", apply);
    keySelect.addEventListener("change", apply);
    apply();
  }

  // ---- 2. Script configurator -----------------------------------------------------

  var HOUR = 60 * 60 * 1000;

  // Reads `const NAME = value;` lines from the settings part of the script
  // (everything before the "---- Script" divider), with the comment lines
  // just above each one as its description.
  function readSettings(script) {
    var settingsPart = script.split(/^\/\/ -+ Script/m)[0];
    var lines = settingsPart.split("\n");
    var settings = [];
    var comments = [];
    lines.forEach(function (line) {
      var comment = /^\/\/\s?(.*)$/.exec(line);
      if (comment) {
        if (!/^-+ Settings/.test(comment[1])) {
          comments.push(comment[1]);
        }
        return;
      }
      var match = /^const ([A-Z0-9_]+) = (.+);\s*$/.exec(line);
      if (match) {
        var name = match[1];
        var value = match[2];
        var setting = { name: name, description: comments.join(" "), raw: value };
        var text = /^"((?:[^"\\]|\\.)*)"$/.exec(value);
        if (text && text[1].indexOf("{APIKey}") >= 0) {
          setting.kind = "apiKey";
        } else if (text) {
          setting.kind = "text";
          setting.value = JSON.parse(value);
        } else if (/_MILLISECONDS$/.test(name) && /^[\d\s*+]+$/.test(value)) {
          setting.kind = "duration";
          // Only digits, spaces, * and + reach here.
          setting.value = value.split("+").reduce(function (sum, term) {
            return sum + term.split("*").reduce(function (product, factor) { return product * Number(factor.trim()); }, 1);
          }, 0);
        }
        if (setting.kind) {
          settings.push(setting);
        }
      }
      if (line.trim() !== "" || !match) {
        comments = [];
      }
    });
    return settings;
  }

  // The Rouge-highlighted tokens of `const NAME = ... ;` inside `code`.
  function valueTokens(code, name) {
    var spans = code.querySelectorAll("span.nx, span.nc, span.no");
    for (var i = 0; i < spans.length; i++) {
      if (spans[i].textContent !== name) {
        continue;
      }
      var prev = spans[i].previousElementSibling;
      if (!prev || prev.textContent !== "const") {
        continue;
      }
      var tokens = [];
      var node = spans[i].nextSibling;
      var afterEquals = false;
      while (node) {
        if (node.nodeType === 1 && node.textContent === ";") {
          break;
        }
        if (afterEquals) {
          tokens.push(node);
        } else if (node.nodeType === 1 && node.textContent === "=") {
          afterEquals = true;
        }
        node = node.nextSibling;
      }
      // Drop the space right after "=".
      if (tokens.length && tokens[0].nodeType === 3 && tokens[0].textContent.trim() === "") {
        tokens.shift();
      }
      return { tokens: tokens, end: node };
    }
    return null;
  }

  function replaceValue(code, name, kind, newValue) {
    var found = valueTokens(code, name);
    if (!found || !found.end) {
      return;
    }
    if (kind === "text") {
      // "..." is <span class="dl">"</span><span class="s2">value</span><span class="dl">"</span>;
      // an empty string has no s2 span.
      var stringSpan = null;
      found.tokens.forEach(function (token) {
        if (token.nodeType === 1 && /^s/.test(token.className) && token.className !== "dl") {
          stringSpan = token;
        }
      });
      var escaped = JSON.stringify(newValue).slice(1, -1);
      if (stringSpan) {
        stringSpan.textContent = escaped;
        return;
      }
    }
    var replacement = kind === "duration"
      ? el("span", { class: "mi", text: newValue })
      : el("span", { class: "s2", text: JSON.stringify(newValue) });
    found.tokens.forEach(function (token) { token.parentNode.removeChild(token); });
    found.end.parentNode.insertBefore(replacement, found.end);
  }

  function durationExpression(hours) {
    if (hours <= 0) {
      return "0";
    }
    if (hours >= 48 && hours % 24 === 0) {
      return (hours / 24) + " * 24 * 60 * 60 * 1000";
    }
    return hours + " * 60 * 60 * 1000";
  }

  function label(setting) {
    if (/_KEY$/.test(setting.name)) {
      return "Vocabulary key (" + setting.name + ")";
    }
    if (/_URL$/.test(setting.name)) {
      return "URL (" + setting.name + ")";
    }
    if (setting.kind === "duration") {
      return "Cache answers for, in hours (" + setting.name + ")";
    }
    return setting.name;
  }

  function setUpConfigurator() {
    var heading = document.getElementById("process-script");
    var block = heading && nextAfterHeading(heading, "div.language-javascript");
    var code = block && block.querySelector("code");
    if (!code) {
      return;
    }
    var settings = readSettings(code.textContent);
    var editable = settings.filter(function (s) { return s.kind !== "apiKey"; });
    if (!editable.length) {
      return;
    }

    // The "Vocabulary and Properties" field contents, kept in step with the *_KEY settings.
    var vocabHeading = document.getElementById("vocabulary-and-properties");
    var vocabCode = vocabHeading && nextAfterHeading(vocabHeading, "pre code");

    var fields = [];
    var form = el("div", { class: "ci-sample-config-fields" });
    editable.forEach(function (setting, i) {
      var id = "script-setting-" + i;
      var input = setting.kind === "duration"
        ? el("input", { id: id, type: "number", min: "0", step: "1", class: "ci-sample-input", value: String(setting.value / HOUR) })
        : el("input", { id: id, type: "text", class: "ci-sample-input", spellcheck: "false", value: setting.value });
      var field = el("div", { class: "ci-sample-field" }, [el("label", { for: id, text: label(setting) }), input]);
      if (setting.description) {
        field.appendChild(el("p", { class: "ci-sample-hint", text: setting.description }));
      }
      form.appendChild(field);
      fields.push({ setting: setting, input: input, current: setting.value });
    });

    var apiKeySetting = settings.filter(function (s) { return s.kind === "apiKey"; })[0];
    var notes = el("p", { class: "ci-sample-hint" }, [
      "Changes update the script below and, for vocabulary keys, the Vocabulary and Properties field. Use the copy button on the script to copy it.",
    ]);
    if (apiKeySetting) {
      notes.appendChild(document.createTextNode(" " + apiKeySetting.name +
        " stays as {APIKey}: the enricher replaces it with the API Key field, so don't paste your key into the script."));
    }

    var reset = el("button", { type: "button", class: "btn ci-sample-button", text: "Reset" });
    var download = el("button", { type: "button", class: "btn ci-sample-button", text: "Download script" });

    var panel = el("details", { class: "ci-sample-config" }, [
      el("summary", { text: "Customize the script" }),
      notes,
      form,
      el("div", { class: "ci-sample-actions" }, [download, reset]),
    ]);
    block.parentNode.insertBefore(panel, block);

    function update(field) {
      var setting = field.setting;
      var value;
      if (setting.kind === "duration") {
        var hours = Math.max(0, Math.round(Number(field.input.value) || 0));
        value = hours * HOUR;
        // Back at the published value: restore its exact expression.
        replaceValue(code, setting.name, "duration", value === setting.value ? setting.raw : durationExpression(hours));
      } else {
        value = field.input.value.trim();
        replaceValue(code, setting.name, "text", value);
        if (vocabCode && /_KEY$/.test(setting.name)) {
          var lines = vocabCode.textContent.split("\n");
          var index = lines.indexOf(field.current);
          if (index >= 0) {
            lines[index] = value;
            vocabCode.textContent = lines.join("\n");
          }
        }
      }
      field.current = value;
      block.classList.toggle("ci-sample-customized", fields.some(function (f) { return f.current !== f.setting.value; }));
    }

    fields.forEach(function (field) {
      field.input.addEventListener("input", function () { update(field); });
    });

    reset.addEventListener("click", function () {
      fields.forEach(function (field) {
        field.input.value = field.setting.kind === "duration" ? String(field.setting.value / HOUR) : field.setting.value;
        update(field);
      });
    });

    download.addEventListener("click", function () {
      var match = /\/rest-api-enricher-samples\/([^/.?#]+)/.exec(window.location.pathname);
      var name = (match ? match[1] : "rest-api-enricher") + "-process-script.js";
      var url = URL.createObjectURL(new Blob([code.textContent], { type: "text/javascript" }));
      var link = el("a", { href: url, download: name });
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    });
  }

  function init() {
    setUpRegistryFilter();
    setUpConfigurator();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
