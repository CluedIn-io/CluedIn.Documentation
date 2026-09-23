---
layout: cluedin
nav_order: 3
parent: Streams
grand_parent: Consume
permalink: /consume/streams/manage-streams
title: Manage streams
tags: ["consume", "data export", "streams"]
last_modified: 2026-09-23
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to manage streams to keep the entire process of delivering data to external systems efficient, well-organized, and aligned with your data management objectives.

## Start, pause, and stop a stream

Stream controls allows you to manage the process of sending records to the export target.

- **Start** – the stream will start accumulating records in the queue and sending them to the export target.

    ![start-stream.gif]({{ "/assets/images/consume/streams/start-stream.gif" | relative_url }})

- **Pause** – the stream will stop sending records to the export target, but it will still continue accumulating records in the queue.

    ![pause-stream.gif]({{ "/assets/images/consume/streams/pause-stream.gif" | relative_url }})

- **Stop** – the stream will stop sending records to the export target and accumulating records in the queue.

    ![stop-stream.png]({{ "/assets/images/consume/streams/stop-stream.png" | relative_url }})

Think of these stream controls as similar to the controls on a video player. When you select **Pause**, the stream halts temporarily, remembering your playback position and storing records in the queue. This way, when you resume the stream, it continues from where you left off, maintaining your progress. On the other hand, **Stop** leads to a complete termination of the streaming process and clearing of the queue. If you start the stream after it had been stopped, it will start sending records to the export target from the beginning, not from the point at which you stopped the stream.

## Stream actions

In addition to the standard stream controls, a stream can provide **stream actions** that perform operations specific to its configured [export target](/consume/export-targets).

The actions available on a stream depend on the export target itself. This means that two streams can expose different actions even when their stream configuration is otherwise similar.

To view the actions available for a stream, open the stream details page and select **More**. If the configured export target provides additional actions, they appear in this menu.

### Run an export immediately

File-based export targets can provide a **Run Export** action. This allows you to trigger an export immediately instead of waiting for the next configured export schedule.

For example, **Run Export** can be available for export targets such as:

- [Amazon S3](/consume/export-targets/amazon-s3-connector)
- [Azure Data Lake Storage Gen2](/consume/export-targets/adl-connector)
- [OneLake](/consume/export-targets/onelake-connector)

To run an export manually:

1. Open the stream.

1. On the stream details page, select **More**.

1. Select **Run Export**.

CluedIn starts an export using the stream's current configuration and export target settings.

Running an export manually does not replace or disable the configured export schedule. The stream continues to run according to its existing schedule after the manual export has been triggered.

{:.important}
Stream actions are defined by the export target. **Run Export** is therefore not available for every stream, and other export targets can expose different actions.

## Edit a stream

You can edit the stream configuration and the export target configuration regardless of the [stream status](/consume/streams/stream-reference#stream-statuses).

{:.important}
If you change filters or actions in the stream configuration or if you make any changes in the export target configuration, saving these changes will trigger stream reprocessing. It means that all records existing in the export target will be deleted, and the stream will start sending records to the export target again.

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

## Duplicate a stream

Duplicating a stream means creating a new stream with the configuration of the existing stream. This configuration includes filters and actions but does not include the export target configuration. This means that you need to select and configure the export target and choose the properties for export from scratch for the duplicated stream.

You can duplicate a stream if you want to send the same selection of golden records to another export target.

Duplication is a beta feature. To access it, go to **Administration** > **Feature Flags**, and enable the **Duplicate Actions** feature.

![duplicate-actions-feature-flag.png]({{ "/assets/images/shared/duplicate-actions-feature-flag.png" | relative_url }})

**To duplicate a stream**

1. In the list of streams, find a stream that you want to duplicate. Then, open the three-dot menu for the stream, and select **Duplicate**.

    ![duplicate-stream-1.png]({{ "/assets/images/consume/streams/duplicate-stream-1.png" | relative_url }})

1. In **Name**, review the default name of the new stream and modify it if needed. The default name is created by adding __duplicate_ to the name of the stream that you're duplicating.

1. In **Conditions**, review the filters that will be duplicated for the new stream.

1. In **Actions**, review the list of actions that will be duplicated for the new stream. To view the details of a specific action, select **View Action Details**.

    ![duplicate-stream-2.png]({{ "/assets/images/consume/streams/duplicate-stream-2.png" | relative_url }})

1. Select **Duplicate**.

    The new stream is created. By default, the export target for the stream is not configured. Now, you can modify the stream configuration if needed and [configure](/consume/streams/create-a-stream#configure-an-export-target) the export target. When you reach the desired configuration, [start](/consume/streams/manage-streams#start-pause-and-stop-a-stream) the stream.
