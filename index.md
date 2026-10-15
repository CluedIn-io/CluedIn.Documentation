---
layout: default
title: Home
nav_exclude: true
search_exclude: true
description: "Documentation, guides and resources to help you ingest, master, govern and publish your data with CluedIn."
permalink: /

# The six lifecycle cards. Each links to a section index.
lifecycle:
  - { title: "Get started", url: "/get-started", icon: rocket, text: "Learn the basics and get up and running quickly." }
  - { title: "Ingest", url: "/ingest", icon: database, text: "Connect to your data from any source." }
  - { title: "Model", url: "/model", icon: model, text: "Design and manage your data model." }
  - { title: "Master", url: "/master", icon: layers, text: "Match, merge and create golden records at scale." }
  - { title: "Govern & improve", url: "/govern", icon: shield, text: "Ensure data quality, lineage and compliance." }
  - { title: "Publish & consume", url: "/publish", icon: share, text: "Deliver trusted data to your business ecosystem." }

# Hand-picked; every url must be a live permalink (validate.py checks links).
guides:
  - { title: "Ingest your first dataset", url: "/ingest/tutorial-ingest-data", icon: database, text: "Connect a data source and run your first ingestion." }
  - { title: "Create a deduplication project", url: "/master/deduplication/create-a-deduplication-project", icon: layers, text: "Identify and merge duplicate records." }
  - { title: "Build an AI agent", url: "/govern/ai-agents/create-configure-and-run-an-ai-agent", icon: sparkles, text: "Automate data management with AI agents." }
  - { title: "Publish to Microsoft Fabric", url: "/solutions/fabric/connect-cluedin-to-fabric", icon: lake, text: "Write trusted data to OneLake and Fabric." }
  - { title: "REST API quickstart", url: "/api/get-started", icon: code, text: "Authenticate and make your first API request." }

popular_searches: [ "ingestion", "deduplication", "Microsoft Fabric", "API", "AI agents" ]
---

{%- assign releases = site.pages | where: "parent", "Release notes" | where_exp: "p", "p.title contains 'Release '" | sort: "nav_order" -%}

<div class="home">

<section class="home-hero">
  <div class="home-hero-text">
    <p class="home-eyebrow">Cleaner data. Brighter possibilities.</p>
    <h1 class="home-title">Build trusted data with CluedIn</h1>
    <p class="home-lead">Documentation, guides and resources to help you ingest, master, govern and publish your data with CluedIn.</p>

    <div class="home-search" id="home-search" data-shortcut-hint="true"></div>

    <div class="home-chips">
      <span class="home-chips-label">Popular searches:</span>
      {%- for q in page.popular_searches %}
      <button type="button" class="home-chip" data-q="{{ q }}">{{ q }}</button>
      {%- endfor %}
    </div>
  </div>

  <div class="home-flow" aria-hidden="true">
    <svg class="home-flow-lines" viewBox="0 0 520 340" preserveAspectRatio="xMidYMid meet">
      <defs>
        <radialGradient id="home-flow-glow">
          <stop offset="0" stop-color="currentColor" stop-opacity="0.22"/>
          <stop offset="1" stop-color="currentColor" stop-opacity="0"/>
        </radialGradient>
      </defs>
      <circle cx="250" cy="172" r="110" fill="url(#home-flow-glow)"/>
      <g class="home-flow-in">
        <path d="M122 112 C 165 112, 170 160, 208 168"/>
        <path d="M122 172 C 160 172, 175 172, 208 172"/>
        <path d="M122 232 C 165 232, 170 184, 208 176"/>
      </g>
      <g class="home-flow-out">
        <path d="M292 168 C 330 150, 330 72, 370 72"/>
        <path d="M292 170 C 335 160, 335 134, 370 134"/>
        <path d="M292 174 C 335 184, 335 196, 370 196"/>
        <path d="M292 176 C 330 196, 330 258, 370 258"/>
      </g>
      <path class="home-flow-arrow" d="M120 46 C 150 40, 170 52, 180 74 M172 68 l8 6 2-10"/>
      <path class="home-flow-arrow" d="M376 316 C 362 312, 356 302, 358 290 M352 297 l6-7 6 6"/>
    </svg>

    <p class="home-flow-note home-flow-note-top">From silos to a<br>smarter tomorrow</p>

    <span class="home-flow-tile" style="left:3.1%;top:26.5%;color:#1d7a46"><svg class="ci"><use href="#ci-sheet"></use></svg></span>
    <span class="home-flow-tile" style="left:14.6%;top:26.5%;color:#1f8ad6"><svg class="ci"><use href="#ci-cloud"></use></svg></span>
    <span class="home-flow-tile" style="left:3.1%;top:44.1%;color:#1d5fb4"><svg class="ci"><use href="#ci-box"></use></svg></span>
    <span class="home-flow-tile" style="left:14.6%;top:44.1%;color:#23a8d8"><svg class="ci"><use href="#ci-users"></use></svg></span>
    <span class="home-flow-tile" style="left:3.1%;top:61.8%;color:#1f4fa8"><svg class="ci"><use href="#ci-database"></use></svg></span>
    <span class="home-flow-tile" style="left:14.6%;top:61.8%;color:#4b5563"><svg class="ci"><use href="#ci-file"></use></svg></span>

    <span class="home-flow-hub">{% include cluedin-mark.html %}</span>
    <span class="home-flow-badge">Trusted data<br>for what's next</span>

    <span class="home-flow-dest" style="top:14.7%"><svg class="ci" style="color:#1b9a7a"><use href="#ci-lake"></use></svg>Microsoft Fabric</span>
    <span class="home-flow-dest" style="top:32.9%"><svg class="ci" style="color:#d4a017"><use href="#ci-chart"></use></svg>Power BI</span>
    <span class="home-flow-dest" style="top:51.2%"><svg class="ci" style="color:#e2492f"><use href="#ci-layers"></use></svg>Databricks</span>
    <span class="home-flow-dest" style="top:69.4%"><svg class="ci"><use href="#ci-grid"></use></svg>Your applications</span>

    <p class="home-flow-note home-flow-note-bottom">Connect · Clean · Enrich<br>Unify · Activate</p>
  </div>
