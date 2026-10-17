---
layout: cluedin
title: General settings
parent: Administer
nav_order: 80
permalink: /administer/general-settings
content_type: reference
redirect_from: ["/administration/general-settings"]
tags: ["administration", "settings", "notifications"]
last_modified: 2026-10-17
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

**General Settings** is the default page under **Organization Settings** (available from the administration menu). It gathers organization-wide and per-user settings that don't belong to a more specific settings area, such as UI preferences, notification preferences, and cluster details.

## Notifications

The **Notifications** section lets you control how you, personally, are notified about activity in CluedIn. These settings are per-user: each person in your organization chooses their own notification preferences, and other users are not affected.

![Notifications section under General Settings]({{ "/assets/images/administration/general-settings/notifications-settings-section.png" | relative_url }})

### Browser notifications

The **Browser notifications** toggle turns operating system (HTML5) notifications on or off for your account. When enabled, CluedIn can show a native browser/OS notification — with an audible chime where your browser supports it — whenever you receive a new notification, even if the CluedIn tab isn't in focus.

Turning this on for the first time prompts your browser to request notification permission. CluedIn only asks for this permission when you actively enable the toggle — it never requests it automatically.

- If you **allow** the permission, the toggle is enabled and persists across sessions.
- If you **block** the permission, CluedIn shows an error message, the toggle stays off, and no OS notifications are sent. To turn it on later, you typically need to allow notifications for the site in your browser's own site settings before enabling the toggle again.

![Browser notifications enabled]({{ "/assets/images/administration/general-settings/os-notifications-enabled.png" | relative_url }})

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

## UI preferences

The **UI preferences** section controls whether users see modules in the side menu that they do not have access to. When this is enabled, users can see restricted modules and request access to them directly from the menu.

## Cluster details

The **Cluster details** section shows read-only information about your CluedIn cluster's networking, including its region, CIDR, and the IP address(es) to whitelist for outbound and inbound traffic.

![Cluster details section, showing region, CIDR, outbound and inbound IP addresses, and the ingress-vs-egress diagram]({{ "/assets/images/administration/general-settings/cluster-details-section.png" | relative_url }})

- **Region** and **CIDR** come from your cloud provider's instance metadata when running on a supported cloud (Azure), or from explicit configuration when set; otherwise they show **Not available**.
- **Outbound IP address(es)** (egress) are the public IP address(es) CluedIn's traffic comes from when it reaches out to external systems, for example to crawl a data source or export to a target. Add these to a customer's allowlist/whitelist so CluedIn's outbound connections aren't blocked — see, for example, the [Snowflake connector](/publish/export-targets/snowflake-connector) documentation. This only shows a value when explicitly configured for your deployment; otherwise it shows **Not available**.
- **Inbound IP address(es)** (ingress) are the public IP address(es) through which users and external systems reach this CluedIn instance — for the API, signing in, and incoming webhook callbacks. Add these to an external system's allowlist/whitelist so it's allowed to send data into CluedIn.

An **Ingress vs egress** diagram summarizes the distinction: ingress is inbound traffic — external systems calling into CluedIn, such as a webhook or an API request; egress is outbound traffic — CluedIn calling out to external systems, such as when crawling or exporting data.
