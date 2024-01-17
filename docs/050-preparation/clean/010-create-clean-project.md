---
layout: default
nav_order: 1
parent: Clean
grand_parent: Preparation
permalink: /preparation/clean/create-clean-project
title: Create a clean project
tags: ["preparation", "clean"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

A clean project is where you specify the data to be cleaned, retrieve it from CluedIn, perform the cleaning process, and then send the cleaned values back to golden records.

You can create a clean project from several places in CluedIn. This article will guide you through the different methods for creating a clean project, helping you select the most convenient one to suit your needs.

There are three ways to create a clean project:

- [From the search results page](#from-the-search-results-page) – this is the most convenient option as you can define filters once and then reuse them to run the clean projects.

- [From the Preparation module](#from-the-preparation-module) – this is a bit laborious option as you have to define filters every time you need to run the clean project.

- [From the glossary term](#from-the-glossary-term) – this is another convenient option as you can rely on previously defined filters that include the records that need to be cleaned.

## From the search results page

If you want to regularly clean your data, we recommend setting up and saving search filters for quick retrieval of the needed data. The main benefit of creating a clean project from the saved search is that you define the vocabulary keys that need to be cleaned just once, and then you can reuse this filter definition multiple times.

**To create a clean project from the search results page**

1. In the search field, select the search icon. Depending on whether you have the saved search that retrieves the data you need to clean, do one of the following:

    - If you have the saved search, in the upper-right corner of the page, select the vertical ellipsis button, and then select **Saved Searches**. Find and open the needed saved search.

        ![clean-project-1.png](../../assets/images/preparation/clean/clean-project-1.png)

        Make sure that the vocabulary keys to be cleaned are displayed on the search results page. This way, you don't have to specify the vocabulary keys in the clean project configuration. To learn how to add vocabulary keys to the search results page, see [Add columns](/key-terms-and-features/search#add-columns).

    - If you don't have the saved search, define the data that you want to clean using [filters](/key-terms-and-features/filters). Then, add the vocabulary keys to be cleaned to the search results page following the [Add columns](/key-terms-and-features/search#add-columns) procedure. If you need to clean the same set of data in future, save the current filter configuration.

1. In the upper-right corner of the page, select the vertical ellipsis button, and then select **Clean**.

    The **Create Clean Project** pane opens for you to configure the clean project. Note that the **Filters** section is already filled in with the information from the search filter definition.

1. Enter the name of the clean project. Then, in the lower-right corner, select **Next**.

    ![clean-project-2.png](../../assets/images/preparation/clean/clean-project-2.png)

1. Review the properties that will be loaded to the clean project. These properties are taken from the column options of your search results page.

    ![clean-project-3.png](../../assets/images/preparation/clean/clean-project-3.png)

    If you do not want to load some properties to the clean project, choose the needed properties, and then select **Remove Property**.

1. In the lower-right corner, select **Create**.

    You created the clean project from the search results page. The next step is to [generate results](/preparation/clean/manage-clean-project#generate-results) of the clean project.

## From the Preparation module

Creating a clean project from the Preparation module requires more effort than using other options. The reason for this is that you need to set filters each time you want to clean data.

**To create a clean project from the Preparation module**

1. On the navigation pane, go to **Preparation** > **Clean**.

1. Select **Create Clean Project**. The **Create Clean Project** pane opens for you to configure the clean project.

1. On the **Configure** tab, do the following:

    1. Enter the name of the clean project.

    1. In the **Filters** section, define what type of data you want to load to the clean project. Then, in the lower-right corner, select **Next**.

        ![clean-project-4.png](../../assets/images/preparation/clean/clean-project-4.png)

1. On the **Choose Vocabulary Keys** tab, do the following:

    1. Select **Add Property**, and then choose what type of property—record property or vocabulary property—you want to load to the clean project.

    1. Depending on the type of property that you chose, select the record properties or find and select the vocabulary keys that you want to load to the clean project.

        ![clean-project-5.png](../../assets/images/preparation/clean/clean-project-5.png)

    1. In the lower-right corner, select **Save Selection**.

1. In the lower-right corner, select **Create**.

    You created the clean project from the Preparation module. The next step is to [generate results](/preparation/clean/manage-clean-project#generate-results) of the clean project.

## From the glossary term

You can create a glossary term to collect a group of records that meet certain criteria, and then clean such records. Creating a clean project from the glossary term is quick and convenient because you don't have to define filters in the clean project configuration.

**To create a clean project from the glossary term**

1. On the navigation pane, go to **Management** > **Glossary**.

1. Find and open the needed glossary term. Then, select **Create Clean Project**.

    The **Create Clean Project** pane opens for you to configure the clean project.

1. On the **Configure** tab, do the following:

    1. Enter the name of the clean project.

    1. In the **Filters** section, choose the operation for defining what to do with the records belonging to the glossary term. Choosing **Is True** will load all records belonging to the term, and choosing **Is Not True** will load all records that do not belong to the glossary term. Then, in the lower-right corner, select **Next**.

        ![clean-project-6.png](../../assets/images/preparation/clean/clean-project-6.png)

1. On the **Choose Vocabulary Keys** tab, do the following:
    
    1. Select **Add Property**, and then choose what type of property—record property or vocabulary property—you want to load to the clean project.

    1. Depending on the type of property that you chose, select the record properties or find and select the vocabulary keys that you want to load to the clean project.

        ![clean-project-5.png](../../assets/images/preparation/clean/clean-project-5.png)

    1. In the lower-right corner, select **Save Selection**.

1. In the lower-right corner, select **Create**.

    You created the clean project from the glossary. The next step is to [generate results](/preparation/clean/manage-clean-project#generate-results) of the clean project.