---
layout: cluedin
title: Commands
parent: Development
nav_order: 060
has_children: false
permalink: /development/commands
tags: ["development","commands"]
---

Commands are the messages in CluedIn that move through the processing pipeline. You can think of Commands like "events", in that they represent an action or a desire for an action to do a certain type of process in CluedIn.

 - DeduplicateCommand

This command will allow you to run a deduplicate process in bulk for an Organization, with the addtion of being able to filter by a particular Entity Type. 

You can invoke this command in the following way:

```csharp  
  var command = new DeduplicateCommand(null, new Guid("<Id of the Organization>"));

  executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - DeduplicateEntityCommand

This command will allow you to run a deduplicate process for any Entity, given the Id of the Entity. 

You can invoke this command in the following way:

```csharp  
    var command = new DeduplicateEntityCommand(null, new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"));

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```
 - DeleteEntityCommand

This command allows you to delete an Entity in full, including all history. Beware that this deletes all data parts and all references to this Entity.


```csharp  
    var command = new DeleteEntityCommand(null, new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"), null);

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - MergeEntitiesCommand

This command will allow you to force a merge on two or more entities. 

```csharp  
    var command = new MergeEntitiesCommand(null, new Guid("<Id of the Organization>"), new Guid[] { "<Guid1>", "<Guid1>"  } );

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ArchiveMetricsValuesCommand


This command is scheduled to run every 24 hours for you, but if you would like to force it, you can run the following code. This command will take all records that are stored in the detail EntityMetrics table and calculate them into an aggregation and move the metrics to the Archive table.

```csharp  
    var command = new ArchiveMetricsValuesCommand(new Guid("<Id of the Organization>"))
            {
                MetricId            = !string.IsNullOrEmpty(metricId) ? (Guid?)new Guid(metricId) : null,
                MetricDimensionType = !string.IsNullOrEmpty(metricDimensionType) ? (MetricDimensionType?)Enum.Parse(typeof(MetricDimensionType), metricDimensionType) : null
            };

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ProcessEntityMetricsCommand

This command allows you to reprocess an Entities metrics. This would be useful for when you are adding your own new data quality metrics and would like to test what score an entity would get.

```csharp  
     var command = new ProcessEntityMetricsCommand(new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"));

     executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ProcessGlobalMetricsCommand

This command is scheduled to run every 24 hours for you, but if you would like to force it, you can run the following code. This command will reprocess the Global Metrics that fuel the quality dashboards in the CluedIn user interface.


```csharp  
       var command = new ProcessGlobalMetricsCommand(new Guid("<Id of the Organization>"));

            executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ParentsProcessingCommand

This command will take an Entity and reprocess its parent to child relationships that are used in calculting the hierarchies of records in the graph.


```csharp  
     var command = new ParentsProcessingCommand(null, new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"), ParentProcessingDirection.Up);

     executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - PostProcessingEntityCommand

 This command allows you to run the inbuilt post processors of CluedIn. Post processing refers to the logic that runs after CluedIn has finished its default processing of a clue. 


```csharp  
     var command = new PostProcessingEntityCommand(null, new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"));

     executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ProcessBigClueCommand

This command is useful for when you know a Clue is big in size. This is typically useful for processing large binary files where you will know that there will be a lot of properties, content, entity codes and edges. This allows Clues to run on a different queue and not block smaller clues from being processed. 


```csharp  
    var command = new ProcessBigClueCommand(JobRunId.Empty, CompressedClue.Compress(clue, executionContext.ApplicationContext));

     executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ProcessEdgesCommand

 This command allows you to take an entity and process its edges. This is useful for when you have added, changed or removed logic around what edges should be on a Clue. 


```csharp  
    var command = new ProcessEdgesCommand(null, new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"));

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ProcessLowPriorityClueCommand

 This command allows you to process a Clue but assign a low priority to it over other processes that are happening in CluedIn. This is typically useful for running delta loads of data. 


```csharp  
    var command = new ProcessLowPriorityClueCommand(null, new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"));

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ProcessClueCommand

 This is the generic command for taking a Clue and processing it in CluedIn.


```csharp  
    var command = new ProcessClueCommand(null, new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"));

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ProcessPrioritizedClueCommand

 This command allows you to process a Clue but assign a high priority to it over other processes that are happening in CluedIn. This is typically useful for data that needs to be as real-time as possible.


```csharp  
    var command = new ProcessPrioritizedClueCommand(null, new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"));

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ProcessVersionHistoryCommand

This command allows you to take an Entity and reprocess all the history of that record. 


```csharp  
    var command = new ProcessVersionHistoryCommand(null, new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"));

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ProcessWebhookDataCommand

This command cannot be invoked from code, but can be used to listen to when you are processing a record where the origin came from a WebhookDataCommand.

 - WebhookDataCommand

This command allows you to invoke that a record has come through a webhook. This is not publicly exposed because CluedIn is the engine that invokes this command and it cannot be done outside of the CluedIn engine. 


 - RefreshEntityBlobCommand

 This command allows you to take a record and reprocess it and save back into all databases. 


 ```csharp  
    var command = new RefreshEntityBlobCommand(null, "<Insert an Entity Code>", new Guid("<Id of the Organization>"));

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ResyncEntityCommand

 This command will take a record from the CluedIn Primary store and make sure that all other stores have the same values. This can happen in certain situations where databases may get out of sync.


```csharp  
    var command = new ResyncEntityCommand(null, new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"), null);

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - SaveEntityCommand

This command allows you to take a Clue and save it directly into the database without any processing.

```csharp  
    var command     = new SaveEntityCommand(null, new Guid("<Id of the Organization>"), CompressedClue.Compress(clue, executionContext.ApplicationContext), "<Insert an Entity Code>");

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - SplitEntityCommand

This command allows you to take a record by its Entity Id and then split it by all of its history and reprocess it again. This is useful for times when you have introduced logic to ignore certain entity codes or you have changed the way that data needs to be processed. This is also useful for deleting individual parts of a record.  

```csharp  
    var command = new SplitEntityCommand(null, new Guid("<Id of the Organization>"), new Guid("<Id of the Entity>"), null);

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - ExternalSearchCommand

 This command allows you to trigger and external search given an entity that is already in CluedIn.


```csharp  
    var command = new ExternalSearchCommand(executionContext, new Guid("<Id of the Entity>"), entity.ProcessedData);

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```

 - PublicApiEnrichmentCommand


 This command allows you to enrich a record through CluedIn and get a callback with the result when it is finished.


```csharp  
    var command = new PublicApiEnrichmentCommand(executionContext, Guid.NewGuid(), "<HttpRequest>", "Your Callback Address", EnrichmentWebhookCallbackFormat.Json, "<EnrichmentWebhookCallbackSchema>");

    executionContext.ApplicationContext.System.Processing.SendCommand(command);
```