---
layout: cluedin
nav_order: 3
parent: Deduplication
grand_parent: Management
permalink: /management/deduplication/manage-a-deduplication-project
title: Manage a deduplication project
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

After creating and configuring your deduplication project, you can begin the deduplication process to eliminate duplicates and produce a unified and accurate representation of a golden record.

The primary action on the deduplication project level is the generation of results. Its purpose is to analyze a specific set of records and detect potential duplicates based on your matching rules. If such duplicates are detected, they are organized into groups. The following diagram illustrates basic project workflow. For more information about project statuses, see [Deduplication reference](/management/deduplication/deduplication-reference).

![manage-dedup-project-flow.gif](../../assets/images/management/deduplication/manage-dedup-project-flow.gif)

{:.important}
Instructions on how to process groups of duplicates, including merging and unmerging, are provided in the [Manage groups of duplicates](/management/deduplication/manage-groups-of-duplicates) article.

## Generate results

The process of generating results involves analyzing a specified set of golden records with the goal of finding duplicates among them based on your matching rules.

**To generate results**

- In the deduplication project, select **Generate Results** and then confirm your choice.

    ![generate-results.gif](../../assets/images/management/deduplication/generate-results.gif)

    If duplicates are detected, the results will be displayed on the page. These results are organized into groups that contain records matching your specified criteria. One group contains duplicate records that can be potentially merged into one golden record.

    Next, [process the groups of duplicates](/management/deduplication/manage-groups-of-duplicates)—open each group one by one to review duplicates and fix conflicting values.

## Discard results

If you want to change matching criteria, remove the limit of records, or regenerate the results of the deduplication project, you can discard the results. This action does not affect merged golden records.

**To discard results**

- In the upper-right corner of the deduplication project, select **Discard Results**, and then confirm your choice.

    ![discard-results.gif](../../assets/images/management/deduplication/discard-results.gif)

    The project status is changed to **Ready to generate**. Now, you can edit the project as needed and generate results again.

## Edit a deduplication project

You can edit a deduplication project only when its [status](/management/deduplication/deduplication-reference#deduplication-project-statuses) is **Requires configuration** or **Ready to generate**. In other statuses, you need to discard the results before editing the project.

Editing a deduplication project involves two aspects:

- Editing the project configuration: project name, entity type, number of records, and description. For example, if you started your project with a limited set of records and you have reached the desired matching rules configuration, you can now remove the limit and run the project on the entire set of data.

- Editing the matching rules configuration: change rule name; [add rule](/management/deduplication/create-a-deduplication-project#add-a-matching-rule); deactivate or delete the rule; modify matching criteria (edit, delete, add).

**To edit the project configuration**

1. In the upper-right corner of a deduplication project, select **Edit**.

1. Make the needed changes, and then select **Save**.

**To edit the matching rules configuration**

- On the **Matching Rules** tab, in the **Status** column, do one of the following:

    - To change the rule name, select the vertical ellipsis button, and then select **Edit name**. Enter the new name and save your changes.

    - To deactivate the rule, turn off the toggle. Deactivated rules are not executed during duplicates detection.

    - To delete the rule, select the vertical ellipsis button, and then select **Delete** and confirm your choice. If you delete the rule, it cannot be reverted.

    - To modify the matching criteria, select the vertical ellipsis button, and then select the needed action: **Edit** or **Delete**.

        ![edit-project.gif](../../assets/images/management/deduplication/edit-project.gif)

You can also add new matching criteria to the rule. To do that, select **Add Matching Criteria**, and fill in the required fields.

When you are satisfied with the project and matching rules configuration, proceed to generate results.

## Archive a deduplication project

You can archive a deduplication project if you no longer need it or if you created it by mistake. You can also consider archiving a deduplication project if you’re confident that you won’t need to run it again in the future.

Archiving does not affect merged that have been submitted to CluedIn. After a deduplication project is archived, it cannot be unarchived.

Archived deduplication projects remain on the Deduplication projects page and they are available for viewing.

You can archive a deduplication project only when its status is **Requires configuration** or **Ready to generate**. In other statuses, you need to discard the results before archiving the project.

**To archive a deduplication project**

- In the upper-right corner of a deduplication project, select **Edit** > **Archive**. Then, confirm that you want to archive the project.

    ![archive-project.gif](../../assets/images/management/deduplication/archive-project.gif)

    The status of a deduplication project becomes **Archived**, and you can no longer work with the project.