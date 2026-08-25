---
layout: cluedin
title: Review source quality with validations and mapping checkpoints
parent: Data Steward course
grand_parent: Learning paths
nav_order: 50
permalink: /learning-paths/data-steward-course/validations-and-mapping-checkpoints
---

## Learning outcome

Use validation evidence and mapping review to distinguish bad values from structural mapping problems.

## Scenario

Your saved search shows a recurring invalid value. You need to determine whether the problem should be corrected in records, at the source, or in the mapping or processing design.

## Read

- [Validations](/integration/additional-operations-on-records/validations)
- [Review mapping](/integration/review-mapping)

## Exercise

1. Run or review validations on a mapped training dataset.
2. Isolate one field with invalid values and inspect several examples.
3. Compare the invalid pattern with the field's mapping and identifier context.
4. Classify the issue as value-level, source-level, field/mapping-level, identifier-level, or requiring rule logic.
5. Decide whether stewardship should remediate it or an architect/source owner should change the design.

## Deliverable

A short classification note containing evidence, issue level, owner, and recommended next action.

## Complete when

- You can isolate invalid values using the documented validation workflow.
- You can explain why a validation failure does or does not indicate a mapping defect.
- You can identify the correct owner for the next action.

## Next

For repeatable value-level problems, learn to remediate a defined population through a clean project.
