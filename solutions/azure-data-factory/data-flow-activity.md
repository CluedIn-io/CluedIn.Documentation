---
title: Configure ADF pipeline with Data flow activity
url: https://documentation.cluedin.net/solutions/azure-data-factory/data-flow-activity
content_type: how-to
section: Solutions & integrations > Azure Data Factory
---

# Configure ADF pipeline with Data flow activity

> how-to: Steps to accomplish one task.

This guide provides step-by-step instructions for configuring an Azure Data Factory (ADF) Data flow activity to send data to CluedIn. This integration enables seamless data transfer from your Azure Data Lake (or other sources) to CluedIn using a private endpoint.

The Data flow activity in ADF is ideal when data transformations such as aggregation, filtering, or applying complex business logic are required before sending data to CluedIn. If no transformations are needed, use the [Copy data activity](https://documentation.cluedin.net/solutions/azure-data-factory/copy-data.md) instead.

**Prerequisites** 

- Configure a private link service between ADF and CluedIn as described in [Configure ADF with private link](https://documentation.cluedin.net/microsoft-integration/adf-integration/private-link).

- Ensure your data is available within Azure, commonly stored in Azure Data Lake or Blob Storage.

- Create an ingestion endpoint and authorization token in CluedIn as described in [Add ingestion endpoint](https://documentation.cluedin.net/integration/endpoint#add-ingestion-endpoint). 

Configuring an ADF pipeline with the Data flow activity consists of 4 steps:

1. [Creating a new pipeline](#ceate-pipeline)

2. [Configuring the source](#configure-source)

3. [Configuring the sink](#configure-sink)

4. [Debugging the pipeline](#debug-pipeline-in-adf)

5. [Validating the result in CluedIn](#validate-result-in-cluedin)

## Create a new pipeline

1. On the Azure Data Factory home page, select **New** > **Pipeline**.

1. In the **Activities** pane, expand the **Move and transform** category, and then drag the **Data flow** activity to the pipeline canvas.

1. Select the new Data flow activity on the canvas, and then go to the **Settings** tab to edit its details.

    ![A Data flow activity on the pipeline canvas with its Settings tab highlighted, showing the Data flow, Run on (Azure IR) and Compute size fields](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-settings.png)

## Configure source

1. Next to the **Data flow** field, select **+ New**.

    ![The Settings tab with the + New button next to the Data flow field highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-new.png)

1. Select **Add Source**.

    ![A new empty data flow canvas with the Add Source box highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-add-source.png)

1. On the **Source Settings** tab, do the following:

    1. Enter the **Output stream name**.

    1. In **Source type**, select **Dataset**.

    1. Next to the **Dataset** dropdown list, select **+ New**.

        ![The Source settings tab with output stream name Training, source type Dataset and the + New button next to Dataset highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-new-dataset.png)

1. In the **New dataset** pane, select your data stored within an Azure storage account (for example, Azure Data Lake Storage Gen2). Then, select **Continue**.

    ![The New dataset pane searched for and showing Azure Data Lake Storage Gen2 selected](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-new-data-set.png)

1. In the **Select format** pane, select **DelimitedText**, and then select **Continue**.

    ![The Select format pane with Avro, DelimitedText and Excel options, DelimitedText selected](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-delimited-text.png)

1. In the **Set properties** pane, enter the name for the dataset. Then, expand the **Linked service** dropdown list, and select **+ New**.

    ![The Set properties pane with name Training and the Linked service dropdown open, + New highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-set-properties.png)

1. Configure the service details:

    - **Name** – enter the name for your linked service.

    - **Account selection method** – select **From Azure subscription**.

    - **Azure subscription** – select the subscription of your Azure Data Lake.

    - **Storage account name** – select the name of your Azure Data Lake storage account.

        ![The New linked service form for Azure Data Lake Storage Gen2 with name, integration runtime, account key authentication and storage account fields](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-new-linked-service.png)

1. Test the connection and then create the new linked service.

2. On the **Set properties** pane, in the **File path** section, add the path to the appropriate folder/file within your Azure Data Lake.

    ![The Set properties pane with the linked service selected, a File path set to the training container, and First row as header checked](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/set-properties.png)

3.  Select **OK**.

## Configure sink

1. Next to the data source, select the plus icon, and then find and select **Sink**.

    ![The plus menu next to the Training source searched for sink, with Sink highlighted under Destination](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-sink.png)

1. On the **Sink** tab, do the following:

    1. Enter the **Output stream name**.

    1. In **Incoming stream**, make sure the data source created in the [previous step](#configure-source) is selected.

    1. In **Sink type**, select **Dataset**.

    1. Next to the **Dataset** dropdown list, select **+ New**.

        ![The Sink tab with incoming stream Training, sink type Dataset and the + New button next to Dataset highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-sink-configuration.png)

1. In the **New dataset** pane, find and select **REST**, and then select **Continue**.

    ![The New dataset pane searched for rest, with REST selected](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/new-dataset-rest.png)

1.  In the **Set properties** pane, enter the name for the dataset. Then, expand the **Linked service** dropdown list and select **+ New**.

    ![The Set properties pane with name RestResourceTraining and the Linked service dropdown open, + New highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/rest-set-properties.png)

1. Configure the service details:

    - **Name** – enter the name for your linked service.

    - **Base URL** – enter the URL of the ingestion endpoint in CluedIn. You can find this URL in the data set that you created for ingesting data into CluedIn. For more information, see [Send data](https://documentation.cluedin.net/integration/endpoint#send-data).

        ![The CluedIn Ingestion point instructions dialog with the Post endpoint URL highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/set-properties-post-url.png)

    - **Authentication type** – select **Anonymous**.

    - **Auth headers** – add a new header with the following details:

        - **Name** – enter **Authorization**.

        - **Value** – enter **Bearer**, add a space, and then paste the token from CluedIn. You can find the token in CluedIn by going to **Administration** > **API Tokens**.  For more information, see [Send data](https://documentation.cluedin.net/integration/endpoint#send-data).

            ![The API Tokens page in CluedIn with the copy button for the Training token highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/set-properties-api-token.png)

        As a result, the new linked service should be configured similar to the following.

        ![The New linked service form for REST with the CluedIn endpoint Base URL, Anonymous authentication and an Authorization auth header](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/new-linked-service-rest.png)

1. Test connection, and then select **Create**.

1. After the sink is configured, go to the **Settings** tab, and then do the following:

    - Ensure the **Insert method** is set to **POST**. 

    - Change the **Delete method**, **Upsert method**, and **Update method** to **None**.

    - Set the **Http Compression type** to **GZip**.

        If you do not set the **HTTP Compression type** to **GZip**, you might encounter an error when starting the pipeline.

    - Set the **Batch size** to **10,000** to ensure smoother transfer.

        ![The sink Settings tab with Insert method POST, other methods None, Http Compression type GZip and Batch size 10000 highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/sink-settings.png)

## Debug pipeline in ADF

Once the source and sink are configured, you can debug the pipeline to ensure it works correctly.

**To debug the pipeline**

1. On the toolbar, select **Debug**.

    ![The pipeline toolbar with the Debug button highlighted above the Data flow activity](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-debug.png)

1. In the **Output** tab at the bottom of the window, monitor the pipeline run status.

    ![The Output tab with pipeline status Succeeded and the Data flow1 activity row showing Succeeded highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/data-flow-output.png)

## Validate result in CluedIn

Once the ADF pipeline is triggered successfully, you should see the data flowing into CluedIn. You can view the incoming records on the **Preview** tab of the data set.

![The Preview tab of the training-data data set in CluedIn, showing the records received from Azure Data Factory](https://documentation.cluedin.net/assets/images/microsoft-integration/azure-data-factory/after-debug.png)

Up: [Azure Data Factory](https://documentation.cluedin.net/solutions/azure-data-factory.md)
