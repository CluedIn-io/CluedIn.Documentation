---
layout: cluedin
title: Rules, streams, glossary, and enrichers
parent: Data Architect course
grand_parent: Learning paths
permalink: /learning-paths/data-architect-course/rules-streams-glossary-and-enrichers
nav_order: 60
tags: ["learning-paths", "data-architect", "training"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This module turns recurring data issues into architecture work.

## Learning objective

Decide when a repeated stewardship problem should become a design, rule, stream, glossary, or enricher change.

## Working model

- **Steward discovers the pattern**.
- **Architect decides whether the pattern should be prevented by design**.
- **The product surface is chosen intentionally**: mapping, vocabulary, validation design, rule, stream, glossary, or enricher.

## Exercises

Classify each recurring problem into the most appropriate architecture surface:

1. Duplicate-looking people caused by weak identifiers.
1. Frequent missing values from one source system.
1. Reusable subset logic that many users need to apply.
1. A recurring downstream action that should happen automatically.

## Support surfaces to revisit

- [Filters](/key-terms-and-features/filters)
- [Validations](/integration/additional-operations-on-records/validations)
- [Vocabulary](/management/data-catalog/vocabulary)

## Completion signal

The learner can explain why not every quality problem should be solved manually by a steward.
