---
layout: cluedin
title: Purview pre-configuration guide
parent: Microsoft Purview
grand_parent: Solutions & integrations
nav_order: 20
permalink: /solutions/purview/pre-configuration-guide
content_type: how-to
redirect_from: ["/microsoft-integration/purview/pre-configuration-guide"]
source_path: docs/180-microsoft-integration/purview/010-purview-pre-configuration-guide.md
last_modified: 2025-04-30
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this guide, you will learn how to prepare for configuring Purview integration in CluedIn. Generally, you need to prepare the following:

- Purview account

- App registration

- Data sources, such as a storage account, Fabric, SQL Server, Snowflake. 

- Key vault

- Purview environment: collections, scanned data sources, role assignments

## Prerequisites

Make sure you have a Microsoft Purview account. For information on how to create it, see [Create a Microsoft Purview account](https://learn.microsoft.com/en-us/purview/legacy/create-microsoft-purview-portal).

## Create resources in Azure

In this section, you will find instructions for creating and preparing Azure resources needed for Purview integration configuration. 

### Register an application and create a service principal

When you register a new application in Microsoft Entra ID, a service principal is automatically created for the app registration. The service principal is the app's identity in the Microsoft Entra tenant. For more information, see Register a [Microsoft Entra app and create a service principal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal).

**To register an application**

1. Sign in to the [Azure portal](https://portal.azure.com/).

1. On the **Home** page of the portal under **Azure services**, select **Microsoft Entra ID**.

1. In the left navigation pane, select **App registrations**. Then, on the **App registrations** page, select **+ New registration**.

    ![The App registrations page in Microsoft Entra ID, with + New registration highlighted in the toolbar]({{ "/assets/images/microsoft-integration/purview/register-app-new-registration.png" | relative_url }})

1. Provide your application's registration information: **Name** and **Supported account types**.

    ![The Register an application form with the Name CluedInPurviewSPN and Single tenant selected under Supported account types]({{ "/assets/images/microsoft-integration/purview/register-app-register-an-application.png" | relative_url }})

1. Select **Register**.

    You will need the **Application (client) ID** and **Directory (tenant) ID** to configure Purview integration in CluedIn as described in [Purview configuration guide](/solutions/purview/configuration-guide).

    ![The app registration Overview page, with the Application (client) ID and Directory (tenant) ID highlighted in Essentials]({{ "/assets/images/microsoft-integration/purview/register-app-overview.png" | relative_url }})

Once the application is registered, create a client secret.

**To create a client secret**

1. Go to **Certificates & secrets** > **Client secrets** > **New client secret**.

    ![The Certificates & secrets page on the Client secrets tab, with + New client secret highlighted]({{ "/assets/images/microsoft-integration/purview/register-app-new-client-secret.png" | relative_url }})

1. Add a description for your client secret. Select an expiration for the secret or specify a custom lifetime. Finally, select **Add**.

    ![The Add a client secret pane with a Description entered and Expires set to the recommended 180 days]({{ "/assets/images/microsoft-integration/purview/register-app-add-client-secret.png" | relative_url }})

1. Record the **Value** of the client secret. You will need it to configure Purview integration in CluedIn as described in [Purview configuration guide](/solutions/purview/configuration-guide). This secret value is never displayed again after you leave this page.

    ![The Client secrets tab listing the new secret, with its masked Value column highlighted and a copy button]({{ "/assets/images/microsoft-integration/purview/register-app-client-secret-value.png" | relative_url }})

### Create a storage account

1. Sign in to the [Azure portal](https://portal.azure.com/).

1. From the left portal menu, select **Storage accounts**.

1. On the **Storage accounts** page, select **Create**.

1. On the **Basics** tab, provide the essential information for your storage account:

    1. In the **Project details** section:

        1. Select the **Subscription** for the new storage account.

        1. Create a new **Resource group** for this storage account or select an existing one.

    1. In the **Instance details** section:

        1. Enter a unique **Storage account name**.

        1. Select the appropriate **Region** for your storage account.

        1. Select the **Primary service** that provides a unique namespace for your Azure Storage data (**Azure Blob Storage or Azure Data Lake Storage Gen 2**).

        1. In **Performance**, leave the default **Standard** option selected. This type of account is recommended by Microsoft for most scenarios.

        1. In **Redundancy**, leave the default **Geo-redundant storage (GRS)** option selected. This way, your data is replicated to a data center in a different region. For read access to data in the secondary region, select **Make read access to data available in the event of regional unavailability**.

    1. Select ****Review + create****.

        ![The Basics tab of Create a storage account, with subscription, resource group, name, region, Standard performance and GRS redundancy]({{ "/assets/images/microsoft-integration/purview/create-storage-account-basics.png" | relative_url }})

1. When you navigate to the **Review + create** tab, Azure runs validation on your storage account settings. After the validation is passed, select **Create**.

### Create a key vault and register Purview

To store encryption keys, secrets, and certificates for communication between Purview, Azure Data Factory, and data stores, create and configure a key vault.

**To create and configure a key vault**

1. Sign in to the [Azure portal](https://portal.azure.com/) and create a key vault following the [instructions from Microsoft](https://learn.microsoft.com/en-us/azure/key-vault/general/quick-create-portal).

    After you create a key vault, you need to grant the Microsoft Purview managed identity access to your Azure Key Vault.

1. In the navigation pane, go to **Settings** > **Access configuration**.

1. In the **Permission model** section, select **Vault access policy**.

    ![The key vault Access configuration page with Vault access policy selected as the Permission model]({{ "/assets/images/microsoft-integration/purview/key-vault-access-configuration.png" | relative_url }})

1. Select **Apply**.

1. In the navigation pane, go to **Access policies**.

1. On the **Access policies** page, select **Create**.

    ![The key vault Access policies page, with + Create highlighted in the toolbar]({{ "/assets/images/microsoft-integration/purview/key-vault-create-access-policy.png" | relative_url }})

1. On the **Permissions** tab, in the **Secret permissions** column, select the checkboxes for **Get** and **List**, and then select **Next**.

    ![The Permissions tab of Create an access policy, with Get and List checked under Secret permissions]({{ "/assets/images/microsoft-integration/purview/key-vault-create-access-policy-permissions.png" | relative_url }})

1. On the **Principal** tab, find and select the Purview account, and then select **Next**.

    ![The Principal tab of Create an access policy, with the CluedIn-Purview account found and shown as the selected item]({{ "/assets/images/microsoft-integration/purview/key-vault-create-access-policy-principal.png" | relative_url }})

1. On the **Application (optional)** tab, select **Next**.

1. On the **Review + create** tab, select **Create**.

### Create a key vault secret

1. In the Azure portal, open the key vault that you created before.

1. In the navigation pane, go to **Objects** > **Secrets**.

1. On the **Secrets** page, select **Generate/Import**.

    ![The key vault Secrets page, with + Generate/Import highlighted in the toolbar]({{ "/assets/images/microsoft-integration/purview/key-vault-create-secrets-generate-import.png" | relative_url }})

1. Enter the **Name** of the secret.

1. To get the **Secret value**, do the following:

    1. Go to the storage account that you created before in [Create a storage account](#create-a-storage-account).

    1. On the navigation pane, go to **Data storage** > **Access keys**.

    1. Copy the value of **key1**.

        ![The storage account Access keys page, with the key1 section and its Copy to clipboard button highlighted]({{ "/assets/images/microsoft-integration/purview/key-vault-create-secrets-copy-key.png" | relative_url }})

    1. Paste the copied value to the **Secret value** field.

        ![The Create a secret form with Upload options set to Manual, the Name dataLakeStorageSecret, and a masked Secret value]({{ "/assets/images/microsoft-integration/purview/key-vault-create-a-secret.png" | relative_url }})

    1. Select **Create**.

## Prepare Microsoft Purview environment

In this section, you will find instructions for preparing your Purview environment for integration with CluedIn. 

### Create a new collection

You need to create 2 collections: one to store the assess from Azure Data Lake Storage and the other one to store the assess from CluedIn.

**To create a new collection**

1. In the [Microsoft Purview portal](https://purview.microsoft.com), navigate to **Data Map** > **Domains**, and then select your default domain.

1. On the default domain page, select **+ New collection**.

1. Provide the details for the collection that will be used to store the assets from CluedIn:

    1. Enter the **Display name** and **Description** of the collection.

        ![The Purview New collection pane with the Display name cluedIn-assets and a description entered]({{ "/assets/images/microsoft-integration/purview/purview-create-new-collection.png" | relative_url }})

    1. Select **Create**.

        The new collection is added to the default domain. Pay attention to the collection ID, which can be found in the URL. You will need this collection ID to configure Purview integration in CluedIn as described in in [Purview configuration guide](/solutions/purview/configuration-guide).

        ![The cluedIn-assets collection in Purview Data Map Domains, with the collection ID highlighted at the end of the browser URL]({{ "/assets/images/microsoft-integration/purview/purview-collection-id.png" | relative_url }})

1. To create a collection that will be used to store the assets from Azure Data Lake Storage, repeat steps 1–3.

### Register a new data source

To enable Purview to discover and catalog metadata from your data sources, register a new data source.

**To register a new data source**

1. In the [Microsoft Purview portal](https://purview.microsoft.com), navigate to **Data Map** > **Data sources**, and then select **Register**.

1. Find and select a data source type. This example uses Azure Data Lake Storage Gen2. Select **Continue**.

    ![The Register data source dialog filtered on Data Lake, with Azure Data Lake Storage Gen2 selected]({{ "/assets/images/microsoft-integration/purview/purview-register-data-source.png" | relative_url }})

1. Enter the **Data source name**.

1. Select the **Storage account name**. This is the storage account that you created before in [Create a storage account](#create-a-storage-account). After you select the storage account name, the **Azure subscription** will be filled out automatically.

1. Make sure the default **Domain** is selected.

1. Select the **Collection** for storing the assets from Azure Data Lake Storage that you created before in [Create a new collection](#create-a-new-collection).

    ![The Register data source form for Azure Data Lake Storage Gen2 with name, storage account, domain and the dataLakeStorage collection set]({{ "/assets/images/microsoft-integration/purview/purview-register-data-source-adls.png" | relative_url }})

1. Select **Register**.

    The new data source is added.

    ![Purview Data sources in Map view: the CluedIn-Purview domain links to the dataLakeStorage collection, which holds the new Azure Data Lake Storage source]({{ "/assets/images/microsoft-integration/purview/purview-data-sources-map-view.png" | relative_url }})

### Scan a data source

To capture technical metadata from your data source in Purview, scan a data source.

**To create a scan**

1. In the [Microsoft Purview portal](https://purview.microsoft.com), navigate to **Data Map** > **Data sources**.

1. Find the data source that you created in [Register a new data source](#register-a-new-data-source), and then select **View details**.

1. On the data source page, select **New scan**.

    ![The Purview data source details page for AzureDataLakeStorage-hhg, with New scan highlighted]({{ "/assets/images/microsoft-integration/purview/purview-new-scan.png" | relative_url }})

1. Enter the **Name** for the scan.

1. Expand the **Credential** dropdown list, and then select **+ New**.

    ![The scan setup pane with the Credential dropdown expanded and + New highlighted]({{ "/assets/images/microsoft-integration/purview/purview-new-scan-new-credential.png" | relative_url }})

1. Enter the **Name** and **Description** of the credential.

1. In **Authentication method**, leave the default **Account key** option selected.

1. In the **Account key** section, expand the **Key Vault connection** dropdown, and then select **+ New**.

    ![The New credential pane with Account key authentication and the Key Vault connection dropdown open on + New]({{ "/assets/images/microsoft-integration/purview/purview-new-scan-new-credential-new-key-vault.png" | relative_url }})

1. Enter the **Name** and **Description** of the new key vault.

1. In **Key Vault name**, select the key vault that you created before in [Create a key vault and register Purview](#create-a-key-vault-and-register-purview).

    ![The New Key Vault pane with a name, description, Azure subscription and the Key Vault name APAC-CluedIn-Key-Vault selected]({{ "/assets/images/microsoft-integration/purview/purview-new-scan-new-credential-new-key-vault-create.png" | relative_url }})

1. Select **Create**.

1. Expand the **Key Vault connection** dropdown, and then select the newly created key vault connection.

1. In **Secret name**, enter the name of the secret that you created before in [Create a key vault secret](#create-a-key-vault-secret).

    ![The New credential pane with the Key Vault connection cluedInKV and the Secret name dataLakeStorageSecret filled in]({{ "/assets/images/microsoft-integration/purview/purview-new-scan-new-credential-create.png" | relative_url }})

1. Select **Create**.

1. Select **Test connection**.

    ![The scan setup pane with the new credential selected and a Connection successful message next to Test connection]({{ "/assets/images/microsoft-integration/purview/purview-new-scan-continue.png" | relative_url }})

1. Once the connection is successful, select **Continue**.

1. Scope your scan to a specific subset of data, and then select **Continue**.

    ![The Scope your scan pane with folders in the apac-container of the storage account selected]({{ "/assets/images/microsoft-integration/purview/purview-new-scan-scope.png" | relative_url }})

1. Keep the default scan rule set, and then select **Continue**.

    ![The Select a scan rule set pane with the AdlsGen2 system default rule set]({{ "/assets/images/microsoft-integration/purview/purview-new-scan-scan-rule-set.png" | relative_url }})

1. Choose your scan trigger. You can set up a schedule or run the scan once. In this example, we run the scan once. Select **Continue**.

    ![The Set a scan trigger pane with Once selected instead of Recurring]({{ "/assets/images/microsoft-integration/purview/purview-new-scan-scan-trigger.png" | relative_url }})

1. Review your scan, and then select **Scan and run**.

    Once the scan is completed, it establishes a connection to the data source and captures technical metadata like names, file size, columns, and so on. As a result of the scan, the collection for storing assets from Azure Data Lake Storage contains a certain number of assets. On the following screenshot, our collection contains 18 assets.

    ![The dataLakeStorage collection overview after the scan, with the Assets card showing 18 highlighted]({{ "/assets/images/microsoft-integration/purview/purview-new-scan-collection-result.png" | relative_url }})

### Assign roles to Purview service principal

To enable Purview to communicate with CluedIn, assign the Data readers and Data source admins roles to the Purview service principal.

**To assign roles to Purview service principal**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Data Map** > **Domains**, and then select your default domain.
    
1. On the default domain page, go to the **Role assignments** tab.

    ![The default CluedIn-Purview domain in Purview Data Map, with the Role assignments tab highlighted]({{ "/assets/images/microsoft-integration/purview/role-assignments.png" | relative_url }})

1. Expand the **Edit role assignments** dropdown list, and then select **Data readers**.

1. Find and select the Purview service principal that you created in [Register an application and create a service principal](#register-an-application-and-create-a-service-principal).

    ![The Add or remove data readers pane with the CluedInPurviewSPN service principal found and highlighted]({{ "/assets/images/microsoft-integration/purview/role-assignments-data-reader.png" | relative_url }})

1. Select **OK**.

1. Expand the **Edit role assignments** dropdown list, and then select **Data source admins**.

1. Find and select the Purview service principal that you created in [Register an application and create a service principal](#register-an-application-and-create-a-service-principal).

    ![The Add or remove data source admins pane with the CluedInPurviewSPN service principal found and highlighted]({{ "/assets/images/microsoft-integration/purview/role-assignments-data-source-admins.png" | relative_url }})

1. Select **OK**.

## Next steps

Now that you have completed all pre-configuration steps, start the configuration of Purview integration in CluedIn using our [Purview configuration guide](/solutions/purview/configuration-guide).