---
layout: cluedin
title: Manage a deduplication project
parent: Deduplication
grand_parent: Master
nav_order: 40
permalink: /master/deduplication/manage-a-deduplication-project
content_type: how-to
redirect_from: ["/management/deduplication/manage-a-deduplication-project"]
source_path: docs/080-management/deduplication/040-manage-a-deduplication-project.md
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

After you create and configure your deduplication project, you can begin the deduplication process to eliminate duplicates and produce a unified and accurate representation of a golden record.

In this article, you will learn how to generate and discard matches in the deduplication project, as well as how to keep your project organized and aligned with your deduplication goals.

The primary action on the deduplication project level is the generation of matches. Its purpose is to analyze a specific set of golden records and detect potential duplicates based on your matching rules. If such duplicates are detected, they are organized into groups. The following diagram illustrates basic project workflow. For more information about project statuses, see [Deduplication reference](/master/deduplication/deduplication-reference).

![Diagram: at project level, Generate matches produces groups 1 to N. At group level, each group is processed and merged into merged golden records. If not satisfied with merges, unmerge groups; to change configuration and start over, Discard matches at project level]({{ "/assets/images/management/deduplication/manage-dedup-project-flow.gif" | relative_url }})

{:.important}
Instructions on how to process groups of duplicates, including merging and unmerging, are provided in the [Manage groups of duplicates](/master/deduplication/manage-groups-of-duplicates) article.

## Preview a project's scope

Before you generate matches—or at any later point—you can check which golden records a project's business domain or filters actually resolve to, independent of any matching rule.

**To preview a project's scope**

- On the **Preview** tab, review the sample of records shown, and the total count of records currently in scope.

    CluedIn samples up to 200 records and shows the true total count alongside them. If the total is much larger than expected, or the records shown are not the ones you meant to check, revisit the project's business domain or filters before generating matches.

## Generate matches

The process of generating matches involves analyzing a specified set of golden records with the goal of finding duplicates among them based on your matching rules.

**To generate matches**

- In the deduplication project, select **Generate matches**, and then confirm your choice.

    ![Animation: selecting Generate matches in a deduplication project, confirming, and watching the groups of duplicates appear]({{ "/assets/images/management/deduplication/generate-results.gif" | relative_url }})

    During the process of generating matches, you can view the number of groups found as well as the percentage of golden records that have been checked for duplicates. When the process is complete, the groups of duplicates are displayed on the page. A group contains duplicate records that can be potentially merged into one golden record.

    CluedIn records when generation started for the current result set. The deduplication project list exposes this as **Last generation**, which helps you understand how fresh a project's matching results are and lets you sort projects by their most recent generation.

    Next, [process the groups of duplicates](/master/deduplication/manage-groups-of-duplicates)—open each group one by one to review duplicates and fix conflicting values.

**Sorting and filtering of groups**

You can sort the groups of duplicates using column headers—**Name** and **Number of matches**. These column headers contain small arrows pointing up and down. A green arrow pointing up means that column is sorted in ascending order. A green arrow pointing down means that column is sorted in descending order. To change the order, click on the grey arrow in the needed column header.

You can filter the groups of duplicates using the **Min matches – Max matches** slider. This allows you to focus on groups that contain a specific number of matches. For example, if you have a lot of groups of duplicates, you might want to start with small groups first. To do this, set the desired number of matches using the slider. Once you've processed the small groups, you can move on to larger groups by adjusting the slider accordingly.

![Animation: sorting groups of duplicates by the Name and Number of matches columns and adjusting the Min matches to Max matches slider]({{ "/assets/images/management/deduplication/sorting-and-filtering.gif" | relative_url }})

**Generate matches for multiple projects at once**

From the list of deduplication projects, you can select multiple projects and generate matches for all of them at once, instead of opening each project individually.

1. On the navigation pane, go to **Management** > **Deduplicate**.

1. In the list of deduplication projects, select the checkbox next to each project that you want to generate matches for. You can also select the checkbox in the header row to select all projects on the page.

1. Near the upper-right corner of the list of deduplication projects, select **Generate matches**.

    Match generation starts independently for each selected project; if it fails to start for one project, the rest of the selected projects are not affected.

