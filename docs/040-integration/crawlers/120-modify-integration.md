---
layout: cluedin
title: Modify an integration
parent: Crawlers
grand_parent: Ingestion
nav_order: 120
has_children: false
permalink: /integration/modify-integrations
tags: ["integration"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

There will be many times when you need to update an integration. This may happen due to:

- Changes in the source system

- Version upgrades

- Fixing mistakes

## When cleanup is required

Certain situations require cleanup in CluedIn, including:

- Renaming a vocabulary key

- Removing edges

- Changing existing edges

- Removing vocabularies

## Using ObsoleteSince for edges

To remove or change edges, use the `ObsoleteSince` extension method to tell CluedIn that:

- Up to a specific version of your crawler, the edge existed.

- After that version, the edge should be removed or changed.

CluedIn will then handle the cleanup automatically.

You can also manage this via post processors:

- If you handle it in the crawler, your crawlers may become harder to maintain.

- If you handle it in post-processing, your crawlers remain business-logic agnostic.

## Using ObsoleteSince for vocabulary keys

The same approach applies to vocabulary keys.

Use the `ObsoleteSince` method on the `VocabularyKey` class to instruct CluedIn to clean up renamed or deprecated keys.

