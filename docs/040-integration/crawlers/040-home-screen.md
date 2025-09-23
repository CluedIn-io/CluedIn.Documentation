---
layout: cluedin
title: Home Screen
parent: Crawlers
grand_parent: Ingestion
nav_order: 040
has_children: false
permalink: /integration/home-screen
tags: ["integration","home-screen"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

The integration Home Screen provides an overview of your integrations, including:

- The number of connected data sources.

- Actions to add new integrations or configure existing ones.

- Information on the amount of data stored in CluedIn based on what you have ingested.

## Notifications and alerts

The Home Screen also notifies you if a data source has stopped working. Common reasons include:

 - Authentication issues – Expired tokens or changes in authentication methods.

 - Configuration changes – For example, a data source has moved and needs updating.

 - Administrative actions – An administrator has paused or stopped the integration.

## State management

CluedIn maintains the state of integrations when they stop working. Once the issue is resolved, CluedIn automatically knows the correct offset (point in time) to resume syncing, ensuring data is restored to a 100% sync state.