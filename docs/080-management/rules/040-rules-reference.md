---
layout: cluedin
nav_order: 4
parent: Rules
grand_parent: Management
permalink: /management/rules/rules-reference
title: Rules reference
tags: ["management", "rules"]
last_modified: 2026-09-23
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will find reference information to help you understand the actions associated with each type of rule.

## Actions in data part rules

The following table contains a list of actions that you can use within data part rules.

| Action | Description |
|--|--|
| Add Alias | Adds an alias to the record. You need to specify the alias that you want to add. |
| Add Tag | Adds a tag to the record. You need to specify the tag that you want to add. |
| Add Value | Adds a value to the vocabulary key. You can select the existing value or create a new value. Use this action when the vocabulary key doesn't contain any value. |
| Add Value with CluedIn AI | Adds a value to the property or vocabulary key according to your prompt. For example, you can check if the email address in the record is a personal address or business address. |
| Change Business Domain | Changes the business domain of the record. You can select the existing business domain or create a new business domain. |
| Copy Value | Copies the value from one field (source field) to another (target field). |
| Delete Value | Deletes the value that you select. |
| Evaluate Regex | Finds values that match a regular expression and replaces them with the needed value. |
| Formula Action (Power Fx) | Runs a Power Fx expression in the rule to compute values, evaluate conditions, or call CluedIn custom functions (for example, AddTag, GetVocabularyKeyValue, SetEntityProperty, SetVocabularyKeyValue). Use this to set vocabulary keys, transform strings, perform type conversions, and make decisions. |
| Mask Value | Applies a mask to the value. You can use this action to hide sensitive data. Note that this action will be deprecated in future releases; therefore, use the [mask action](/management/access-control/access-control-reference#) in access control policy rules instead. |
| Move Value | Moves the value from one field (source field) to another (target field). |
| Normalize Date | Converts the values of the vocabulary key to ISO 8601 format (YYYY-MM-DDT00:00:00+00:00). You can enter the culture or input format to tell CluedIn that you expect dates for the specified vocabulary key to be in a certain way. If you don't enter the culture or input format, CluedIn will analyze the values and determine their date format on its own before converting them to ISO 8601 format. This action gives you more control over how dates are interpreted before they are converted to ISO 8601 format.<br> **Important!** To use this action, the **Date Time** option must be disabled in **Administration** > **Settings** > **Processing Property Data Type Normalization**. For dates that have already been converted when the **Date Time** option was enabled, the Normalize Date rule action has no effect at all because the dates are already normalized. |
| Remove Alias | Removes alias from the record. You need to specify the alias that you want to remove. |
| Remove All Tags | Removes all tags from the record. |
| Remove line breaks | Removes line breaks from the value. By default, line breaks are replaced with spaces, but you can specify other replacement options. |
| Remove Tag | Removes a tag from the record. You need to specify the tag that you want to remove.|
| Replace | Replaces one value with another. You need to provide both the value you want to replace and its corresponding replacement value. |
| Set Value | Changes the value of the vocabulary key. You can select the existing value or create a new value. Use this action when the vocabulary key contains a value and you want to change this value to another one. |
| Set Value with CluedIn AI | Changes the value of the property or vocabulary key according to your prompt. |
| To CamelCase | Changes the value to camel case and removes all spaces. |
| To LowerCase | Changes the value to lower case. |
| To TitleCase | Changes the value to title case. |
| To UpperCase | Changes the value to upper case. |
| Trim WhiteSpace | Removes white space from the value. |
| Unmask Value | Removes the mask from the value. |

## Actions in survivorship rules

The following table contains a list of actions that you can use within survivorship rules.

| Action | Description |
|--|--|
| Best Quality | The value from the source with the highest quality wins. |
| Latest Manual | The value from the record that was the last to be modified in CluedIn wins. |
| Latest Matching Condition | The value from the most recently modified data part that matches the condition you define wins. The condition can use Power Fx, which allows you to express more complex survivorship logic based on the values and properties on each data part. |
| Latest Modified Date | The value from the record that was the last to be modified in the external system wins. |
| Maximum Value | The highest value found across the matching data parts wins. This is useful for numeric, date, or other comparable values where the greatest value should survive. |
| Minimum Value | The lowest value found across the matching data parts wins. This is useful when the smallest numeric, date, or other comparable value should survive. |
| Most Frequent Value | The value that occurs most often in the records. |
| Most Properties | The value from the record that has the most properties wins. |
| Oldest Modified Date | The value from the record that was the first to be modified in the external system wins. |
| Provider Definition | The value from the record that has the specified provider definition wins. |


### Use Latest Matching Condition for advanced survivorship logic

Use **Latest Matching Condition** when recency alone is not enough to decide which data part should provide the winning value.

With this action, CluedIn evaluates a condition against the candidate data parts. From the data parts that satisfy the condition, the most recently modified matching data part is selected.

The condition can be written using [Power Fx](/management/rules/power-fx-formulas), which makes it possible to base survivorship on business logic rather than only on source priority or timestamps.

For example, suppose a customer golden record contains data parts from several systems, but you only want the value to survive from a data part where the `customer.status` vocabulary key is set to `Active`.

You can use a Power Fx condition such as:

```powerfx
GetVocabularyKeyValue(Entity, "customer.status") = "Active"
```

CluedIn evaluates the formula against each candidate data part. Only data parts where `customer.status` is `Active` are considered, and the latest matching data part supplies the winning value.

You can also combine multiple checks. For example, prefer the latest data part where the customer is active and the source has marked the record as verified:

```powerfx
GetVocabularyKeyValue(Entity, "customer.status") = "Active" &&
GetVocabularyKeyValue(Entity, "customer.verified") = true
```

Another example is to select from data parts belonging to a particular business process or source classification:

```powerfx
GetVocabularyKeyValue(Entity, "customer.sourceTier") = "Authoritative"
```

This pattern is useful for survivorship requirements such as:

- Use the latest value only from data parts that have passed a validation check.
- Prefer the latest data part with a particular status, classification, or approval flag.
- Select values only from data parts where a required vocabulary key is populated with a specific value.
- Combine several conditions to model more complex source-governance rules.

Because Power Fx conditions are evaluated against the data part being considered for survivorship, `Entity` represents that candidate data part within the condition.

{:.important}
If no candidate data part matches the condition, the **Latest Matching Condition** action cannot select a matching data part. Design the rule conditions so that the expected records can satisfy the expression, or use additional survivorship rules to provide an appropriate fallback.

## Actions in golden record rules

The following table contains a list of actions that you can use within golden record rules.

| Action | Description |
|--|--|
| Add Alias | Adds an alias to the record. You need to specify the alias that you want to add. |
| Add Tag | Adds a tag to the record. You need to specify the tag that you want to add. |
| Add Value | Adds a value to the vocabulary key. You can select the existing value or create a new value. Use this action when the vocabulary key doesn't contain any value. |
| Add Value with CluedIn AI | Adds a value to the property or vocabulary key according to your prompt. For example, you can check if the email address in the record is a personal address or business address. |
| Change Business Domain | Changes the business domain of the record. You can select the existing business domain or create a new business domain. |
| Mask Value | Applies a mask to the value. You can use this action to hide sensitive data. Note that this action will be deprecated in future releases; therefore, use the [mask action](/management/access-control/access-control-reference#) in access control policy rules instead. |
| Normalize Date | Converts the values of the vocabulary key to ISO 8601 format (YYYY-MM-DDT00:00:00+00:00). You can enter the culture or input format to tell CluedIn that you expect dates for the specified vocabulary key to be in a certain way. If you don't enter the culture or input format, CluedIn will analyze the values and determine their date format on its own before converting them to ISO 8601 format. This action gives you more control over how dates are interpreted before they are converted to ISO 8601 format.<br> **Important!** To use this action, the **Date Time** option must be disabled in **Administration** > **Settings** > **Processing Property Data Type Normalization**. For dates that have already been converted when the **Date Time** option was enabled, the Normalize Date rule action has no effect at all because the dates are already normalized. |
| Remove Alias | Removes alias from the record. You need to specify the alias that you want to remove. |
| Remove All Tags | Removes all tags from the record. |
| Remove Tag | Removes a tag from the record. You need to specify the tag that you want to remove. |
