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

Everything a steward does makes more sense once they understand that CluedIn is not just storing raw records. It is turning raw source records into data parts and then projecting a trustworthy golden record that can change over time as new data, fixes, merges, or enrichments arrive.

## What you should get from this module

- understand the source record -> data part -> golden record progression
- learn where to look in the UI for each stage of the data lifecycle
- see why stewardship work must account for history and topology, not just current values

![golden-record-5.png]({{ "/assets/images/key-terms-and-features/golden-record-5.png" | relative_url }})

## Guided walkthrough

Use the golden-record documentation as the conceptual spine for this module. Walk through the three layers slowly:

### Source record
This is the raw record as CluedIn received it. A steward usually sees source-level behavior when inspecting datasets during ingestion, validations, or mapping review.

### Data part
This is the mapped and processed contribution from a source or change event. Clean projects, enrichers, deduplication, manual edits, and ingestion can all create or modify data parts.

### Golden record
This is the current operational view that users search and consume. It is a projection over contributing data parts, not a frozen object.

Now take the learner through the major UI surfaces they will use most often:

- **Ingestion** for understanding what entered the platform
- **Search** for finding operational records
- **Golden record pages** for reading current state
- **History** for understanding how the state was formed
- **Topology** for visualizing contributing parts and merge context
- **Governance** and **Management** surfaces for structured remediation paths

The critical teaching point is this: the current value on a record page is not the whole story. If a steward only looks at the current value, they miss whether the issue came from a source update, a clean project, a merge, or another contributing branch. The History page exists precisely to answer that question.

Also explain the idea of survivorship in simple language. Even when two sources disagree, CluedIn chooses an operational value. A steward does not need to author survivorship rules in this module, but they must learn that the winning value may reflect recency or manual intervention rather than universal truth.

## Role lens

The steward should leave this module with a healthy suspicion of surface appearances. The job is not to trust the visible record blindly. The job is to verify whether the visible record is justified by the contributing evidence and the platform's current rules.

## Practice assignment

Open a few records in your training domain and do the following for each one:

1. View the record from search results.
2. Open the golden record page and inspect the visible properties.
3. Open **History** and identify at least two contributing data parts or branches.
4. Explain which source or change path most likely produced the current visible value for one important property.
5. Open **Topology** if available and note whether the record has been shaped by merges or later interventions.

Repeat until the learner can narrate the life of a record rather than just describe its final screen.

## Exit criteria

- The learner can explain the difference between source records, data parts, and golden records.
- The learner can name the main UI surfaces used to investigate record quality.
- The learner understands why History and Topology matter in stewardship.

## Suggested source material

- [Golden records](/key-terms-and-features/golden-records)
- [History](/key-terms-and-features/golden-records/history)
