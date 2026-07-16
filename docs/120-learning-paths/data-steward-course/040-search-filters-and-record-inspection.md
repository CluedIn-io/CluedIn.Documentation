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

A steward who cannot isolate the right record set will either fix too little, fix too much, or fix the wrong thing. Search is therefore not a convenience feature for the steward. It is the primary operational lens for quality work.

![search-results-page-default.png]({{ "/assets/images/key-terms-and-features/search-results-page-default.png" | relative_url }})

## What this module teaches

By the end of this module, you should be able to:

- use search to find candidate records fast
- narrow scope using business domains and filters
- add the right columns to prove an issue exists
- save useful working views for repeated stewardship
- inspect individual records with a diagnostic mindset

## What search is really for

Search is not just for looking up one known record. For the steward, search serves four jobs:

- find one record and inspect it
- isolate a population of affected records
- compare patterns across records
- create reusable working sets through saved searches

That means the steward should think of search as an **operational workbench**.

## The search box

The search box lets you:

- enter keywords
- switch business domains
- reopen recent searches
- reopen saved searches

A strong steward uses business-domain selection early. If you know you are investigating the /Person domain, do not search across the entire instance unless you have a reason to.

![search-box.png]({{ "/assets/images/key-terms-and-features/search-box.png" | relative_url }})

## Business domain as a steward filter

If you choose the wrong domain or forget to limit scope, you can misread severity.

For example:

- a malformed phone problem in /Person may be serious
- the same pattern in a small auxiliary domain may not matter the same way

Always ask: “Which business object am I really stewarding?”

## The search results page

By default, the search results page shows basic columns such as name, business domain, and description. That is good for browsing, but not enough for quality work.

A steward should quickly customize the result view so that the suspected problem is visible directly in the table.

### Why add columns

You add columns so that the evidence becomes visible at list level rather than only record level.

Examples:

- add email, phone, country, or job title columns to inspect consistency
- add created or modified dates to spot suspicious recency patterns
- add vocabulary keys that help separate true defects from expected variants

![search-select-vocab-to-add-as-column.png]({{ "/assets/images/key-terms-and-features/search-select-vocab-to-add-as-column.png" | relative_url }})

## How a steward should think about filters

Filters define the exact subset of records you want to act on. In CluedIn, filters are used not only in search, but also in clean projects, streams, rules, and glossary terms. Learning filters well therefore pays off across the whole platform.

### Basic filter mode

Basic mode is good for broad narrowing by things such as business domains, providers, sources, and tags.

Use it when:

- you already know the provider or source causing trouble
- you want a fast first cut
- you want to compare tagged versus untagged records

### Advanced filter mode

Advanced mode is where the steward becomes powerful. It lets you filter by record properties, vocabulary keys, and glossary membership with explicit logic.

Use it when:

- you need precision
- you need to isolate malformed values
- you need to identify missing values
- you want a reusable working set for cleaning or monitoring

![filters-6.png]({{ "/assets/images/key-terms-and-features/filters-6.png" | relative_url }})

## Core filter ideas in plain language

A filter is made of:

- a property type
- an object
- an operation
- a value
- AND / OR logic between rules or groups

The steward does not need to memorize the whole reference. Instead, learn the common operational patterns:

- **Contains** for spotting a string or fragment
- **Equals** for exact values
- **Exists / Is Not Null** for completeness checks
- **Does Not Exist / Is Null** for missing-data queues
- **In** for small approved sets
- grouped logic for more precise issue definitions

## Saved searches

Saved searches are one of the most underused stewardship tools. A saved search captures not just a keyword, but an operationally useful configuration:

- the filters
- the columns
- the scope

Why this matters:

- recurring quality issues rarely happen only once
- saved searches let you reopen a defect queue instantly
- saved searches make your work reproducible and shareable

![save-a-search.png]({{ "/assets/images/key-terms-and-features/save-a-search.png" | relative_url }})

A good steward creates saved searches for:

- missing mandatory values
- invalid tags
- suspect source-specific populations
- records waiting for cleanup validation
- post-fix verification checks

## How to inspect a record after search narrows the set

After you isolate the right population, open a representative record and inspect it in this order:

1. **Overview / Properties** – what does the record currently say?
1. **History** – where did those values come from?
1. **Topology** – what structural changes shaped the record?
1. **Relations / Hierarchy** – is context affecting interpretation?
1. **Pending changes** if relevant – is something awaiting review?

The steward’s aim is not just to find a bad value. It is to understand the source and shape of the problem.

## Common search patterns every steward should know

### Pattern 1: find missing values

Use advanced filter logic to identify records where a required field does not exist or is null.

Useful for:

- completeness campaigns
- priority queues for business remediation
- tag creation later

### Pattern 2: find malformed values

Search for a known bad token or use tags / validations where available to narrow the set.

Useful for:

- typo cleanup
- invalid phone or email reviews
- source-specific formatting issues

### Pattern 3: find records from one risky source

Filter by provider or source and then add quality-relevant columns.

Useful for:

- intake triage
- proving that the issue belongs to one source branch
- identifying whether escalation belongs upstream

### Pattern 4: verify that a fix worked

Reopen the same saved search after the remediation and confirm that either:

- the record count went down
- the bad values disappeared
- only unresolved edge cases remain

## Common mistakes

### Mistake: using search as a one-record lookup only

This misses the bigger opportunity. Stewardship is usually about populations, not one-off examples.

### Mistake: editing before isolating scope

Never act before you know how many records are involved.

### Mistake: failing to add the right columns

If the problem is not visible in the table, you will make weaker decisions and slower reviews.

### Mistake: not saving useful searches

If you repeat the same investigation twice manually, you should probably have saved it.

## Practice exercise

Build one saved search that you would genuinely want as a steward.

Your saved search should include:

- a business domain limit
- at least one advanced filter
- at least two added columns that prove the issue
- a clear name that another steward could understand

Then open one record from the result set and document:

- what the visible issue is
- whether the issue seems source-specific or general
- what the likely next action is

## You are ready for the next module when

You can do all of the following without hesitation:

- narrow search to the right business domain
- add columns that make the issue visible
- build a filter precise enough to isolate a work queue
- save that search for reuse
- open one representative record and describe where you would inspect next

## What comes next

Next you will move one step earlier in the lifecycle and learn how to catch problems before they become harder to clean: validations and mapping checkpoints at dataset level.
