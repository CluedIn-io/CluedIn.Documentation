---
layout: cluedin
title: Terminology
parent: Get started
nav_order: 50
permalink: /get-started/terminology
content_type: reference
---

Each term below has exactly one home in the documentation. If you are looking for the definition, start here; if you are looking for how to work with the thing, follow the link.

| Term | What it means | Canonical home |
|---|---|---|
| Golden record | The single trusted record for one real-world thing, built from all the data parts that describe it. | [Core concepts](/get-started/core-concepts/golden-records) - working with them: [Master](/master/golden-records) |
| Data part | One system's version of a record at one point in time. Golden records are assembled from data parts. | [Data life cycle](/get-started/core-concepts/data-life-cycle) |
| Clue | The unit of data CluedIn ingests - a record plus its metadata and identifiers. | [Clue reference](/get-started/core-concepts/clue-reference) |
| Business domain | The classification of a record, such as Customer or Product. Formerly called *entity type*. | [Model](/model/business-domains) |
| Vocabulary | The set of properties that describe records in a business domain. Formerly called *schema*. | [Model](/model/vocabularies) |
| Vocabulary key | One property within a vocabulary. | [Model](/model/vocabularies/vocabulary-keys) |
| Identifier | A value that identifies a record across systems and lets CluedIn connect records. Formerly called *entity code*. | [Model](/model/identifiers) |
| Edge / relationship | A connection between two records. | [Model](/model/relationships) |
| Origin | The system a data part came from. | [Core concepts](/get-started/core-concepts/origin) |
| Eventual connectivity | Records connecting up as evidence arrives, rather than requiring an agreed schema up front. | [Core concepts](/get-started/core-concepts/eventual-connectivity) |
| Data source | A file, database, endpoint or connector that feeds records into CluedIn. | [Ingest](/ingest/data-sources) |
| Mapping | The definition of which source column becomes which vocabulary key. | [Ingest](/ingest/mapping) |
| Clean project | A workspace for fixing recurring data quality problems. | [Govern & improve](/govern/cleaning) |
| Deduplication project | A workspace for finding and merging duplicate records. | [Master](/master/deduplication) |
| Rule | Logic applied automatically to data parts or golden records. | [Govern & improve](/govern/rules) |
| Enricher | A service that adds data from an external source. | [Govern & improve](/govern/enrichment) |
| Glossary term | A named group of golden records that meet a condition. | [Govern & improve](/govern/work-with-glossary) |
| Stream | A continuous export of golden records to an export target. | [Publish & consume](/publish/streams) |
| Export target | The destination a stream writes to. | [Publish & consume](/publish/export-targets) |

Several of these names changed in the 2025.05 release. See [Terminology changes](/release-notes/terminology-changes) for the full before-and-after list.
