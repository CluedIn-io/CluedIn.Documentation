---
layout: cluedin
nav_order: 2
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

## Deduplication guidelines

To enhance the efficiency of your deduplication project and to be able to smoothly revert merges, we recommend that you follow these guidelines.

![dedup-checklist.gif](../../assets/images/management/deduplication/dedup-checklist.gif)

When you need to run a deduplication project on a large set of data, we recommend that you **start small** and limit the size of data. This approach allows you to to verify the accuracy and efficiency of your matching rules before applying them to the entire data set. If the deduplication result doesn't meet your expectations, you can easily and quickly revert changes and start again.

When it comes to matching rules, our recommendation is to create **separate projects for strict and fuzzy matching functions, grouped by domain**. There are two reasons for this recommendation:

- Quick and efficient merging and unmerging. If all rules are consolidated within a single project and you decide to revert changes, all rules will be reverted, even those that were executed correctly. To prevent this, create separate projects for individual sets of rules. This way, you can selectively revert only those projects where rules didn't work as intended.

- Streamlined management of projects on a day-to-day basis. If you have projects targeting a specific domain, and the data for that domain has been updated, then you can easily re-evaluate those specific projects. For example, suppose you have one project that merges duplicates based on first and last names and another project that merges duplicates based on addresses. Now, you add the libpostal library to enrich addresses. In this scenario, you can easily re-evaluate only the address-based project, knowing that first and last names have remained unchanged.

To increase the efficiency of your deduplication projects, start by running projects with **strict equality matching functions** to eliminate obvious duplicates.

Once you've reached a state with no duplicates based on equality matching, proceed to execute projects with **fuzzy matching functions** for a more nuanced deduplication process. Since you've already merged some records based on equality matching functions, this means that you now have fewer duplicates in the system, so fuzzy matching would run much faster.

Finally, when you achieve the desired outcome on a small data set, **grow big** and proceed to run the deduplication project on the entire data set.

To demonstrate the practical application of these guidelines, let's delve into a real-life scenario with the following **example**. Suppose you have 1 million records that need to be checked for duplicates. Due to merging by codes, the number is reduced to 600 thousand records. Then, you can subsequently run the following deduplication projects:

- One project that addresses strict duplicates, resulting in 400 thousand merged records.

- Another project that deals with approximate duplicates using fuzzy matching. This time, the project needs to analyze only 400 thousand records, saving you the time and resources of not having to run fuzzy matching on the entire data set of 1 million records.

For additional examples showcasing the application of deduplication guidelines, see [Deduplication in practice](/management/deduplication/deduplication-in-practice).

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

        ![add-rule.gif](../../assets/images/management/deduplication/сreate-project.gif)

    After you add matching rules, [generate results](/management/deduplication/manage-a-deduplication-project#generate-results) of the project to see if CluedIn finds any duplicates.