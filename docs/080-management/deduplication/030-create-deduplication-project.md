---
layout: cluedin
nav_order: 3
parent: Deduplication
grand_parent: Management
permalink: /management/deduplication/create-a-deduplication-project
title: Create a deduplication project
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to create a deduplication project in an efficient manner, providing you with the capability to easily revert merges when needed.

## Create a deduplication project

Before creating a deduplication project, take the following aspects into account:

- **Number of golden records** that you want to check for duplicates. For an extensive set of data with hundreds of thousands or millions of records, limit the number of records in the project to test your configuration. When you are satisfied with the configuration, you can then remove the limit and run the project on the entire set of data.

- **Matching functions** that you want to use for detecting duplicates. To ensure a faster deduplication process and facilitate easy reversion of changes, create separate projects for equality matching functions and fuzzy matching functions. You can create multiple deduplication projects.

**To create a deduplication project**

1. On the navigation pane, go to **Management** > **Deduplication**.

1. Select **Create Deduplication Project**.

1. Enter the name of the deduplication project.

1. Find and select the entity type to restrict the golden records for the deduplication project. Only records that belong to the selected entity type will be checked for duplicates.

    You can add multiple entity types. This is useful when you want to run a deduplication project across similar entity types.

1. (Optional) To limit the number of golden records that will be checked for duplicates, select the corresponding checkbox and enter the number.

    This is useful when you are working with a large set of data. Run a deduplication project on a sample set of data to make sure your matching rules work correctly. When you are confident in the effectiveness of your configuration with the sample set, you can then remove the limit and run the project on a larger set of data.

1. (Optional) In the **Description** section, enter the details about the deduplication project.

1. In the upper-right corner, select **Create**.

    ![сreate-project.gif](../../assets/images/management/deduplication/сreate-project.gif)

    After you create a deduplication project, add matching rules to check for duplicates in golden records within the selected entity type.

## Add a matching rule

Deterministic and probabilistic matching rules play a crucial role in detecting duplicates. You can add multiple matching rules into a single deduplication project. However, the fewer rules you have in a project, the faster it runs and the easier it is to revert changes if necessary.

{:.important}
In the project, matching rules are combined using the **OR** logical operator, while matching criteria within a rule are combined using the **AND** logical operator.

**To add a matching rule**

1. On the **Matching Rules** tab and select **Add Matching Rule**.

1. Enter the name of the matching rule, and select **Next**.

1. On the **Matching Criteria** tab, do the following:

    1. Enter the name of the matching criteria.

    1. Select the property type—vocabulary key or property—that will be checked for duplicate values.

        {:.important}
        If the property or vocabulary key contains empty values, they will be ignored when generating the deduplication project results.

    1. Choose the [matching function](/management/deduplication/deduplication-reference#matching-functions) for detecting duplicates.

    1. (Optional) Select the normalization rules to apply during duplicate detection. These rules are temporarily applied solely for the purpose of identifying duplicates. For example, selecting **To lower-case** means that the system will convert values to lower case before comparing them to identify duplicates.

    1. Select **Next**.

1. On the **Preview** tab, do one of the following:

    - If you want to add another matching criteria, select **Add Matching Criteria**, and then repeat step 3.

        Multiple matching criteria within one rule are combined using the **AND** logical operator. It means that all matching criteria in the rule must be true for a record to be identified as a duplicate. However, if you want to add another matching criteria combined using the **OR** logical operator, then add another rule.

    - If you are satisfied with the matching rule configuration, select **Add Rule**.

        ![add-rule.gif](../../assets/images/management/deduplication/add-rule.gif)

    After you add matching rules, [generate results](/management/deduplication/manage-a-deduplication-project#generate-results) of the project to see if CluedIn finds any duplicates.