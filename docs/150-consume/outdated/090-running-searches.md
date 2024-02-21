---
layout: cluedin
title: Running Searches
parent: Consume
nav_order: 90
permalink: /consume/running-searches
tags: ["consume","search"]
published: false
---

CluedIn allows you to run searches on the data that exists within your account that (by default) is not only from External Data Sources or that is not a Shadow Entity. 

The search supports Full Text Querying with a Fuzzy Search and an Exact Match. To run a Fuzzy Search, simply type the word or words in that you want to search for. For exact match searches, you will need to surround your search with "" e.g. "CluedIn Sales".

![Diagram](../assets/images/consume/results.png)

The results that are returned are sorted by Relevance by default and one can change the sort order to either New or Old. The New or Old sort order is based off a rule that is as follows:

- If the record does not have a created or modified date, then it will use the date that CluedIn first saw the record. 
- If the record has a Modified date, created date and discovery date, then the one that is the highest of those three will be the one that CluedIn will user to sort by. 

You have many ways to display your results, in the form of different "views".

![Diagram](../assets/images/consume/entity-type-views.png)

The inbuilt filters can be used to filter your data even more. You can apply multiple filters. 

![Diagram](../assets/images/consume/additional-filters.png)

You can also run advanced searches will the ability to filter on very specific Vocaularies.

![Diagram](../assets/images/consume/advanced-search-filters.png)