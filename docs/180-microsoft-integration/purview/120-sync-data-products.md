---
layout: cluedin
nav_order: 12
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: microsoft-integration/purview/sync-data-products
title: Sync data products
last_modified: 2025-04-30
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to sync Purview data products and data assets into CluedIn data sources. This feature works only if Azure Data Factory (ADF) automation is enabled and configured. For more information, see [Azure Data Factory pipeline automation](/microsoft-integration/purview/adf-pipeline-automation).

## Preparation

To sync Purview data products and data assets into CluedIn data sources, complete 2 preparation steps:

1. [Prepare a data product in Purview](#preparation-in-purview) – create a governance domain and a glossary term to act a filter for the data products you want to sync, create a data product and add data assets and a glossary term to it, publish the prepared resources, and finally assign the appropriate roles to Purview service principal in the governance domain.
    
2. [Configure settings in CluedIn](#preparation-in-cluedin) – enable the sync data products feature in Purview settings and provide the glossary term to identify the data products for syncing.

### Preparation in Purview

**To create a governance domain**

1. In the [Microsoft Purview portal](https://purview.microsoft.com), navigate to **Unified Catalog** > **Catalog management** > **Governance domain**.

1. Select **new governance domain**.

    ![sync-data-products-new-governance-domain.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-new-governance-domain.png" | relative_url }})

1. Enter the **Name** of the governance domain.

1. Enter the **Description** of the governance domain.

1. Select the **Type** of the governance domain.

    ![sync-data-products-new-governance-domain-creation.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-new-governance-domain-creation.png" | relative_url }})

1. Select **Save**.

The governance domain should have a dedicated glossary term that acts as a filter for the data products you want to sync.

**To create a glossary term for a governance domain**

1. On the governance domain details page, in the glossary terms card, select **View all**.

1. Select **New term**.

1. Enter the **Name** and **Description** of the term.

    ![sync-data-products-new-glossary-term.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-new-glossary-term.png" | relative_url }})

1. Select **Create**.

When the glossary term is created, note two methods for obtaining its identification:

1. The name of the glossary term.

1. The ID of the glossary term, which can be found in the URL.

    ![sync-data-products-glossary-term-identification.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-glossary-term-identification.png" | relative_url }})

**To create data products**

1. On the governance domain details page, in the data products card, select **Go to data products**.

1. Select **New data product**.

1. Enter the **Name** and **Description** of the data product.

1. In **Type**, select **Master data and reference data**.

    ![sync-data-products-new-data-product.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-new-data-product.png" | relative_url }})

1. Select **Next**.

1. Enter the **Use cases** for the data product.

    ![sync-data-products-new-data-product-business-details.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-new-data-product-business-details.png" | relative_url }})

1. In **Next steps**, select **Add data assets**.

1. Select **Done**.

**To add data assets to the data product**

1. On the data product details page, expand the **Add data assets** dropdown list, and then select **Find and select**.

1. Find and select the data asset that you want to add to the data product.

    ![sync-data-products-find-and-select.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-find-and-select.png" | relative_url }})

1. Select **Add**.

    As a result, the data assets are added to the data product.

    ![sync-data-products-data-assets.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-data-assets.png" | relative_url }})

**To add a glossary term to the data product**

1. On the data product details page, in the **Glossary terms** section, select **Add**.

1. Find and select the glossary term that you want to add to the data product.

    ![sync-data-product-select-glossary-term.png]({{ "/assets/images/microsoft-integration/purview/sync-data-product-select-glossary-term.png" | relative_url }})

1. Select **Add**.

    As a result, the glossary term is added to the data product.

    ![sync-data-products-details-page.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-details-page.png" | relative_url }})

**To publish a governance domain**

- On the governance domain details page, select **Publish**.

    ![synd-data-products-publish.png]({{ "/assets/images/microsoft-integration/purview/synd-data-products-publish.png" | relative_url }})

    After successful publishing, the status of the governance domain changes to **Successful**.

**To publish a glossary term**

1. On the governance domain details page, in the glossary terms card, select **View all**.

1. Select the glossary term that you created before.

1. On the glossary term detail page, select **Publish**.

**To publish a data product**

1. On the governance domain details page, in the data products card, select **Go to data products**.

1. Select the data product that you created before.

1. On the data product detail page, select **Publish**.

**To assign roles to service principal**

1. On the governance domain details page, go to the **Roles** tab.

1. Find the **Data Catalog Reader** role, and then select the icon next to the role name.

1. Find and select the Purview service principal.

    ![sync-data-products-data-catalog-reader.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-data-catalog-reader.png" | relative_url }})

1. Select **Save**.

1. Find the **Data Product Owners** role, and then select the icon next to the role name.

1. Find and select the Purview service principal.

    ![sync-data-products-data-product-owners.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-data-product-owners.png" | relative_url }})

1. Select **Save**.

### Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.

1. Turn on the toggle in **Sync Data Products DataSources**.

1. In **Sync Data Products Term Pattern**, enter the identification of the glossary term that is associated with the governance domain that you want to sync. 

1. If you want to automatically add the asset that has been already synced to CluedIn to the list of data assets of a specific data product, turn on the toggle in **Append Asset to Data Product**.

    ![sync-data-products.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products.png" | relative_url }})

1. Select **Save**.

    Once you save the changes, synchronization begins.

## Feature overview

Once you enable synchronization of data products, you will receive a notification when the data product is synced.

![sync-data-products-notification.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-notification.png" | relative_url }})

Additionally, you will receive notifications about the execution of ADF automation pipelines, which create ingestion endpoints in CluedIn and ingest the data from data assets.

![sync-data-products-adf-notification.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-adf-notification.png" | relative_url }})

**How to check the ingested data in CluedIn?**

As a result of pipeline run, a new data source group is created in CluedIn. The data source group corresponds to Purview data product, and the data sources within the group correspond to data assets within the data product.

![sync-data-products-result.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-result.png" | relative_url }})

After you create the mapping and process the data set, it will be synced to Purview.

![sync-data-products-notification-sync-to-purview.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-notification-sync-to-purview.png" | relative_url }})

As a result, you can view a visual representation of an asset within the CluedIn processing pipeline.

![sync-data-products-sync-to-purview-lineage.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-sync-to-purview-lineage.png" | relative_url }})

Since we enabled **Append Asset to Data Product**, a new asset is created in the data product to represent the entity type that was created in CluedIn.

![sync-data-products-append-assets.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-append-assets.png" | relative_url }})