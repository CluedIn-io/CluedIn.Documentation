---
layout: cluedin
title: Review source-level validations
parent: Data Steward course
grand_parent: Learning paths
permalink: /learning-paths/data-steward-course/review-source-level-validations
nav_order: 50
tags: ["learning-paths", "data-steward", "training"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This module focuses on the validation surface for source records.

## Learning objective

Understand how validations help a steward identify bad values before they become golden-record quality problems.

## What to learn

- where validations are accessed;
- when to use auto-validation vs manual validation;
- what advanced validation is for;
- how to read validation results and locate invalid values.

![Access validations]({{ "/assets/images/integration/additional-operations/access-validations.png" | relative_url }})

![Validation results]({{ "/assets/images/integration/additional-operations/validations-result.png" | relative_url }})

![Invalid values]({{ "/assets/images/integration/additional-operations/validations-invalid-values.png" | relative_url }})

## Exercises

1. Open the **Validations** pane for a mapped data set.
1. Run auto-validation and explain which fields CluedIn suggested.
1. Add one manual validation for a field that matters to stewardship.
1. Find invalid values and correct one example.
1. Verify that the corrected value no longer appears as invalid.

## Steward judgment to reinforce

Validations help you find evidence quickly, but the steward still decides whether the bad value should be corrected, escalated, or converted into a repeatable architecture change.

## Related documentation

- [Validations](/integration/additional-operations-on-records/validations)
- [Review mapping](/integration/review-mapping)
