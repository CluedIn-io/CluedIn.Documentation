---
category: Statistics
title: Search Database
---

# Statistics Sections
1. [Statistics Room Overview](/docs/70-Statistics/00-Intro/Statistics%20Room.html)
2. [Processing Pipelines](/docs/70-Statistics/10-Pipelines/Pipelines.html)
3. [Graph Database](/docs/70-Statistics/20-Graph/Graph.html)
4. [Search Database](/docs/70-Statistics/30-Search/Search.html)
5. [Relational Database](/docs/70-Statistics/40-Relational/Relational.html)
6. [Cache Database](/docs/70-Statistics/50-Cache/Cache.html)
7. [Configuration](/docs/70-Statistics/60-Configuration/Configuration.html)

The data on this page is updated once per second.

This page should give you an overview of the health of our search database, and the data contained inside.

# Overview

- Health - red = problem; yellow = possible problem, or soon to be; green = good
- Nodes
- Indices
- Open File Descriptors
- Documents
- Threads Count

The overview section provides information about different key values that are of interest in the Search Database. Their count is given in overview, but some also offer a list breakdown.

# Charts Overview

## Memory

The pie chart is made out of the used, max, and percentage of memory used.

## CPU

Shows how much of the CPU is used.

## Disk Size

The chart is made out of the used, available, and percentage of disk size used.

The 2 axis chart shows the used disk size in the last 10 days. 

## Shard status distribution

The pie chart provides a breakdown of the database shards and their status.

## Entity Type Distribution

The pie chart shows a breakdown of all entity types, and how many entities each contains.

The 2 axis chart shows the number of total entities over the last 10 days.

## Documents

The 2 axis chart shows the total number of stored documents over the last 10 days.

# Nodes

This panel is accesible from the Actions section.

The database's nodes are listed here with the following columns:
- Name
- Load Average
- Docs - Count
- Disk Usage %
- Thread - Count
- CPU %
- Memory Usage %
- Thread Pool

The Thread Pool breakdown of each node can be seen as a breakdown when the button under the column is clicked.

# API

### GET /api/statistics/search

#### Overview

| Property             | Type                  | Description   |
|----------------------|-----------------------|---------------|
| Status               | string                | health status that can be green, yello, or red |
| NodesCount           | int                   | the current number of nodes |
| IndicesCount         | int                   | the current number of indices |
| Shards               | object                | breakdown of shards |
| EntityTypes          | object                | breakdown of entity types |
| Documents            | object                | breakdown of documents |
| Disk                 | object                | breakdown of disk use |
| ThreadsCount         | int                   | count of used threads |
| ProcessingCPUPercent | int                   | percentage of CPU used |
| Memory               | object                | memory used in bytes |
| OpenFileDescriptors  | object                | breakdown of open file descriptors |
| Nodes                | object                | breakdown of nodes |

---

##### Shards

| Property             | Type                  | Description   |
|----------------------|-----------------------|---------------|
| Count                | int                   | total number of shards |
| Active               | int                   | number of active shards  |
| Relocating           | int                   | number of relocating shards |
| Initializing         | int                   | number of initializing shards |
| Unassigned           | int                   | number of unassigned shards |
| DelayedUnassigned    | int                   | number of delayed unassigned shards |

---

###### EntityTypes

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| Count           | int                   | number of entity types |
| Total           | array of objects      | sum of all entities over time|
| Data            | array of data objects | the entity types data |

##### Total objects

| Property        | Type                | Description   |
|-----------------|---------------------|---------------|
| Value           | int                 | sum of all entities |
| Date            | string              | date the value has been saved in cache store |

When the endpoint is queried, a new value is added to this array, if there has been at least a day since the date of last added value. This array can have a maximum of 10 values.

##### EntityTypes Data

| Property        | Type                | Description   |
|-----------------|---------------------|---------------|
| term            | string              | entity type name |
| count           | int                 | number of entities of this entity type |

---

##### Documents

| Property             | Type                  | Description   |
|----------------------|-----------------------|---------------|
| Count                | array of objects      | count over time |
| StoreSize            | long                  | store size in bytes |

##### Count objects

| Property        | Type                | Description   |
|-----------------|---------------------|---------------|
| Value           | int                 | total number of documents |
| Date            | string              | date the value has been saved in cache store |

---

##### Disk

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| PercentageUsed  | int                   | percentage of used disk |
| Total           | array of objects      | total disk used in bytes over time |
| Free            | long                  | free disk space in bytes |

###### Total objects

| Property        | Type                | Description   |
|-----------------|---------------------|---------------|
| Value           | long                | total disk used in bytes |
| Date            | string              | date the value has been saved in cache store |

---

##### Memory

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| Used            | long                  | used memory in bytes |
| Max             | long                  | max memory in bytes |
| PercentageUsed  | int                   | percentage used |

---

##### OpenFileDescriptors

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| Min             | int                   | minimum open file descriptors |
| Max             | int                   | maximum open file descriptors |
| Avg             | int                   | average open file descriptors |

---

##### Nodes

| Property             | Type                  | Description   |
|----------------------|-----------------------|---------------|
| Count                | int                   | number of nodes |
| Data                 | array of data objects | the nodes data |

Nodes reuse some of the data structures defined above, so those will not be repeated.

##### Threads

| Property             | Type                  | Description   |
|----------------------|-----------------------|---------------|
| Count                | int                   | number of threads |
| PeakCount            | int                   | number of threads at peak use |

##### ThreadPool (dictionary)

