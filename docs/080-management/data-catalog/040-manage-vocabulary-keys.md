---
layout: cluedin
nav_order: 4
parent: Data catalog
grand_parent: Management
permalink: /management/data-catalog/manage-vocabulary-keys
title: Manage vocabulary keys
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to efficiently create and manage vocabulary keys, helping you to structure and organize metadata within the system.

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

## Edit a vocabulary key

You can edit a vocabulary key to make necessary changes to its configuration, ensuring that metadata is organized and consistent.

{:.important}
Changing the data type, storage, classification, and [mapping](#map-one-vocabulary-key-to-another) will trigger the reprocessing of a vocabulary key. Additionally, if you change the name of the vocabulary key, a new key will be generated, with the existing key automatically mapped to the new one and marked as obsolete.

**To edit a vocabulary key**

1. Open the vocabulary key that you want to edit.

1. In the upper-right corner of the vocabulary key details page, select **Edit**.

1. Make the needed change and then save them.

    Depending on the section that you want to edit, you may have to follow different steps. For example, direct editing is not possible for the **Name** and **Data Type** sections; instead, you must select the corresponding button to open the pane for editing.

    ![edit-vocabulary-key.gif](../../assets/images/management/data-catalog/edit-vocabulary-key.gif)

### Map one vocabulary key to another

The purpose of vocabulary key mapping is to keep data organized and consistent by preventing duplicate values in the system. For the practical application of vocabulary key mapping, check the video in [Modeling approaches](/management/data-catalog/modeling-approaches).

To demonstrate the importance and efficiency of vocabulary key mapping, let's look at an example. Suppose you have contact records coming into CluedIn from various sources—Salesforce, SAP, and MS SQL Server—and each source has its unique vocabulary. Some properties in data coming from these sources are the same, and some are different. For example, the _gender_ property exists in data from all three sources. It means that _gender_ values would be stored in three separate vocabulary keys. To keep all _gender_ values under one vocabulary key instead of keeping them in each separate vocabulary key, you can map these three vocabulary keys to one, thus improving the organization and getting better visibility of your data.

**To map one vocabulary key to another**

1. Open the vocabulary key that you want to map to another vocabulary key.

1. In the upper-right corner of the vocabulary key details page, select **Edit**.

1. In the **Maps to** section, select **Add mapping**.

1. Find and select a vocabulary key to which you want to map the current vocabulary key. Then, select **Add Key**.

1. Select **Confirm**.

    ![map-vocabulary-key.gif](../../assets/images/management/data-catalog/map-vocabulary-key.gif)

1. Select **Save**, and then confirm your choice.    

    The **Mapped** label appears under the vocabulary key name. Hover over the label to find the vocabulary key to which the current vocabulary key is mapped.

The vocabulary key mapping is executed on the clue level, so the **History** of the golden record does not show source and target properties. However, you can view the source and target properties in the **Explain Log** of the golden record (**Records** > data source > **Translate properties** > **Summaries**).

When you try to use a vocabulary key that is mapped to another vocabulary key, a prompt will inform you of the mapping. Throughout the system, the following guidelines are applied to mapped vocabulary keys:

- When you use a vocabulary key in rules, streams, glossary terms, or anywhere else in the system, and it is mapped to another vocabulary key, the values from the mapped vocabulary key will be used. Essentially, the system takes the left-most vocabulary key and returns the values from the right-most vocabulary key. For example, if vocabulary key A is mapped to vocabulary key B, and vocabulary key B is mapped to vocabulary key C, then when you use vocabulary key A in the filter rule, the values from the vocabulary key C will be returned.

- When you request a specific vocabulary key for display purposes and it is mapped to another vocabulary key, the values from the source vocabulary key will be used. However, because the source vocabulary key is mapped, all its values are stored in the mapped vocabulary key, meaning you won't see any values for the source vocabulary key. For example, if you add a vocabulary key column to the search results page, it will be empty because all values are stored in the mapped vocabulary key.

- When you make changes to the current vocabulary key mapping or to the vocabulary key it is mapped to, the system will evaluate whether these changes are compatible with the vocabulary key configuration.

## Delete a vocabulary key

If you no longer need a vocabulary key, you can delete it. The process of deleting a vocabulary key is different depending on whether the vocabulary key is used anywhere in the system. If a vocabulary key is used somewhere in the system (for example, in a data set mapping, in a golden record, in a rule, and so on), you need to remap the vocabulary key first, and only then you can delete it.

**To delete a vocabulary key**

1. Open the vocabulary key that you want to delete.

1. In the upper-right corner of the vocabulary key details page, select **Edit** > **Remove**.

1. On the **Map to existing** tab, choose whether you want to map the current vocabulary key to another vocabulary key:

    - If the current vocabulary key is used somewhere in the system, the only available option is to map it to another vocabulary key.

    - If the current vocabulary key is not used anywhere in the system, you can delete it right away or you can map it to another vocabulary key.

    After you made your choice, select **Next**.

1. On the **Select vocabulary key** tab, use the search box to find the existing vocabulary key to which you want to map the current vocabulary key. Then, select the checkbox next to the needed key. Finally, select **Next**.

1. On the **Confirm** tab, review the details about the vocabulary key, and select **Confirm**.

    ![delete-vocabulary-key.gif](../../assets/images/management/data-catalog/delete-vocabulary-key.gif)
