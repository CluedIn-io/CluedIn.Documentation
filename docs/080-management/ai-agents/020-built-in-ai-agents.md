---
layout: cluedin
title: Built-in AI agents
parent: AI agents
grand_parent: Management
nav_order: 020
permalink: /management/ai-agents/built-in-ai-agents
tags: ["management", "ai agents", "built-in ai agents"]
---

# On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about the built-in AI agents that are available in CluedIn by default and how you can use them to automate key data management tasks, improve data quality, and streamline your data governance efforts.

The built-in AI agents include preconfigured [jobs](/management/ai-agents/create-configure-and-run-an-ai-agent#configure-an-ai-agent-job). You only need to specify a set of golden records the agent should work with.

CluedIn provides two built-in AI agents—Data Steward and Data Architect.

![builtin_agents_sp.png]({{ "/assets/images/management/ai-agents/built-in-ai-agents/builtin_agents_sp.png" | relative_url }})


## Data Steward

The Data Steward AI agent ensures data quality, accuracy, and compliance. By default, this agent has the following tasks:

- Fix data quality issues – analyzes a data source and suggests improvements to enhance data accuracy and consistency.

- Look for duplicates – scans the data source for potential duplicate records and groups them into a deduplication project for further review.

## Data Architect

The Data Architect AI agent designs and implements the technical blueprint for your organization's data infrastructure. It ensures that data is accessible, reliable, and secure. By default, this agent has the following task:

- Create rules – evaluates the data source and recommends potential data quality rules that can be applied to maintain standards over time.