| Property             | Type                  | Description   |
|----------------------|-----------------------|---------------|
| Percolate            | object                | percolate threads |
| Fetch_Shard_Started  | object                | fetch shard started threads |
| Listener             | object                | listener threads |
| Index                | object                | index threads |
| Refresh              | object                | refresh threads |
| Suggest              | object                | suggest threads |
| Generic              | object                | generic threads |
| Warmer               | object                | warmer threads |
| Search               | object                | search threads |
| Flush                | object                | flush threads |
| Optimize             | object                | optimize threads |
| Fetch_Shard_Store    | object                | fetch shard store threads |
| Management           | object                | management threads |
| Get                  | object                | get threads |
| Merge                | object                | merge threads |
| Bulk                 | object                | bulk threads |
| Snapshot             | object                | snapshot threads |

##### ThreadPool Object

| Property             | Type                  | Description   |
|----------------------|-----------------------|---------------|
| Threads              | int                   | total threads number |
| Queue                | int                   | queue threads number |
| Active               | int                   | active threads number |
| Rejected             | int                   | rejected threads number |
| Largest              | int                   | largest threads number |
| Completed            | int                   | completed threads number |

---

```json
{
    "Status": "yellow",
    "NodesCount": 1,
    "IndicesCount": 1,
    "Shards": {
        "Count": 5,
        "Active": 5,
        "Relocating": 0,
        "Initializing": 0,
        "Unassigned": 5,
        "DelayedUnassigned": 0
    },
    "EntityTypes": {
        "Count": 14,
        "Total": [
            {
                "Value": 2861,
                "Date": "04/03/2020"
            },
            {
                "Value": 2861,
                "Date": "05/03/2020"
            }
        ],
        "Data": [
            {
                "term": "/Contract",
                "count": 1656
            },
            {
                "term": "/LegalEntity",
                "count": 1173
            },
            {
                "term": "/Person",
                "count": 14
            },
            {
                "term": "/Infrastructure/User",
                "count": 5
            },
            {
                "term": "/Finance/BankAccount",
                "count": 3
            },
            {
                "term": "/Organization",
                "count": 2
            },
            {
                "term": "/Temporal/Year",
                "count": 1
            },
            {
                "term": "/Temporal/Quarter",
                "count": 1
            },
            {
                "term": "/Temporal/Month",
                "count": 1
            },
            {
                "term": "/Temporal/Millennium",
                "count": 1
            },
            {
                "term": "/Temporal/Decade",
                "count": 1
            },
            {
                "term": "/Temporal/Date",
                "count": 1
            },
            {
                "term": "/Temporal/Century",
                "count": 1
            },
            {
                "term": "/Provider/Root",
                "count": 1
            }
        ]
    },
    "Documents": {
        "Count": [
            {
                "Value": 2861,
                "Date": "04/03/2020"
            },
            {
                "Value": 2861,
                "Date": "05/03/2020"
            }
        ],
        "StoreSize": 3603083
    },
    "Disk": {
        "PercentageUsed": 42,
        "Total": [
            {
                "Value": 62725787648,
                "Date": "05/03/2020"
            }
        ],
        "Free": 36656398336
    },
    "ThreadsCount": 42,
    "ProcessingCPUPercent": 0,
    "Memory": {
        "Used": 155576616,
        "Max": 1056309248,
        "PercentageUsed": 15
    },
    "OpenFileDescriptors": {
        "Min": 173,
        "Max": 173,
        "Avg": 173
    },
    "Nodes": {
        "Count": 1,
        "Data": [
            {
                "LoadAverage": null,
                "Documents": {
                    "Count": 2861,
                    "StoreSize": 3603083
                },
                "Disk": {
                    "PercentageUsed": 42,
                    "Total": 62725787648,
                    "Free": 36656398336
                },
                "Threads": {
                    "Count": 42,
                    "PeakCount": 43
                },
                "ThreadPool": {
                    "Percolate": {
                        "Threads": 0,
                        "Queue": 0,
                        "Active": 0,
                        "Rejected": 0,
                        "Largest": 0,
                        "Completed": 0
                    },
                    "Fetch_Shard_Started": {
                        "Threads": 1,
                        "Queue": 0,
                        "Active": 0,
                        "Rejected": 0,
                        "Largest": 4,
                        "Completed": 5
                    },
                    "..."
                },
                "ProcessingCPUPercent": null,
                "Memory": {
                    "Used": 155576616,
                    "Max": 1056309248,
                    "PercentageUsed": 15
                },
                "UptimeInMiliseconds": 20345428
            },
            {
                "LoadAverage": null,
                "Documents": {
                    "Count": 2861,
                    "StoreSize": 3603083
                },
                "Disk": {
                    "PercentageUsed": 42,
                    "Total": 62725787648,
                    "Free": 36656398336
                },
                "Threads": {
                    "Count": 42,
                    "PeakCount": 43
                },
                "ThreadPool": {
                    "Percolate": {
                        "Threads": 0,
                        "Queue": 0,
                        "Active": 0,
                        "Rejected": 0,
                        "Largest": 0,
                        "Completed": 0
                    },
                    "Fetch_Shard_Started": {
                        "Threads": 1,
                        "Queue": 0,
                        "Active": 0,
                        "Rejected": 0,
                        "Largest": 4,
                        "Completed": 5
                    },
                    "..."
                },
                "ProcessingCPUPercent": null,
                "Memory": {
                    "Used": 155576616,
                    "Max": 1056309248,
                    "PercentageUsed": 15
                },
                "UptimeInMiliseconds": 20345428
            }
        ]
    }
}
```