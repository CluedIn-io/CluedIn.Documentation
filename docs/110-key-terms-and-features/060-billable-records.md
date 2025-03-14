---
layout: cluedin
title: Billable records
parent: Key terms and features
permalink: /key-terms-and-features/billable-records
nav_order: 6
---

A billable record is a unique data part that forms a golden record. In this case, an ingested record is considered a data part. For more information about records, data parts, and golden records, see [Data life cycle](/key-terms-and-features/data-life-cycle).

The following video illustrates the difference between billable records and golden records.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/928817481?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" title="billable-records-1"></iframe>
</div>

Not all data parts are considered billable records. The data parts that appeared from the following processes are not billable records:

- Enrichment
- Clean projects
- User input (editing properties manually)
- Shadow entities
- Any updates to the source record

{:.important}
Every time a golden record is processed, the count of billable records is recalculated. If you remove records from CluedIn, the count of billable records would go down as it is recalculated.

Each record that you ingest and process from your source counts as a billable record. If 2 records come from the same source and share the same code ([entity origin code (primary identifier)](/key-terms-and-features/entity-codes) and [origin](/key-terms-and-features/origin)) then they are considered exact duplicates and are merged into one golden record. This is 1 billable record.

If 2 similar records come from different sources and are identified as duplicates, they are also merged into 1 golden record, but they will be counted as 2 billable records.

If 2 unique records come from the same or different sources, then 2 golden records are created. Therefore, there are 2 data parts, which means that there are 2 billable records.

When you ingest a record for the first time, a unique entity origin code (primary identifier) is created in the mapping to identify this record once processed. If you later change the value that was used to create the entity origin code (primary identifier) in the golden record and re-ingest the original record with the updated value, this will be considered as 2 data parts, resulting in 2 billable records. This is because CluedIn perceives the code that was initially created during the mapping as different from the updated record.