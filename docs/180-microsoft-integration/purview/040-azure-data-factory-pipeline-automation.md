---
layout: cluedin
nav_order: 4
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: microsoft-integration/purview/adf-pipeline-automation
title: ADF pipeline automation
last_modified: 2025-04-30
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to configure the Azure Data Factory (ADF) pipeline automation to sync data between Purview and CluedIn.

To configure the ADF pipeline to sync data between Purview and CluedIn, complete three steps:

1. [Prepare ADF resource and ADF service principal in the Azure portal](#preparation-in-azure-portal) – register the ADF application and assign the appropriate permissions.
    
1. [Prepare data source in Purview](#preparation-in-purview) – create a glossary term and associate it with the data sources that you want to sync.

1. [Configure settings in CluedIn](#preparation-in-cluedin) – provide ADF credentials, enable the ADF pipeline automation feature, and provide the glossary term to identify the data sources for syncing.

## Preparation

This section contains the steps required to prepare for syncing data from Purview to CluedIn with the help of ADF pipeline.

### Preparation in Azure portal

1. Register an application for ADF following the steps described in [Register an application and create a service principal](/microsoft-integration/purview/pre-configuration-guide#register-an-application-and-create-a-service-principal). You will need the **Application (client) ID** and **Directory (tenant) ID** to configure ADF in CluedIn.

    ![register-app-adf-spn.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-create-glossary.png" | relative_url }})

1. Create a client secret for ADF application following the steps described in [Register an application and create a service principal](/microsoft-integration/purview/pre-configuration-guide#register-an-application-and-create-a-service-principal).

    ![register-app-adf-client-secret.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-create-glossary.png" | relative_url }})

1. Register ADF application in the key vault that you created in [Create a key vault and register Purview](/microsoft-integration/purview/pre-configuration-guide#create-a-key-vault-and-register-purview):

    1. Go to **Access policies** and select **Create**.

    1. On the **Permissions** tab, in the **Secret permissions** column, select the checkboxes for **Get** and **List**, and then select **Next**.

    1. On the **Principal** tab, find and select the ADF service principal, and then select **Next**.

        ![adf-key-vault.png]({{ "/assets/images/microsoft-integration/purview/adf-key-vault.png" | relative_url }})

    1. Select **Create**.

    1. On the **Application (optional)** tab, select **Next**.

    1. On the **Review + create** tab, select **Create**.

1. Give a Contributor role to the ADF application to the data factory resource:

    1. In the ADF resource, go to **Access control (IAM)**, and then select **Add** > **Add role assignment**.

    1. On the **Role** tab, go to **Privileged administrator roles**, and review information about the **Contributor** role.

        ![adf-assign-contributor-role.png]({{ "/assets/images/microsoft-integration/purview/adf-assign-contributor-role.png" | relative_url }})

    1. Select **Next**.

    1. In **Members** > **Select members**, find and select ADF service principal.

        ![adf-assign-contributor-role-members.png]({{ "/assets/images/microsoft-integration/purview/adf-assign-contributor-role-members.png" | relative_url }})

    1. Select **Review + assign**.

    As a result, the ADF application now has the Contributor access to the data factory resource.

    ![adf-resource-with-adf-service-principal.png]({{ "/assets/images/microsoft-integration/purview/adf-resource-with-adf-service-principal.png" | relative_url }})

### Preparation in Purview

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Unified Catalog** > **Catalog management** > **Classic types**.
    
1. Find and select the glossary that you created in [Sync data sources](/microsoft-integration/purview/sync-data-sources#preparation-in-purview).

1. Add a term to the glossary:

    1. On the terms card, select **View terms**.
    
    1. Select **New term**.
    
    1. Select the **System default** term template and select **Continue**.
    
    1.  Enter the **Name** of the term and select **Create**.

    The new term is added to the glossary. Next, add the term to the asset that you want to sync with CluedIn.

    ![adf-new-term.png]({{ "/assets/images/microsoft-integration/purview/adf-new-term.png" | relative_url }})

1. To add the term to the asset that you want to sync with CluedIn:

    1. Navigate to **Data Map** > **Domains**. In your default domain, select the collection that stores the assets from Azure Data Lake Storage.

    1. Select the assets card.

    1. Find and select the asset that you want to sync with CluedIn.

    1. On the asset details page, select **Edit**.

    1. In **Glossary terms**, find and select the term you created in step 3.

        ![adf-add-term-to-asset.png]({{ "/assets/images/microsoft-integration/purview/adf-add-term-to-asset.png" | relative_url }})

    1. Select **Save**.

    The term is added to the asset that you want to sync with CluedIn. On the term details page, you can find the assets associated with the term.

    ![adf-term-with-asset.png]({{ "/assets/images/microsoft-integration/purview/adf-term-with-asset.png" | relative_url }})

    Once you have prepared the data sources that you want to sync, configure the appropriate settings in CluedIn.

### Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.

1. In **Azure Data Factory Base Url**, enter the resource ID of your ADF resource. To find the resource ID, go to your ADF resource, select **JSON View**, and then copy the value of **Resource ID**. The resource ID should be in the following format: `https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.DataFactory/factories/{factoryName}/`.

    ![adf-resource-id.png]({{ "/assets/images/microsoft-integration/purview/adf-resource-id.png" | relative_url }})

1. In **Azure Data Factory Client ID**, enter a unique identifier assigned to the ADF application when you registered it in Microsoft Entra ID. You can find this value on the application overview page, in **Application (client) ID**.

1. In **Azure Data Factory Client Secret**, enter a string value that your ADF application uses to prove its identity when requesting a token.

1. In **Azure Data Factory Tenant ID**, enter a unique identifier for your Microsoft Entra ID tenant in which your ADF application is registered.
You can find this value on the application overview page, in **Directory (tenant) ID**.

1. Turn on the toggle in **Azure Data Factory Pipeline Automation**.

1. In **ADF Pipeline Automation Term Pattern**, enter the name of the term that is associated with assets you want to ingest into CluedIn via automated pipeline.

    ![adf-cluedin-settings.png]({{ "/assets/images/microsoft-integration/purview/adf-cluedin-settings.png" | relative_url }})

1. Select **Save**.

    Once you save the changes, the data will start to come forward to CluedIn ingestion endpoint.

## Feature overview

When the synchronization is completed, you will receive a notification.

![adf-notifications.png]({{ "/assets/images/microsoft-integration/purview/adf-notifications.png" | relative_url }})

**How to check the pipelines in ADF?**

The ADF pipelines are created automatically for each Purview asset. To verify the pipelines in ADF, go to **Author**, and then do the following:

1. Expand the **Pipelines** dropdown list – you will see the pipeline that has been created automatically.

1. Expand the **Datasets** dropdown list – you will see the dataset that has been sent to CluedIn as well as REST connection to CluedIn ingestion endpoint.

    ![adf-pipelines.png]({{ "/assets/images/microsoft-integration/purview/adf-pipelines.png" | relative_url }})

Additionally, go to **Manage** > **Linked services**. Here, you will see the linked services that define connection information to a data store. For example, in the following screenshot, there are three linked services:

1. Azure Data Lake Storage – connects ADF to your Azure Data Lake Storage account and allows you to copy data from the storage account.

1. Azure Key Vault – connects ADF to Azure Key Vault, where ADF retrieves the credentials at runtime to access the data store.

1. REST – connects ADF to CluedIn ingestion endpoint.

    ![adf-linked-services.png]({{ "/assets/images/microsoft-integration/purview/adf-linked-services.png" | relative_url }})

Finally, go to **Monitor** > **Pipeline runs** to verify that the pipeline has run successfully.

![adf-pipeline-runs.png]({{ "/assets/images/microsoft-integration/purview/adf-pipeline-runs.png" | relative_url }})

**How to check the ingested data in CluedIn?**

As a result of pipeline run, the data source in CluedIn now contains a data set.

![adf-ingested-data.png]({{ "/assets/images/microsoft-integration/purview/adf-ingested-data.png" | relative_url }})
