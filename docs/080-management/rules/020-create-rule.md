---
layout: default
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

In this article, you will learn how to create a business rule to streamline the modification and management of your records.

## Create a rule

The procedure for creating a rule is the same for all types of rules. However, the actions associated with each type of rule are different.

**To create a rule**

1. On the navigation pane, go to **Management** > **Rule Builder**.

1. Choose the type of rule that you want to create. Then, select **Create Rule**.

1. Enter the name of the rule, and then select **Create**.

    The rule details page opens.

1. In the **Filters** section, select **Add First Filter**, and then specify to which properties or vocabulary keys the rule will be applied. For more information on how to set up a filer, see [Filters](/key-terms-and-features/filters).

1. In the **Actions** section, select **Add Action**, and then configure the action that will be performed on the records matching the filter:

    1. Enter the name of the action.

    1. In the **Action** section, choose the action to be performed by the rule. The information about the available actions for each rule is provided in [Rules reference](/management/rules/rules-reference).

        Depending on the chosen action, you might need to provide additional details.

        ![create-rule-1.png](../../assets/images/management/rules/create-rule-1.png)

    1. In the lower-right corner, select **Add Action**.

        **Note:** You can add multiple actions to the rule.

1. In the upper-right corner of the rule details page, select **Save**.

1. Activate the rule by turning on the toggle next to the rule status.

    You created the rule. The rule will be applied to the records that match the rule's filter when they are processed or reprocessed. Next, explore the available methods to reprocess the records, along with the various options for [managing the rule](/management/rules/manage-rules).


## Re-process records

The main approach to reprocess the records is through the rule details page.

**To reprocess records through the rule details page**

1. Near the upper-right corner, select ![reprocess-icon.png](../../assets/images/management/rules/preprocess-icon.png).

1. Confirm that you want to reprocess records matching the rule's filter.

    You can track the reprocessing of records in the status bar. If, during the reprocessing, you decide to add another action to the rule or modify a filter, you can cancel the current reprocessing operation and make the needed changes. After the reprocessing is completed, the records associated with the rule are updated in accordance with the rule's actions.

    **Note:** The reprocessing option available on the rule details page is applicable only to the records that match the current rule's filter.

The other approaches to reprocessing the records include the following:

- Reprocessing using the GraphQL tool – use this approach if you need to re-process many records.

- Reprocessing each record manually – use this approach if you need to re-process few records.

**To reprocess records using GraphQL**

1. On the navigation pane, go to **Consume** > **GraphQL**.

1. Enter a query to re-process the records that should be affected by the rule.

    For example, the following query will re-process all records that contain the "customer.location" vocabulary key set to "New York".
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

**To reprocess records manually**

1. Find and open the needed record.

1. In the upper-right corner of the record details page, select **More** > **Re-process entity**.

    ![create-rule-2.png](../../assets/images/management/rules/create-rule-2.png)

    After the record is re-processed, the rule's action will be applied to it.