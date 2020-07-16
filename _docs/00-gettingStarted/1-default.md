---
category: Get Started
title: CluedIn Overview
---

# Getting started

The following diagram depicts the main components of a CluedIn application. ![Diagram](cluedin_arch.png)

## CluedIn architecture

CluedIn is made up of various functional layers.

### CluedIn Applications

We have a combinations of microservices running on .Net Core and NodeJS that handle various distinct functions, from handling the UI, to queuing and processing the large streams of data we need to ingest. 

### CluedIn Security

This handles how we connect securely to the cluster and handle permissions and grants to the different services the system is made up of.

### CluedIn Data

- Neo4j - Manages complex relationships between CluedIn data objects ("Clues")You can either use the open source version, limited a single server, or the commercial version (if you required a cluster for extra resilience or performance).
- SqlServer - Manages our relational data storage. Free developer editions are sufficient. It can run in Windows or Linux. Alternatively a SAAS option (like SQL Azure) can be used.
- ElasticSearch - Indexes and searches the data for flexible querying. This can be scaled out as needed. 
- RabbitMQ - The servicebus that handles queueing across the system.
- Redis - Used as the cache for the system.

The diagram shows the different communication paths within the application.

Notice all the communication from the browser into the application comes through a set of ingress definitions (i.e. only a single public IP is required). The communication will typically be all over SSL. The traffic for the CluedIn.App component will have the SSL terminated at the ingress (so you could use CertManager, for example, to roll the certificates automatically). Traffic for the CluedIn API must be SSL and is terminated on the API (passing through the ingress). This means the correct certificates need to be managed manually and assigned to the CluedIn API component.

### Installation

- For development and evaluation purposes [using Docker](/docs/00-gettingStarted/docker-local.html)
- For testing and production environments [using Kubernetes](/docs/00-gettingStarted/kubernetes.html)

### Integration

- [Build my first provider](/docs/10-integration/index.html)
