---
layout: cluedin
title: How to connect CluedIn to Slack for alerts
parent: Knowledge base
permalink: /kb/connect-to-slack
nav_order: 2
---

# CluedIn → Slack Alerts: End-to-End Setup Guide

This walkthrough shows two supported patterns for getting **data quality** and **master data (MDM) alerts** from CluedIn into Slack channels:

- **Option A (Fastest):** Post alerts to Slack with an **Incoming Webhook**  
- **Option B (Flexible/Recommended):** Use a **Slack App (bot)** with fine-grained permissions, per-channel routing, threads, and richer formatting

Both options include examples for **Data Quality (DQ)** and **Master Data (MDM)** events, plus testing, routing, and troubleshooting.

---

## Prerequisites

- **CluedIn**: Access to Alerts/Workflows (or Webhooks/Integrations), and permissions to configure environment variables/secret store.
- **Slack**: Workspace admin rights (to create/manage apps) and permission to install apps in target channels.
- **Network/Security**: Allow outbound HTTPS from CluedIn to Slack endpoints.

---

## Terminology

- **DQ Alert**: Triggers when rules/thresholds fail (e.g., completeness < 98%, schema drift, dedupe conflicts, pipeline errors).
- **MDM Alert**: Triggers on golden record lifecycle events (create/update/merge/survivorship changes, source conflict).
- **Routing**: Logic that picks a Slack channel per alert (by domain, severity, or entity type).
- **Block Kit**: Slack’s JSON format for rich messages.

---

## Option A — Incoming Webhook (Fastest Path)

> Great for simple “send this alert to #data-quality” use cases.

### 1) Create a Slack Incoming Webhook

1. Go to **https://api.slack.com/apps** → **Create New App** → “From scratch”.
2. App name: `CluedIn Alerts`, Workspace: _your workspace_.
3. In **Incoming Webhooks**, **Activate** webhooks.
4. **Add New Webhook to Workspace**, choose a default channel (e.g., `#data-quality`), then copy the **Webhook URL** (looks like `https://hooks.slack.com/services/T...`).

### 2) Store the Webhook URL in CluedIn

- Put the webhook URL in **CluedIn Secrets/Key Vault**: `SLACK_WEBHOOK_DQ` (for DQ) and/or `SLACK_WEBHOOK_MDM` (for MDM).  
  You can reuse one URL or keep per-channel secrets.

### 3) Create/Adjust CluedIn Alert Rules

- **DQ Examples**:  
  - Completeness < 98% for `Customer`  
  - New **Schema Drift** detected for `Product` (new column, type change)  
  - **Deduplication conflict** rate > threshold  
  - **Pipeline job failure** (ingestion/enrichment/curation)

- **MDM Examples**:  
  - **Golden Record created** (Customer)  
  - **Survivorship rule changed** attribute owner/priority  
  - **Merge/Split** events  
  - **Upstream conflict** on key attribute (email, legal name, VAT)

### 4) Add a “Send to Slack (Webhook)” Workflow Step

- For each alert rule, add an action that POSTs to the webhook URL with a **Block Kit** payload.

**Minimal payload (JSON):**
```json
{
  "text": "CluedIn Alert",
  "blocks": [
    { "type": "header", "text": { "type": "plain_text", "text": "🚨 Data Quality Alert" } },
    { "type": "section", "fields": [
      { "type": "mrkdwn", "text": "*Domain:*\nCustomer" },
      { "type": "mrkdwn", "text": "*Severity:*\nHigh" }
    ]},
    { "type": "section", "text": { "type": "mrkdwn", "text": "*Rule:* Completeness < 98%\n*Score:* 96.2%\n*Records impacted:* 1,283" } },
    { "type": "context", "elements": [
      { "type": "mrkdwn", "text": "Run ID: 2025-08-24T03:45Z • Env: prod" }
    ] }
  ]
}



