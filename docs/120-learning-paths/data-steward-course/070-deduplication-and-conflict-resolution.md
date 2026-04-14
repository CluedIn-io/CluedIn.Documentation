---
layout: cluedin
title: Resolve duplicates and understand merge decisions
parent: Data Steward course
grand_parent: Learning paths
nav_order: 70
permalink: /learning-paths/data-steward-course/deduplication-and-conflict-resolution
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Deduplication is one of the most visible stewardship workflows in CluedIn because it forces the learner to compare records, interpret conflict sets, and make explicit merge decisions. It is also where weak identifiers and poor modeling become painfully obvious.

## What you should get from this module

- understand the difference between identifier-based merges and deduplication projects
- review duplicate groups and resolve conflicts carefully
- recognize when deduplication symptoms point to architectural issues

![dedup-9.png]({{ "/assets/images/getting-started/deduplication/dedup-9.png" | relative_url }})

## Guided walkthrough

Begin by contrasting two mechanisms:

- records can merge during processing because identifiers match exactly
- records can be grouped into a deduplication project because a fuzzy match rule suggests they are duplicates

That distinction matters. A steward should not assume every duplicate-looking problem belongs in deduplication. Sometimes the real issue is a poor identifier strategy upstream.

Now walk through the documented deduplication flow:

1. create the project
2. define the business domain scope
3. add matching rules and criteria
4. generate results
5. inspect duplicate groups
6. fix conflicts and preview the merge
7. approve and merge

The key teaching point is not the clicking sequence. It is the review discipline. When looking at a duplicate group, the steward should ask:

- are these truly the same real-world entity?
- which fields are in conflict and which are consistent?
- would merging these records collapse distinct entities accidentally?
- is this a one-off resolution or evidence that identifiers or mappings need redesign?

Also connect deduplication back to record inspection. After a merge, the steward should understand that History and Topology become even more important because the record's current form now depends on additional data parts and merge actions.

## Role lens

A strong steward is conservative with merges. The damage from a false merge is usually worse than the inconvenience of a duplicate group staying unresolved a bit longer. Good stewards merge with evidence, not optimism.

## Practice assignment

Create or review a deduplication project in a training domain.

- Examine one duplicate group.
- List the fields that make the records look similar.
- List the fields that create doubt.
- Document your decision to merge or not merge.
- After the merge, open the resulting record and inspect its History or Topology.

Then state whether the project exposed a recurring architectural issue, such as weak identifiers or bad source harmonization.

## Exit criteria

- The learner can explain the difference between exact identifier merges and fuzzy deduplication work.
- The learner can review a duplicate group and justify a merge decision.
- The learner knows when to escalate duplicate patterns as architectural issues.

## Suggested source material

- [Deduplicate data](/getting-started/data-deduplication)
- [Review mapping](/integration/review-mapping)
- [History](/key-terms-and-features/golden-records/history)
