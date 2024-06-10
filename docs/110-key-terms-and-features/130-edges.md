---
layout: cluedin
title: Edges
parent: Key terms and features
nav_order: 13
has_children: false
permalink: /key-terms-and-features/edges
tags: ["development","edges"]
---

An Edge is your way to be able to create relationships between records. This relationship will consist of a source and a target, or a "to" and a "from". As well as this, you will have an Edge Type. This Edge Type will explain the relationship e.g. /WorksFor, /LivesWith. Each edge can also contain properties including a Weight and a general property bag. 

When you are creating edges in your solution, you will also notice that you can set a "Weight". This value is to indicate the strength of the relationship between two entities. This weight is used in the processing pipeline to help evaluate decisions.

## How do I pass data to another record through and edge

There are many cases where you will denormalize references to other entities, but you do want to have some friendly values to reference these records. When you are creating your edges, you will notice that you can pass in extra properties on either the "from" reference or the "to" reference. Placing properties on these references will propagate these values onto the appropriate entity. For example, if you were creating a clue for a company and it had a reference to a country via an Id. In this case you would want to reference that country, but that the country bring back friendly values to the company clue so that it is easy to look at in the user interface. In this way, if you update the values in the country clue then CluedIn will automatically update all references to this country. The properties is only for passing Vocabularies. By default, it will only copy these properties to the target reference when that target reference exists. 

## Edge types

Edges Types are a way to determine the relationships between data. This is typically in the structure of a Object - Verb - Object. For example, John - works at - Lego. In CluedIn, edges can store properties such as weights and general metadata, but the main idea behind these edges is to describe the relationship of two nodes for processing and querying purposes. 

In CluedIn, there are static Edge Types and Dynamic Edge Types. Static Edge Types are your way to set an Edge Type based off known rules that will not change. All other Edge Types should be Dynamic. 

It is always recommended to leave Edges in crawlers as generic as possible and introduce new processors in the processing server to dynamically resolve generic edge types into specific ones. Imagine you have an edge type of "Works At" that you set statically in your crawlers - you can see that it has a temporal factor to it, in that you have no guarantee that this will always be "Works At". Due to this, you can introduce new processors that would check other values e.g. A Job start and end date, and use this to dynamically change the edge type to "Worked At" if this person was ever to leave.
