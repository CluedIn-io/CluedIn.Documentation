---
layout: cluedin
title: Aggregation
parent: Preparation
nav_order: 10
has_children: false
permalink: preparation/aggregation
tags: ["preparation","aggregation"]
published: false
---

CluedIn has a processing pipeline that takes Clue objects and runs processing over them to turn into entities. It is through this process that data is matured, enriched and much more. One process that typically is required is to aggregate or calculate functions at processing time. This could be as simple as calculating two values and persisting the calculated value into a new property. This could be as complex as running Graph Queries at processing time that will calculate what clusters or graph patterns are in the data so that at query time, the results are already prepared. 

![Diagram](../assets/images/preparation/intro-aggregation.png)

CluedIn has a specific processing pipeline to handle aggregations. 