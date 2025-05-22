---
layout: cluedin
nav_order: 6
parent: Data catalog
grand_parent: Management
permalink: /management/data-catalog/lookup-data-type
title: Lookup data type
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to work with vocabulary keys that use the Lookup data type to ensure that only valid values are entered in golden records. You will also learn how to identify and fix anomalies in lookup vocabulary keys.

## Overview

A **Lookup** data type is a data type that allows a vocabulary key to get its value from a predefined list of values, typically stored in a glossary term. When a vocabulary key is configured with the Lookup data type, it means that its values are restricted to this controlled list. Instead of manually entering free-form text, users **select from a dropdown list of values**. This helps maintain consistency, standardization, and data quality across your golden records.

The Lookup data type provides an effective way to implement and manage **reference data** in CluedIn. Reference data consists of standardized, stable values used to classify or categorize other types of data. Common examples of reference data include country codes, currency codes, units of measurement, industry types, or product categories.

The process of creating a vocabulary key of the Lookup data type consists of the following steps:

1. [Adding reference data to CluedIn](#add-reference-data)

1. [Creating a glossary term](#create-a-glossary-term) that lists all reference data values that can be used in a vocabulary key of the Lookup data type.

1. [Changing the data type of the vocabulary key](#change-data-type-of-vocabulary-key) and associating it with the relevant glossary term.

## Add reference data

You can add reference data to CluedIn in one of the following ways:

- By uploading a file with reference data.

- By ingesting reference data from a database or an ingestion endpoint.

- By creating a manual data entry project for adding reference records.

In this article, we’ll explore two options for adding reference data: uploading a file and creating a manual data entry project. Note that the processing of reference data ingested from a database or an ingestion endpoint follows the same steps as file-based ingestion.

### Upload a file with reference data

If you have a file with reference data that you want to use in your project, you can upload it to CluedIn. Once the file is uploaded, map it to standard fields. When creating mapping for the data set, make sure you use a business domain and a vocabulary that represent the concept of your reference data. For more information about getting your data into CluedIn, see [Getting started with data ingestion](/getting-started/data-ingestion).

In this article, we'll use the example of the currency reference data. We mapped the reference data to the Currency business domain and the ProjectCurrency vocabulary.

![how-to-use-lookup-keys-1.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-1.png)

After processing the data set, we have a certain number of valid currency records. These represent all the currencies permitted for use in the project. To add these currencies to the vocabulary key of the Lookup data type, first create a glossary category, and then define a term under that category to represent the currency list.

### Create a manual data entry project

If you do not have the existing reference data that you can ingest to CluedIn, you can create reference data records with the help of a manual data entry project. First, create a manual data entry project using the business domain and a vocabulary that represent the concept of your reference data.

![how-to-use-lookup-keys-2.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-2.png)

Then, add the form fields for entering the reference data. For example, if you want to enter currency reference data, you can add two fields: ID and Name. Finally, add the currency reference records manually one by one in the manual data entry project. When you create all the needed currencies, create a glossary category and then define a term under that category to represent the currency list.

## Create a glossary term

Now that you have the needed reference data in CluedIn, create a glossary category and define a term under that category to represent the currency list. When creating a glossary term, define which records should be included the term. In this case, we are listing all currencies that belong to the Currency business domain.

![how-to-use-lookup-keys-3.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-3.png)

Once you configure and activate the glossary term, you can see the list of acceptable currency values on the **Matches** tab. For more information, see [Getting started with Glossary in CluedIn](/getting-started/glossary).

{:.important}
A glossary term must be **active** for its values to appear as the allowed options in vocabulary keys that use the Lookup data type.

![how-to-use-lookup-keys-4.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-4.png)

## Change data type of vocabulary key

Now that you have created and activated a glossary term containing the list of acceptable currencies, the next step is to decide which vocabulary key in your project should be associated with this currency list.

For example, suppose you have a `trainingcompany.currency` vocabulary key used in golden records. You can configure this vocabulary key to the Lookup data type so that users can select values from the predefined currency list, ensuring consistency and accuracy. To do this, [edit the vocabulary key](/management/data-catalog/manage-vocabulary-keys#edit-a-vocabulary-key), change the data type to Lookup, and then select the glossary term that contains the list of allowed values.

![how-to-use-lookup-keys-5.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-5.png)

After saving changes, the vocabulary key is reprocessed and its data type is changed. As a result, 3 computed keys are added to the golden record that contains a vocabulary key of the Lookup data type: `Entity Code`, `Entity ID`, and `Name`. These computed keys are parts of the lookup vocabulary key. You may notice these keys on the search results page, on the golden record Overview page, in the data catalog, and in filters in some places of the platform. Note that at time of processing a rule, the `-Entity Code` part of the lookup vocabulary key is the only property available, not the `-Name` or the `-Entity ID`. So, if you are trying to do comparisons across two lookup vocabulary keys, then you must use the `-Entity Code` to do the comparison.

{:.important}
When lookup reference data is changed or updated, it will be automatically reflected anywhere the vocabulary key of the Lookup data type is used. This means that you do not need to take any additional actions after modifying reference data.

When you try to edit the currency property in a golden record, you can select a currency from the predefined list, but you cannot create a new currency value.

![how-to-use-lookup-keys-6.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-6.png)

If the currency is not in the glossary term, it will be marked as an invalid value. To fix this, edit the property and select the value from the predefined list. To learn how to quickly identify invalid reference data, see [Find anomalies in reference data](#find-anomalies-in-lookup-vocabulary-keys)

![how-to-use-lookup-keys-7.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-7.png)

## Find anomalies in lookup vocabulary keys

_This feature will be available in 2025.01 release._

To quickly find anomalies in vocabulary keys that use the Lookup data type, [create](/management/rules/create-rule) a golden record rule with the corresponding action. First, define which golden records the rule should be applied to. Then, add the rule action:

1. Enter the action name.

1. Specify the condition for identifying invalid values: find and select the needed lookup vocabulary key and use the **Is Invalid Lookup** operator.

1. Enter the tag that should be added to golden records that contain invalid values.

    ![how-to-use-lookup-keys-8.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-8.png)

After saving, activating, and reprocessing the rule, the tag will be added to golden records that contain invalid values in the lookup vocabulary key. To verify that the rule has been applied, go to search and use the **Tags** filter. As a result, all golden records that contain invalid values in the lookup vocabulary key will be displayed on the page. Learn how to fix invalid values in the following section.

![how-to-use-lookup-keys-9.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-9.png)

## Fix invalid values in lookup vocabulary keys

Once you have identified invalid values that are used in the vocabulary key of the Lookup data type, [create](/preparation/clean/create-clean-project#from-the-search-results-page) a clean project. If is convenient to create a clean project from the search results page that displays tagged golden records. In the clean project configuration, add the vocabulary key that contains invalid values. In this case, it is `trainingcompany.currency`. Once the records are loaded into the clean project, you can start fixing invalid values. For example, you can group invalid values using text facet and edit them in bulk. To learn more about fixing values in a clean project, see [Clean data](/preparation/clean/manage-clean-project#clean-data).

![how-to-use-lookup-keys-10.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-10.png)

After correcting all invalid values, process your changes.

![how-to-use-lookup-keys-11.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-11.png)

If the updated values match the allowed values in the lookup vocabulary key, they will no longer be marked as invalid.

![how-to-use-lookup-keys-12.png](../../assets/images/management/data-catalog/how-to-use-lookup-keys-12.png)