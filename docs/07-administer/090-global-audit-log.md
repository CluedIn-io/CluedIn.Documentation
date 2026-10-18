---
layout: cluedin
title: Global audit log
parent: Administer
nav_order: 90
permalink: /administer/global-audit-log
content_type: how-to
tags: ["audit log", "revert", "deduplication", "clean", "jobs", "ai agents"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Global Audit Log** lists changes made across CluedIn — who made each change, when, and what it affected — in a single, filterable list. For some kinds of change, you can also revert them directly from the log.

## Prerequisites

To view an entry, you need view access to the area it belongs to (for example, Deduplication management or AI agents). To revert an entry, you need edit access to that same area.

## View and filter the Global Audit Log

**To open the Global Audit Log**

1. On the navigation pane, go to **Administration** > **Global Audit Logs**.

Each row shows the affected object, the action performed (for example, Insert, Update, or Action), a link to view the detailed changes, who made the change, and when.

![Global Audit Log list with Name, Action, Changes, Modified by, Modified at and Actions columns, showing enabled and disabled Revert icons]({{ "/assets/images/administration/global-audit-log/audit-log-list-actions-column.png" | relative_url }})

Use the toolbar to:

- Select **Refresh** to reload the list.
- Select **Reset** to clear the current filters.
- Filter by date range.
- Filter by object type, using the **View all** dropdown.

## Revert a reversible change

The **Actions** column shows a **Revert** button on every row. Whether it is enabled depends on the specific entry:

- It is **enabled** when CluedIn can safely reverse that exact change.
- It is **disabled**, with the reason shown in a tooltip, when it cannot — for example, because the change itself cannot be reverted automatically, or because the object it affects has since moved into a state where reverting is no longer possible (such as a deduplication project that is no longer in the review stage).

![Disabled Revert button on an Insert row showing the tooltip "Reverting this type of change is not supported"]({{ "/assets/images/administration/global-audit-log/revert-disabled-tooltip.png" | relative_url }})

CluedIn currently supports reverting the following kinds of entry:

- **Deduplication merges** – undoes the specific group or groups of duplicates that the entry merged. The deduplication project must still be in the review stage, with no undo already in progress.
- **Clean project commits** – undoes the project's currently committed changes. The project must still be in the review stage, with no undo already in progress.
- **Custom job updates** – restores the job's previous name, description, schedule, and enabled state. A job's actions are not revertible from the audit log.
- **AI agent updates** – restores the agent's previous name, description, and instructions.

Other kinds of entry, including every **Insert** and **Delete**, are not revertible from the audit log.

{:.important}
Reverting from the Global Audit Log changes the object's current configuration. It does not revert changes an AI agent made to your data — for that, see [View and revert changes made by AI agent](/govern/ai-agents/view-and-revert-changes-made-by-ai-agent).

**To revert an entry**

1. On the row you want to revert, select the **Revert** button in the **Actions** column.

1. In the confirmation dialog, review what will be undone, then select **Revert**.

    ![Revert confirmation dialog reading "Revert this change? This will undo … on AI Agents. This cannot be undone." with Cancel and Revert buttons]({{ "/assets/images/administration/global-audit-log/revert-confirm-dialog.png" | relative_url }})

## Verify the result

When the revert succeeds, a confirmation message appears and the list refreshes. A new entry is added to the top of the log, recording the revert's outcome (success or failure) and a reference to the change set it reverted.

If the revert fails, an error message explains why, and no partial change is applied.

## What this changes

Reverting writes the object's previous values back through the same update path a user would use, so it triggers the same downstream effects as making that change manually — for example, reverting a deduplication merge starts the project's normal undo process. Reverting is itself audited, so it does not remove the original entry from the log.
