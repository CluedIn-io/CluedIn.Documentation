---
layout: cluedin
title: Resources for Data Steward
parent: Playbooks
nav_order: 80
permalink: /playbooks/resources-for-data-steward
content_type: reference
source_path: docs/210-playbooks/110-resources-for-data-steward.md
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

| Audience | Time to read |
|--|--|
| Data Steward | 3 min |

This page includes links to relevant documentation and videos to help Data Stewards perform their tasks in the [data quality virtuous cycle](/playbooks/project-delivery/start-your-cluedin-project#data-journey).

## Before you start

Learn about the fundamental concepts and features in CluedIn.

| Activity | Resources |
|--|--|
| Learn about golden records in CluedIn | [Golden records](/get-started/core-concepts/golden-records) |
| Learn how to search for golden records in CluedIn | [Search](/master/search) |
| Learn how to work with filters in CluedIn | [Filters](/master/filters) |

## Data ingestion

Data Stewards can review the records in quarantine and approve or reject them as needed. Approved records will go into processing and aggregate to the existing golden records or create new golden records.

| Activity | Resources |
|--|--|
| Learn about the quarantine tool in CluedIn| [Quarantine](/ingest/troubleshooting/quarantine) |
| Learn how to make changes to data that has been quarantined before submitting it to CluedIn | [Video](https://vimeo.com/manage/videos/818029549) |

## Data transformation

Data Stewards can identify and correct any data quality issues with the help of clean projects, enhance golden records with information from third-party sources, and establish criteria for finding and eliminating duplicates.

### Cleaning

| Activity | Resources |
|--|--|
| Get acquainted with the cleaning process in CluedIn | [How to get started with data cleaning](/govern/cleaning/tutorial-clean-data) |
| Learn about different ways to create a clean project | [Create a clean project](/govern/cleaning/create-clean-project) |
| Fix data quality issues in the clean application | [Manage a clean project](/govern/cleaning/manage-clean-project) |
| Build automated rules based on data cleaning activities | [Video](https://vimeo.com/manage/videos/818226739) |
| Understand the statuses of the clean project | [Clean project reference](/govern/cleaning/clean-reference) |
| Use profiling to find data quality issues | [Video](https://vimeo.com/manage/videos/915819936) |

### Enrichment

| Activity | Resources |
|--|--|
| Get acquainted with the enrichment process | [Concept of enricher](/govern/enrichment/concept-of-enricher) |
| Learn about different enrichers and find instructions on how to configure each enricher | [Enricher reference](/govern/enrichment/enricher-reference) |
| Enrich data from third-party services in CluedIn | [Video](https://vimeo.com/manage/videos/818212859) |

### Deduplication

| Activity | Resources |
|--|--|
| Get acquainted with the deduplication process in CluedIn | [How to get started with deduplication](/master/deduplication/tutorial-deduplicate-data) |
| Watch step-by-step video on the basic deduplication of data | [Video](https://vimeo.com/manage/videos/818181700) |
| Learn about the strategies on how to efficiently deduplicate large data sets in CluedIn | [Deduplication in practice](/master/deduplication/deduplication-in-practice) |
| Create a deduplication project and configure matching rules for detecting duplicates | [Create a deduplication project](/master/deduplication/create-a-deduplication-project) |
| Learn how to use probabilistic matching rules to find duplicates | [Video](https://vimeo.com/manage/videos/818195428) |
| Learn how to process and merge groups of duplicates | [Manage groups of duplicates](/master/deduplication/manage-groups-of-duplicates) |
| Learn how to split merged records | [Video](https://vimeo.com/manage/videos/818196287) |

## Data automation

Data Stewards can create business rules to apply data transformations, capture data quality issues, and determine operational values.

| Activity | Resources |
|--|--|
| Get acquainted with high-level rule creation process | [How to get started with rules](/govern/rules/tutorial-create-rules) |
| Get acquainted with different types of rules in CluedIn | [Data part rules](/govern/rules/rule-types#data-parts-rules), [survivorship rules](/govern/rules/rule-types#survivorship-rules), [golden record rules](/govern/rules/rule-types#golden-record-rules) |
| Learn how to create a business rule | [Create a rule](/govern/rules/create-rule) |
| Use OpenAI for data automation in CluedIn | [Video](https://vimeo.com/manage/videos/811556560) |
| Use OpenAI to explain automation in rules | [Video](https://vimeo.com/manage/videos/811562503) |

## Data export

Data Stewards can configure the stream and define which golden records should be sent to the external systems.

| Activity | Resources |
|--|--|
| Get acquainted with the high-level streaming process | [How to get started with streaming](/publish/streams/tutorial-stream-data) |
| Learn how to create and configure a stream | [Create a stream](/publish/streams/create-a-stream) |
| Watch a video about creating a stream proactively without having the data yet | [Video](https://vimeo.com/manage/videos/818559305) |
| Watch a video about synchronized and event log stream modes | [Video](https://vimeo.com/manage/videos/818044917) |

## Additional data management activities

Data Stewards can use hierarchies to visualize relations between golden records, create glossary categories and terms to group golden records, and use other tools in CluedIn to facilitate data management.

| Activity | Resources |
|--|--|
| Visualize relations between golden records with the help of hierarchies | [How to get started with hierarchies](/model/hierarchies/tutorial-create-hierarchies) |
| Build manual hierarchies | [Video](https://vimeo.com/manage/videos/818043927) |
| Build automated hierarchies | [Video](https://vimeo.com/manage/videos/818032837) |
| Create glossary categories and terms | [How to get started with glossary](/govern/work-with-glossary) |
| Use glossary terms in streams | [Video](https://vimeo.com/manage/videos/818045893) |
| Using Copilot to help in the data management process | [Video](https://vimeo.com/manage/videos/915817750) |