</section>

<nav class="home-cards" aria-label="The data lifecycle">
  {%- for card in page.lifecycle %}
  <a class="home-card" href="{{ card.url | relative_url }}">
    <svg class="ci home-card-icon"><use href="#ci-{{ card.icon }}"></use></svg>
    <span class="home-card-title">{{ card.title }}</span>
    <span class="home-card-text">{{ card.text }}</span>
    <span class="home-card-go"><svg class="ci"><use href="#ci-arrow-right"></use></svg></span>
  </a>
  {%- endfor %}
</nav>

<div class="home-panels">
  <section class="home-panel" aria-labelledby="home-guides-title">
    <div class="home-panel-head">
      <h2 class="home-panel-title" id="home-guides-title">Popular guides</h2>
      <a class="home-panel-more" href="{{ '/learning-paths' | relative_url }}">View all learning paths <svg class="ci"><use href="#ci-arrow-right"></use></svg></a>
    </div>
    <ul class="home-guides">
      {%- for guide in page.guides %}
      <li>
        <a class="home-guide" href="{{ guide.url | relative_url }}">
          <svg class="ci home-guide-icon"><use href="#ci-{{ guide.icon }}"></use></svg>
          <span class="home-guide-text">
            <span class="home-guide-title">{{ guide.title }}</span>
            <span class="home-guide-desc">{{ guide.text }}</span>
          </span>
          <svg class="ci home-guide-go"><use href="#ci-chevron-right"></use></svg>
        </a>
      </li>
      {%- endfor %}
    </ul>
  </section>

  <section class="home-panel" aria-labelledby="home-new-title">
    <div class="home-panel-head">
      <h2 class="home-panel-title" id="home-new-title">What's new</h2>
      <a class="home-panel-more" href="{{ '/release-notes' | relative_url }}">View release notes <svg class="ci"><use href="#ci-arrow-right"></use></svg></a>
    </div>
    <ul class="home-releases">
      {%- for r in releases limit: 4 %}
      <li class="home-release{% if forloop.first %} is-latest{% endif %}">
        <a href="{{ r.url | relative_url }}">{{ r.title | remove_first: "Release " }}</a>
        <span>{{ r.summary }}</span>
      </li>
      {%- endfor %}
    </ul>
    {%- assign latest = releases | first %}
    {%- if latest %}
    <a class="home-callout" href="{{ latest.url | relative_url }}">
      <svg class="ci"><use href="#ci-bell"></use></svg>
      <span>
        <strong>Read the latest release</strong>
        <span>See everything that changed in {{ latest.title | remove_first: "Release " }}.</span>
      </span>
      <svg class="ci home-guide-go"><use href="#ci-chevron-right"></use></svg>
    </a>
    {%- endif %}
  </section>
</div>

<p class="home-help">
  <span>Need help? Start with <a href="{{ '/troubleshooting' | relative_url }}">troubleshooting</a> or <a href="mailto:{{ site.email }}">contact support</a>.</span>
  <span class="home-help-tagline">Better data for a brighter tomorrow.</span>
</p>

</div>

<script src="{{ '/assets/js/home.js' | relative_url }}" defer></script>

<!-- Start of HubSpot Embed Code -->
<script type="text/javascript" id="hs-script-loader" async defer src="//js.hs-scripts.com/2770606.js"></script>
<!-- End of HubSpot Embed Code -->
