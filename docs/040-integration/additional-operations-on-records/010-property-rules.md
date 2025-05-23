---
layout: cluedin
nav_order: 1
parent: Additional operations
grand_parent: Ingestion
permalink: /integration/additional-operations-on-records/property-rules
title: Property rules
tags: ["integration", "property rules"]
last_modified: 2024-01-15
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Property rules help you improve the quality of mapped records ([clues](/key-terms-and-features/clue-reference)) by normalizing and transforming property values. The difference between property rules and [pre-process rules](/integration/additional-operations-on-records/preprocess-rules) is that property rules are applied only to property values of the record while pre-process rules are applied to the whole record. So, if you want to apply some changes to the property values, create a property rule.

Property rules are applied to the clues before pre-process rules and advanced mapping code.

![property-rules-diagram.png](../../assets/images/integration/additional-operations/property-rules-diagram.png)

You can [create property rules on you own](#create-property-rules-on-your-own) or [use the CluedIn AI recommendation engine](#create-property-rules-using-ai) to generate property rules.

**Prerequisites**

To access property rules, go to **Administration** > **Feature Flags** and make sure that the following features are enabled:

- **Mapping Property Rules**

- **Data Set Quarantine**

### Create property rules on your own

You can apply the rule to all values of the property or define specific values. The available actions for the rule depend on the type of the property and are divided into several categories:

- Basic – set a new value (for example, you can enter a new value or use the value from another property) or write [custom CEL expression](#custom-cel-expression-examples).

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

### Create property rules using AI

CluedIn AI recommendation engine helps you create property rules in a quick and efficient manner. The engine analyzes properties and runs data type checks to come up with suggested actions.

{:.important}
To use AI capabilities to create property rules, first complete all the steps described in [Azure Open AI Integration](/microsoft-integration/open-ai-integration).

**To create property rules using AI**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set.

1. Go to the **Map** tab, and then select **Edit mapping**.

1. On the **Map columns to vocabulary key** tab, select **Generate rules**.

1. In the pane that opens, expand each property to review suggested validations and actions.

    ![property-rules-2.png](../../assets/images/integration/additional-operations/property-rules-2.png)

1. In the lower-right corner, select **Create rules**.

    The rules are added next to the properties.

    ![property-rules-3.png](../../assets/images/integration/additional-operations/property-rules-3.png)

    By selecting these rules, you can view, create, or remove rules from the property. The rules will be applied when you process the records.

## Custom CEL expression examples

This section contains some examples of CEL expressions in property rules.

**Remove the first occurrence of characters**

The following CEL expression removes the first occurrences of the characters `#` and `$` from property values. You can use this expression if you have a property (for example, postal code) that contains values with one occurrence of `#` and `$`.

```
("" + value).replace("#", "").replace("$", "")
```

On the screenshot, rows 1 and 3 contain several occurrences of `#` and `$`. The property rule removed only the first occurrences of those characters. To remove all occurrences of specific characters, use the expression from the next section.

![removing-first-occurrence.png](../../assets/images/integration/additional-operations/removing-first-occurrence.png)

**Remove all occurrences of characters**

The following CEL expression removes all occurrences of the characters `#` and `$` from property values. You can use this expression if you have a property (for example, postal code) that contains values with multiples occurrences of `#` and `$`.

```
("" + value).replace(/[#\$]/g, "")
```

![removing-all-occurrences.png](../../assets/images/integration/additional-operations/removing-all-occurrences.png)

**Turn non-numeric values to blank or null**

The following CEL expressions turn the value to blank or null if the value is not a number. You can use any of these expressions if you have a property (for example, revenue) that should contain only numbers, and you want to remove any non-numeric values.

```
(+value == value) ? value : ""
```
  
```
(+value == value) ? value : null
``` 

If the property contains non-numeric values, applying any of the above expressions will result in golden records without such property. Regardless of the expression you use, the result will be the same.

![property_rule_turn_non-numeric_values_to_blank.png](../../assets/images/integration/additional-operations/property_rule_turn_non-numeric_values_to_blank.png)