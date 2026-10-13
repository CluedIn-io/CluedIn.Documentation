---
title: Review source quality with validations and mapping checkpoints
url: https://documentation.cluedin.net/learning-paths/data-steward/validations-and-mapping-checkpoints
content_type: tutorial
section: Learning paths > Data Steward course
---

# Review source quality with validations and mapping checkpoints

> tutorial: Guided end-to-end learning.

## Learning outcome

Use validation evidence and mapping review to distinguish bad values from structural mapping problems.

## Scenario

Your saved search shows a recurring invalid value. You need to determine whether the problem should be corrected in records, at the source, or in the mapping or processing design.

## Read

- [Validations](https://documentation.cluedin.net/ingest/processing/validations.md)
- [Review mapping](https://documentation.cluedin.net/ingest/mapping/review-mapping.md)

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

Continue to [Clean recurring quality issues with clean projects](https://documentation.cluedin.net/learning-paths/data-steward/clean-projects-and-remediation.md).

Up: [Data Steward course](https://documentation.cluedin.net/learning-paths/data-steward.md)
