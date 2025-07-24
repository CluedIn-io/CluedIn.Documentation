---
layout: cluedin
nav_order: 10
parent: Export targets
grand_parent: Consume
permalink: {{ site.baseurl }}/consume/export-targets/create-service-principal
title: Create a service principal
last_modified: 2025-01-07
---

This article outlines how to register an application and create a service principal.

When you register a new application in Microsoft Entra ID, a service principal is automatically created for the app registration. Following the steps in this article will provide you with the **Client ID**, **Tenant ID**, and **Client Secret** required to configure integration with CluedIn.

**Prerequisites:** Make sure you have access to Microsoft Azure and Microsoft Entra ID.

**To register and application and create a service principal**

1. Go to the [Azure portal](https://portal.azure.com/).

1. Select **Microsoft Entra ID**.

    ![microsoft-entra-id.png](../../assets/images/consume/service-principal/microsoft-entra-id.png)

1. On the left-hand navigation pane, under **Manage**, select **App registrations**.

    ![app-registrations.png](../../assets/images/consume/service-principal/app-registrations.png)

1. Select **New registration**.

    ![new-registration.png](../../assets/images/consume/service-principal/new-registration.png)

1. Enter the **Name** of service principal, select **Supported account types**, and then select **Register**.

    ![app-registration-fields.png](../../assets/images/consume/service-principal/app-registration-fields.png)

    After successful registration, you can find **Client ID** (a) and **Tenant ID** (b) on the overview page of your service principal (app registration).

    ![client-and-tenant-id.png](../../assets/images/consume/service-principal/client-and-tenant-id.png)

1. To create **Client Secret**, select the **Add a certificate or secret** link on the overview page of your service principal (app registration).

     ![add-certificate-or-secret.png](../../assets/images/consume/service-principal/add-certificate-or-secret.png)

1. Select **New client secret**.

    ![new-client-secret-1.png](../../assets/images/consume/service-principal/new-client-secret-1.png)

1. In the **Description** field, enter the name of the client secret. In the **Expires** field, select an expiration for the secret. Finally, select **Add**.

    ![new-client-secret-2.png](../../assets/images/consume/service-principal/new-client-secret-2.png)

    Now, you can find the client secret value under **Certificates & secrets**.

     ![secret-value.png](../../assets/images/consume/service-principal/secret-value.png)
