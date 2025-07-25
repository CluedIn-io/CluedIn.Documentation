---
layout: cluedin
nav_order: 5
parent: Streams
grand_parent: Consume
permalink: /consume/streams/stream-logs
title: Stream logs
tags: ["consume", "data export", "streams"]
last_modified: 2025-04-18
---

In this article, you will learn how to ensure that your golden records have been successfully exported and how to identify issues when something goes wrong.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1070316791?h=c9b20fb462&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Stream logs in CluedIn"></iframe>
</div>

CluedIn offers three types of logs to assist in monitoring and troubleshooting your streams:

- **Golden record stream logs** – view the streams that exported a specific golden record.

- **Stream logs** – view golden records exported by a specific stream.

- **Export target health checks** – view the health check status of the export target, updated every minute.

**Golden record stream logs**

Each golden record contains the **Streams** tab, where you can find the stream that exported the golden record and the date it was sent to the export target.

![golden-record-streams.png]({{ "/assets/images/consume/streams/golden-record-streams.png" | relative_url }})

This page lists active and paused streams that exported the golden record. However, if the stream is stopped, it is not displayed on the **Streams** tab because all of its logs are cleared. You can select the stream to view its details.

**Stream logs**

Each stream contains the **Stream Log** tab, where you’ll find all golden records that were exported by this stream. If the stream encounters an error while exporting golden records, it will be displayed on the page. This way, you can quickly identify and address any issues.

![stream-log.png]({{ "/assets/images/consume/streams/stream-log.png" | relative_url }})

You can filter the stream logs by two categories:

- **Severity** – the level of importance or urgency of an event or issue. Learn about standard severity levels [here](https://learn.microsoft.com/en-us/dotnet/core/extensions/logging?tabs=command-line#log-level).

- **Area** – the place in the streaming pipeline that produces logs:

    - **Stream ingestion log** – logs coming from the stream.

    - **Health check** – logs coming from the export target assigned to the stream. When the health check status of the export target changes, for example, from **Healthy** to **Unhealthy**, a new log is added to the page.

    - **Export target** – other messages that the export target itself would like to log in the stream.

This page displays logs only when the stream is active or paused. If you stop the stream, the logs are cleared.

**Export target health checks**

Each export target contains the **Health Checks** tab, where you can find the health check status of the export target.

![export-target-health-check.png]({{ "/assets/images/consume/streams/export-target-health-check.png" | relative_url }})

CluedIn runs health checks for the export target every 60 seconds. If the export target encounters any issues, its health status will be marked as **Unhealthy**. If the export target becomes **Unhealthy**, the stream associated with that export target is stopped and the corresponding log is added to the **Stream Log** page as well.
