---
layout: cluedin
title: Capstone architecture review checklist
parent: Data Architect course
grand_parent: Learning paths
nav_order: 120
permalink: /learning-paths/data-architect-course/capstone-architecture-review
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The capstone asks the learner to think like the owner of a CluedIn implementation. Instead of learning one feature at a time, they review an end-to-end design and decide whether it will hold up for stewardship, governance, and consumption.

## What you should get from this module

- combine the course into one end-to-end architecture review
- use product behavior as evidence for design quality
- produce a practical improvement plan rather than a vague critique

![review-mapping-2.png]({{ "/assets/images/integration/data-sources/review-mapping-2.png" | relative_url }})

## Guided walkthrough

Choose one domain or dataset and conduct a full review across the platform.

### Semantic design
- Is the business domain clear?
- Is the vocabulary disciplined?
- Are key fields named in ways that support search and reuse?

### Identity and mapping
- Is the primary identifier safe?
- Are additional identifiers justified?
- Do mappings preserve enough information for stewardship and export?

### Record behavior
- Do processed records look understandable in search?
- Does History make the record lifecycle intelligible?
- Are duplicate or relation behaviors aligned with design intent?

### Remediation and governance
- Could stewards isolate common issues with filters, glossary, or tags?
- Are clean-project and rule paths obvious?
- Would Tag Monitoring or AI-assisted remediation produce useful queues?

### Consumption
- Does the stream design offer a clear downstream contract?
- Would consumers understand the impact of later merges, cleaning, or relation updates?

End with an improvement plan that distinguishes:
- immediate fixes
- near-term design changes
- steward enablement changes
- future automation opportunities

## Role lens

A complete architect is not the person who can configure the most features. It is the person who can look at a CluedIn implementation and explain whether it is coherent, teachable, governable, and safe to scale.

## Practice assignment

Write an architecture review memo for one domain with four sections:

1. What is working well
2. What is confusing or risky
3. What stewards would struggle with today
4. What you would change first and why

## Exit criteria

- The learner can assess an implementation end to end rather than feature by feature.
- The learner produces a concrete improvement plan.
- The learner can justify recommendations in operational as well as technical terms.

## Suggested source material

- [Golden records](/key-terms-and-features/golden-records)
- [Review mapping](/integration/review-mapping)
- [Vocabulary](/management/data-catalog/vocabulary)
- [Tag monitoring](/governance/tag-monitoring)
- [Stream data](/getting-started/data-streaming)
