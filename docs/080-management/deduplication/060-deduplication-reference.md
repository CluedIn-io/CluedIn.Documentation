---
layout: cluedin
nav_order: 6
parent: Deduplication
grand_parent: Management
permalink: /management/deduplication/deduplication-reference
title: Deduplication reference
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will find reference information to help you understand matching rules and functions, deduplication project statuses, and group statuses.

## Matching rules

Matching rules allow you to set up complex logic for detecting duplicates. In the deduplication project, matching rules are combined using the **OR** logical operator, while matching criteria within a rule are combined using the **AND** logical operator. So, if you want a record to be identified as a duplicate if it meets at least one of your criteria, then you need a separate rule for each criteria. On the other hand, if you want a record to be identified as a duplicate if it meets all of your criteria, then you need one rule that includes all of your criteria.

For example, in the following configuration, either records with the same email address or records with the same first and last name are identified as duplicates.

![rules.png](../../assets/images/management/deduplication/rules.png)

## Matching functions

The following table provides the description of methods used for detecting duplicates.

| Function | Description |
|--|--|
| Equals | Identifies records as duplicates if two values are the same. |
| Fuzzy match - Sift4 | Detects approximate duplicates using a string similarity algorithm. This algorithm takes into account the number of matching characters and the transpositions (swaps) needed to make the strings identical. For example, 'algorithm' and 'algorrithm' would be identified as fuzzy matches.<br> In this method, you have to specify the threshold— a parameter that sets the maximum number of characters by which two strings can differ and still be considered a match.   |
| Fuzzy match - phonetic, DoubleMetaphone | Detects approximate duplicates using a phonetic matching algorithm. This algorithm encodes words into a phonetic representation, allowing for matching based on pronunciation rather than spelling. For example, 'night' and 'knight' would be identified as fuzzy matches.  |
| Contains | Matches two values if one contains the other. |
| Starts with | Matches two values if one starts with the other. |
| Ends with | Matches two values if one ends with the other. |
| First token equals | Extracts the first word from both values and compares for exact match ignoring casing. |
| Email | Matches two email address values if the are semantically equal. |

## Deduplication project

This section contains reference information about deduplication project statuses.

### Project statuses

The following table provides descriptions of deduplication project statuses.

| Status | Description |
|--|--|
| Requires configuration | The deduplication project has been created, no matching rules have been added yet. |
| Ready to generate | The deduplication project has been configured, no results have been generated yet. This status also appears when you discard the results at any further stage of the project.|
| Generating | CluedIn is analyzing the specified set of golden records with the aim to detect duplicates based on your matching rules. |
| Aborting generation | The process of generating the results of the deduplication project is being cancelled. The status will shortly change to **Ready to generate**. |
| Ready for review | CluedIn has generated the results of the deduplication project, you can start [processing groups of duplicates](/management/deduplication/manage-groups-of-duplicates). |
| Committing | CluedIn is merging records from selected groups. This status is applicable whether you are merging a single group, multiple groups, or all groups in the project. |
| Merged | CluedIn has merged records from all groups in the project. If the project contains groups that were not selected for merge, the project status remain **Ready for review**. |
| Unmerging | CluedIn is reverting the results of merge. When records are unmerged, the project status becomes **Ready for review**. |
| Abort unmerging | The process of reverting changes is being cancelled. The status will shortly change to **Ready to generate**. |

### Project status workflow

The following diagram shows the deduplication project workflow along with its statuses and main activities.

![dedup-project-status-workflow.gif](../../assets/images/management/deduplication/dedup-project-status-workflow.gif)

## Group of duplicates

This section contains reference information about the statuses of a group of duplicates.

### Group statuses

The following table provides descriptions of the statuses of groups of duplicates.

| Status | Description |
|--|--|
| New | The group with potential duplicates has been generated. This status is also applicable when you revoke the group's approval. |
| Approved | The group has been approved and it is ready for merge. If you change your mind, you can reject the group. If you are uncertain about the selection of values in the group, you can revoke your approval and start processing the group from scratch. |
| Rejected | The group has been rejected and it cannot be merged. If you change your mind, you can approve the group. |
| Merge Committed | The group has been merged. When all groups in the project have this status, the status of the project becomes **Merged**. If you are not satisfied with the merged golden record, you can revert the changes by unmerging the records.  |
| Unmerged | The changes made to the golden record through merging have been reverted, restoring duplicate records to their previous state before the merge. |

### Group status workflow

The following diagram shows the group of duplicates workflow along with its statuses and main activities.

![group-of-duplicates-status-workflow.gif](../../assets/images/management/deduplication/group-of-duplicates-status-workflow.gif)
