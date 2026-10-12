---
layout: cluedin
title: Bulk actions on the search results page
parent: Golden records
grand_parent: Key terms and features
permalink: /golden-records/bulk-actions-on-search-results
nav_order: 6
has_children: false
---

In this article, you will learn how to select multiple golden records on the search results page and perform a bulk action on them: delete, merge, reprocess, split, or add a tag.

## Select golden records

**To select golden records on the search results page**

1. On the search results page, find the golden records that you want to act on. You can search for golden records by entering a keyword or applying [filters](/key-terms-and-features/filters).

1. Select the checkboxes next to the golden records that you want to act on.

    As soon as you select at least one golden record, a toolbar with the available bulk actions appears above the search results.

    ![bulk-actions-toolbar.png]({{ "/assets/images/golden-records/bulk-actions-toolbar.png" | relative_url }})

### Select all golden records across all pages

If your search or filter criteria matches more golden records than fit on the current page, you can extend your selection to every matching golden record, not just the ones on the page you're viewing.

**To select all golden records across all pages**

1. Select all the golden records on the current page.

1. In the banner that appears above the search results, select **Select all `<number>` items across all pages**.

    ![select-all-across-pages-banner.png]({{ "/assets/images/golden-records/select-all-across-pages-banner.png" | relative_url }})

    CluedIn selects every golden record that matches your current search and filters, including the ones on other pages. The banner updates to confirm how many records are selected.

    ![select-all-across-pages-selected.png]({{ "/assets/images/golden-records/select-all-across-pages-selected.png" | relative_url }})

    The selection is kept as you move between pages. To remove the selection, select **Clear all selection**.

    **Note:** If you change your search term or filters while all records are selected, the selection is cleared, since it no longer matches your current search.

## Delete golden records

To delete the selected golden records, see [Delete several golden records](/golden-records/delete-golden-records#delete-several-golden-records).

## Merge golden records

To merge the selected golden records, select **Merge** in the toolbar. For more information about reviewing and completing a merge, see [Deduplication](/management/deduplication).

## Reprocess golden records

Reprocessing a golden record re-runs the existing processing pipeline against it, for example after you've changed rules or other configuration that affects how records are processed.

**To reprocess several golden records**

1. [Select](#select-golden-records) the golden records that you want to reprocess.

1. In the toolbar, select **Reprocess**.

1. In the confirmation dialog, select **Reprocess**.

    ![reprocess-confirm-modal.png]({{ "/assets/images/golden-records/reprocess-confirm-modal.png" | relative_url }})

    Each selected golden record is reprocessed individually. If reprocessing fails for some of the selected records, a notification tells you how many succeeded and how many failed.

## Split golden records

Splitting undoes a previous merge (a manual merge, a deduplication project merge, or a merge based on a shared identifier), separating a golden record back into the individual records it was made up of. This is the same split capability available from a single golden record's [Entity Topology](/key-terms-and-features/golden-records/golden-record-relations) page, applied to every selected record in turn.

**To split several golden records**

1. [Select](#select-golden-records) the golden records that you want to split.

1. In the toolbar, select **Split**.

    CluedIn reviews the first selected golden record and shows its split details.

1. Do one of the following:

    - If the golden record has data parts that can be split, review the details and select **Confirm split**.

    - If the golden record has no merged data parts to split, CluedIn shows a message explaining that it can't be split.

        ![split-records-modal.png]({{ "/assets/images/golden-records/split-records-modal.png" | relative_url }})

    - To move on without splitting the current record, select **Skip**.

1. Repeat the previous step for each remaining selected golden record. The dialog shows your progress (for example, _Record 2 of 5_) and closes automatically once every selected record has been reviewed.

## Add a tag to golden records

**To add a tag to several golden records**

1. [Select](#select-golden-records) the golden records that you want to tag.

1. In the toolbar, select **Add tag**.

1. In the **Tag** field, select an existing tag or enter a name to create a new one. Optionally, select a folder to organize the tag in.

    ![add-tag-modal.png]({{ "/assets/images/golden-records/add-tag-modal.png" | relative_url }})

1. Select **Add**.

    The tag is applied to every selected golden record. You can find more information about tags in [Tag monitoring](/governance/tag-monitoring).
