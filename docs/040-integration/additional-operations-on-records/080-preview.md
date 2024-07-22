---
layout: cluedin
nav_order: 8
parent: Additional operations
grand_parent: Integration
permalink: /integration/additional-operations-on-records/preview
title: Preview
last_modified: 2024-05-21
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about the various operations available on the **Preview** tab of the data set to gain a better understanding of the uploaded records.

## Profiling

Profiling provides a breakdown and distribution of all vocabulary key values in a graphic format. It can help you identify issues and anomalies in data quality. Profiling is not limited to a data set, meaning that it displays information about vocabulary key values coming from different data sources.

Profiling is a beta feature. To access profiling, go to **Administration** > **Feature Flags**, and enable the **Profiling dashboards** feature.

![preview-profiling-1.png](../../assets/images/integration/additional-operations/preview-profiling-1.png)

You can view profiling at any stage of the data ingestion process: immediately after uploading the data, after creating the mapping, or after processing the data. Profiling is type-specific, so if you change the data type during mapping and then process the data, the profiling dashboard may look different from when you first uploaded the data. For example, if you change the data type for the 'Revenue' column from text to integer, the profiling dashboard will display metrics such as minimum value, maximum value, and average value instead of a breakdown and distribution of text values.

**To view profiling**

- In the column header, open the menu, and select **View profiling**.

    ![preview-profiling-2.gif](../../assets/images/integration/additional-operations/preview-profiling-2.gif)

    For more information, see [Vocabulary keys](/management/data-catalog/vocabulary-keys).

## View duplicates

This feature allows you to check if the column contains duplicate values. Viewing duplicates in a column is available only after the mapping for the data set has been created. 

**To view duplicates**

1. Open the menu in the column heading, and then select **View duplicates**.

    ![preview-duplicates-1.gif](../../assets/images/integration/additional-operations/preview-duplicates-1.gif)

    You can view the total number of duplicate values in the column, identify which values are duplicates, and see how many times each duplicate value occurs.