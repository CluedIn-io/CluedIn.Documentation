---
layout: cluedin
title: How to standardize dates
parent: Knowledge base
permalink: kb/how-to-standardize-dates
nav_order: 3
---

In this article, you will learn how to standardize dates using two different methods: by applying data part rules and by configuring data type during mapping.

To begin with, we have ingested, mapped, and processed a file containing contact data. Note that the records include dates in various short date and long date patterns typical to the en-US culture. Next, we’ll demonstrate how to apply two standardization methods, both leading to the same result.

![how-to-standardize-dates-input.png]({{ "/assets/images/kb/how-to/how-to-standardize-dates-input.png" | relative_url }})| relative_url }})

**Standardizing dates using data part rules**

To convert dates into ISO 8601 format (YYYY-MM-DDT00:00:00+00:00), [create](/management/rules/create-rule) a data part rule and add an action to normalize dates. In the action, specify the culture of the input dates to help CluedIn interpret the values. Additionally, you can specify the input format for the same purpose. Both culture and input are optional parameters. If you don’t provide the culture or input format, CluedIn will analyze the values and determine their input date format before converting them to ISO 8601 format.

![how-to-standardize-dates-rule-action.png]({{ "/assets/images/kb/how-to/how-to-standardize-dates-rule-action.png" | relative_url }})| relative_url }})

Next, save, activate and re-process the rule. To verify that the rule has been applied, go to the **Data** tab of the data set that initially contained non-standardized dates. As a result, all dates are standardized according to ISO 8601 format.

![how-to-standardize-dates-output.png]({{ "/assets/images/kb/how-to/how-to-standardize-dates-output.png" | relative_url }})| relative_url }})

This method is preferred for standardizing dates as it avoids changing the data type of the original field during mapping to the vocabulary key. Keeping the default data type (Text) helps reduce the likelihood of format validation errors during initial processing.

**Standardizing dates using mapping**

This method requires enabling the **Date Time** setting in **Administration** > **Settings** > **Processing Property Data Type Normalization**. By default, this setting is disabled because date normalization using rules is the preferred method.

![how-to-standardize-dates-org-settings.png]({{ "/assets/images/kb/how-to/how-to-standardize-dates-org-settings.png" | relative_url }})| relative_url }})

When creating mapping for the data set, change the data type for the field containing dates to **DateTime**.

![how-to-standardize-dates-mapping-preview.png]({{ "/assets/images/kb/how-to/how-to-standardize-dates-mapping-preview.png" | relative_url }})| relative_url }})

After processing the data set, the dates will be converted to the ISO 8601 format.

![how-to-standardize-dates-output.png]({{ "/assets/images/kb/how-to/how-to-standardize-dates-output.png" | relative_url }})| relative_url }})