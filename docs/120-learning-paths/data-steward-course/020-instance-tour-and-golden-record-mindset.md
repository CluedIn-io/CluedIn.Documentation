---
layout: cluedin
title: First tour of the instance and the golden record mindset
parent: Data Steward course
grand_parent: Learning paths
nav_order: 20
permalink: /learning-paths/data-steward-course/instance-tour-and-golden-record-mindset
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

A Data Steward should not think of CluedIn as a database full of rows. CluedIn is a system for building, improving, and governing trusted golden records from multiple contributing sources. This module teaches you how to move through the instance and how to interpret the golden record as the center of stewardship work.

![golden-record-5.png]({{ "/assets/images/key-terms-and-features/golden-record-5.png" | relative_url }})

## What this module teaches

By the end of this module, you should be able to:

- explain what a golden record is
- distinguish source records, data parts, and golden records
- understand why history and topology matter to stewards
- perform a basic tour of the instance with the right mental model

## The most important concept in CluedIn: the golden record

A golden record is the trusted representation of a data subject such as a person, organization, or product. It is not just one row copied from one source. It is a consolidated projection built from one or more contributions.

In practice, this means:

- one golden record may be influenced by multiple sources
- those sources may disagree
- CluedIn must decide which values win
- steward actions can reshape the golden record over time

If you only look at the current values and never ask where they came from, you will make weak decisions. The golden record mindset is: **current value plus lineage plus contributing sources plus operational impact**.

## Source record, data part, golden record

To steward well, you need three layers clear in your head.

### Source record

This is the raw record as it arrived from a file, database, pipeline, crawler, or other source. It has not yet become a trusted business object.

Think of it as “what the source said.”

### Data part

After mapping and pre-processing, the source record becomes a data part in a shape CluedIn understands. A data part is a processed contribution from a single origin or operational action.

Think of it as “what one branch contributes.”

### Golden record

The golden record is the business-facing representation that combines contributions from one or more data parts.

Think of it as “what the platform currently trusts.”

## Why stewards must care about data parts

When a value looks wrong on a golden record, the wrongness may come from several places:

- the source sent a bad value
- the mapping turned a source field into the wrong meaning
- a more recent but lower-quality value won
- a clean project or manual change introduced a value
- a duplicate merge combined conflicting records
- an enrichment or rule changed the value

That is why good stewardship is not just editing cells. It is understanding which branch or process caused the visible result.

## Default survivorship in plain language

When multiple contributing branches provide different values for the same property, CluedIn needs a winner. By default, manually added changes are prioritized; otherwise, the most recent value wins.

A steward should remember two things:

1. the “visible” value is not necessarily the “best” value
1. a newer value can still be operationally worse than an older one

This is one of the main reasons stewards escalate recurring issues to architects. If the wrong source keeps winning, the platform may need survivorship or rule changes.

## First tour of the instance

Do not try to memorize every screen. Learn what each major area is *for*.

### Ingestion

Use this area when you need to inspect where data came from, how it was mapped, whether validations were applied, and whether a dataset was processed.

### Search

Use this area to find record sets, narrow them with filters, save your working views, and decide what needs attention.

### Golden record page

Use this page when you need to inspect one record closely. This is where you confirm what the record currently looks like.

### History

Use this when you need to answer, “Why does this record have this value?” History shows data parts, branches, sources, and changes over time.

![history-1.png]({{ "/assets/images/key-terms-and-features/history-1.png" | relative_url }})

### Topology

Use this when you want a more visual understanding of how the record is composed and how operations such as merges changed its structure.

### Clean

Use this when you need to fix a repeated issue across a controlled set of records.

### Deduplication

Use this when similar records need to be reviewed and merged safely.

### Glossary and Governance

Use these when you need named sets of records, tags, monitoring views, and prioritization surfaces.

### AI agents

Use these when you want automation, but only after you understand the data scope, the instruction quality, and the expected result.

## How to read a golden record page like a steward

A weak steward opens a record and asks, “Is this wrong?” A strong steward asks:

- What business domain is this record in?
- Which properties look authoritative and which look suspicious?
- Are the suspicious values isolated or repeated across many records?
- Does the History page show the same source or process causing the issue repeatedly?
- Is this a manual fix, a clean-project fix, a deduplication problem, or a platform-design issue?

The golden record page is not just for viewing. It is the starting point for a diagnostic path.

## The difference between current truth and explainable truth

A record can look correct and still be poorly governed. It can also look wrong but be easy to explain and fix.

Stewards should optimize for **explainable trust**:

- you can identify where the value came from
- you can describe why it won
- you can explain how it could be corrected
- you can estimate who else is affected

If you cannot explain those four things, keep investigating.

## What “good” looks like for a steward on this module

By the end of an investigation, you should be able to say something like:

> This person record is built from two contributing sources. The visible phone number comes from the most recent branch, but the branch is unreliable because validation failures are common in that source. The correct next action is to isolate all records from that source with invalid phones, tag them, and review whether the issue should be fixed through validations, clean-up, or a source-side correction.

That is stewardship. It is not random clicking.

## Practice exercise

Choose one golden record in a safe business domain and inspect it.

Write down:

- the business domain
- two properties that look trustworthy
- one property that looks suspicious or hard to explain
- which source or branch seems to influence it
- what additional evidence you would need before making a change

## You are ready for the next module when

You can clearly explain:

- what the difference is between source record, data part, and golden record
- why a steward must use History and not only the Properties tab
- why the same visible value can require different remediation paths depending on its origin

## What comes next

Next you will learn how data reaches this point in the first place. Even though a steward is not the primary owner of ingestion design, a good steward understands how importing, mapping, identifiers, and processing decisions create the conditions for later quality work.
