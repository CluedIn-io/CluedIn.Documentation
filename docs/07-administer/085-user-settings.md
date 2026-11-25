---
layout: cluedin
title: User settings
parent: Administer
nav_order: 85
permalink: /administer/user-settings
content_type: reference
tags: ["administration", "settings", "notifications", "password"]
last_modified: 2026-11-06
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

**User Settings** is where you manage your own account: your password and your personal notification preferences. Unlike [General settings](/administer/general-settings), nothing here is organization-wide — changes only ever affect the signed-in user who made them.

Open it from the user menu in the top right corner of CluedIn, then **Settings**.

## Change password

The **Change Password** section lets you update the password for your own account. Enter your current password, then a new password that meets the organization's password requirements, and confirm it.

## Notifications

The **Notifications** section lets you control how you, personally, are notified about activity in CluedIn. These settings are per-user: each person in your organization chooses their own notification preferences independently, and changing yours never affects anyone else's.

![Notifications section under User Settings]({{ "/assets/images/administration/user-settings/notifications-settings-section.png" | relative_url }})

### Browser notifications

The **Browser notifications** toggle turns operating system (HTML5) notifications on or off for your account. When enabled, CluedIn can show a native browser/OS notification — with an audible chime where your browser supports it — whenever you receive a new notification, even if the CluedIn tab isn't in focus.

Turning this on for the first time prompts your browser to request notification permission. CluedIn only asks for this permission when you actively enable the toggle — it never requests it automatically.

- If you **allow** the permission, the toggle is enabled and persists across sessions.
- If you **block** the permission, CluedIn shows an error message, the toggle stays off, and no OS notifications are sent. To turn it on later, you typically need to allow notifications for the site in your browser's own site settings before enabling the toggle again.

### Notification types

The **Notification types** checkboxes let you choose which categories of [notifications](/administer/ui-configuration/notifications) you want to receive:

- **Errors**
- **In Progress**
- **Pending Approval**
- **Action Required**

All types are enabled by default. Unchecking a type mutes it for your account only:

- It no longer contributes to your unread notification count (shown in the notification bell and the browser tab title).
- It no longer triggers a browser notification, even if **Browser notifications** is turned on.

Notifications of a muted type are still generated — you can re-enable a type at any time to resume being notified about it.

### Notification sections

The **Notification sections** checkboxes let you choose which parts of CluedIn can send you a notification at all. Unchecking a section mutes every notification from it for your account, the same way unchecking a notification type does.
