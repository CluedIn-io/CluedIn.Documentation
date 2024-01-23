---
layout: cluedin
title: Agent Jobs
parent: Development
nav_order: 480
permalink: /developer/agent-jobs
tags: ["development","agents","jobs"]
---

Your user interface will show you a list of the jobs that are running, have run and are scheduled to run within the platform. You can drill into the information on an individual job to see more details. 

A design is missing for the Job Details.

[HttpGet]
[Route("api/v1/jobs")]

This call will return 5 counts for the dashboard including completed, executing, failed, queued, cancelled.

[HttpGet]
[Route("api/v1/jobs")]
int page, int take, string state = null, Guid? configurationId = null

You can page through all jobs with all states or you can filter by State and Congifuration Id (AKA ProviderDefinitionId)

e.g. State can be one of the following:
```csharp

Unknown ,

    /// <summary>The queued job state</summary>
    Queued                 ,

    /// <summary>The executing job state</summary>
    Executing              ,

    /// <summary>The execution completed</summary>
    ExecutionCompleted      ,

    /// <summary>The cancelling job state</summary>
    Cancelling              ,

    /// <summary>The submitting job state</summary>
    Submitting              ,

    /// <summary>The completed job state</summary>
    Completed               ,

    /// <summary>The cancelled job state</summary>
    Cancelled               ,

    /// <summary>The failed job state.</summary>
    Failed   
```
               
[HttpGet]
[Route("api/v1/jobrun")]
id

To call this you pass in the Job Id (that you have from the previous calls) and it will show you the details of the Job. There is LOTS of details here that will look nice in a UI.

```
[Id]
,[JobId]
,[AgentId]
,[AgentKey]
,[UpdateDate]
,[AgentResultIsSuccess]
,[AgentResultIsCancellationRequested]
,[AgentResultMessage]
,[AgentState]
,[AgentQueuedDate]
,[AgentStartTime]
,[AgentEndTime]
,[AgentElapsedQueuedTime]
,[AgentElapsedExecutionTime]
,[AgentPercentCompleted]
,[AgentLastSubmittedDate]
,[AgentExpectedTasksCount]
,[AgentTasksCount]
,[AgentTasksQueuedCount]
,[AgentTasksCompletedCount]
,[AgentTasksFailedCount]
,[AgentCluesCount]
,[AgentCluesQueuedCount]
,[AgentCluesCompletedCount]
,[AgentCluesFailedCount]
,[ProcessingState]
,[ProcessingQueuedDate]
,[ProcessingStartTime]
,[ProcessingEndTime]
,[ProcessingTasksCount]
,[ProcessingTasksQueuedCount]
,[ProcessingTasksCompletedCount]
,[ProcessingTasksFailedCount]
,[ProcessingTasksSkippedCount]
,[ProcessingTaskRetriesCount]
,[ProcessingTasksAlreadyExistsCount]
,[ProcessingTasksAlreadyUpToDateCount]
,[ProcessingTasksIgnoredCount]
,[ProcessingTasksReceivedPayloadsCount]
,[ProcessingTasksReceivedCluesCount]
,[ProcessingTasksReceivedLogLinesCount]
,[ProcessingUpdatedDate]
```

[HttpGet]
[Route("api/v1/jobs/executing")]

This will get you JUST the executing jobs. The idea being that if you are wanting to show the executing jobs in a place like this: