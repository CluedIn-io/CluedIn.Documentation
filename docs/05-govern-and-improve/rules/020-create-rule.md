---
layout: cluedin
title: Create a rule
parent: Rules
grand_parent: Govern & improve
nav_order: 20
permalink: /govern/rules/create-rule
content_type: how-to
redirect_from: ["/management/rules/create-rule"]
source_path: docs/080-management/rules/020-create-rule.md
tags: ["management", "rules"]
last_modified: 2026-10-26
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Create a rule in the rule builder to change records automatically, test it on one golden record, and then apply it to all golden records that match its filters. Use a data part rule to normalize values in records from different sources, a survivorship rule to choose which value the golden record uses, and a golden record rule to tag or otherwise act on golden records; see [Rule types](/govern/rules/rule-types).

In this article, "rule" means a rule created in the rule builder. It is not a [property rule](/ingest/mapping/property-rules) or a [pre-process rule](/ingest/mapping/preprocess-rules), which act on records during mapping. Inside the **Filters** section, the conditions you add with **Rule** and **Group** are filter conditions, not rules of their own.

## Prerequisites

- The **Rule Builder** claim with at least the Consulted access level, which lets you create and manage your own rules. Informed lets you view rules only. See [Feature access](/administer/users-and-roles/feature-access).

- Golden records for the rule to act on, produced by [processing](/ingest/processing/process-data) a data set.

