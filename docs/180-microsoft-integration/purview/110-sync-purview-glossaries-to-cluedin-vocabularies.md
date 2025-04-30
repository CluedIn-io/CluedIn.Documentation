---
layout: cluedin
nav_order: 11
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/purview/sync-purview-glossaries-to-cluedin-vocabularies
title: Sync Purview glossaries to CluedIn vocabularies
last_modified: 2025-04-30
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to sync Purview glossaries to CluedIn vocabularies.

## Preparation

To sync glossaries from Purview to CluedIn vocabularies and vocabulary keys, complete 2 preparation steps:

1. [Prepare glossary terms in Purview](#preparation-in-purview) – create a new term template with an attribute to indicate that glossary terms can be synced to CluedIn vocabulary keys and prepare glossary terms for syncing.

1. [Configure settings in CluedIn](#preparation-in-cluedin) – enable the sync Purview glossaries to CluedIn vocabularies feature and provide the attribute to identify the glossary terms for syncing. 

### Preparation in Purview

Make sure you have the existing classic type glossary that contains some glossary terms along with child glossary terms. The child glossary terms in Purview must be assigned to the schema of the asset that is synced with CluedIn. Purview glossary terms will be synced to CluedIn vocabularies and Purview child glossary terms will be synced to CluedIn vocabulary keys.

On the following screenshot, we have the CluedIn glossary that contains 7 glossary terms. The Contact glossary term contains 2 child glossary terms: Email and FullName. In this section, you will find an instruction on how to prepare these two child glossary terms for synchronization with CluedIn.

![sync-purview-glossary-to-cluedin-vocabulary-child-terms.png](../../assets/images/microsoft-integration/purview/sync-purview-glossary-to-cluedin-vocabulary-child-terms.png)

Additionally, the glossary terms should contain an attribute to indicate that they can be synced to CluedIn vocabulary keys. The name of this attribute should be the same as in the **Glossary to Vocabulary Attribute Filter** field from [CluedIn settings](#preparation-in-cluedin). The default value is _CluedInVocab_. You can create this attribute in Purview with the help of a new term template.

**To create a new term template**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Unified Catalog** > **Catalog management** > **Classic types**, and then select the glossary that contains the term you want to sync to CluedIn.

1. On the glossary terms details page, select **New term**.

1. Select **New term template**.

1. Enter the **Template name**.

    ![new-term-template.png](../../assets/images/microsoft-integration/purview/new-term-template.png)

1. Select **New attributes**.

1. Enter the **Attribute name**. It should be the same as in the **Glossary to Vocabulary Attribute Filter** field from CluedIn settings. The default value is _CluedInVocab_.

1. In **Field type**, select **Boolean**.

    ![new-attribute.png](../../assets/images/microsoft-integration/purview/new-attribute.png)

1. Select **Apply**, and then select **Create**.

    Now, when you create a new glossary term that you want to sync to CluedIn vocabulary key, set the attribute to **True**.

    ![new-term-from-cluedin-template.png](../../assets/images/microsoft-integration/purview/new-term-from-cluedin-template.png)

**To prepare Purview child glossary terms**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Data Map** > **Domains**. In your default domain, select the collection that stores the assets from Azure Data Lake Storage.

1. Select the assets card.

1. Find and select the asset that is synced with CluedIn.

1. On the asset details page, select **Schema**.

1. Find and select the column that should be associated with the child glossary term that you want to sync. 

    ![sync-purview-glossary-to-cluedin-vocabulary-asset.png](../../assets/images/microsoft-integration/purview/sync-purview-glossary-to-cluedin-vocabulary-asset.png)

1. On the column details pane, select **Edit**.

    ![sync-purview-glossary-to-cluedin-vocabulary-schema-edit.png](../../assets/images/microsoft-integration/purview/sync-purview-glossary-to-cluedin-vocabulary-schema-edit.png)

1. In **Glossary terms**, find and select the child glossary term that you want to assign to the column.

    ![sync-purview-glossary-to-cluedin-vocabulary-fullname-edit.png](../../assets/images/microsoft-integration/purview/sync-purview-glossary-to-cluedin-vocabulary-fullname-edit.png)

1. Select **Save**.

    The child glossary term is now associated with the column.

    ![sync-purview-glossary-to-cluedin-vocabulary-fullname-glossary-term.png](../../assets/images/microsoft-integration/purview/sync-purview-glossary-to-cluedin-vocabulary-fullname-glossary-term.png)

1. Repeat steps 1–8 for all child glossary terms that you want to sync to CluedIn vocabularies.

### Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.
    
1. Turn on the toggle in **Sync Purview glossaries to CluedIn glossaries**.

1. You can leave the other settings for this feature at their default values.

    ![sync-purview-glossary-to-cluedin-vocabulary-settings.png](../../assets/images/microsoft-integration/purview/sync-purview-glossary-to-cluedin-vocabulary-settings.png)

1. Select **Save**.

## Feature demonstration

Once you enable synchronization of Purview glossaries to CluedIn vocabularies, you will receive a notification when the vocabulary key is created in CluedIn. If there are matching CluedIn vocabularies, they will be updated; otherwise, new CluedIn vocabularies are created for the incoming Purview glossaries.

**To find synced vocabulary keys in CluedIn**

1. On the navigation pane, go to **Management** > **Data Catalog** > **View All Vocabularies**.

1. Find and expand the vocabulary that is named as the Purview glossary term.

    The vocabulary (a) corresponds to the glossary term in Purview. It contains vocabulary keys (b) that correspond to child glossary terms in Purview. According to default settings, the vocabulary is automatically associated with the Purview/Contact entity type, and the vocabulary key prefix is "purview". However, you can change these settings if needed.

    ![sync-purview-glossary-to-cluedin-vocabulary-result.png](../../assets/images/microsoft-integration/purview/sync-purview-glossary-to-cluedin-vocabulary-result.png)