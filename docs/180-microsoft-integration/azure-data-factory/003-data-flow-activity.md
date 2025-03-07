---
layout: cluedin
title: Configure ADF pipeline with Data flow activity
parent: Azure Data Factory Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/adf-integration/data-flow-activity
nav_order: 030
has_children: false
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This guide provides step-by-step instructions for configuring an Azure Data Factory (ADF) Data flow activity to send data to CluedIn. This integration enables seamless data transfer from your Azure Data Lake (or other sources) to CluedIn using a private endpoint.

The Data flow activity in ADF is ideal when data transformations such as aggregation, filtering, or applying complex business logic are required before sending data to CluedIn. If no transformations are needed, use the [Copy data activity](/microsoft-integration/adf-integration/copy-data) instead.

**Prerequisites** 

- Configure a private link service between ADF and CluedIn as described in [Configure ADF with private link](https://documentation.cluedin.net/microsoft-integration/adf-integration/private-link).

- Ensure your data is available within Azure, commonly stored in Azure Data Lake or Blob Storage.

- Create an ingestion endpoint and authorization token in CluedIn as described in [Add ingestion endpoint](https://documentation.cluedin.net/integration/endpoint#add-ingestion-endpoint). 

Configuring an ADF pipeline with the Data flow activity consists of 4 steps:

1.  [Creating a new pipeline](#ceate-pipeline)
    
2.  [Configuring the source](#configure-source)
    
3.  [Configuring the sink](#configure-sink)
    
4.  [Debugging the pipeline](#debug-and-validate-pipeline)

## Create a new pipeline

1. On the Azure Data Factory home page, select **New** > **Pipeline**.

1. In the **Activities** pane, expand the **Move and transform** category, and then drag the **Data flow** activity to the pipeline canvas.

1. Select the new Data flow activity on the canvas, and then go to the **Settings** tab to edit its details.

    ![data-flow-settings.png](../../assets/images/microsoft-integration/azure-data-factory/data-flow-settings.png)

## Configure source

1. Next to the **Data flow** field, select **+ New**.

    ![data-flow-new.png](../../assets/images/microsoft-integration/azure-data-factory/data-flow-new.png)

1. Select **Add Source**.

    ![data-flow-add-source.png](../../assets/images/microsoft-integration/azure-data-factory/data-flow-add-source.png)

1. On the **Source Settings** tab, do the following:

    1. Enter the **Output stream name**.

    1. In **Source type**, select **Dataset**.

    1. Next to the **Dataset** dropdown list, select **+ New**.

        ![data-flow-new-dataset.png](../../assets/images/microsoft-integration/azure-data-factory/data-flow-new-dataset.png)

1. In the **New dataset** pane, select your data stored within an Azure storage account (for example, Azure Data Lake Storage Gen2). Then, select **Continue**.

    ![data-flow-new-data-set.png](../../assets/images/microsoft-integration/azure-data-factory/data-flow-new-data-set.png)

1. In the **Select format** pane, select **DelimitedText**, and then select **Continue**.

    ![data-flow-delimited-text.png](../../assets/images/microsoft-integration/azure-data-factory/data-flow-delimited-text.png)

1. In the **Set properties** pane, enter the name for the dataset. Then, expand the **Linked service** dropdown list, and select **+ New**.

    ![data-flow-set-properties.png](../../assets/images/microsoft-integration/azure-data-factory/data-flow-set-properties.png)

1. Configure the service details:

    - **Name** – enter the name for your linked service.

    - **Account selection method** – select **From Azure subscription**.

    - **Azure subscription** – select the subscription of your Azure Data Lake.

    - **Storage account name** – select the name of your Azure Data Lake storage account.

        ![data-flow-new-linked-service.png](../../assets/images/microsoft-integration/azure-data-factory/data-flow-new-linked-service.png)

1. Test the connection and then create the new linked service.
    
2. On the **Set properties** pane, in the **File path** section, add the path to the appropriate folder/file within your Azure Data Lake.

    ![set-properties.png](../../assets/images/microsoft-integration/azure-data-factory/set-properties.png)
    
3.  Select **OK**.

## Configure sink

1. Next to the data source, select the plus icon, and then find and select **Sink**.

    ![data-flow-sink.png](../../assets/images/microsoft-integration/azure-data-factory/data-flow-sink.png)

1. On the **Sink** tab, do the following:

    1. Enter the **Output stream name**.

    1. In **Incoming stream**, make sure the data source created in the [previous step](#configure-source) is selected.

    1. In **Sink type**, select **Dataset**.

    1. Next to the **Dataset** dropdown list, select **+ New**.

        ![data-flow-sink-configuration.png](../../assets/images/microsoft-integration/azure-data-factory/data-flow-sink-configuration.png)

1. In the **New dataset** pane, find and select **REST**, and then select **Continue**.

    ![new-dataset-rest.png](../../assets/images/microsoft-integration/azure-data-factory/new-dataset-rest.png)

1.  In the **Set properties** pane, enter the name for the dataset. Then, expand the **Linked service** dropdown list and select **+ New**.

    ![rest-set-properties.png](../../assets/images/microsoft-integration/azure-data-factory/rest-set-properties.png)

1. Configure the service details:

    - **Name** – enter the name for your linked service.
    
    - **Base URL** – enter the URL of the ingestion endpoint in CluedIn. You can find this URL in the data set that you created for ingesting data into CluedIn. For more information, see [Send data](https://documentation.cluedin.net/integration/endpoint#send-data).

        ![set-properties-post-url.png](../../assets/images/microsoft-integration/azure-data-factory/set-properties-post-url.png)
    
    - **Authentication type** – select **Anonymous**.

    - **Auth headers** – add a new header with the following details:

        - **Name** – enter **Authorization**.
        
        - **Value** – enter **Bearer**, add a space, and then paste the token from CluedIn. You can find the token in CluedIn by going to **Administration** > **API Tokens**.  For more information, see [Send data](https://documentation.cluedin.net/integration/endpoint#send-data).

            ![set-properties-api-token.png](../../assets/images/microsoft-integration/azure-data-factory/set-properties-api-token.png)

        As a result, the new linked service should be configured similar to the following.

        ![new-linked-service-rest.png](../../assets/images/microsoft-integration/azure-data-factory/new-linked-service-rest.png)

1. Test connection, and then select **Create**.

1. After the sink is configured, go to the **Settings** tab, and then do the following:

    - Ensure the **Insert method** is set to **POST**. 
    
    - Change the **Delete method**, **Upsert method**, and **Update method** to **None**.

    - Set the **Http Compression type** to **GZip**.

    - Set the **Batch size** to **10,000** to ensure smoother transfer.

        ![sink-settings.png](../../assets/images/microsoft-integration/azure-data-factory/sink-settings.png)

## Debug and validate pipeline

Once the source and sink are configured, you can debug the pipeline to ensure it works correctly.

**To debug the pipeline**

1. On the toolbar, select **Debug**.

1. In the **Output** tab at the bottom of the window, monitor the pipeline run status.

    Once triggered successfully, you should see data flowing into CluedIn.

    ![after-debug.png](../../assets/images/microsoft-integration/azure-data-factory/after-debug.png)