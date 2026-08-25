---
layout: cluedin
title: Rules, clean projects, and processing logic
parent: Data Architect course
grand_parent: Learning paths
nav_order: 60
permalink: /learning-paths/data-architect-course/rules-clean-projects-and-processing-logic
---

## Learning outcome

Choose the correct layer for repeatable data logic and define how it is tested, processed, and reversed.

## Scenario

Stewards repeatedly correct the same pattern. You need to decide whether the durable solution belongs in the source, validation, clean workflow, generated rule, or architect-owned rule.

## Read

- [Create rules](/getting-started/rule-builder)
- [Manage a clean project](/preparation/clean/manage-clean-project)
- [Validations](/integration/additional-operations-on-records/validations)

## Exercise

1. Choose one recurring quality issue from a steward workflow.
2. Compare source correction, validation, clean project, generated rule, and architect-authored rule as possible owners of the logic.
3. Select one approach and document why it is the lightest durable option.
4. Define the population it affects and whether reprocessing is required.
5. Test the logic in a safe environment and inspect sample records afterward.
6. Document how the change can be disabled, reverted, or mitigated.

## Deliverable

A processing-logic decision record with ownership, scope, timing, validation evidence, and reversibility.

## Complete when

- The selected mechanism matches the problem's repeatability and ownership.
- Processing implications are explicit.
- The result is verified on actual records, not only in configuration.

## Next

Design deduplication and glossary structures that stewards can operate confidently.
