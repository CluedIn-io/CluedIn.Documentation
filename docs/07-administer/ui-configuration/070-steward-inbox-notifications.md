---
layout: cluedin
title: Connect Slack or Microsoft Teams to the Steward Inbox
parent: UI configuration
grand_parent: Administer
nav_order: 70
permalink: /administer/ui-configuration/steward-inbox-notifications
content_type: how-to
tags: ["administration", "settings", "notifications", "steward inbox", "slack", "microsoft teams"]
last_modified: 2026-10-22
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The Steward Inbox can post task assignments and new-task alerts to a Slack channel or a Microsoft Teams channel, in addition to email and the in-app notification bell. This page covers connecting, testing, and disconnecting those two channels from **Organization Settings > Advanced**.

![The Steward Inbox notifications section in Organization Settings, Advanced tab, with Slack and Microsoft Teams both in their default not-connected state]({{ "/assets/images/administration/ui-configuration/steward-inbox-notifications/steward-inbox-notifications-section.png" | relative_url }})

## Prerequisites

- You need the **Organizational Admin** role (or equivalent tenant-management access) to change these settings.
- **For Slack:** your CluedIn administrator must have configured a Slack App Client ID and Secret for this CluedIn instance. If they haven't, the **Connect Slack** button is disabled and shows a message asking you to contact your administrator — this is a one-time setup an administrator does for the whole instance, not something each organization configures itself.
- **For Microsoft Teams:** you need a webhook URL from a Teams channel's **Incoming Webhook** or **Workflows** connector. See [Create an Incoming Webhook](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook) in Microsoft's documentation if you don't already have one.

## Connect Slack

Slack uses a one-click OAuth flow — you never see or paste a webhook URL.

1. Go to **Organization Settings > Advanced**.
2. In the **Steward Inbox notifications** section, select **Connect Slack**.
3. You're redirected to Slack to sign in (if needed) and choose which workspace and channel notifications should post to.
4. Approve the request. Slack redirects you back to CluedIn, which shows the connected workspace and channel (for example, "Acme Corp · #steward-alerts").

If your administrator hasn't configured Slack OAuth for this instance yet, **Connect Slack** is disabled and shows a message explaining that instead - see the screenshot above.

## Connect Microsoft Teams

Microsoft Teams doesn't support the same one-click OAuth install as Slack, so this channel is connected with a webhook URL instead — but CluedIn still validates it for you before saving it.

1. Go to **Organization Settings > Advanced**.
2. In the **Steward Inbox notifications** section, paste the Teams channel's webhook URL into the **Webhook URL** field.
3. Select **Save & validate**.
4. CluedIn checks that the URL looks like a Teams webhook and sends a real validation message to it. If delivery succeeds, the URL is saved and the section shows **Connected**.

If the URL doesn't look like a Teams webhook - for example a copy-paste mistake - CluedIn rejects it immediately with a clear reason, before ever trying to save or deliver to it:

![The Microsoft Teams webhook field after pasting a URL that isn't a Teams webhook, showing CluedIn's validation message]({{ "/assets/images/administration/ui-configuration/steward-inbox-notifications/teams-webhook-validation.png" | relative_url }})

## Send a test notification

Once a channel shows **Connected**, select **Send test notification** next to it. CluedIn posts a short test message to the connected Slack or Teams channel so you can confirm delivery without waiting for a real steward task.

## Disconnect a channel

Select **Disconnect** next to a connected channel. This clears the saved connection (the Slack workspace/channel or the Teams webhook URL) — steward task notifications stop going to that channel immediately, but email and in-app notifications are unaffected.

## Verify the result

- A connected channel shows its status (**Connected to _workspace_ · _#channel_** for Slack, **Connected** for Teams) instead of **Not connected**.
- The connection survives a page reload and logging out and back in — it's saved against your organization, not your browser session.
- **Send test notification** delivers a real message to the channel immediately; it isn't queued or delayed.

## What this changes

Connecting or disconnecting a channel only changes where steward task notifications are delivered. It does not change:

- Who tasks are assigned to, or any task's approval/board state.
- Email or in-app notifications, which are configured separately and keep working regardless of Slack/Teams connection state.

## If something goes wrong

- **"Slack OAuth is not configured"** when selecting Connect Slack — your CluedIn administrator hasn't set up a Slack App Client ID/Secret for this instance yet. This is an instance-wide setting, not something you can configure from Organization Settings.
- **"That doesn't look like a Microsoft Teams webhook URL"** — double check you copied the full URL from the channel's Incoming Webhook or Workflows connector, including the `https://` prefix.
- **A validation or test message fails to send** — the webhook URL may have been revoked or the channel/connector removed in Teams. Create a new Incoming Webhook or Workflow in Teams and paste the new URL in.
