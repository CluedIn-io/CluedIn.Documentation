---
title: How to tag records with data quality issues
url: https://documentation.cluedin.net/govern/tags/how-to-tag-records-with-data-quality-issues
content_type: how-to
section: Govern & improve > Tags
---

# How to tag records with data quality issues

> how-to: Steps to accomplish one task.

In this article, you will learn how to tag records with data quality issues using golden record rules and CluedIn Copilot. We will use invalid email address as an example of a data quality issue.

**To tag records with data quality issues**

1. To begin with, we have ingested, mapped, and processed a file containing contact data. Some records include invalid email addresses. Note that the email addresses in rows 1–3 violate common email address formatting rules.

    ![Ingested contact data where the email values in rows 1 to 3 are highlighted because they are not valid email addresses](https://documentation.cluedin.net/assets/images/kb/how-to/invalid-email.png)

1. To tag records with such data quality issues, [create](https://documentation.cluedin.net/govern/rules/create-rule.md) a data part rule and add an action to tag records if the email value does not match the acceptable patten of a common regular expression (for example, `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$`). You can use the **Conditions** section of the action to specify the acceptable pattern for the vocabulary key value.

    ![Add action dialog: condition trainingcontact.email Does not match pattern with an email regular expression, and action Add Tag with value Invalid email format](https://documentation.cluedin.net/assets/images/kb/how-to/validate-email-action.png)

    Alternatively, you can use [CluedIn Copilot](https://documentation.cluedin.net/solutions/copilot.md) to create a data part rule. First, ask Copilot to generate a common regular expression that would check for valid email format. For example, you can use the following prompt.

    ```
    Write a common regular expression that would check for valid email format and shortly describe it.
    ```

    Then, instruct Copilot to create a data part rule using the prompt similar to the following.

    ```
    Create a golden record rule named "User email format validation" for the TrainingContact entity type. This rule should use CluedIn AI action on the trainingcontact.email vocabulary key to tag with "Invalid email format" any email with a pattern that doesn't match the above regex.
    ```

    ![Copilot chat creating the golden record rule User email format validation that tags TrainingContact records with Invalid email format](https://documentation.cluedin.net/assets/images/kb/how-to/validate-email-copilot.png)

1. Next, activate and re-process the rule. To verify that the rule has been applied, go to search and use the **Tags** filter.

    ![Tags filter in search with Invalid email format selected, matching 3 records](https://documentation.cluedin.net/assets/images/kb/how-to/tag-in-search.png)

    As a result, you will see all records where the email value is in the invalid format. Records with invalid email addresses contain the corresponding tag.

    ![Search results showing Results found: 3, the TrainingContact records Sutton, Leeland and Adela](https://documentation.cluedin.net/assets/images/kb/how-to/tagged-records.png)

1. When the records with data quality issues are tagged, you can then [create](https://documentation.cluedin.net/govern/cleaning/create-clean-project.md) a clean project to fix such issues. To do it, in the upper-right corner of the search results page, open the three-dot menu, and select **Clean**.

    ![Search results toolbar with the Clean button highlighted, above the three tagged records](https://documentation.cluedin.net/assets/images/kb/how-to/create-clean-project.png)

Up: [Tags](https://documentation.cluedin.net/govern/tags.md)
