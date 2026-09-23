---
layout: cluedin
title: Notifications
parent: User Interface
nav_order: 100
permalink: /user-interface/notifications
tags: ["ui", "notifications"]
last_modified: 2026-09-23
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Notifications in CluedIn keep you informed about important events, background operations, approvals, warnings, and other activity that may require your attention.

A notification is designed to give you enough context to understand:

- **What happened**
- **Where it happened**
- **How important it is**
- **Whether somebody needs to act**
- **How far a longer-running operation has progressed**
- **What you can do next**

Not every notification contains every element. CluedIn only displays the parts that are relevant to the event.

## Notification anatomy

A notification can contain the following elements.

### Unread indicator

Unread notifications are visually highlighted so you can quickly distinguish new activity from notifications that you have already seen.

The unread state helps you scan a large set of notifications without having to remember which events you have already reviewed.

After a notification has been read, the visual emphasis is removed.

### Source icon

The icon identifies the part of CluedIn, integration, or process that produced the notification.

This provides immediate context before you read the full message. For example, notifications originating from an import, workflow, AI agent, stream, or another subsystem can use different icons.

### Severity badge

A severity badge communicates the importance or outcome of the notification at a glance.

Typical severity levels include:

- **Success** – the operation completed successfully.
- **Warning** – the operation completed, but there is something you should review.
- **Danger** – the operation failed or requires attention.

Severity helps users prioritize which notifications to investigate first.

### Category and source

The metadata row can show the notification category and source.

The **category** groups similar notifications together, while the **source** identifies the component or process that generated the event.

This is particularly useful when several parts of CluedIn are performing background work at the same time.

### Status badge

A notification can include a status badge to describe its current state.

Status is separate from severity. For example, a background operation can have an **In progress** status without being a warning, or it can have a **Completed** status with a success severity.

Keeping status and severity separate makes it easier to understand both **where an operation is in its lifecycle** and **whether anything is wrong**.

### Assignees

Notifications that represent work requiring human involvement can show one or more assignees.

Assignee avatars make it clear who is responsible for reviewing or completing the task. When multiple people are assigned, avatars can be displayed as an overlapping group to keep the notification compact.

Assignees are shown only when the notification is associated with a person or group of people.

### Timestamp

The timestamp tells you when the event occurred.

Recent notifications can use a relative time such as **6m ago**, while older notifications can display a locale-appropriate date and time.

This makes recent activity easy to scan while still preserving precise context for older events.

### Title

The title is a short description of the event.

It should communicate the most important information without requiring you to expand the notification. Examples include a completed import, a failed export, a new approval request, or a finished AI agent job.

### Body

The body provides additional context about the event.

It can contain plain text or formatted Markdown and may include information such as:

- What operation was performed
- Which records or objects were affected
- Why an operation failed
- What the user should do next
- Links to additional information

For longer messages, CluedIn can initially limit the height of the body and provide a **Show more** option. This keeps the notification list easy to scan without hiding detailed information when it is needed.

## Progress information

Long-running operations can include progress information.

A notification can show a sequence of tasks or stages, making it possible to understand how far an operation has progressed without navigating away from the notification.

For example:

- Completed steps are shown as complete.
- The active step can show a progress bar and percentage.
- Future steps can be shown as pending.

Progress bars are intended for active work. Once a task is complete or has not yet started, the notification can display its status without showing a progress bar.

This is useful for processes such as large imports, exports, synchronization jobs, AI operations, or other background tasks that take time to complete.

## Notification actions

Some notifications allow you to take action directly from the notification.

### Button actions

Buttons are used when the notification requires a clear user response.

Depending on the event, an action can represent a positive, cautionary, or destructive operation.

Examples can include:

- Approve
- Reject
- Retry
- Review
- Resolve

Button actions reduce the number of steps required to respond to an event because you can act from the notification instead of first locating the related object elsewhere in CluedIn.

Buttons are only shown when a direct response is appropriate.

### Link actions

A notification can also contain one or more link-style actions.

Links are useful for navigation rather than direct state changes. For example, a notification might provide a link to:

- Open the affected record
- View a job
- Review logs
- Open a rule
- View an export or stream

Separating button actions from link actions makes it clearer whether selecting an action will **perform an operation** or simply **take you somewhere for more information**.

## Attachments

Notifications can contain attachments when additional files or supporting material are associated with the event.

If there is more than one attachment, CluedIn can group them into an expandable attachment section. This keeps the notification compact while still allowing access to every file.

Attachments are useful for events that produce supporting artifacts, reports, exports, evidence, or other files that a user may need to review.

## Optional notification zones

Some parts of a notification are displayed only when they are relevant.

Examples include:

- **Progress information** – only for operations that have meaningful stages or take time to complete.
- **Action buttons** – only when a user response is required or useful.
- **Assignees** – only when a person or group is responsible for the event.
- **Attachments** – only when files are associated with the notification.

This adaptive structure prevents simple notifications from becoming unnecessarily large while still allowing complex notifications to provide detailed operational context.

## Read and unread states

Notifications have a visual read state.

**Unread notifications** receive stronger visual emphasis, such as a tinted background or a visible indicator.

**Read notifications** use a more neutral appearance.

The purpose of the read state is not to indicate whether an issue has been resolved. It only indicates whether the notification has been seen.

A notification can therefore be read while the underlying task is still pending, in progress, or requires action.

## How the notification elements work together

A well-structured notification allows you to understand an event in layers.

First, the **icon, category, severity, status, and timestamp** provide a fast summary.

Next, the **title and body** explain what happened.

If the event is still running, **progress information** shows what is happening now.

If somebody is responsible for the event, **assignees** make ownership visible.

Finally, **actions, links, and attachments** give you a direct path to the next step.

This structure is designed to make notifications useful both when you are quickly scanning activity and when you need to investigate an individual event in detail.

## Notifications and workflows

Notifications can also be used with CluedIn workflows. For example, a CluedIn event can trigger a workflow that sends information or an approval request to external systems such as Outlook or Microsoft Teams.

For more information, see [Create and manage workflows](/workflow/create-and-manage-workflows).
