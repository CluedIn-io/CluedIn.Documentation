---
layout: cluedin
nav_order: 13
parent: Export targets
grand_parent: Consume
permalink: /consume/export-targets/file-name-patterns
title: File name patterns
last_modified: 2025-02-05
---

In this article, you will learn about the file name patterns that you can use in the export target configuration to customize the output file names.

CluedIn supports the following file name patterns:

- `{DataTime}` and `{DataTime:formatString}`. `DataTime` is in UTC, and `formatString` accepts formats available to the `DateTime.ToString()` method in C#. For more information, see Microsoft documentation: [Standard date and time format strings](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings) and [Custom date and time format strings](https://learn.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings).

    When using `{DataTime}` without `formatString`, it defaults to the `o` format (for example, `2024-07-05T03:02:57.2612933Z`).

- `{StreamId}` and `{DataTime:formatString}`. `formatString` accepts formats available to the `Guid.ToString()` method in C#. For more information, see [Guid.ToString Method](https://learn.microsoft.com/en-us/dotnet/api/system.guid.tostring?view=net-8.0).

    When using `{StreamId}` without `formatString`, it defaults to `D` format (for example, `ba4afc12-f6dc-4394-b9d5-68f6dacf3b3b`).

- `{OutputFormat}` and `{OutputFormat:formatString}`. `formatString` accepts the following methods:

    - `ToUpperInvariant`
    - `ToUpper` (equivalent to `ToUpperInvariant`)
    - `ToLower`
    - `ToUpperInvariant` (equivalent to `ToLowerInvariant`)

    When using `{OutputFormat}` without `formatString`, no extra formatting is performed (for example, `csv`, `parquet`, `json`).

- `{ContainerName}` and `{ContainerName:formatString}`. `{ContainerName}` uses the value in the **Target Name** of the [stream](/consume/streams/create-a-stream#configure-an-export-target). `formatString` accepts the following methods:

    - `ToUpperInvariant`
    - `ToUpper` (equivalent to `ToUpperInvariant`)
    - `ToLower`
    - `ToLowerInvariant` (equivalent to `ToLowerInvariant`)

**Example filename patterns**

| File name pattern  | Example output  |
|--|--|
| `{StreamId:N}_{DataTime:yyyyMMddHHmmss}.{OutputFormat}` | `ba4afc12f6dc4394b9d568f6dacf3b3b_20240705030355.parquet` |
| `{StreamId}_{DataTime}.{OutputFormat:ToUpper}` | `ba4afc12-f6dc-4394-b9d5-68f6dacf3b3b_2024-07-05T03:02:57.2612933Z.PARQUET` |
| `{ContainerName}_{DataTime:yyyyMMddHHmmss}.{OutputFormat}` | `CustomerRecord_20240705030355.parquet` |

**Default file name patterns**

| Connector | Default file name pattern |
|--|--|
| [Azure Data Lake connector](/consume/export-targets/adl-connector) | `{StreamId:D}_{DataTime:yyyyMMddHHmmss}.{OutputFormat}` |
| [OneLake connector](/consume/export-targets/onelake-connector) | `{StreamId:N}_{DataTime:yyyyMMddHHmmss}.{OutputFormat}` |