---
layout: cluedin
title: Manage groups of duplicates
parent: Deduplication
grand_parent: Master
nav_order: 50
permalink: /master/deduplication/manage-groups-of-duplicates
content_type: how-to
redirect_from: ["/management/deduplication/manage-groups-of-duplicates"]
source_path: docs/080-management/deduplication/050-manage-groups-of-duplicates.md
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Process and merge groups of duplicates when a deduplication project has generated matches and you want to turn each group into one golden record. You review each group, choose the values the merged golden record keeps, approve or reject the group, and then merge the approved groups. Merging changes golden records; if a merge did not go as expected, you can unmerge it.

## Prerequisites

- The **Deduplication Review** claim, which covers processing, approving, rejecting, merging and unmerging groups of duplicates. See [Claims](/administer/users-and-roles/claims#management).
- A deduplication project with the **Ready for review** status, which means that matches have been [generated](/master/deduplication/manage-a-deduplication-project#generate-matches).
- If you want to fix conflicts automatically with **Auto-select**, the [survivorship rules](/govern/rules) that should pick the values.

When you generate matches and CluedIn detects duplicates, they are organized into groups. These groups contain golden records identified as potential duplicates based on your matching rules. The following diagram illustrates basic group workflow. For more information about group statuses, see [Deduplication reference](/master/deduplication/deduplication-reference).

![Group workflow diagram: fix conflicts manually or automatically, approve or reject the group, merge approved groups, and unmerge if not satisfied]({{ "/assets/images/management/deduplication/manage-group-flow.gif" | relative_url }})

On the **Matches** tab, and when you open a group, CluedIn shows its match confidence—how strongly the group's records resemble each other—and which matching rule or rules contributed to the group. See [Match confidence and rule attribution](/master/deduplication/deduplication-reference#match-confidence-and-rule-attribution).

When you open a group of duplicates, you can find the following details:

- Golden records that were identified as possible duplicates.

- Conflicting values – variations in the same property or vocabulary key across all golden records within the group.

- Matching values – consistent values for the same property or vocabulary key across all golden records within the group.

## Process a group of duplicates

To ensure the merged golden records meet your requirements, you need to process each group of duplicates. Processing a group of duplicates involves three key steps:

1. Fixing duplicates – select the appropriate values from conflicting values that will be used in the merged golden record. You can fix duplicates in one of the following ways:

    - **Manually** – by selecting the appropriate values on your own.

    - **Automatically** – by turning on the **Auto-select** toggle. CluedIn will select the appropriate values based on your [survivorship rules](/govern/rules).

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

    ![Animation: on the Matches tab, a group is opened, conflicting values are fixed, and the group is approved or rejected]({{ "/assets/images/management/deduplication/fix-duplicates.gif" | relative_url }})

    Once all groups within the project have been processed, proceed to merge the groups.

## Review groups faster

When you are processing many groups in a row, CluedIn preloads the next several groups in the background so that moving between them does not wait on a new page load each time, and offers keyboard shortcuts for the three most common actions on the group review page:

| Key | Action |
|--|--|
| A | Approve the group. |
| R | Reject the group. |
| S | Skip the group—move to the next group in the list without approving or rejecting it. |

After you approve, reject, or skip a group, CluedIn takes you straight to the next group in the list rather than back to the **Matches** tab, so you can work through many groups in a row using only the keyboard. You are returned to the **Matches** tab once there is no next group left to show.

Approving and rejecting with a keyboard shortcut still asks you to confirm, the same as selecting the button. Skipping does not change the group's status; the group remains **New** and you can open it again later. The shortcuts are disabled while you are typing in a text field, so they do not interfere with entering values on the page.

## Approve or reject many groups at once by confidence

Instead of processing groups one by one, you can approve every group above a confidence threshold, or reject every group below one, in a single action. This is useful once you trust a project's matching rules and want to clear out the groups you are confident about, leaving only the uncertain ones for manual review.

**To approve or reject groups by confidence threshold**

1. On the **Matches** tab of the deduplication project, select **Approve all above threshold** or **Reject all below threshold**.

1. Set the confidence threshold. As you adjust it, CluedIn shows how many of the current groups would be affected.

1. Confirm your choice.

    Only groups with the **New** status are affected—a group that has already been approved or rejected is not changed. Groups whose confidence has not yet been calculated are never included, regardless of the threshold.

Approving or rejecting by threshold changes the group's status the same way as approving or rejecting it individually; it does not merge any records. [Merge the approved groups](#merge-groups) as a separate step.

## Get an AI explanation of a group

If you want a plain-language explanation of why CluedIn grouped a set of records together, select **Explain this cluster** on the group review page. CluedIn sends the group's field values, its calculated match confidence, and the matching rules that contributed to it, to the configured AI model, and returns an explanation along with its own assessment of how likely the records are to be the same thing.

{:.important}
This feature requires an AI model to be configured for your organization. See [AI agents](/govern/ai-agents).

The explanation is a second opinion to help you decide, not a decision CluedIn makes for you—you still approve, reject or skip the group yourself.

## Merge groups

Only groups with the **Approved** status can be merged. For additional details on group statuses, see [Deduplication reference](/master/deduplication/deduplication-reference).

**To merge groups**

1. Select the checkboxes next to the groups that you want to merge, and then select **Merge**. Alternatively, you can use the **Merge All** option, and CluedIn will automatically select groups suitable for merging.

1. Review the groups that will be merged, and then select **Next**.

1. Choose the strategy for dealing with stale data if it is identified during merging.

1. Select **Confirm**.

    ![Animation: approved groups on the Matches tab are merged with Merge All, reviewed, and confirmed, and their status changes]({{ "/assets/images/management/deduplication/merge-results.gif" | relative_url }})

    The groups are merged, each generating merged golden records. Next, check the merged golden records to ensure they align with your specific requirements. If you are not satisfied, you have the option to revert changes by unmerging records.

## Check merged record

All merged golden records produced within the deduplication project are listed on the **Merges** tab. Selecting a golden record takes you to the **Topology** tab, where you can view the records that make up the golden record, linked together in a visual representation. The link between such records is the deduplication project. Having such link allows you to easily unmerge records in needed.

![Animation: on the Merges tab, a merged golden record is selected and its Topology tab shows the records that make it up]({{ "/assets/images/management/deduplication/check-merged-record.gif" | relative_url }})

## Unmerge records

If merged golden record is not as you expected, you can revert the changes by unmerging records.

{:.important}
The unmerging option enables dynamic testing of your deduplication project configuration, allowing you to iteratively refine it until you achieve the desired results.

You can unmerge records in one of the following ways:

- On the **Topology** tab of the golden record – select the deduplication project that links the records together and then undo deduplication merge.

- On the **Matches** tab of the deduplication project – select the checkboxes next to the groups that you want to unmerge, and then select **Unmerge**.

- On the **Merges** tab of the deduplication project – select **Unmerge All**.

    ![Animation: merged groups on the Matches tab are unmerged and their status changes from Merge Committed to Unmerged]({{ "/assets/images/management/deduplication/unmerge-records.gif" | relative_url }})

    After you unmerge the records, the group status is changed to **Unmerged**, and you can no longer process the group. If you want to continue working with the same group, you can [discard matches](/master/deduplication/manage-a-deduplication-project#discard-matches) and start again.

## Verify the result

- **After you approve or reject a group**, its status on the **Matches** tab is **Approved** or **Rejected**. Approving and rejecting change only the group's status; no golden records are changed yet.
- **While groups are being merged**, the project status is **Committing**, which means that CluedIn is merging records from the selected groups.
- **When the merge has finished**, each merged group has the **Merge Committed** status. If every group in the project was merged, the project status becomes **Merged**; if some groups were not selected for merge, the project status stays **Ready for review**.
- The merged golden records are listed on the project's **Merges** tab. On a merged golden record's **Topology** tab, the records that make it up are linked through the deduplication project, and the golden record's [history](/master/golden-records/history) has a data part whose source is the deduplication project.
- **After you unmerge**, the group status is **Unmerged**. While records are being unmerged, the project status is **Unmerging**; when it finishes, the project status becomes **Ready for review**.
- Approvals, rejections, merges and unmerges are recorded on the project's **Audit Log** tab. See [Deduplication project audit log actions](/master/deduplication/deduplication-reference#deduplication-project-audit-log-actions).

For all statuses, see [Group statuses](/master/deduplication/deduplication-reference#group-statuses) and [Project statuses](/master/deduplication/deduplication-reference#project-statuses).

## What this changes

- **Fixing conflicts, approving, rejecting and revoking** change only the group. Golden records are not changed until you merge.
- **Merging changes golden records.** Merging does not create a new golden record. It uses one of the duplicate records as a base and aggregates data from the others into it, with the values you chose on the **Fix Conflicts** tab. The duplicates in the group become one golden record, so the number of golden records decreases.
- **A merge can lead to further merges.** A merged golden record can contain new information that meets a matching rule, so generate matches again after merging until no more duplicates are found. See [Concept of deduplication](/master/deduplication/concept-of-deduplication).
- **A merge can be undone.** Unmerging reverts the changes made to the golden record through merging, and restores the duplicate records to their state before the merge. **Unmerge All** reverts every merge in the project, including merges produced by rules that worked as intended; this is why [separate projects for strict and fuzzy matching](/master/deduplication/deduplication-in-practice) are recommended.
- [Discarding matches](/master/deduplication/manage-a-deduplication-project#discard-matches) or [archiving the project](/master/deduplication/manage-a-deduplication-project#archive-a-deduplication-project) does not affect golden records that have already been merged.

## If something goes wrong

- **A group cannot be merged.** Only groups with the **Approved** status can be merged. Rejected groups cannot be merged until you approve them.
- **You are not sure about the values you selected.** Before merging, select **Reset Conflicts** to start again, or **Revoke** the approval to bring the group back to **New**.
- **The merged golden record is not what you expected.** [Unmerge the records](#unmerge-records), then [discard matches](/master/deduplication/manage-a-deduplication-project#discard-matches), adjust the matching rules, and generate matches again.
- **You want to work with an unmerged group again.** A group with the **Unmerged** status can no longer be processed. [Discard matches](/master/deduplication/manage-a-deduplication-project#discard-matches) and generate them again.
