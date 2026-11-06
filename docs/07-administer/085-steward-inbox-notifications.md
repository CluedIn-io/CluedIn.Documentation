---
layout: cluedin
title: Steward Inbox notifications
parent: Administer
nav_order: 85
permalink: /administer/steward-inbox-notifications
content_type: how-to
tags: ["administration", "notifications", "slack", "teams", "steward inbox"]
last_modified: 2026-11-06
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

When a new item appears in a user's [Steward Inbox](/govern) — such as a triggered [tag alert](/govern/tags/tag-monitoring#create-tag-alerts), an unhealthy rule, or a task assigned to them — CluedIn can post about it to Slack and Microsoft Teams, in addition to the in-app notification. This article covers connecting those two channels, and customizing the layout of the messages CluedIn sends.

## Prerequisites

- You need the **OrganizationAdmin** role to change these settings.
- A Slack **incoming webhook URL** for the channel you want notifications posted to, created from Slack's own app settings. A Slack incoming webhook always posts to one specific, predetermined channel.
- A Microsoft Teams **webhook URL** for the channel you want notifications posted to, for example from a Power Automate flow configured with a "When a Teams webhook request is received" trigger.

## Connect Slack and Microsoft Teams

**To connect Slack and/or Microsoft Teams**

1. On the navigation pane, go to **Administration** > **Settings** > **Advanced settings**.

1. In the **Search settings** box, enter `Steward Inbox` to jump to the **Steward Inbox** section.

1. Paste your webhook URL into **Slack webhook URL** and/or **Microsoft Teams webhook URL**.

    ![The Steward Inbox settings section, with the Slack webhook URL and Microsoft Teams webhook URL fields filled in]({{ "/assets/images/administration/notification-templates/webhook-settings.png" | relative_url }})

1. Select **Save**.

Each field is a plain webhook URL — there is no separate "connect" or authorization step.

## Customize notification message templates

By default, every Steward Inbox notification type uses the same general layout in Slack and Teams: a headline, the item's title and description, its type, and action buttons. You can replace this with your own layout per notification type and per channel, built from a fixed set of blocks.

**To build a custom notification template**

1. On the navigation pane, go to **Administration** > **Settings** > **Advanced settings**.

1. Next to **Notification message templates**, select **Customize**.

    ![The Notification message templates settings section, with a Customize button]({{ "/assets/images/administration/notification-templates/settings-section.png" | relative_url }})

1. Select the **Notification type** you want to customize, or leave it set to **Default** to change the layout used by any type without its own template.

1. Select the **Channel** (Slack or Microsoft Teams) you want to customize. Slack and Teams templates are stored and edited separately, since the two platforms don't share a layout model.

    The block list starts out with the current default layout for that type and channel.

    ![The notification message template builder, showing the default blocks for a notification type]({{ "/assets/images/administration/notification-templates/builder-panel.png" | relative_url }})

1. Edit, add, remove, and reorder blocks as needed:

    | Block | Purpose |
    |---|---|
    | **Header** | A bold title line. Plain text only — any `**bold**` markers you type are stripped. |
    | **Text** | A paragraph. Supports `**bold**` for emphasis. |
    | **Divider** | A visual separator line. |
    | **Image** | An image, by URL, with alt text. |
    | **Button** | A single, fixed link button with its own label and URL. |
    | **Actions** | Expands to the "View task" link plus whatever actions the notification type supports (for example Approve/Reject/Ignore) — not editable itself, only where it sits in the layout. |

    Use the up/down arrows next to a block to reorder it, and the trash icon to remove it. Select a block type from **Add block** and select **Add** to insert a new one at the end.

1. In any **Header** or **Text** block, use the following placeholders — each wrapped in double curly braces, for example `{% raw %}{{title}}{% endraw %}` — to insert data from the notification itself:

    | Placeholder | Resolves to |
    |---|---|
    | `headline` | The short summary line CluedIn would otherwise show as the header (for example "A new task needs your attention"). |
    | `title` | The notification's title. |
    | `description` | The notification's description. |
    | `taskType` | The notification type, in a human-readable form (for example "Tag Alert Triggered"). |
    | `dueDate` | The due date, when the notification has one. Otherwise blank. |
    | `itemCount` | The number of items involved, when applicable. Otherwise blank. |
    | `dueDateLine` | A ready-made "Due: ..." line, including its own line break, when there's a due date — otherwise blank, so the line disappears entirely rather than leaving an empty "Due:" label. |
    | `itemCountLine` | The same, for a ready-made "Items: ..." line. |
    | `url` | The deep link back into the Steward Inbox for this item. |

    ![The notification message template builder with an edited Header block and a newly added Image block]({{ "/assets/images/administration/notification-templates/builder-edited.png" | relative_url }})

1. Select **Show raw preview** at any point to see the exact Slack Block Kit or Teams Adaptive Card JSON your current blocks would produce, rendered with illustrative sample data.

1. Select **Send test** to post the current (unsaved) blocks to the channel connected for that type, using sample data. Nothing is saved by sending a test.

1. Select **Save**.

## Verify the result

Once a webhook URL is saved, the next Steward Inbox notification of any kind posts to that channel, usually within about a minute.

A saved template is used immediately for any new matching notification — you don't need to wait for a deploy or restart.

To check either one without waiting for a real event, use the message builder's **Send test** button, which posts immediately using sample data.

## What this changes

- Saving a template only affects notifications of that exact (notification type, channel) combination going forward. It has no effect on notifications already sent.
- A template saved against **Default** affects any notification type that doesn't have its own, more specific template.
- Deleting a saved template (**Delete saved**, shown once a template exists for the selected type and channel) reverts that type/channel back to the built-in default layout.
- Customizing templates does not change which events generate a Steward Inbox notification in the first place, only how that notification is formatted for Slack and Teams.

## If something goes wrong

**Send test reports no webhook is configured** — the channel you selected (Slack or Teams) has no webhook URL saved yet. Add one under [Connect Slack and Microsoft Teams](#connect-slack-and-microsoft-teams) first.

**A real notification isn't arriving in Slack/Teams** — confirm the webhook URL is still valid (an incoming webhook can be revoked or regenerated on Slack's or Microsoft's side independently of CluedIn), and that the notification type you're expecting is one Steward Inbox actually raises for your data.
