---
layout: cluedin
nav_order: 11
parent: Export targets
grand_parent: Consume
permalink: /consume/export-targets/create-security-role
title: Create secusity role for Dataverse connector
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

    ![power-apps-intended-environment.png](/.attachments/power-apps-intended-environment-38bf37eb-2381-4d9e-a58d-2977d4cf90fd.png)

1. Select **Power Platform** > **Power Platform Admin Center**.

    ![power-platform-admin-center.png](/.attachments/power-platform-admin-center-8cefb99e-1327-4990-b36d-cbed88accf59.png)

1. Select **Environments**, and then select your intended environment.

   ![intended-environment.png](/.attachments/intended-environment-9d1043d4-0423-4836-bb33-5f75f82cfa92.png)

1. At the top of the page, select **Settings**.

    ![environment-settings.png](/.attachments/environment-settings-cf6e6053-8ac3-46fc-97a2-95bd9c8524fb.png)

1. Expand the **Users + permissions** dropdown, and then select **Security roles**.

    ![user-permissions-security-roles.png](/.attachments/user-permissions-security-roles-81ab7500-d04f-4629-9f3d-fe2dbd6b3de2.png)

1. At the top of the page, select **New role**. Enter the **Role Name** and select the **Business unit** of your organization. If needed, change the **Member's privilege inheritance** according to your preference. Finally, select **Create**.

    ![create-new-role.png](/.attachments/create-new-role-dfb8def3-28ba-4ae9-91f6-1995dff842f3.png)

1. In the list of all security roles, find and select the role that you've just created.

    ![select-security-role.png](/.attachments/select-security-role-610cb0b9-140b-46e1-8730-0dcaa7135858.png)

1. Edit the security role's privileges according to the [reference table](#reference-table). To open the edit mode, select the three-dot button next to the table that you want to edit.

   ![edit-table.png](/.attachments/edit-table-35e4e815-7a62-4ebf-a67e-403e7f6b1f2a.png)
   
1. Once you've updated the security role's privileges according to the [reference table](#reference-table), select **Save**.

   ![save-security-role-update.png](/.attachments/save-security-role-update-38147b82-6b30-4f6c-984e-e008010a10f1.png)

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
