---
layout: cluedin
title: Audits
parent: Govern & improve
nav_order: 85
permalink: /govern/audits
content_type: concept
tags: ["audits", "data quality", "governance", "findings", "manual audit", "AI-assisted audit"]
last_modified: 2026-11-01
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

An **audit** is a run that assesses a set of golden records against a check - either a built-in template (completeness against the contract, provenance, accuracy against an outside authority, and others) or a prompt you write yourself - and records each record as **correct** or **not correct**. Audits let you track data quality findings over time instead of only seeing a point-in-time score.

**To open Audits**

- On the navigation pane, go to **Management** > **Audits**.

    ![The Audit List page, showing the header, KPI row, the Start your first data audit hero, the Audit guidance and Recent activity panel, and the empty audit history table]({{ "/assets/images/governance/audits/audit-list-overview.png" | relative_url }})

## KPI row

Four cards summarize your organization's audits at a glance:

- **Runs this week** - audits created in the last 7 days.
- **Open findings** - "not correct" findings that haven't been resolved yet.
- **Failed audits** - audits with at least one "not correct" finding.
- **Last audit** - the date of the most recently created audit, or "Never" if none exist yet.

## Starting an audit

Select **New audit** in the page header, or, before your organization has created one yet, **Create manual audit** or **Build AI-assisted audit** from the empty-state hero. Both open the same panel:

- **Manual** audits are worked through by a person - you (or anyone with access) open the audit afterward and mark each record correct or not correct yourself.
- **AI-based** audits also need an AI endpoint and, optionally, a rule limiting which records are in scope - the AI evaluates each matching record against the check and records a finding automatically.

Either way, give the audit a name, pick what it should check (a built-in template, one of your own saved templates, or a custom prompt in your own words), and optionally a time frame, the users involved, and a recurrence interval to re-run it automatically.

## Audit guidance and recent activity

The right-hand panel is a standing reference, not something you configure:

- **Audit guidance** lists the kinds of things an audit template can check for - completeness, accuracy, duplicates, and governance rules.
- **Recent activity** shows your organization's most recently created audits, each linking to its own detail page.

## Audit history

Below the KPI row, **Audit history** lists every audit as a table (Audit, Status, Mode, Scope, Findings, Created by, Started, Duration), with:

- **Tabs** - **All audits**, **Open findings** (audits with an unresolved "not correct" finding that haven't been stopped), and **Failed** (any audit with at least one "not correct" finding, matching the Failed audits KPI).
- **Search and filters** - search by name, and filter by Status, Mode, Type, or Auditor.
- **Export CSV** - export either the current page or every matching audit.

    ![The Audit history table after creating an audit, showing an updated KPI row and the new audit's row and recent-activity entry]({{ "/assets/images/governance/audits/audit-history-populated.png" | relative_url }})

Select an audit's name to open its detail page, where you work through its findings, and - for a manual audit - mark records correct or not correct yourself.
