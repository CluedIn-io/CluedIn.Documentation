---
layout: cluedin
nav_order: 6
parent: Export targets
grand_parent: Consume
permalink: consume/export-targets/dataverse-connector
title: Dataverse connector
last_modified: 2025-01-14
---

This article outlines how to configure the Dataverse connector to publish data from CluedIn to Microsoft Dataverse.

**Prerequisites:** 

- Create a service principal (app registration) following the instruction in [this article](/consume/export-targets/create-service-principal). This step is needed to get **Client ID**, **Tenant ID**, and **Client Secret** for connector configuration.

- Make sure you use a service principal to authenticate and access Dataverse.

- Make sure you have a Power Apps account. For more information on how to sign up for Power Apps, see [Microsoft documentation](https://learn.microsoft.com/en-us/power-apps/maker/signup-for-powerapps).

- Create a **security role** in Power Platform Admin Center following the instruction in [this article](/consume/export-targets/create-security-role).

- Create an **application user** and tag it with 2 security roles—the role you created in the previous requirement and the System Administrator role—following the instruction in [this article](/consume/export-targets/create-application-user).

**To configure Dataverse connector**

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **Dataverse Connector**. Then, select **Next**.

    ![choose_target_dataverse_connector.png](../../assets/images/consume/export-targets/choose_target_dataverse_connector.png)

1. On the **Configure** tab, enter the connection details:

    1. **Name** – user-friendly name of the export target that will be displayed on the **Export Target** page in CluedIn.

    1. **URL** – you can find this value in [Power Apps](https://make.powerapps.com/), in the environment that contains your Dataverse instance. In the upper-right corner of the Power Apps page, select the settings icon, and then select **Developer Resources**. Copy the value in **Web API endpoint** and paste it to the **URL** field in CluedIn. You do not need to copy the version of the API (`/api/data/v9.2`).

        ![web-api-endpoint.png](../../assets/images/consume/export-targets/web-api-endpoint.png)

    1. **TenantID** – unique identifier for your Microsoft Entra tenant. You can find this value in the **Overview** section of app registration.

        ![dataverse-tenant-id.png](../../assets/images/consume/export-targets/dataverse-tenant-id.png)

    1. **ClientID** – unique identifier assigned to the Dataverse app when it was registered in the Microsoft identity platform. You can find this value in the **Overview** section of app registration.

        ![dataverse-client-id.png](../../assets/images/consume/export-targets/dataverse-client-id.png)

    1. **ClientSecret** – confidential string used by your Dataverse app to authenticate itself to the Microsoft identity platform. You can find this value in the **Certificates & secrets** section of app registration.

        ![dataverse-client-secret.png](../../assets/images/consume/export-targets/dataverse-client-secret.png)

1. Test the connection to make sure it works, and then select **Add**.

    ![dataverse-connector-configure.png](../../assets/images/consume/export-targets/dataverse-connector-configure.png)