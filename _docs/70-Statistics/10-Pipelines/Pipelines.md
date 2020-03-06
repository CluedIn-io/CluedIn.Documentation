---
category: Statistics
title: Processing Pipelines
---

---

The processing pipelines in CluedIn can be described as a tree of different processing steps. Each processing step has dependencies on previous steps being run and hence you can conceptualise it as a dependency tree of processing steps.

# Statistics Sections
1. [Statistics Room Overview](/docs/70-Statistics/00-Intro/Statistics%20Room.html)
2. [Processing Pipelines](/docs/70-Statistics/10-Pipelines/Pipelines.html)
3. [Graph Database](/docs/70-Statistics/20-Graph/Graph.html)
4. [Search Database](/docs/70-Statistics/30-Search/Search.html)
5. [Relational Database](/docs/70-Statistics/40-Relational/Relational.html)
6. [Cache Database](/docs/70-Statistics/50-Cache/Cache.html)
7. [Configuration](/docs/70-Statistics/60-Configuration/Configuration.html)

The data here should help you monitor different flows through our system. 

Key things to look out for is memory usage, if the expected flow has messages going through the pipelines, and the incoming and outgoing speeds are not too low (might be a signal for a bottleneck).

# Overview

In the charts you can see the number of data points currently processing and the incoming and outgoing rates, updated once per second.

The current memory usage is used to gauge the general health of the system. It provides the currently used RAM, the maximum RAM, and a health alarm (color coded into the card as red or green).

# Pipeline Processes

This panel is accesible from the Actions section.

In the Pipeline Processes view we offer a visualisation grouping all the processors in our system, in a tree structure. Each node is either a group, or a Process.

The Process nodes can be clicked to reveal their properties:
- Process Name - Friendly/DisplayName
- Command Name - The name of the command that triggers this process
- Pipeline Name - The name of the Pipeline this process uses
- Description - A description of what this process is doing
- Incoming - The rate of incoming data points per second
- Messages - Current number of messages in this specific Pipeline
- Outgoing - The rate of outgoing data points per second

The data is updated once per second.

The Pipeline Processes are grouped as follows:

- Incoming - All processes found in this group relate to ingesting data into the application
    - Main Processes - All the processes that relate to the main Clue Processing, which is done after the initial data ingestion
- Webhooks - All processes relating to pulling and processing data from web hooks
- Events - All processes that are triggered by events (applying Governance over data, such as anonymisation)
- Errors - All processes relating to error processing and logging
- Outgoing - All processes relating to pushing data to an external source
- Metrics - All processes relating to the calculation of our different data metrics

# API

There are 2 endpoints that make up the Pipelines Overview, and the Pipelines Processes tree map.

### GET /api/statistics/pipelines/overview

#### Overview

| Property        | Type             | Description   |
|-----------------|------------------|---------------|
| Messages        | array of ints    | total number of messages currently in the pipelines  |
| Incoming        | array of floats  | rate of messages incoming into the pipelines |
| Outgoing        | array of floats  | rate of messages outgoing out of the pipelines |
| Memory          | integer          | the currently used RAM in bytes |
| MemoryLimit     | integer          | the maximum RAM usable |
| MemoryAlarm     | boolean          | status of memory usage |


The statistics provided are updated to their current values each time the endpoint is queried.

The first 3 keys provide arrays of max 10 values, and are used in making up our charts. Each time the endpoint is queried, a new point is added to these arrays. It is recommended to query once per second, so after the first 10 seconds, you will have a complete chart of the values of those statistics in the last 10 seconds. This timing can be slower as well, but it will also slow the update time on the memory value.

Example response:

```json
{
    "Messages": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ],
    "Incoming": [
        0.2,
        0.2,
        0.2,
        0.2,
        0.0,
        0.0,
        0.0,
        0.2,
        0.0,
        0.2,
        0.0
    ],
    "Outgoing": [
        0.2,
        0.2,
        0.2,
        0.2,
        0.0,
        0.0,
        0.0,
        0.2,
        0.0,
        0.2,
        0.0
    ],
    "Memory": 93736960,
    "MemoryLimit": 1651938099,
    "MemoryAlarm": false
}
```

### GET /api/statistics/pipelines/map

#### Node

| Property        | Type                | Description   |
|-----------------|------------------   |---------------|
| Name            | string              | which is the key |
| Description     | string              | short description |
| PipelineProcess | object              | null in case the node is a group / has children |
| Children        | dictionary of nodes | dictionary of nodes |

#### PipelineProcess

