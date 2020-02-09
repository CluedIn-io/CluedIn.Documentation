---
category: Preparation
title: Aggregation
---

CluedIn has a processing pipeline that takes Clue objects and runs processing over them to turn into entities. It is through this process that data is matured, enriched and much more. One process that typically is required is to aggregate or calculate functions at processing time. This could be as simple as calculating two values and persisting the calculated value into a new property. This could be as complex as running Graph Queries at processing time that will calculate what clusters or graph patterns are in the data so that at query time, the results are already prepared. 

CluedIn has a specific processing pipeline to handle aggregations. 