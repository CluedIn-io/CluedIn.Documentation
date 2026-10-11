---
layout: cluedin
title: Audits
parent: Management
nav_order: 100
permalink: /management/audits
tags: ["management", "audits", "governance", "data quality"]
last_modified: 2026-10-11
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
- **Open findings** – records marked **Not correct** on audits that are still active.
- **Failed audits** – audits with at least one record marked **Not correct**.

Below the summary cards, you can filter the audit list by auditor and open any audit to see its details.

## Create an audit

Select **New audit** to start one. You can set:

- **Name** and **Description**.
- **Mode** – **Manual**, where a person reviews each record, or **AI-based**, where an AI agent assists the review.
- **What should this audit check?** – pick one of the built-in templates (for example *Completeness against the contract* or *Validate records are accurate*), or select **Ask for something else, in your own words** to describe a custom check.
- **Time frame** – the start and end dates the audit covers.
- **Users involved** – the auditors participating in the audit, in addition to its creator. Pick from the users already in your organization.
- **AI endpoint** – for an AI-based audit, the configured AI endpoint used to evaluate records.

An audit starts in the **Not started** state. Select **Start audit** from its detail page to make it **Active**.

### Run an AI-based audit

For an audit in **AI-based** mode, once it is **Active** and has an AI endpoint configured, select **Run AI audit** on its detail page.

CluedIn searches your estate for candidate records, and for each one asks the configured AI endpoint whether the record is actually in scope for what you asked it to check and, if so, whether it passes. A finding is recorded automatically for every relevant record, the same way a finding would be recorded if a person marked it by hand. The run continues in the background — findings appear on the detail page as they come in.

## Record findings

While an audit is **Active**, any involved auditor can mark golden records as **Correct** or **Not correct**:

- **On a record's golden record page**, use the Correct/Not correct control next to **Delete**.
- **In search results**, select one or more records and use the **Correct**/**Not correct** bulk actions.

These controls are only available while you have an active audit. Once an audit is **Stopped**, its findings remain visible on the audit's detail page, but no new findings can be recorded against it.

## Review audit results

Each audit's detail page shows a chart of its findings — how many records were marked **Correct** versus **Not correct** — alongside the audit's configuration and lifecycle state.

Below the chart, a findings list shows every record that has been audited: its name (linked back to its golden record page), the result, whether it was marked by a person or by an AI audit run, who recorded it, and when.

Select **Stop audit** to end an active audit. Stopping an audit preserves its findings and counts for later review; it does not delete them.
