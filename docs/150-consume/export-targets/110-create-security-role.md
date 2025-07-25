---
layout: cluedin
nav_order: 11
parent: Export targets
grand_parent: Consume
permalink: /consume/export-targets/create-security-role
title: Create security role for Dataverse connector
last_modified: 2025-01-14
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to create a security role in Power Apps in order to use it for Dataverse connector.

**Prerequisites:** Make sure you have an existing Power Apps account.

## Create security role

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

## Reference table

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
