---
layout: cluedin
nav_order: 7
parent: Additional operations
grand_parent: Integration
permalink: /integration/additional-operations-on-records/remove-golden-records
title: Remove golden records
last_modified: 2024-04-30
---

In this article, you will learn how to remove golden records that were created from a specific data source.

If you no longer need specific golden records, you can easily remove them. Keep in mind that when you remove golden records from CluedIn, the count of [billable records](/key-terms-and-features/billable-records) will decrease when it is recalculated.

After removing golden records, you'll notice that the **Data** tab disappears from the data set. Additionally, the **Process** tab won't contain any information about previous processing. However, the incoming records on the **Preview** tab remain intact; and the mapping configuration on the **Map** tab is preserved, so you can edit, reset, or reuse it for other data sets.

Removing golden records can be useful in the following cases:

- If you notice an error in the mapping configuration. Although the mapping configuration is preserved after removing golden records, you can reset the mapping and start again.

- If you processed a subset of data to test the mapping configuration and you don't need the test data anymore. Since the mapping configuration is preserved, you can reuse it for other data sets.

**Prerequisites**

Go to **Administration** > **Feature Flags**, and then enable the **Remove Golden Records** feature.

![remove-golden-records-1.png](../../assets/images/integration/additional-operations/remove-golden-records-1.png)

**To remove golden records**

1. On the navigation pane, go to **Integrations** > **Data Sources**.

1. Find and open the data source that contains golden records that you want to remove.

1. Near the upper-right corner of the data source details page, select **Remove records**.

    The **Remove processed records** dialog opens where you can view the number of golden records that will be removed as well as the data set containing those records.

1. Confirm that you want to remove golden records by entering _REMOVE_. Then, select **Remove records**.

    ![remove-golden-records-2.gif](../../assets/images/integration/additional-operations/remove-golden-records-2.gif)

The process of removing golden records might take some time. After golden records are removed, you can make changes in the data set (edit mapping, add or remove property or pre-process rules) or process the data set again.