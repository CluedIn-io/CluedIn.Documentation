---
layout: cluedin
title: Side navigation menu
parent: User interface
grand_parent: Administration
permalink: /administration/side-navigation-menu
nav_order: 020
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

On this page you can learn about the supported side menu layouts, as well as how to switch between them.

# Supported side menu layouts

CluedIn features a side navigation menu on the left that helps you navigate between the main modules of the platform.

![side_nav_menu.png](../../assets/images/administration/user-interface/side_nav_menu.png)

Initially, the menu consisted of all platform modules categorized into expandable groups. With this approach, there was no prioritization of modules based on how frequently they are used. Eventually, a new menu was introduced, taking prioritization into account.

By default, the new side layout menu is enabled, but you can switch to the old menu whenever needed.

{: .important }
> The side menu layout applies at the organization level, and not for individual users.

## New side menu layout

The new side menu layout consists of the following elements.

![new_side_nav_menu_explained.png](../../assets/images/administration/user-interface/new_side_nav_menu_explained.png)

1. Action center – the **Create** button redirects to a page with most commonly used actions (related to ingestion, preparation, and other).

1. Search bar (applies to the side menu only).

1. Home page.

1. Frequently used modules – contain direct links to most frequently used modules of ClueIn.

    Hovering over a frequently used module displays brief information about the module, as well as statistics about the number of items in that module (total number of items, as well as the items with the largest count).

    ![new_menu_popup_sp.png](../../assets/images/administration/user-interface/new_menu_popup_sp.png)

1. Other modules – contain links to all modules of CluedIn, categorized into collapsible groups, such as **Consume**, **Management**, and so on.

## Old side menu layout

The old side menu layout consists of the following elements.

![old_side_nav_menu_explained.png](../../assets/images/administration/user-interface/old_side_nav_menu_explained.png)

1. Action center – the **Create** button redirects to a page with most commonly used actions (related to ingestion, preparation, and other).

1. Home page.

3. Links to all modules of CluedIn, categorized into groups, such as **Ingestion**, **Preparation**, and so on.

# Set a side menu layout

By default, the old side layout menu is enabled, but you can switch to the new menu whenever needed.

**Pre-requisites**

- You must have access to manage the [feature flags](/administration/feature-flags). This access requires [administrator permissions](/administration/roles/claims#admin).

**To set a side menu layout**

1. On the navigation menu, go to **Administration** > **Feature flags**.

1. Locate the feature called **New Main Menu**.

1. Do one of the following:

    - To enable the new side menu layout, turn the toggle on.

        ![enable_new_menu.png](../../assets/images/administration/user-interface/enable_new_menu.png)

    - To enable the old side menu layout, turn the toggle off.

        ![enable_old_menu.png](../../assets/images/administration/user-interface/enable_old_menu.png)

1. Confirm your changes.

    The selected side menu layout is now applied to CluedIn at the organization level.