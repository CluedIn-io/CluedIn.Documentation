---
layout: cluedin
title: Data Quality Dashboard
parent: Governance
nav_order: 3
permalink: /governance/data-quality-dashboard
tags: ["governance", "data quality", "metrics", "accuracy", "completeness", "connectivity", "relevance", "consistency", "currentness", "iso 25012", "business domains", "ai agents", "trust center", "provenance", "explainability", "human accountability", "thresholds"]
last_modified: 2026-10-13
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Data Quality Dashboard** gives you a single, visual overview of the quality of the data mastered in CluedIn. It is built on nine data quality metrics—**Accuracy**, **Completeness**, **Connectivity**, **Consistency**, **Currentness**, **Relevance**, **Provenance**, **Explainability**, and **Human Accountability**—and breaks them down by business domain, by source, by AI agent, and by overall trust, so you can quickly see where data quality issues are concentrated and act on them.

{:.note}
Consistency, Currentness, Provenance, and Explainability are per-record metrics. Consistency measures how often different sources agree on the same property value. Currentness measures how recently a record was last modified relative to an expected refresh interval (configurable by an administrator, 90 days by default). Provenance measures whether a record's data can be traced back to a known source. Explainability measures whether a record's properties map to a governed, documented vocabulary key rather than an untracked, free-form value. Human Accountability is the only organization-wide (not per-record) metric of the nine — see [Trust Dimensions](#trust-dimensions) below.

**To open the Data Quality Dashboard**

- On the navigation pane, go to **Governance** > **Quality metrics**.

    ![data-quality-dashboard-overview.png]({{ "/assets/images/governance/data-quality-dashboard/data-quality-dashboard-overview.png" | relative_url }})

The dashboard is organized into five tabs:

- **Overview** – each data quality metric as an overall, organization-wide score, plus their trend over time.
- **Business Domain** – the [Quality by Business Domain](#quality-by-business-domain) heatmap.
- **Source** – the [Quality by Source](#quality-by-source) breakdown.
- **AI Agent** – the [Quality by AI Agent](#quality-by-ai-agent) summary.
- **Trust Center** – the [Trust Center](#trust-center) overview, trust dimensions, freshness chart, and improvement guides.

## Setting a threshold on a metric

Every metric tile, on the Overview tab and in the Trust Center, lets you set a target threshold:

- Select **Set threshold** on a metric tile, enter a whole-number percentage (for example, `80`), and select **Save**.
- Once a threshold is set, the tile shows a **Target: X%** badge, colored green when the metric's current score meets or exceeds the threshold and red when it doesn't.
- Select the badge at any time to change or clear the threshold.
- If any metric is below its configured threshold when the dashboard loads, a notification appears listing which ones need attention.

    ![metric-threshold.png]({{ "/assets/images/governance/data-quality-dashboard/metric-threshold.png" | relative_url }})

{:.note}
A threshold of 0, or no threshold set, means the metric has no target configured — no badge is shown and it's never flagged as below target.

## Quality by Business Domain

The **Quality by Business Domain** section shows a heatmap of every data quality metric against every [business domain](/key-terms-and-features/entity-type) that has been scored. Each cell shows the score for one metric within one business domain, so you can quickly spot which combinations of metric and business domain need attention.

If no business domain has been scored yet, this section shows an empty state instead of the heatmap.

{:.important}
A business domain only appears in the heatmap once data quality metrics have been calculated for at least one record of that business domain.

## Quality by Source

The **Quality by Source** section lists every source connected to your CluedIn environment, together with its icon, so you can identify at a glance which systems are feeding data into CluedIn. Where the data quality metrics have been calculated for a specific source, the corresponding score is shown next to it; otherwise, the entry shows **No data yet**.

If no sources are connected yet, this section shows an empty state instead of the list.

![quality-by-source.png]({{ "/assets/images/governance/data-quality-dashboard/quality-by-source.png" | relative_url }})

## Quality by AI Agent

The **Quality by AI Agent** section lists your [AI agents](/management/ai-agents) and shows, for each one, the following information:

- **Pending review** – the number of results produced by that agent's jobs that are waiting to be approved or rejected.

- **Est. quality improvement** – an estimate, in percentage points, of how much the data quality metrics would improve, on average, if all of that agent's pending results were approved. This estimate is only shown while the agent has at least one pending result; otherwise, the entry shows **No pending results to review**.

If no AI agents exist in your environment yet, this section shows an empty state instead of the list.

![quality-by-ai-agent.png]({{ "/assets/images/governance/data-quality-dashboard/quality-by-ai-agent.png" | relative_url }})

## Trust Center

The **Trust Center** tab brings together an overall trust score, the trust-specific metrics, a view of how fresh your data is, and concrete guidance for improving each metric.

![trust-center.png]({{ "/assets/images/governance/data-quality-dashboard/trust-center.png" | relative_url }})

### Overall Trust Score

The **Overall Trust Score** is a single number from 0–100, averaging every available data quality metric, including the trust dimensions below. It's colour-coded:

- **Green** (80–100) – your data quality and trust signals are strong.
- **Amber** (50–79) – some trust signals need attention.
- **Red** (0–49) – multiple trust signals are below target.

### Trust Dimensions

- **Provenance** – the fraction of a record's data that can be traced back to a known, identifiable source.
- **Explainability** – the fraction of a record's properties that map to a governed vocabulary key, rather than an untracked, free-form value whose meaning and origin aren't documented.
- **Human Accountability** – the only organization-wide metric here, rather than per-record: the fraction of AI agent suggestions that were explicitly acted on by a person rather than auto-approved. This metric only appears once your organization has at least one AI agent suggestion.

{:.note}
Rejecting an AI agent suggestion always counts as a human decision. An approval only counts if auto-approve is currently turned off for AI agents (see [AI Agents](/management/ai-agents)) — an auto-approved suggestion was never reviewed by a person.

### Freshness & Decay

This chart groups your records into buckets by how many days have passed since they were last modified, so you can see at a glance how much of your data is fresh versus going stale. It's built from the same Currentness metric shown on the Overview tab.

### How to improve your score

Each metric has a short, concrete guide for improving it — for example, Accuracy suggests plugging in an external enricher, such as Dun & Bradstreet, to validate your data against an official source of truth.

## Data quality for a Stream

Each [Stream](/consume/streams/concept-of-a-stream) also has its own **Data Quality** tab, which shows the same data quality metrics scoped to that stream's own business domain. For details, see [View stream details](/consume/streams/manage-streams#view-stream-details).
