---
layout: cluedin
nav_order: 7
parent: Additional operations
grand_parent: Integration
permalink: /integration/additional-operations-on-records/remove-records
title: Remove records
last_modified: 2024-00-25
---

In this article, you will learn how to remove records (also referred to as data parts) that were created from a specific data source. For more information about records, data parts, and golden records, see [Data life cycle](/key-terms-and-features/data-life-cycle).

If you no longer need records from a specific data source, you can easily remove them. If a record is not merged during processing, it becomes a golden record. Removing such a record also removes the golden record. However, if a record is merged into the existing golden record, removing it doesn't remove the entire golden record; only the specific data part represented by that record is removed. Keep in mind that when you remove records from CluedIn, the count of [billable records](/key-terms-and-features/billable-records) will decrease when it is recalculated.

After removing records, you'll notice that the **Data** tab disappears from the data set. Additionally, the **Process** tab won't contain any information about previous processing. However, the incoming records on the **Preview** tab remain intact; and the mapping configuration on the **Map** tab is preserved, so you can edit, reset, or reuse it for other data sets.

Removing records can be useful in the following cases:

- If you notice an error in the mapping configuration. Although the mapping configuration is preserved after removing records, you can reset the mapping and start again.

- If you processed a subset of data to test the mapping configuration and you don't need the test data anymore. Since the mapping configuration is preserved, you can reuse it for other data sets.

**What happens if you remove records from one of the data sources that form a golden record?**

Consider a scenario where a golden record is composed of data parts from three sources. If you remove records from one of these sources, the corresponding data part will be removed from the golden record. This means that all properties originating from the data part are removed from the golden record, and the data part itself is deleted from the [history](/key-terms-and-features/golden-records/history) of the golden record. Since the records from the other sources remain intact, the golden record still exists. However, if you remove records from all sources that form a golden record, then the golden record will be deleted.

**What is the difference between removing records and deleting golden records using the GraphQL tool?**

Removing records from a specific data source is designed to remove the corresponding data parts from all relevant golden records. If these golden records contain other data parts, they will continue to exist. However, deleting a golden record using the [GraphQL tool](/consume/graphql/graphql-actions) will result in the complete deletion of the entire golden record.

**Prerequisites**

Go to **Administration** > **Feature Flags**, and then enable the **Remove Golden Records** feature.

![remove-golden-records-1.png](../../assets/images/integration/additional-operations/remove-golden-records-1.png)

**To remove records**

1. On the navigation pane, go to **Integrations** > **Data Sources**.

1. Find and open the data source that contains records that you want to remove.

1. Near the upper-right corner of the data source details page, select **Remove records**.

    The **Remove processed records** dialog opens where you can view the number of records that will be removed as well as the data set containing those records.

1. Confirm that you want to remove records by entering _REMOVE_. Then, select **Remove records**.

    ![remove-golden-records-2.gif](../../assets/images/integration/additional-operations/remove-golden-records-2.gif)

The process of removing records might take some time. During or after the process of removing records, you can make changes in the data set (edit mapping, add or remove property or pre-process rules) or process the data set again.