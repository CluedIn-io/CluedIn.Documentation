---
layout: cluedin
title: Deduplication, glossary, and stewardship enablement
parent: Data Architect course
grand_parent: Learning paths
nav_order: 70
permalink: /learning-paths/data-architect-course/deduplication-glossary-and-stewardship-enablement
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Architects often underestimate how much their work determines whether stewardship can scale. This module focuses on the features that directly shape that operating scale: deduplication design, glossary structure, and the quality of handoffs into steward workflows.

## What you should get from this module

- design deduplication in a way that stewards can review confidently
- use glossary as a structured operating artifact, not just a label store
- build features in ways that reduce stewardship friction

![create-term-1.png]({{ "/assets/images/getting-started/glossary/create-term-1.png" | relative_url }})

## Guided walkthrough

Use the deduplication and glossary guides together. They reveal two complementary design responsibilities.

### Deduplication
Architects should think about deduplication before stewards ever open a duplicate group. Matching rules, vocabulary quality, and identifier strategy determine whether duplicate groups are meaningful or noisy. The better the semantic model and identifiers, the better the deduplication projects.

### Glossary
Glossary terms turn useful populations into reusable named artifacts. Architects should care because glossary can become a durable bridge between modeling and operations. A good glossary term helps stewards find the same population repeatedly, helps streams target the right records, and gives shared names to governed subsets.

### Stewardship enablement
Now tie both features back to stewardship:
- Are duplicate groups explainable?
- Are glossary terms aligned with actual operational questions?
- Can stewards move from glossary or tag queues into clean projects or AI jobs cleanly?
- Are the fields surfaced in those flows sufficient for confident review?

The architectural challenge is not just enabling features. It is enabling them in a way that produces a trustworthy and teachable operating model.

## Role lens

A good architect makes stewardship less improvisational. The right deduplication design and glossary structure turn messy operational work into a guided workflow.

## Practice assignment

Design one stewardship enablement package for a domain:

- a deduplication strategy
- a glossary category and term design
- the search columns stewards should use
- the tags or rules that should signal quality issues
- the likely escalation points back to architecture

## Exit criteria

- The learner understands how architecture affects deduplication quality.
- The learner can position glossary as an operating artifact.
- The learner can design for stewardship usability, not only platform correctness.

## Suggested source material

- [Deduplicate data](/getting-started/data-deduplication)
- [Work with glossary](/getting-started/glossary)
