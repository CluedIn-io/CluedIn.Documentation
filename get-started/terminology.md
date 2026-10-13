---
title: Terminology
url: https://documentation.cluedin.net/get-started/terminology
content_type: reference
section: Get started
---

# Terminology

> reference: Facts, options, APIs.

Each term below has exactly one home in the documentation. If you are looking for the definition, start here; if you are looking for how to work with the thing, follow the link.

| Term | What it means | Canonical home |
|---|---|---|
| Golden record | The single trusted record for one real-world thing, built from all the data parts that describe it. | [Core concepts](https://documentation.cluedin.net/get-started/core-concepts/golden-records.md) - working with them: [Master](https://documentation.cluedin.net/master/golden-records.md) |
| Data part | One system's version of a record at one point in time. Golden records are assembled from data parts. | [Data life cycle](https://documentation.cluedin.net/get-started/core-concepts/data-life-cycle.md) |
| Clue | The unit of data CluedIn ingests - a record plus its metadata and identifiers. | [Clue reference](https://documentation.cluedin.net/get-started/core-concepts/clue-reference.md) |
| Business domain | The classification of a record, such as Customer or Product. Formerly called *entity type*. | [Model](https://documentation.cluedin.net/model/business-domains.md) |
| Vocabulary | The set of properties that describe records in a business domain. Formerly called *schema*. | [Model](https://documentation.cluedin.net/model/vocabularies.md) |
| Vocabulary key | One property within a vocabulary. | [Model](https://documentation.cluedin.net/model/vocabularies/vocabulary-keys.md) |
| Identifier | A value that identifies a record across systems and lets CluedIn connect records. Formerly called *entity code*. | [Model](https://documentation.cluedin.net/model/identifiers.md) |
| Edge / relationship | A connection between two records. | [Model](https://documentation.cluedin.net/model/relationships.md) |
| Origin | The system a data part came from. | [Core concepts](https://documentation.cluedin.net/get-started/core-concepts/origin.md) |
| Eventual connectivity | Records connecting up as evidence arrives, rather than requiring an agreed schema up front. | [Core concepts](https://documentation.cluedin.net/get-started/core-concepts/eventual-connectivity.md) |
| Data source | A file, database, endpoint or connector that feeds records into CluedIn. | [Ingest](https://documentation.cluedin.net/ingest/data-sources.md) |
| Mapping | The definition of which source column becomes which vocabulary key. | [Ingest](https://documentation.cluedin.net/ingest/mapping.md) |
| Clean project | A workspace for fixing recurring data quality problems. | [Govern & improve](https://documentation.cluedin.net/govern/cleaning.md) |
| Deduplication project | A workspace for finding and merging duplicate records. | [Master](https://documentation.cluedin.net/master/deduplication.md) |
| Rule | Logic applied automatically to data parts or golden records. | [Govern & improve](https://documentation.cluedin.net/govern/rules.md) |
| Enricher | A service that adds data from an external source. | [Govern & improve](https://documentation.cluedin.net/govern/enrichment.md) |
| Glossary term | A named group of golden records that meet a condition. | [Govern & improve](https://documentation.cluedin.net/govern/work-with-glossary.md) |
| Stream | A continuous export of golden records to an export target. | [Publish & consume](https://documentation.cluedin.net/publish/streams.md) |
| Export target | The destination a stream writes to. | [Publish & consume](https://documentation.cluedin.net/publish/export-targets.md) |

Several of these names changed in the 2025.05 release. See [Terminology changes](https://documentation.cluedin.net/release-notes/terminology-changes.md) for the full before-and-after list.

Up: [Get started](https://documentation.cluedin.net/get-started.md)
