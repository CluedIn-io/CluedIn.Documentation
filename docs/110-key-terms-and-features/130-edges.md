---
layout: cluedin
title: Edges
parent: Key terms and features
nav_order: 13
has_children: false
permalink: {{ site.baseurl }}/key-terms-and-features/edges
tags: ["development","edges"]
---

An edge is your way to be able to create relations between records. This relation will consist of a source and a target, or a "to" and a "from". In addition to an edge, you will have an edge type. This edge type will explain the relation (for example, /WorksFor, /LivesWith). Each edge can also contain properties including a weight and a general property bag. Weight is used to indicate the strength of the relation between two golden records. This weight is used in the processing pipeline to help evaluate decisions.

**How can you pass data to another record through an edge?**

There are many cases where you will denormalize references to other entities, but you do want to have some friendly values to reference these records. When you are creating your edges, you will notice that you can pass in extra properties on either the "from" reference or the "to" reference. Placing properties on these references will propagate these values onto the appropriate entity. For example, you created a clue for a company and it had a reference to a country via an ID. In this case, you would want to reference that country, but that country should bring back friendly values to the company clue so that it is easy to look at in the user interface. In this way, if you update the values in the country clue, then CluedIn will automatically update all references to this country. The properties are used only for passing vocabularies. By default, it will only copy these properties to the target reference when that target reference exists. 

**What are the edge types?**

Edges types are a way to determine the relations between data. This is typically in the structure of Object - Verb - Object. For example, John - works at - Lego. In CluedIn, edges can store properties such as weights and general metadata, but the main idea behind these edges is to describe the relation of two nodes for processing and querying purposes. 

In CluedIn, there are static edge types and dynamic edge types. Static edge types are your way to set an edge type based on known rules that will not change. All other edge types should be dynamic. 

It is always recommended to leave edges in crawlers as generic as possible and introduce new processors in the processing server to dynamically resolve generic edge types into specific ones. Imagine you have an edge type of "Works At" that you set statically in your crawlers - you can see that it has a temporal factor to it, in that you have no guarantee that this will always be "Works At". Due to this, you can introduce new processors that would check other values e.g. A Job start and end date, and use this to dynamically change the edge type to "Worked At" if this person was ever to leave.
