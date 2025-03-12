---
layout: cluedin
title: Sync Data Products
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/purview/features/sync-dataproducts
nav_order: 090
has_children: false
tags: ["integration", "microsoft", "azure", "purview", "collection", "sync", "dataproduct", "dataasset"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

## Sync Data Products Settings

This feature will enable you to sync the Purview Data Products and Data Assets into CluedIn DataSources. The data source groups can be viewed in **Integrations** > **Data Sources**.

![Settings Sync Data Products](../media/settings-sync-dataproducts.png)

## Sync Data Products by Glossary Term
There are 2 ways to select the Glossary Term that you want to sync.

![Glossary Term Setup](../media/data-product-glossary-term-setup.png)

1. By providing the Glossary Term ID, which can be found in the Url path.

1. By providing the Glossary Term Name. In case you implemented a multiple glossary term with the same name.


#### Link Glossary Term to Data Product

In the Glossary Term Page, you can see a `Link `data product` on the right-hand side of the screen.

![Glossary Term Setup](../media/assign-glossary-term-to-dataproduct.png)

## Purview Data Product Preview

Let's break down the details we can see in the Purview Data Product Page

- Data Product name - **Customer Journey**
- Data Product Type - **Master data and reference data**
- Data Assets Count - **10** 
- Linked Glossary Term - **Sync to CluedIn**

![Purview Data Products](../media/purview-dataproduct.png)

Navigating to the list of associated Data Assets to the Data Product

![Purview Data Products Data Assets](../media/purview-dataproduct-dataaassets.png)

## CluedIn Syncronization

When the CluedIn Job executes and synchronizes the Purview Data Products to CluedIn. New `DataSources` will be created.

![Data Product DataSources](../media/sync-dataproducts-to-cluedin-dataSets.png)

![Data Product DataSources](../media/sync-dataassets-to-cluedin-datasources.png)

Requirements to Sync
- Data Product Status must be **_Published_**
- Data Product Type must be **_Master data and Reference data_**
- Data Product must be in a valid Glossary Term _(see next section below)_


## Append Asset to Data Product

As we write back to Purview the CluedIn Assets, we are now able to easily see the Assets we are creating by adding this into the associated Data Product that we synchronize.

![Data Product DataSources](../media/add-dataasset-to-dataproduct.png)

Requirements to Sync

- `Service Principal` must be in the Business Domain Role **Data Product Owner**. Please see the _Setup Permissions_ document.