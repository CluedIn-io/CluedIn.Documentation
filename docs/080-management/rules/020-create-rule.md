---
layout: cluedin
nav_order: 2
parent: Rules
grand_parent: Management
permalink: /management/rules/create-rule
title: Create a rule
tags: ["management", "rules"]
last_modified: 2023-11-16
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to create a rule, validate it on one golden record to ensure it works as expected, and then apply the rule to all records.

## Create a rule

Creating a rule involves defining the golden records to which the rule will be applied and specifying the actions to modify these records. The procedure of creating a rule is the same for all types of rules. However, the actions associated with each type of rule are different.

**To create a rule**

1. On the navigation pane, go to **Management** > **Rule builder**.

1. Choose the type of rule that you want to create. Then, select **Create rule**.

1. Enter the name of the rule, and then select **Create**. The rule details page opens.

1. In the **Filters** section, select **Add first filter**, and then specify the golden records to which the rule will be applied. For more information on how to set up a filer, see [Filters](/key-terms-and-features/filters).

1. In the **Actions** section, select **Add action**, and then configure the action that will be applied to the golden records matching the filters:

    1. Enter the name of the action.

    1. In the **Action** section, choose the action to be performed by the rule. For more information about the available actions for each rule type, see [Rules reference](/management/rules/rules-reference). Depending on the chosen action, you might need to provide additional details.

    1. In the lower-right corner, select **Add action**.

1. If you want to add more actions to the rule, repeat step 5.

1. Near upper-right corner, select **Save**, and then confirm that you want to save the rule.

1. Activate the rule by turning on the toggle next to the rule status.

    ![create-a-rule.gif](../../assets/images/management/rules/create-a-rule.gif)

    At this point, the rule has not yet been applied to the golden records. To ensure the rule is configured correctly, we recommend applying it to one golden record to verify the results.

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

    ![test-a-rule.gif](../../assets/images/management/rules/test-a-rule.gif)

1. Depending on the results of your review, do one of the following:

    - If the rule has been applied to the golden record as you intended, proceed to apply the rule to all golden records.

    - If the rule has not been applied to the golden record as intended, edit the rule, and then repeat steps 1–7 until you achieve the desired result.

## Apply a rule to all records

After testing a rule on one golden record and verifying that it is applied as intended, you can proceed to apply the rule to all golden records.

**To apply a rule to all golden records**

1. On the navigation pane, go to **Management** > **Rule builder**.

1. Choose the needed type of rule, and then open the rule that you created.

1. Near upper-right corner, select the reprocessing button.

1. Confirm that you want to reprocess all golden records that match the rule's filter.

    ![reprocess-a-rule.gif](../../assets/images/management/rules/reprocess-a-rule.gif)

    {:.important}
    The reprocessing option available on the rule details page is applicable only to the records that match the rule's filter.

    You can track the reprocessing of records in the status bar. If, during the reprocessing, you decide to add another action to the rule or modify a filter, you can cancel the current reprocessing operation and make the needed changes.

    After the reprocessing is completed, the records associated with the rule are modified in accordance with the rule's actions.

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