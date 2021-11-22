---
layout: default
title: Searching for Data
parent: User Interface
nav_order: 080
permalink: /user-interface/searching-for-data
tags: ["ui","search"]
---

CluedIn provides a simple to use search over your data. This allows you to search through your data like you would run a Google Search. We also offer different ways to search through your data in a more "query" based way. The search for business users will allow them to search for "Marketing" and it will bring back all results that contain the word "Marketing" in any single attribute of the data and will order the results by relevance. Relevance for CluedIn is measured on many different properties of data including:

 - The number of term matches (the TFID from Elastic Search)
 - The recency of the data from a created date, discovered date or modified date with a logrithmic decay
 - The number of incoming edges to this record in the graph (density)
 - The number of properties that a record has
 - The Entity Type itself

 You can use the filters on the left hand side to filter your results by the automatic categorisation that CluedIn has given to the records. 

 By default, the search does not bring back results for Shadow Entities. If you need this, you will need to enable this in your container.config file. We also do not show records that are only from external data sources. Once again, you can enable this in your container.config if you need to be able to search through this data. We have disabled these by default as they often cause clutter and noise in the data. 

 You have different views of your data that you can choose within the CluedIn User Interface. 