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