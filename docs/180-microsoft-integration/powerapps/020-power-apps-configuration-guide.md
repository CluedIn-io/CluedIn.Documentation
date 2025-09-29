---
layout: cluedin
nav_order: 20
parent: Power Apps Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/powerapps/configuration-guide
title: Power Apps configuration guide
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2025-09-29
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this guide, you will learn how to configure Power Apps integration in CluedIn.

Make sure that you have completed all of the actions described in [Power Apps pre-configuration guide](/microsoft-integration/powerapps/pre-configuration-guide).

## Basic Power Apps configuration

Basic Power Apps configuration is required to establish connection between your CluedIn instance and your Power Apps environment.

**To configure Power Apps in CluedIn**

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Power Apps** section.

1. In **Base URL**, enter the root address used to access resources within your Power Apps environment. You can find this value in your [Power Apps](https://make.powerapps.com/) environment: in the upper-right corner of the Power Apps page, select the settings icon, and then select **Developer Resources**. Copy the value in **Web API endpoint** and paste it to the **URL** field in CluedIn. You do not need to copy the version of the API (`/api/data/v9.2`).

    ![dev-resources-base-url.png]({{ "/assets/images/microsoft-integration/power-apps/dev-resources-base-url.png" | relative_url }})

1. In **Tenant Id**, enter a unique identifier for your Microsoft Entra ID tenant in which your application is registered. This is the application that you created during the pre-configuration stage in [Register a new application](/microsoft-integration/powerapps/pre-configuration-guide#register-a-new-application). You can find this value in **Directory (tenant) ID**.

1. In **Client Id**, enter a unique identifier assigned to an application when you registered it in Microsoft Entra ID. This is the application that you created during the pre-configuration stage in [Register a new application](/microsoft-integration/powerapps/pre-configuration-guide#register-a-new-application). You can find this value in **Application (client) ID**.

1. In **Client Secret**, enter a string value that your application uses to prove its identity when requesting a token. This is the client secret that you created during the pre-configuration stage in [Create a client secret](/microsoft-integration/powerapps/pre-configuration-guide#create-a-client-secret)

1. In **Parallel Execution Count**, sets the maximum number of threads that can run simultaneously for each executing job (e.g., the "Sync Entity Types Job"). This value controls the concurrency for individual tasks

1. In **Main Owner Email**, enter a valid email address (ideally an administrator's) to be used as the primary contact for system-generated items like Entity Types, Vocabularies, and Streams.

    ![cluedin-power-apps.png]({{ "/assets/images/microsoft-integration/power-apps/cluedin-power-apps.png" | relative_url }})

1. In the upper-right corner, select **Save**.

    Proceed to the next section to configure Power Apps integration features that you want to use.

## Next steps

Explore different [features](/microsoft-integration/powerapps/features) that are available as part of Power Apps integration in CluedIn.