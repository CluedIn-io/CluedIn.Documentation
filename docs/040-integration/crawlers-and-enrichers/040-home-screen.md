---
layout: cluedin
title: Home Screen
parent: Crawlers and enrichers
grand_parent: Integration
nav_order: 040
has_children: false
permalink: /integration/home-screen
tags: ["integration","home-screen"]
---

Your integration Home Screen will give you details of how many data sources you have connected and actions to be able to add new integrations or configure existing sources. 

You will also be able to see information on the amount of data that is stored in CluedIn based off the data you have ingested. 

Your integration home screen will notify and alert you if there is a data source that has stopped working. This could be for many reasons, but it typically falls within:

 - The authentication has stopped working due to expiry of authentication tokens or change in authentication.
 - The configuration needs attention e.g. a data source has moved location and will need to be updated to support a new source location.
 - An Administrator has paused or stopped the integration.

 CluedIn will maintain the state of when the integration has stopped working and so on resolution, we know exactly the offset or point in time in which we need to sync data to get it back to a 100% sync state. 