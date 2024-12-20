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

In this article, you will find reference information to help you understand matching rules and functions, normalization rules, deduplication project statuses, and group statuses.

## Matching rules

Matching rules allow you to set up complex logic for detecting duplicates. In the deduplication project, matching rules are combined using the **OR** logical operator, while matching criteria within a rule are combined using the **AND** logical operator. So, if you want a record to be identified as a duplicate if it meets at least one of your criteria, then you need a separate rule for each criteria. On the other hand, if you want a record to be identified as a duplicate if it meets all of your criteria, then you need one rule that includes all of your criteria.

For example, in the following configuration, either records with the same email address or records with the same first and last name are identified as duplicates.

![rules.png](../../assets/images/management/deduplication/rules.png)

## Matching functions

Matching functions specify how values of a vocabulary key or property should be compared. The following table provides the description of matching functions.

| Function | Description |
|--|--|
| Equals | Identifies records as duplicates if two values are the same. |
| Fuzzy match - Sift4 | Detects approximate duplicates using a string similarity algorithm. This algorithm takes into account the number of matching characters and the transpositions (swaps) needed to make the strings identical. For example, `algorithm` and `algorrithm` would be identified as fuzzy matches.<br> In this method, you have to specify the threshold— a parameter that sets the maximum number of characters by which two strings can differ and still be considered a match.   |
| Fuzzy match - phonetic, DoubleMetaphone | Detects approximate duplicates using a phonetic matching algorithm. This algorithm encodes words into a phonetic representation, allowing for matching based on pronunciation rather than spelling. For example, `night` and `knight` would be identified as fuzzy matches.  |
| Contains | Matches two values if one contains the other. |
| Starts with | Matches two values if one starts with the other. |
| Ends with | Matches two values if one ends with the other. |
| First token equals | Extracts the first word from both values and compares for exact match ignoring casing. |
| Email | Matches two email address values if they are semantically equal. |

Watch the following video where we provide an explanation of matching functions along with practical examples.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/990163626?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" title="Matching functions in a deduplication project"></iframe>
</div>

## Normalization rules

Normalization rules clean up values before comparing them to identify duplicates. The following table provides the description of normalization rules.

