---
layout: cluedin
title: Review source quality with validations and mapping checkpoints
parent: Data Steward course
grand_parent: Learning paths
nav_order: 50
permalink: /learning-paths/data-steward-course/validations-and-mapping-checkpoints
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Some quality issues are easiest to catch before they fully become stewardship problems. Validations and review mapping allow the steward to work earlier in the lifecycle, where bad patterns are cheaper to spot and easier to explain.

## What you should get from this module

- understand what validations reveal about source-level issues
- know when to review mapping instead of editing golden records
- separate invalid values from structural mapping defects

![validations-result.png]({{ "/assets/images/integration/additional-operations/validations-result.png" | relative_url }})

## Guided walkthrough

Begin with the validations article. Stress the prerequisites: the dataset must be mapped to standard fields and open in edit mode. That alone teaches an important lesson: source-level review depends on semantic setup.

Walk the learner through the three validation modes:

- **Auto-validation** for a quick first pass
- **Manual validation** when the field needs a specific method or business logic
- **Advanced validation** when JavaScript-based logic is needed

Then explain how to read the results:

- which fields have invalid values
- how the status bars expose the valid/invalid split
- how filtering to invalid values turns the data set page into a targeted review surface

Now connect validations to review mapping. If a field is repeatedly invalid because the wrong source column was chosen, the issue is not "bad data cleaning". It is probably a mapping issue. Review mapping teaches the learner where to inspect:

- mapped properties
- business domain and vocabulary selection
- primary identifier and additional identifiers
- edge configuration if relationship behavior looks wrong

One of the best habits a steward can learn here is to write down whether an issue is **value-level**, **field-level**, or **identifier-level**. That tiny discipline dramatically improves architect handoffs.

## Role lens

The steward does not need to own mapping design, but they should become excellent at recognizing when validations are exposing a source problem versus a modeling problem. That is where stewardship adds value instead of just generating noise.

## Practice assignment

Take one training dataset and do the following:

1. Run auto-validation.
2. Identify one field with invalid values.
3. Filter to the invalid values and inspect the pattern.
4. Decide whether the likely remedy is:
   - direct value correction
   - source-data correction
   - mapping review
   - additional rule logic
5. Review the mapping and write a short escalation note if the issue looks structural.

## Exit criteria

- The learner can explain the difference between auto, manual, and advanced validation.
- The learner can isolate invalid values on a dataset page.
- The learner can decide when a validation outcome should trigger mapping review.

## Suggested source material

- [Validations](/integration/additional-operations-on-records/validations)
- [Review mapping](/integration/review-mapping)
