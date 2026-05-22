---
layout: cluedin
title: Platform model: business domains, vocabularies, and golden records
parent: Data Architect course
grand_parent: Learning paths
nav_order: 20
permalink: /learning-paths/data-architect-course/platform-model-business-domains-vocabularies-and-golden-records
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Architecture in CluedIn starts with semantics. Before rules, streams, or AI, the architect needs a crisp model for what kinds of entities exist, how their metadata is named, and how multiple sources should converge into trustworthy golden records.

## What you should get from this module

- understand the conceptual model behind business domains, vocabularies, and golden records
- design modeling choices that make stewardship and consumption easier
- avoid weak semantic design that creates confusion later

![golden-record-4.png]({{ "/assets/images/key-terms-and-features/golden-record-4.png" | relative_url }})

## Guided walkthrough

Start with the golden-record documentation and the vocabulary documentation together. Explain the stack in business terms:

- **Business domain** expresses what the thing is.
- **Vocabulary** expresses how its metadata is organized.
- **Golden record** expresses the current trustworthy projection of that thing across sources and changes.

Architects need to make these three layers work together cleanly. Poor business-domain design leads to overbroad buckets that confuse search, filters, and relations. Poor vocabulary design leads to inconsistent naming, duplicated meanings, and weak downstream reuse.

Walk through the vocabulary page and discuss:
- naming and key-prefix discipline
- primary business domain assignment
- owners and accountability
- usage visibility across rules, glossary, and streams

Then return to the golden-record model and explain why the architecture matters operationally. If the domain and vocabulary are coherent, then search, saved searches, glossary, and streams become easier to use. If they are sloppy, the entire platform becomes harder to interpret.

Also introduce the idea that golden records are shaped over time by ingestion, clean projects, enrichers, deduplication, manual changes, and rules. The architect is designing not just the starting model, but the space in which those later interventions will behave.

## Role lens

The architect should treat semantics as infrastructure. Business domains and vocabularies are not decoration for the UI. They are the frame that makes mapping, governance, rule authoring, and downstream export consistent over time.

## Practice assignment

Take one real or example entity type and design:

- the business domain name
- the vocabulary name and key prefix
- five to ten high-value vocabulary keys
- the likely owners of the vocabulary
- two common stewardship questions this design should support in search or glossary

Then critique your own model: where could ambiguity or overlap still create problems?

## Exit criteria

- The learner can explain how business domains, vocabularies, and golden records fit together.
- The learner can propose a coherent vocabulary design with naming discipline.
- The learner understands how semantic design affects operations later.

## Suggested source material

- [Golden records](/key-terms-and-features/golden-records)
- [Vocabulary](/management/data-catalog/vocabulary)
