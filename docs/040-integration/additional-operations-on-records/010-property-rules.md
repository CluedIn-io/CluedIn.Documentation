---
layout: default
nav_order: 1
parent: Additional operations on records
grand_parent: Integrations
permalink: /integration/additional-operations-on-records/property-rules
title: Property rules
tags: ["integration", "property rules"]
last_modified: 2023-11-07
---

Property rules help you improve the quality of mapped records by normalizing and transforming property values. The difference between property rules and [pre-process rules](/integration/additional-operations-on-records/preprocess-rules) is that property rules are applied only to property values of the record while pre-process rules are applied to the whole record. So, if you want to apply some changes to the property values, create a property rule.

Property rules are applied to the records during processing.

**Prerequisites**

To access property rules, go to **Administration** > **Feature Flags** and make sure that the following features are enabled:

- **Mapping Property Rules**

- **Data Set Quarantine**

You can apply the rule to all values of the property or define specific values. The available actions for the rule depend on the type of the property and are divided into several categories:

- Basic – set a new value (for example, you can enter a new value or use the value from another property).

- Normalization – transform data into a consistent form.

- Quarantine – send records to the [quarantine](/integration/additional-operations-on-records/quarantine) where you can modify them and decide what to do with them afterwards.

You can add multiple rules for one property.

**To create a property rule**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set.

1. Go to the **Map** tab, and then select **Edit mapping**.

1. On the **Map columns to vocabulary key** tab, find the property for which you need to create a rule, and then select **Add property rule**.

1. In **Filter**, select whether you want to apply the rule to all values or to specific values.

1. If you want to apply the rule to specific values:

    1. Select a condition to determine which values will be affected by the rule.

    1. Select whether you want to apply the rule when the condition is met or when the condition is not met.

        For example, if you want to detect all invalid email addresses, select **Is valid email address**, and then select **Apply action when condition is not met**.

1. Select the **Action** that will be applied to the values of the property.

    ![property-rules-1.png](../../assets/images/integration/additional-operations/property-rules-1.png)

1. In the lower-right corner, select **Add rule**.

     The rule is added next to the property. The rule will be applied when you process the records.