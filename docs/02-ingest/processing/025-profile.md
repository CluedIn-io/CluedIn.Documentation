---
layout: cluedin
title: Profile
parent: Processing
grand_parent: Ingest
nav_order: 25
permalink: /ingest/processing/profile
content_type: how-to
last_modified: 2026-10-28
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

After a data set finishes uploading, CluedIn computes a data profile for it: the row count, and for each column, its detected data type, how many values are missing, how many distinct values it has, a few example values, its most common value format, and other columns whose values move together with it. You can view this profile on the **Profile** tab of the data set.

The profile is also structured so that it can be used later to help identify relationships between data sets.

## View the data profile

1. Go to the data set, and then select the **Profile** tab.

1. If the profile is still being computed, the tab shows a **Profiling in progress** message. Wait a moment and check back - profiling usually finishes quickly, but can take longer for larger data sets.

    ![Profile tab showing a Profiling in progress message while the data set's columns are being analyzed]({{ "/assets/images/integration/additional-operations/profile-in-progress.png" | relative_url }})

1. For a data set larger than a size your administrator configures, the tab instead shows a **Profiling not started** message with a **Run profiling** button - profiling such a large data set is not started automatically, to avoid the cost of doing so for every upload. Select **Run profiling** to compute it anyway.

    ![Profile tab showing a Profiling not started message with a Run profiling button]({{ "/assets/images/integration/additional-operations/profile-notstarted.png" | relative_url }})

1. Once profiling finishes, the tab shows summary tiles and a table with one row per column.

    ![Profile tab dashboard showing stat tiles for rows, columns, average completeness, and profiled-at time, above a table of the id, cost, price, quantity, email, and discount_code columns, each with its detected type, null percentage, distinct values, example values, pattern, and closely related fields]({{ "/assets/images/integration/additional-operations/profile-dashboard.png" | relative_url }})

    The summary tiles show the total row count, column count, average completeness across all columns, and when the profile was computed. The table includes the following information for each column:

    - **Detected type** – the data type CluedIn inferred from the column's values, such as Integer, Decimal, Boolean, DateTime, or String.

    - **Null %** – the percentage of records where the column is empty or missing a value.

    - **Distinct values** – the number of unique values found in the column.

    - **Example values** – a few of the distinct values found in the column.

    - **Pattern** – the column's most common value "shape", with digits collapsed to `9`, uppercase letters to `A`, and lowercase letters to `a`, and the share of the column's values that share it. Only shown when it covers more than a tenth of the column's values; this can reveal structure a column's detected type alone does not, such as a text column that is consistently formatted as an email address or a fixed-width code. A column with nothing to report shows **No repeating pattern**.

    - **Closely related fields** – other columns whose values move together with this one, each with a couple of real value pairs so you can see the relationship rather than infer it from a statistic. Only a strong relationship is shown; two columns that merely happen to drift together are left out. A column with nothing to report shows **No closely related fields**.

    Profiling reads at most the first 10,000 rows of a larger data set. When it does, a note under **Columns** says how many of the data set's rows the statistics are based on.

## Verify the result

The **Profile** tab shows one of these states: not started (for a large data set awaiting a manual run), profiling in progress, the computed profile, or an error if profiling failed. Refreshing the data set page after profiling finishes shows the generated results without the need to re-upload the data.

## If something goes wrong

If profiling fails, the **Profile** tab shows a **Profiling failed** message with the error. Try reopening the tab to retry; if the problem continues, contact the person responsible for maintaining CluedIn for your organization.

![Profile tab showing a Profiling failed message with an error about reading the data set's rows]({{ "/assets/images/integration/additional-operations/profile-failed.png" | relative_url }})
