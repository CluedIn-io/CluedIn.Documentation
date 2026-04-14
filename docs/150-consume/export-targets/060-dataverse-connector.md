---
layout: cluedin
nav_order: 6
parent: Export targets
grand_parent: Consume
permalink: /consume/export-targets/dataverse-connector
title: Dataverse connector (legacy)
last_modified: 2026-04-13
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

> **Note:**
> This is the legacy Dataverse connector (V1). It is only available for CluedIn installations that have been upgraded and were previously using the Dataverse connector. This connector has been superseded by the new [Dataverse connector](/consume/export-targets/dataverse-connector-v2) (V2), which is not backwards compatible. There is no automated migration path from V1 to V2, as customers may have built apps on top of the V1 tables. For new installations, use the [Dataverse connector](/consume/export-targets/dataverse-connector-v2) (V2).
>
> The legacy connector is visually indicated by a greyscale icon with a "legacy" pill tag.

This article outlines how to configure the Dataverse connector to publish data from CluedIn to Microsoft Dataverse.

## Configure Dataverse connector

Before you begin, make sure you have completed the [prerequisites](#prerequisites), including [creating a security role](#create-a-security-role) and [creating an application user](#create-an-application-user).

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **Dataverse Connector**. Then, select **Next**.

    ![choose_target_dataverse_connector.png]({{ "/assets/images/consume/export-targets/choose_target_dataverse_connector_legacy.png" | relative_url }})

1. On the **Configure** tab, enter the connection details:

    ![dataverse-connector-configure.png]({{ "/assets/images/consume/export-targets/dataverse-connector-configure.png" | relative_url }})

    1. **Name** – user-friendly name of the export target that will be displayed on the **Export Target** page in CluedIn.

    1. **URL** – you can find this value in [Power Apps](https://make.powerapps.com/), in the environment that contains your Dataverse instance. In the upper-right corner of the Power Apps page, select the settings icon, and then select **Developer Resources**. Copy the value in **Web API endpoint** and paste it to the **URL** field in CluedIn. You do not need to copy the version of the API (`/api/data/v9.2`).

        ![web-api-endpoint.png]({{ "/assets/images/consume/export-targets/web-api-endpoint.png" | relative_url }})

    1. **TenantID** – unique identifier for your Microsoft Entra tenant. You can find this value in the **Overview** section of app registration.

        ![dataverse-tenant-id.png]({{ "/assets/images/consume/export-targets/dataverse-tenant-id.png" | relative_url }})

    1. **ClientID** – unique identifier assigned to the Dataverse app when it was registered in the Microsoft identity platform. You can find this value in the **Overview** section of app registration.

        ![dataverse-client-id.png]({{ "/assets/images/consume/export-targets/dataverse-client-id.png" | relative_url }})

    1. **ClientSecret** – confidential string used by your Dataverse app to authenticate itself to the Microsoft identity platform. You can find this value in the **Certificates & secrets** section of app registration.

        ![dataverse-client-secret.png]({{ "/assets/images/consume/export-targets/dataverse-client-secret.png" | relative_url }})

1. Test the connection to make sure it works, and then select **Add**.

## Prerequisites

- Create a service principal (app registration) by following the instructions in [this article](/consume/export-targets/create-service-principal). This step is needed to get **Client ID**, **Tenant ID**, and **Client Secret** for connector configuration.

- Make sure you use a service principal to authenticate and access Dataverse.

- Make sure you have a Power Apps account. For more information on how to sign up for Power Apps, see [Microsoft documentation](https://learn.microsoft.com/en-us/power-apps/maker/signup-for-powerapps).

- Create a security role in Power Platform Admin Center by following the instructions in the [Create a security role](#create-a-security-role) section.

- Create an application user and tag it with 2 security roles—the role you created in the previous step and the System Administrator role—by following the instructions in the [Create an application user](#create-an-application-user) section.

## Create a security role

This section outlines how to create a security role in Power Apps in order to use it for the Dataverse connector.

1. Sign in to your [Power Apps account](https://make.powerapps.com/) and make sure you are in the intended environment.

    ![power-apps-home-page.png]({{ "/assets/images/consume/export-targets/power-apps-home-page.png" | relative_url }})

1. Select **Power Platform** > **Power Platform Admin Center**.

    ![power-platform-admin-center.png]({{ "/assets/images/consume/export-targets/power-platform-admin-center.png" | relative_url }})

1. Select **Environments**, and then select your intended environment.

   ![intended-environment.png]({{ "/assets/images/consume/export-targets/intended-environment.png" | relative_url }})

1. At the top of the page, select **Settings**.

    ![environment-settings.png]({{ "/assets/images/consume/export-targets/environment-settings.png" | relative_url }})

1. Expand the **Users + permissions** dropdown, and then select **Security roles**.

    ![user-permissions-security-roles.png]({{ "/assets/images/consume/export-targets/user-permissions-security-roles.png" | relative_url }})

1. At the top of the page, select **New role**. Enter the **Role Name** and select the **Business unit** of your organization. If needed, change the **Member's privilege inheritance** according to your preference. Finally, select **Create**.

    ![create-new-role.png]({{ "/assets/images/consume/export-targets/create-new-role.png" | relative_url }})

1. In the list of all security roles, find and select the role that you've just created.

    ![select-security-role.png]({{ "/assets/images/consume/export-targets/select-security-role.png" | relative_url }})

1. Edit the security role's privileges according to the [reference table](#reference-table). To open the edit mode, select the three-dot button next to the table that you want to edit.

   ![edit-table.png]({{ "/assets/images/consume/export-targets/edit-table.png" | relative_url }})

1. Once you've updated the security role's privileges according to the [reference table](#reference-table), select **Save**.

   ![save-security-role-update.png]({{ "/assets/images/consume/export-targets/save-security-role-update.png" | relative_url }})

### Reference table

| Table | Create | Read | Write | Delete |
|--|--|--|--|--|
| _Customization_ |  |  |  |  |
| Solution | Organization | Organization | Organization | Organization |
| Publisher | Organization | Organization | Organization | Organization |
| Entity | Organization | Organization | Organization | Organization |
| Entity Key | Organization | Organization |  | Organization |
| Attribute | Organization | Organization | Organization | Organization |
| System Form | Organization | Organization | Organization | Organization |
| View | Organization | Organization | Organization | Organization |
| Custom Control Default Config | Organization |  | Organization | Organization |
| Process | Organization | Organization | Organization | Organization |
| _Custom Tables_ |  |  |  |  |
| Connection Reference | Organization | Organization | Organization | Organization |
| Connector | Organization | Organization | Organization | Organization |
| Dataflow | Organization | Organization | Organization | Organization |

## Create an application user

This section outlines how to create an application user in Power Apps in order to use it for the Dataverse connector.

1. Sign in to your [Power Apps account](https://make.powerapps.com/) and make sure you are in the intended environment.

    ![power-apps-home-page.png]({{ "/assets/images/consume/export-targets/power-apps-home-page.png" | relative_url }})

1. Select **Power Platform** > **Power Platform Admin Center**.

    ![power-platform-admin-center.png]({{ "/assets/images/consume/export-targets/power-platform-admin-center.png" | relative_url }})

1. Select **Environments**, and then select your intended environment.

   ![intended-environment.png]({{ "/assets/images/consume/export-targets/intended-environment.png" | relative_url }})

1. At the top of the page, select **Settings**.

    ![environment-settings.png]({{ "/assets/images/consume/export-targets/environment-settings.png" | relative_url }})

1. Expand the **Users + permissions** dropdown, and then select **Application users**.

    ![user-permissions-application-users.png]({{ "/assets/images/consume/export-targets/user-permissions-application-users.png" | relative_url }})

1. At the top of the page, select **New app user**.

1. In the **Create a new app user** pane, do the following:

    1. Select **Add an app**, and then select the app registration (service principal) created earlier. This must be the app registration that you use to get Client ID, Tenant ID, and Client Secret for Dataverse connector configuration.

    1. Enter the **Business unit**.

    1. In the **Security roles** field, select the pencil icon, and then enter the security role created earlier. Also, you need to enter the System Administrator role to the new app user. The **Security roles** field must contain two roles.

    1. Select **Create**.

        ![create-a-new-app-user.png]({{ "/assets/images/consume/export-targets/create-a-new-app-user.png" | relative_url }})

    As a result, the new application user is created.

    ![new-app-user-successfully-created.png]({{ "/assets/images/consume/export-targets/new-app-user-successfully-created.png" | relative_url }})
