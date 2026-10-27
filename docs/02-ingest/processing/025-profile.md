---
layout: cluedin
title: Profile
parent: Processing
grand_parent: Ingest
nav_order: 25
permalink: /ingest/processing/profile
content_type: how-to
last_modified: 2026-10-27
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

After a data set finishes uploading, CluedIn computes a data profile for it: the row count, and for each column, its detected data type, how many values are missing, how many distinct values it has, and a few example values. You can view this profile on the **Profile** tab of the data set.

The profile is also structured so that it can be used later to help identify relationships between data sets.

## View the data profile

1. Go to the data set, and then select the **Profile** tab.

1. If the profile is still being computed, the tab shows a **Profiling in progress** message. Wait a moment and check back - profiling usually finishes quickly, but can take longer for larger data sets.

    ![Profile tab showing a Profiling in progress message while the data set's columns are being analyzed]({{ "/assets/images/integration/additional-operations/profile-in-progress.png" | relative_url }})

1. Once profiling finishes, the tab shows the row count and a table with one row per column.

    ![Profile tab showing 8 rows profiled and a table with the id, name, signup_date, and is_active columns, each with its detected type, null percentage, distinct values, and example values]({{ "/assets/images/integration/additional-operations/profile-results.png" | relative_url }})

    The table includes the following information for each column:

    - **Detected type** – the data type CluedIn inferred from the column's values, such as Integer, Decimal, Boolean, DateTime, or String.

    - **Null %** – the percentage of records where the column is empty or missing a value.

    - **Distinct values** – the number of unique values found in the column.

    - **Example values** – a few of the distinct values found in the column.

## Verify the result

The **Profile** tab shows one of three states: profiling in progress, the computed profile, or an error if profiling failed. Refreshing the data set page after profiling completes shows the generated profile without the need to re-upload the data.

## If something goes wrong

If profiling fails, the **Profile** tab shows a **Profiling failed** message with the error. Try reopening the tab to retry; if the problem continues, contact the person responsible for maintaining CluedIn for your organization.

![Profile tab showing a Profiling failed message with an error about reading the data set's rows]({{ "/assets/images/integration/additional-operations/profile-failed.png" | relative_url }})