| Property        | Type             | Description   |
|-----------------|------------------|---------------|
| DisplayName     | string           | friendly name |
| CommandName     | string           | the name of the Command that triggers this Process |
| PipelineName    | string           | the name of the Pipeline this Process is using |
| Incoming        | float            | the rate of incoming messages into the Pipeline |
| Messages        | int              | the current number of messages in the Pipeline |
| Outgoing        | float            | the rate of outgoing messages into the Pipeline |

You can see from the response and the structure of the data that each Node has a dictionary of Children. In the case the Node has any children, it means it's a group, and it just contains other nodes to display further down the tree structure, and the PipelineProcess should be null. If the Children property is an empty object, then PipelineProcess should contain the data about the Process the Node represents.

This hierarchy system is liable to change in the future, once we can paint a more clearer picture of the order our processing takes. Given that it currently happens concurrently at multiple steps, it is hard to come up with a completely true model that fits what the system is technically doing underneath.

Example response:

```json
{
    "Tree": {
        "Description": null,
        "PipelineProcess": null,
        "Children": {
            "Incoming": {
                "Description": "All processes relating to ingesting data",
                "PipelineProcess": null,
                "Children": {
                    "Process Big Clue Command": {
                        "Description": "Processes big clues.",
                        "PipelineProcess": {
                            "DisplayName": "Process Big Clue Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.ProcessBigClueCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.ProcessBigClueCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Process Low Priority Clue Command": {
                        "Description": "Processes lower priority clues.",
                        "PipelineProcess": {
                            "DisplayName": "Process Low Priority Clue Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.ProcessLowPriorityClueCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.ProcessLowPriorityClueCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Process Prioritized Clue Command": {
                        "Description": "Processes prioritized clues.",
                        "PipelineProcess": {
                            "DisplayName": "Process Prioritized Clue Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.ProcessPrioritizedClueCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.ProcessPrioritizedClueCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Processing": {
                        "Description": "All processes relating to the main processing.",
                        "PipelineProcess": null,
                        "Children": {
                            "External Search Command": {
                                "Description": "Processes external data and enriches clues.",
                                "PipelineProcess": {
                                    "DisplayName": "External Search Command",
                                    "CommandName": "CluedIn.ExternalSearch.ExternalSearchCommand",
                                    "PipelineName": "CluedIn.ExternalSearch.ExternalSearchCommand:CluedIn.ExternalSearch_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Public Api Enrichment Command": {
                                "Description": "",
                                "PipelineProcess": {
                                    "DisplayName": "Public Api Enrichment Command",
                                    "CommandName": "CluedIn.PublicApi.PublicApiEnrichmentCommand",
                                    "PipelineName": "CluedIn.PublicApi.PublicApiEnrichmentCommand:CluedIn.PublicApi_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Split Entity Command": {
                                "Description": "Processes splitting entities that contain data of 2 or more entities.",
                                "PipelineProcess": {
                                    "DisplayName": "Split Entity Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.SplitEntityCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.SplitEntityCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Deduplicate Command": {
                                "Description": "Removes duplicates in data.",
                                "PipelineProcess": {
                                    "DisplayName": "Deduplicate Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.DeduplicateCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.DeduplicateCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Parents Processing Command": {
                                "Description": "Processes parents relationships and data in each of those nodes",
                                "PipelineProcess": {
                                    "DisplayName": "Parents Processing Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.ParentsProcessingCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.ParentsProcessingCommand:CluedIn.Core_CluedIn_ParentIds",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Process Edges Command": {
                                "Description": "Processes proper edges to related entities.",
                                "PipelineProcess": {
                                    "DisplayName": "Process Edges Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.ProcessEdgesCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.ProcessEdgesCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Process Version History Command": {
                                "Description": "Processes clue modifications and history.",
                                "PipelineProcess": {
                                    "DisplayName": "Process Version History Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.ProcessVersionHistoryCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.ProcessVersionHistoryCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Save Entity Command": {
                                "Description": "Processes entity saving.",
                                "PipelineProcess": {
                                    "DisplayName": "Save Entity Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.SaveEntityCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.SaveEntityCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Percolate Entity Update Command": {
                                "Description": "Processes entity percolation.",
                                "PipelineProcess": {
                                    "DisplayName": "Percolate Entity Update Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.PercolateEntityUpdateCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.PercolateEntityUpdateCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Merge Entities Command": {
                                "Description": " Processes the merging of entities with the same information",
                                "PipelineProcess": {
                                    "DisplayName": "Merge Entities Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.MergeEntitiesCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.MergeEntitiesCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Deduplicate Entity Command": {
                                "Description": "Removes duplicates in entities.",
                                "PipelineProcess": {
                                    "DisplayName": "Deduplicate Entity Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.DeduplicateEntityCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.DeduplicateEntityCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Delete Entity Command": {
                                "Description": "Deletes a specified entity",
                                "PipelineProcess": {
                                    "DisplayName": "Delete Entity Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.DeleteEntityCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.DeleteEntityCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Post Processing Entity Command": {
                                "Description": "Processes final step of an entity's processing flow.",
                                "PipelineProcess": {
                                    "DisplayName": "Post Processing Entity Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.PostProcessingEntityCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.PostProcessingEntityCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            }
                        }
                    },
                    "Webhooks": {
                        "Description": "All processing relating to webhooks.",
                        "PipelineProcess": null,
                        "Children": {
                            "Webhook Data Command": {
                                "Description": "Brings back data from webhook.",
                                "PipelineProcess": {
                                    "DisplayName": "Webhook Data Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.WebhookDataCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.WebhookDataCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            },
                            "Process Web Hook Clue Command": {
                                "Description": "Processes clues from webhook data.",
                                "PipelineProcess": {
                                    "DisplayName": "Process Web Hook Clue Command",
                                    "CommandName": "CluedIn.Core.Messages.Processing.ProcessWebHookClueCommand",
                                    "PipelineName": "CluedIn.Core.Messages.Processing.ProcessWebHookClueCommand:CluedIn.Core_CluedIn",
                                    "Incoming": null,
                                    "Messages": 0,
                                    "Outgoing": null
                                },
                                "Children": {}
                            }
                        }
                    }
                }
            },
            "Events Command": {
                "Description": "All processing relating to events.",
                "PipelineProcess": null,
                "Children": {
                    "Processing Event Command": {
                        "Description": "Processes general event.",
                        "PipelineProcess": {
                            "DisplayName": "Processing Event Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.ProcessingEventCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.IProcessingCommand:CluedIn.Core_CluedIn_Clues",
                            "Incoming": 0.0,
                            "Messages": 0,
                            "Outgoing": 0.0
                        },
                        "Children": {}
                    },
                    "Anonymise Data Command": {
                        "Description": "Anonymises specified data.",
                        "PipelineProcess": {
                            "DisplayName": "Anonymise Data Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.AnonymiseDataCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.AnonymiseDataCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "De Anonymise Data Command": {
                        "Description": "Deanonymises specified data.",
                        "PipelineProcess": {
                            "DisplayName": "De Anonymise Data Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.DeAnonymiseDataCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.DeAnonymiseDataCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "I Export Command": {
                        "Description": "Exports data into specified format.",
                        "PipelineProcess": {
                            "DisplayName": "I Export Command",
                            "CommandName": "CluedIn.Core.Messages.WebApi.IExportCommand",
                            "PipelineName": "CluedIn.Core.Messages.WebApi.IExportCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": null,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Mesh Data Command": {
                        "Description": "Handles mesh command.",
                        "PipelineProcess": {
                            "DisplayName": "Mesh Data Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.MeshDataCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.MeshDataCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Send Mail Command": {
                        "Description": "Sends specified mail.",
                        "PipelineProcess": {
                            "DisplayName": "Send Mail Command",
                            "CommandName": "CluedIn.Core.Messages.SendMailCommand",
                            "PipelineName": "CluedIn.Core.Messages.SendMailCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Enqueue Agent Job Command": {
                        "Description": "Adds an agent job to the job queue.",
                        "PipelineProcess": {
                            "DisplayName": "Enqueue Agent Job Command",
                            "CommandName": "CluedIn.Core.Messages.AgentController.EnqueueAgentJobCommand",
                            "PipelineName": "CluedIn.Core.Messages.AgentController.EnqueueAgentJobCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Remove Data Command": {
                        "Description": "Removes specified data.",
                        "PipelineProcess": {
                            "DisplayName": "Remove Data Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.RemoveDataCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.RemoveDataCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Remove From Processing Data Command": {
                        "Description": "Removes specified data from processing.",
                        "PipelineProcess": {
                            "DisplayName": "Remove From Processing Data Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.RemoveFromProcessingDataCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.RemoveFromProcessingDataCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Resync Entity Command": {
                        "Description": "Resyncs and entity, meaning it pulls in the latest data and reprocesses it.",
                        "PipelineProcess": {
                            "DisplayName": "Resync Entity Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.ResyncEntityCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.ResyncEntityCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "I Web Api Command": {
                        "Description": "Handles event relating to the web api.",
                        "PipelineProcess": {
                            "DisplayName": "I Web Api Command",
                            "CommandName": "CluedIn.Core.Messages.WebApi.IWebApiCommand",
                            "PipelineName": "CluedIn.Core.Messages.WebApi.IWebApiCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Refresh Entity Blob Command": {
                        "Description": "Refreshes the SQLServer stored blob store of the entity.",
                        "PipelineProcess": {
                            "DisplayName": "Refresh Entity Blob Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.RefreshEntityBlobCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.RefreshEntityBlobCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Offline Merge Evaluation Command": {
                        "Description": "Handles offline merge evaluation.",
                        "PipelineProcess": {
                            "DisplayName": "Offline Merge Evaluation Command",
                            "CommandName": "CluedIn.Processing.Commands.OfflineMergeEvaluationCommand",
                            "PipelineName": "CluedIn.Processing.Commands.OfflineMergeEvaluationCommand:CluedIn.Processing.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Offline N E R Evaluation Command": {
                        "Description": "Handles offline NER evaluation.",
                        "PipelineProcess": {
                            "DisplayName": "Offline N E R Evaluation Command",
                            "CommandName": "CluedIn.Processing.Commands.OfflineNEREvaluationCommand",
                            "PipelineName": "CluedIn.Processing.Commands.OfflineNEREvaluationCommand:CluedIn.Processing.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Breach Report Command": {
                        "Description": "When triggered, logs a breach report.",
                        "PipelineProcess": {
                            "DisplayName": "Breach Report Command",
                            "CommandName": "CluedIn.Reports.Messages.BreachReportCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.Export.IExportCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Export Entity Command": {
                        "Description": "Exports entity into specified format.",
                        "PipelineProcess": {
                            "DisplayName": "Export Entity Command",
                            "CommandName": "CluedIn.Reports.Messages.ExportEntityCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.Export.IExportCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Archive Metrics Values Command": {
                        "Description": "Archives metrics values generated up to this points.",
                        "PipelineProcess": {
                            "DisplayName": "Archive Metrics Values Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.Metrics.ArchiveMetricsValuesCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.Metrics.ArchiveMetricsValuesCommand:CluedIn.Core_CluedIn",
                            "Incoming": 0.0,
                            "Messages": 0,
                            "Outgoing": 0.0
                        },
                        "Children": {}
                    }
                }
            },
            "Errors": {
                "Description": "All processing relating to errors.",
                "PipelineProcess": null,
                "Children": {
                    "Error Packet": {
                        "Description": "Processes error and logs accordingly.",
                        "PipelineProcess": {
                            "DisplayName": "Error Packet",
                            "CommandName": "CluedIn.Logging.Errors.ErrorPacket",
                            "PipelineName": "CluedIn.Logging.Errors.ErrorPacket:CluedIn.Logging.Errors_CluedIn",
                            "Incoming": 0.0,
                            "Messages": 0,
                            "Outgoing": 0.0
                        },
                        "Children": {}
                    }
                }
            },
            "Outgoing": {
                "Description": "All processing relating to pushing data to external systems.",
                "PipelineProcess": null,
                "Children": {
                    "Outgoing Custom Web Hook Command": {
                        "Description": "Handles pushing data to specified web hook in custom manner.",
                        "PipelineProcess": {
                            "DisplayName": "Outgoing Custom Web Hook Command",
                            "CommandName": "CluedIn.WebHooks.Commands.OutgoingCustomWebHookCommand",
                            "PipelineName": "CluedIn.WebHooks.Commands.OutgoingCustomWebHookCommand:CluedIn.WebHooks_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    }
                }
            },
            "Metrics": {
                "Description": "All processing relating to generating metrics.",
                "PipelineProcess": null,
                "Children": {
                    "Process Entity Metrics Command": {
                        "Description": "Processes entity metrics.",
                        "PipelineProcess": {
                            "DisplayName": "Process Entity Metrics Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.Metrics.ProcessEntityMetricsCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.Metrics.ProcessEntityMetricsCommand:CluedIn.Core_CluedIn",
                            "Incoming": null,
                            "Messages": 0,
                            "Outgoing": null
                        },
                        "Children": {}
                    },
                    "Process Global Metrics Command": {
                        "Description": "Processes global metrics.",
                        "PipelineProcess": {
                            "DisplayName": "Process Global Metrics Command",
                            "CommandName": "CluedIn.Core.Messages.Processing.Metrics.ProcessGlobalMetricsCommand",
                            "PipelineName": "CluedIn.Core.Messages.Processing.Metrics.ProcessGlobalMetricsCommand:CluedIn.Core_CluedIn",
                            "Incoming": 0.0,
                            "Messages": 0,
                            "Outgoing": 0.0
                        },
                        "Children": {}
                    }
                }
            }
        }
    }
}
```