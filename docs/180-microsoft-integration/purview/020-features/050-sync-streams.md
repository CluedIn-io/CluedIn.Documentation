---
layout: cluedin
title: Sync CluedIn Streams
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/purview/features/sync-streams
nav_order: 050
has_children: false
tags: ["integration", "microsoft", "azure", "purview", "collection", "sync", "streams"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

## Sync CluedIn Streams

![Settings Sync Streams](../media/settings-sync-streams.png)

A background processing in CluedIn synchronizes streams and their respective export connector as assets in Purview. These assets show outbound lineage from CluedIn entity types to the export target.

Details of CluedIn Streams named as `Customer Golden Record` with Export Target configured with Target name `Customer`

![CluedIn Streams](../media/cluedin-stream.png)

Full Lineage of Purview Asset to CluedIn Stream

![Full Lineage](../media/sync-streams-asset-lineage.png)

CluedIn Stream created as a Process Asset and Export Target as the Entity Asset.

![Stream and Export Target Asset](../media/sync-streams-process-and-export-target.png)
