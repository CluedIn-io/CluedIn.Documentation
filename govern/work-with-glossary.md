---
title: Work with the glossary
url: https://documentation.cluedin.net/govern/work-with-glossary
content_type: how-to
section: Govern & improve
---

# Work with the glossary

> how-to: Steps to accomplish one task.

Glossary can help you in documenting groups of golden records that meet specific criteria, simplifying the process of cleaning and streaming these groups of records.

In this article, you will learn how to work with the glossary in CluedIn. Glossary consists of terms that are grouped into categories. Each term contains a list of golden records that correspond to your conditions.

Working with the glossary in CluedIn includes creating categories and creating terms within those categories. You can have multiple terms under one category.

**Before you start:** Make sure you have completed all steps in the [Ingest data guide](https://documentation.cluedin.net/ingest/tutorial-ingest-data.md) and [Stream data guide](https://documentation.cluedin.net/publish/streams/tutorial-stream-data.md).

## Create category

Category refers to a logical grouping of terms. For example, you can have a category named **Customer**, which would contain customer records organized by regions. Each region is a separate term within the category. In other words, a category acts as a folder for terms.

**To create a category**

1. On the navigation pane, go to **Management** > **Glossary**.

1. Depending on whether or not you have created categories before, do one of the following:

    - If you haven't created any categories before, then in the middle of the page, select **Create Category**.

    - If you already created some categories, then, in the upper-left corner of the page, select **Create** > **Create Category**. 

1. Enter the category name. Then, in the lower-right corner, select **Create**.

    ![Create Category pane with Customer entered as the Category Name](https://documentation.cluedin.net/assets/images/getting-started/glossary/create-category-1.png)

    You created the category. Now, you can create a term in the category.

## Create term

Term refers to the list of golden records that meet specific conditions. For example, within the **Customer** category, you can have a term named **North America** encompassing customer records where the **BusinessRegion** vocabulary key is set to **North America**. 

**To create a term**

1. Select **Create Term**.

1. On the **Create Term** pane, do the following:

    1. Enter the term name.

    1. In the **Category** section, leave the **Choose an existing Category** checkbox selected.

    1. Select the category that you created before.

    1. In the **Filters** section, define which golden records should be included in the term.

        ![Create Term pane with term name Dropbox, existing category Customer, and a filter where trainingcontact.email contains dropbox.com](https://documentation.cluedin.net/assets/images/getting-started/glossary/create-term-1.png)

    1. In the lower-right corner, select **Create**.

        You created the term.

1. (Optional) Specify additional details about the term:

    1. Select **Edit**.

    1. In the **Certification Level** dropdown list, select the quality level of the records.

    1. Enter the **Short Description** and **Long Description** of the term.

        ![Term details in edit mode with Certification Level Gold, a Short Description, and a Long Description](https://documentation.cluedin.net/assets/images/getting-started/glossary/create-term-3.png)

1. In the upper-right corner of the term details page, select **Save**.

1. Go to the **Matches** tab to view the records that meet the condition that you set up.

    By default, all records are displayed in the following columns: **Name**, **Business Domain**, and **Description**. To add more columns to the table, see step 3 of [Find data](https://documentation.cluedin.net/govern/cleaning/tutorial-clean-data.md#find-data).

1. Activate the term by turning on the toggle next to the term status.

    ![Dropbox term page on the Matches tab with the status toggle set to Active and highlighted](https://documentation.cluedin.net/assets/images/getting-started/glossary/create-term-4.png)

    You created the term and defined the records that are included in this term.

Now, you can clean the glossary term and stream it to a Microsoft SQL Server database. As an example, [update the configuration of the stream](#update-stream-configuration) that you created in the [Stream data](https://documentation.cluedin.net/publish/streams/tutorial-stream-data.md) guide.

## Manage glossary

You can do the following actions with the terms in the glossary:

- Endorse the term when you are confident that the records are of good quality, signaling to other users that the term is reliable for their use. To do that, in the upper-right corner of the term page, select **Endorse**.

    ![Dropbox term page with the Endorse button in the upper-right corner and Endorsed by showing the user who endorsed it](https://documentation.cluedin.net/assets/images/getting-started/glossary/manage-glossary-1.png)

- Rate the term, enabling other users to view that it is reliable for their use.

    ![Dropbox term overview showing a Certified Gold badge and a 100% rating with five stars](https://documentation.cluedin.net/assets/images/getting-started/glossary/manage-glossary-2.png)

## Update stream configuration

Streaming the glossary terms to the database is more convenient than streaming specific records based on filters. You only need to specify the name of the glossary term, rather than setting filters for properties or vocabulary values.

**To update the stream**

1. On the navigation pane, go to **Consume** > **Streams**.

1. Open the needed stream.

1. On the **Configuration** pane, in the **Filters** section, delete the existing filter.

1. Select **Add First Filter**, and then specify the glossary term that you created:

    1. In the **Select Property Type** dropdown list, select **Glossary**.

    1. In the **All Glossary** dropdown list, select the glossary term that you created.

    1. In the **Choose Operation** dropdown list, select **Is True**.

        ![Stream Filters section with Glossary selected as the property type, the Dropbox - Customer term, and the Is True operation](https://documentation.cluedin.net/assets/images/getting-started/glossary/update-stream-configuration-1.png)

1. In the upper-right corner select **Save**. Then, confirm that you want to save your changes.

    The stream is updated with the new filter. As a result, the database table now contains the records from the glossary term.

    If you update the glossary term, the records will be automatically updated in the database.

## Results & next steps

After completing all steps outlined in this guide, you learned how to create a glossary term to document a group of golden records and how to send those golden records from the glossary term to a Microsoft SQL Server database. If you make any changes to the glossary term in CluedIn, the associated records will be automatically updated in the database.

Next, learn how to add edges to build relations between golden records in the [Add relations between records](https://documentation.cluedin.net/model/relationships/tutorial-add-relations.md).

Up: [Govern & improve](https://documentation.cluedin.net/govern.md)
