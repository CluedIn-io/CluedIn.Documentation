---
category: Consume
title: Configuration Search Relevance
---

The full text search component of CluedIn can be tweaked for relevance and ordering. This can be done by utilising the CluedIn Rest API and calling the Search Settings Endpoint with the appropriate scores and values. The range of scoring can be made between the value 0 and 10 with 0 being a low boost and 10 being the highest boost. For example, if you wanted to naturally boost records that were more connected in the graph, then you could put a stronger weight on that component. 