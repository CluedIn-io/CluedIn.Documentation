---
layout: cluedin
title: Sync CluedIn Crawlers and Enrichers
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/purview/features/sync-crawlers-and-enrichers
nav_order: 040
has_children: false
tags: ["integration", "microsoft", "azure", "purview", "collection", "sync", "crawlers", "enrichers"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}


## Sync CluedIn Crawlers and Enrichers

![Settings Sync Crawlers and Enrichers](../media/settings-sync-crawlers-and-enrichers.png)

This feature will create or update existing crawlers and enricher lineages in Purview. The **DataSource** provider types (data imported via files, endpoints, or databases) are handled by the **Sync CluedIn Data Sources** feature.

The following image shows an example of a crawler lineage.

![Example of a Crawler lineage](../media/crawler_lineage.png)

When a Crawler imports clues into CluedIn, this feature creates a lineage from the Crawler provider to the entity types of the CluedIn entities via the **Crawl** process.

The following image shows an example of an enricher lineage.

![Example of an Enricher lineage](../media/enricher_lineage.png)

When an enricher enriches an entity, this feature creates a lineage from the enricher provider to the entity types of the CluedIn entities via the **Enrich** process.

