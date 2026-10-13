---
title: First tour of the instance and the golden record mindset
url: https://documentation.cluedin.net/learning-paths/data-steward/instance-tour-and-golden-record-mindset
content_type: tutorial
section: Learning paths > Data Steward course
---

# First tour of the instance and the golden record mindset

> tutorial: Guided end-to-end learning.

## Learning outcome

Trace a visible golden-record value back to the evidence that contributed to it.

## Scenario

A business user says a value on a record is wrong. Before editing it, you need to understand whether the visible value came from a source, a later change, or a merge.

## Read

- [Golden records](https://documentation.cluedin.net/get-started/core-concepts/golden-records.md)
- [History](https://documentation.cluedin.net/master/golden-records/history.md)

## Exercise

1. Find three records from your training domain.
2. Open each golden record and choose one important property.
3. Use History to identify the data parts or changes contributing to that property.
4. Where useful, inspect relations or topology to understand merge or connection context.
5. For one record, explain why the current value is visible and what evidence you would need before changing it.

## Deliverable

An issue-log entry for one record showing the visible value, contributing evidence, likely origin, and whether any action is justified.

## Complete when

- You can explain the difference between source data, contributing data parts, and the golden record.
- You can use History to investigate where a value came from.
- You do not treat the current record screen as the whole evidence set.

## Next

Continue to [How ingestion, mapping, and processing affect stewardship](https://documentation.cluedin.net/learning-paths/data-steward/ingestion-mapping-and-processing-for-stewards.md).

Up: [Data Steward course](https://documentation.cluedin.net/learning-paths/data-steward.md)
