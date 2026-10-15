---
layout: cluedin
title: Bulk actions on the search results page
parent: Golden records
grand_parent: Master
nav_order: 70
permalink: /master/golden-records/bulk-actions-on-search-results
content_type: how-to
redirect_from: ["/golden-records/bulk-actions-on-search-results"]
last_modified: 2026-10-13
---

In this article, you will learn how to select multiple golden records on the search results page and perform a bulk action on them: delete, merge, reprocess, split, or add a tag.

## Select golden records

**To select golden records on the search results page**

1. On the search results page, find the golden records that you want to act on. You can search for golden records by entering a keyword or applying [filters](/master/filters).

1. Select the checkboxes next to the golden records that you want to act on.

    As soon as you select at least one golden record, a toolbar with the available bulk actions appears above the search results.

    ![Bulk actions toolbar above the search results with 2 items selected, showing delete, Merge, Reprocess, Split, and Add tag]({{ "/assets/images/golden-records/bulk-actions-toolbar.png" | relative_url }})

### Select all golden records across all pages

If your search or filter criteria matches more golden records than fit on the current page, you can extend your selection to every matching golden record, not just the ones on the page you're viewing.

**To select all golden records across all pages**

1. Select all the golden records on the current page.

1. In the banner that appears above the search results, select **Select all `<number>` items across all pages**.

    ![Selection banner reading All 1 items are selected on this page, with the link Select all 2 items across all pages]({{ "/assets/images/golden-records/select-all-across-pages-banner.png" | relative_url }})

    CluedIn selects every golden record that matches your current search and filters, including the ones on other pages. The banner updates to confirm how many records are selected.

    ![Selection banner reading Selected all 2 items across all pages, with the Clear all selection link]({{ "/assets/images/golden-records/select-all-across-pages-selected.png" | relative_url }})

    The selection is kept as you move between pages. To remove the selection, select **Clear all selection**.

    **Note:** If you change your search term or filters while all records are selected, the selection is cleared, since it no longer matches your current search.

## Delete golden records

To delete the selected golden records, see [Delete several golden records](/master/golden-records/delete-golden-records#delete-several-golden-records).

## Merge golden records

To merge the selected golden records, select **Merge** in the toolbar. For more information about reviewing and completing a merge, see [Deduplication](/master/deduplication).

## Reprocess golden records

Reprocessing a golden record re-runs the existing processing pipeline against it, for example after you've changed rules or other configuration that affects how records are processed.

**To reprocess several golden records**

1. [Select](#select-golden-records) the golden records that you want to reprocess.

1. In the toolbar, select **Reprocess**.

1. In the confirmation dialog, select **Reprocess**.

    ![Reprocess 2 records confirmation dialog with Cancel and Reprocess buttons]({{ "/assets/images/golden-records/reprocess-confirm-modal.png" | relative_url }})

    Each selected golden record is reprocessed individually. If reprocessing fails for some of the selected records, a notification tells you how many succeeded and how many failed.

## Split golden records

Splitting undoes a previous merge (a manual merge, a deduplication project merge, or a merge based on a shared identifier), separating a golden record back into the individual records it was made up of. This is the same split capability available from a single golden record's [Entity Topology](/master/golden-records/golden-record-relations) page, applied to every selected record in turn.

Golden records that have nothing to split (no merged data parts) are skipped automatically — you're only prompted for the ones that can actually be split.

**To split several golden records**

1. [Select](#select-golden-records) the golden records that you want to split.

1. In the toolbar, select **Split**.

    CluedIn reviews the selected golden records and, for the first one that has data parts to split, shows the split details.

1. Review the details, and then do one of the following:

    - Select **Confirm split** to split the golden record.

    - Select **Skip** to move on without splitting it.

1. Repeat the previous step for each remaining golden record that has data parts to split. The dialog shows your progress (for example, _Record 2 of 5_) and closes automatically once every selected record has been reviewed. A summary tells you how many records were split.

## Add a tag to golden records

**To add a tag to several golden records**

1. [Select](#select-golden-records) the golden records that you want to tag.

1. In the toolbar, select **Add tag**.

1. In the **Tag** field, select an existing tag or enter a name to create a new one. Optionally, select a folder to organize the tag in.

    ![Add tag dialog with a Tag field to select or create a tag, an optional folder selector, and an Add link]({{ "/assets/images/golden-records/add-tag-modal.png" | relative_url }})

1. Select **Add**.

    The tag is applied to every selected golden record. You can find more information about tags in [Tag monitoring](/govern/tags/tag-monitoring).