| Normalization rule | Description |
|--|--|
| To lowercase | Converts values to lover case. |
| Trim whitespace | Removes whitespace characters from values. |
| Remove punctuation | Removes punctuation marks from the values. For example, `CluedIn.!?,` will be converted to `CluedIn`. |
| Remove special characters | Removes special characters from the values. For example, `CluedIn”#€%&(/)€` will be converted to `CluedIn`. |
| Remove diacritic marks | Removes diacritic marks from the values. For example, `spăn'ĭsh` will be converted to `spanish`. |
| Person name variations | Generates person name variations. For example, `Timothy Daniel Ward` will be converted to `Tim D. Ward`, `Tim Ward`. |
| First name nickname variants | Generates nickname variations for the person's first name. For example, `Timothy` will be converted to `Tim`, `Timmy`. |
| Organization name | Normalizes organization name. For example, `CluedIn ApS` will be converted to `CluedIn`. |
| Phone number | Removes well-known phone number formatting characters. For example, `+45-123 456 789 (001)` will be converted to `45123456789001`. |
| Email mask| Normalizes email address to match other variants. |
| [Street address](#street-address-normalization) | Normalizes common street name tokens. |
| Geography country | Converts country to ISO code. For example, `Australia` will be converted to `AU`. |
| Replace text | Replaces text using configured pattern. You need to enter both the value to be replaced and the replacement value. |
| Regex replace text | Replaces text using configured regex pattern. |
| Split text | Splits text using configured separator. |
| Regex split text | Splits text using configured regex separator pattern. |
| Split text by whitespace | Splits text by whitespace into tokens. |
| Transliterate | Transliterates text value to an ASCII string. For example, `Ελληνική Δημοκρατία` will be converted to `Ellēnikē Dēmokratia`. |

Watch the following video where we provide an explanation of normalization rules along with practical examples.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/994932994?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" title="Normalization rules in a deduplication project"></iframe>
</div>

### Street address normalization

Street address normalization converts input addresses into standardized versions before comparing them to identify duplicates.

For example, let's consider two addresses: _123 Fantasy strabe_ and _123 Fantasy street_. When street address normalization is selected, any time CluedIn sees `strabe`, `strasse`, `street`, or `str`, it turns it into `[STR]`. If the only thing that differs in an address is the way street is spelled, then the addresses will match.

| Input | Normalized version |
|--|--|
| `strabe`, `strasse`, `street`, `str\.?`, `st` | `[STR]` |
| `Allee`, `aly` | `[ALY]` |
| `Boulevard`, `BLVD` | `[BLVD]` |
| `Lane`, `Ln` | `[LANE]` |
| `Drive`, `Dr` | `[DRIVE]` |
| `avenue`, `ave` | `[AVE]` |
| `University`, `univ` | `[UNIVERSITY]` |
| `West`, `w` | `[WEST]` |
| `North`, `n` | `[NORTH]` |
| `East`, `e` | `[EAST]` |
| `South`, `s` | `[SOUTH]` |
| `Floor`, `flr` | `[FLOOR]` |
| `First`, `1st` | `[1ST]` |
| `Second`, `2nd`, `2rd` | `[2ND]` |
| `Third`, `3rd` | `[3RD]` |
| `Fourth`, `4th` | `[4TH]` |
| `Fifth`, `5th` | `[5TH]` |
| `p\.?\s*o\.?\s+box`, `post\s*box`, `post\s*boks`, `GPO\s*Box` | `[POBOX]` |
| `Private\sbag`, `Locked\sBag`, `Private\sMail\sBag`, `Locked\sBag`, `PMB` | `[PMB]` |
| `Plaza`, `PLAZ`, `PLZ` | `[PLZ]` |
| `Suite`, `STE` | `[STE]` |
| `Trailer`, `TRLR` | `[TRLR]` |
| `Apartment`, `APT` | `[APT]` |
| `Basement`, `BSMT` | `[BSMT]` |
| `Building`, `BLDG` | `[BLDG]` |
| `Department`, `DEPT` | `[DEPT]` |
| `Hanger`, `HNGR` | `[HNGR]` |
| `Lobby`, `LBBY` | `[LBBY]` |
| `Lower`, `LOWR` | `[LOWR]` |
| `Office`, `OFC` | `[OFC]` |
| `Penthouse`, `PH` | `[PH]` |
| `Space`, `SPC` | `[SPC]` |
| `Level`, `LVL` | `[LEVEL]` |
| `Highway`, `Highwy`, `Hiway`, `Hiwy`, `Hway`, `Hwy` | `[HWY]` |

## Deduplication project

This section contains reference information about deduplication project statuses.

### Project statuses

The following table provides descriptions of deduplication project statuses.

| Status | Description |
|--|--|
| Requires configuration | The deduplication project has been created, no matching rules have been added yet. |
| Ready to generate | The deduplication project has been configured, no matches have been generated yet. This status also appears when you discard matches at any further stage of the project. |
| Generating | CluedIn is analyzing the specified set of golden records with the aim to detect duplicates based on your matching rules. |
| Aborting generation | The process of generating matches of the deduplication project is being cancelled. The status will shortly change to **Ready to generate**. |
| Ready for review | CluedIn has generated matches of the deduplication project, you can start [processing groups of duplicates](/management/deduplication/manage-groups-of-duplicates). |
| Committing | CluedIn is merging records from selected groups. This status is applicable whether you are merging a single group, multiple groups, or all groups in the project. |
| Merged | CluedIn has merged records from all groups in the project. If the project contains groups that were not selected for merge, the project status remains **Ready for review**. |
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
