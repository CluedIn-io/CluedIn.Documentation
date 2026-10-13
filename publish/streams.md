---
title: Streams
url: https://documentation.cluedin.net/publish/streams
content_type: landing
section: Publish & consume
---

# Streams

When you have the ready-to-use data in CluedIn, you can send it to any external system where the data can be used for executing various business tasks.

The following diagram shows the basic steps of sending the records from CluedIn to an external system.

![Diagram of sending data from CluedIn to other systems in three steps: 1 create a stream with a filter for golden records, 2 configure an export target by choosing a connector and properties, 3 start streaming records to the export target](https://documentation.cluedin.net/assets/images/consume/streams/streams.gif)

When you start the stream, all records matching the stream's filters will be sent to the external system (target). If new records appear in CluedIn and they match the stream's filters, they will be automatically sent to the target. In addition to that, if you make any changes to the records in CluedIn—for example, fix some values by running a [clean project](https://documentation.cluedin.net/govern/cleaning.md)—these changes will be automatically made in the corresponding records stored within the target.

This section covers the following areas:

- [Creating a stream](https://documentation.cluedin.net/publish/streams/create-a-stream.md) – learn how to create a stream, configure the export target for the stream, and define which golden records and specific properties to send to an external system.

- [Managing streams](https://documentation.cluedin.net/publish/streams/manage-streams.md) – learn how to edit a stream and work with the stream controls, as well how these actions affect the stream.

- [Reference information about streams](https://documentation.cluedin.net/publish/streams/stream-reference.md) – find information about stream statuses and other stream indicators.

## In this section

- [Concept of a stream](https://documentation.cluedin.net/publish/streams/concept-of-a-stream.md) (concept): In this article, you'll learn about the process of sending golden records from CluedIn to the export target.
- [Create a stream](https://documentation.cluedin.net/publish/streams/create-a-stream.md) (how-to): Create a stream when you want to send golden records from CluedIn to an external system (for example, a Microsoft SQL Server database) and keep sending them as they change.
- [Manage streams](https://documentation.cluedin.net/publish/streams/manage-streams.md) (how-to): In this article, you will learn how to manage streams to keep the entire process of delivering data to external systems efficient, well-organized, and aligned with your data management objectives.
- [Stream reference](https://documentation.cluedin.net/publish/streams/stream-reference.md) (reference): In this article, you will find reference information to help you understand stream statuses and other stream indicators.
- [Stream logs](https://documentation.cluedin.net/publish/streams/stream-logs.md) (how-to): In this article, you will learn how to ensure that your golden records have been successfully exported and how to identify issues when something goes wrong.
- [Tutorial: stream data](https://documentation.cluedin.net/publish/streams/tutorial-stream-data.md) (tutorial): Streaming data from CluedIn involves setting up an export target and creating a stream.

Up: [Publish & consume](https://documentation.cluedin.net/publish.md)
