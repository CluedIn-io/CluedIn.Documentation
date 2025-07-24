---
layout: cluedin
title: Datastores
parent: Development
nav_order: 080
has_children: false
permalink: {{ site.baseurl }}/development/datastores
tags: ["development","data-stores"]
published: false
---

The concept of a Datastore in CluedIn is a place to persist a permutation of the data that is crawled into a purpose-fit format. CluedIn has 5 different datastores that it uses by default to persist any data that flows through the processing engine. A developer doesn’t have a choice over which datastores data will persist to, CluedIn will decide this based off that it deems most suitable. One can add new datastores and even new datastore types, but by default CluedIn ships with support for a:

* Native Graph Store
* Search Store
* Relational Store
* Distributed Cache Store
* Blob Store

Developer may also change the implementation of these stores if desired, but CluedIn will natively ship with support for:

* Neo4j Community Edition as the Graph Store
* ElasticSearch Enterprise Edition as the Search Store
* Redis as the Distributed Cache Store
* SQL Server Community Edition as the Relational Store
* SQL Server Community Edition as the Blob Store

CluedIn also provides a messaging queue backbone for delivering discrete messages in-between the different micro-services of CluedIn, but also uses this queue as a robust delivery mechanism for delivering Clue objects to the processing server from Crawlers. Although we offer our REST API as the delivery endpoint for posting Clue objects, we do provide integration templates via C#, .net templates, that will allow you to directly talk to the messaging queue. CluedIn ships with RabbitMQ as the default implementation of this messaging queue. 

During processing, your Datastores will constantly be queried and written to. Because of this we have different queues that are responsible for different interactions with the Datastores. 

To access your Data Stores via our REST API, you are best to use the GraphQL api. To access it from C#, you can access all of these Data Stores from your ExecutionContext object.

ExecutionContext.Organisation.DataStores.Graph will give you access to be able to directly run queries against the Graph. 