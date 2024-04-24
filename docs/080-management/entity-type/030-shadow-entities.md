---
layout: cluedin
title: Shadow entities
parent: Entity type
grand_parent: Management
nav_order: 3
has_children: false
permalink: /preparation/shadow-entities
published: false
tags: ["management","shadow-entities"]
---

In an effort to remove "noise" from your CluedIn data, we have the idea of "Shadow Entities". A Shadow entity is a record that exists in the datastores but has been flagged as a record that will be hidden from the results in your data access layers of CluedIn. This is based off the "Eventual Connectivity" pattern in that this Shadow Entity may turn into a real Entity when it is exposed to new and more data. 

If you find that you are ingesting data and you expect a result to show up in the search catalog (and it does not), chances are it is a Shadow Entity. Shadow Entities are usually constructed from "Unstructured Text" i.e. we have a reference to a Person or Company that is only a "soft" reference. 

Shadow Entities are also constructed when the "Eventual Connectivity" patterns constructs an edge to an Entity via an Entity Code and that Entity Code doesn't not exist in any other data source yet. 

![Diagram](../assets/images/preparation/intro-shadow-entity.png)

The Shadow Entity Center is the User Interface that CluedIn provides in which a Data Steward can manually link Shadow Entities to Entities. The main use-case of this is when we find a "soft" reference to a Person or Company in unstructured text and the Data Steward knows the exact Entity that this can be linked to or merged with. 

The idea behind a Shadow Entity is key to our Data Integration Pattern (Eventual Connectivity). Think of it like a placeholder to a reference that doesn't exist yet - but we think it will in the future.

A Shadow Entity is "essentially" an Entity Code reference and hence like an Entity Code it will have a Type, Origin and Id. There are many Shadow Entities that will have an Id such as

1234567
Some Guid
82901848093485
These types of Shadow Entities are not the main focus of this Shadow Entity UI tool. The other types of Shadow Entities that are common are references to People and Companies such as:

Sitecore
Tim Ward
Timothy Ward
sig@cluedin.net
This could be generated from Crawlers, but a majority of the time it is generated from the NER (Named Entity Recognition) process of processing text to try and attempt to find references to "Objects". CluedIn currently does this for companies, locations, people and a few other object types.

These will also cause Entity Codes but a special type of Entity Code (name Entity Codes) that doesn't act as a unique reference to an Object. Hence you will have many of these in an account (especially if you crawl files) and they will rarely be able to find a link or merge with another Entity based off these codes. Because of this, a Data Steward will need to manually link these up.

Imagine the situation where there is a reference to a "Tim Ward" or even a "Tim" in a Word document. It is hard, and in some cases close to impossible to know which Tim or Tim Ward you are referring too. If a human was to read the text and see the context then they might be able to tell or have a good guess - but more importantly if someone that is "close" to the data in the Graph might be better to add context around this "Soft reference". Even better, if we chose 2 or 3 people that are "close" to the data - that between them they could probably agree on who this "Tim" or "Tim Ward" is.

It might be that these 2 or 3 people are not users of the CluedIn platform and hence they will never have the option of adding context because they don't have access to CluedIn. Because of this CluedIn will choose the next most relevant people in line that DO have a user account in CluedIn, they will be the ones that are sent the data to label.

In the picture above I can explain what needs to be shown on the screen for this to be useful.

1: General Meta Data on the Shadow Entity reference that is "soft".
2: The name of the Shadow Entity.
3: The text or content where the Shadow Entity reference was found.
4: A list of REAL Entities that are possible matches to the soft reference (you can only choose one)
5: The ability to go to the next, back or skip.

The UI picture is only a quick "mockup" but as you can imagine it would also be nice to be able to:

1: Click on a real entity and see more details.
2: Click on the "Content" (3) and see more details on that Entity (3)
3: See a Graph/Network of the records that are connected to the Entity (3) and even a Shortest Path between the Shadow Entity (1) and the list of REAL entities (4)

To build the UI you will need to use the following backend endpoints

```CSharp
GET [Route("api/v1/shadow/all")]
public async Task Get(string entityType, int page, int take)
```

This will allow you to page through the Shadow Entities, probably 20 at a time. As you can see you can also filter by entityType e.g. "/Organization" but if you don't specify one then "/Organization" will be chosen by default.

When you select a record (4) and you want to merge it with the Shadow Entity you will want to use the Entity (4) as the Target and the Shadow Entity as the Source and call the Merge endpoint that already exists in the platform and that is in use on the Search page when you click the "Merge" button.

There is no need for delete endpoints as once the merge is finished, that Shadow Entity will no longer be a shadow Entity. You will also notice that in the GET call that I return the TOTAL amount of Shadow Entitles which allows you to serve the data for a Notification on the homescreen but also know how many records you need to page through to finish.

The final question you might have is "How do I get the content for the Content (2) part of the UI?"

For this, we are using the Highlights that come from Elastic Search to allow you to see where we found a reference to this person. This comes back in the GET response.