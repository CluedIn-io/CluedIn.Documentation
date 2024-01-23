---
layout: cluedin
title: Entity Type Translation
parent: Preparation
nav_order: 80
has_children: false
permalink: /preparation/entity-type-translation
tags: ["preparation"]
---


Similar to Edge Types, there are many times where you will find that determining the type of data you are ingesting cannot be known upfront or it is not static in nature. Because of this, Entity Type Translation allows you to change the type of data at processing time. For example, CluedIn uses this engine by default to transform /Infrastructure/User clues into /Person or /Contact or maybe even a /Service/Account. This is due to the nature of data in source systems often being mixed and a more specific typing needs more analysis to determine the fact. 

For example, if you were bringing in an /Infrastructure/User and you found that the FirstName and LastName were both valid person names, that an Age was set and that they also had a record in the HR system, then this would allow you to transform this into a /Person object. 