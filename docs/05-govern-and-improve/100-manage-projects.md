---
layout: cluedin
title: Manage projects
parent: Govern & improve
nav_order: 100
permalink: /govern/projects
content_type: how-to
tags: ["projects", "streams", "rules", "hierarchies", "deduplication", "cleaning", "ai-agents"]
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

A project is a single place to organize work that spans multiple areas of CluedIn. When you create a project, CluedIn automatically creates a matching, empty folder with the project's name in each participating area — today, [Streams](/publish/streams), [Rules](/govern/rules), [Hierarchies](/model/hierarchies), [Deduplication](/master/deduplication), [Clean](/govern/cleaning), and AI agents. The project's detail page lists everything already filed into those folders in one table, and lets you create a new stream, rule, hierarchy, deduplication project, clean project, or AI agent that's placed into the right folder automatically, without having to pick a folder yourself.

## Prerequisites

- The `management.projects` permission. The built-in `Admin` and `OrganizationAdmin` roles have it by default; other roles need it granted under [Roles](/administer/users-and-roles).

## Create a project

1. On the navigation pane, go to **Management** > **Projects**, or select **Create** > **Create Project** from the action center.
1. Select **Create project**.
1. Enter a **Name** for the project. The name must be unique within your organization — CluedIn rejects a duplicate name.
1. Optionally, enter a **Description** and upload an **Image** for the project.
1. Select **Create project**.

### Verify the result

CluedIn opens the new project's detail page, which shows a single, empty table for everything that can be filed into the project. The project also now appears in the **Projects** list, together with its description and image, if provided.

## Change a project's image

1. On the navigation pane, go to **Management** > **Projects**, then select the project.
1. Select **Remove image** to remove the current image.
1. Add a new image the same way as when creating the project.

### What this changes

Creating a project creates an empty folder with the project's name in every participating area, even before anything is filed into them. You can see these folders from each area's own list page — for example [Streams](/publish/streams/manage-streams) or [Rules](/govern/rules) — the same way as any other folder.

If a folder could not be created in one of the areas — for example, because of a temporary error — CluedIn does not create the project either, so you never end up with a project that is missing one of its folders. Create the project again with the same name once the underlying problem is resolved.

## Edit a project

1. On the navigation pane, go to **Management** > **Projects**, then select the project.
1. Select **Edit**.
1. Change the **Name**, the **Description**, or both. The name must still be unique within your organization.
1. Select **Save**.

### Verify the result

The project's detail page immediately shows the new name and description.

### What this changes

Renaming a project renames the matching folder in every participating area to keep it in sync, the same way creating a project creates one. If a folder could not be renamed in one of the areas, CluedIn renames the areas that already succeeded back to the original name and the project keeps its original name, so the project and its folders never end up out of sync. Try the rename again once the underlying problem is resolved.

## Create an item from a project

1. On the navigation pane, go to **Management** > **Projects**, then select the project.
1. Select **Add**, then choose a type: stream, rule, hierarchy, deduplication project, clean project, or AI agent.
1. Fill in the rest of the form as you normally would. The **Folder** field is already set to the project's name and can't be changed from here.
1. Select **Create**.

The new item is placed into the project's folder automatically and appears in the project's table. It also shows up from that area's own standard list page, filed under the folder with the project's name.

## If something goes wrong

**Project name already exists.** Project names must be unique within your organization. Choose a different name, or open the existing project instead. This applies to both creating a project and renaming one.
