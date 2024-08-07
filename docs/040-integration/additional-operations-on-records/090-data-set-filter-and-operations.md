---
layout: cluedin
nav_order: 9
parent: Additional operations
grand_parent: Integration
permalink: /integration/additional-operations-on-records/data-set-filters-and-operations
title: Data set filters and operations
published: false
last_modified: 2024-05-21
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Data set filters and operations allow you to view, search, and analyze uploaded data based on various criteria. Additionally, you can switch to edit mode to manually change values and add columns.

Data set filters and operations are an alpha feature. To access data set filters and operations, go to **Administration** > **Feature Flags**, and enable the **Data Set Filters & Operations** feature.

![preview-filters-and-operations-1.png](../../assets/images/integration/additional-operations/preview-filters-and-operations-1.png)

## Filter records

You can apply the following filters to any column:

- Search – select a specific value in the column to display all records containing the selected value.

- Is empty – display all records where the column contains empty values.

- Is not empty – display all records where the column does not contain empty values.

- Aggregation – consolidate and summarize all values contained in the column.

**To apply a filter**

- In the column header, open the menu, select **Filter**, and then select the needed option.

    ![preview-filters-and-operations-2.gif](../../assets/images/integration/additional-operations/preview-filters-and-operations-2.gif)

    All applied filters are displayed in the **Filters** tab. If you don't need a filter temporarily, you can disable it and enable it again when needed. If you no longer need a filter, you can delete it by selecting the delete icon.

## Sort records

You can sort the records by the following criteria:

- Sort by oldest – arrange the records in ascending order based on the time they were created, displaying the oldest records first.

- Soft by new – arrange the records in descending order based on the time they were created, displaying the most recent records first.

## Switch to edit mode

In the  edit mode, you can make changes to the values directly in the cells and add columns to the data set.

{:.important}
Exiting the edit mode reverts all changes made to the data set in the edit mode and returns the data set to its original state.

**To switch to the edit mode**

- Next to the sorting dropdown, open the menu, and select **Switch to edit mode**. Then, confirm that you want to switch to the edit mode.

**To make manual changes**

1. Click on the value that you want to change and make the needed changes. The edited value will be displayed in bold.

1. Select **Save**. The bold formatting of the changed value disappears.

    ![preview-edit-mode-1.gif](../../assets/images/integration/additional-operations/preview-edit-mode-1.gif)

    The history of your manual changes is displayed in the **Operations** tab. If you no longer need the change or you made it by mistake, you can revert the change. To do it, select the **Undo the last operation** icon or the delete icon. Note that changes can only be reverted consecutively, one by one, and not selectively.

**To add a column to the data set**

1. Select **Add column**.

1. Enter the column name.

1. Select the column type:

    - Stored column – generate the values for the column: empty values that can modified later, values based on other existing fields in the data set, or values based on the low-code approach expression.

    - Computed column – combine the values from two already existing columns into one new column.

1. Select **Next**.

1. Choose an option for generating the values for the column fields:

    - (Stored column) Empty – a new column with empty fields will be added to the data set.

    - (Stored column or computed column) From existing fields – select the fields from the data set that you want to combine to create values for a new column. You can add multiple fields. By default, the values are separated with a space, but you can enter another delimiter if needed.

    - (Stored column or computed column) Expression – enter a C.E.L supported expression to create values for a new column.

1. Select **Save**.

    ![preview-edit-mode-2.gif](../../assets/images/integration/additional-operations/preview-edit-mode-2.gif)

**To exit the edit mode**

- Next to the sorting dropdown, open the menu, and select **Switch to original**. Then, confirm that you want to switch back to the original mode.

    All changes made in the edit mode will be lost.