---
layout: default
title: Getting Started
nav_order: 10
has_children: true
permalink: /getting-started
---

{: .fs-6 .fw-300 }

## CluedIn Architecture

CluedIn is made up of various functional layers, all encapsulated into their own [Docker](https://www.docker.com/) containers.

### CluedIn Applications

We have a combination of microservices running on .Net Core that handle various distinct functions, from handling the UI, to queuing and processing the large streams of data we need to ingest. 

### CluedIn Security

This handles how we connect securely to the cluster and handle permissions and grants to the different services the system is made up of.

### CluedIn Data

- Neo4j - Manages complex relationships between CluedIn data objects ("Clues"). 
- SqlServer - Manages our relational data storage. Alternatively a SAAS option (like SQL Azure) can be used.
- ElasticSearch - Indexes and searches the data for flexible querying. This can be scaled out as needed. 
- RabbitMQ - The servicebus that handles queueing across the system.
- Redis - Used as the cache for the system.

Notice all the communication from the browser into the application comes through a set of ingress definitions (i.e. only a single public IP is required). The communication will all run over SSL in a production environment. 


