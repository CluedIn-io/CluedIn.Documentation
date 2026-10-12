---
layout: cluedin
title: Data Quality Dashboard
parent: Governance
nav_order: 3
permalink: /governance/data-quality-dashboard
tags: ["governance", "data quality", "metrics", "accuracy", "completeness", "connectivity", "relevance", "consistency", "currentness", "iso 25012", "business domains", "ai agents"]
last_modified: 2026-10-12
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Data Quality Dashboard** gives you a single, visual overview of the quality of the data mastered in CluedIn. It is built on six data quality metrics—**Accuracy**, **Completeness**, **Connectivity**, **Consistency**, **Currentness**, and **Relevance**—and breaks them down by business domain, by source, and by AI agent, so you can quickly see where data quality issues are concentrated and act on them.

{:.note}
Consistency and Currentness are based on the [ISO/IEC 25012](https://en.wikipedia.org/wiki/ISO/IEC_25012) data quality characteristics of the same name. Consistency measures how often different sources agree on the same property value; Currentness measures how recently a record was last modified relative to an expected refresh interval (configurable by an administrator, 90 days by default).

**To open the Data Quality Dashboard**

- On the navigation pane, go to **Governance** > **Quality metrics**.

    ![data-quality-dashboard-overview.png]({{ "/assets/images/governance/data-quality-dashboard/data-quality-dashboard-overview.png" | relative_url }})

The dashboard is organized into four tabs:

- **Overview** – each of the six data quality metrics as an overall, organization-wide score, plus their trend over time.
- **Business Domain** – the [Quality by Business Domain](#quality-by-business-domain) heatmap.
- **Source** – the [Quality by Source](#quality-by-source) breakdown.
- **AI Agent** – the [Quality by AI Agent](#quality-by-ai-agent) summary.

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

## Data quality for a Stream

Each [Stream](/consume/streams/concept-of-a-stream) also has its own **Data Quality** tab, which shows the same data quality metrics scoped to that stream's own business domain. For details, see [View stream details](/consume/streams/manage-streams#view-stream-details).
