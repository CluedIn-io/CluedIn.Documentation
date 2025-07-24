---
layout: cluedin
nav_order: 1
parent: Deduplication
grand_parent: Management
permalink: {{ site.baseurl }}/management/deduplication/concept-of-deduplication
title: Concept of deduplication
---

Let's explore the concept of deduplication in CluedIn through an example. We have three duplicate records—_Person 1_, _Person 2_, and _Person 3_. How do we merge these three records into a single, consolidated golden record?

![dedup-concept.png](../../assets/images/management/deduplication/dedup-concept.png)

Note that the email is the same for _Person 1_ and _Person 2_, but different for _Person 3_.

To begin with, we need to set up matching rules in the deduplication project: one rule to check for the same email and the other rule to check for the same first name and last name. Records meeting the criteria of either the first or second rule will be selected as possible duplicates.

When you generate matches in the deduplication project, _Person 1_ and _Person 2_ are selected as possible duplicates because they have the same email address. At this point, the second rule did not identify any duplicates because the three records have different first and last names. When reviewing the group of duplicates, you have to choose the appropriate values among conflicting values. In this case, the conflicting values would be first name and last name. After merging, the duplicates result in a merged golden record—_Merged Person 1 and 2_—which combines consolidated and complete information.

{:.important}
Merging does not create a new golden record; instead, it uses one of the duplicate records as a base and aggregates data from the others to form a comprehensive golden record.

![dedup-concept-1.gif](../../assets/images/management/deduplication/dedup-concept-1.gif)

Now, after the first run of the deduplication project, we have two duplicate records: _Merged Person 1 and 2_ and _Person 3_. When a merged golden record appears, the rules that led to the merge need to be re-evaluated. It means that you need to generate matches in the deduplication project again. This time, the second rule comes into play: _Merged Person 1 and 2_ and _Person 3_ are selected as possible duplicates because they have the same first and last names. However, the email is identified as a conflicting value, so you have to choose the appropriate email for the merged golden record. After merging, the duplicates result in a merged golden record—_Merged Person 1, 2, 3_—with consolidated and complete information.

![dedup-concept-2.gif](../../assets/images/management/deduplication/dedup-concept-2.gif)

{:.important}
Every time golden records are merged, it is crucial to re-evaluate them, as they may contain new information. This new information may align with criteria from matching rules, potentially making golden records eligible for subsequent merges.

Essentially, each merging operation has the potential to produce golden records that could initiate further iterations of the merging process. This is why deduplication can be a somewhat time-consuming process, requiring multiple runs until no duplicates are identified, ensuring a comprehensive consolidation of data.