---
layout: cluedin
title: Data Quality Dashboard
parent: Govern & improve
nav_order: 80
permalink: /govern/data-quality-dashboard
content_type: concept
redirect_from: ["/governance/data-quality-dashboard"]
source_path: docs/070-governance/030-data-quality-dashboard.md
tags: ["governance", "data quality", "metrics", "accuracy", "completeness", "connectivity", "relevance", "consistency", "currentness", "iso 25012", "business domains", "sources", "ai agents", "trust center", "provenance", "explainability", "human accountability", "thresholds", "needs attention", "trusted vocabularies", "copilot"]
last_modified: 2026-11-02
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Data Quality Dashboard** gives you a single, visual overview of the quality of the data mastered in CluedIn. It is built on nine data quality metrics—**Accuracy**, **Completeness**, **Connectivity**, **Consistency**, **Currentness**, **Relevance**, **Provenance**, **Explainability**, and **Human Accountability**—and breaks them down by business domain, by source, by AI agent, and by overall trust, so you can quickly see where data quality issues are concentrated and act on them.

{:.note}
Consistency, Currentness, Provenance, Explainability, and Relevance are per-record metrics. Consistency measures how often different sources agree on the same property value. Currentness measures how recently a record was last modified relative to an expected refresh interval (configurable by an administrator, 90 days by default). Provenance measures whether a record's data can be traced back to a known source. Explainability measures whether a record's properties map to a governed, documented vocabulary key rather than an untracked, free-form value. Relevance measures the share of a record's mapped vocabulary keys that belong to a vocabulary [marked Trusted](/model/vocabularies/manage-vocabularies#vocabulary-details-page) — a record with most of its mapped keys in a Trusted vocabulary scores higher than one mapped mostly to untrusted vocabularies, regardless of how many vocabularies it touches overall. Human Accountability is the only organization-wide (not per-record) metric of the nine — see [Trust Dimensions](#trust-dimensions) below.

**To open the Data Quality Dashboard**

- On the navigation pane, go to **Governance** > **Quality metrics**.

    ![The Data Quality Dashboard Overview tab, showing the organization-wide score for each data quality metric, a trend chart, and a radar chart]({{ "/assets/images/governance/data-quality-dashboard/data-quality-dashboard-overview.png" | relative_url }})

The dashboard is organized into five tabs:

