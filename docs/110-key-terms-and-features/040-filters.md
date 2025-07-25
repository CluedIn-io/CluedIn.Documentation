---
layout: cluedin
title: Filters
parent: Key terms and features
permalink: /key-terms-and-features/filters
nav_order: 4
has_children: false
tags: ["filters"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Filters play a significant role in various parts of CluedIn. Filters are used in advanced search, clean projects, streams, rules, and glossary. The purpose of a filter is to define a specific set of records for further activities in the system.

In this article, you will learn how the filter in CluedIn works, what it consists of, and how to create efficient and complex filters to precisely define the data you require.

## Overview

Filters can be as simple or complex as you need. Simple filters consist of a single condition or several conditions combined with a logical operator. Complex filters consist of groups of conditions combined with a logical operator. The filter consists of the following elements:

1. **AND/OR operator** – a logical operator that combines conditions expressed within rules or groups (if available).

1. **Group** – a container for rules, allowing you to create complex filters by combining multiple conditions. Each group has its own AND/OR operator, which dictates how the conditions within the group are combined.

1. **Rule** – a set of parameters that make up a filter condition. It defines what to look for in your data.

    ![filters-1.png]({{ "/assets/images/key-terms-and-features/filters-1.png" | relative_url }})

Creating a filter is a step-by-step process in which parameters are defined one after another. The following diagram shows the sequence of defining filter parameters.

![filters-2.png]({{ "/assets/images/key-terms-and-features/filters-2.png" | relative_url }})

**Property type** is a parameter that defines the type of object in CluedIn. There are the following property types:

- Property – a metadata about a golden record. You can find many properties on the golden record details page. For more information, see [Properties](#properties).

- Vocabulary – a schema that contains attributes (vocabulary keys) shared across different golden records.

- Glossary – a group of records that meet specific criteria. A glossary is essentially a predefined subquery or a rule that can be combined into another rule to reduce complexity and promote reuse and consistency.

**Object** is a parameter that defines a specific element you are filtering on. **Operation** defines the relationship between filter parameters. The available operations change based on the object's data type (DateTime, Text, Integer, and so on). For more information, see [Operations](#operations). **Value** is a criteria that you use to define the filter results.

For example, the following filter will return all records where such Property (object type) as Tag (object) Contains (operation) the value Invalid (criteria).

![filters-3.png]({{ "/assets/images/key-terms-and-features/filters-3.png" | relative_url }})

If you want to define several criteria in one filter, you can add more rules to the same filter. For example, the following filter will return all records where such Property (object type) as Tag (object) Contains (operation) the value Invalid or To review (criteria).

![filters-4.png]({{ "/assets/images/key-terms-and-features/filters-4.png" | relative_url }})

When adding more rules to the filter, pay attention to the **AND**/**OR** operator in the upper-left corner of the filter. Selecting **AND** will return only those records where all combined criteria match. Selecting **OR** will return only those records where any of the combined criteria match.

## Filters in search

Filters in search help you narrow down the exact records you want to see or use for such activities as merge or clean. There are two filter modes in search:

- **Basic** – you can filter records by business domains, providers, sources, or tags (if available in the system). You can select multiple values in each filter parameter.

    ![filters-5.png]({{ "/assets/images/key-terms-and-features/filters-5.png" | relative_url }})

- **Advanced** – you can filter records by various properties or vocabulary keys. You can also filter records by their association with a particular glossary. Advanced mode gives you more precision in defining filter criteria. The following screenshot displays the same filters as in the screenshot above, but they are represented in the advanced filter mode.

    ![filters-6.png]({{ "/assets/images/key-terms-and-features/filters-6.png" | relative_url }})

After you set up your search filters, you can save them for future use. This eliminates the need to specify filter criteria each time you want to find the same set of records. You can also share saved searches within your organization, making them available to others who need to work with the same set of records. For more information, see [Saved searches](/key-terms-and-features/search#saved-searches).

{:.important}
Saved searches are particularly useful in [clean projects](/preparation/clean), especially if you need to clean your records on a regular basis. You can set up and save a search filter to detect specific data issues, and when the saved search returns results, you can run the clean project to fix those issues.

## Reference information

This section includes descriptions of properties and operations available in filters. Refer to the relevant section to learn more about each option.

### Properties

| Property | Description |
|--|--|
| Aliases | An alternative or secondary name associated with the record. |
| Authors | User who created the record. |
| Created Date | Date when the record was created in the source system or date when the record was created via a manual data entry project in CluedIn. |
| Description | Description of the record. |
| Discovery Date | Date when the record was discovered in CluedIn during processing. |
| Display Name | Name of the record in CluedIn that is shown at the top of on the record details page next to the business domain. If the record in the source system does not contain the display name, then the Name is shown instead of Display Name. |
| Document Mime Type | A label that specifies the nature and format of the record. It is part of the metadata for records added via a crawler or posted to CluedIn. |
| Encoding | A type of encoding scheme (e.g., UTF-8) used to represent the characters in the record. It is part of the metadata for records added via a crawler or posted to CluedIn. |
| Entity Codes | Additional unique identifiers of the record. |
| Business Domain | An attribute of the record that corresponds to a specific business domain. You can set up a filter to return only those records that are associated with a particular business domain. |
| Last Changed By | User who was the last to edit the record. |
| Last Processed Date | Date when the record was processed for the last time. |
| Modified Date | Date when the record was modified in the source system or date when the record has been modified via clean, deduplication, or manual data entry project in CluedIn. |
| Name | Name of the record in CluedIn that is shown in the search results page and in the record properties of the record details page.|
| Origin Entity Code | Unique primary identifier of the record.  |
| Origin Entity Codes in source records | Additional unique identifier of the record that is composed of the source name and the field used in the creation of origin entity code.  |
| Property Count | The number of properties the record has. |
| Provider | A system from which the data came to CluedIn, such as SAP, HubSpot, or Azure Data Lake. You can set up a filter to return only those records that were created from a specific provider. |
| Revision | A version number of the record. It is part of the metadata for records added via a crawler or posted to CluedIn. |
| Source | A source of the incoming data, such as a specific file, endpoint, or database. You can set up a filter to return only those records that were created from a specific source. |
| Tag | A label that automatically categorizes records across business domains. You can set up a filter to return only those records that contain a specific tag. |

### Operations

| Operation | Description |
|--|--|
| Begins With | Valid for a property or vocabulary key that contains text or numbers. You have to specify a single value. The filter results include only those records where the selected property or vocabulary key begins with the value in the filter. |
| Between | Valid for a property that contains dates. You need to specify two values. The filter results include only those records where the selected property is between the two values in the filter. |
| Contains | Valid for a property or a vocabulary key that contains text or numbers. You have to specify a single value. The filter results include only those records where the selected property or vocabulary key contains the value in the filter. |
| Ends With | Valid for a property or vocabulary key that contains text or numbers. You have to specify a single value. The filter results include only those records where the selected property or vocabulary key ends with the value in the filter. |
| Equals | Valid for a property or a vocabulary key that contains text, numbers, or dates. You need to specify a single value. Filter results include only those records where the selected property or vocabulary key matches the value in the filter. |
| Exists/Is Not Null | Valid for a property or a vocabulary key that contains text, numbers, or dates. You do not have to specify a value. The operation checks for the presence of data in the property or vocabulary key. The filter results include only those records where the selected property or vocabulary key has a value. |
| Greater | Valid for a property that contains dates. You need to specify a single value. The filter results include only those records where the selected property is greater than the value in the filter. |
| Greater or Equal | Valid for a property that contains dates. You need to specify a single value. The filter results include only those records where the selected property is greater than or the same as the value in the filter. |
| In | Valid for a property or a vocabulary key that contains text or numbers. You can specify multiple values. The filter results include only those records where the selected property or vocabulary key contains the values in the filter. |
| Less | Valid for a property that contains dates. You need to specify a single value. The filter results include only those records where the selected property is less than the value in the filter. |
| Less or Equal | Valid for a property that contains dates. You need to specify a single value. The filter results include only those records where the selected property is less than or the same as the value in the filter. |
| Not Begins With | Valid for a property or vocabulary key that contains text or numbers. You have to specify a single value. The filter results include only those records where the selected property or vocabulary key does not begin with the value in the filter. |
| Not Between | Valid for a property that contains dates. You need to specify two values. The filter results include only those records where the specified property is not between the two values in the filter. |
| Not Contains | Valid for a property or a vocabulary key that contains text or numbers. You have to specify a single value. The filter results include only those records that do not contain the specified value. |
| Not Ends With | Valid for a property or vocabulary key that contains text or numbers. You have to specify a single value. The filter results include only those records where the selected property or vocabulary key does not end with the value in the filter. |
| Not Equal | Valid for a property or a vocabulary key that contains text, numbers, or dates. You need to specify a single value. Filter results include only those records where the selected property or vocabulary key does not match the value in the filter. |
| Does Not Exist/Is Null | Valid for a property or a vocabulary key that contains text, numbers, or dates. You do not have to specify a value. The operation checks for the presence of data in the property or vocabulary key. The filter results include only those records where the specified property or vocabulary key has no value. |
| Not In | Valid for a property or a vocabulary key that contains text or numbers. You can specify multiple values. The filter results include only those records where the selected property or vocabulary key does not contain the values in the filter. |
| Is Not True | Valid for a glossary. The filter results include only those records that do not belong to the specified glossary. |
| Is True | Valid for a glossary. The filter results include only those records that belong to the specified glossary. |