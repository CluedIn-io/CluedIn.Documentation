---
layout: cluedin
nav_order: 3
parent: Data catalog
grand_parent: Management
permalink: /management/data-catalog/vocabulary-keys
title: Vocabulary keys
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to efficiently create and manage vocabulary keys, enabling you to structure and organize metadata within the system. You will also discover the importance of specifying the correct data type for a vocabulary key to unlock the full potential of filters.

## Vocabulary key overview

A vocabulary key helps CluedIn understand the data you send. It is an attribute that helps describe a golden record. Such attributes provide information about the golden record's features, connections, and characteristics that are important for understanding and using the data effectively.

In CluedIn, you can browse all vocabulary keys by going to **Management** > **Data Catalog** > **View All Vocabulary Keys**. In addition, you can browse all vocabulary keys belonging to a specific vocabulary on the [vocabulary details page](/management/data-catalog/vocabulary#vocabulary-details-page).

## Vocabulary key details page

On the vocabulary key details page, you can view relevant information about a vocabulary key and take other actions to [manage a vocabulary key](#manage-a-vocabulary-key).

### Configuration

This tab contains general information about the vocabulary key, including:

- Display name – a user-friendly identifier of the vocabulary key.  This name is displayed at the top of the vocabulary details page.

- Name – an identifier of the vocabulary key that, together with the key prefix, forms a complete vocabulary key.

- Group – a collection that brings together related vocabulary keys, facilitating easier navigation among all keys within the vocabulary.

- Visibility settings – a configuration that determines if the vocabulary key is visible in the system. When the toggle is turned off, it means that the vocabulary key is not available in filters, column options in search results page, or golden record properties. While all vocabulary key values are retained in the system, they can only be viewed on the vocabulary key details page.

- Data type – a type of data that the vocabulary key can hold. For more information, see [Data types](/management/data-catalog/data-types).

    {:.important}
    The data type is closely connected with the list of available operators in filters. Depending on the data type assigned to the vocabulary key, the list of operators may differ. For example, the list of operators for a vocabulary key with the Number data type is different from that for a vocabulary key with the Text data type.

- Storage type – a type of field—keyword, typed, untyped—where the vocabulary key value is stored.

    _Keyword_ is generally used for strings. _Typed_ is the default choice for numeric and date-related data types, enabling the use of specific operators in filters (for example, _Between_, _Equals_, _Greater or Equal_). If you change the storage to _Untyped_, you won't have access to the specific operators designed for numeric or date-related data types. Nevertheless, you can still use operators available for strings.

- Classification – a logical category that makes the vocabulary key easy to search.

- Description – a summary that explains the purpose of the vocabulary key. You can add rich formatting to the description, such as bolding, underlining, or italicizing text.

- [Mapping](#map-one-vocabulary-key-to-another) to another vocabulary key – a section that shows if the current vocabulary key is mapped to another vocabulary key. The purpose of such mapping is to avoid having duplicate values in the system.

### Usage

This tab contains the global view of vocabulary key usage in the system: number of golden records, streams, glossary terms, rules, data set mappings, clean projects, deduplication projects, and saved searches where the vocabulary key is used. You can select the **View all** button to view more details and find links to the corresponding elements in the system.

![vocabulary-key-usage.gif](../../assets/images/management/data-catalog/vocabulary-key-usage.gif)

### All values

This tab displays all values associated with the key, along with the total number of golden records in which each value is used. When you select a specific value, a new tab containing the search results will open. This tab lists golden records where the selected vocabulary key value is used. Note that the vocabulary key column is not displayed by default, so you may need to [add columns](/key-terms-and-features/search#add-columns) to the search results page.

![vocabulary-key-all-values.gif](../../assets/images/management/data-catalog/vocabulary-key-all-values.gif)

### Lineage

This tab shows the transformations of the vocabulary key.

- Integrations – data source from which the vocabulary key originates.

- Source vocabulary keys – vocabulary key that originates from a specific data source (integration).

- Core vocabulary keys – vocabulary key to which the source vocabulary key is mapped.

- Streams – streams where the vocabulary key is used.

### Profiling

This tab contains a breakdown and distribution of all vocabulary key values in a graphic format. It can help you identify issues and anomalies in data quality.

Profiling is a beta feature. To access profiling, go to **Administration** > **Feature Flags**, and enable the **Profiling dashboards** feature.

![preview-profiling-1.png](../../assets/images/integration/additional-operations/preview-profiling-1.png)

Profiling is type-specific, so the dashboards for text and number vocabulary keys are different. The following image shows an example of profiling for a text vocabulary key.

![vocab-key-profiling-1.png](../../assets/images/management/data-catalog/vocab-key-profiling-1.png)

The profiling for a text vocabulary key contains the following dashboards:

- Total values – the total number of values that the vocabulary key has.

- Values over time – a time-series visualization displaying the count of values that appeared in CluedIn over time. The x axis represents the time, and the y axis represents the count of values.  For a more granular view, you can select a specific time period using the mouse.

- Distribution of values (bar gauge) – the distribution of vocabulary key values based on the number of records where each value is used. Each bar represents a distinct value, with the color gradient indicating the frequency of that value's occurrence in the records: green indicates a lower number of records, while red indicates a higher number of records. This gradient provides a quick visual cue for identifying the most and least common values.

- Distribution of values (pie chart) – the distribution of vocabulary key values based on the number of records where each value is used. Each slice of the pie represents a distinct key value, with the area of the slice indicating the frequency of that value's occurrence in the records. The larger the slice, the higher the number of records that contain the value. This type of visualization helps to quickly understand the relative proportions of different vocabulary key values.

The following image shows an example of profiling for a number vocabulary key.

![vocab-key-profiling-2.png](../../assets/images/management/data-catalog/vocab-key-profiling-2.png)

The profiling for a number vocabulary key contains the following dashboards:

- Minimum value – the minimum value among all values of a vocabulary key.

- Standard deviation – the amount of variation or dispersion in a set of values. It indicates how much individual values deviate from the average value. A low standard deviation indicates that the values tend to be close to the average, while a high standard deviation indicates that the values are spread out over a wider range of values.

- Maximum value – the maximum value among all values of a vocabulary key.

- Average value – the average value, calculated by dividing the sum of all values by the number of values. This visualization helps to quickly understand the central tendency among the vocabulary key values.

- Number of values – the total number of values that the vocabulary key has.

- Sum value – the sum of all vocabulary key values.

- Values over time – a time-series visualization displaying the count of values that appeared in CluedIn over time. The x axis represents the time, and the y axis represents the count of values.

### Pending changes and Audit log

The **Pending changes** tab contains tasks for reviewing changes to the vocabulary key submitted by users who are not Vocabulary Owners. The **Audit log** tab contains a detailed history of changes to the vocabulary key.

## Create a vocabulary key

Depending on the selected [data modeling approach](/management/data-catalog/modeling-approaches), you can create a vocabulary key in two ways:

- **Automatically** – this option is part of the data-first approach. When [creating a mapping](/integration/create-mapping) for a data set, you have the option to generate a new vocabulary. CluedIn will then automatically create vocabulary keys and assign data types. You can customize the names of vocabulary keys and data types. Once the mapping is created, you can then open the vocabulary and make additional adjustments to vocabulary keys if needed.

    ![create-vocabulary-key-mapping.gif](../../assets/images/management/data-catalog/create-vocabulary-key-mapping.gif)

- **Manually** – this option is part of the model-first approach, which assumes that you need to create vocabulary keys before creating the mapping for a data set. The following procedure outlines the steps to manually create a vocabulary key.

**To create a vocabulary key**

1. Go to the **Vocabulary Keys** tab, and then select **Add Vocabulary Key**.

1. Enter the display name of the vocabulary key. This name is displayed at the top of the vocabulary details page.

1. Enter the name of the vocabulary key. This name, together with the key prefix, forms a complete vocabulary key.

1. Enter the name of the group to which the vocabulary key will belong.

1. (Optional) If you don't want to the vocabulary key to be displayed anywhere else in the system, turn off the corresponding toggle.

1. Select the data type of the vocabulary key. For more information, see [Data types](/management/data-catalog/data-types).

1. Review the storage for the vocabulary key. This is the type of field—keyword, typed, untyped—where the vocabulary key value is stored. The storage is selected by default according to the data type. The keyword storage option cannot be changed. 

    If you configure the storage as typed but send untyped data—such as a combination of integer and string, as in _'10-regular'_—then such untyped values (_'regular'_) would be excluded from the filter results. Even though these values are still stored, they are treated as anomalies.

1. (Optional) Select the classification for the vocabulary key. This is a way to categorize vocabulary keys, making them easier to search.

1. Select **Create**.

    ![create-vocabulary-key.gif](../../assets/images/management/data-catalog/create-vocabulary-key.gif)

    The vocabulary key page opens, where you can view and manage vocabulary key details.

## Manage a vocabulary key

Once the vocabulary key is created, you can edit its configuration based on your requirements or establish mapping to other vocabulary key, ensuring the maintenance of organized and consistent metadata.

### Edit a vocabulary key

You can edit a vocabulary key to make necessary changes in its configuration.

{:.important}
Changing the data type, storage, classification, and [mapping](#map-one-vocabulary-key-to-another) will trigger the reprocessing of a vocabulary key. Additionally, if you change the name of the vocabulary key, a new key will be generated, with the existing key automatically mapped to the new one and marked as obsolete.

**To edit a vocabulary key**

1. Open the vocabulary key that you want to edit.

1. In the upper-right corner of the vocabulary key details page, select **Edit**.

1. Make the needed change and then save them.

    Depending on the section that you want to edit, you may have to follow different steps. For example, direct editing is not possible for the **Name** and **Data Type** sections; instead, you must select the corresponding buttons to open the panes for editing.

    ![edit-vocabulary-key.gif](../../assets/images/management/data-catalog/edit-vocabulary-key.gif)

### Map one vocabulary key to another

The purpose of mapping one vocabulary key to another is to ensure organized and consistent data, preventing duplicate values within the system. To demonstrate the importance and efficiency of vocabulary key mapping, let's look at an example.

Suppose you have contact records coming into CluedIn from various sources—Salesforce, SAP, and MS SQL Server—and each source has its unique vocabulary. Some properties in data coming from these sources are the same, and some are different. For example, the _gender_ property exists in data from all three sources. It means that _gender_ values would be stored in three separate vocabulary keys. To keep all _gender_ values under one vocabulary key instead of keeping them in each separate vocabulary key, you can map these three vocabulary keys to one, thus improving the organization and getting better visibility of your data.

**To map one vocabulary key to another**

1. Open the vocabulary key that you want to map to another vocabulary key.

1. In the upper-right corner of the vocabulary key details page, select **Edit**.

1. In the **Maps to** section, select **Add mapping**.

1. Find and select a vocabulary key to which you want to map the current vocabulary key. Then, select **Add Key**.

    ![map-vocabulary-key.gif](../../assets/images/management/data-catalog/map-vocabulary-key.gif)

1. Select **Save**, and then confirm your choice.    

The vocabulary key mapping is executed on the clue level, so the **History** of the golden record does not show source and target properties. However, you can view the source and target properties in the **Explain Log** of the golden record (**Records** > data source > **Translate properties** > **Summaries**).

If two vocabulary keys from different sources have conflicting values, you need to create a survivorship rule to define which value wins for the golden records belonging to the same entity type. For the practical application of vocabulary key mapping and survivorship rules, check the video in [Modeling approaches](/management/data-catalog/modeling-approaches).
