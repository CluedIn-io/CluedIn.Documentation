---
title: How to standardize dates
url: https://documentation.cluedin.net/govern/cleaning/how-to-standardize-dates
content_type: how-to
section: Govern & improve > Cleaning
---

# How to standardize dates

> how-to: Steps to accomplish one task.

In this article, you will learn how to standardize dates using two different methods: by applying data part rules and by configuring data type during mapping.

To begin with, we have ingested, mapped, and processed a file containing contact data. Note that the records include dates in various short date and long date patterns typical to the en-US culture. Next, we’ll demonstrate how to apply two standardization methods, both leading to the same result.

![Contact records whose joined_date column, highlighted, mixes short and long en-US date formats such as 04/04/2025 and November 4, 2024](https://documentation.cluedin.net/assets/images/kb/how-to/how-to-standardize-dates-input.png)

## Standardize dates using data part rules

1. To convert dates into ISO 8601 format (YYYY-MM-DDT00:00:00+00:00), [create](https://documentation.cluedin.net/govern/rules/create-rule.md) a data part rule and add an action to normalize dates. In the action, specify the culture of the input dates to help CluedIn interpret the values.

    Additionally, you can specify the input format for the same purpose.

    Both culture and input are optional parameters. If you don’t provide the culture or input format, CluedIn will analyze the values and determine their input date format before converting them to ISO 8601 format.

    ![Add action pane of a data part rule with the Normalize Date action, a Field Name selected, Culture set to en-US, and an empty Input Format](https://documentation.cluedin.net/assets/images/kb/how-to/how-to-standardize-dates-rule-action.png)

1. Save, activate and re-process the rule. To verify that the rule has been applied, go to the **Data** tab of the data set that initially contained non-standardized dates. As a result, all dates are standardized according to ISO 8601 format.

    ![Data tab with the Joined Date column, highlighted, showing all dates in ISO 8601 format such as 2024-09-23T00:00:00](https://documentation.cluedin.net/assets/images/kb/how-to/how-to-standardize-dates-output.png)

    This method is preferred for standardizing dates as it avoids changing the data type of the original field during mapping to the vocabulary key. Keeping the default data type (Text) helps reduce the likelihood of format validation errors during initial processing.

## Standardizing dates using mapping

1. Go to **Administration** > **Settings** > **Processing Property Data Type Normalization**.

1. Enable the **Date Time** setting. By default, this setting is disabled because date normalization using rules is the preferred method.

    ![Processing Property Data Type Normalization settings with the Date Time setting highlighted and enabled](https://documentation.cluedin.net/assets/images/kb/how-to/how-to-standardize-dates-org-settings.png)

1. When creating mapping for the data set, change the data type for the field containing dates to **DateTime**.

    ![Mapping Preview with the joined_date field highlighted, mapped to joinedDate with the DateTime data type](https://documentation.cluedin.net/assets/images/kb/how-to/how-to-standardize-dates-mapping-preview.png)

    After processing the data set, the dates will be converted to the ISO 8601 format.

    ![Data tab with the Joined Date column, highlighted, showing all dates in ISO 8601 format such as 2024-09-23T00:00:00](https://documentation.cluedin.net/assets/images/kb/how-to/how-to-standardize-dates-output.png)

Up: [Cleaning](https://documentation.cluedin.net/govern/cleaning.md)
