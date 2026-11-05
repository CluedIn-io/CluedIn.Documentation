---
layout: cluedin
title: Steward Inbox
parent: Administration
permalink: /administration/steward-inbox
nav_order: 45
tags: ["administration", "steward inbox", "tasks", "governance"]
---

In this article, you will learn how to use the Steward Inbox to find, prioritize, and resolve the stewardship work assigned to you.

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

## Overview

The Steward Inbox brings together, in one place, everything in CluedIn that is currently waiting on you:

- **Match approvals** &mdash; deduplication projects you own that have duplicate match groups waiting for review.
- **AI Agent result approvals** &mdash; AI agents you own that have results waiting to be approved or rejected.
- **Unhealthy rules** &mdash; processing rules you own that require attention (for example, because they were automatically disabled after a vocabulary change).
- **Record change approvals** &mdash; changes to records that need your approval before they take effect.

Rather than visiting each of these areas individually to check for outstanding work, the Steward Inbox surfaces all of it together, with suggested actions, a lightweight task board, and metrics on your stewardship activity.

## Access the Steward Inbox

You can get to the Steward Inbox in two ways:

- On the navigation pane, under **Quick access**, select **Steward Inbox**.

    ![steward-inbox-nav.png]({{ "/assets/images/administration/steward-inbox/steward-inbox-nav.png" | relative_url }})

- In the upper-right corner, select the ellipsis button, and then select **My tasks**.

    ![steward-inbox-my-tasks-menu.png]({{ "/assets/images/administration/steward-inbox/steward-inbox-my-tasks-menu.png" | relative_url }})

## List view

By default, the Steward Inbox opens in **List** view, which shows your tasks as a sortable, filterable table.

![steward-inbox-list.png]({{ "/assets/images/administration/steward-inbox/steward-inbox-list.png" | relative_url }})

- Use the **task type** and **status** filters, and the sort order dropdown, to narrow down the list.
- Each row shows the task's title, type, status, and (where relevant) how many underlying items it represents &mdash; for example, the number of pending match groups in a deduplication project.
- Select a task's title to open its [task details panel](#task-details-and-suggested-actions).

## Board view

Select **Board** to switch to a Trello-style board with three lanes: **To Do**, **Doing**, and **Done**.

![steward-inbox-board.png]({{ "/assets/images/administration/steward-inbox/steward-inbox-board.png" | relative_url }})

Drag a task card from one lane to another to update its status. The status is saved immediately and persists the next time you open the Steward Inbox or reload the page.

{:.important}
Moving a task to a lane is independent from actually resolving it. Dragging a card into **Done** marks your own progress on the board; it does not by itself approve, reject, or otherwise act on the underlying item. Use the task's [suggested actions](#task-details-and-suggested-actions) to make that decision.

When you move a task into **Done**, CluedIn celebrates with a brief confetti animation. The animation plays once for that move and does not repeat if you refresh the page.

## Task details and suggested actions

Select a task (from either the list or the board) to open its details panel. The panel shows:

- The task type and current status.
- A description of the task and, where applicable, how many underlying items it covers.
- **Suggested actions** for resolving the task.

The suggested actions depend on the task type:

- For **record change approvals**, you can **Approve** or **Reject** the change directly from the panel.
- For the other task types (match approvals, AI agent result approvals, and unhealthy rules), select **View** to open the related project, agent, or rule and complete the review there.

## Metrics

At the top of the Steward Inbox, a metrics panel shows:

- **Outstanding tasks** &mdash; the number of tasks currently assigned to you that aren't marked Done.
- **Completed tasks (last 14 days)** &mdash; a trend chart of how many tasks you moved to Done each day over the last two weeks.

Both update automatically as you work through your tasks.
