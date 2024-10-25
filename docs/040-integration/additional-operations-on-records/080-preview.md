---
layout: cluedin
nav_order: 8
parent: Additional operations
grand_parent: Integration
permalink: /integration/additional-operations-on-records/preview
title: Preview
last_modified: 2024-10-25
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about various actions available on the **Preview** tab of the data set to help you analyze and get a better understanding of the uploaded records.

## Profiling

Profiling provides a breakdown and distribution of all vocabulary key values in a graphic format. It can help you identify issues and anomalies in data quality. Profiling is not limited to a data set, meaning that it displays information about vocabulary key values coming from different data sources.

Profiling is a beta feature. To access profiling, go to **Administration** > **Feature Flags**, and enable the **Profiling dashboards** feature.

![preview-profiling-1.png](../../assets/images/integration/additional-operations/preview-profiling-1.png)

You can view profiling at any stage of the data ingestion process: immediately after uploading the data, after creating the mapping, or after processing the data. Profiling is type-specific, so if you change the data type during mapping and then process the data, the profiling dashboard may look different from when you first uploaded the data. For example, if you change the data type for the 'Revenue' column from text to integer, the profiling dashboard will display metrics such as minimum value, maximum value, and average value instead of a breakdown and distribution of text values.

**To view profiling**

- In the column header, open the menu, and select **View profiling**.

    ![preview-profiling-2.gif](../../assets/images/integration/additional-operations/preview-profiling-2.gif)

    For more information, see [Vocabulary keys](/management/data-catalog/vocabulary-keys).

## Data set filters and operations

Data set filters and operations allow you to view, search, analyze, and modify uploaded data. These actions are only available when you switch to the edit mode of the data set.

To access data set filters and operations, go to **Administration** > **Feature Flags**, and enable the **Data Set Filters & Operations** feature.

![preview-filters-and-operations-1.png](../../assets/images/integration/additional-operations/preview-filters-and-operations-1.png)

### Switch to edit mode

Switching to the edit mode allows you to use filters, modify the data set, and perform various operations. When you switch to the edit mode, the original data set is cloned, so you can revert back to it at any time. Reverting to the original data set means losing all changes made in the edit mode.

**To switch to the edit mode**

- Near the upper-right corner of the data set, open the three-dot menu, and then select **Switch to edit mode**. Then, confirm that you want to switch to the edit mode.

    ![Switch_to_edit_mode.png](../../assets/images/integration/additional-operations/Switch_to_edit_mode.png)

    Depending on the size of your data set, switching to the edit mode might take some time. You'll receive a notification when the data set has been switched to the edit mode.

If you decide to go back to the original data set, exit the edit mode. To do that, near the upper-right corner of the data set, open the three-dot menu, and then select **Switch to original**. Then, confirm that you want to switch to the original data set.

### Filter records

When the data set is in the edit mode, you can apply the following filters to any column:

- **Search** – select or enter a specific value to display all records containing that value.

- **Is empty** – display all records where the column contains empty values.

- **Is not empty** – display all records where the column does not contain empty values.

- **Aggregation** – consolidate and summarize all values contained in the column.

**To apply a filter**

- In the column header, open the three-dot menu, and then select **Filter**. Then, select the needed filtering option.

    ![apply-filter.gif](../../assets/images/integration/additional-operations/apply-filter.gif)

    All applied filters are displayed on the **Filters** pane. If you don't need a filter temporarily, you can disable it and enable it again when needed. If you no longer need a filter, you can delete it by selecting the delete icon.

### Perform operations

When the data set is in the edit mode, you can perform various transformations on the values in any column. For example, you can transform the values to upper case, remove extra spaces, replace one value with another, and more. The purpose of operations is to help you transform and improve the contents of columns automatically and efficiently.

The following table shows all available operations and their description.