- **Overview** – each data quality metric as an overall, organization-wide score, a [Needs attention](#needs-attention) summary, a trend chart showing every metric over time, and a radar chart comparing them all at a glance.
- **Business Domain** – the [Quality by Business Domain](#quality-by-business-domain) table.
- **Source** – the [Quality by Source](#quality-by-source) breakdown.
- **AI Agent** – the [Quality by AI Agent](#quality-by-ai-agent) summary.
- **Trust Center** – the [Trust Center](#trust-center) overview, trust dimensions, freshness and trust-signal charts, governance maturity, and trust gaps.

## Recalculating metrics manually

The scores on this dashboard are only as current as the last time the jobs that compute them ran:

- **Global metrics** – computes the organization-wide metric scores shown throughout this dashboard. Runs once a day by default.
- **High time resolution metrics** – recomputes the metrics this organization keeps at a high time resolution. Runs every 15 minutes by default.

If you've just ingested or changed data and don't want to wait for the next scheduled run, select **Run Global metrics** or **Run High time resolution metrics** at the top of the page to trigger the corresponding job immediately.

![The Data Quality Dashboard header, showing the Run High time resolution metrics and Run Global metrics buttons]({{ "/assets/images/governance/data-quality-dashboard/recalculate-metrics.png" | relative_url }})

{:.note}
These are the same two jobs listed on the [Jobs](/administer/jobs) page under **System-provided jobs** — running them from here is a shortcut, not a separate action. If your organization requires approval to run jobs, selecting the button sends a request to the job's owner instead of running it immediately.

## Setting a threshold on a metric

Every metric tile, on the Overview tab and in the Trust Center, lets you set a target threshold:

- Select **Set threshold** on a metric tile, enter a whole-number percentage (for example, `80`), and select **Save**.
- Once a threshold is set, the tile shows a **Target: X%** badge, colored green when the metric's current score meets or exceeds the threshold and red when it doesn't.
- Select the badge at any time to change or clear the threshold.
- If any metric is below its configured threshold when the dashboard loads, a notification appears listing which ones need attention, and the [Needs attention](#needs-attention) summary lists them in full.

    ![A metric tile with a Target badge, colored red because the metric's current score is below the configured threshold]({{ "/assets/images/governance/data-quality-dashboard/metric-threshold.png" | relative_url }})

{:.note}
A threshold of 0, or no threshold set, means the metric has no target configured — no badge is shown and it's never flagged as below target.

## Metric detail page

Selecting a score — a KPI tile's **View records** link, or a cell in the [Quality by Business Domain](#quality-by-business-domain) or [Quality by Source](#quality-by-source) table — opens a detail page scoped to that specific metric and dimension, so a score of 88% for a business domain's Accuracy takes you straight to the records behind that domain's Accuracy score, not the organization-wide one.

The detail page shows:

- The current value and a trend chart, sorted worst-score-first by default.
- A **Compare with** selector, grouped by Business Domain and Source, that overlays a second line on the chart for comparison. It never lists crawler or connector types, since comparing a score against a connector type isn't a meaningful axis.
- A short guidance banner naming what the metric measures and a **Go to** shortcut to the part of the platform that improves it — for example, Accuracy's shortcut goes to Enrichment, and Completeness's goes to Clean.
- For a metric with a real Copilot skill behind its fix (currently Explainability), a **Fix with AI** action next to the shortcut. It starts a new Copilot chat session with a prompt scoped to the issue and takes you there, so you watch and can refine whatever Copilot proposes before it's applied — it doesn't change anything on its own. This action only appears when Copilot is configured for your organization.
- An **Entities used for calculation** table listing the golden records contributing to the score.

{:.note}
The entities table currently lists records only when viewing a metric's organization-wide score. Opening the detail page from a specific business domain or source scopes the chart and the comparison correctly, but the entities table does not yet filter down to that dimension.

## Needs attention

Below the Overview tab's metric tiles, a **Needs attention** strip lists every metric currently scoring below its configured threshold — each entry names the metric, its current score against its target, a short suggestion for what to review, and a **View** link that scrolls back up to that metric's tile. The strip only appears once at least one metric has both a threshold set and a score below it; it's hidden entirely otherwise.

The Business Domain and Trust Center tabs each show their own equivalent: the Business Domain tab lists business domain/metric combinations below target, and the Trust Center's [Trust Gaps](#trust-gaps) list covers the trust dimensions specifically.

![The Needs attention strip, listing two metrics below their configured threshold with View links]({{ "/assets/images/governance/data-quality-dashboard/data-quality-dashboard-overview.png" | relative_url }})

### Filtering the trend charts

The Overview tab's **Metrics over time** chart has a time-period selector (7/30/90 days, or all time) and a business domain selector; **Current snapshot** has its own business domain selector. Selecting a specific business domain re-plots the chart from that domain's own scores instead of the organization-wide ones. The Trust Center's **Trust signals over time** chart (see [Trust Center](#trust-center)) has the same pair of filters, scoped to Provenance and Explainability.

## Quality by Business Domain

The **Quality by Business Domain** table lists every [business domain](/model/business-domains/business-domains-explained) that has been scored, one row per domain, with a column per data quality metric — so you can quickly spot which combinations of business domain and metric need attention. A summary strip above the table shows the number of scored business domains, the total records across them, and their average quality; a **Records by domain** chart and a **Quality trend by domain** chart sit below it, and a **Needs attention** callout lists any domain/metric combination currently below its configured threshold.

If no business domain has been scored yet, this section shows an empty state instead of the table.

{:.important}
A business domain only appears in the table once data quality metrics have been calculated for at least one record of that business domain.

![The Quality by Business Domain table, showing business domains as rows and data quality metrics as columns, with a summary strip above]({{ "/assets/images/governance/data-quality-dashboard/quality-by-business-domain.png" | relative_url }})

## Quality by Source

The **Quality by Source** section lists every source feeding data into your CluedIn environment — connectors, file uploads, API ingestion endpoints, databases, and enrichers alike — each shown by its own name (for example, the uploaded file's name or the ingestion endpoint's configured name) together with its icon or a generic source icon, so you can identify at a glance which systems are behind your data quality scores. A summary strip shows the total number of sources, how many have at least one computed metric, and how many need attention; a search box and connector-type/status filters narrow the table down. Each row shows, where available, the source's record count, when it was last evaluated, a **Healthy**/**Needs attention**/**No data** status, and its score for every data quality metric — a **No data** state for a field that hasn't been calculated yet. A **Source quality distribution** bar and a **Needs attention** panel (with a **Critical**/**Medium** severity per issue) sit below the table.

{:.note}
A source whose records all came from a single ingestion event (for example, a one-off file upload) can appear more than once if that file was ingested more than once — each ingestion gets its own score.

If no sources are connected yet, the summary strip, filters, and table still show (with zero values and the table's own empty state) rather than the whole section being replaced by a blank page.

![The Quality by Source tab, showing summary cards, search and filters, and the sources table]({{ "/assets/images/governance/data-quality-dashboard/quality-by-source.png" | relative_url }})

## Quality by AI Agent

The **Quality by AI Agent** section shows a summary strip (AI agents monitored, pending reviews, and recommended improvements across all agents) above a table of your [AI agents](/govern/ai-agents), one row per agent, with the following columns:

- **Quality score** – the agent's own current data quality score, averaged across whichever metrics it has measured history for. Shows **—** while the agent has no measured history yet.
- **Pending review** – the number of results produced by that agent's jobs that are waiting to be approved or rejected.
- **Improvements suggested** – how many data quality metrics would score measurably higher if every one of the agent's pending results were approved.
- **Runs** – shows **No data** until per-agent run history is tracked.
- **Status** – **Healthy**, **Attention** (while the agent has pending reviews), or **No data**.

Next to the table, an **Agent quality trend** panel lets you pick an agent and a time window; it shows a **No trend data yet** state until that agent has at least two days of measured history.

Below the table, a **Review queue** lists AI agent suggestions waiting on a human — the same ones your [Steward Inbox](/govern/ai-agents) surfaces — with an impact level (**High**/**Medium**/**Low**, based on how many records the suggestion affects), when it was detected, and a **Review** action that takes you to it.

If no AI agents exist in your environment yet, the table shows an empty state instead of the list.

![The Quality by AI Agent tab, showing the agent table, trend panel, and review queue]({{ "/assets/images/governance/data-quality-dashboard/quality-by-ai-agent.png" | relative_url }})

## Trust Center

The **Trust Center** tab brings together an overall trust score, the trust-specific metrics, a view of how fresh your data is, trust signals over time, governance maturity, and your trust gaps.

![The Trust Center tab, showing the Overall Trust Score, trust dimensions, the Freshness & Decay chart, and Trust Signals Over Time]({{ "/assets/images/governance/data-quality-dashboard/trust-center.png" | relative_url }})

### Overall Trust Score

The **Overall Trust Score** is a single number from 0–100, averaging every available data quality metric, including the trust dimensions below. A fixed target of 70 drives an **On target**/**Below target** badge next to the score. It's also colour-coded:

- **Green** (80–100) – your data quality and trust signals are strong.
- **Amber** (50–79) – some trust signals need attention.
- **Red** (0–49) – multiple trust signals are below target.

### Trust Dimensions

- **Provenance** – the fraction of a record's data that can be traced back to a known, identifiable source.
- **Explainability** – the fraction of a record's properties that map to a governed vocabulary key, rather than an untracked, free-form value whose meaning and origin aren't documented.
- **Human Accountability** – the only organization-wide metric here, rather than per-record: the fraction of AI agent suggestions that were explicitly acted on by a person rather than auto-approved. This metric only appears once your organization has at least one AI agent suggestion.

{:.note}
Rejecting an AI agent suggestion always counts as a human decision. An approval only counts if auto-approve is currently turned off for AI agents (see [AI Agents](/govern/ai-agents)) — an auto-approved suggestion was never reviewed by a person.

### Freshness & Decay

This chart groups your records into buckets by how many days have passed since they were last modified, so you can see at a glance how much of your data is fresh versus going stale. It's built from the same Currentness metric shown on the Overview tab.

### Trust Signals Over Time

This chart plots Provenance and Explainability over time, with the same time-period and business domain filters as the Overview tab's **Metrics over time** chart (see [Filtering the trend charts](#filtering-the-trend-charts)).

### Governance Maturity

The **Governance Maturity** section shows a progress bar per governance practice, each as a percentage from 0–100%, colour-coded against a shared legend (**On track** ≥ 70%, **In progress** 40–69%, **Needs attention** 20–39%, **At risk** < 20%):

- **Cleaning** – the percentage of your (non-archived) clean projects that have actually been applied at least once, rather than only ever created.
- **Matching & Merging** – the percentage of your (non-archived) matching/merging projects that run automatically on a schedule, rather than requiring someone to generate and commit candidates manually every time.
- **Agent Coverage** – the percentage of your active business domains that are targeted by at least one enabled AI agent job.
- **Rule Coverage** – the percentage of your vocabulary keys that are referenced by at least one rule.
- **Data Sharing** – the percentage of your streams that are started and have actually sent at least one record, rather than only ever configured.

{:.note}
A score of 0% on any bar means that practice hasn't been set up yet for your organization, not that data is missing — the section always shows all five practices.

### Trust Gaps

The **Trust Gaps** list shows every trust dimension (Provenance, Explainability, and Human Accountability) currently below its configured threshold, with its current score against its target, a short suggestion for what to review, and a **Take action** link that scrolls back up to that dimension's tile. It shows **No trust gaps** once every trust dimension meets its target, or once none of them has a threshold configured yet — see [Setting a threshold on a metric](#setting-a-threshold-on-a-metric).

![The Governance Maturity progress bars and the Trust Gaps list, showing a trust dimension below its configured target with a Take action link]({{ "/assets/images/governance/data-quality-dashboard/governance-maturity.png" | relative_url }})

## Data quality for a Stream

Each [Stream](/publish/streams/concept-of-a-stream) also has its own **Data Quality** tab, which shows the same data quality metrics scoped to that stream's own business domain. For details, see [View stream details](/publish/streams/manage-streams#view-stream-details).
