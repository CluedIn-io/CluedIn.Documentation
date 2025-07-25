---
layout: cluedin
title: Deduplication
parent: Management
nav_order: 020
has_children: true
permalink: /management/deduplication
---

The goal of deduplication is to eliminate duplicate records by merging them together into a single, accurate, and consolidated golden record. This process maintains full traceability, allowing you to identify contributing records for the resulting golden record and providing the possibility to revert changes if necessary.

{:.important}
You can reduce the number of duplicates in the system proactively even before creating a deduplication project. For this purpose, CluedIn provides the possibility of merging by identifiers: those [data parts](/key-terms-and-features/data-life-cycle) that have identical primary identifiers or additional identifiers are merged during processing. For more information, see [Identifiers](/integration/review-mapping#identifiers).
 
The following diagram shows the basic steps for merging duplicates in CluedIn.

![dedup-main.gif]({{ "/assets/images/management/deduplication/dedup-main.gif" | relative_url }})

This section covers the following areas:

- [Concept of deduplication](/management/deduplication/concept-of-deduplication) – explore how deduplication works through a simple yet detailed example.

- [Deduplication in practice](/management/deduplication/deduplication-in-practice) – discover the practical application of deduplication guidelines through an example.

- [Creating a deduplication project](/management/deduplication/create-a-deduplication-project) – learn how to create a deduplication project and configure matching rules.

- [Managing a deduplication project](/management/deduplication/manage-a-deduplication-project) – learn how to effectively manage a deduplication project, including generating and discarding results, editing project configuration, and more.

- [Managing groups of duplicates](/management/deduplication/manage-groups-of-duplicates) – learn how to process groups of duplicates, including merging duplicates, verifying merged records, and reverting merges.

- [Reference information about deduplication projects](/management/deduplication/deduplication-reference) – find information about matching functions, rule conditions, deduplication project statuses, and group statuses.