---
layout: cluedin
nav_order: 3
parent: Rules
grand_parent: Management
permalink: /management/rules/manage-rules
title: Manage rules
tags: ["management", "rules"]
last_modified: 2023-11-16
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to manage rules to keep them organized, efficient, and aligned with your data management goals.

## Edit a rule

You can edit a rule to make necessary changes in rule name, description, filters, and actions.

**To edit a rule**

1. On the navigation pane, go to **Management** > **Rule builder**.

1. Choose the needed type of rule, and then open the rule that you want to edit.

1. In the rule details page, make the needed changes.

1. If you are the owner of the rule, near the upper-right corner of the rule details page, select **Save**.

    If you modified filters or actions, select the checkbox to reprocess the records affected by the previous and current rule configuration. Selecting the checkbox will revert the records affected by the previous rule configuration to their initial state before the rule was applied. Simultaneously, the records affected by the current rule configuration will be adjusted according to the rule's action. If you don't select the checkbox, the rule will be updated but the records won't be reprocessed.
    
    ![manage-rules-1.png]({{ "/assets/images/management/rules/manage-rules-1.png" | relative_url }})
    
    After you confirm that you want to update the rule, your changes will be applied immediately.

1. If you are not the owner of the rule, near the upper-right corner of the rule details page, select **Submit for approval**.

    The owner of the rule will receive a notification about your changes and can then approve or reject them.

## Delete a rule

You can delete a rule in any status if you no longer need it. You can delete a rule only if you are the owner of the rule; you cannot delete rules created by other users.

After the rule is deleted, the records affected by the rule will still contain changes according to the rule's action. However, when you reprocess such records, they will return to their initial state before the rule was applied.

There are two ways to delete a rule:

- From the list of rules – this option allows you to delete multiple rules at once.

- From the rule details page.

**To delete a rule from the list of rules**

1. Select the checkbox next to the rule that you want to delete.

1. Select **Delete**, and then confirm your choice.

**To delete a rule from the rule details page**

- Select the delete icon. Then, confirm your choice.

## Activate and deactivate a rule

When active, the rule is applied to records that match its filter during processing or reprocessing. If you no longer want to apply the rule, you can deactivate it. If you change your mind, you can easily activate the rule.

After the rule is deactivated, the records affected by the rule will still contain changes according to the rule's action. However, when you reprocess such records, they will return to their initial state before the rule was applied.

There are two ways to activate and deactivate a rule:

- From the list of rules – this option allows you to activate or deactivate multiple rules at once.

- From the rule details page.

**To activate or deactivate the rule from the list of rules**

1. Select the checkbox next to the rule that you want to activate or deactivate.

1. Near the upper-right corner of the list of rules, select the needed action.

**To activate or deactivate the rule from the rule details page**

- Near the upper-right corner, turn on or off the status toggle.

## Edit rule processing order

The default rule processing order is the order in which the rules were created. However, you have the flexibility to adjust the rule processing sequence. This allows you to prioritize the execution of specific rules over others. For example, if you have two rules with the same filters but different actions, you can determine which rule should be applied to the records first.

**To edit the rule processing order**

1. In the list of rules, near the upper-right corner, select **Edit rule processing order**.

1. Change the rule processing order by doing one of the following:

    - Select the rule and drag it to the needed position.

    - Choose the number of the rule to define the order of processing.

    - Move the rule up or down by using the arrows in the right side of the rule.

1. Select **Save**.

## Process pending changes

If you are the owner of the rule and somebody else makes changes to the rule, you'll receive a notification about a request for approval. All requests are listed on the **Pending changes** tab of the rule.

**To process pending changes**

1. Review the details of the change request by selecting **View changes**.

    A new pane opens, where you can view the changes to the rule.

1. Depending on whether you agree with the suggested changes, in the **Actions** tab, select **Approve** or **Reject**.

    If you approved the change request, the rule is updated accordingly. If you rejected the change request, no changes are made to the rule.

## Duplicate a rule

Duplicating a rule means creating a new rule with the configuration of the existing rule. This configuration includes filters and rule actions but does not include the activities performed by the rule. By activities, we mean the changes applied to data parts or golden records according to the rule’s actions. For example, if you duplicate a golden record rule with the action to add tags to all golden records, the new rule will not automatically add the same tags to golden records.

You can duplicate a rule if you want to:

- Use the same actions for a different set of golden records. In this case, you only need to modify the filters in the duplicated rule.
- Use different rule actions for the same set of golden records. In this case, you only need to modify the actions in the duplicated rule.

Duplication is a beta feature. To access it, go to **Administration** > **Feature Flags**, and enable the **Duplicate Actions** feature.

![duplicate-actions-feature-flag.png]({{ "/assets/images/shared/duplicate-actions-feature-flag.png" | relative_url }})

**To duplicate a rule**

1. In the list of rules, find a rule that you want to duplicate. Then, open the three-dot menu for the rule, and select **Duplicate**.

    ![duplicate-rule-1.png]({{ "/assets/images/management/rules/duplicate-rule-1.png" | relative_url }})

1. In **Name**, review the default name of the new rule and modify it if needed. The default name is created by adding __duplicate_ to the name of the rule that you're duplicating.

1. In **Conditions**, review the filters that will be duplicated for the new rule.

1. In **Actions**, review the list of rule actions that will be duplicated for the new rule. To view the details of a specific rule action, select **View Action Details**.

    ![duplicate-rule-2.png]({{ "/assets/images/management/rules/duplicate-rule-2.png" | relative_url }})

1. Select **Duplicate**.

    The new rule is created. By default, it is inactive. Now, you can modify the rule configuration as needed. When you reach the desired configuration, save your changes, [activate](/management/rules/manage-rules#activate-and-deactivate-a-rule) the rule, and then [reprocess](/management/rules/create-rule#apply-a-rule-to-all-records) the affected records.