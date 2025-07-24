---
layout: cluedin
nav_order: 3
parent: Deduplication
grand_parent: Management
permalink: management/deduplication/create-a-deduplication-project
title: Create a deduplication project
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to create a deduplication project and configure matching rules for detecting duplicates. The approach described here ensures that you can easily revert merges when needed.

## Create a deduplication project

Before creating a deduplication project, take the following aspects into account:

- **Number of golden records** that you want to check for duplicates. For an extensive set of data with hundreds of thousands or millions of records, use advanced filters to narrow down the number of records in the project to test your configuration. When you are satisfied with the configuration, you can then modify the filters and run the project on the entire set of data.

    For example, if you want to deduplicate all golden records of the Company business domain, start by narrowing down the companies to a specific country. To do this, apply two filter rules: one to identify all golden records of the Company business domain, and another to find all golden records that match the specific country. This approach allows you to refine your matching rules on a targeted subset of data. When you are satisfied with the configuration, simply remove the filter rule for the specific country and run the project for all golden records of the Company business domain.

- **Matching functions** that you want to use for detecting duplicates. To ensure a faster deduplication process and make it easier to revert merges, create separate projects for equality matching functions and fuzzy matching functions. You can create multiple deduplication projects.

**To create a deduplication project**

1. On the navigation pane, go to **Management** > **Deduplication**.

1. Select **Create Deduplication Project**.

1. Enter the name of the deduplication project.

1. In the **Choose project type** section, select an option for identifying the golden records that you want to deduplicate:

    - **By business domain** – select the business domain; all golden records belonging to the selected business domain will be checked for duplicates. You can add multiple business domain. This is useful when you want to run a deduplication project across similar business domain.

    - **Using advanced filters** – add filter rules; all golden records that meet the filter criteria will be checked for duplicates. You can add multiple filter rules. Read more about filters [here](/key-terms-and-features/filters).

        This option is useful when you are working with a large set of data. You can narrow down the number of golden records and run a deduplication project on a sample set of data to make sure your matching rules work correctly. When you are confident in the effectiveness of your configuration with the sample set, you can then modify the filters and run the project on a larger set of data.

    ![create-dedup-project.png](../../assets/images/management/deduplication/create-dedup-project.png)

1. Select **Create**.

    After you create a deduplication project, add matching rules for detecting duplicates among golden records that correspond to the selected business domain or filter criteria.

## Add a matching rule

Deterministic and probabilistic matching rules play a crucial role in detecting duplicates. You can add multiple matching rules into a single deduplication project. However, the fewer rules you have in a project, the faster it runs and the easier it is to revert merges if necessary.

{:.important}
In the project, matching rules are combined using the **OR** logical operator, while matching criteria within a rule are combined using the **AND** logical operator.

**To add a matching rule**

1. On the **Matching Rules** tab, select **Add Matching Rule**.

1. Enter the name of the matching rule, and select **Next**.

1. On the **Matching Criteria** tab, do the following:

    1. Enter the name of the matching criteria.

    1. Select the property type—vocabulary key or property—that will be checked for duplicate values.

        {:.important}
        If the property or vocabulary key contains empty values, they will be ignored when generating the deduplication project results.

    1. Choose the [matching function](/management/deduplication/deduplication-reference#matching-functions) for detecting duplicates.

        ![add-matching-rule-criteria.png](../../assets/images/management/deduplication/add-matching-rule-criteria.png)

    1. (Optional) Select the [normalization rules](/management/deduplication/deduplication-reference#normalization-rules) to apply during duplicate detection. These rules are temporarily applied solely for the purpose of identifying duplicates. For example, selecting **To lower-case** means that the system will convert values to lower case before comparing them to identify duplicates.

    1. Select **Next**.

1. On the **Preview** tab, do one of the following:

    - If you want to add another matching criteria, select **Add Matching Criteria**, and then repeat step 3.

        Multiple matching criteria within one rule are combined using the **AND** logical operator. It means that a golden record is identified as a duplicate only if it meets all the matching criteria specified in the rule. However, if you want to add another matching criteria combined using the **OR** logical operator, then add another rule.

    - If you are satisfied with the matching rule configuration, select **Add Rule**.

    After you add matching rules, [generate matches](/management/deduplication/manage-a-deduplication-project#generate-matches) to detect duplicates among golden records that correspond to the selected business domain or filter criteria.