- A decision on the rule type, which you choose in step 2 of [Create a rule](#create-a-rule). See [Rule types](/govern/rules/rule-types).

## Inputs

| Field | Required | What it accepts |
|--|--|--|
| Rule type | Yes | **Data part rules**, **Survivorship rules**, or **Golden record rules**. See [Rule types](/govern/rules/rule-types). |
| **Name** | Yes | The name of the rule. |
| **Filters** | Not marked as required | Filter conditions that define the golden records the rule applies to. See [Filters](/master/filters). |
| Action **Name** | Yes | The name of the action. |
| **Action** | Yes | The action to perform. The actions available depend on the rule type; see [Rules reference](/govern/rules/rules-reference). Some actions need more details, such as a **Value**. |
| **Description** | No | A rich-text description of how the rule works. |
| **Folder** | No | An existing folder, or the name of a new one. See [Organize rules into folders](/govern/rules/manage-rules#organize-rules-into-folders). |

## How a rule is applied

- **Filters decide which records the rule applies to.** Within a filter, the **AND**/**OR** operator decides how conditions combine: **AND** returns only records where all conditions match, **OR** returns records where any condition matches. Each group has its own operator. See [Filters](/master/filters).

- **Actions run in the order in which they are listed.** You can [reorder actions](/govern/rules/manage-rules#reorder-actions-within-a-rule).

- **Rules run in the rule processing order**, which by default is the order in which the rules were created. See [Edit rule processing order](/govern/rules/manage-rules#edit-rule-processing-order).

- **Only active rules are applied**, to records that match the filter during processing or reprocessing. Saving and activating a rule does not apply it to golden records that already exist; they have to be reprocessed.

- **Data part rules and golden record rules see different values.** Golden record rules take into account only the properties of the golden record, not the properties of its specific data parts. See [Best practices for rules](/govern/rules/best-practices-for-rules).

## Create a rule

Creating a rule involves defining the golden records to which the rule will be applied and specifying the actions to modify these records. The procedure of creating a rule is the same for all types of rules. However, the actions associated with each type of rule are different.

**To create a rule**

1. On the navigation pane, go to **Management** > **Rule builder**.

1. Choose the type of rule that you want to create. Then, select **Create rule**.

1. Enter the name of the rule, and then select **Create**. The rule details page opens.

1. In the **Filters** section, select **Add first filter**, and then specify the golden records to which the rule will be applied. For more information on how to set up a filer, see [Filters](/master/filters).

1. In the **Actions** section, select **Add action**, and then configure the action that will be applied to the golden records matching the filters:

    1. Enter the name of the action.

    1. In the **Action** section, choose the action to be performed by the rule. For more information about the available actions for each rule type, see [Rules reference](/govern/rules/rules-reference). Depending on the chosen action, you might need to provide additional details.

    1. In the lower-right corner, select **Add action**.

1. If you want to add more actions to the rule, repeat step 5.

    Before saving, check the **Rule preview** panel on the right to see what the rule would do; see [Preview a rule before saving](#preview-a-rule-before-saving).

1. Near upper-right corner, select **Save**, and then confirm that you want to save the rule.

1. Activate the rule by turning on the toggle next to the rule status.

    ![Animation: creating a golden record rule named Training with a filter and an Add Tag action, then saving and activating it]({{ "/assets/images/management/rules/create-a-rule.gif" | relative_url }})

    At this point, the rule has not yet been applied to the golden records. To ensure the rule is configured correctly, we recommend applying it to one golden record to verify the results.

## Preview a rule before saving

While you configure a rule's filters and actions, the **Rule preview** panel on the right side of the **Configuration** tab tests the draft against a sample of real golden records, so you can catch a misconfigured filter or action before you save. The preview is a simulation only: it does not change any records, and it does not require the rule to be saved or active.

![The Rule preview panel showing the Matching records tab, with stat tiles for sampled, match, and would-change counts]({{ "/assets/images/management/rules/rule-preview-panel.png" | relative_url }})

- **Sample size** – Near the top of the panel, choose how many records to sample (25, 100, or 500). Select **Refresh preview** to re-run the preview after changing the filters, actions, or sample size; the preview does not update automatically as you type.

- **Matching records** – The records in the sample that match the rule's filters. Select a record to see a condition-by-condition explanation of why it matched, including its current value for each condition.

- **Action preview** – For each matching record, the before and after value of every field the rule's actions would change. A record the actions would not change is labeled **No change**.

- **Checks** – Issues to review before activating the rule, such as an action that failed or a value an action could not map to a new value (for example, an abbreviation missing from a mapping table). When the sample has any checks, a warning banner appears above the tabs; select **Review** to go to the **Checks** tab.

The preview only ever samples existing records; it does not predict how the rule will behave for records ingested later. After saving and activating the rule, use [Test a rule on one record](#test-a-rule-on-one-record) to confirm the real, saved rule behaves as expected.

## Test a rule on one record

After creating a rule, it is a good idea to test it on one golden record to verify that the configuration is correct. This way, you can reprocess just the one golden record instead of all affected golden records. If you find that the rule's actions have not been applied as intended, you can edit the rule and test it on one golden record again until you achieve the desired configuration.

**To test a rule on one golden record**

1. Go to search and add the same filters that you set up in the rule (step 4 in [Create a rule](#create-a-rule)). Then, start the search.

1. Open one golden record from the search results.

1. Near upper-right corner, select **More** > **Re-process entity**.

1. After you see a notification that the request for reprocessing has been sent, reload the page.

1. Check if the golden record has been modified according to the rule.

1. Check what rule has been applied to the golden record:

    1. Go to the **Explain log** tab.

    1. Expand the **Golden record** entry.

    1. Expand **Evaluate rules** > **Summaries**.

        In the tables, you can view the rules and actions that have been applied to the golden record.

    ![Animation: reprocessing one golden record from the More menu, then the Explain Log tab listing the rule and action under Applied rules]({{ "/assets/images/management/rules/test-a-rule.gif" | relative_url }})

1. Depending on the results of your review, do one of the following:

    - If the rule has been applied to the golden record as you intended, proceed to apply the rule to all golden records.

    - If the rule has not been applied to the golden record as intended, edit the rule, and then repeat steps 1–7 until you achieve the desired result.

## Apply a rule to all records

After testing a rule on one golden record and verifying that it is applied as intended, you can proceed to apply the rule to all golden records.

**To apply a rule to all golden records**

1. On the navigation pane, go to **Rule Builder** (or, alternatively, **Management** > **Rule Builder**).

1. Choose the needed type of rule, and then open the rule that you created.

1. In the upper-right corner of the page, select the reprocessing button.

    ![The rule details page with the reprocessing button highlighted, between the Remove and Cancel buttons]({{ "/assets/images/management/rules/create-a-rule/reprocess_btn_sp.png" | relative_url }})

1. Confirm that you want to reprocess all golden records that match the rule's filters.

    {:.important}
    The reprocessing option available on the rule details page is applicable only to the records that match the rule's filters.

    You can track the reprocessing of records in the status bar. If, during the reprocessing, you decide to add another action to the rule or modify a filter, you can cancel the current reprocessing operation and make the needed changes.

    ![The rule header during reprocessing, with a Cancel Reprocessing button and a progress bar at Processing 0 percent]({{ "/assets/images/management/rules/create-a-rule/processing_progress_bar_sp.png" | relative_url }})

1. After the reprocessing is complete, check the rule status.

    ![The rule header after reprocessing, showing 411 affected records and the Healthy status highlighted]({{ "/assets/images/management/rules/create-a-rule/rule_status_after_execution_sp.png" | relative_url }})

    - **Healthy** – the rule executed successfully:

        - Records associated with the rule are modified in accordance with the rule's actions.

        - The **Affected Records** tab shows the list of modified records.

            ![The Affected records tab of a rule, listing the modified golden records with their business domain and property values]({{ "/assets/images/management/rules/create-a-rule/affected_records_tab_sp.png" | relative_url }})

            To view the changes made to a specific record, go to the **History** or **Topology** tab of the golden record page.

    - **Unhealthy** – issues occurred during rule execution. Open the [rule execution logs](#view-rule-execution-logs) to review the details and adjust the rule as needed.

There is an alternative approach to reprocess the records associated with the rule. It involves the GraphQL tool.

**To reprocess records using GraphQL**

1. On the navigation pane, go to **Consume** > **GraphQL**.

1. Enter a query to reprocess the records that should be affected by the rule.

    For example, the following query will reprocess all records that contain the "customer.location" vocabulary key set to "New York".
    ```
    {
     search(query: "customer.location:New York") {
         entries {
             actions {
                 postProcess
             }
         }
     }
    }
    ```

1. Execute the query.

    After the query is executed, the rule's action will be applied to the records matching the rule's filter.

## View rule execution logs

If there are issues in the rule configuration or when applying the rule to the golden records, corresponding information appears in rule execution logs. Use these logs to identify the root cause of an issue and adjust the rule as needed.

CluedIn stores logs only from the last unsuccessful rule execution. Historical logs from earlier executions are not retained.

Each log entry is assigned a severity type, which indicates the importance or seriousness of the logged event. Currently, CluedIn retains only logs of the **Error** severity type (messages about problems that prevented part of a rule from executing correctly). Support for additional severity types will be added in the future.

**To view rule execution logs**

1. On the navigation pane, go to **Rule Builder** (or, alternatively, **Management** > **Rule Builder**).

1. Choose the needed type of rule, and then open the rule that you created.

1. On the rule page, go to the **Log** tab.

1. In the upper-right corner of the page, select the period for which you want to view the logs.

1. Select the category of interest:

    - **PowerFx Rule** – contains logs about errors caused by the configuration of [PowerFx formulas](/govern/rules/power-fx-formulas) in the rule.

    - **General Exceptions** – contains logs about other errors that prevented the rule from executing correctly.

    - **All** – includes both types of information: errors related to PowerFx rules and general exceptions.

1. Review the **Message** column for details about why the issue occurred.

    ![The Log tab of an Unhealthy rule, with categories on the left and General Exception errors listed by message and severity]({{ "/assets/images/management/rules/view-rule-execution-logs/log_tab.png" | relative_url }})

## Verify the result

Reprocessing runs in the background. Selecting the reprocessing button starts it, and you can track its progress on the rule details page.

- **While reprocessing runs**, the rule details page shows a progress bar and a **Cancel Reprocessing** button.

- **When it has finished**, the rule shows its status, **Healthy** or **Unhealthy**, and the number of **Affected Records**.

- **On the Affected records tab**, the modified golden records are listed. To view the changes made to one record, go to the **History** or **Topology** tab of the golden record page.

- **On one golden record**, the **Explain log** tab shows under **Evaluate rules** > **Summaries** which rules and actions were applied. See [Test a rule on one record](#test-a-rule-on-one-record).

## What this changes

- **Saving and activating a rule** saves configuration only. Golden records that already exist are not changed until they are reprocessed. While the rule is active, it is applied to records that match its filter whenever they are processed or reprocessed.

- **Reprocessing** applies the rule's actions to the records that match its filters: data part rules change values in data parts, survivorship rules change which value the golden record uses, and golden record rules act on the golden record, for example by adding a tag.

- **Undoing a rule.** Deactivating or deleting a rule does not undo its changes by itself: the records affected by the rule still contain changes according to the rule's action, and return to their initial state when they are reprocessed. When you edit a rule's filters or actions, you can choose to reprocess the records affected by the previous and current configuration. See [Manage rules](/govern/rules/manage-rules).

## If something goes wrong

- **The rule status is Unhealthy.** Open the [rule execution logs](#view-rule-execution-logs) to see why. Only the logs from the last unsuccessful execution are kept.

- **Errors in the PowerFx Rule log category.** A [PowerFx formula](/govern/rules/power-fx-formulas) in the rule is misconfigured.

- **The rule was not applied to a golden record.** Check that the rule is active, that the golden record matches the rule's filters (run the same filters in search), and that the record has been reprocessed since the rule was activated. The **Explain log** shows whether any matching rules were found. See [Rules not working as expected](/troubleshooting/rules-not-working).

- **Another rule overrides the result.** Rules run in the rule processing order. See [Edit rule processing order](/govern/rules/manage-rules#edit-rule-processing-order).

- **Reprocessing is slow.** See [Rules running slowly](/troubleshooting/rules-slow).

- **You need to change the rule during reprocessing.** Select **Cancel Reprocessing**, make the changes, and reprocess again.
