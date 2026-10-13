---
title: Stream logs
url: https://documentation.cluedin.net/publish/streams/stream-logs
content_type: how-to
section: Publish & consume > Streams
---

# Stream logs

> how-to: Steps to accomplish one task.

In this article, you will learn how to ensure that your golden records have been successfully exported and how to identify issues when something goes wrong.

CluedIn offers three types of logs to assist in monitoring and troubleshooting your streams:

- **Golden record stream logs** – view the streams that exported a specific golden record.

- **Stream logs** – view golden records exported by a specific stream.

- **Export target health checks** – view the health check status of the export target, updated every minute.

## Golden record stream logs

Each golden record contains the **Streams** tab, where you can find the stream that exported the golden record and the date it was sent to the export target.

![The golden record Streams tab listing the Training stream with change type Added, persist version, persist hash and date sent](https://documentation.cluedin.net/assets/images/consume/streams/golden-record-streams.png)

This page lists active and paused streams that exported the golden record. However, if the stream is stopped, it is not displayed on the **Streams** tab because all of its logs are cleared. You can select the stream to view its details.

## Stream logs

Each stream contains the **Stream Log** tab, where you’ll find all golden records that were exported by this stream. If the stream encounters an error while exporting golden records, it will be displayed on the page. This way, you can quickly identify and address any issues.

![The Stream log tab of the Training stream, listing exported records with severity, area Stream ingestion log, and machine name, plus severity and area filters](https://documentation.cluedin.net/assets/images/consume/streams/stream-log.png)

You can filter the stream logs by two categories:

- **Severity** – the level of importance or urgency of an event or issue. Learn about standard severity levels [here](https://learn.microsoft.com/en-us/dotnet/core/extensions/logging?tabs=command-line#log-level).

- **Area** – the place in the streaming pipeline that produces logs:

    - **Stream ingestion log** – logs coming from the stream.

    - **Health check** – logs coming from the export target assigned to the stream. When the health check status of the export target changes, for example, from **Healthy** to **Unhealthy**, a new log is added to the page.

    - **Export target** – other messages that the export target itself would like to log in the stream.

This page displays logs only when the stream is active or paused. If you stop the stream, the logs are cleared.

## Export target health checks

Each export target contains the **Health Checks** tab, where you can find the health check status of the export target.

![The Health Check tab of an SQL Server export target, listing health checks with the Healthy state, host and creation time](https://documentation.cluedin.net/assets/images/consume/streams/export-target-health-check.png)

CluedIn runs health checks for the export target every 60 seconds. If the export target encounters any issues, its health status will be marked as **Unhealthy**. If the export target becomes **Unhealthy**, the stream associated with that export target is stopped and the corresponding log is added to the **Stream Log** page as well.

Up: [Streams](https://documentation.cluedin.net/publish/streams.md)