## Generate matches with multiple strategies

Instead of generating matches once, you can run generate matches with more than one matching strategy in sequence, and then compare whether the strategies agree on the same groups. This is useful when you are not sure which strategy best fits your data, or want to validate a strategy against another before relying on it.

**To generate matches with multiple strategies**

1. In the deduplication project, select **Generate matches**.

1. Turn on **Compare multiple strategies**, and select the strategies that you want to run.

1. Confirm your choice.

    CluedIn runs each selected strategy in turn, recording each run on the **Report** tab. The groups shown on the **Matches** tab after this finishes are from the last strategy that ran; this is the same result you get from generating matches normally.

1. On the **Audit** tab, select two or more of the runs, and then select **Compare** to see whether they grouped the same records together.

For the statistics recorded for each run, see [Report tab](/master/deduplication/deduplication-reference#report-tab). For how run comparison works, see [Run comparison (Audit tab)](/master/deduplication/deduplication-reference#run-comparison-audit-tab).

## Choose an ACI partitioning strategy

When you run generate matches with **Run in ACI** selected, on an ACI-compatible project, you can choose how CluedIn splits the work across containers if it needs more than one.

**To choose an ACI partitioning strategy**

1. In the deduplication project, select **Generate matches**, and turn on **Run in ACI**.

1. Under **Advanced options**, select one of the following:

    - **None (default)** – no partitioning strategy; CluedIn uses its default container split.
    - **MinHash** – groups similar records into the same container using MinHash locality-sensitive hashing, so likely matches are more often compared within the same container.
    - **BIRCH** – groups records into containers using a hashing-based clustering approach.
    - **Sorted neighbourhood** – sorts records and assigns neighboring records to the same container.

1. Confirm your choice to generate matches.

{:.important}
This setting only affects how ACI distributes work across containers when a run needs more than one. It does not change which records are matched, or their calculated confidence.

## Automate a deduplication project

Automating a deduplication project means that CluedIn generates matches and merges groups on a recurring schedule, without you reviewing each group yourself. Because automation skips manual review, CluedIn only allows it when it can be confident the merges are correct, in one of two ways:

- **Exact-match rules only** – by default, a project can be automated only if every matching rule uses an exact matching function, such as **Equals** or **Email**, with no fuzzy matching and no normalization rules beyond a small set of safe ones. Matches found this way are merged automatically because there is no ambiguity in what counts as a match.

- **A confidence threshold** – alternatively, you can set a minimum match confidence for the project. Once set, automation is no longer restricted to exact-match rules: any group whose calculated confidence is at or above the threshold is merged automatically, regardless of which matching function found it. A group whose confidence has not yet been calculated is never merged automatically, even if the project's threshold is 0%.

{:.important}
Setting a confidence threshold is an opt-in, project-level choice. A project that does not set one keeps the original exact-match-only behavior.

**To preview automatic merges before turning on automation**

- In the project configuration, enter a candidate confidence threshold, and select **Preview**. CluedIn shows how many of the project's current groups would be merged at that threshold, without merging anything.

**To automate a deduplication project**

1. In the project configuration, optionally set a confidence threshold, and then save the project.

1. Select **Automate**, and confirm your choice.

    The project status becomes **Automated**. CluedIn generates matches and merges eligible groups on the configured schedule.

**To stop automation**

- In the project, select **Stop automation**.

Merges made through automation appear on the **Merges** tab and can be [unmerged](/master/deduplication/manage-groups-of-duplicates#unmerge-records) like any other merge, and are recorded on the **Audit Log** tab as **Auto-merge by confidence** when a threshold produced them.

## Discard matches

If you want to change matching rules, modify project filters, or regenerate matches in the deduplication project, you can discard matches. This action does not affect merged golden records.

**To discard matches**

- In the upper-right corner of the deduplication project, select **Discard matches**, and then confirm your choice.

    ![Animation: selecting Discard matches in a deduplication project, confirming, and the status changing to Ready to generate]({{ "/assets/images/management/deduplication/discard-results.gif" | relative_url }})

    The project status is changed to **Ready to generate**. Now, you can edit the project as needed and generate matches again.

## Export possible matches and import review decisions

You can export a project's possible matches to a file, review them outside CluedIn—for example, with a colleague who does not have access to CluedIn—and then import the decisions back in.

**To export possible matches**

- On the **Matches** tab, select **Export**, and then choose **CSV** or **Excel**.

    The exported file has one row per record, with the group it belongs to, its current status, its match confidence, and the matching rules that contributed to the group—enough to identify which group and record each row refers to.

**To import review decisions**

1. On the **Matches** tab, select **Import decisions**.

1. Choose a CSV or Excel file with a **GroupId** column, an optional **EntityId** column, and a **Decision** column set to **Merge** or **DoNotMerge** for each row. The exported file is already in this format; set the **Decision** column to record your reviewers' choices, and remove rows you do not want to apply.

    Include **EntityId** only when you want to reject a single record out of a group rather than the whole group.

1. Select the file, and confirm the import.

    CluedIn applies **Merge** as approving the group, and **DoNotMerge** as rejecting the group or, when **EntityId** is set, removing that record from the group. After the import finishes, CluedIn reports how many rows were applied and, for any row it could not apply—for example, a group that no longer exists—the reason why.

Applying decisions through import changes group status the same way as approving or rejecting manually; it does not merge any records. [Merge the approved groups](/master/deduplication/manage-groups-of-duplicates#merge-groups) as a separate step.

## Edit a deduplication project

You can edit a deduplication project only when its [status](/master/deduplication/deduplication-reference#deduplication-project-statuses) is **Requires configuration** or **Ready to generate**. In other statuses, you need to discard matches before editing the project.

Editing a deduplication project involves two aspects:

- Editing the project configuration: project name, business domain, or advanced filters, and description. For example, if you used advanced filters to narrow down the number of golden records for the project and you have reached the desired matching rules configuration, you can now modify the filters and run the project on the entire set of data.

- Editing the matching rules configuration: change rule name; [add rule](/master/deduplication/create-a-deduplication-project#add-a-matching-rule); deactivate or delete the rule; modify matching criteria (edit, delete, add).

**To edit the project configuration**

1. In the upper-right corner of a deduplication project, select **Edit**.

1. Make the needed changes, and then select **Save**.

**To edit the matching rules configuration**

- On the **Matching Rules** tab, in the **Status** column, do one of the following:

    - To change the rule name, select the vertical ellipsis button, and then select **Edit name**. Enter the new name and save your changes.

    - To deactivate the rule, turn off the toggle. Deactivated rules are not executed during the process of generating matches.

    - To delete the rule, select the vertical ellipsis button, and then select **Delete** and confirm your choice. If you delete the rule, it cannot be reverted.

    - To modify the matching criteria, expand the rule and select the vertical ellipsis button in the needed row. Then select the needed action: **Edit** or **Delete**.

        ![Animation: expanding a matching rule on the Matching Rules tab and using the vertical ellipsis menu to edit or delete a matching criterion]({{ "/assets/images/management/deduplication/edit-project.gif" | relative_url }})

You can also add new matching criteria to the rule. To do that, expand the rule, and then select **Add Matching Criteria**. When you are satisfied with the project and matching rules configuration, proceed to generate matches.

## Organize deduplication projects into folders

You can use folders to organize deduplication projects—for example, by business domain or by team. Deduplication projects that aren't assigned to a folder appear in the root list.

![Deduplication projects list with a folder bar showing Root, Finance and Sales above the projects table, which includes a Last generation column]({{ "/assets/images/management/deduplication/organize-deduplication-projects-folders.png" | relative_url }})

**To assign a deduplication project to a folder**

1. In the list of deduplication projects, find the project that you want to move. Then, open the three-dot menu for the project, and select **Move to folder**.

1. In **Select folder**, choose an existing folder, or type a new folder name to create one.

    ![Move to folder dialog with the Select folder dropdown set to No folder]({{ "/assets/images/management/deduplication/move-deduplication-project-to-folder.png" | relative_url }})

1. Select **Save**.

You can also drag a deduplication project from the list and drop it onto a folder in the folder bar to move it there.

**To view the deduplication projects in a folder**

- In the folder bar, select the folder that you want to view.

    ![Sales folder selected in the folder bar, listing the deduplication projects Marketing Leads and CRM Contacts]({{ "/assets/images/management/deduplication/deduplication-project-inside-folder.png" | relative_url }})

    Select **Root** to return to the list of deduplication projects that aren't assigned to a folder.

**To move a deduplication project to a different folder**

- Open the three-dot menu for the project, select **Move to folder**, choose the new folder, and then select **Save**. You can also drag the project onto a different folder in the folder bar.

**To remove a deduplication project from its folder**

- Open the three-dot menu for the project, and select **Remove from folder**. The project returns to the root list. You can also drag the project onto **Root** in the folder bar.

**To rename a folder**

- In the folder bar, select the pencil icon next to the folder, enter the new name, and then select **Save**. Renaming a folder updates it for every deduplication project assigned to it.

## Archive a deduplication project

You can archive a deduplication project if you no longer need it or if you created it by mistake. You can also archive a deduplication project if you’re confident that you won’t need to run it again in the future. Archiving does not affect merges that have been submitted to CluedIn.

After a deduplication project is archived, it cannot be unarchived. Archived projects are available only for viewing.

You can archive a deduplication project only when its status is **Requires configuration** or **Ready to generate**. In other statuses, you need to discard matches before archiving the project.

**To archive a deduplication project**

- In the upper-right corner of a deduplication project, select **Edit** > **Archive**. Then, confirm that you want to archive the project.

    ![Animation: selecting Edit then Archive in a deduplication project and confirming, after which the project status becomes Archived]({{ "/assets/images/management/deduplication/archive-project.gif" | relative_url }})

    The status of a deduplication project becomes **Archived**, and you can no longer work with the project.

**To view an archived deduplication project**

1. In the upper-right corner of the **Deduplication** page, select **View Archived**.

    ![Deduplicate page listing deduplication projects, with View archived highlighted in the upper-right corner]({{ "/assets/images/management/deduplication/manage-dedup-project-view-archived.png" | relative_url }})

1. From the list of archived deduplication projects, select the one that you want to view.    

## Duplicate a deduplication project

Duplicating a deduplication project means creating a new deduplication project with the configuration of the existing project. This configuration includes filters and matching rules but does not include the deduplication activities performed in the project. By activities, we mean generated matches and merges.

You can duplicate a deduplication project if you want to:

- Use the same matching rules for a different set of golden records. In this case, you only need to modify the filters in the duplicated project.
- Use different matching rules for the same set of golden records. In this case, you only need to modify the matching rules in the duplicated project.

Duplication is a beta feature. To access it, go to **Administration** > **Feature Flags**, and enable the **Duplicate Actions** feature.

![Duplicate Actions feature flag card, marked Beta, with the toggle set to Enabled]({{ "/assets/images/shared/duplicate-actions-feature-flag.png" | relative_url }})

**To duplicate a deduplication project**

1. In the list of deduplication projects, find a project that you want to duplicate. Then, open the three-dot menu for the project, and select **Duplicate**.

    ![Three-dot menu for a deduplication project opened, with the Duplicate option highlighted]({{ "/assets/images/management/deduplication/duplicate-deduplication-1.png" | relative_url }})

1. In **Display Name**, review the default name of the new project and modify it if needed. The default name is created by adding __duplicate_ to the name of the project that you're duplicating.

1. In **Filters**, review the filters that will be duplicated for the new project.

1. In **Matching Rules**, review the list of matching rules that will be duplicated for the new project. To view the details of a specific matching rule, select the angle bracket (>) next to the name of the matching rule.

    ![Duplicate deduplication project dialog with the Display name, read-only Filters and business domain, Matching rules list, and the Duplicate button]({{ "/assets/images/management/deduplication/duplicate-deduplication-2.png" | relative_url }})

1. Select **Duplicate**.

    The new deduplication project is created, and it has the **Ready to generate** [status](/master/deduplication/deduplication-reference#project-statuses). Now, you can modify the deduplication project configuration as needed. When you reach the desired configuration, [generate matches](/master/deduplication/manage-a-deduplication-project#generate-matches), and then start working with the [groups of duplicates](/master/deduplication/manage-groups-of-duplicates).    