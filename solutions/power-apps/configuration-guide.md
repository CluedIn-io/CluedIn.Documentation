---
title: Power Apps configuration guide
url: https://documentation.cluedin.net/solutions/power-apps/configuration-guide
content_type: how-to
section: Solutions & integrations > Power Apps
---

# Power Apps configuration guide

> how-to: Steps to accomplish one task.

In this guide, you will learn how to configure Power Apps integration in CluedIn.

Make sure that you have completed all of the actions described in [Power Apps pre-configuration guide](https://documentation.cluedin.net/solutions/power-apps/pre-configuration-guide.md).

## Basic Power Apps configuration

Basic Power Apps configuration is required to establish connection between your CluedIn instance and your Power Apps environment.

**To configure Power Apps in CluedIn**

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Power Apps** section.

1. In **Base URL**, enter the root address used to access resources within your Power Apps environment. You can find this value in your [Power Apps](https://make.powerapps.com/) environment: in the upper-right corner of the Power Apps page, select the settings icon, and then select **Developer Resources**. Copy the value in **Web API endpoint** and paste it to the **URL** field in CluedIn. You do not need to copy the version of the API (`/api/data/v9.2`).

    ![The Power Apps Developer resources pane, with the Web API endpoint URL highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/dev-resources-base-url.png)

1. In **Tenant Id**, enter a unique identifier for your Microsoft Entra ID tenant in which your application is registered. This is the application that you created during the pre-configuration stage in [Register a new application](https://documentation.cluedin.net/solutions/power-apps/pre-configuration-guide.md#register-a-new-application). You can find this value in **Directory (tenant) ID**.

1. In **Client Id**, enter a unique identifier assigned to an application when you registered it in Microsoft Entra ID. This is the application that you created during the pre-configuration stage in [Register a new application](https://documentation.cluedin.net/solutions/power-apps/pre-configuration-guide.md#register-a-new-application). You can find this value in **Application (client) ID**.

1. In **Client Secret**, enter a string value that your application uses to prove its identity when requesting a token. This is the client secret that you created during the pre-configuration stage in [Create a client secret](https://documentation.cluedin.net/solutions/power-apps/pre-configuration-guide.md#create-a-client-secret)

1. In **Parallel Execution Count**, set the maximum number of threads that can run simultaneously for each executing job (for example, the "Sync Entity Types" job). This value controls the concurrency for individual tasks.

1. In **Main Owner Email**, enter a valid email address—ideally that of an administrator. This address will be used as the primary contact for system-generated items such as entity types, vocabularies, and streams.

    ![The PowerApps section of CluedIn settings, with Base Url, Tenant Id, Client Id, Client Secret, Parallel Execution Count and Main Owner Email filled in](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/cluedin-power-apps-2.png)

1. In the upper-right corner, select **Save**.

## Next steps

Explore different [features](https://documentation.cluedin.net/solutions/power-apps/features.md) that are available as part of Power Apps integration in CluedIn.

Up: [Power Apps](https://documentation.cluedin.net/solutions/power-apps.md)
