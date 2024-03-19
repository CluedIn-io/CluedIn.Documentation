---
layout: cluedin
title: Microsoft Purview Integration
parent: Microsoft Integration
permalink: /microsoft-integration/purview
nav_order: 020
has_children: true
tags: ["integration", "microsoft", "azure", "purview"]
---

CluedIn integrates with your Microsoft Purview instance to synchronize your assets, glossaries, and lineage of your data journey in CluedIn.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/903163655?h=40b1cff944&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Purview x CluedIn Integration"></iframe>
</div>

The following table provides a list of integration features.

| Integration feature | Description
| ---- | ------ |
| Poll CluedIn Data Sources | Update properties and metrics on the existing "Cluedin Dataset" Purview entities.
| Synchronize CluedIn Vocabularies to Purview Glossary Terms | Create Purview Glossary Terms from CluedIn Vocabularies.
| Synchronize Data Sources | Create and update "Cluedin Ingest Process", "Cluedin Dataset", "Cluedin Map Process", and "Cluedin Entity" entities on Purview lineages that link Purview assets to CluedIn data sets and their matching CluedIn Entity Types.
| Synchronize Purview Glossaries Terms To CluedIn Glossary Terms | Create CluedIn glossary terms from Purview glossary terms.
| Synchronize Purview Glossary Terms To CluedIn Vocabularies | Create Purview glossary terms from CluedIn vocabulary.
| Synchronize Streams | Create and update "Cluedin Entity", "Cluedin Stream Process", and "Cluedin Organization Provider" entities on Purview lineages that link CluedIn streams and connectors.
| Synchronize Crawlers And Enrichers | Create and update "Cluedin Organization Provider", "Cluedin Crawl Process", "Cluedin Enrich Process", "Cluedin Ingest Process", "Cluedin Dataset", "Cluedin Map Process", and "Cluedin Entity" entities on Purview lineages that link Purview assets to CluedIn data sets and matching CluedIn Entity Types. |

We have the following **assumptions** about the customers' Microsoft Azure setup:

- Customers own only one Purview resource.

- When ingesting data from ADF, the ADF pipeline should only do a one-to-one mapping from targeted file on Azure to API endpoint.