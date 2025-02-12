---
layout: cluedin
title: How to tag records with data quality issues
parent: Knowledge base
permalink: /kb/how-to-tag-records-with-data-quality-issues
nav_order: 2
---

In this article, you will learn how to tag records with data quality issues using data part rules. We will use invalid email address as an example of a data quality issue.

To begin with, we have ingested, mapped, and processed a file containing contact data. Some records include invalid email addresses. Note that the email addresses in rows 1–3 violate common email address formatting rules.

![invalid-email.png](../../assets/images/kb/how-to/invalid-email.png)

To tag records with such data quality issues, [create](/management/rules/create-rule) a data part rule and add an action to tag records if the email value does not match the acceptable patten of a common regular expression (for example, `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$`). You can use the **Conditions** section of the action to specify the acceptable pattern for the vocabulary key value.

![validate-email-action.png](../../assets/images/kb/how-to/validate-email-action.png)

Next, save, activate and re-process the rule. To verify that the rule has been applied, go to search and use the **Tags** filter.

![tag-in-search.png](../../assets/images/kb/how-to/tag-in-search.png)

As a result, you will see all records where the email value is in the invalid format. Records with invalid email addresses contain the corresponding tag.

![tagged-records.png](../../assets/images/kb/how-to/tagged-records.png)

When the records with data quality issues are tagged, you can then [create](/preparation/clean/create-clean-project) a clean project to fix such issues. To do it, in the upper-right corner of the search results page, open the three-dot menu, and select **Clean**.

![create-clean-project.png](../../assets/images/kb/how-to/create-clean-project.png)