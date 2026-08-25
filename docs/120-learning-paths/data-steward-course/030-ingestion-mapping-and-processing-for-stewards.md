---
layout: cluedin
title: How ingestion, mapping, and processing affect stewardship
parent: Data Steward course
grand_parent: Learning paths
nav_order: 30
permalink: /learning-paths/data-steward-course/ingestion-mapping-and-processing-for-stewards
---

## Learning outcome

Recognize when a quality problem originates in source data, mapping, identifiers, or processing rather than in the golden record itself.

## Scenario

A newly processed dataset produces records that are hard to search and some records appear unexpectedly combined. You need to gather evidence without redesigning the mapping yourself.

## Read

- [Ingest data](/getting-started/data-ingestion)
- [Review mapping](/integration/review-mapping)

## Exercise

1. Open a training dataset and review its ingestion and mapping state.
2. Identify the business domain, mapped vocabulary fields, display information, and primary identifier.
3. Inspect processed records in Search.
4. Find one design choice that could make stewardship easier or harder.
5. Describe the symptom that a weak primary identifier, missing mapping, or incorrect data type could create after processing.
6. Draft an escalation note using concrete fields, examples, and expected behavior.

## Deliverable

A mapping-observation note containing the current design, visible consequence, example records, and recommended architect review point.

## Complete when

- You can describe the import, mapping, and processing flow at a stewardship level.
- You can identify mapping choices that affect searchability and identity.
- You can escalate a structural concern with evidence rather than saying only that the data looks wrong.

## Next

Use Search and Filters to turn a reported symptom into a reproducible problem population.
