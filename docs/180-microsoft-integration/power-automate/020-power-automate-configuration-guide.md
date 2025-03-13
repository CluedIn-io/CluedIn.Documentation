---
layout: cluedin
nav_order: 20
parent: Power Automate Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/power-automate/configuration-guide
title: Power Automate configuration guide
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2025-03-13
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this guide, you will learn how to configure and register a custom connector in CluedIn.

Make sure that you have completed all of the actions described in [Pre-configuration guide](/microsoft-integration/power-automate/pre-configuration-guide).

{:.important}
This guide is for public CluedIn instances. If you have a zero-trust corporate environment, contact our CluedIn support at [support@cluedin.com](mailto:support@cluedin.com) to configure workflows for your use case.

**To configure workflows in CluedIn**

1. Go to **Administration** > **Feature Flags**, and then enable the **Workflow Builder** feature.

    ![workflow-builder-feature.png](../../assets/images/microsoft-integration/power-automate/workflow-builder-feature.png)

    As a result, the **Workflows** module appears on the navigation pane.

1. Go to **Administration** > **Settings**. Scroll down to the **Workflows** section and complete the following fields:

    - **Client Username** – an email of a Microsoft Entra ID user for handling workflows. This is the user that you created during the pre-configuration stage in [Create a user account](/microsoft-integration/power-automate/pre-configuration-guide#create-a-user-account). You can find the needed value in the **User principal name** field.

    - **Client Password** – a password of a Microsoft Entra ID user for handling workflows. This is the user that you created during the pre-configuration stage in [Create a user account](/microsoft-integration/power-automate/pre-configuration-guide#anchor=create-a-user-account).

    - **Client ID** – a unique identifier assigned to an application when you registered it in Microsoft Entra ID. This is the application that you created during the pre-configuration stage in [Create a service application](/microsoft-integration/power-automate/pre-configuration-guide#create-a-service-application). You can find this value in **Application (client) ID**.

        ![client-id.png](../../assets/images/microsoft-integration/power-automate/client-id.png)

    - **Azure Tenant ID** – an ID of the Azure tenant that contains the service principal that handles the Power Automate widget. This is the service principal that was created automatically when you registered a new application in [Create a service application](/microsoft-integration/power-automate/pre-configuration-guide#create-a-service-application). For guidance on how to find the ID, see [Find your Microsoft Entra tenant](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id#find-your-microsoft-entra-tenant).

    - **Power Automate Environment ID** – an ID of the Power Automate environment. This is the environment that you prepared during the pre-configuration stage in [Configure an environment](/microsoft-integration/power-automate/pre-configuration-guide#configure-an-environment). You can find the ID on the home page of the environment.

        ![env-id.png](../../assets/images/microsoft-integration/power-automate/env-id.png)

    - **CluedIn Connector** – a name of the custom connector that allows communication between CluedIn and Power Automate. By default, it is _CluedIn_, and you do not need to change it.

    - **Approvals for creating items** – enabling this control means that when a user creates an element in CluedIn (for example, a vocabulary, a vocabulary key, or a rule), an approval request is sent to other users with the same or higher claim access level to the feature. For example, if a Data Governance Administrator creates a vocabulary, the approval request is sent to other users with the same role. If you don't enable this control, the approval requests will be sent only in case of modifications of the existing elements.

    - **Approvals for activating/deactivating rules** – enabling this control means that when a user activates or deactivates a rule, an approval request is sent to all rule owners.

    - **Enterprise Flow Cache Duration** – a time period for which data is stored in the cache for enterprise flows. This duration can impact the performance and efficiency of your workflows. In the context of Power Automate, the cache duration helps manage the flow’s performance by temporarily storing data to reduce the need for repeated data retrievals.

    - **Entity Type Cache Duration** – a time period for which the records that belong to the entity types with the **Batch approval workflow** option enabled are stored in the cache.

        ![workflows-cluedin-configuration.png](../../assets/images/microsoft-integration/power-automate/workflows-cluedin-configuration.png)

1. Select **Register Custom Connector**.

    A custom connector is going to be created in Power Automate. Next, proceed to [Power Automate post-configuration guide](/microsoft-integration/power-automate/post-configuration-guide) to verify that the connector has been created successfully. 