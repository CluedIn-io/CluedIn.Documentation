---
layout: cluedin
nav_order: 5
parent: Deduplication
grand_parent: Management
permalink: /management/deduplication/manage-groups-of-duplicates
title: Manage groups of duplicates
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to process and merge groups of duplicates, as well as how to undo a merge if it did not go as expected.

When you generate matches and CluedIn detects duplicates, they are organized into groups. These groups contain golden records identified as potential duplicates based on your matching rules. The following diagram illustrates basic group workflow. For more information about group statuses, see [Deduplication reference](/management/deduplication/deduplication-reference).

![manage-group-flow.gif]({{ "/assets/images/management/deduplication/manage-group-flow.gif" | relative_url }})

When you open a group of duplicates, you can find the following details:

- Golden records that were identified as possible duplicates.

- Conflicting values – variations in the same property or vocabulary key across all golden records within the group.

- Matching values – consistent values for the same property or vocabulary key across all golden records within the group.

## Process a group of duplicates

To ensure the merged golden records meet your requirements, you need to process each group of duplicates. Processing a group of duplicates involves three key steps:

1. Fixing duplicates – select the appropriate values from conflicting values that will be used in the merged golden record. You can fix duplicates in one of the following ways:

    - **Manually** – by selecting the appropriate values on your own.

    - **Automatically** – by turning on the **Auto-select** toggle. CluedIn will select the appropriate values based on your [survivorship rules](/management/rules).

1. Defining if a group is suitable for merging – approve or reject the group.

**To process a group of duplicates**

1. On the **Matches** tab of the deduplication project, select the group name.

1. On the **Fix Conflicts** tab, review conflicting values and choose the appropriate values to be used in the merged golden record. If you are not certain about the correctness of the selected values, you can **Reset Conflicts** and start again.

    {:.important}
    Turning on the **Auto-select** toggle prevents the display of selected values on the **Fix Conflicts** tab. Instead, you can review those values on the next tab (**Preview Merge**).

1. Go to the **Preview Merge** tab and review the property or vocabulary keys values that the merged golden record will hold.

1. Depending on the results of your review, choose if a group is suitable for merging:

    - If you want to merge the group, select **Approve**, and then confirm your choice. This is a preliminary step before merging.

        If you change your mind, you can **Revoke** the approval, which brings the group back to the **New** status.

    - If you don't want to merge the group, select **Reject**, and then confirm your choice. Rejected groups cannot be merged. However, if you change your mind, you can **Approve** the rejected group later.

    ![fix-duplicates.gif]({{ "/assets/images/management/deduplication/fix-duplicates.gif" | relative_url }})

    Once all groups within the project have been processed, proceed to merge the groups.

## Merge groups

Only groups with the **Approved** status can be merged. For additional details on group statuses, see [Deduplication reference](/management/deduplication/deduplication-reference).

**To merge groups**

1. Select the checkboxes next to the groups that you want to merge, and then select **Merge**. Alternatively, you can use the **Merge All** option, and CluedIn will automatically select groups suitable for merging.

1. Review the groups that will be merged, and then select **Next**.

1. Choose the strategy for dealing with stale data if it is identified during merging.

1. Select **Confirm**.

    ![merge-results.gif]({{ "/assets/images/management/deduplication/merge-results.gif" | relative_url }})

    The groups are merged, each generating merged golden records. Next, check the merged golden records to ensure they align with your specific requirements. If you are not satisfied, you have the option to revert changes by unmerging records.

## Check merged record

All merged golden records produced within the deduplication project are listed on the **Merges** tab. Selecting a golden record takes you to the **Topology** tab, where you can view the records that make up the golden record, linked together in a visual representation. The link between such records is the deduplication project. Having such link allows you to easily unmerge records in needed.

![check-merged-record.gif]({{ "/assets/images/management/deduplication/check-merged-record.gif" | relative_url }})

## Unmerge records

If merged golden record is not as you expected, you can revert the changes by unmerging records.

{:.important}
The unmerging option enables dynamic testing of your deduplication project configuration, allowing you to iteratively refine it until you achieve the desired results.

You can unmerge records in one of the following ways:

- On the **Topology** tab of the golden record – select the deduplication project that links the records together and then undo deduplication merge.

- On the **Matches** tab of the deduplication project – select the checkboxes next to the groups that you want to unmerge, and then select **Unmerge**.

- On the **Merges** tab of the deduplication project – select **Unmerge All**.

    ![unmerge-records.gif]({{ "/assets/images/management/deduplication/unmerge-records.gif" | relative_url }})

    After you unmerge the records, the group status is changed to **Unmerged**, and you can no longer process the group. If you want to continue working with the same group, you can [discard matches](/management/deduplication/manage-a-deduplication-project#discard-matches) and start again.