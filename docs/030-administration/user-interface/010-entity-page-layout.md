---
layout: cluedin
title: Golden record page layout
parent: Administration
permalink: /administration/entity-page-layout
nav_order: 070
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

A golden record page layout is the way in which information about a golden record is arranged on the golden record overview page. In this article, you will learn about the types of layouts and how they are applied to golden records.

## Overview of golden record page layouts

The golden record page layout is assigned to the business domain. This ensures that all golden records belonging to that business domain consistently display relevant information on the golden record overview page.

All layouts are stored in **Administration** > **Golden record layouts**. CluedIn contains several built-in golden record page layouts:

- Default layout

- Discussion layout

- Document layout

- Organization layout

- Person layout

You cannot edit built-in layouts, but you can create custom layouts.

When you create a new business domain while creating mapping, the default layout is assigned to such business domain. You change the layout later by [editing](/management/entity-type#manage-an-entity-type) the business domain.

The layouts consist of the following elements:

- **Nav** – a container for the following information about a golden record: golden record properties, core vocabularies, source vocabularies, information sources, sources, and relations.

- **Main** – a container for the following information about a golden record: quality metrics and suggested searches.

The following screenshot displays the arrangement of nav (a) and main (b) containers on the golden record overview page.

![golden-record-overview.png]({{ "/assets/images/administration/entity-page-layout/golden-record-overview.png" | relative_url }})

## Layout details page

On the layout details page, you can view relevant information about the golden record page layout and take other actions to manage the layout.

**Configuration**

This tab contains general information about the layout, including:

- Layout template that defines the arrangement of elements on the golden record overview page (the placement of main and nav containers).

- Elements that are displayed on the golden record overview page (all or custom core and non-core vocabulary keys, suggested search, and quality metrics).

**Business domains**

This tab contains all business domains that use the current layout. You can also add more business domains to which the layout will be assigned.

## Create a layout

If built-in layouts are not sufficient for you, you create your own layout.

**To create a layout**

1. On the navigation pane, go to **Administration** > **Golden record layouts**.

1. Select **Create layout**.

1. Enter the display name of the layout.

1. Choose the layout template for organizing the information on the golden record overview page: simple, two column, header, or two column inverse.

1. Select **Create**.

    ![create-layout.gif]({{ "/assets/images/administration/entity-page-layout/create-layout.gif" | relative_url }})

    Alternatively, you can create a layout from the business domain page. You can do it when editing the business domain.

    After the layout is created, you can assign it to the business domain. As a result, the information on the **Overview** tab of all golden records belonging to the business domain will be arranged according to the selected layout.

## Manage a layout

You can change the layout configuration and choose the elements that should be displayed on the golden record overview page. Note that you cannot delete the layout.

**To edit a layout**

1. On the navigation pane, go to **Administration** > **Golden record layouts**.

1. Open the layout that you want to edit, and then select **Edit**.

    The layout template opens in edit mode and contains the following sections:

    - **Display name** – you can change the layout name.

    - **Select layout template** – you can choose another layout template.

    - **Configure layout** – you can choose what elements you want to be displayed on the golden record overview page. By default, all core vocabulary keys and non-core vocabulary keys that the golden record contains are displayed on the golden record overview page, together with quality metrics and suggested searches. You can select custom core and non-core vocabulary keys or disable the quality metrics and suggested searches.

1. To add custom core or non-core vocabulary keys, in the corresponding section, choose the **Custom** option, and then do the following:

    1. Select **Add vocabulary keys**.

    1. Find and select the vocabulary keys to be displayed on the golden record overview page.

    1. Select **Add**.

    The vocabulary keys that you added are displayed on the page.

1. Make other changes as needed.

1. After completing your edits to the layout, select **Save**.

    ![edit-layout.gif]({{ "/assets/images/administration/entity-page-layout/edit-layout.gif" | relative_url }})

    The changes will be automatically applied to the overview pages of all golden records that belong to the business domain associated with the current layout.