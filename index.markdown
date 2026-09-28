---
layout: page
title:
nav_order: 0
description: "Find your way around CluedIn: guides, concepts, integrations, and API reference."
permalink: /
---

<section class="docs-hero" aria-labelledby="docs-hero-title">
  <div class="docs-hero-content">
    <div class="docs-eyebrow"><span></span> CLUEDIN DOCUMENTATION</div>
    <h1 id="docs-hero-title">Make your data<br><em>work better.</em></h1>
    <p>Everything you need to connect, clean, govern, and deliver trusted data with CluedIn.</p>
    <div class="docs-hero-actions">
      <a class="docs-primary-action" href="{{ '/getting-started' | relative_url }}">Start building <span aria-hidden="true">↗</span></a>
      {% if site.baseurl == '' %}
      <a class="docs-secondary-action" href="{{ '/quick-feature-tour' | relative_url }}">Take a quick tour <span aria-hidden="true">→</span></a>
      {% else %}
      <a class="docs-secondary-action" href="{{ '/key-terms-and-features' | relative_url }}">Browse key concepts <span aria-hidden="true">→</span></a>
      {% endif %}
    </div>
  </div>
  <div class="docs-hero-art" aria-hidden="true">
    <div class="docs-orbit docs-orbit-one"></div><div class="docs-orbit docs-orbit-two"></div>
    <div class="docs-art-card docs-art-card-one"><span class="docs-art-icon">◈</span><span>Connect</span><i></i><i></i></div>
    <div class="docs-art-card docs-art-card-two"><span class="docs-art-icon">✦</span><span>Trust</span><i></i><i></i></div>
    <div class="docs-art-card docs-art-card-three"><span class="docs-art-icon">◎</span><span>Activate</span><i></i><i></i></div>
    <div class="docs-art-core">C<span>.</span></div>
  </div>
</section>

<section class="docs-home-section" aria-labelledby="docs-paths-title">
  <div class="docs-section-heading"><div><span class="docs-kicker">EXPLORE THE PLATFORM</span><h2 id="docs-paths-title">Find your path</h2></div><p>Start with a workflow, then go deeper when you're ready.</p></div>
  <div class="docs-feature-grid">
    <a class="docs-feature-card" href="{{ '/integration' | relative_url }}"><span class="docs-feature-icon blue">↗</span><span class="docs-feature-number">01 / CONNECT</span><strong>Bring data in</strong><span>Ingest and map data from your sources.</span><b aria-hidden="true">↗</b></a>
    <a class="docs-feature-card" href="{{ '/Preparation' | relative_url }}"><span class="docs-feature-icon violet">✧</span><span class="docs-feature-number">02 / PREPARE</span><strong>Improve quality</strong><span>Clean, enrich, and standardize records.</span><b aria-hidden="true">↗</b></a>
    <a class="docs-feature-card" href="{{ '/management' | relative_url }}"><span class="docs-feature-icon cyan">◎</span><span class="docs-feature-number">03 / MANAGE</span><strong>Create golden records</strong><span>Apply rules, resolve duplicates, and model relationships.</span><b aria-hidden="true">↗</b></a>
    <a class="docs-feature-card" href="{{ '/consume' | relative_url }}"><span class="docs-feature-icon coral">⇢</span><span class="docs-feature-number">04 / ACTIVATE</span><strong>Deliver trusted data</strong><span>Stream clean data to the systems that use it.</span><b aria-hidden="true">↗</b></a>
  </div>
</section>

<section class="docs-home-section docs-home-resources" aria-labelledby="docs-resources-title">
  <div class="docs-section-heading"><div><span class="docs-kicker">POPULAR RESOURCES</span><h2 id="docs-resources-title">Go further</h2></div></div>
  <div class="docs-resource-grid">
    <a href="{{ '/deployment' | relative_url }}"><span>◉</span><strong>Installation</strong><small>Set up your environment</small><b aria-hidden="true">↗</b></a>
    <a href="{{ '/microsoft-integration' | relative_url }}"><span>▦</span><strong>Microsoft integration</strong><small>Connect across your Microsoft stack</small><b aria-hidden="true">↗</b></a>
    {% if site.baseurl == '' %}
    <a href="{{ '/rest-api' | relative_url }}"><span>{ }</span><strong>REST API</strong><small>Explore endpoints and examples</small><b aria-hidden="true">↗</b></a>
    {% else %}
    <a href="{{ '/kb' | relative_url }}"><span>✳</span><strong>Knowledge base</strong><small>Find answers and practical guides</small><b aria-hidden="true">↗</b></a>
    {% endif %}
    <a href="{{ '/release-notes' | relative_url }}"><span>✳</span><strong>What's new</strong><small>Explore recent releases</small><b aria-hidden="true">↗</b></a>
  </div>
</section>
