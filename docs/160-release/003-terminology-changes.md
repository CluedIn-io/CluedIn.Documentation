---
layout: cluedin
title: Terminology changes
parent: Release overview
nav_order: 3
permalink: /release-notes/terminology-changes
last_modified: 2025-04-02
---

In the [2025.01 release](/release-notes/2025-01) of CluedIn, we have updated some of the terminology used in the platform. The terminology changes simplify CluedIn interface, making it more intuitive and better aligned with common industry concepts.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1070987058?h=457aee92de&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Terminology changes in CluedIn"></iframe>
</div>

The terminology changes only affect the terms, the functionality behind the terms remains the same. The following table provides a summary of terminology changes in CluedIn.

| Old term | New term | Definition |
|--|--|--|
| Entity type | Business domain | A well-known business object that provides context for golden records. In CluedIn, all golden records must have a business domain to ensure systematic organization of data management processes. Learn more in [Business domain](/key-terms-and-features/entity-type). |
| Entity origin code | Primary identifier | A mechanism used in CluedIn to define the uniqueness of a golden record. It is configured during the mapping process. The primary identifier consists of a business domain, an origin, and a key that uniquely identifies the record. This combination allows you to achieve absolute uniqueness across all the data sources you interact with. Learn more in [Identifiers](/key-terms-and-features/entity-codes). |
| Entity codes | Identifiers | Additional mechanism to define the uniqueness of a golden record. If a data set contains additional columns that can uniquely represent a record, these columns can also be used to generate identifiers. Learn more in [Identifiers](/key-terms-and-features/entity-codes). |