---
layout: cluedin
title: Queues in CluedIn
parent: PaaS operations
permalink: paas-operations/queues-in-cluedin
nav_order: 14
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about the queue-based service bus architecture used by CluedIn and find a complete list of queues involved in its operations.

## Introduction

Queues are central to how CluedIn operates. Each operation or record in CluedIn is represented as a message in a queue. This design means that to truly understand how CluedIn functions under the hood, you need to understand how these queues behave.

Some of these queues are visible directly in the CluedIn UI—for example, on the **Monitoring** tab of a data set or within the **Processing Pipeline** section in **Engine Room**. For customers running CluedIn in a self-managed environment, a great deal of insight can be gained simply by observing the state of these queues.

You might ask questions like:

- How many messages are currently in a queue?
    
- How many consumers are connected to a given queue?
    
- Are there any dead-letter messages?

**Why CluedIn uses a service bus instead of an event log?**

A common question is: why did CluedIn adopt a queue-based service bus architecture (e.g., RabbitMQ) instead of a log-based event-driven system (e.g., Kafka)? The answer lies in a combination of **operational simplicity**, **data safety**, and **reliability**.

While both approaches are valid and widely used in modern architectures, event-driven platforms like Kafka come with added complexity—especially in areas like infrastructure (e.g., managing Zookeeper), monitoring, and tracing data lineage. They also follow a different philosophy: Kafka acts more like a distributed commit log where messages are retained for a period and can be replayed, while RabbitMQ uses a work queue model where messages are consumed and removed.

