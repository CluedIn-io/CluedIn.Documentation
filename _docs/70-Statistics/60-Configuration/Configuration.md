---
category: Statistics
title: Configuration
---

# Statistics Sections
1. [Statistics Room Overview](/docs/70-Statistics/00-Intro/Statistics%20Room.html)
2. [Processing Pipelines](/docs/70-Statistics/10-Pipelines/Pipelines.html)
3. [Graph Database](/docs/70-Statistics/20-Graph/Graph.html)
4. [Search Database](/docs/70-Statistics/30-Search/Search.html)
5. [Relational Database](/docs/70-Statistics/40-Relational/Relational.html)
6. [Cache Database](/docs/70-Statistics/50-Cache/Cache.html)
7. [Configuration](/docs/70-Statistics/60-Configuration/Configuration.html)

The data on this page is updated on page refresh.

Configuration is managed using Yaml and .Config files, however these are closed down from the User Interface. It is however very useful to explore the possible configuration options and also to be aware of the current state of the application. For example, we may want to know if a certain feature is enabled or not.

The Configuration Endpoint exposes parts of the Configuration that are for read only access. We will not expose Secrets, Passwords, API Tokens or anything that exposes credentials. This is also useful for debugging and exploring potential issues.

For example, you can configure CluedIn with many different parameters and features, but if there are settings that are against our recommended settings, we can expose this in the configuration user interface to alert the first places to potentially look. This is also important to validate if the configuration that has been set is actually in action in the running state of the application. All settings are read-only.

# Connection Strings

A table listing all connection strings, with the following columns:
- Name
- Connection String
- Provider Name
- Description

# Groups

A table listing all the groups of configurations.

When selecting a group, you can see a table with the following columns in a sidepanel on the right side of the screen:
- Key
- Value
- Description

# API

### GET /api/statistics/configuration

#### ConnectionStrings Object

| Property            | Type                  | Description   |
|---------------------|-----------------------|---------------|
| Name                | string                | the name of the connection string (may be thought of as a key as well) |
| ConnectionString    | string                | the connection string needed to make a connection to the provider |
| ProviderName        | string                | the name of the provider |
| Description         | string                | short description of provider's purpose |

#### PairedGroups Group Object

| Property            | Type                  | Description   |
|---------------------|-----------------------|---------------|
| Key                 | string                | the key of this property |
| Value               | string                | the value of this property |
| Group               | string                | the group this property belongs to |
| Description         | string                | short description of property and it's purpose |

---

```json
{
    "ConnectionStrings": [
        {
            "Name": "LocalSqlServer",
            "ConnectionString": "data source=.\\SQLEXPRESS;Integrated Security=SSPI;AttachDBFilename=|DataDirectory|aspnetdb.mdf;User Instance=true",
            "ProviderName": "System.Data.SqlClient",
            "Description": "Used for local development"
        },
        "..."
    ],
    "PairedGroups": {
        "Ungrouped": [
            ...
        ],
        "General": [
            {
                "Key": "ServerUrl",
                "Value": "https://*:9000",
                "Group": "General",
                "Description": "No Description"
            },
            {
                "Key": "ServerReturnUrl",
                "Value": "https://localhost:9000",
                "Group": "General",
                "Description": "No Description"
            },
            "..."
        ],
        "Logging": [
            "..."
        ],
        "Agent": [
            "..."
        ],
        "Agent Controller: [
            "..."
        ],
        "Feature Flags": [
            "..."
        ],
        "Job Server": [
            "..."
        ],
        "Events": [
            "..."
        ],
        "Subscription Prefetch": [
            "..."
        ],
        "Subscription": [
            "..."
        ],
        "Filtering": [
            "..."
        ],
        "Schema": [
            "..."
        ],
        "Testing": [
            "..."
        ],
        "Aggregation": [
            "..."
        ],
        "Models": [
            "..."
        ],
        "Providers": [
            "..."
        ],
        "File Sink": [
            "..."
        ],
        "Seq Sink": [
            "..."
        ],
        "Enrichers": [
            "..."
        ],
    }
}
```