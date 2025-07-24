---
layout: cluedin
title: Deploying a New External Search Provider
parent: Development
nav_order: 120
has_children: false
permalink: {{ site.baseurl }}/development/deploying-search-provider
tags: ["development","search-providers"]
published: false
---

An External Search Provider will generate new binaries that will need to be hosted in CluedIn in run. This means that we need to be able to move *.dll files into the ServerComponentHost of CluedIn. It is simply a matter of copying the *.dll files from your External Search Provider into CluedIn. 

External Searches are only availble Globally or otherwise they are disabled. External Searches are not enabled through the CluedIn User Interface, but rather through configuration toggles. 

You will need to place respective API Tokens into the CluedIn Configuration files if your external search provider requires one. CluedIn does not ship with any API Tokens out of the box.