---
title: Delete golden records
url: https://documentation.cluedin.net/master/golden-records/delete-golden-records
content_type: how-to
section: Master > Golden records
---

# Delete golden records

> how-to: Steps to accomplish one task.

In this article, you will learn how to delete golden records. Please note that deleting golden records is permanent and irreversible, so carefully consider which golden records you want to delete.

You can delete a golden record in two places:

- [On the golden record page](#delete-one-golden-record) – use this option if you want to delete one golden record.

- [On the search results page](#delete-several-golden-records) – use this option if you want to delete several golden records at once.

**Important!** Deleting a golden record is different from [deleting data parts](https://documentation.cluedin.net/master/golden-records/delete-data-parts-from-golden-records.md) or [removing records from a data source](https://documentation.cluedin.net/ingest/processing/remove-records.md). When you remove records from a data source, all data parts originating from that source are removed from every golden record in which they are used. Deleting data parts from a golden record allows you to delete specific data parts originating from almost any source in a golden record. In contrast, deleting a golden record means that the entire record is permanently removed.

## Delete one golden record

If you no longer need a specific golden record, you can delete it on the golden record page.

**To delete a golden record**

1. Open the golden record that you want to delete.

1. In the upper-right corner, select **Delete**.

1. Review the details of the golden record that will be deleted, and then select **Next**.

1. Confirm that you want to delete the golden record by entering _DELETE_. Then, select **Confirm**.

    ![Animation: on a golden record page, selecting Delete, reviewing the record details, selecting Next, entering DELETE, and selecting Confirm](https://documentation.cluedin.net/assets/images/golden-records/golden-record-delete.gif)

    The entire golden record is permanently deleted and cannot be restored.

## Delete several golden records

If you no longer need a set of golden records, you can select those golden records on the search results page and delete them. The search results page also lets you [merge, reprocess, split, or tag](https://documentation.cluedin.net/master/golden-records/bulk-actions-on-search-results.md) several golden records at once, using the same selection.

**To delete several golden records**

1. On the search results page, find golden records that you want to delete. You can search for golden records by entering a keyword or applying [filters](https://documentation.cluedin.net/master/filters.md).

1. Select the checkboxes next to the golden records that you want to delete.

    As soon as you select at least one golden record, a toolbar with the available bulk actions appears above the search results.

    ![Bulk actions toolbar above the search results with 2 items selected, showing the delete icon, Merge, Reprocess, Split, and Add tag](https://documentation.cluedin.net/assets/images/golden-records/bulk-actions-toolbar.png)

    If you want to select every golden record matching your current search across all pages, not just the ones on the current page, see [Select all golden records across all pages](https://documentation.cluedin.net/master/golden-records/bulk-actions-on-search-results.md#select-all-golden-records-across-all-pages).

1. In the toolbar, select the delete icon.

1. Review the details of the golden records that will be deleted, and then select **Next**.

1. Confirm that you want to delete golden records by entering _DELETE_. Then, select **Confirm**.

    ![Animation: on the search results page, selecting golden records, choosing delete, reviewing them, selecting Next, entering DELETE, and confirming](https://documentation.cluedin.net/assets/images/golden-records/delete-golden-records-search.gif)

    The selected golden records are permanently deleted and cannot be restored.

Up: [Golden records](https://documentation.cluedin.net/master/golden-records.md)
