---
layout: default
nav_order: 3
parent: Streams
grand_parent: Consume
permalink: /consume/streams/stream-reference
title: Stream reference
tags: ["consume", "streams"]
last_modified: 2024-01-16
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will find reference information to help you understand stream statuses and other stream indicators.

## Stream statuses

| Status | Description |
|--|--|
| New | Stream has not been started yet. |
| Streaming | Stream is accumulating or sending data to the export target. |
| Paused | Data is being accumulated in the queue. |
| Stopped | No data is being accumulated or sent to the export target.  |

## Stream indicators

Stream indicators assist in understanding the state of the stream, highlighting missing elements, and indicating areas that still require configuration.

| Indicator | Description |
|--|--|
| No export target | When no export target is defined, the golden records matching the stream's filters will be accumulated in the queue. If you want to send the records to an external system, you need to add the export target to the stream. |
| No filters | When no filters are defined, all golden records will be accumulated or sent to the export target. |
| No properties selected | When no properties are selected, default properties of the golden records will be accumulated or sent to the export target. The list of default properties vary depending on the export target. |
| Streaming | The records are being sent to the export target. |
| Exporting | The export target is receiving records. |
| Not exporting | The export target is not receiving records. To fix this, check the [export target](/consume/export-targets) configuration. |

## Message queues

When starting the stream, records in CluedIn undergo a three-part process before being sent to the export target: ingestion, processing, and publishing. At each stage, the records are temporarily stored in queues named accordingly.

| Queue | Description |
|--|--|
| Ingestion | This is where all of the potential records that could be streamed are stored. |
| Processing | This is where the records that meet the stream's filters are stored and where the stream's actions are executed. |
| Publishing | This is where the records are sent to the export target. |