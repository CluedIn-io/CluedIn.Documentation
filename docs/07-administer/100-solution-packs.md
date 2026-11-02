---
layout: cluedin
title: Solution Packs
parent: Administer
nav_order: 100
permalink: /administer/solution-packs
content_type: reference
tags: ["administration", "marketplace", "solution packs", "business domains", "vocabularies"]
last_modified: 2026-11-02
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

A Solution Pack is an industry or domain accelerator that bundles prebuilt Rules, Matching configurations,
Dashboards, Workflow templates, Business Domains, Vocabularies, AI Agents, suggested Roles, Golden Record rules,
Data Profiling rules and Glossary terms for a specific use case, such as retail master data or financial services
customer 360. Installing a pack is a faster starting point than building the same configuration by hand.

Browse, install, update and uninstall packs from **Settings** > **Marketplace** > **Solution Packs**.

![The Solution Packs catalogue, showing a featured pack, filters, a grid of catalogue packs and a Recommended for your workspace panel]({{ "/assets/images/administration/solution-packs/solution-packs-catalogue.png" | relative_url }})

## Browse the catalogue

The catalogue lists every available pack, with a search box and filters for Industry, Domain, Compatibility and
Installed status. Each pack shows:

- Its industry and the business domains it covers.
- Whether it is CluedIn Verified, its compatibility range and version.
- How many other organizations have installed it, and when it was last updated.
- A count of each kind of artifact it includes (Rules, Matching configs, Dashboards, Workflows, Business Domains,
  Vocabularies, AI Agents, Roles, Golden Record rules, Data Profiling rules, Glossary terms).

Select **View details** on a pack to open its details page, with its full description and every artifact it
includes, grouped by kind.

![The Solution Pack details page for Healthcare Data Quality, listing its Rules, Matching configs, Dashboards, Workflows, Business Domains, Vocabularies, AI Agents, Role, Golden Record rules, Data Profiling rules and Glossary terms]({{ "/assets/images/administration/solution-packs/solution-packs-details-panel.png" | relative_url }})

### Recommended for your workspace

The panel on the right of the catalogue recommends packs based on your own workspace: the source types you have
connected, and the business domains already in use. A pack is recommended when its declared source types or
domains match what you already have configured; when nothing matches yet, it falls back to the most-installed
packs. The same detected sources and domains in use are listed above the recommendations.

## Install a pack

1. On the navigation pane, go to **Settings** > **Marketplace** > **Solution Packs**.
1. Find a pack, either from the catalogue grid or the Recommended for your workspace panel.
1. Select **Install pack**.

### What this creates

Installing a pack creates the [Business Domains]({{ "/model/business-domains" | relative_url }}) and
[Vocabularies]({{ "/model/vocabularies" | relative_url }}) it declares as real, organization-scoped configuration,
immediately visible on their own pages. A business domain that already exists under the same name is reused
rather than duplicated.

The pack's other declared artifacts — Rules, Matching configurations, Dashboards, Workflow templates, AI Agents,
suggested Roles, Golden Record rules, Data Profiling rules and Glossary terms — are tracked against the installed
pack, and their counts are shown on the pack's card and details page, but they are not yet created as working
configuration in their own areas. The pack's details page marks each artifact **Available now** or **Tracked with
this pack; not yet available in its own area** accordingly.

## Update a pack

When a pack you have installed has a newer catalogue version, its row in **Installed packs** shows an
**Update available** status and an **Update** action. Selecting **Update** records the pack as being on the
latest version; it does not currently re-run installation for artifacts added by the new version.

## Uninstall a pack

From **Installed packs**, select **Uninstall** on the pack, then confirm. This removes the Business Domains and
Vocabularies the pack installed. If a business domain is still referenced by a vocabulary your organization added
separately, that business domain is left in place rather than failing the whole uninstall — uninstall always
clears the pack's own installed-state tracking, even when some of what it created could not be fully removed.

Rules, Matching configurations, Dashboards, Workflows, AI Agents, suggested Roles, Golden Record rules, Data
Profiling rules and Glossary terms the pack declared are not affected, since installing a pack does not yet create
them as working configuration — see [What this creates](#what-this-creates).

## Upload a custom pack

Besides the built-in catalogue, you can upload your own Solution Pack package. A package is the same zip format
[Import/Export Configuration]({{ "/operate/configuration/configuration-import-export" | relative_url }}) already uses: a
`solution-pack-manifest.json` describing the pack, optionally alongside a Configuration Migration bundle of real
Vocabularies.

1. On the navigation pane, go to **Settings** > **Marketplace** > **Solution Packs**.
1. Select **Upload pack**, at the top of the catalogue.
1. Choose a `.zip` package.

The uploaded pack appears in the catalogue tagged **Custom**, alongside the built-in packs, with a status of
**Not installed**. Installing it works the same way as any other pack — see [Install a pack](#install-a-pack). If
its package bundled a Configuration Migration bundle of Vocabularies, installing it imports them in one pass
through the same pipeline Import Configuration uses, rather than one artifact at a time.

An uploaded package must contain a valid `solution-pack-manifest.json`; anything else is rejected with an error
explaining why.

## Export a pack

Any pack — built-in or custom — can be exported as a package: select **Export** on its row in **Installed packs**.

![The Installed packs table, with View details, Export and Uninstall actions on a row]({{ "/assets/images/administration/solution-packs/solution-packs-installed-actions.png" | relative_url }})

- Exporting a **custom** pack re-downloads exactly what was uploaded for it.
- Exporting a **built-in** pack builds a package from what your organization actually has installed: its manifest,
  alongside a Configuration Migration bundle of the Vocabularies it installed. This is also how you turn a
  built-in pack into a starting point for your own custom pack — export it, then upload the result after editing
  it, which registers it as a separate Custom pack rather than replacing the original.
