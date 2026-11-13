---
layout: cluedin
title: Run Clean, deduplication, and enrichment tools from an AI agent
parent: AI agents
grand_parent: Govern & improve
nav_order: 70
permalink: /govern/ai-agents/run-tools-from-an-ai-agent
content_type: how-to
tags: ["management", "ai agents", "tools", "clean", "deduplication", "enrichment"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Tools** tab on an AI agent's page lists existing platform capabilities - [CluedIn Clean](/govern/cleaning) (powered by OpenRefine), [deduplication projects](/master/deduplication), and [enrichers](/govern/enrichment) - that you can ask the agent to run directly from its chat, instead of opening each feature's own page.

## Prerequisites

- The agent chat is available for your organization. If the **Tools** tab is not visible on the agent's page, the agent chat is not enabled; contact your CluedIn administrator.
- At least one clean project, deduplication project, or configured enricher already exists for the tool you want to run. The **Tools** tab does not create one.
- Edit-level access to the tool you want to run: **Clean** projects, **Deduplication** project management, or **Enrichment**. Running a clean project or an enricher you don't own needs the same elevated (Accountable, for Clean) or Consultant-level access the equivalent page itself requires from a non-owner.

## Run a tool from the Tools tab

1. On the navigation pane, go to **AI Agents** (or, **Management** > **AI Agents**).

1. Select the AI agent you want to use.

1. Select the **Tools** tab.

    Each tool - **CluedIn Clean**, **Deduplication Projects**, and **Enrichers** - shows a status badge:

    - **Available** - you have access, and at least one project or enricher is configured.
    - **Unavailable - you don't have permission to use this tool** - ask your administrator for edit-level access to that tool.
    - **Unavailable - nothing is configured yet** - create a clean project, deduplication project, or enricher first, using the **View all** link.

    ![The Tools tab of an AI agent, listing CluedIn Clean, Deduplication Projects, and Enrichers, each showing an Unavailable - nothing is configured yet badge]({{ "/assets/images/management/ai-agents/run-tools-from-an-ai-agent/tools_tab.png" | relative_url }})

1. Under the tool you want to use, find the project or enricher in the list, and select **Run via agent**.

    {:.important}
    Only the 5 most recent items per tool are listed. Select **View all** to open the tool's own page and find an older one.

1. Confirm the action.

    The agent's chat panel opens, and the request - naming the project or enricher - is sent automatically. The agent runs the corresponding action and replies in the chat confirming what it ran, or explaining why it could not.

## Verify the result

- The chat panel shows your request as a sent message, followed by the agent's reply confirming the action (for example, that it started generating results for a clean project, or triggered an enrichment job) or explaining why it failed.
- The reply includes a link back to the clean project, deduplication project, or enricher, where you can see its own progress and results the same way as if you had run it from its own page.

## What this changes

- Running a tool through the agent performs the same action as running it from the tool's own page - the same backend service, the same audit log entry, and the same permission checks.
- **CluedIn Clean**: the agent moves the clean project into (re-)generation, the same as selecting **Generate Results** on the project itself.
- **Deduplication Projects**: the agent generates matching results for the project, the same as selecting **Generate Results** on the project itself.
- **Enrichers**: the agent starts an enrichment job for the records the enricher is configured to search, the same as triggering it from the **Enrich** page. Only one enrichment job per enricher can run at a time.
- None of these actions require a separate approval step when run through the agent - this is why running a tool you don't own needs the higher permission level described in [Prerequisites](#prerequisites).

## If something goes wrong

- **The Tools tab is not available.** The agent chat is not enabled for your organization. Contact your CluedIn administrator.
- **A tool shows "Unavailable - you don't have permission to use this tool."** You need edit-level access to that tool. Contact your CluedIn administrator.
- **A tool shows "Unavailable - nothing is configured yet."** Select **View all** and create a clean project, deduplication project, or enricher first.
- **The agent replies with an error naming a permission issue.** You have enough access to see the tool as Available, but not enough to run it on a project or enricher you don't own. Ask the project or enricher's owner to run it, or ask for Accountable-level (Clean) or Consultant-level (Enrichment) access.
- **The agent replies that an enrichment job is already running.** Only one job per enricher runs at a time. Wait for the current job to finish, then try again.
