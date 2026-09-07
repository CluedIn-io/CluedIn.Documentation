---
layout: cluedin
title: Configure ADF with private link
parent: Azure Data Factory
grand_parent: Solutions & integrations
nav_order: 10
permalink: /solutions/azure-data-factory/private-link
content_type: how-to
redirect_from: ["/microsoft-integration/adf-integration/private-link"]
source_path: docs/180-microsoft-integration/azure-data-factory/001-adf-with-private-link.md
---

In this article, you will learn how to configure a private link service between Azure Data Factory (ADF) and CluedIn.

**Prerequisites**

- CluedIn endpoint is configured to be private. For detailed instruction, see [Internal load balancer](/operate/configuration/advanced-network#internal-load-balancer).

- Host name resolution is configured with private IP. For detailed instruction, see [Host name resolution](/operate/configuration/advanced-network#host-name-resolution).

If you have any questions, you can request CluedIn support by sending an email to <a href="mailto:support@cluedin.com">support@cluedin.com</a> (or reach out to your delivery manager if you have a committed deal).

**To configure private link between ADF and CluedIn**

1. Create a private link service to CluedIn private endpoint as described in [Private link service with private endpoint](/operate/configuration/advanced-network#private-link-service-with-private-endpoint). You may skip creating a private endpoint as we will use managed private endpoint from ADF.

1. In Azure Data Factory Studio, go to the **Manage** tab. In the **Security** section, select **Managed private endpoints**.

1. Select **New**.

1. Find and select the private link service.

1. Enter the following information:

    - **Name** – enter **cluedin-private-endpoint**.

    - **Account selection method** – select **From Azure subscriptions**.

    - **Azure subscriptions** – enter the subscription of private link service created in step 1.

    - **Private link service** – enter the name of private link service created in step 1.

    - **FQDN names** – enter your company CluedIn host name. The following names are provided as an example:
            
        - `app.company.com`

        - `clean.company.com`

        - `cluedin.company.com`

1. Select **Create**.

    Once the managed private endpoint is created, wait for provisioning state to be **Succeeded**.

    ![managed-private-endpoint-succeeded.png]({{ "/assets/images/microsoft-integration/azure-data-factory/managed-private-endpoint-succeeded.png" | relative_url }})

1. Go to the private link service created in step 1 and approve the managed private endpoint:

    1. Open the private link service created in step 1.

    1. Go to **Settings** > **Private endpoint connections**.

    1. Check and approve the managed private endpoint. Make sure the private endpoint name matches **[adf name].[managed private endpoint name]**.

    ![private-endpoint-connections.png]({{ "/assets/images/microsoft-integration/azure-data-factory/private-endpoint-connections.png" | relative_url }})

    Once approved, your ADF should gain connectivity towards CluedIn private endpoint. Next, create ADF pipeline using the [Copy data](/solutions/azure-data-factory/copy-data) or [Data flow](/solutions/azure-data-factory/data-flow-activity) activity to send data to CluedIn.