---
layout: cluedin
title: Built-in AI agents
parent: AI agents
grand_parent: Govern & improve
nav_order: 20
permalink: /govern/ai-agents/built-in-ai-agents
content_type: reference
redirect_from: ["/management/ai-agents/built-in-ai-agents"]
source_path: docs/080-management/ai-agents/020-built-in-ai-agents.md
tags: ["management", "ai agents", "built-in ai agents"]
---

# On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about the built-in AI agents that are available in CluedIn by default and how you can use them to automate key data management tasks, improve data quality, and streamline your data governance efforts.

The built-in AI agents include preconfigured [jobs](/govern/ai-agents/create-configure-and-run-an-ai-agent#configure-an-ai-agent-job). You only need to specify a set of golden records the agent should work with.

CluedIn provides three built-in AI agents—Data Steward, Data Architect, and Setup Advisor.

![AI agents page listing agents with description, active jobs, cost and author, including the built-in Data Architect and Data Steward agents]({{ "/assets/images/management/ai-agents/built-in-ai-agents/builtin_agents_sp.png" | relative_url }})


## Data Steward

The Data Steward AI agent ensures data quality, accuracy, and compliance. By default, this agent has the following tasks:

- Fix data quality issues – analyzes a data source and suggests improvements to enhance data accuracy and consistency.

- Look for duplicates – scans the data source for potential duplicate records and groups them into a deduplication project for further review.

## Data Architect

The Data Architect AI agent designs and implements the technical blueprint for your organization's data infrastructure. It ensures that data is accessible, reliable, and secure. By default, this agent has the following task:

- Create rules – evaluates the data source and recommends potential data quality rules that can be applied to maintain standards over time.

## Setup Advisor

The Setup Advisor AI agent reviews your organization's account setup and proposes safe improvements, so a new account does not stay unconfigured or undocumented. Unlike Data Steward and Data Architect, it does not work against a data source you choose — it reviews your organization as a whole on demand. By default, it reviews:

- Missing descriptions – proposes a description for any rule, glossary term, or stream that doesn't have one yet, generated from the item's own name and configuration.

- Data quality thresholds – proposes a minimum acceptable score for any [data quality metric](/govern/data-quality-dashboard) that has no threshold configured yet.

- AI spend limits – proposes a daily and monthly AI spend limit for an organization that hasn't set either.

Every proposal from Setup Advisor is a suggestion, not an automatic change: review and approve or reject each one the same way as [any other AI agent's results](/govern/ai-agents/review-the-results-returned-by-an-ai-agent) before it takes effect.