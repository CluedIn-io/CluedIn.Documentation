---
layout: cluedin
nav_order: 3
parent: Data catalog
grand_parent: Management
permalink: management/data-catalog/vocabulary-keys
title: Vocabulary keys
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about vocabulary keys and the importance of specifying the correct data type for a vocabulary key to unlock the full potential of filters.

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