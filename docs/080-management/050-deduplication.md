---
layout: cluedin
title: Deduplication
parent: Management
nav_order: 020
has_children: true
permalink: /management/deduplication
---

The goal of deduplication is to eliminate duplicate records by merging them together into a single, accurate, and consolidated golden record. This process maintains full traceability, allowing you to identify contributing records for the resulting golden record and providing the possibility to revert changes if necessary.

**Important!** You can reduce the number of duplicates in the system proactively even before creating a deduplication project. For this purpose, CluedIn provides the possibility of merging by codes: those [data parts](/key-terms-and-features/data-life-cycle) that have identical entity origin codes or entity codes are merged during processing. For more information, see [Codes](/integration/review-mapping#codes).
 
The following diagram shows the basic steps for merging duplicates in CluedIn.

![dedup-main.gif](/.attachments/dedup-main-66f61ed2-5235-491d-b4d9-a8c1c5a04e48.gif)

This section covers the following areas:

- [Concept of deduplication](/Documentation/Management/Deduplication/Concept-of-deduplication) – explore how deduplication works through a simple yet detailed example.

- [Creating a deduplication project](/Documentation/Management/Deduplication/Create-a-deduplication-project) – learn how to create a deduplication project and configure matching rules according to our deduplication guidelines.

- [Managing a deduplication project](/Documentation/Management/Deduplication/Manage-a-deduplication-project) – learn how to effectively manage a deduplication project, including generating and discarding results, editing project configuration, and more.

- [Managing groups of duplicates](/Documentation/Management/Deduplication/Manage-groups-of-duplicates) – learn how to process groups of duplicates, including merging duplicates, verifying merged records, and reverting merges.

- [Reference information about deduplication projects](/Documentation/Management/Deduplication/Deduplication-reference) – find information about matching functions, rule conditions, deduplication project statuses, and group statuses.