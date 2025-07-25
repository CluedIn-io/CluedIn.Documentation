---
layout: cluedin
nav_order: 4
parent: Clean
grand_parent: Preparation
permalink: preparation/clean/clean-application-reference
title: Clean application reference
tags: ["preparation", "clean"]
---

In this article, you will find reference information about common transformation functions in the clean application. The purpose of these functions is to help you edit and improve the contents of cells automatically and efficiently.

To access the common transformation functions, expand the menu in the column heading, and then select **Edit cells** > **Common transforms**.

![common-transform.png]({{ "/assets/images/preparation/clean/common-transform.png" | relative_url }})

The following table provides the description of common transformation functions.

| Function | Description |
|--|--|
| Trim leading and trailing whitespace | Removes extra spaces and line breaks before or after visible text characters. |
| Collapse consecutive whitespace | Removes tabs and multiple spaces in a row and replaces them with a single space. |
| Unescape HTML entities | Replaces HTML character references with Unicode characters. For example, `&nbsp;` will be replaced with a space. |
| Replace smart quotes with ASCII | Replaces curly quotation marks with straight double quote character ("). |
| To titlecase | Transforms text in the column into Title Case. |
| To uppercase | Transforms text in the column into UPPER CASE. |
| To lowercase | Transforms text in the column into lower case. |
| To number | Transforms the data in the cells and converts the data type to number. For example, "10" as a text string will be transformed to "10" as a number.  |
| To date | Transforms the data in the cells and converts the data type into the ISO-8601-compliant extended format with time in UTC: YYYY-MM-DDTHH:MM:SSZ. For example, 10/3/2023 will be converted to 2023-10-03T00:00:00Z. |
| To text | Transforms the data in the cells and converts the data type to text. |
| To null | Converts the data in the cells into null values. |
| To empty string | Converts the data in the cells into an empty string. |