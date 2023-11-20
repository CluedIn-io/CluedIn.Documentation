---
layout: default
nav_order: 4
parent: Rules
grand_parent: Management
permalink: /management/rules/rules-reference
title: Rules reference
tags: ["management", "rules"]
last_modified: 2023-11-16
---
## On this page
{: .no_toc .text-delta }
1. TOC
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
| Change Entity Type | Changes the entity type of the record. You can select the existing entity type or create a new entity type. |
| Copy Value | Copies the value from one field (source field) to another (target field). |
| Delete Value | Deletes the value that you select. |
| Evaluate Regex | Finds values that match a regular expression and replaces them with the needed value. |
| Mask Value | Applies a mask to the value. You can use this action to hide sensitive data. |
| Move Value | Moves the value from one field (source field) to another (target field). |
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
| Latest Manual | The value from the record that was the last to be modified in CluedIn wins. |
| Latest Modified Date | The value from the record that was the last to be modified in the external system wins. |
| Most Frequent Value | The value that occurs most often in the records. |
| Most Properties | The value from the record that has the most properties wins. |
| Oldest Modified Date | The value from the record that was the first to be modified in the external system wins. |
| Provider Definition | The value from the record that has the specified provider definition wins. |

## Actions in golden record rules

The following table contains a list of actions that you can use within golden record rules.

| Action | Description |
|--|--|
| Add Alias | Adds an alias to the record. You need to specify the alias that you want to add. |
| Add Tag | Adds a tag to the record. You need to specify the tag that you want to add. |
| Add Value | Adds a value to the vocabulary key. You can select the existing value or create a new value. Use this action when the vocabulary key doesn't contain any value. |
| Add Value with CluedIn AI | Adds a value to the property or vocabulary key according to your prompt. For example, you can check if the email address in the record is a personal address or business address. |
| Change Entity Type | Changes the entity type of the record. You can select the existing entity type or create a new entity type. |
| Mask Value | Applies a mask to the value. You can use this action to hide sensitive data. |
| Remove Alias | Removes alias from the record. You need to specify the alias that you want to remove. |
| Remove All Tags | Removes all tags from the record. |
| Remove Tag | Removes a tag from the record. You need to specify the tag that you want to remove. |
