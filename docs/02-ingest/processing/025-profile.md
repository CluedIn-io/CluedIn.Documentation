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

After a data set finishes uploading, CluedIn computes a data profile for it: the row count, and for each column, its detected data type, how many values are missing, how many distinct values it has, and a few example values. You can view this profile on the **Profile** tab of the data set, together with an optional, deeper analysis you can run on request.

The profile is also structured so that it can be used later to help identify relationships between data sets.

## View the data profile

1. Go to the data set, and then select the **Profile** tab.

1. If the profile is still being computed, the tab shows a **Profiling in progress** message. Wait a moment and check back - profiling usually finishes quickly, but can take longer for larger data sets.

    ![Profile tab showing a Profiling in progress message while the data set's columns are being analyzed]({{ "/assets/images/integration/additional-operations/profile-in-progress.png" | relative_url }})

1. Once profiling finishes, the tab shows summary tiles and a table with one row per column.

    ![Profile tab dashboard showing stat tiles for rows, columns, average completeness, and profiled-at time, above a table of the id, cost, price, quantity, email, and discount_code columns, each with its detected type, null percentage, distinct values, and example values]({{ "/assets/images/integration/additional-operations/profile-dashboard.png" | relative_url }})

    The summary tiles show the total row count, column count, average completeness across all columns, and when the profile was computed. The table includes the following information for each column:

    - **Detected type** – the data type CluedIn inferred from the column's values, such as Integer, Decimal, Boolean, DateTime, or String.

    - **Null %** – the percentage of records where the column is empty or missing a value.

    - **Distinct values** – the number of unique values found in the column.

    - **Example values** – a few of the distinct values found in the column.

    Below the table, a chart shows the columns with the highest percentage of empty values, if any.

## Run advanced analysis

Because it costs more to compute, a deeper analysis of the data set is not generated automatically - you start it from the **Advanced analysis** card at the bottom of the **Profile** tab.

**To run advanced analysis**

1. On the **Profile** tab, in the **Advanced analysis** card, select **Run advanced analysis**.

    ![Advanced analysis card with a description of what it computes and a Run advanced analysis button]({{ "/assets/images/integration/additional-operations/profile-advanced-notstarted.png" | relative_url }})

    The card shows an **Analysis in progress** message with a progress indicator while it runs.

1. Once it finishes, the card shows three sections:

    ![Advanced analysis card showing a Correlated fields chart with a cost to price bar, and the start of an Anomalies chart for the quantity column]({{ "/assets/images/integration/additional-operations/profile-advanced-results.png" | relative_url }})

    - **Correlated fields** – pairs of numeric columns whose values move together, as a Pearson correlation coefficient from -1 (perfectly inverse) to 1 (perfectly aligned). Only pairs with a coefficient of at least 0.5 in either direction are shown.

    - **Anomalies** – numeric columns that have values more than three standard deviations from the column's mean, with how many such values each column has.

    - **Data patterns** – the most common value "shapes" per column, with digits collapsed to `9`, uppercase letters to `A`, and lowercase letters to `a`. This can reveal structure a column's detected type alone does not, such as a text column that is consistently formatted as an email address or a fixed-width code.

    Any section with nothing to report says so instead of showing an empty chart.

## Verify the result

The **Profile** tab shows one of three states for the basic profile: profiling in progress, the computed profile, or an error if profiling failed. The **Advanced analysis** card shows its own status independently, since it is only computed when requested. Refreshing the data set page after either finishes shows the generated results without the need to re-upload the data.

## If something goes wrong

If profiling fails, the **Profile** tab shows a **Profiling failed** message with the error. Try reopening the tab to retry; if the problem continues, contact the person responsible for maintaining CluedIn for your organization.

![Profile tab showing a Profiling failed message with an error about reading the data set's rows]({{ "/assets/images/integration/additional-operations/profile-failed.png" | relative_url }})

Advanced analysis fails independently of the basic profile and shows its own error message in the same card; select **Run advanced analysis** again to retry.
