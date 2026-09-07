---
layout: cluedin
title: Data Catalog
parent: Unsupported features
grand_parent: Archive
nav_order: 40
permalink: /archive/unsupported-features/data-catalog
content_type: reference
redirect_from: ["/governance/data-catalog"]
source_path: docs/070-governance/outdated/040-data-catalog.md
tags: ["governance","data-catalog"]
published: false
---

Using the Vocabularies in your integrations, CluedIn will automatically build you up a Data Catalog of all the properties that are available across all integrations that have been enabled in the platform. 

![Diagram](/assets/images/governance/intro-catalog.png)  

This means that the Catalog will give you a list of all property names, both Core and Provider Specific Vocabulary Keys that exist. This means that that these will be the exact property names that you will use to query data out of CluedIn. 

![Diagram](/assets/images/governance/list-view.png)  

You can set the details of each Vocabulary key in your Crawler Templates such as Data Type, Visibility, Description and more. You can also use this Data Catalog to be able to view the distribution of values you have for you Vocabulary Keys. They are available in the "Values" tab of an individual Vocabulary Key when you click on it in the user interface. 

![Diagram](/assets/images/governance/vocabulary-value-facets.png)  

Clicking on an individual value will take you to all records that have that value for that Vocabulary Key. 

You can filter your Data Catalog by the Entity Type, the source (e.g. HubSpot) or the type of Vocabulary it is e.g. Core, Provider.