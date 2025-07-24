---
layout: cluedin
nav_order: 12
parent: Export targets
grand_parent: Consume
permalink: consume/export-targets/create-application-user
title: Create application user for Dataverse connector
last_modified: 2025-01-14
---

This article outlines how to create an application user in Power Apps in order to use it for Dataverse connector.

**Prerequisites:** Make sure you have an existing Power Apps account.

**To create an application user**

1. Sign in to your [Power Apps account](https://make.powerapps.com/) and make sure you are in the intended environment.

    ![power-apps-home-page.png](../../assets/images/consume/export-targets/power-apps-home-page.png)

1. Select **Power Platform** > **Power Platform Admin Center**.

    ![power-platform-admin-center.png](../../assets/images/consume/export-targets/power-platform-admin-center.png)

1. Select **Environments**, and then select your intended environment.

   ![intended-environment.png](../../assets/images/consume/export-targets/intended-environment.png)

1. At the top of the page, select **Settings**.

    ![environment-settings.png](../../assets/images/consume/export-targets/environment-settings.png)

1. Expand the **Users + permissions** dropdown, and then select **Application users**.

    ![user-permissions-application-users.png](../../assets/images/consume/export-targets/user-permissions-application-users.png)

1. At the top of the page, select **New app user**.

1. In the **Create a new app user** pane, do the following:

    1. Select **Add an app**, and then select the [app registration (service principal)](/consume/export-targets/create-service-principal) created earlier. This must be the app registration that you use to get Client ID, Tenant ID, and Client Secret for Dataverse connector configuration.

    1. Enter the **Business unit**.

    1. In the **Security roles** field, select the pencil icon, and then enter the [security role](/consume/export-targets/create-security-role) created earlier. Also, you need to enter the System Administrator role to the new app user. The **Security roles** field must contain two roles.

    1. Select **Create**.

        ![create-a-new-app-user.png](../../assets/images/consume/export-targets/create-a-new-app-user.png)

    As a result, the new application user is created.

    ![new-app-user-successfully-created.png](../../assets/images/consume/export-targets/new-app-user-successfully-created.png)
