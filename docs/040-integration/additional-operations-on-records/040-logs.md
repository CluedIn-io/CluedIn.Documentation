---
layout: cluedin
nav_order: 5
parent: Additional operations
grand_parent: Integration
permalink: /integration/additional-operations-on-records/logs
title: Logs
tags: ["integration", "logs"]
last_modified: 2023-11-07
---

Logs inform you about warnings or errors in your records based on the built-in logic and limitations of CluedIn. These logs are generated for records only, not for the infrastructure. Be sure to check the logs before processing the data.

There are two levels of logs:

- Warning – the data has been processed, but some values have been changed.

- Error – the data cannot be processed because it does not correspond to CluedIn business rules or limitations.

CluedIn performs validations on the following stages of the record life cycle: parsing, storing, mapping, and processing. If an inconsistency is detected at any of these stages, a new log entry will appear on the **Logs** tab of the data set. By selecting the log message, you will find the error or warning details. In case of an error,  related records will also be displayed, providing information for debugging purposes.

![logs-1.png](../../assets/images/integration/additional-operations/logs-1.png)

If a record contains an error, it is not saved in CluedIn. However, if CluedIn recognizes an invalid character, it will convert it automatically to a valid one and the record will be stored in the platform.

The following table contains examples of **validation messages** explaining what has gone wrong with the record.

| Data source type | Log level | Validation message |
|--|--|--|
| Endpoint | Error | JSON is not an array. |
| Endpoint | Error | JSON is not a valid JSON object. |
| Endpoint | Error | JSON array contains more than 100,000 records. |
| File | Error | File could not be parsed. |
| Endpoint/File/SQL | Error | Record has more than 500 columns. |
| Endpoint/File/SQL | Error | The object is either null or empty or is an empty object (`{}`). |
| Endpoint/File/SQL | Error | Property in the record is invalid. |
| Endpoint/File/SQL | Error | Property in the record has Arabic letters (not supported), Asian letters (not supported), or Cyrillic letters (not supported). |
| Endpoint/File/SQL | Warning | Property in the record had the key named “id” and it was renamed to “_id”. |
| Endpoint/File/SQL | Warning | Property in the record had spaces and they were removed. |
| Endpoint/File/SQL | Warning | Property in the record had dots and they were removed. |

{:.important}
The reason for strict rules for property names is that property names are translated to vocabulary keys using the same pattern as the [Microsoft Common Data Model](https://learn.microsoft.com/en-us/common-data-model/).

You can delete the logs by selecting **Purge Logs**. This action does not affect the data set, it only deletes all logs for the data set.