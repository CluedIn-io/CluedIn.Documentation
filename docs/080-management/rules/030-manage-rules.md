---
layout: default
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
1. TOC
{:toc}

In this article, you will learn how to manage rules to keep them organized, efficient, and aligned with your data management goals.

## Edit a rule

You can edit a rule to make necessary changes in rule name, description, filters, and actions.

**To edit a rule**

1. In the rule details page, make the needed changes.

1. If you are the owner of the rule, near the upper-right corner of the rule details page, select **Save**.

    After you confirm that you want to update the rule, your changes will be applied immediately.

1. If you are not the owner of the rule, near the upper-right corner of the rule details page, select **Submit for approval**.

    The owner of the rule will receive a notification about your changes and can then approve or reject them.

## Delete a rule

You can delete a rule in any status if you no longer need it. You can delete a rule only if you are the owner of the rule; you cannot delete rules created by other users.

There are two ways to delete a rule:

- From the list of rules – this option allows you to delete multiple rules at once.

- From the rule details page.

**To delete a rule from the list of rules**

1. Select the checkbox next to the rule that you want to delete.

1. Select **Delete**, and then confirm your choice.

**To delete a rule from the rule details page**

- Select the delete icon. Then, confirm your choice.

After the rule is deleted, the records affected by the rule will still contain changes according to the rule's action. However, when you [reprocess](/management/rules/create-rule#re-process-records) such records, they will return to their initial state before the rule was applied.

## Activate and deactivate a rule

When active, the rule is applied to records that match its filter during processing or reprocessing. If you no longer want to apply the rule, you can deactivate it. Yet, if you change your mind, you can easily activate the rule.

There are two ways to activate and deactivate a rule:

- From the list of rules – this option allows you to activate or deactivate multiple rules at once.

- From the rule details page.

**To activate or deactivate the rule from the list of rules**

1. Select the checkbox next to the rule that you want to activate or deactivate.

1. Near the upper-right corner of the list of rules, select the needed action.

**To activate or deactivate the rule from the rule details page**

- Near the upper-right corner, turn on or off the status toggle.

After the rule is deactivated, the records affected by the rule will still contain changes according to the rule's action. However, when you reprocess such records, they will return to their initial state before the rule was applied.

## Edit rule processing order

The default rule processing order is the order in which the rules were created. However, you have the flexibility to adjust the rule processing sequence. This allows you to prioritize the execution of specific rules over others. For example, if you have two rules with the same filters but different actions, you can determine which rule should be applied to the records first.

**To edit the rule processing order**

1. In the list of rules, near the upper-right corner, select **Edit Rule Processing Order**.

1. Change the rule processing order by doing one of the following:

    - Select the rule and drag it to the needed position.

    - Choose the number of the rule to define the order of processing.

    - Move the rule up or down by using the arrows in the right side of the rule.

1. Select **Save**.

## Process pending changes

If you are the owner of the rule and somebody else makes changes to the rule, you'll receive a notification about a request for approval. All requests are listed on the **Pending Changes** tab of the rule.

**To process pending changes**

1. Review the details of the change request by selecting **View Changes**.

    A new pane opens, where you can view the changes to the rule.

1. Depending on whether you agree with the suggested changes, in the **Actions** tab, select **Approve** or **Reject**.

    If you approved the change request, the rule is updated accordingly. If you rejected the change request, no changes are made to the rule.

