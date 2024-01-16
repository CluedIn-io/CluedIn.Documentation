---
layout: default
nav_order: 2
parent: Streams
grand_parent: Consume
permalink: /consume/streams/manage-streams
title: Manage streams
tags: ["consume", "streams"]
last_modified: 2024-01-16
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to manage streams to keep the entire process of delivering data to external systems efficient, well-organized, and aligned with your data management objectives.

## Start, pause, and stop a stream

Stream controls allows you to manage the process of sending records to the export target.

- **Start** – the stream will start accumulating records in the queue and sending them to the export target.

    ![manage-streams-1.png](../../assets/images/consume/streams/manage-streams-1.png)

- **Pause** – the stream will stop sending records to the export target, but it will still continue accumulating records in the queue.

    ![manage-streams-2.png](../../assets/images/consume/streams/manage-streams-1.png)

- **Stop** – the stream will stop sending records to the export target and accumulating records in the queue.

    ![manage-streams-3.png](../../assets/images/consume/streams/manage-streams-1.png)

Think of these stream controls as similar to the controls on a video player. When you select **Pause**, the stream halts temporarily, remembering your playback position and storing records in the queue. This way, when you resume the stream, it continues from where you left off, maintaining your progress. On the other hand, **Stop** leads to a complete termination of the streaming process and clearing of the queue. If you start the stream after it had been stopped, it will start sending records to the export target from the beginning, not from the point at which you stopped the stream.

## Edit a stream

You can edit the stream configuration and the export target configuration regardless of the [stream status](/consume/streams/stream-reference#stream-statuses).

**Important:** If you change filters or actions in the stream configuration or if you make any changes in the export target configuration, saving these changes will trigger stream reprocessing. It means that all records existing in the export target will be deleted, and the stream will start sending records to the export target again.

**To edit the stream configuration**

- On the **Configuration** tab, edit the needed items. You can edit any field or section. Then, select **Save** and confirm your choice.

**To edit the export target configuration**

1. On the **Export Target Configuration** tab, select **Edit Export Configuration**, and then confirm your choice.

1. Make the needed changes, select **Save**, and then confirm your choice.

## View stream details

On the stream details page, there are several tabs where you can view stream-related information:

- **Preview Condition** – you can view the records that match the filters from the **Configuration** tab.

- **Data** – you can view the records that will be sent to the export target. These records match the filters from the **Configuration** tab and contain the properties you selected on the **Export Target Configuration** tab.

- **Monitoring** – you can view real-time data on ingestion, processing, and publishing of records, as well as any exceptions.
