---
layout: cluedin
nav_order: 4
parent: Deduplication
grand_parent: Management
permalink: {{ site.baseurl }}/management/deduplication/manage-a-deduplication-project
title: Manage a deduplication project
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

After you create and configure your deduplication project, you can begin the deduplication process to eliminate duplicates and produce a unified and accurate representation of a golden record.

In this article, you will learn how to generate and discard matches in the deduplication project, as well as how to keep your project organized and aligned with your deduplication goals.

The primary action on the deduplication project level is the generation of matches. Its purpose is to analyze a specific set of golden records and detect potential duplicates based on your matching rules. If such duplicates are detected, they are organized into groups. The following diagram illustrates basic project workflow. For more information about project statuses, see [Deduplication reference](/management/deduplication/deduplication-reference).

![manage-dedup-project-flow.gif](../../assets/images/management/deduplication/manage-dedup-project-flow.gif)

{:.important}
Instructions on how to process groups of duplicates, including merging and unmerging, are provided in the [Manage groups of duplicates](/management/deduplication/manage-groups-of-duplicates) article.

## Generate matches

The process of generating matches involves analyzing a specified set of golden records with the goal of finding duplicates among them based on your matching rules.

**To generate matches**

- In the deduplication project, select **Generate matches**, and then confirm your choice.

    ![generate-results.gif](../../assets/images/management/deduplication/generate-results.gif)

    During the process of generating matches, you can view the number of groups found as well as the percentage of golden records that have been checked for duplicates. When the process is complete, the groups of duplicates are displayed on the page. A group contains duplicate records that can be potentially merged into one golden record.

    Next, [process the groups of duplicates](/management/deduplication/manage-groups-of-duplicates)—open each group one by one to review duplicates and fix conflicting values.

**Sorting and filtering of groups**

You can sort the groups of duplicates using column headers—**Name** and **Number of matches**. These column headers contain small arrows pointing up and down. A green arrow pointing up means that column is sorted in ascending order. A green arrow pointing down means that column is sorted in descending order. To change the order, click on the grey arrow in the needed column header.

You can filter the groups of duplicates using the **Min matches – Max matches** slider. This allows you to focus on groups that contain a specific number of matches. For example, if you have a lot of groups of duplicates, you might want to start with small groups first. To do this, set the desired number of matches using the slider. Once you've processed the small groups, you can move on to larger groups by adjusting the slider accordingly.

![sorting-and-filtering.gif](../../assets/images/management/deduplication/sorting-and-filtering.gif)

## Discard matches

If you want to change matching rules, modify project filters, or regenerate matches in the deduplication project, you can discard matches. This action does not affect merged golden records.

**To discard matches**

- In the upper-right corner of the deduplication project, select **Discard matches**, and then confirm your choice.

    ![discard-results.gif](../../assets/images/management/deduplication/discard-results.gif)

    The project status is changed to **Ready to generate**. Now, you can edit the project as needed and generate matches again.

## Edit a deduplication project

You can edit a deduplication project only when its [status](/management/deduplication/deduplication-reference#deduplication-project-statuses) is **Requires configuration** or **Ready to generate**. In other statuses, you need to discard matches before editing the project.

Editing a deduplication project involves two aspects:

- Editing the project configuration: project name, business domain, or advanced filters, and description. For example, if you used advanced filters to narrow down the number of golden records for the project and you have reached the desired matching rules configuration, you can now modify the filters and run the project on the entire set of data.

- Editing the matching rules configuration: change rule name; [add rule](/management/deduplication/create-a-deduplication-project#add-a-matching-rule); deactivate or delete the rule; modify matching criteria (edit, delete, add).

**To edit the project configuration**

1. In the upper-right corner of a deduplication project, select **Edit**.

1. Make the needed changes, and then select **Save**.

**To edit the matching rules configuration**

- On the **Matching Rules** tab, in the **Status** column, do one of the following:

    - To change the rule name, select the vertical ellipsis button, and then select **Edit name**. Enter the new name and save your changes.

    - To deactivate the rule, turn off the toggle. Deactivated rules are not executed during the process of generating matches.

    - To delete the rule, select the vertical ellipsis button, and then select **Delete** and confirm your choice. If you delete the rule, it cannot be reverted.

    - To modify the matching criteria, expand the rule and select the vertical ellipsis button in the needed row. Then select the needed action: **Edit** or **Delete**.

        ![edit-project.gif](../../assets/images/management/deduplication/edit-project.gif)

You can also add new matching criteria to the rule. To do that, expand the rule, and then select **Add Matching Criteria**. When you are satisfied with the project and matching rules configuration, proceed to generate matches.

## Archive a deduplication project

You can archive a deduplication project if you no longer need it or if you created it by mistake. You can also archive a deduplication project if you’re confident that you won’t need to run it again in the future. Archiving does not affect merges that have been submitted to CluedIn.

After a deduplication project is archived, it cannot be unarchived. Archived projects are available only for viewing.

You can archive a deduplication project only when its status is **Requires configuration** or **Ready to generate**. In other statuses, you need to discard matches before archiving the project.

**To archive a deduplication project**

- In the upper-right corner of a deduplication project, select **Edit** > **Archive**. Then, confirm that you want to archive the project.

    ![archive-project.gif](../../assets/images/management/deduplication/archive-project.gif)

    The status of a deduplication project becomes **Archived**, and you can no longer work with the project.

**To view an archived deduplication project**

1. In the upper-right corner of the **Deduplication** page, select **View Archived**.

    ![manage-dedup-project-view-archived.png](../../assets/images/management/deduplication/manage-dedup-project-view-archived.png)

1. From the list of archived deduplication projects, select the one that you want to view.    

## Duplicate a deduplication project

Duplicating a deduplication project means creating a new deduplication project with the configuration of the existing project. This configuration includes filters and matching rules but does not include the deduplication activities performed in the project. By activities, we mean generated matches and merges.

You can duplicate a deduplication project if you want to:

- Use the same matching rules for a different set of golden records. In this case, you only need to modify the filters in the duplicated project.
- Use different matching rules for the same set of golden records. In this case, you only need to modify the matching rules in the duplicated project.

Duplication is a beta feature. To access it, go to **Administration** > **Feature Flags**, and enable the **Duplicate Actions** feature.

![duplicate-actions-feature-flag.png](../../assets/images/shared/duplicate-actions-feature-flag.png)

**To duplicate a deduplication project**

1. In the list of deduplication projects, find a project that you want to duplicate. Then, open the three-dot menu for the project, and select **Duplicate**.

    ![duplicate-deduplication-1.png](../../assets/images/management/deduplication/duplicate-deduplication-1.png)

1. In **Display Name**, review the default name of the new project and modify it if needed. The default name is created by adding __duplicate_ to the name of the project that you're duplicating.

1. In **Filters**, review the filters that will be duplicated for the new project.

1. In **Matching Rules**, review the list of matching rules that will be duplicated for the new project. To view the details of a specific matching rule, select the angle bracket (>) next to the name of the matching rule.

    ![duplicate-deduplication-2.png](../../assets/images/management/deduplication/duplicate-deduplication-2.png)

1. Select **Duplicate**.

    The new deduplication project is created, and it has the **Ready to generate** [status](/management/deduplication/deduplication-reference#project-statuses). Now, you can modify the deduplication project configuration as needed. When you reach the desired configuration, [generate matches](/management/deduplication/manage-a-deduplication-project#generate-matches), and then start working with the [groups of duplicates](/management/deduplication/manage-groups-of-duplicates).    