CluedIn made an early architectural decision to use a **service bus** and an [actor model](https://en.wikipedia.org/wiki/Actor_model). This approach provided a few key advantages:

- **Easier traceability** – it's more straightforward to track "who did what and when" in a service bus pattern.
    
- **Durability** – messages in CluedIn are stored on disk, so even if a service crashes or is restarted (even abruptly), the messages remain intact, virtually eliminating the risk of data loss.
    
- **Snapshotting and recovery** – the queue-based model makes it easier to pause, inspect, or recover processing flows.
    
- **Operational resilience** – RabbitMQ offers robust support for acknowledgment, retries, and dead-lettering, which are vital for maintaining a healthy pipeline under load.
    
After years of investment in this architecture, we’ve reached a point where CluedIn’s pipeline is **stable, performant, and resilient**, even under heavy record volumes. This is why we don’t anticipate major architectural changes to this part of the system in the near future.

## Source queues

The source queues are used for data ingestion in CluedIn.

### General ingestion queues

The following queues are not linked to a specific data source. They are cross-source queues, primarily used for service-to-service communication and to enable asynchronous execution of long-running jobs.

| Name | Queue name | Purpose | Error handling |
| --- | --- | --- | --- |
| Ingestion Data Set | `ingestion-data-set` | General-purpose queue used to ingest records from all source types (files, endpoints, databases, and so on). | If a failure occurs, the data source is set to an error state, and a message is displayed in the UI. |
| Commit Data Set | `commit-data-set` | General-purpose queue used to initiate processing of a source of any type. | In case of an error, the message is retried after 30 seconds; errors are logged in the logs. |
| File Recovery Queue | `file-recovery` | Used when a file upload fails during processing. Upon pod restart, a recovery message is sent to retry parsing/loading the file. | If recovery fails, the data source is set to an error state, and the error is visible in the UI. |
| Cloning Data Set Queue | `cloning-data-set` | Instructs the system to set a source in edit mode and clone the data; can also revert the data set to its original state. | In case of an error, it is logged in the data set logs and chunk loading may fail. |
| Source Operation Queue | `operation-data-set` | Stores all jobs related to operations on a data set, especially actions performed in edit mode. | If a failure occurs, the error is logged. |
| Source Anomaly Detection | `profiling-anomaly-detection-job` | Verifies if ingestions are in a correct state, attempts self-healing, and triggers alerts if needed. | If a failure occurs, the error is logged, and the message is moved to the dead letter queue after 5 attempts. |
| Source Anomaly Detection Dead Letter | `profiling-anomaly-detection-job_dead_letter` | Stores messages that failed after 5 retry attempts in the anomaly detection queue. | If moved back manually to `profiling-anomaly-detection-job`, the job will be retried. |
| Source Key Metrics Queue | `profiling-ingestion-metrics` | Scheduled job that collects key ingestion metrics. | Retries up to 5 times; if a failure occurs, the message is stored in the dedicated dead letter queue; the dead letter queue also serves as a log for critical failures. Messages can be manually retried. |
| Source Key Metrics Dead Letter Queue | `profiling-ingestion-metrics_dead_letter` | Stores messages that failed after 5 retry attempts in the key metrics queue. | Moving the message back to `profiling-ingestion-metrics` will retry the job. |
| Duplicate Check | `profiling-duplicate-check-job` | Scheduled job to detect duplicate records based on identifiers. | After 5 retries, the message is moved to the `profiling-duplicate-check-job_dead_letter` queue. |
| Duplicate Check Dead-Letter Queue | `profiling-duplicate-check-job_dead_letter` | Backup queue for messages that failed duplicate checks. | Messages can be manually moved back to `profiling-duplicate-check-job` to retry. |
| Exporter Queue | `exporter` | Sends export information to consumers. | If a failure occurs, the message is rejected, and an error is logged. |

### Dedicated ingestion queues

The following queues are dedicated to individual data sources. Depending on the source type and the actions performed, a separate set of queues may be created for each source.

| Name | Queue name | Purpose | Error handling |
| --- | --- | --- | --- |
| Source Mapping Queue | `clue_datasource_submit_[datasetId]` | Receives JSON data and applies mapping to transform it into a clue. | If mapping fails, an error log is added to the data set logs in the UI. |
| Source Processing Queue | `clue_datasource_process_[datasetId]` | Sends clues to the data processing pipelines. | In case of an error, logs are generated, and a **Retry** button appears on the **Process** tab of the data set. |
| Source Error Processing Queue | `clue_datasource_process_[datasetId]_error` | Stores clues that failed during processing. | Temporarily stores clues that could not be successfully sent. |
| Manual Data Entry Mapping Queue | `clue_manual_entry_submit_[manualProjectId]` | Receives user-entered data and transforms it into clues. | If mapping fails, an error log is added to the logs in the UI. |
| Manual Data Entry Processing Queue | `clue_manual_entry_process_[manualProjectId]` | Sends manually entered clues to the data pipelines. | In case of an error, logs are generated and a **Retry** button appears on the **Process** tab of the data set. |
| Manual Data Entry Error Processing Queue | `clue_manual_entry_process_[manualProjectId]_error` | Stores clues that failed during manual data entry processing. | Temporarily stores clues that could not be successfully sent. |
| Quarantine Mapping Queue | `source_mapping_quarantine_[sourceId]` | Reverse maps clues for approval validation before resending them to the quarantine processing queue. | In case of an error, a log message is shown in the UI. |
| Quarantine Processing Queue | `source_process_quarantine_[sourceId]` | Sends approved or quarantined clues to the data processing pipeline. | In case of an error, logs are generated, and a **Retry** button appears on the **Process** tab of the data set. |
| Quarantine Error Processing Queue | `source_process_quarantine_[sourceId]_error` | Stores clues that failed during quarantine processing. | Temporarily stores clues that could not be successfully sent. |
| Source Failed Loading Queue | `dataset_failed_elastic_search_bulk_[datasetId]` | Stores failed chunks when saving records to Elasticsearch. | If a failure occurs, a **Retry** button is shown in the UI. |
| Manual Data Entry Failed Loading Queue | `manual-data-entry-session_failed_elastic_search_bulk_[manualProjectId]` | Stores failed chunks when saving manually entered records to Elasticsearch. | If a failure occurs, a **Retry** button is shown in the UI. |

## Data pipeline queues

### Clue processing queues

| Name | Queue name | Purpose | Error handling |
| --- | --- | --- | --- |
| Default Clue Processing | `CluedIn.Core.Messages.Processing.IProcessingCommand`, `CluedIn.Core_CluedIn_Clues` | General clue data ingestion. | [Default processing error handling](#processing-error-handling-queues) |
| High Priority Clue Processing | `CluedIn.Core.Messages.Processing.ProcessPrioritizedClueCommand`, `CluedIn.Core_CluedIn` | Prioritized clue ingestion. | [Default processing error handling](#processing-error-handling-queues) |
| Big Clue Processing | `CluedIn.Core.Messages.Processing.ProcessBigClueCommand`, `CluedIn.Core_CluedIn` | Clues with raw byte size larger than 500 KB threshold to be executed with less concurrency. | [Default processing error handling](#processing-error-handling-queues) |
| Low Priority Clue Processing | `CluedIn.Core.Messages.Processing.ProcessLowPriorityClueCommand`, `CluedIn.Core_CluedIn` | Clue data ingestion by low priority crawling jobs. | [Default processing error handling](#processing-error-handling-queues) |

### Edge processing queue

| Name | Queue name | Purpose | Error handling |
| --- | --- | --- | --- |
| Edge Processing Queue | `CluedIn.Core.Messages.Processing.ProcessEdgesCommand`, `CluedIn.Core_CluedIn` | Resolves edges and creates shadow entities for missing reference points. | [Default processing error handling](#processing-error-handling-queues) |
| Parent Processing Queue | `CluedIn.Core.Messages.Processing.ParentsProcessingCommand`, `CluedIn.Core_CluedIn_ParentIds` | Old queue, disabled by default. | [Default processing error handling](#processing-error-handling-queues) |

### Metrics processing queue

| Name | Queue name | Purpose | Error handling |
| --- | --- | --- | --- |
| Entity Metrics Queue | `CluedIn.Core.Messages.Processing.Metrics.ProcessEntityMetricsCommand`, `CluedIn.Core_CluedIn` | Calculates entity level metric values. | [Default processing error handling](#processing-error-handling-queues) |
| Global Metrics Queue | `CluedIn.Core.Messages.Processing.Metrics.ProcessGlobalMetricsCommand`, `CluedIn.Core_CluedIn` | Scheduled job to calculate global dimension metric values. | [Default processing error handling](#processing-error-handling-queues) |
| Archive Metrics Queue | `CluedIn.Core.Messages.Processing.Metrics.ArchiveMetricsValuesCommand`, `CluedIn.Core_CluedIn` | Creates history of entity level metric values. | [Default processing error handling](#processing-error-handling-queues) |

### Commands queue

| Name | Queue name | Purpose | Error handling |
| --- | --- | --- | --- |
| Deduplicate Entity | `CluedIn.Core.Messages.Processing.DeduplicateEntityCommand`, `CluedIn.Core_CluedIn` | Deduplicates entity by overlapping entity codes or any enabled fuzzy matchers. | [Default processing error handling](#processing-error-handling-queues) |
| Anonymise | `CluedIn.Core.Messages.Processing.AnonymiseDataCommand`, `CluedIn.Core_CluedIn` | Anonymizes entity data processing. | [Default processing error handling](#processing-error-handling-queues) |
| Mesh Commands | `CluedIn.Core.Messages.Processing.MeshDataCommand`, `CluedIn.Core_CluedIn` | Mesh command execution from mesh center. | [Default processing error handling](#processing-error-handling-queues) |
| Delete Entity | `CluedIn.Core.Messages.Processing.DeleteEntityCommand`, `CluedIn.Core_CluedIn` | Deletion of entities. | [Default processing error handling](#processing-error-handling-queues) |
| Merge Entity | `CluedIn.Core.Messages.Processing.MergeEntitiesCommand`, `CluedIn.Core_CluedIn` | Merging of multiple entities and single entity, either by automatic entity deduplication or manual merging. | [Default processing error handling](#processing-error-handling-queues) |
| Deduplicate | `CluedIn.Core.Messages.Processing.DeduplicateCommand`, `CluedIn.Core_CluedIn` | Used for background admin job to execute entity deduplication for all entities or by a specific business domain. | [Default processing error handling](#processing-error-handling-queues) |
| Remove From Processing | `CluedIn.Core.Messages.Processing.RemoveFromProcessingDataCommand`, `CluedIn.Core_CluedIn` | Mesh command to mark entities as removed from processing. | [Default processing error handling](#processing-error-handling-queues) |
| Split Entity | `CluedIn.Core.Messages.Processing.SplitEntityCommand`, `CluedIn.Core_CluedIn` | Re-evaluates entity code overlap and fuzzy matching overlap of records inside an entity and splits entity into several golden records if required. | [Default processing error handling](#processing-error-handling-queues) |
| Ensure No Entity Code Overlap | `CluedIn.Core.Messages.Processing.EnsureNoDuplicatedEntitiesForEntityCodesCommand`, `CluedIn.Core_CluedIn` | Variant of Deduplicate Entity triggered by clue ingestion to validate if deduplication is needed. | [Default processing error handling](#processing-error-handling-queues) |
| Send Mail | `CluedIn.Core.Messages.SendMailCommand`, `CluedIn.Core_CluedIn` | Used to send emails to users. | [Default processing error handling](#processing-error-handling-queues) |

### Enricher queue

| Name | Queue name | Purpose | Error handling |
| --- | --- | --- | --- |
| Entity Enrichment Queue | `CluedIn.ExternalSearch.ExternalSearchCommand`, `CluedIn.ExternalSearch_CluedIn` | Performs enrichment for an entity. | [Default processing error handling](#processing-error-handling-queues) |
| Public Enricher Queue | `CluedIn.PublicApi.PublicApiEnrichmentCommand`, `CluedIn.PublicApi_CluedIn` | Performs async enrichment of data submitted via the public API endpoint to enrich arbitrary data that is not ingested into CluedIn. | [Default processing error handling](#processing-error-handling-queues) |

### Processing retry handling

| Name | Queue name | Purpose | Error handling |
|--|--|--|--|
| Dedicated Retry Queue | `CluedIn.Core.Messages.Processing.RetryCommand`, `CluedIn.Core_CluedIn` | Used when in-queue retry exceeds threshold (default 2) retry count. Messages will be serialized in fashion to avoid concurrency of processing the same subject at the same time. | In-queue retry until max retry count is reached, then message is sent to dead letter. |

### Processing error handling queues

Default processing error handling goes through the following steps:

 - In-place "fast" retry with exponential backoff (default 3 attempts).

 - In-queue retry – commands erroring due to transient error will be re-queued to the same queue (default 10 times for general transient errors, default 30 times for database concurrency errors).

 - Dedicated retry queue – once in-queue retry attempts have reached threshold (default after 2 retry attempts), the message is routed to dedicated retry queue that will be serialized in a fashion to avoid concurrent processing of the same records.

 - When all retries have been exhausted, the message is sent to the dead-letter queue.

| Name | Queue name | Purpose | Error handling |
|--|--|--|--|
| Processing Dead-Letter Queue | `DeadLetterCommands` | Contains processing dead-letter messages when all reties have been exhausted. | Messages can be retried by moving them to `CluedIn.Core.Messages.Processing.DeadLetterCommand, CluedIn.Core_CluedIn_Retry`. |
| Recoverable Dead-Letter Queue | `CluedIn_DeadLetterMessages_Recoverable` | Contains messages that were dead-lettered due to identified transient error. | Messages can be retried by moving them to `CluedIn_DeadLetterMessages_Retry`. |
| Non-Recoverable Dead-Letter Queue | `CluedIn_DeadLetterMessages_NonRecoverable` | Contains messages that was dead-lettered due to non-transient error. | Messages can be retried by moving them to `CluedIn_DeadLetterMessages_Retry`. | 
| Retry Dead-Letter Processing Command Queue | `CluedIn.Core.Messages.Processing.DeadLetterCommand`, `CluedIn.Core_CluedIn_Retry` | Re-queues processing commands to be retried. | N/A |
| Retry Dead-Letter Command Qqueue | `CluedIn_DeadLetterMessages_Retry` | Re-queues generic commands to be retried. | N/A |

## Stream queues

| Name | Queue name | Purpose | Error handling |
| --- | --- | --- | --- |
| StreamControlCommands Queue | `StreamControlCommands` | Used for stream maintenance and state change. | [Default stream error handling](#stream-error-handling-queues) |
| Stream Subscribe Queue | `StreamSubscriber_[streamId]` | Receives messages containing entities to be handled by the stream. | [Default stream error handling](#stream-error-handling-queues) |
| Stream Events Queue | `StreamEvents_[machinename]` | Used for managing control events such as start, stop and pause. | [Default stream error handling](#stream-error-handling-queues) |

### Stream error handling queues

Stream error handling is similar to [processing error handling](#processing-error-handling-queues) and goes through the following steps:

- In-place "fast" retry with exponential backoff (default 3 attempts).

- In-queue retry – commands erroring due to transient error will be re-queued to the same queue (default 10 times for general transient errors, default 30 times for database concurrency errors).

- When all retries have been exhausted, the message is sent to the dead-letter queue.

| Name | Queue name | Purpose | Error handling |
|--|--|--|--|
| Stream Dead-Letter Queue | `StreamSubscriber-deadLetter-[streamid]` | Dead-etter queue for stream. | Messages can be moved to retry queue or admin Web API can be used to retry messages. |

## Distributed jobs subsystem queues

| Name | Queue name | Purpose | Error handling |
|--|--|--|--|
| Distributed Job Control Queue | `CluedIn.DistributedJobs.Commands.IDistributedJobsControlCommand`, `CluedIn.DistributedJobs_DistributedJobQueueManager` | Used by distributed jobs subsystem to handle job lifecycle events, | In-place retry; otherwise, always use non-recoverable dead-letter queue (except for completion callback commands). |
| Distributed Job Queue | `DistributedJob_[job id]` | Created per job and removed when job is done. Used to store and process job-specific work item commands. | Perform in-place retry, then silently drop command if cannot process after all tries. |

## Robust callback subsystem queue

| Name | Queue name | Purpose | Error handling |
|--|--|--|--|
| Robust Callbacks Queue | `CluedIn.Processing.RobustCallback.RobustCallbackCommand`, `CluedIn.Processing_CluedIn` | Used to store and process robust callbacks.  | Default robust messaging error handling. |

## Remote events

| Name | Queue name | Purpose | Error handling |
|--|--|--|--|
| Remove Events Queue | `RemoteEvents_[machinename]` | Synchronizes events between machines. | N/A |