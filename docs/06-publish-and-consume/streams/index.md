---
layout: cluedin
title: Streams
parent: Publish & consume
nav_order: 20
has_children: true
permalink: /publish/streams
content_type: landing
summary: "A stream is a continuous export: you define which golden records and which properties, point it at an export target, and CluedIn keeps the target up to date as the data changes."
list_children: false
redirect_from: ["/consume/streams"]
source_path: docs/150-consume/002-streams.md
tags: ["consume", "data export", "streams"]
last_modified: 2024-01-15
---

When you have the ready-to-use data in CluedIn, you can send it to any external system where the data can be used for executing various business tasks.

The following diagram shows the basic steps of sending the records from CluedIn to an external system.

![streams.gif]({{ "/assets/images/consume/streams/streams.gif" | relative_url }})

When you start the stream, all records matching the stream's filters will be sent to the external system (target). If new records appear in CluedIn and they match the stream's filters, they will be automatically sent to the target. In addition to that, if you make any changes to the records in CluedIn—for example, fix some values by running a [clean project](/govern/cleaning)—these changes will be automatically made in the corresponding records stored within the target.

This section covers the following areas:

- [Creating a stream](/publish/streams/create-a-stream) – learn how to create a stream, configure the export target for the stream, and define which golden records and specific properties to send to an external system.

- [Managing streams](/publish/streams/manage-streams) – learn how to edit a stream and work with the stream controls, as well how these actions affect the stream.

- [Reference information about streams](/publish/streams/stream-reference) – find information about stream statuses and other stream indicators.