---
layout: cluedin
title: Monitor AI usage and spend
parent: AI agents
grand_parent: Govern & improve
nav_order: 70
permalink: /govern/ai-agents/monitor-ai-usage-and-spend
content_type: how-to
tags: ["management", "ai agents", "ai usage", "spend limits", "cost"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

CluedIn's **AI Usage & Spend** dashboard reports token usage and estimated spend across every AI-backed capability in the product — Copilot, AI Rules, AI Agents (including their embeddings and document vision calls), Audits, and External Search — in one place. From the same page, authorized users can configure organization-wide spend limits.

## Prerequisites

- You need at least **Consultant**-level access to the **Artificial Intelligence** administration area to view the dashboard.
- You need at least **Consultant**-level access to the **Tenant Management** administration area to save spend limits, since spend limits are stored as organization settings.
- At least one [AI deployment](/govern/ai-agents/prerequisites-to-using-ai-agents#configure-a-deployment) must have made AI requests for the dashboard to show any usage.

## View AI usage and spend

**To view AI usage and spend**

1. On the navigation pane, go to **Administration** > **Artificial Intelligence**, and then select **Usage & Spend**.

1. Use the date range picker in the top-right corner to choose the period to report on (for example, the last 7 or 30 days, or a custom range).

    The dashboard shows:

    - **Total tokens** and **Estimated spend** for the selected period.
    - A **Token usage over time** chart, showing total tokens per day.
    - A **Breakdown by AI capability** table, with prompt tokens, completion tokens, total tokens, and estimated spend per AI capability.

    ![The AI Usage and Spend dashboard, with total tokens and estimated spend tiles, a token usage over time chart, and a breakdown by AI capability table]({{ "/assets/images/management/ai-agents/monitor-ai-usage-and-spend/usage_dashboard_overview.png" | relative_url }})

{:.important}
All monetary values on this dashboard are **estimates**, based on the **Cost Per Input Token** and **Cost Per Output Token** configured on each [AI deployment](/govern/ai-agents/prerequisites-to-using-ai-agents#configure-a-deployment). They are not an invoice. A deployment with no cost per token configured reports $0.00 estimated spend even though it has usage.

## Configure spend limits

Spend limits apply organization-wide, across every AI capability. A limit is checked independently per billing currency: for example, a $5 limit is not affected by spend in a different currency.

**To configure spend limits**

1. On the **Usage & Spend** dashboard, scroll down to the **Spend limits** section.

1. Configure the following settings:

    - **Daily spend limit** – the maximum estimated AI spend allowed per calendar day (UTC). Leave at 0 for no limit.
    - **Monthly spend limit** – the maximum estimated AI spend allowed per calendar month (UTC). Leave at 0 for no limit.
    - **Block AI requests when a spend limit is reached** – when off (the default), reaching a limit only shows a warning on the dashboard. When on, new AI requests fail until the limit resets.

    ![The Spend limits section of the Usage and Spend dashboard, with Daily spend limit and Monthly spend limit sliders, and a Block AI requests checkbox]({{ "/assets/images/management/ai-agents/monitor-ai-usage-and-spend/breakdown_and_spend_limits.png" | relative_url }})

1. Select **Save spend limits**.

## Verify the result

Once a limit is reached, the **Usage & Spend** dashboard shows a warning banner at the top of the page, naming whether the limit is the daily or monthly one and whether AI requests are currently being blocked.

![A warning banner on the Usage and Spend dashboard stating that the organization has reached its configured daily AI spend limit]({{ "/assets/images/management/ai-agents/monitor-ai-usage-and-spend/spend_limit_warning_banner.png" | relative_url }})

If **Block AI requests when a spend limit is reached** is on, any further AI request — from Copilot, an AI Rule, an AI Agent, or any other AI capability — fails with an error until the limit resets (at the next calendar day or month, UTC).

## What this changes

Saving spend limits only changes organization configuration; it does not affect any AI request already in progress. Raising a limit, or turning off **Block AI requests when a spend limit is reached**, takes effect immediately for new AI requests.
