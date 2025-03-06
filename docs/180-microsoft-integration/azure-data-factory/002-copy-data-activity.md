---
layout: cluedin
title: Configure ADF pipeline with Copy data activity
parent: Azure Data Factory Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/adf-integration/copy-data
nav_order: 020
has_children: false
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This guide provides step-by-step instructions on how to configure an Azure Data Factory (ADF) Copy data activity to send data to CluedIn using a private endpoint. 

**Prerequisites** 

- Configure a private link service between ADF and CluedIn as described in [Configure ADF with private link](https://documentation.cluedin.net/microsoft-integration/adf-integration/private-link).

- Make sure you have Azure Data Lake with some CSV data. 

- Create an ingestion endpoint and authorization token in CluedIn as described in [Add ingestion endpoint](https://documentation.cluedin.net/integration/endpoint#add-ingestion-point). 

Configuring ADF pipeline with the Data flow activity consists of 4 steps:

1.  [Creating a new pipeline](#ceate-pipeline)
    
2.  [Configuring the source](#configure-source)
    
3.  [Configuring the sink](#configure-sink)
    
4.  [Debugging the pipeline](#debug-and-validate-pipeline)

## Create a pipeline

1. On the home page of Azure Data factory, select **New** > **Pipeline**.

1. In the **Activities** pane, expand the **Move and Transform** category, and then drag the **Copy data** activity to the pipeline canvas.

    ![copy-data-activity.png](../../assets/images/microsoft-integration/azure-data-factory/copy-data-activity.png)

## Configure source

1. Go to the **Source** tab. Select **+ New** to create a source dataset.

1. In the **New dataset** pane, find and select **Azure Data Lake Storage Gen2**, and then select **Continue**.

1. In the **Select format** pane, select **DelimitedText**, and then select **Continue**.

1. In the **Set properties** pane, enter the name for the dataset. Then, in the **Linked service** field, expand the dropdown and select **+ New**.

1. In the **New linked service** pane, provide the following details:
 
    - **Name** – enter the name for your linked service.

    - **Account selection method** – select **From Azure subscription**.

    - **Azure Subscriptions** – select the subscription of your Azure Data Lake.

    - **Storage account name** – select the name of your Azure Data Lake storage account.

1. Test connection, and then select **Create**.

    After the linked service is created, you'll be taken back to the **Set properties** pane.

1. In the **File path** section, add the path to the appropriate folder/file of your Azure Data Lake.

1. Select **OK**.

    ![configure-source.png](../../assets/images/microsoft-integration/azure-data-factory/configure-source.png)

## Configure sink

1.  Go to the **Sink** tab. Select **+ New** to create a sink dataset.

1. In the **New dataset** pane, find and select **REST**, and then select **Continue**.

1. In the **Set properties** pane, enter the name for the dataset. Then, in the **Linked service** field, expand the dropdown and select **+ New**.

1. In the **New linked service** pane, provide the following details:

    - **Name** – enter the name for your linked service.

    - **Base URL** – enter the URL of the ingestion endpoint in CluedIn. For more information, see [Send data](/integration/endpoint#send-data).

    - **Authentication type** – select **Anonymous**.

    - **Auth headers** – add a new header with the following details:

        - **Name** – enter **Authorization**.

        - **Value** – enter **Bearer**, add a space, and then paste the token from CluedIn. For more information, see [Send data](/integration/endpoint#send-data).

    ![configure-sink-new-linked-service.png](../../assets/images/microsoft-integration/azure-data-factory/configure-sink-new-linked-service.png)

1. Test connection, and then select **Create**.

    After the linked service is created, you'll be taken back to the **Set properties** pane.

1. Select **OK**.

1. In the Request method field, select **POST**.

    ![configure-sink-request-method.png](../../assets/images/microsoft-integration/azure-data-factory/configure-sink-request-method.png)

## Debug and validate pipeline

Once the source and sink are configured, you can debug the pipeline to ensure it is working.

**To debug the pipeline**

1. On the toolbar, select **Debug**. You can see the status of the pipeline run in the **Output** tab at the bottom of the window.

    ![debug-pipeline.png](../../assets/images/microsoft-integration/azure-data-factory/debug-pipeline.png)

The following image illustrates the ingestion endpoint in CluedIn before debugging the pipeline.

![before-debug.png](../../assets/images/microsoft-integration/azure-data-factory/before-debug.png)

The following image the ingestion endpoint in CluedIn after debugging the pipeline.

![after-debug.png](../../assets/images/microsoft-integration/azure-data-factory/after-debug.png)