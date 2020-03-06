---
category: Statistics
title: Relational Database
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

Our relational database handles all the internal data used in running our product, such as authentication details, registered providers, blobs storage, and, the most resource heavy use, metrics. You can use the data here to see if any of these are causing a bottleneck.

# Overview

- Connections
- Blobs Total

A breakdown of the current connections can be viewed as a sidepanel

# Charts Overview

## Memory

The chart is made out of the used, available, and percentage of memory used.

## CPU

Shows how much of the CPU the database is using, and that percentage is further broken down as a sidepanel, showing the percentage each database is using for it's queries.

## Database Size Distribution

The pie chart shows a breakdown of all the databases and their store size. A description is also provided for each database.

The 2 axis chart shows the total database size over the last 10 days.

## Blob Sizes

The pie chart shows a breakdown of the memory used and allocated to store Blobs.

# API

### GET /api/statistics/relational

#### DatabaseSizes

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| Count           | int                   | number of databases |
| Total           | array of objects      | sum of all database byte sizes over time |
| Data            | array of data objects | the stores data |

##### Total objects

| Property        | Type                | Description   |
|-----------------|---------------------|---------------|
| Value           | long                | sum of all store byte sizes |
| Date            | string              | date the value has been saved in cache store |

When the endpoint is queried, a new value is added to this array, if there has been at least a day since the date of last added value. This array can have a maximum of 10 values.

##### DatabaseSizes Data

| Property        | Type                | Description   |
|-----------------|---------------------|---------------|
| Name            | string              | name of database |
| Size            | long                | size in bytes |

---

#### NumberOfBlobs

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| NumberOfBlobs   | int                   | the total number of blobs stored in the database |

---

#### BlobsDatabaseSize

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| Name            | string                | the name of the database |
| TotalSize       | string                | sum of all sizes |
| UnallocatedSize | string                | memory not yet used for anything |
| ReservedSize    | string                | reserved memory |
| DataSize        | string                | memory used to store the data of the blobs |
| IndexSize       | string                | memory used to store the indexes of this database |
| UnusedSize      | string                | memory reserved but not used yet |

---

#### DatabaseConnections

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| Count           | int                   | number of databases that have connections open |
| Total           | array of objects      | sum of all connections over time |
| Data            | array of data objects | the database connections data |

##### Total Objects

| Property        | Type                | Description   |
|-----------------|---------------------|---------------|
| Value           | int                 | sum of all connections |
| Date            | string              | date the value has been saved in cache store |

##### DatabaseConnections Data

| Property        | Type                | Description   |
|-----------------|---------------------|---------------|
| Name            | string              | name of database |
| Connections     | int                 | number of connections |

When the endpoint is queried, a new value is added to this array, if there has been at least a day since the date of last added value. This array can have a maximum of 10 values.

---

#### MemoryUsage

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| Free            | int                   | amount of free space in bytes |
| Total           | float                 | amount of space used |
| Percentage      | float                 | percentage of space used out of total available |

---

#### CPUPercentUsed

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| CPUPercentUsed  | int                   | percentage of CPU used |


#### CPUPercentBreakdown

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| Count           | int                   | count of all databases using CPU |
| Data            | array of data objects | cpu percent breakdown data |

##### CPUPercentBreakdown Data

| Property        | Type                  | Description   |
|-----------------|-----------------------|---------------|
| Name            | string                | name of the database |
| CPUPercent      | int                   | cpu percent used by this database |

---

```json
{
    "DatabaseSizes": {
        "Count": 10,
        "Total": [
            {
                "Value": 360448,
                "Date": "05/03/2020"
            }
        ],
        "Data": [
            {
                "Name": "DataStore.Db.Authentication",
                "Size": 16384
            },
            {
                "Name": "DataStore.Db.BlobStorage",
                "Size": 81920
            },
            {
                "Name": "DataStore.Db.Clean",
                "Size": 16384
            },
            {
                "Name": "DataStore.Db.Configuration",
                "Size": 16384
            },
            {
                "Name": "DataStore.Db.ExternalSearch",
                "Size": 16384
            },
            {
                "Name": "DataStore.Db.Metrics",
                "Size": 81920
            },
            {
                "Name": "DataStore.Db.OpenCommunication",
                "Size": 81920
            },
            {
                "Name": "DataStore.Db.TokenStore",
                "Size": 16384
            },
            {
                "Name": "DataStore.Db.Training",
                "Size": 16384
            },
            {
                "Name": "DataStore.Db.WebApp",
                "Size": 16384
            }
        ]
    },
    "NumberOfBlobs": 2861,
    "BlobsDatabaseSize": {
        "Name": "DataStore.Db.BlobStorage",
        "TotalSize": "80.00 MB",
        "UnallocatedSize": "56.35 MB",
        "ReservedSize": "16024 KB",
        "DataSize": "11776 KB",
        "IndexSize": "3304 KB",
        "UnusedSize": "944 KB"
    },
    "DatabasesConnections": {
        "Count": 5,
        "Total": [
            {
                "Value": 13,
                "Date": "05/03/2020"
            }
        ],
        "Data": [
            {
                "Name": "DataStore.Db.Authentication",
                "Connections": 1
            },
            {
                "Name": "DataStore.Db.BlobStorage",
                "Connections": 1
            },
            {
                "Name": "DataStore.Db.Configuration",
                "Connections": 1
            },
            {
                "Name": "DataStore.Db.Metrics",
                "Connections": 1
            },
            {
                "Name": "DataStore.Db.OpenCommunication",
                "Connections": 9
            }
        ]
    },
    "MemoryUsage": {
        "Free": 544219136,
        "Total": 3304062976,
        "PercentageUsed": 83
    },
    "CPUPercentUsed": 1,
    "CPUPercentUsedBreakdown": {
        "Count": 10,
        "Data": [
            {
                "Name": "DataStore.Db.Metrics",
                "CPUPercent": 70
            },
            {
                "Name": "DataStore.Db.OpenCommunication",
                "CPUPercent": 10
            },
            {
                "Name": "DataStore.Db.BlobStorage",
                "CPUPercent": 9
            },
            {
                "Name": "DataStore.Db.Configuration",
                "CPUPercent": 7
            },
            {
                "Name": "DataStore.Db.TokenStore",
                "CPUPercent": 0
            },
            {
                "Name": "DataStore.Db.Authentication",
                "CPUPercent": 0
            },
            {
                "Name": "DataStore.Db.WebApp",
                "CPUPercent": 0
            },
            {
                "Name": "DataStore.Db.Training",
                "CPUPercent": 0
            },
            {
                "Name": "DataStore.Db.ExternalSearch",
                "CPUPercent": 0
            },
            {
                "Name": "DataStore.Db.Clean",
                "CPUPercent": 0
            }
        ]
    }
}
```

