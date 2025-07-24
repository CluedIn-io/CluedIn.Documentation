---
layout: cluedin
nav_order: 030
parent: Manual data entry
grand_parent: Ingestion
permalink: {{ site.baseurl }}/integration/manual-data-entry/manage-a-manual-data-entry-project
title: Manage a manual data entry project
last_modified: 2025-04-01
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article you will learn how to manage a manual data entry project: edit the project configuration and form fields and manage access to the project and data from the project.

## Edit manual data entry project configuration

Once you have created a manual data entry project, you can change its configuration if needed. You can edit the following configuration details of a manual data entry project: project name, vocabulary, record approval option, and description. You cannot change the business domain.

**To edit manual data entry project configuration**

1. On the navigation pane, go to **Ingestion** > **Manual Data Entry**.

1. Find and open the project that you want to edit.

1. In the upper-right corner, select **Edit**.

1. Make the needed changes.

1. Select **Save**.

    The manual data entry project configuration is updated.

## Edit form fields

Once you have created the form fields, you can modify them if needed. You can edit all the details of a form field. Additionally, if you no longer want to use the form field to create manual records, you can archive such form field.

Note that the changes you make in the form fields do not affect the records that have been already generated and processed.

**To edit a form field**

1. In the manual data entry project, go to the **Form Fields** tab.

1. Select the form field that you want to edit.

1. Make the needed changes.

1. Select **Save**.

    The form field configuration is updated.

**To archive a form field**

1. In the manual data entry project, go to the **Form Fields** tab.

1. Select the form field that you want to archive.

1. Select **Archive**, and then select **Confirm**.

    The status of the form field becomes **Archived**. This form field is no longer available when adding new manual records.

## Manage sessions

If you used an option to add multiple records simultaneously, then your manual data entry project contains sessions that store such records. These sessions are available on the **Sessions** tab. The sessions can have one of the following statuses:

- **Not generated** – this status means that either the session does not contain any records, or it contains some records but they have not yet been generated and processed. You can open such session and add some records. When you select the session, it opens in a new tab.

- **Generated** – this status means that the records from the session have been generated and processed. You can open such session and add more records if needed. When you generate the records, previously generated records will remain unchanged, while newly added records will be generated and processed.

If you no longer need the session, you can delete it. This action is irreversible, and you will not be able to recover the deleted session. The records generated from such session will remain intact.

**To delete a session**

1. In the manual data entry project, go to the **Sessions** tab.

1. Find the session that you want to delete.

1. On the right side of the session row, open the three-dot menu, and then select **Delete**.

    ![manual-data-entry-delete-session.png](../../assets/images/integration/manual-data-entry/manual-data-entry-delete-session.png)

1. Confirm that you want to delete the session.

    The session is no longer listed on the **Sessions** tab. 

## Manage access to manual data entry project

The user who created the manual data entry project is the owner of the project. This user can make direct changes to the project, approve or reject changes submitted by non-owner users, process the records that require approval, as well as add other users or roles to the list of owners. You can find the list of users and/or roles who can manage the manual data entry project on the **Owners** tab of the manual data entry project. For more information about ownership, see [Feature access](/administration/user-access/feature-access).

## Manage access to data from manual data entry project

The user who created the manual data entry project has access to all records generated within the project. This user can grant permission to other users and/or roles to access the records generated within the project. On the **Permissions** tab of the manual data entry project, you can find the list of users and/or roles who have access to all records generated within the project. For more information about permissions, see [Data access](/administration/user-access/data-access).

If the user is not listed on the **Permissions** tab of the project, they will not be able to view the generated records on the **Data** tab.