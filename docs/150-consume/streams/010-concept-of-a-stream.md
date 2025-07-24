---
layout: cluedin
nav_order: 1
parent: Streams
grand_parent: Consume
permalink: consume/streams/concept-of-a-stream
title: Concept of a stream
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you'll learn about the process of sending golden records from CluedIn to the export target. We'll focus on each step of the process so that you know what to expect when you create a stream yourself.

![stream-concept.gif](../../assets/images/consume/streams/stream-concept.gif)

## Stream configuration

This is the initial part where you determine which golden records will be sent to the export target. Using **filters**, you can precisely specify which golden records you want to send to the export target. All golden records matching the filters are displayed on the **Preview** tab of the stream.

If you want to modify golden records that will be exported—for example, mask certain values—you can do it by adding **actions**. The changes applied by the actions do not affect golden records stored in CluedIn, only golden records that will be sent to the export target. These changes will be visible only in the export target.

At this point, stream configuration is done, and it's time to configure the export target—an external system that will receive golden records from CluedIn.

## Export target configuration

This is the part where you configure the destination for golden records. First of all, you need to select the **type of connector**—an external system ready to receive golden records from CluedIn. 

Next, you need to define two **connector properties**:

- **Target name** – a name of a container that will receive golden records from CluedIn. For example, in SQL databases this container is a table, and in Elasticsearch databases it is the index.

- **Streaming mode** – a mode that defines how golden records will be sent to the export target:

    - **Synchronized stream** – with this mode, golden records in the export target will mirror golden records in CluedIn. It means that every time a golden record is changed in CluedIn, it is automatically changed in the export target. Also, if you delete a golden record in CluedIn, it is automatically deleted in the export target.

        ![synched-stream.gif](../../assets/images/consume/streams/synched-stream.gif)

    - **Event log stream** – with this mode, each time an action occurs in CluedIn, a corresponding event is sent to the export target (for example, Create, Insert, Update, Delete).

        ![event-log-stream.gif](../../assets/images/consume/streams/event-log-stream.gif)

Now, it's time to decide if you want to stream **golden record relations**, also known as edges. Relations give you the necessary information to link your data correctly in the export target. You can choose both outgoing relations and incoming relations.

Finally, you need to select specific **golden record properties** that will be exported. You can automatically select all properties associated with golden records from stream configuration, or you can select specific properties.

At this point, export target configuration is done, and it's time to start sending golden records to the export target.

## Sending golden records to export target

This is the final part of the process where you start sending golden records to the export target. After selecting **Start**, CluedIn starts sending golden records to the export target, and the export target starts receiving those golden records. 