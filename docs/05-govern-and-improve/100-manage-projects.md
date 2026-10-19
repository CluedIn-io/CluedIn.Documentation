---
layout: cluedin
title: Manage projects
parent: Govern & improve
nav_order: 100
permalink: /govern/projects
content_type: how-to
tags: ["projects", "streams", "rules"]
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

A project is a single place to organize work that spans multiple areas of CluedIn. When you create a project, CluedIn automatically creates a matching, empty folder with the project's name in each participating area — today, [Streams](/publish/streams) and [Rules](/govern/rules). From the project's detail page, you can see everything already filed into those folders and create new streams or rules that are placed into them automatically, without having to pick a folder yourself.

## Prerequisites

- The `management.projects` permission. The built-in `Admin` and `OrganizationAdmin` roles have it by default; other roles need it granted under [Roles](/administer/users-and-roles).

## Create a project

1. On the navigation pane, go to **Management** > **Projects**.
1. Select **Create project**.
1. Enter a **Name** for the project. The name must be unique within your organization — CluedIn rejects a duplicate name.
1. Select **Create project**.

### Verify the result

CluedIn opens the new project's detail page, which lists a **Streams** and a **Rules** section (both empty for a brand-new project). The project also now appears in the **Projects** list.

### What this changes

Creating a project creates an empty folder with the project's name in both the Streams area and the Rules area, even before anything is filed into them. You can see these folders from the standard [Streams](/publish/streams/manage-streams) and [Rules](/govern/rules) list pages, the same way as any other folder.

If a folder could not be created in one of the areas — for example, because of a temporary error — CluedIn does not create the project either, so you never end up with a project that is missing one of its folders. Create the project again with the same name once the underlying problem is resolved.

## Create a stream or rule from a project

1. On the navigation pane, go to **Management** > **Projects**, then select the project.
1. In the **Streams** or **Rules** section, select **Create stream** or **Create rule**.
1. Fill in the rest of the form as you normally would. The **Folder** field is already set to the project's name and can't be changed from here.
1. Select **Create**.

The new stream or rule is placed into the project's folder automatically. It also shows up from the standard Streams or Rules area, filed under the folder with the project's name.

## If something goes wrong

**Project name already exists.** Project names must be unique within your organization. Choose a different name, or open the existing project instead.
