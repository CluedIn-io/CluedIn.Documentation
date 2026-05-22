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

Stewards are not usually the primary owners of mapping design, but they absolutely need literacy in ingestion, mapping, and processing. Many downstream quality problems are caused long before the steward sees them on the search page.

## What you should get from this module

- understand the basic ingestion flow from file or source to searchable records
- recognize which mapping decisions create downstream stewardship pain
- learn what to escalate when a record problem is rooted in ingestion design

![create-mapping-7.png]({{ "/assets/images/getting-started/data-ingestion/create-mapping-7.png" | relative_url }})

## Guided walkthrough

Follow the "Ingest data" guide end to end, but keep the explanation role-specific.

### Import
Data enters via files or other sources. At this stage, the steward mainly cares that the data is present and inspectable.

### Map
Mapping is where source columns are translated into the language CluedIn understands. This is a huge stewardship concern because incorrect mapping can make quality work harder in several ways:

- a meaningful field might be ignored
- the wrong data type might be assigned
- a business domain might be too broad or too narrow
- the wrong primary identifier might merge records that should stay separate
- poor preview naming or descriptions can make search and review harder

### Process
Processing turns mapped records into searchable golden records. This is where identifier behavior starts to matter in a very visible way. If there are duplicates in the primary identifier, records can be merged during processing before the steward ever reaches deduplication.

Teach the learner to review processed outcomes with two questions in mind:

1. Do the records look complete enough to review?
2. Do they look distinct enough to trust?

If the answer to either question is no, the steward should not just start fixing symptoms. They should note whether the problem likely comes from missing mapping, weak identifiers, or poor preprocessing.

This is also a good place to teach one key handoff pattern. When you escalate a mapping concern, do not just say "the data looks wrong". Say something more like: "In domain X, values from source column Y appear to be mapped inconsistently, and search results are missing the field we need to review the issue." That kind of feedback is actionable.

## Role lens

For the steward, ingestion literacy is about evidence, not ownership. You need enough knowledge of the ingestion flow to distinguish between:

- a bad source value
- a bad mapping decision
- a problem introduced after processing

That distinction determines whether you fix, monitor, or escalate.

## Practice assignment

Use a training dataset and walk through import, mapping preview, and processing. Then answer:

- Which field appears to be the best display name for a steward to inspect?
- Which field is acting as the primary identifier?
- If the primary identifier were wrong, what type of visible problem would you expect after processing?
- Which fields would make stewardship easier if they were exposed in search columns?

## Exit criteria

- The learner can describe the import, map, and process flow.
- The learner can identify at least three mapping decisions that affect downstream stewardship.
- The learner can frame a mapping escalation in clear operational terms.

## Suggested source material

- [Ingest data](/getting-started/data-ingestion)
- [Review mapping](/integration/review-mapping)
