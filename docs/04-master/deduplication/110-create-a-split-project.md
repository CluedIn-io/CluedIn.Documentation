---
layout: cluedin
title: Create a Split project
parent: Deduplication
grand_parent: Master
nav_order: 110
permalink: /master/deduplication/create-a-split-project
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Create a Split project when golden records that a [deduplication project](/master/deduplication/create-a-deduplication-project) previously merged no longer belong together - for example, because the data changed, or because you want to apply a stricter rule set than the one that merged them. A Split project evaluates every golden record in your organization against its own matching rules, and splits apart the contributing records of any golden record whose records no longer all match each other.

A Split project only ever undoes a merge: it removes contributing records that a previous merge brought in, and never removes a golden record's own original data. If none of a golden record's contributing records came from a merge, the Split project leaves it untouched, even if your rules would otherwise flag it.

## Prerequisites

- The **Deduplication Project Management** claim, which covers creating and editing a Split project. See [Claims](/administer/users-and-roles/claims#management).
- Golden records that were produced by merging, so there is something for the project to potentially split apart.

## Inputs

The project:

| Field | Required | What it accepts | Example |
|--|--|--|--|
| **Name** | Required | A name that helps you find the project later. | `Contact re-split` |
| **Description** | Optional | A description of the project. | `Re-evaluate contacts merged before the stricter email rule` |
| **Folder** | Optional | A folder to organize the project in. | `Data quality` |

Each rule:

| Field | Required | What it accepts | Example |
|--|--|--|--|
| Rule name | Required | A name for the rule. | `Same email` |
| **Field type** | Required | **Vocabulary Key** or **Property**, and then the key or property to compare. | `contact.email` |
| **Comparison function** | Required | One of the [matching functions](/master/deduplication/deduplication-reference#matching-functions). | **Equals** |

{:.note}
A Split project currently evaluates every golden record in your organization - there is no equivalent to a deduplication project's business domain or advanced filter scope yet. Normalization rules aren't available on a Split project's rules either.

## Create a Split project

1. On the navigation pane, go to **Management** > **Deduplication**.

1. Select **Split projects**.

1. Select **Create Split project**.

1. Enter a name, and optionally a description and folder, then save.

1. On the project's detail page, add one or more rules: enter a rule name, choose the field type and field, choose a comparison function, then select **Add rule**.

1. Select **Run Split project**.

## Verify the result

The project's run status shows **Running** while it evaluates golden records, then **Completed**, along with how many golden records it evaluated and how many it split. A run that fails shows **Failed**. You can select **Cancel run** while a run is in progress; the project keeps whatever it already split up to that point.

## What this changes

For each golden record a Split project splits, it removes the contributing records that no longer match from that golden record, the same way [unmerging records](/master/deduplication/manage-groups-of-duplicates#unmerge-records) does - the removed records are reprocessed and, if their own data still ties them together, reappear as their own golden record. Golden records it evaluates but doesn't split are left completely unchanged.
