---
title: Deduplication
url: https://documentation.cluedin.net/master/deduplication
content_type: landing
section: Master
---

# Deduplication

The goal of deduplication is to eliminate duplicate records by merging them together into a single, accurate, and consolidated golden record. This process maintains full traceability, allowing you to identify contributing records for the resulting golden record and providing the possibility to revert changes if necessary.

> **Important:** You can reduce the number of duplicates in the system proactively even before creating a deduplication project. For this purpose, CluedIn provides the possibility of merging by identifiers: those [data parts](https://documentation.cluedin.net/get-started/core-concepts/data-life-cycle.md) that have identical primary identifiers or additional identifiers are merged during processing. For more information, see [Identifiers](https://documentation.cluedin.net/ingest/mapping/review-mapping.md#identifiers).

The following diagram shows the basic steps for merging duplicates in CluedIn.

![How to merge duplicates in CluedIn: 1 configure matching rules, 2 review groups of duplicates, 3 merge duplicates, 4 reevaluate merged records, 5 optionally revert merges](https://documentation.cluedin.net/assets/images/management/deduplication/dedup-main.gif)

This section covers the following areas:

- [Concept of deduplication](https://documentation.cluedin.net/master/deduplication/concept-of-deduplication.md) – explore how deduplication works through a simple yet detailed example.

- [Deduplication in practice](https://documentation.cluedin.net/master/deduplication/deduplication-in-practice.md) – discover the practical application of deduplication guidelines through an example.

- [Creating a deduplication project](https://documentation.cluedin.net/master/deduplication/create-a-deduplication-project.md) – learn how to create a deduplication project and configure matching rules.

- [Managing a deduplication project](https://documentation.cluedin.net/master/deduplication/manage-a-deduplication-project.md) – learn how to effectively manage a deduplication project, including generating and discarding results, editing project configuration, and more.

- [Managing groups of duplicates](https://documentation.cluedin.net/master/deduplication/manage-groups-of-duplicates.md) – learn how to process groups of duplicates, including merging duplicates, verifying merged records, and reverting merges.

- [Reference information about deduplication projects](https://documentation.cluedin.net/master/deduplication/deduplication-reference.md) – find information about matching functions, rule conditions, deduplication project statuses, and group statuses.

- [Matching one of multiple fields](https://documentation.cluedin.net/master/deduplication/match-one-of-multiple-fields.md) – learn how to identify duplicates when any value from a group of fields matches across records.

## In this section

- [Concept of deduplication](https://documentation.cluedin.net/master/deduplication/concept-of-deduplication.md) (concept): Let's explore the concept of deduplication in CluedIn through an example.
- [Deduplication in practice](https://documentation.cluedin.net/master/deduplication/deduplication-in-practice.md) (concept): In this article, you'll discover various strategies on how to efficiently deduplicate large data sets in CluedIn.
- [Create a deduplication project](https://documentation.cluedin.net/master/deduplication/create-a-deduplication-project.md) (how-to): Create a deduplication project when you want CluedIn to find golden records that describe the same thing, so that you can review and merge them.
- [Manage a deduplication project](https://documentation.cluedin.net/master/deduplication/manage-a-deduplication-project.md) (how-to): After you create and configure your deduplication project, you can begin the deduplication process to eliminate duplicates and produce a unified and accurate representation of a golden record.
- [Manage groups of duplicates](https://documentation.cluedin.net/master/deduplication/manage-groups-of-duplicates.md) (how-to): Process and merge groups of duplicates when a deduplication project has generated matches and you want to turn each group into one golden record.
- [Deduplication reference](https://documentation.cluedin.net/master/deduplication/deduplication-reference.md) (reference): In this article, you will find reference information to help you understand matching rules and functions, normalization rules, deduplication project statuses, and group statuses.
- [Tutorial: deduplicate data](https://documentation.cluedin.net/master/deduplication/tutorial-deduplicate-data.md) (tutorial): Deduplication process helps you find and merge duplicate records based on a set of rules that you define.
- [Best Practices for Matching and Merging](https://documentation.cluedin.net/master/deduplication/best-practices-for-matching-and-merging.md) (concept): Matching and merging is a core capability of CluedIn.
- [Get better matches in deduplication projects](https://documentation.cluedin.net/master/deduplication/better-matches.md) (how-to): Deduplication Projects in CluedIn help identify and merge duplicate records across your data sources.
- [Match one of multiple fields](https://documentation.cluedin.net/master/deduplication/match-one-of-multiple-fields.md) (how-to): In this article, you will learn how to identify duplicates when a record contains several values of the same kind and any one of those values can match another record.

Up: [Master](https://documentation.cluedin.net/master.md)
