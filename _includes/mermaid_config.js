{
  /*
    Mermaid initialization options, merged into mermaid.initialize() by the
    just-the-docs theme when `mermaid` is enabled in _config.yml.
    Reference: https://mermaid.js.org/config/schema-docs/config.html

    Colours below follow the CluedIn brand: teal accent #19cca3, dark navy
    #0d2547, white surfaces with light-grey #d1d6dc borders. Using the "base"
    theme so these themeVariables take effect across every diagram on the site;
    individual diagrams can still override per-node styling with classDef.

    securityLevel is set to "loose" so `click` directives in diagrams can link
    to other documentation pages; Mermaid disables links under its default
    "strict" level. Diagrams are authored in-repo, so this is safe here.

    IMPORTANT: use block comments only here, never line comments that start
    with two slashes. This file is inlined into a script tag whose newlines
    are collapsed by HTML compression, so a slash-slash comment would comment
    out the rest of the script (the closing brace and the
    mermaid.initialize/run calls), breaking every diagram on the site with
    "Unexpected end of input".
  */
  "securityLevel": "loose",
  "theme": "base",
  "themeVariables": {
    "fontFamily": "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif",
    "fontSize": "14px",
    "primaryColor": "#ffffff",
    "primaryBorderColor": "#19cca3",
    "primaryTextColor": "#0d2547",
    "secondaryColor": "#f2fbf9",
    "secondaryBorderColor": "#19cca3",
    "secondaryTextColor": "#0d2547",
    "tertiaryColor": "#f5f7fa",
    "tertiaryBorderColor": "#d1d6dc",
    "tertiaryTextColor": "#0d2547",
    "lineColor": "#8a97a8",
    "textColor": "#0d2547",
    "mainBkg": "#ffffff",
    "nodeBorder": "#19cca3",
    "clusterBkg": "#f5f7fa",
    "clusterBorder": "#d1d6dc",
    "titleColor": "#0d2547",
    "edgeLabelBackground": "#ffffff",
    "noteBkgColor": "#f2fbf9",
    "noteBorderColor": "#19cca3"
  },
  "flowchart": {
    "curve": "basis",
    "htmlLabels": true,
    "padding": 12,
    "nodeSpacing": 45,
    "rankSpacing": 55
  }
}
