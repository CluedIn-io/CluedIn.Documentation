---
layout: cluedin
title: Install a Solution Pack
parent: Administer
nav_order: 100
permalink: /administer/solution-packs
content_type: how-to
tags: ["administration", "solution packs", "marketplace"]
last_modified: 2026-11-04
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

A Solution Pack is a bundle of prebuilt Rules, Matching configurations, Dashboards, Workflow templates, Business Domains, Vocabularies, and AI Agents for a specific industry or use case. Installing a pack gets your workspace closer to production-ready data quality without building every configuration from scratch. Use this page to browse, install, uninstall, and upload Solution Packs from the **Solution Packs Marketplace**.

## Prerequisites

- You must be signed in to CluedIn.
- Installing, uninstalling, uploading, and removing packs require the **Solution Packs** claim (**Marketplace** category) at **Accountable**. Organization administrators have this by default.

## Browse the catalogue

1. Go to **Administration** > **Organization settings** > **Marketplace** > **Solution Packs**.
2. On the **Catalogue** tab, use the search box and the Industry, Domain, Compatibility, and Installed status filters to narrow the list.
3. Select **View details** on a pack to see its full list of artifacts before installing.

A **Recommended for your workspace** panel suggests packs based on your connected source types and the business domains already in use.

## Install a Solution Pack

1. On the catalogue or a pack's details page, select **Install pack**.
2. A progress dialog shows each step of the install: Validating pack, Installing artifacts, Finishing up.

### Verify the result

Once the dialog closes, the pack's status changes to **Installed**, and its details page shows **Installed by** with the name of the user who installed it.

### What this changes

- Business Domains, Vocabularies (including their vocabulary keys), and AI Agents are created immediately and are usable right away.
- Rules that map to a known template (Completeness, Format, or Outlier check) are created as real, inactive rules in [Rule Builder](/govern/rules) - review and activate them from there.
- Other artifact kinds (Dashboards, Workflow templates, Matching configurations, Roles, Golden Record rules, Data Profiling rules, Glossary terms) are tracked against the pack so you can see what it includes while dedicated installers for them are built; they do not yet appear in their own area.

{:.note}
On an organization with no data yet, a newly installed pack's Business Domains and Vocabularies may not immediately show as "Used" elsewhere in CluedIn. That's expected - nothing has been ingested against them yet, so usage can't be determined.

## Uninstall a Solution Pack

1. Go to the pack's details page, or the **Installed packs** tab, and select **Uninstall**.
2. Confirm the uninstall.

### What this changes

Uninstalling removes every real entity the pack created, including any Rules it materialized. An entity the pack only linked to or updated - for example, a Business Domain another installed pack also depends on - is left in place.

## Upload a custom Solution Pack

Besides the built-in catalogue, you can upload your own Solution Pack.

1. On the catalogue page, select **Upload pack**.
2. Review the requirements shown in the **Before you upload** panel, then select **Choose file**.
3. Select a `.zip` archive from your computer.

### Inputs

| Requirement | Details |
|---|---|
| File format | A single `.zip` archive. Any other file type is rejected. |
| Manifest | A `solution-pack-manifest.json` file at the root of the archive, describing the pack and its artifacts. |
| Required manifest fields | `id`, `name`, `industry`, `description`, `compatibilityLabel`, `version`, `thumbnailKey`, `domains`, `artifacts`, `relevantSourceTypes`. The upload is rejected if any of these are missing. |
| Migration bundle (optional) | A bundled Configuration Migration export alongside the manifest installs real Vocabularies on top of what the manifest declares. |

### What this changes

A successfully uploaded pack is added to the catalogue as a custom pack, marked with a **Custom** badge, and can be installed the same way as a built-in pack. You can also **Export** an installed custom pack later (for example, to share it with another organization), and **Remove** it from the catalogue once it is no longer installed.

### If something goes wrong

If the archive is missing its manifest, or the manifest is missing a required field, the upload is rejected with a message naming the problem - fix the archive and upload it again.
