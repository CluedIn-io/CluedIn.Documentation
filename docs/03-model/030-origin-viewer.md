---
layout: cluedin
title: Origin viewer
parent: Model
nav_order: 30
permalink: /model/origin-viewer
content_type: how-to
tags: ["governance", "identifiers", "origin"]
last_modified: 2026-10-24
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Compare how the records from 2 or 3 sources overlap, based on which golden records their [identifiers](/model/identifiers) merged into. The origin viewer shows this as a Venn diagram: how many entities came from only one of the selected sources, and how many are shared because records from more than one source merged into the same golden record.

Use this to understand, for a given set of sources, how much entity resolution across them is actually happening - for example, to sanity-check that two systems you expect to describe the same customers are in fact merging, or to see how much of a new source's data is net-new versus already represented elsewhere.

## Prerequisites

- At least 2 sources must have contributed processed records. A source with no processed entities does not appear in the picker.

## Open the origin viewer

1. On the navigation pane, go to **Governance** > **Global Data Model**.

1. In the **Sources** list, select a source to open its details panel, then select **View identifier overlap**.

   This opens the origin viewer with that source preselected. You can also go to the origin viewer directly and select sources from there.

1. Select 2 or 3 sources to compare.

The Venn diagram updates once 2 or 3 sources are selected: each circle represents one source, labeled with its name, and each region shows how many entities fall into that combination of sources - for example, the number in the overlapping area between two circles is how many entities have records from both sources.

## Verify the result

A region's count only appears once at least one entity matches that exact combination of sources; a combination with no matching entities is left blank rather than shown as zero.

## What this changes

Nothing. The origin viewer is read-only - it queries existing processed entities and does not change mappings, identifiers, or golden records.

## Useful resources

- [Identifiers](/model/identifiers)
- [Origin](/get-started/core-concepts/origin)
- [Global Data Model](/model/global-data-model)
