---
layout: cluedin
title: Use glossary, tags, and governance views to organize work
parent: Data Steward course
grand_parent: Learning paths
nav_order: 80
permalink: /learning-paths/data-steward-course/glossary-tags-and-governance
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

A steward eventually outgrows one-off searches. To operate at scale, they need stable ways to group work, label quality concerns, and monitor what is happening over time. In the current docs, glossary and tag monitoring are the strongest documented governance tools for this purpose.

## What you should get from this module

- use glossary terms to define reusable sets of records
- understand how tags surface quality problems operationally
- use governance views to turn individual issues into monitored queues

![tag_card.png]({{ "/assets/images/governance/tag-monitoring/monitor-tag-usage/Image/tag_card.png" | relative_url }})

## Guided walkthrough

First, teach glossary as a formalized reusable grouping tool. A glossary term is more than a saved search with a nicer name. It is a documented, reusable set of records that can support cleaning, downstream streaming, and governance conversations. Show how categories and terms create a shared language for groups like "North America customers" or "records pending quality review".

Next, teach tags as quality signals. Tags mark records with issues or states that matter operationally. The Tag Monitoring module then turns those tags into governance surfaces by showing:

- which tags are used
- how many records are flagged
- how that count changes over time
- which rules created the tags
- which records are currently affected

This is powerful because it changes stewardship from "I found a bad record" into "I am monitoring the volume and trajectory of a quality issue".

Also connect the module to clean projects and AI jobs. From Tag Monitoring, the steward can create a clean project for tagged records or use AI-assisted remediation where appropriate. That means tags are not just labels; they are launch points into action.

## Role lens

Glossary is best when the steward wants to name and reuse a meaningful population of records. Tags are best when the steward wants to signal a condition or issue that can be monitored, triaged, and reduced over time. Mature stewardship normally uses both.

## Practice assignment

Build one glossary term and review one tag-driven queue.

- Create a glossary category and term for a meaningful subset of records.
- Open Tag Monitoring and inspect one tag in detail.
- State which rule applies the tag, what fraction of records are affected, and whether the trend looks stable or worsening.
- Decide whether the next action should be a clean project, an AI job, or an architect escalation.

## Exit criteria

- The learner can explain the operational difference between glossary and tags.
- The learner can navigate Tag Monitoring and interpret what it shows.
- The learner can launch an appropriate remediation path from a tagged record set.

## Suggested source material

- [Work with glossary](/getting-started/glossary)
- [Tag monitoring](/governance/tag-monitoring)
