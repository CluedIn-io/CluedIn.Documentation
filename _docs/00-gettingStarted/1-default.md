---
category: Get Started
title: CluedIn Overview
---

# Getting started

The following diagram depicts the main components of the CluedIn application with a reference architecture on Microsoft Azure. You can also see a reference architecture directly on the [Microsoft](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/data/cluedin) website. 

![Diagram](cluedin_arch.png)

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

### Installation

- For development and evaluation purposes [using Docker](/docs/00-gettingStarted/30-docker-local.html)
- For testing and production environments [using Kubernetes](/docs/00-gettingStarted/40-kubernetes.html)

### Integration

- [Build my first provider](/docs/10-Integration/build-integration.html)
