---
layout: cluedin
title: First tour of the instance and the golden record mindset
parent: Data Steward course
grand_parent: Learning paths
nav_order: 20
permalink: /learning-paths/data-steward-course/instance-tour-and-golden-record-mindset
---

## Learning outcome

Trace a visible golden-record value back to the evidence that contributed to it.

## Scenario

A business user says a value on a record is wrong. Before editing it, you need to understand whether the visible value came from a source, a later change, or a merge.

## Read

- [Golden records](/key-terms-and-features/golden-records)
- [History](/key-terms-and-features/golden-records/history)

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

Look earlier in the lifecycle to understand how ingestion and mapping choices create downstream symptoms.