| Operation | Description |
|--|--|
| Camel case | Transforms all values in the column to camel case (directorOfSales). |
| Capitalize | Changes the first letter of the first word to uppercase (Director of sales).  |
| Decapitalize | Changes the first letter of the first word to lowercase (director of sales). |
| Auto-generated value | Replaces values with automatically created unique values. |
| Kebab case | Transforms all values in the column to kebab case (director-of-sales). |
| Lower case | Transforms all values in the column to lowercase (director of sales). |
| Set value | Replaces all values in the column with the specified value. |
| Slugify | Converts a string into a lowercase, hyphen-separated version of the string, with all special characters removed.  |
| Swap case | Invert the case of each letter in a string. This means that all uppercase letters are converted to lowercase, and all lowercase letters are converted to uppercase. |
| Trim | Removes all leading and trailing whitespace from a string. |
| Trim Left | Removes only the leading whitespace from a string. |
| Trim Right | Removes only the trailing whitespace from a string. |
| Upper case | Converts all letters of each word to uppercase (DIRECTOR OF SALES). |
| Title case | Converts the first letter of each word to uppercase (Director Of Sales). |
| Keep only numbers | Extracts and retains only the numeric characters from a string, removing any non-numeric characters.  |
| To Boolean | Converts a value to a Boolean data type, which can be either true or false. |
| Replace | Replaces the first occurrence of a specified pattern within a string with another character or sequence of characters. |
| Replace all | Replaces all occurrences of a specified pattern within a string with another character or sequence of characters. |
| Replace spaces | Replaces spaces in a string with another character or sequence of characters. |
| Replace character(s) with space | Replaces specified characters with a space. |

**To perform an operation**

- In the column header, open the three-dot menu, and then select **Operations**. Then, select the needed operation.

    ![perform-operation.gif](../../assets/images/integration/additional-operations/perform-operation.gif)

    All applied operations are displayed on the **Operations** pane. If you no longer need the change or you made it by mistake, you can revert the change. To do it, select the **Undo the last operation** icon or the delete icon. Note that changes can only be reverted consecutively, one by one, and not selectively.

### Modify data manually

When the data set is in the edit mode, you can manually modify the data directly in the cells.

**To modify data manually**

1. Click on the value that you want to change and make the needed changes. The edited value will be displayed in bold.

1. Select **Save**. The bold formatting of the changed value disappears.

    ![modify-data-manually.gif](../../assets/images/integration/additional-operations/modify-data-manually.gif)

    The history of your manual changes is displayed on the **Operations** tab. If you no longer need the change or you made it by mistake, you can revert the change. To do it, select the **Undo the last operation** icon or the delete icon. Note that changes can only be reverted consecutively, one by one, and not selectively.

### Add columns

When the data set is in the edit mode, you can add new columns to the data set.

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

    ![add-column.gif](../../assets/images/integration/additional-operations/add-column.gif)

    The new column is added to the data set and is marked with the information icons. If you no longer need the column, you can delete it. To do it, in the column header, open the three-dot menu, select **Delete computed field**, and then confirm your choice.

## View duplicates

This feature allows you to check if the column contains duplicate values. Viewing duplicates in a column is available only after the mapping for the data set has been created. 

**To view duplicates**

1. Open the menu in the column heading, and then select **View duplicates**.

    ![preview-duplicates-1.gif](../../assets/images/integration/additional-operations/preview-duplicates-1.gif)

    You can view the total number of duplicate values in the column, identify which values are duplicates, and see how many times each duplicate value occurs.

## Clear content

This feature is available only for data sets created using an endpoint. It allows you to delete records from the **Preview** tab. This is useful when you send many requests to the same endpoint and want to avoid processing each record every time. When processing records, CluedIn checks if they have been processed before. If they have, they won't be processed again. To reduce processing time, you can remove already processed records from the **Preview** tab.

You can clear the content regardless of whether the records have been processed or not, but if you haven't processed the records, they will be permanently deleted.

**To clear the content**

1. Near the upper-right corner of the table, select the vertical ellipsis button, and then select **Clear content**.

1. Confirm that you want to delete the records by entering _DELETE_. Then, select **Confirm**.

    ![clear-content.gif](../../assets/images/integration/additional-operations/clear-content.gif)

     After records are deleted, you can send more data to the endpoint.