---
layout: default
title: Edges
parent: Development
nav_order: 370
has_children: false
permalink: /development/edges
tags: ["development","edges"]
---

An Edge is your way to be able to create relationships between records. This relationship will consist of a source and a target, or a "to" and a "from". As well as this, you will have an Edge Type. This Edge Type will explain the relationship e.g. /WorksFor, /LivesWith. Each edge can also contain properties including a Weight and a general property bag. 

When you are creating edges in your solution, you will also notice that you can set a "Weight". This value is to indicate the strength of the relationship between two entities. This weight is used in the processing pipeline to help evaluate decisions.

## How do I pass data to another record through and edge

There are many cases where you will denormalise references to other entities, but you do want to have some friendly values to reference these records. When you are creating your edges, you will notice that you can pass in extra properties on either the "from" reference or the "to" reference. Placing properties on these references will propagate these values onto the appropriate entity. For example, if you were creating a clue for a company and it had a reference to a country via an Id. In this case you would want to reference that country, but that the country bring back friendly values to the company clue so that it is easy to look at in the user interface. In this way, if you update the values in the country clue then CluedIn will automatically update all references to this country. The properties is only for passing Vocabularies. By default, it will only copy these properties to the target reference when that target reference exists. 
