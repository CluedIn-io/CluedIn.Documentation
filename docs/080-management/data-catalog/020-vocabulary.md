---
layout: cluedin
nav_order: 2
parent: Data catalog
grand_parent: Management
permalink: /management/data-catalog/vocabulary
title: Vocabulary
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to create and manage vocabularies to enhance the efficiency and organization of metadata in CluedIn.

## Vocabulary overview

A vocabulary is a framework that defines how metadata is stored and organized within the system. The primary purpose of vocabulary is to hold vocabulary keys.

A well-defined vocabulary is essential for maintaining data consistency, accuracy, and usability across an organization. By providing a standardized framework, a vocabulary contributes to effective data integration, improved decision making, and streamlined operations. It ensures that all stakeholders are working with consistent and reliable master data definitions and structures.

In CluedIn, all vocabularies are stored in **Management** > **Data Catalog** > **View All Vocabularies**.

## Vocabulary details page

On the vocabulary details page, you can view relevant information about a vocabulary and take other actions to [manage a vocabulary](#manage-a-vocabulary).

**Configuration**

This tab contains general information about the vocabulary, including:

- Vocabulary name – a user-friendly identifier of the vocabulary.

- Primary business domain – a business domain linked with the vocabulary.

- Source – a source system that indicates the origin of data within the vocabulary.

- Key prefix – a namespace that is added before vocabulary key names for consistent naming, efficient searching, and data filtering.

- Description – a summary that explains the purpose of the vocabulary. You can add rich formatting to the description, such as bolding, underlining, or italicizing text.

You can edit any aspect of the vocabulary configuration, with the exception of the key prefix. 

**Usage**

This tab provides the global view of vocabulary usage in the system: number of golden records, streams, glossary terms, and rules where the vocabulary is used. By selecting the respective button, you can access a list of streams, glossary terms, and rules, along with links to the corresponding elements in the system.

![vocabulary-usage.gif](../../assets/images/management/data-catalog/vocabulary-usage.gif)

**Owners**

This tab contains a list of users who can manage the vocabulary (Vocabulary Owners). You can add or remove vocabulary owners if necessary.

**Vocabulary keys**

This tab contains groups of vocabulary keys associated with the vocabulary. You can search for specific keys or use [data type](/management/data-catalog/data-types) and classification filters to explore the available metadata within the vocabulary.

![vocabulary-keys.gif](../../assets/images/management/data-catalog/vocabulary-keys.gif)

For information on how to manage vocabulary keys, see [Vocabulary keys](/management/data-catalog/vocabulary-keys).

**Pending changes**

This tab contains tasks for reviewing changes to the vocabulary submitted by users who are not Vocabulary Owners.

**Audit log**

This tab contains a detailed history of changes to the vocabulary, such as:

- Create a vocabulary
- Added user to owners
- Create a vocabulary key
- Delete a vocabulary key

## Create a vocabulary

Depending on the selected [data modeling approach](/management/data-catalog/modeling-approaches), you can create a vocabulary in two ways:

- **Automatically** – this option is part of the data-first approach. When [creating a mapping](/integration/create-mapping) for a data set, you have the option to enter the name of a new vocabulary. CluedIn will then automatically suggest the key prefix and generate the vocabulary. Once the mapping is created, you can then open the vocabulary and make any necessary adjustments.

- **Manually** – this option is part of the model-first approach, which assumes that you need to create a vocabulary before using it in the mapping for a data set. The following procedure outlines the steps to manually create a vocabulary.

**To create a vocabulary**

1. On the navigation pane, go to **Management** > **Data Catalog**. Then, select **View All Vocabularies**.

1. Select **Create Vocabulary**.

1. Enter the name of the vocabulary.

1. Find and select the primary business domain that will most likely use the vocabulary.

1. (Optional) Find and select the source of the vocabulary to indicate where the data in the vocabulary comes from.

1. Enter the key prefix of the vocabulary that will be added before vocabulary key names.

    {:.important}
    The key prefix cannot start with a number, but it can include numbers in other positions. Additionally, the key prefix must not contain special characters or spaces. Note that it is not possible to edit the key prefix once the vocabulary has been created.

1. (Optional) Enter the description of the vocabulary.

1. Select **Create**.

    ![create-vocabulary.gif](../../assets/images/management/data-catalog/create-vocabulary.gif)

    The vocabulary page opens, where you can view and manage vocabulary details.
    
## Manage a vocabulary

Once the vocabulary is created, you can edit its configuration based on your requirements to ensure the maintenance of organized and consistent metadata.

Only Vocabulary Owners and Administrators can edit the vocabulary configuration. When you're editing a vocabulary configuration, you can change almost all of its aspects: name, primary business domain, source, and description.

**To edit vocabulary configuration**

1. In the upper-right corner of the vocabulary, select **Edit**.

1. Make the needed changes, and then select **Save** and confirm your choice.

    ![edit-vocabulary.gif](../../assets/images/management/data-catalog/edit-vocabulary.gif)