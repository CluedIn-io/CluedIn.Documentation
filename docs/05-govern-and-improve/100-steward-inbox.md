---
layout: cluedin
title: Steward Inbox
parent: Govern & improve
nav_order: 100
permalink: /govern/steward-inbox
content_type: concept
tags: ["steward inbox", "tasks", "approvals", "quarantine", "ai suggestions", "folders", "data steward"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

<div class="audience">
  <p class="audience-question">Where do I find everything that needs my attention as a data steward?</p>
  <p class="audience-who">Data stewards.</p>
</div>

The **Steward Inbox** is a single, mail-client-style place to see and act on every task assigned to you across CluedIn — match approvals, record change approvals, quarantined records, AI agent proposals, unhealthy streams, and the setup checklist items CluedIn creates while you configure your environment — instead of checking each module separately.

**To open the Steward Inbox**

- On the navigation pane, select **Steward Inbox**.

    ![The Steward Inbox in List view, showing the KPI summary, folder tabs, the task list, and the reading pane]({{ "/assets/images/governance/steward-inbox/steward-inbox-list.png" | relative_url }})

{:.note}
A [workflow](/govern/workflows/concept-of-approvals) rule-change approval that's routed to you internally (rather than through Outlook or Teams) shows up here as a task too.

## Summary and views

The KPI row at the top — **Open**, **New**, **In progress**, **Completed**, **Ignored** — counts your tasks by status. Selecting a card filters the list to that status; selecting it again clears the filter. Select **Hide summary** to collapse the row and get more room for the list, or **Show summary** to bring it back.

Switch between two layouts with the view switch in the top right:

- **List** – a resizable list of tasks on the left (drag the divider, or select it and press the Left/Right arrow keys) and a reading pane on the right that shows whichever task is selected. Select the expand icon in the reading pane for a full-screen view of the task.
- **Board** – your tasks as cards in four columns, one per status (**To Do**, **Doing**, **Done**, **Ignored**). Drag a card to a different column to change its status; selecting a card opens the same task detail in a panel.

## Finding a task

Use the toolbar above the list to narrow it down:

- **Search** – matches a task's title or description.
- **Status**, **Task type**, and **Domain** filters – each option shows how many tasks match it. A filter that isn't on its default value (**All …**) shows a small **×** next to it to clear just that filter.
- **Sort** – toggles the list between newest-received-first and grouped by status.

An unread task is marked with a green stripe on the left of its row rather than bold text. If a filter change means the task currently open in the reading pane no longer matches, the reading pane returns to its empty state — it never keeps showing a task the list no longer displays.

To act on several tasks at once, tick their checkboxes (or tick the header checkbox to select every task currently shown) and use the bulk action bar that appears: **Move to folder**, **Mark as read**, and **Ignore** — plus **Remove from folder** and **Move to another folder** when you're inside a folder.

## Resolving a task

Every task's main action (and, where one applies, a second action) sits at the top left of its detail view. What they are depends on the task's type:

| Task type | Main action | Second action |
|---|---|---|
| Record change approval | Approve | Reject |
| Quarantined records | Fix and release | Reject |
| AI agent proposal | Approve | Reject |
| Every other type | Open in source | — |

For a task type that doesn't yet have an in-inbox action, selecting **Open in source** takes the task to **In progress** and opens the underlying item (for example, the stream or the clean project) so you can resolve it there; once it's in progress, the button becomes **Mark as complete**.

**Open in source**, **Forward**, and **Ignore** are always available as text links at the top right of the task (on a narrow screen, **Forward** and **Ignore** move into a **⋮** menu). The same actions, plus **Move to folder**, are available from a task's row in the list via its own **⋮** menu.

### Reviewing the affected data

For a quarantined-records task, the **Affected data** section of the task lists the individual quarantined records that **Fix and release** or **Reject** will act on. This list is read-only for now — approving or rejecting always acts on every record shown, not a subset you pick.

## AI suggestions

A task's **AI suggestion** section shows one of a few states:

- **No AI suggestion** – AI isn't available for this task yet, or hasn't been asked to look at it. If it's available, an **Assign to AI** button lets you request one.
- **Preparing** – a suggestion has been requested and CluedIn is working on it.
- A proposed change set, with a **Why** toggle that expands to show what AI would change and why.

If you accept a suggestion, CluedIn applies the change for you. If you reject it, nothing changes, and you can ask AI to look at the task again later. AI never applies a change on its own — a suggestion only takes effect once you accept it.

{:.note}
AI suggestions currently cover the setup checklist tasks CluedIn creates while you configure your environment. Suggestions for the other task types (match approvals, quarantined records, and so on) are on the roadmap, starting with match approvals and quarantined records.

## Folders

Folders are a personal way to group tasks that doesn't affect their status — moving a task into a folder doesn't move it out of **All Tasks**, and doesn't change whether it's open, in progress, or completed.

Each folder appears as its own tab, showing how many open tasks it contains. Once there are more folders than fit on screen, the extra ones move into an **All folders** menu.

**To create a folder**

- Select **+ New folder** next to the search box (only shown while you're viewing **All Tasks**), from the **All folders** menu, or from the folder dropdown in the move-to-folder window.

A new folder starts out empty, showing **No tasks in this folder yet** and an **Add tasks** button.

**To add tasks to a folder**

1. Open the folder's **⋮** menu (hover over its tab) and select **Add tasks**, or select the **Add tasks** button shown in an empty folder.
1. Use the search box and the status/type filters to find the tasks you want, and tick them. **Select all** ticks every task currently matching the filters; the count under the search box shows how many are selected and how many more match a different filter you haven't applied yet. **Show selected** reviews just your current picks, and **Clear selection** starts over.
1. Select **Add**.

You can also drag a task's row directly onto a folder tab, or use **Move to folder** from a task's **⋮** menu or the bulk action bar.

**To rename or delete a folder**

- Open the folder's **⋮** menu and select **Rename folder** or **Delete folder**. Deleting a folder asks for confirmation and moves its tasks back to **All Tasks** without changing their status.
