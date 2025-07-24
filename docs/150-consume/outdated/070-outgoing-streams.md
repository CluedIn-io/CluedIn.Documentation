---
layout: cluedin
title: Outgoing Streams
parent: Consume
nav_order: 70
permalink: {{ site.baseurl }}/consume/outgoing-streams
tags: ["consume","streams"]
published: false
---

It is often the case the introducing new platforms like CluedIn can be thought of as quite "disruptive" i.e. our teams need to learn a new system and query language to be able to interact with the data. 

Although we offer our GraphQL api to "pull" data from CluedIn, we often recommend and prefer that you "push" the data from CluedIn to a target consumer. We call these out "Outgoing Streams" in which a CluedIn user will specify the filter of data that a consumer needs and a target and target model and CluedIn will open up a "long-running" stream of data that matches that filter in CluedIn today and in the future until you turn the stream off. 

You may want to be able to push data to a SQL Database.

![Diagram](../assets/images/consume/stream1.png)

This screenshot shows that you can setup a Filter. The Filter is your predicate or query for what data you are wanting to push out on this stream. Because CluedIn persists data, this will fetch historical data as well as new records that match this predicate. 

The Rules part of the user interface allows you to apply transformations to the data on the way out of the stream. Imagine a situation where you would like to Mask the data as it goes out on the stream - this will allow you to do that. 

The Export Target Configuration is your ability to control the projection that happens on the stream i.e. what properties from a record you push to the target. 

The Data tab shows you a history of the records that have been sent out on this stream so that you can trace the full lineage of the platform. 