---
layout: cluedin
title: Audits
parent: Management
nav_order: 100
permalink: /management/audits
tags: ["management", "audits", "governance", "data quality"]
last_modified: 2026-10-12
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Audits** module lets you run manual or AI-based audits against your golden records and record whether each one is correct.

Use audits when you need a structured, trackable review of your data — for example, checking completeness against a contract, validating that merge decisions were justified, or confirming that personal data stayed inside its intended boundary.

## Open the Audits page

To open Audits, go to **Management** > **Audits**.

At the top of the page, summary cards show:

- **Audits in the last week** – audits created in the last 7 days.
- **Open findings** – records marked **Not correct** that have not yet been resolved (see [Resolve findings](#resolve-findings)), regardless of whether their audit is still active.
- **Failed audits** – audits with at least one record marked **Not correct**.

Next to the summary cards, a small chart breaks down every audit by its current status (**Not started**, **Active**, **Stopped**).

Below the summary cards, you can filter the audit list by auditor and open any audit to see its details. Each audit's **Status** is shown as a colored badge — blue for **Not started**, green for **Active**, grey for **Stopped** — so you can tell at a glance which audits are currently running. Select a column header to sort the table by that column.

Select multiple audits using the checkboxes on the left of the table to **Start audits** or **Stop audits** in bulk. Only audits in the right lifecycle state for the action are affected — starting a selection only starts the ones that are **Not started**, and stopping only stops the ones that are **Active**.

## Create an audit

Select **New audit** to start one. You can set:

- **Name** and **Description**.
- **Mode** – **Manual**, where a person reviews each record, or **AI-based**, where an AI agent assists the review.
- **What should this audit check?** – pick one of the built-in templates (for example *Completeness against the contract* or *Validate records are accurate*), pick a [reusable template](#reusable-templates) your organization has saved, or select **Ask for something else, in your own words** to describe a custom check.
- **Limit AI audit to records matching** – for an AI-based audit, an optional rule, built with the same rule builder as Advanced Search, that restricts which golden records the AI audit run considers. Leave it empty to consider every record.
- **Time frame** – the start and end dates the audit covers.
- **Users involved** – the auditors participating in the audit, in addition to its creator. Pick from the users already in your organization.
- **AI endpoint** – for an AI-based audit, the configured AI endpoint used to evaluate records.
- **Repeat every (days)** – an optional number of days after which, once the audit is stopped, CluedIn automatically creates and starts a new audit with the same configuration. Leave it empty for a one-off audit.

An audit starts in the **Not started** state. Select **Start audit** from its detail page to make it **Active**.

### Run an AI-based audit

For an audit in **AI-based** mode, once it is **Active** and has an AI endpoint configured, select **Run AI audit** on its detail page.

CluedIn searches your estate for candidate records — restricted to the audit's scope rule if one was set, otherwise every record — and for each one asks the configured AI endpoint whether the record is actually in scope for what you asked it to check and, if so, whether it passes. A finding is recorded automatically for every relevant record, the same way a finding would be recorded if a person marked it by hand. The run continues in the background — findings appear on the detail page as they come in.

### Recurring audits

If an audit was created with **Repeat every (days)** set, CluedIn checks hourly for audits that have become due. An audit becomes due once that many days have passed since it was last stopped (or since it last automatically recurred). When it becomes due, CluedIn creates a new audit with the same name, description, mode, template, prompt, scope rule, AI endpoint, time frame and involved users, starts it, and — for an AI-based audit — runs it immediately. Each occurrence is its own audit, so earlier runs and their findings are preserved on their own detail pages.

### Reusable templates

When writing a custom prompt, check **Save this prompt as a reusable template** and give it a name to make it available to everyone in your organization the next time they create an audit — it appears in the template picker alongside the built-in templates. Saved templates are listed below the template picker, where you can also delete ones you no longer need.

## Record findings

While an audit is **Active**, any involved auditor can mark golden records as **Correct** or **Not correct**:

- **On a record's golden record page**, use the Correct/Not correct control next to **Delete**.
- **In search results**, select one or more records and use the **Correct**/**Not correct** bulk actions.

These controls are only available while you have an active audit. Once an audit is **Stopped**, its findings remain visible on the audit's detail page, but no new findings can be recorded against it.

Every finding records the identifier of the golden record that was audited, not just its name at the time — so it stays traceable even if the record is later renamed or merged.

## Review audit results

Each audit's detail page shows a chart of its findings — how many records were marked **Correct** versus **Not correct** — alongside the audit's configuration and lifecycle state.

Below the chart, a findings list shows every record that has been audited: its name (linked back to its golden record page), the result, whether it was marked by a person or by an AI audit run, who recorded it, and when.

Select **Stop audit** to end an active audit. Stopping an audit preserves its findings and counts for later review; it does not delete them.

Select **Export findings (CSV)** on an audit's detail page to download its findings list as a CSV file, for reporting or further analysis outside CluedIn.

### Resolve findings

For a record marked **Not correct**, the findings list lets you:

- **Assign** the finding to a user in your organization, to make clear who is responsible for following it up.
- **Mark resolved** once the underlying issue has been fixed. A resolved finding shows who resolved it and when, and no longer counts toward the **Open findings** summary metric.
- **Reopen** a resolved finding if it turns out the issue was not actually fixed.

Assigning and resolving findings works regardless of whether the audit is still active, so remediation can continue after an audit is stopped.
