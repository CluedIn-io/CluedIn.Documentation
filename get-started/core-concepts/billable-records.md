---
title: Billable records
url: https://documentation.cluedin.net/get-started/core-concepts/billable-records
content_type: concept
section: Get started > Core concepts
---

# Billable records

> concept: Explains how something works.

A billable record is a unique data part that forms a golden record. In this case, an ingested record is considered a data part. For more information about records, data parts, and golden records, see [Data life cycle](https://documentation.cluedin.net/get-started/core-concepts/data-life-cycle.md).

The following video illustrates the difference between billable records and golden records.

Not all data parts are considered billable records. The data parts that appeared from the following processes are not billable records:

- Enrichment
- Clean projects
- User input (editing properties manually)
- Shadow entities
- Any updates to the source record

> **Important:** Every time a golden record is processed, the count of billable records is recalculated. If you remove records from CluedIn, the count of billable records would go down as it is recalculated.

Each record that you ingest and process from your source counts as a billable record. If 2 records come from the same source and share the same identifier ([primary identifier](https://documentation.cluedin.net/model/identifiers.md) and [origin](https://documentation.cluedin.net/get-started/core-concepts/origin.md)) then they are considered exact duplicates and are merged into one golden record. This is 1 billable record.

If 2 similar records come from different sources and are identified as duplicates, they are also merged into 1 golden record, but they will be counted as 2 billable records.

If 2 unique records come from the same or different sources, then 2 golden records are created. Therefore, there are 2 data parts, which means that there are 2 billable records.

When you ingest a record for the first time, a unique primary identifier is created in the mapping to identify this record once processed. If you later change the value that was used to create the primary identifier in the golden record and re-ingest the original record with the updated value, this will be considered as 2 data parts, resulting in 2 billable records. This is because CluedIn perceives the identifier that was initially created during the mapping as different from the updated record.

Up: [Core concepts](https://documentation.cluedin.net/get-started/core-concepts.md)
