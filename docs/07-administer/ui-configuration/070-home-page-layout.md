---
layout: cluedin
title: Home page layout
parent: UI configuration
grand_parent: Administer
nav_order: 70
permalink: /administer/ui-configuration/home-page-layout
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The Home page is made up of individual widgets - KPIs, charts, the Steward Inbox, and data quality summaries. An administrator can choose which widgets appear by default for users with a given role, and any user can further customize their own Home page by adding or removing widgets.

## Available widgets

- **KPIs** - golden records, sources, AI agents, clean projects, and deduplication projects at a glance.
- **Requires attention** - change requests, role requests, and other items waiting on action.
- **Business domains and tags** - golden record counts by business domain and top tags.
- **Statistics** - billable records, users, business domains, and vocabulary usage.
- **Useful links** - quick access to documentation and onboarding resources.
- **Steward inbox** - the number of outstanding steward tasks, with a link to the full [Steward Inbox]({{ "/govern-and-improve/workflows" | relative_url }}).
- **Data quality overview** - the overall percentage of bad data across your organization's quality metrics.
- **Data quality by source** - the percentage of bad data broken down by data source, worst first.

A user who has not chosen their own widgets, and whose role has no default layout configured, sees the original five widgets (KPIs, Requires attention, Business domains and tags, Statistics, and Useful links) - the Home page's unchanged default.

## Customize your own Home page

Select **Customize home page** in the top-right corner of the Home page, then check or clear the widgets you want to see. Your selection is saved to your account and loads the same way the next time you sign in, on any device.

![The Home page with the Customize home page panel open, showing a checklist of all eight widgets]({{ "/assets/images/administration/home-page-layout/customize-panel.png" | relative_url }})

Once saved, the widgets you chose appear on your Home page. The original widgets keep their full-width layout; the Steward inbox and data quality widgets are sized as smaller cards and appear side by side when more than one is enabled.

![The Home page showing the Steward inbox, Data quality overview, and Data quality by source widgets next to each other]({{ "/assets/images/administration/home-page-layout/home-with-widgets.png" | relative_url }})

## Configure a default layout per role

An administrator can choose which widgets appear by default for users with a particular role, from **Administration** > **Organization settings** > **Home Page Layouts**.

1. Select the role.
2. Check or clear the widgets you want that role to see by default.
3. Select **Save**.

![The Home Page Layouts admin page, with a role selected and a checklist of widgets]({{ "/assets/images/administration/home-page-layout/admin-role-layout.png" | relative_url }})

A user who has not customized their own Home page sees their role's configured default. If a user belongs to more than one role with a configured default, they see the default of whichever of those roles is found first - this is not currently configurable. A user can still customize their own Home page at any time, which takes priority over any role default. Clearing every widget for a role removes its default layout; users with that role then see the original five widgets.
