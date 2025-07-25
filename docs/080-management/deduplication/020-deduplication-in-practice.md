---
layout: cluedin
nav_order: 2
parent: Deduplication
grand_parent: Management
permalink: /management/deduplication/deduplication-in-practice
title: Deduplication in practice
---

In this article, you'll discover various strategies on how to efficiently deduplicate large data sets in CluedIn.

Let's start with the video, which shows a real-life scenario for deduplicating 100 thousand records.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/910767689?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" title="Deduplication in practice"></iframe>
</div>

To enhance the efficiency of your deduplication project and to be able to smoothly revert merges, we recommend that you follow these guidelines.

![dedup-checklist.gif]({{ "/assets/images/management/deduplication/dedup-checklist.gif" | relative_url }})

When you need to run a deduplication project on a large set of data, we recommend that you **start small** and limit the size of data. This approach allows you to to verify the accuracy and efficiency of your matching rules before applying them to the entire data set. If the deduplication result doesn't meet your expectations, you can easily and quickly revert changes and start again.

When it comes to matching rules, our recommendation is to create **separate projects for strict and fuzzy matching functions, grouped by domain**. There are two reasons for this recommendation:

- Quick and efficient merging and unmerging. If all rules are consolidated within a single project and you decide to revert changes, all rules will be reverted, even those that were executed correctly. To prevent this, create separate projects for individual sets of rules. This way, you can selectively revert only those projects where rules didn't work as intended.

- Streamlined management of projects on a day-to-day basis. If you have projects targeting a specific domain, and the data for that domain has been updated, then you can easily re-evaluate those specific projects. For example, suppose you have one project that merges duplicates based on first and last names and another project that merges duplicates based on addresses. Now, you add the libpostal library to enrich addresses. In this scenario, you can easily re-evaluate only the address-based project, knowing that first and last names have remained unchanged.

To increase the efficiency of your deduplication projects, start by running projects with **strict equality matching functions** to eliminate obvious duplicates.

Once you've reached a state with no duplicates based on equality matching, proceed to execute projects with **fuzzy matching functions** for a more nuanced deduplication process. Since you've already merged some records based on equality matching functions, this means that you now have fewer duplicates in the system, so fuzzy matching would run much faster.

Finally, when you achieve the desired outcome on a small data set, **grow big** and proceed to run the deduplication project on the entire data set.