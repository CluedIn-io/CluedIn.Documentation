---
title: AI agents
url: https://documentation.cluedin.net/govern/ai-agents
content_type: landing
section: Govern & improve
---

# AI agents

The **AI Agents** module in CluedIn is a smart automation component that uses artificial intelligence to assist with key data management tasks.

![AI agents page listing agents such as Financial Data Steward and Team Leader, with columns for Description, Active, Requires review, Cost, Author, and Created at](https://documentation.cluedin.net/assets/images/management/ai-agents/ai-agents/ai_agents_module.png)

The module helps create business rules, find and resolve data quality issues, and find potential duplicates with minimal manual effort. This enables you to focus on strategic decisions rather than repetitive tasks, while ensuring higher data consistency and reliability.

_Video coming soon_

This section covers the module itself: setting up, running and reviewing an agent. When an agent does a task that has its own home in the documentation, the article for that task lives there. For example, [Onboard datasets with an AI agent](https://documentation.cluedin.net/ingest/mapping/onboard-datasets-with-an-ai-agent.md) is part of Mapping.

## Copilot experience for AI agents

AI agents include an embedded **Copilot experience** that helps you set up and work with an agent through natural conversation.

Instead of configuring every part of an agent manually, you can describe the outcome you want and use the Copilot pane to help build the configuration step by step.

For example, you can ask the agent to:

- Identify the data it should work on.
- Suggest or create jobs for a particular data-management task.
- Configure how the agent should analyze or change the data.
- Explain what additional information or settings are required.
- Help refine the agent configuration before it is run.
- Review the outcome of previous jobs and decide what to do next.

This makes agent setup more accessible for users who understand the business outcome they want but do not want to configure every technical detail themselves.

The Copilot experience is contextual to the agent you are working with. It can use the agent's current configuration, available jobs, and relevant CluedIn context to guide the conversation.

> **Important:** To use the Copilot experience, the Copilot model deployment must be configured correctly. If the deployment setting is missing, CluedIn will prompt you to open the Copilot settings and complete the configuration.

### Use natural language to configure an agent

You can use conversational instructions to describe the job you want the agent to perform.

For example:

```
Create a job that finds customer records with missing websites and enriches them where possible.
```

Or:

```
Analyze newly ingested Product data, identify the most important data quality issues, and create jobs to resolve them.
```

The Copilot can then help translate that intent into the agent configuration and jobs required to perform the work.

This allows the configuration process to become iterative: you can ask questions, refine the scope, test the resulting jobs, and adjust the agent through conversation.

## Event-driven and proactive agents

AI agents do not have to rely only on a user opening the agent and manually starting a job.

Agents can also be triggered by **internal CluedIn events**, allowing them to react proactively when something important happens in the platform.

For example, an agent can react to an event such as:

> New data sources have arrived.

When this type of event occurs, the agent can proactively begin the appropriate workflow—for example:

- Inspect the newly arrived data.
- Profile the data and identify data quality issues.
- Suggest or create mappings.
- Detect duplicate candidates.
- Create cleaning or remediation jobs.
- Apply validation logic.
- Prepare follow-up work for review or approval.

This event-driven model allows agents to behave more like ongoing data-management workers rather than one-off AI tools.

Instead of waiting for a user to notice that new data has arrived and decide what to do next, an agent can respond to the event and start the relevant analysis automatically.

### Combine events with human review

An event-triggered agent can still include human checkpoints.

For example, an agent could:

1. Detect that a new data source has arrived.
2. Analyze the data and prepare recommended mappings.
3. Create a test job.
4. Present the proposed changes for review.
5. Continue only after the results are approved.

This makes it possible to combine proactive automation with governance and human oversight.

### Example scenario

Suppose a new supplier data source is added to CluedIn.

An agent could be configured to respond by:

1. Detecting the new source.
2. Describing and profiling the data.
3. Comparing the data with existing Supplier and Company business domains.
4. Suggesting mappings.
5. Checking for duplicate suppliers.
6. Creating data-quality jobs for missing or invalid values.
7. Presenting the proposed actions to a data steward.

The goal is to reduce the amount of manual coordination required after common platform events while still allowing users to review and control important changes.

This section covers the following areas:

- [Prerequisites to using AI agents](https://documentation.cluedin.net/govern/ai-agents/prerequisites-to-using-ai-agents.md) – perform the necessary setup to enable the AI agents functionality.

- [Using built-in AI agents](https://documentation.cluedin.net/govern/ai-agents/built-in-ai-agents.md) – learn about CluedIn's built-in AI agents that contain templates for handling common data management tasks.

- [Creating and configuring an AI agent](https://documentation.cluedin.net/govern/ai-agents/create-configure-and-run-an-ai-agent.md) – learn how to create, configure, and run an AI agent tailored to your specific business needs.

- [Onboarding datasets with an AI agent](https://documentation.cluedin.net/ingest/mapping/onboard-datasets-with-an-ai-agent.md) – learn how to ask an AI agent to plan how your datasets map to business domains, vocabularies, and vocabulary keys, review and change the plan, and create everything once you approve it.

- [Reviewing the results returned by an AI agent](https://documentation.cluedin.net/govern/ai-agents/review-the-results-returned-by-an-ai-agent.md) – learn how to interpret, validate, and take action based on the outputs generated by AI agents.

- [Viewing and reverting changes made by an AI agent](https://documentation.cluedin.net/govern/ai-agents/view-and-revert-changes-made-by-ai-agent.md) – learn how to view the historical record of the changes made by an AI agent and, if needed, revert any of the changes.

- [AI agents FAQs](https://documentation.cluedin.net/govern/ai-agents/ai-agents-faqs.md) – find answers to common questions related to AI agents.

## In this section

- [Prerequisites to using AI agents](https://documentation.cluedin.net/govern/ai-agents/prerequisites-to-using-ai-agents.md) (reference): In this article, you will learn about the steps required to start using the AI agents in CluedIn.
- [Built-in AI agents](https://documentation.cluedin.net/govern/ai-agents/built-in-ai-agents.md) (reference): In this article, you will learn about the built-in AI agents that are available in CluedIn by default and how you can use them to automate key data management tasks, improve data quality, and streamline your data gove...
- [Create, configure, and run an AI agent](https://documentation.cluedin.net/govern/ai-agents/create-configure-and-run-an-ai-agent.md) (how-to): Create an AI agent when you want CluedIn to analyze a set of golden records and suggest changes for a specific task, such as fixing data quality issues, finding duplicates, or creating rules.
- [Review the results returned by AI agent](https://documentation.cluedin.net/govern/ai-agents/review-the-results-returned-by-an-ai-agent.md) (how-to): AI agents examine incoming data and provide suggestions based on configured prompts.
- [View and revert changes made by AI agent](https://documentation.cluedin.net/govern/ai-agents/view-and-revert-changes-made-by-ai-agent.md) (how-to): All changes that an AI agent makes to golden records are recorded for further review.
- [AI agents FAQs](https://documentation.cluedin.net/govern/ai-agents/ai-agents-faqs.md) (reference): This article addresses commonly asked questions about AI agents in CluedIn, including their setup, operation, and security controls.

Up: [Govern & improve](https://documentation.cluedin.net/govern.md)
