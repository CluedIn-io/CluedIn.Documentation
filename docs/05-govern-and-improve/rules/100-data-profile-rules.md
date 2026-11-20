---
layout: cluedin
title: Schedule and alert on data profile rules
parent: Rules
grand_parent: Govern & improve
nav_order: 100
permalink: /govern/rules/data-profile-rules
content_type: how-to
tags: ["management", "rules", "data profiling", "alerts", "steward inbox"]
last_modified: 2026-11-20
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

A data profile rule checks a metric computed over the golden records of a business domain, such as row count, completeness, or uniqueness, against a threshold you set. This article explains how to run a data profile rule on a schedule, how to configure its alerts, and where those alerts appear.

You manage data profile rules in **Management** > **Data Profile Rules**. You can also start from the **Action Center**: **Create Data Profiling Rule** opens the creation pane directly, and **Configure Alerts** opens the alert settings for all rules.

## Prerequisites

- The **Rule Builder** claim with at least the Consulted access level, which lets you create rules and change their schedule and alert settings. Informed lets you view rules only. See [Feature access](/administer/users-and-roles/feature-access).

## Run a data profile rule on a schedule

Every active data profile rule is evaluated automatically on the organization-wide data profiling interval, which is once a day by default. To run a rule more or less often than that, give it its own schedule.

**To set a custom schedule for a rule**

1. Go to **Management** > **Data Profile Rules** and open the rule.

1. In the **Schedule** card, select **Use a custom schedule**.

1. In **Run every (minutes)**, enter how often the rule should run. The minimum is 5 minutes and the maximum is 31 days (44,640 minutes).

1. Select **Save schedule**.

To go back to the organization-wide interval, clear **Use a custom schedule** and select **Save schedule**.

Scheduled runs are recorded the same way as runs you start with **Run**. They appear in the **Run history** chart and the **Recent runs** table, and they update the **Profile outcome** card. Inactive rules are not evaluated on a schedule.

![The detail page of a data profile rule, with the Schedule card set to run every 5 minutes, the Alerts card, and a run history of scheduled runs]({{ "/assets/images/management/data-profile-rules/rule-detail-schedule-alerts.png" | relative_url }})

## Configure alerts for a rule

When a data profile rule starts failing, organization admins get an in-app notification and a **Data Profile Alert** task in their [Steward Inbox](#data-profile-alerts-in-the-steward-inbox). When the rule passes again, they get a resolution notification.

By default, an alert is raised once, when the rule starts failing. To be reminded for as long as the rule keeps failing, turn on reminders for the rule.

**To configure reminders for a rule**

1. Open the rule.

1. In the **Alerts** card, select **Keep reminding me while it keeps failing**.

1. In **Every (minutes)**, enter how often to send a reminder.

1. Select **Save alert settings**.

To change the alert settings of several rules at once, on the **Data Profile Rules** page, select **Alerts**.

## Data Profile Alerts in the Steward Inbox

Each failing data profile rule creates a **Data Profile Alert Triggered** task in the Steward Inbox of every organization admin. The task shows the rule, the business domain, the metric, and the threshold it failed, and its **View** action opens the rule. When the rule passes again, the task is marked resolved. If the rule fails again later, a new task is created.

![The Steward Inbox with a Data Profile Alert Triggered task selected, showing the rule description and guidance on how to solve it]({{ "/assets/images/management/data-profile-rules/steward-inbox-alert.png" | relative_url }})

## Verify the result

- After you save a schedule, the **Schedule** card shows **Use a custom schedule** selected with your interval. The next scheduled run appears in **Recent runs** within the interval you set, give or take the 5 minutes between scheduler checks.
- After you save alert settings, a confirmation message appears and the **Alerts** card keeps your values when you reload the page.

## What this changes

Changing a rule's schedule or alert settings only saves configuration. It doesn't evaluate the rule or change any golden records. Every evaluation, scheduled or manual, adds a run to the rule's history; runs are not deleted when you change the schedule.

