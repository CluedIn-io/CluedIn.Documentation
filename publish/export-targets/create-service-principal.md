---
title: Create a service principal
url: https://documentation.cluedin.net/publish/export-targets/create-service-principal
content_type: how-to
section: Publish & consume > Export targets
---

# Create a service principal

> how-to: Steps to accomplish one task.

This article outlines how to register an application and create a service principal.

When you register a new application in Microsoft Entra ID, a service principal is automatically created for the app registration. Following the steps in this article will provide you with the **Client ID**, **Tenant ID**, and **Client Secret** required to configure integration with CluedIn.

**Prerequisites:** Make sure you have access to Microsoft Azure and Microsoft Entra ID.

**To register and application and create a service principal**

1. Go to the [Azure portal](https://portal.azure.com/).

1. Select **Microsoft Entra ID**.

    ![Azure portal Azure services list with Microsoft Entra ID highlighted](https://documentation.cluedin.net/assets/images/consume/service-principal/microsoft-entra-id.png)

1. On the left-hand navigation pane, under **Manage**, select **App registrations**.

    ![Microsoft Entra ID Overview page with App registrations highlighted under Manage in the left pane](https://documentation.cluedin.net/assets/images/consume/service-principal/app-registrations.png)

1. Select **New registration**.

    ![The App registrations page with the New registration button highlighted](https://documentation.cluedin.net/assets/images/consume/service-principal/new-registration.png)

1. Enter the **Name** of service principal, select **Supported account types**, and then select **Register**.

    ![The Register an application page with a Name entered, the single-tenant supported account type selected, and the Register button](https://documentation.cluedin.net/assets/images/consume/service-principal/app-registration-fields.png)

    After successful registration, you can find **Client ID** (a) and **Tenant ID** (b) on the overview page of your service principal (app registration).

    ![App registration Overview page with callouts on the Application (client) ID (a) and the Directory (tenant) ID (b)](https://documentation.cluedin.net/assets/images/consume/service-principal/client-and-tenant-id.png)

1. To create **Client Secret**, select the **Add a certificate or secret** link on the overview page of your service principal (app registration).

     ![App registration Overview page with the Add a certificate or secret link highlighted next to Client credentials](https://documentation.cluedin.net/assets/images/consume/service-principal/add-certificate-or-secret.png)

1. Select **New client secret**.

    ![The Certificates & secrets page on the Client secrets tab, with New client secret highlighted](https://documentation.cluedin.net/assets/images/consume/service-principal/new-client-secret-1.png)

1. In the **Description** field, enter the name of the client secret. In the **Expires** field, select an expiration for the secret. Finally, select **Add**.

    ![The Add a client secret pane with a Description entered, Expires set to 365 days, and the Add button](https://documentation.cluedin.net/assets/images/consume/service-principal/new-client-secret-2.png)

    Now, you can find the client secret value under **Certificates & secrets**.

     ![The Certificates & secrets page listing the new client secret, with its Value highlighted](https://documentation.cluedin.net/assets/images/consume/service-principal/secret-value.png)

Up: [Export targets](https://documentation.cluedin.net/publish/export-targets.md)
