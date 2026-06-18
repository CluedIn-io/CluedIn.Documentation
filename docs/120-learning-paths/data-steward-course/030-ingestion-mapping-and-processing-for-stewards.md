---
layout: cluedin
title: How ingestion, mapping, and processing affect stewardship
parent: Data Steward course
grand_parent: Learning paths
nav_order: 30
permalink: /learning-paths/data-steward-course/ingestion-mapping-and-processing-for-stewards
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

A steward does not need to become an integration engineer, but a steward does need to understand the chain that turns incoming data into searchable golden records. Many downstream quality issues are born during ingestion, mapping, identifier selection, or processing. This module teaches you enough to diagnose those problems accurately.

![create-mapping-7.png]({{ "/assets/images/getting-started/data-ingestion/create-mapping-7.png" | relative_url }})

## What this module teaches

By the end of this module, you should be able to:

- explain the three major ingestion phases: import, map, process
- understand what mapping adds to raw data
- understand why identifiers matter to stewardship
- spot the difference between a source-quality issue and a mapping-design issue
- know what evidence to gather before escalating ingestion problems

## The three phases of ingestion in simple language

### 1. Import

The data arrives in CluedIn. At this point it can be viewed, but it is not yet part of trusted operational work.

A key steward insight: imported data is not automatically ready for quality work. If it has not been mapped and processed, search will not behave as a learner might expect.

### 2. Map

Mapping gives semantic meaning to fields. It tells CluedIn which fields correspond to business meaning, vocabulary keys, display behavior, dates, identifiers, and relationships.

A key steward insight: many bad outcomes are not “bad data,” but “bad meaning assignment.”

### 3. Process

Processing turns mapped data into data parts and golden records, merging by identifiers where appropriate and making the results searchable and operational.

A key steward insight: after processing, problems become visible in golden-record form, but their root cause may still live in source data or mapping design.

## What mapping actually does

New stewards often think mapping is just column renaming. It is much more than that.

Mapping defines:

- the business domain
- the vocabulary used
- the primary identifier
- other identifiers
- how fields become recognizable CluedIn properties
- whether records can link to other records through relations
- whether source data will generate healthy or unhealthy golden records

That means mapping quality directly affects later stewardship quality.

## Business domain and vocabulary in steward terms

### Business domain

The business domain tells CluedIn what type of thing the record is. A steward cares because domains shape search scope, governance scope, and the meaning of a record.

If a person-like dataset is mapped into the wrong business domain, every downstream activity becomes harder to interpret.

### Vocabulary

Vocabulary gives a structured, consistent language for metadata. A steward cares because search columns, clean projects, glossary terms, rules, exports, and AI jobs all depend on usable vocabulary keys.

If key names are confusing or inconsistent, stewardship becomes slower and less reliable.

## The most important ingestion concept for a steward: identifiers

Identifiers are central to trust. If identifier strategy is weak, records that should merge may stay separate, and records that should stay separate may merge.

### Primary identifier

The primary identifier is the main unique representation for a record. If two records share the same primary identifier, they can merge.

A steward should know:

- a good primary identifier reduces later duplicate work
- a bad primary identifier can create incorrect automatic merges
- an auto-generated key may avoid bad merges but increases the chance of duplicates that must be handled later

### Additional identifiers

Additional identifiers can also cause records to merge when they match.

A steward should know:

- additional identifiers can be useful
- they can also be risky if the field is not actually reliable
- suspicious merges should prompt questions about both primary and additional identifiers

## How mapping review helps a steward

Even when the architect owns mapping design, the steward should know what to inspect in a mapping review:

- Are the right columns mapped to the right vocabulary keys?
- Does the chosen display behavior make records understandable in search?
- Is the primary identifier truly unique?
- Are additional identifiers helpful or risky?
- Are relationships being added from the right source fields?
- Are any fields ignored that should actually be visible for quality work?

This is why mapping review is not “architecture-only.” It is a steward diagnostic skill.

## Common stewardship symptoms that point to ingestion or mapping issues

### Symptom: records are missing from search

Possible causes:

- data imported but not processed
- wrong business domain assumptions
- wrong saved search or filter scope

### Symptom: records merged in suspicious ways

Possible causes:

- primary identifier not unique
- additional identifiers too aggressive
- source data duplication upstream

### Symptom: columns or values are hard to interpret in search

Possible causes:

- vocabulary keys poorly chosen
- wrong data types
- missing or weak display fields

### Symptom: relations do not appear as expected

Possible causes:

- edge relations not configured
- relation configuration incomplete
- records not reprocessed after mapping changes

### Symptom: clean-up keeps addressing the same issue source after source

Possible causes:

- source system problem
- mapping transformation missing
- lack of validation or normalization earlier in the pipeline

## Processing in steward language

Processing is the step that makes the data operational in CluedIn.

When processing happens:

- mapped records become data parts
- data parts are evaluated against identifiers
- new golden records are created or existing ones are updated
- records become searchable and available for quality work

A steward should remember that processing is a **shape change** in operational visibility. Before processing, you mainly have incoming data. After processing, you have stewardable business objects.

## What to inspect on the dataset page

When reviewing a dataset, a steward should look for:

- whether the dataset is processed
- whether mapping exists
- what the current mapping says about business domain and vocabulary
- whether the primary identifier looks safe
- whether the preview reveals obvious field-quality problems
- whether validations are present or missing
- whether the source seems likely to create duplicate or malformed records

## Red flags that deserve escalation

Escalate to the Data Architect when you see patterns such as:

- the chosen identifier would merge large numbers of unrelated records
- the visible record name or description is derived from weak fields
- mapped fields do not reflect business meaning
- a relationship depends on a field that is not stable
- the same source repeatedly produces quality issues that should be normalized earlier
- a vocabulary design makes stewardship harder rather than easier

## What not to do as a steward

Do not treat every ingestion issue as something to fix with clean projects. Clean projects are valuable, but they are not a substitute for correct identifiers, correct mapping, or correct source-side handling.

A useful rule is:

- use stewardship tools to fix today’s damaged operational set
- escalate design flaws so tomorrow’s records arrive better shaped

## Practice exercise

Find one dataset and answer the following:

- What is the business domain?
- What vocabulary is used?
- What is the primary identifier?
- Does the identifier appear safe?
- If the identifier failed, what symptom would you expect in search or deduplication?
- Which fields would be most important to a steward during later remediation?

## You are ready for the next module when

You can explain:

- how imported data differs from processed data
- why mapping is more than field renaming
- why identifier strategy matters to stewardship
- which symptoms suggest an ingestion or mapping issue rather than a clean-up issue

## What comes next

Now that you understand how records arrive, you are ready to learn the most practical day-to-day steward skill: finding the right records fast. The next module covers search, filters, saved searches, and record inspection.
