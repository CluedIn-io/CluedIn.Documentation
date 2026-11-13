---
layout: cluedin
title: Stream logs
parent: Streams
grand_parent: Publish & consume
nav_order: 50
permalink: /publish/streams/stream-logs
content_type: how-to
redirect_from: ["/consume/streams/stream-logs"]
source_path: docs/150-consume/streams/040-stream-logs.md
tags: ["consume", "data export", "streams"]
last_modified: 2026-10-27
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to ensure that your golden records have been successfully exported and how to identify issues when something goes wrong.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1070316791?h=c9b20fb462&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Stream logs in CluedIn"></iframe>
</div>

CluedIn offers three types of logs to assist in monitoring and troubleshooting your streams:

- **Golden record stream logs** – view the streams that exported a specific golden record.

- **Stream logs** – view golden records exported by a specific stream.

- **Export target health checks** – view the health check status of the export target, updated every minute.

In addition, the **Stream Log** tab shows a **delivery confirmation** summary so you can confirm, at a glance, how many records a stream has attempted to deliver, how many were delivered successfully, and how many failed.

## Golden record stream logs

Each golden record contains the **Streams** tab, where you can find the stream that exported the golden record and the date it was sent to the export target.

![The golden record Streams tab listing the Training stream with change type Added, persist version, persist hash and date sent]({{ "/assets/images/consume/streams/golden-record-streams.png" | relative_url }})

This page lists active and paused streams that exported the golden record. However, if the stream is stopped, it is not displayed on the **Streams** tab because all of its logs are cleared. You can select the stream to view its details.

## Delivery confirmation

At the top of the **Stream Log** tab, the **Delivery confirmation** panel shows the stream's own ID – a stable identifier you can copy and reference when raising a support request – alongside three counts for the selected time window:

- **Attempted** – the total number of records the stream tried to deliver to its export target.

- **Successful** – records confirmed delivered to the export target.

- **Failed** – records that failed to deliver; see them with their error details in the stream log below, filtered by severity **Error**.

![The Delivery confirmation panel of the Training stream, showing a copyable Stream ID, Attempted, Successful and Failed counts, and a date range filter]({{ "/assets/images/consume/streams/stream-delivery-confirmation.png" | relative_url }})

By default, the counts cover all time. Use the date filter next to the counts to narrow them to a specific window, for example to confirm how many records a stream delivered since this morning.

## Stream logs

Each stream contains the **Stream Log** tab, where you’ll find all golden records that were exported by this stream. If the stream encounters an error while exporting golden records, it will be displayed on the page. This way, you can quickly identify and address any issues.

![The Stream log tab of the Training stream, listing exported records with severity, area Stream ingestion log, and machine name, plus severity, area, entity ID and date filters]({{ "/assets/images/consume/streams/stream-delivery-confirmation.png" | relative_url }})

You can filter the stream logs by:

- **Severity** – the level of importance or urgency of an event or issue. Learn about standard severity levels [here](https://learn.microsoft.com/en-us/dotnet/core/extensions/logging?tabs=command-line#log-level).

- **Area** – the place in the streaming pipeline that produces logs:

    - **Stream ingestion log** – logs coming from the stream.

    - **Health check** – logs coming from the export target assigned to the stream. When the health check status of the export target changes, for example, from **Healthy** to **Unhealthy**, a new log is added to the page.

    - **Export target** – other messages that the export target itself would like to log in the stream.

- **Entity ID** – search for the logs of a specific golden record by its entity ID, to confirm whether and how that record was delivered.

- **Date range** – narrow the logs to a specific time window.

This page displays logs only when the stream is active or paused. If you stop the stream, the logs are cleared.

## Export target health checks

Each export target contains the **Health Checks** tab, where you can find the health check status of the export target.

![The Health Check tab of an SQL Server export target, listing health checks with the Healthy state, host and creation time]({{ "/assets/images/consume/streams/export-target-health-check.png" | relative_url }})

CluedIn runs health checks for the export target every 60 seconds. If the export target encounters any issues, its health status will be marked as **Unhealthy**. If the export target becomes **Unhealthy**, the stream associated with that export target is stopped and the corresponding log is added to the **Stream Log** page as well.
