---
layout: cluedin
nav_order: 5
parent: Deduplication
grand_parent: Management
permalink: /management/deduplication/run-deduplication-in-spark
title: Run deduplication in Spark
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

For large deduplication projects, you can generate matches using Apache Spark instead of the standard CluedIn engine. Spark is a distributed processing engine that spreads the matching work across a cluster, which makes it a better fit for projects with very large numbers of golden records.

{:.important}
Running in Spark produces the same kind of results as the standard engine—the same matching rules and normalization rules apply, and duplicate groups are reviewed, merged, and unmerged the same way. See [Generate matches](/management/deduplication/manage-a-deduplication-project#generate-matches) for the standard flow.

## Before you start

Running in Spark is available only if your organization has the feature enabled. If you don't see the **Run in Spark** option described below, contact your CluedIn administrator.

## Generate matches using Spark

**To generate matches using Spark**

1. In the deduplication project, select **Generate matches**.

1. In the confirmation dialog, turn on the **Run in Spark** toggle.

    If the toggle is disabled, your project's matching rules currently aren't supported in Spark. CluedIn lists the specific reasons underneath the toggle—see [Supported matching rules](#supported-matching-rules) below for what to check.

1. Confirm your choice.

    Progress is shown the same way as a standard generation run. When it's complete, groups of duplicates appear on the page exactly as they would from a standard run.

{:.important}
If the CluedIn server restarts while a Spark-based generation is still running—for example, during scheduled maintenance—the run automatically picks up where it left off. You don't need to start it again.

## Supported matching rules

Most matching rules that you can build in a deduplication project work the same way in Spark.

**Matching functions**

All [matching functions](/management/deduplication/deduplication-reference#matching-functions) are supported: Equals, Fuzzy match - Sift4, Fuzzy match - phonetic (DoubleMetaphone), Contains, Starts with, Ends with, First token equals, and Email.

**Normalization rules**

Most [normalization rules](/management/deduplication/deduplication-reference#normalization-rules) are supported:

| Supported | Not yet supported |
|--|--|
| To lowercase | Person name variations |
| Trim whitespace | First name nickname variants |
| Remove punctuation | Organization name |
| Remove special characters | Replace text |
| Remove diacritic marks | Split text |
| Organization name postfix | Regex split text |
| Phone number | Split text by whitespace |
| Email mask | |
| Street address | |
| Geography country | |
| Regex replace text | |
| Transliterate | |

{:.important}
**Organization name** isn't supported yet, but **Organization name postfix** is—it covers the most common case (stripping legal suffixes like *Ltd*, *Inc*, or *GmbH*) and is already the recommended choice for large deduplication projects even outside of Spark.

A rule that uses an unsupported matching function or normalization rule is reported as incompatible, with the specific rule and field named in the reason—it's never silently skipped or run with different behavior.

## Rules with no strong matching field

A matching rule needs at least one criterion using Equals, First token equals, or Email (or a case-insensitive equals) so CluedIn can efficiently narrow down candidates before comparing them closely. This is called a *blocking* criterion.

A rule made up entirely of Fuzzy match or Contains/Starts with/Ends with criteria—with nothing exact to narrow down candidates first—can still run in Spark, but only if the project's current scope is small enough to compare efficiently without that shortcut. CluedIn checks this automatically each time and tells you the real number if a rule doesn't currently qualify. If your project grows past that point later, the same rule may need to be split so that at least one criterion uses Equals, First token equals, or Email—the same best practice already recommended in [Create a deduplication project](/management/deduplication/create-a-deduplication-project#add-a-matching-rule).

## Frequently asked

**Will my results be different?**

No. CluedIn only allows **Run in Spark** for rules it can run identically to the standard engine. If a rule can't be run this way, the toggle tells you why instead of giving you a different result.

**Is it always faster?**

For large projects, yes—that's the point of using it. For smaller projects, the standard engine is already fast, and Spark's own startup time means it isn't worth choosing until your data is genuinely large.

**Does review, merging, or undoing work differently for groups found through Spark?**

No. A group of duplicates found through Spark goes through the same [review, merge, and undo](/management/deduplication/manage-groups-of-duplicates) process as one found the standard way.
