---
layout: cluedin
title: Add records in a manual data entry project
parent: Manual data entry
grand_parent: Ingest
nav_order: 20
permalink: /ingest/manual-data-entry/add-records-in-a-manual-data-entry-project
content_type: how-to
redirect_from: ["/integration/manual-data-entry/add-records-in-a-manual-data-entry-project"]
source_path: docs/040-integration/manual-data-entry/020-add-records-in-a-manual-data-entry-project.md
last_modified: 2026-11-26
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to add the records manually directly in CluedIn.

Once you have created a manual data entry project and added all the form fields you need, you can start adding the records manually. There are two options for adding the records manually:

- Adding single records – use the **Form** view of a session to fill out one record at a time, with every field of the record on screen. Right after you fill out all the required fields, you can publish the records to CluedIn.

- Adding multiple records – use the **Tabular** view of a session to enter many records at once in a spreadsheet-like table, and then publish them to CluedIn simultaneously.

Both views work on the same session, and you can switch between them at any time.

## Add single record

The process of adding a single record consists of filling out all the required fields and then publishing the record. You can add records one at a time. There are two ways to add a record:

- [In the manual data entry project](#add-single-record-in-the-manual-data-entry-project)
- [From the action center](#add-a-record-from-the-action-center)

### Add a record in the manual data entry project

1. On the navigation pane, go to **Ingestion** > **Manual Data Entry**.

1. Find and open the project where you want to add a record.

1. In the upper-right corner of the project page, select **Add Record**.

    A session opens in the **Form** view. The **Draft records** list on the left shows the records of the session, and the form on the right shows the fields of the selected record. If a form field is an [identifier seed](/ingest/manual-data-entry/configure-a-manual-data-entry-project#create-form-fields), the record already has its next value.

1. Fill out the fields for a record.

    ![Session in Form view with a draft record, the Name, Customer ID and Postal code fields filled in, the auto-save status and the required fields progress above the form, and Save & add another at the bottom]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-form-view.png" | relative_url }})

    Every change is saved to the session automatically. Above the form, you can see when the record was last saved and how many of its required fields are filled. A required field that is empty or a value that is too long is highlighted in red.

1. To add another record, select **Save & add another** at the bottom of the page, or press **Ctrl+Enter** (**⌘+Enter** on a Mac). To move between the records of the session, use **Previous** and **Next**, or select a record in the **Draft records** list.

1. When all required fields are filled, select **Publish** in the upper-right corner of the page.

    **Publish** stays unavailable while any record of the session has an empty required field. After the records are processed, you can find them on the **Data** tab of the manual data entry project.

You can switch between the **Form** and **Tabular** views of a session at any time with the switch in the upper-right corner. Changes you haven't saved yet in the Tabular view are saved before the Form view opens, so you don't lose any work.

### Add a record from the action center

1. On the navigation pane, select **Create**.

1. Select **Enter data manually**.

    The **Manual data entry** pane opens to the right side of the page.

1. In the **Name** dropdown list, find and select the manual data entry project where you want to add a record.

    After selecting a project, the relevant form fields will appear.

1. Fill out the fields for a record.

    ![Manual Data Entry pane with a project selected in Name and the First Name, Last Name, Email and Job Title fields filled in]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-add-in-action-center.png" | relative_url }})

1. Select **Add record**.

    After the record is processed, you can find it on the **Data** tab of the manual data entry project you selected in step 3. To add more records, repeat steps 2–4.

## Add multiple records

The **Tabular** view of a session works like a spreadsheet: one row represents one record, and the columns represent the form fields. Use it to enter many records at once. You can switch between the **Form** and **Tabular** views of a session at any time.

**Prerequisites**

Go to **Administration** > **Feature Flags**, and then enable the **Manual data entry tabular view** feature.

![Manual data entry tabular view feature flag card, marked Beta, with the toggle set to Enabled]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-tabular-view-feature-flag.png" | relative_url }})

**To add multiple records**

1. On the manual data entry project page, select **Add Record**, and then select **Tabular** in the upper-right corner of the session.

1. Enter the data in the cells. To add more rows, select **Add row**, or press **Enter** in the last row.

    ![Session in Tabular view with the toolbar (Add row, Undo, Redo, Save, Reset, Fill down, Freeze, Filter, AI autofill, Install Excel add-in), lettered columns, three rows of customer data, and the active cell and validation summary on the right]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-tabular-view.png" | relative_url }})

    The right side of the toolbar shows the active cell (for example, **D1 · State/Region**), the number of rows, and how many required fields are still missing. Select the summary to show only the rows that need attention.

    To delete a record, select the delete icon in the **Actions** column.

1. Select **Save** (or press **Ctrl+S**) to save your changes to the session. If you want to take a break, you can close the session and return to it later.

1. When all required fields are filled, send the records for processing:

    1. Select **Publish**.

    1. If you want to remove the session once the records have been processed, select the **Cleanup session** checkbox. If you do not select this checkbox, the session will remain on the **Sessions** tab.

    1. Select **Confirm**.

    Once processed, the records appear on the **Data** tab of the manual data entry project.

### Work faster in the Tabular view

| Action | How |
|--|--|
| Move to the next or previous cell | **Tab** / **Shift+Tab** |
| Move to the cell below or above | **Enter** or **↓** / **Shift+Enter** or **↑** (in text cells) |
| Add a row | **Add row**, or **Enter** in the last row |
| Copy the cell above into the selected cell | **Ctrl+D** (**⌘+D** on a Mac) |
| Copy the selected cell into the empty cells below it | **Fill down**. Cells that already have a value are not changed. |
| Undo, redo, save | **Ctrl+Z**, **Ctrl+Shift+Z**, **Ctrl+S** (or the toolbar buttons) |
| Keep the header row or the first column in view while scrolling | **Freeze** > **Freeze header row** / **Freeze first column** |
| Show only the rows with a missing required field or a value that is too long | **Filter** > **Rows with issues** |

Fill down and **Ctrl+D** are not available in an identifier seed column, so its values stay unique.

### Fill empty cells with AI

AI autofill suggests values for the empty cells of the columns you choose, based on the other values in each row—for example, a city from a postal code. Nothing changes until you accept the suggestions.

**Prerequisites**

Your organization needs an AI endpoint. If none is set up, the **AI autofill** panel tells you so. Ask an administrator to add one.

**To fill empty cells with AI**

1. In the Tabular view, select **AI autofill**.

1. Under **Columns to fill**, select the columns that you want AI to fill. Each column shows how many of its cells are empty. Lookup, toggle and identifier seed columns are not listed.

1. (Optional) Enter **Instructions** for the AI, such as "Use the official state name, not its abbreviation".

1. Select **Generate suggestions**.

    ![The AI autofill panel with Postal code, Country and Street address selected under Columns to fill, and four suggestions in the preview, one of them cleared]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-ai-autofill.png" | relative_url }})

1. Review the suggestions. Clear the checkbox of any suggestion that you don't want, and then select **Accept**. To discard all suggestions, select **Reject all**.

    The accepted values are added to the table as one change, which you can undo with **Undo**. Select **Save** to keep them.

### Enter records in Excel

You can also enter and edit records of a manual data entry project from Microsoft Excel with the CluedIn Excel Add-in. Select **Install Excel add-in** in the Tabular view to open the [installation instructions](/solutions/excel-add-in).

The link opens the CluedIn Excel Add-in article by default. An administrator can point it elsewhere, such as your organization's own add-in deployment, with the `REACT_APP_UI_EXCELADDIN_INSTALL_URL` setting of the CluedIn UI.
