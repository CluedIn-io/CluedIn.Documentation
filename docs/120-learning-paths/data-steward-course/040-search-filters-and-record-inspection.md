---
layout: cluedin
title: Find and inspect records with search, filters, and saved searches
parent: Data Steward course
grand_parent: Learning paths
nav_order: 40
permalink: /learning-paths/data-steward-course/search-filters-and-record-inspection
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Search is the steward's home base. The platform only becomes manageable when the learner can isolate the right slice of records quickly, add the right columns, save investigative views, and move from list-level symptoms to record-level evidence.

## What you should get from this module

- use search, column options, and filters to isolate target records
- save reusable investigation views for recurring data quality work
- move from a search result set into a reliable record inspection workflow

![search-results-page-default.png]({{ "/assets/images/key-terms-and-features/search-results-page-default.png" | relative_url }})

## Guided walkthrough

Start with the search box and the default results page. Explain that the default table is intentionally simple. The steward's job is to shape it into an investigation surface.

### Search box
Teach the learner to search by a distinctive value first: an email, code, unusual name, or tag. Then show recent searches and saved searches as productivity tools rather than convenience features.

### Column options
This is where stewardship becomes practical. Add the vocabulary keys and properties that make the problem visible. A good steward does not repeatedly open each record one by one if the issue can be exposed in the table.

### Basic and advanced filters
Use basic filters when the operational question is broad, such as narrowing to a domain, provider, source, or tag. Use advanced filters when the question depends on a property or vocabulary value. Teach the learner that advanced filters are not just search constraints; they are the entry point to saved searches, clean projects, glossary logic, and many governance workflows.

### Saved searches
A saved search is a repeatable stewardship view. Show the learner how to save the configuration once they have the right columns and filters, then reuse it later to verify whether remediation worked.

### Record inspection
From the results page, open a record and inspect:

- overview and visible properties
- history if the value looks surprising
- relations if context matters
- topology if a merge or consolidation is suspected

This module should feel like detective work. The learner is building a case, not just retrieving rows.

## Role lens

A mature steward builds a small library of saved searches around common issue types: missing required values, suspicious tags, recently changed records, duplicates under review, or records within a glossary term. That turns reactive work into an operational routine.

## Practice assignment

Create three saved searches in your training domain:

1. A search for records with an obvious missing or suspicious value.
2. A search for records belonging to one business domain with one extra vocabulary column added.
3. A search targeted by a tag or advanced vocabulary filter.

For each saved search, state what operational question it answers and how you would know that the issue is fixed.

## Exit criteria

- The learner can add useful columns instead of relying on the default table.
- The learner can use advanced filters confidently.
- The learner can create and reuse saved searches for recurring work.

## Suggested source material

- [Search](/key-terms-and-features/search)
- [Filters](/key-terms-and-features/filters)
- [Golden records](/key-terms-and-features/golden-records)
- [History](/key-terms-and-features/golden-records/history)
