---
layout: cluedin
title: Manage a manual data entry project
parent: Manual data entry
grand_parent: Ingest
nav_order: 30
permalink: /ingest/manual-data-entry/manage-a-manual-data-entry-project
content_type: how-to
redirect_from: ["/integration/manual-data-entry/manage-a-manual-data-entry-project"]
source_path: docs/040-integration/manual-data-entry/030-manage-a-manual-data-entry-project.md
last_modified: 2025-04-01
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article you will learn how to manage a manual data entry project: edit the project configuration and form fields, review quarantined records, and manage access to the project and data from the project.

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

    ![Session row in the manual data entry project with the three-dot menu open and the Delete option highlighted]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-delete-session.png" | relative_url }})

1. Confirm that you want to delete the session.

    The session is no longer listed on the **Sessions** tab. 

## Review quarantined records

The **Quarantine** tab of a manual data entry project lists the records that were held back from processing:

- records that failed the form fields' [validation rules](/ingest/manual-data-entry/configure-a-manual-data-entry-project#create-form-fields) when they were added with quarantine turned on, for example from [Create with AI](/ingest/manual-data-entry/create-records-with-ai);

- records that a [column rule or pre-process rule](/ingest/manual-data-entry/configure-a-manual-data-entry-project#add-rules-to-the-mapping) sent to quarantine.

The **Quarantine reason** column says why each record is held. For a validation failure, the reason names the field and what to fix.

![The Quarantine tab with one record whose quarantine reason is Email: Enter a valid supplier email address]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-quarantine.png" | relative_url }})

**To correct and reprocess a quarantined record**

1. In the manual data entry project, go to the **Quarantine** tab.

1. Select the value you want to correct, edit it, and then click outside the cell. The change is saved to the quarantined record.

1. In the **Actions** column, select the process icon. To reprocess several records, select them, and then select **Process**.

    The records are checked against the form fields' validation rules again. If any record still fails, nothing is sent and a message lists what to fix.

    ![A message saying 1 record still fails validation, so nothing was sent to processing, with the field and what to fix]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-quarantine-still-invalid.png" | relative_url }})

    When the records pass, they are sent to processing and removed from the **Quarantine** tab. The reprocessing appears on the **Process** tab, and the records then appear on the **Data** tab.

To discard a quarantined record instead, select the reject icon in the **Actions** column. **Reject all** discards every quarantined record of the project. Records waiting on the **Approval** tab are not affected.

## Manage access to manual data entry project

The user who created the manual data entry project is the owner of the project. This user can make direct changes to the project, approve or reject changes submitted by non-owner users, process the records that require approval, as well as add other users or roles to the list of owners. You can find the list of users and/or roles who can manage the manual data entry project on the **Owners** tab of the manual data entry project. For more information about ownership, see [Feature access](/administer/users-and-roles/feature-access).

## Manage access to data from manual data entry project

The user who created the manual data entry project has access to all records generated within the project. This user can grant permission to other users and/or roles to access the records generated within the project. On the **Permissions** tab of the manual data entry project, you can find the list of users and/or roles who have access to all records generated within the project. For more information about permissions, see [Data access](/administer/users-and-roles/data-access).

If the user is not listed on the **Permissions** tab of the project, they will not be able to view the generated records on the **Data** tab.