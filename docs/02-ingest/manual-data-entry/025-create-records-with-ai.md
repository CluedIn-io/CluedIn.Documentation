---
layout: cluedin
title: Create records with AI
parent: Manual data entry
grand_parent: Ingest
nav_order: 25
permalink: /ingest/manual-data-entry/create-records-with-ai
content_type: how-to
last_modified: 2026-11-21
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to describe the records you need in plain language and let AI draft them. You review the records and correct them before anything is added, either to a new manual data entry project or to an existing one.

This is useful when you need sample or reference records quickly, for example a list of suppliers for a pilot, all the countries for a reference list, or test data for a new business domain.

**Prerequisites**

- An AI provider must be configured for your organization. If none is configured, you will see an error message when you try to generate records.

- You need the **Manual Data Entry Project Management** or **Manual Data Entry Input** claim at Consultant level or above. To create a new project, you need the claim that creates manual data entry projects.

## Generate records

1. On the navigation pane, go to **Ingestion** > **Manual Data Entry**.

1. Select **Create**, and then select **Create with AI**.

    ![The Create menu on the Manual Data Entry page with Create Manual Data Entry Project and Create with AI]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-create-with-ai-menu.png" | relative_url }})

1. In **What records do you want?**, describe the records. For example, _European furniture suppliers with their country, contact email and website_.

1. (Optional) In **Columns**, enter the column names you want, separated by commas, such as _Name, Country, Email, Website_. If you leave this empty, AI chooses the columns.

1. (Optional) In **Number of records**, enter how many records to generate, up to 300. Leave it empty to get every record the description calls for. For example, _all the countries in the world_ returns every country. If the description doesn't name a complete set, you get 10 records.

1. Select **Generate**.

    The generated records appear in a table for you to review.

    ![Generated supplier records in the review table, with an editable value in each cell and a delete icon on each row]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-ai-review.png" | relative_url }})

1. Review the records:

    - To correct a value, select it, edit it, and then select another value or click outside the cell.

    - To leave a record out, select the delete icon on its row.

    - If the records are not what you need, change the description and select **Generate again**.

    A value that is a link to an image shows a small preview of the image.

Next, add the records to a [new project](#add-the-records-to-a-new-project) or to an [existing project](#add-the-records-to-an-existing-project).

## Add the records to a new project

A new project gets one text form field for each column, in a new vocabulary.

1. In **Add to**, select **A new project, with a form field for each column**.

1. Enter the **Project name**.

1. Select the **Business domain** for the records.

1. Review the **Vocabulary key prefix**. It is filled in from the project name, and the new vocabulary's keys start with it. The prefix must start with a letter, contain only letters and digits, and not be used by another vocabulary.

    ![The Add to section with a new project selected, the project name, the Organization business domain and the vocabulary key prefix]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-ai-new-project.png" | relative_url }})

1. Select **Add _n_ records**.

    CluedIn creates the project, its vocabulary and its form fields, and then sends the records for processing. The project's **Process** tab opens, where you can follow the processing.

Afterwards, you can [add validation rules](/ingest/manual-data-entry/configure-a-manual-data-entry-project#create-form-fields) to the form fields and [review the mapping](/ingest/manual-data-entry/configure-a-manual-data-entry-project#review-and-modify-mapping-configuration), for example to choose the field used for the records' names.

## Add the records to an existing project

1. In **Add to**, select **An existing project**.

1. Select the **Project**.

    Each column is matched to the form field with the same label or vocabulary key name.

1. Review the mapping. For each column, select the form field it goes to, or select **Don't import** to leave the column out.

    If the project's form fields have [validation rules](/ingest/manual-data-entry/configure-a-manual-data-entry-project#create-form-fields), values that fail a rule are highlighted in the review table. Point to a highlighted value to see what to fix.

    ![A review table with an invalid email highlighted and its message shown, the column mapping to the project's form fields, and a warning that one record will be quarantined]({{ "/assets/images/integration/manual-data-entry/manual-data-entry-ai-existing-project.png" | relative_url }})

1. Decide what happens to records that fail validation:

    - To add the valid records and send the failing ones to the project's quarantine, keep **Quarantine records that fail validation instead of rejecting them** selected. You can correct the quarantined records later. For more information, see [Review quarantined records](/ingest/manual-data-entry/manage-a-manual-data-entry-project#review-quarantined-records).

    - To add records only if they are all valid, clear the checkbox. If any record fails, nothing is added and the errors are shown.

1. Select **Add _n_ records**.

    The records are sent for processing, and the project's **Process** tab opens.

## Verify the result

On the project's **Process** tab, a new row shows the number of records sent and how many were processed successfully. If records were quarantined, the row shows how many. Processing runs in the background, so the counts fill in over a few seconds. Processed records then appear on the project's **Data** tab.

## What this changes

- Generating records saves nothing. Records are added only when you select **Add _n_ records**.
- Adding to a new project creates the project, a vocabulary with one key per column, and a text form field per column, and then processes the records into golden records.
- Adding to an existing project processes the records into golden records in the same way as records entered by hand. Records sent to quarantine are not processed until you reprocess them.

## If something goes wrong

| What you see | What it means and what to do |
|---|---|
| _The AI could not generate these records_ | No AI provider is configured for your organization, or the provider failed. Check the AI configuration, then try again. |
| _The AI did not return any usable records_ | The description could not be turned into records. Describe the data more specifically, or name the columns. |
| _Another vocabulary already uses this prefix_ | Enter a different **Vocabulary key prefix**. |
| An error listing records and fields when you add | Quarantine was turned off and some records fail the project's validation rules. Correct the highlighted values, or select the quarantine option. |
