---
layout: cluedin
title: Events
parent: Development
nav_order: 100
has_children: false
permalink: development/events
tags: ["development","events"]
published: false
---


There are many events that occur within CluedIn while data is being ingested and processed. These Events are made available to you as a developer to interact with. 

Here are some of the events that you can hook into:

```csharp
AgentJobAbandonEvent
AgentJobCrawlingFinishedEvent
AgentJobEnqueuedEvent
AgentJobFinishedEvent
AgentJobQueueEvent
AgentJobSentToAgentEvent
AgentJobStateChangedEvent
AgentJobStatusUpdatedEvent
AgentPingEvent
AgentRegistrationEvent
AgentRegistrationEventType
ProcessingJobFinishedEvent
ProcessingJobStartedEvent
ProcessingJobStatusUpdatedEvent
WorkflowEvent
WorkflowFailedEvent
WorkflowFinishedEvent
WorkflowStartedEvent
```

In your code, you can subscribe to one of these events.