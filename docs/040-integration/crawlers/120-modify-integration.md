---
layout: default
title: Modify an Integration
parent: Crawlers
grand_parent: Integration
nav_order: 120
has_children: false
permalink: /integration/modify-integrations
tags: ["integration"]
---

There will be many times where you will need to change an integration. This may be due to changes in the source, changes in versions or fixing mistakes. 

There are some situations where you may need to cleanup changes. These include:

 - You change the name of a Vocabulary Key
 - You need to remove edges
 - You need to change existing edges
 - You need to remove Vocabularies

 Due to CluedIn being a append-only system (with support for deleting if necessary) it means that certain changes require cleanup. 

 For removing or changing edges, you can use the "ObsoleteSince" extension method to instruct to CluedIn that since a particular Version if your Crawlers, you had an edge, and after the case you need to remove or change the data in the edge. 

 If you do this, this CluedIn will do the cleanup for you. You can also perform this using Post Processors. If you decide to do it in your CluedIn Crawlers then it means that your Crawlers might become a bit harder to manage. If you solve it in Post Processing, then you make sure that your crawlers always stay business-logic-agnostic. 

 For changing or removing Vocabulary Key Names, the same method applies. There is the "ObsoleteSince" extension methods available on the VocabulayKey class which will allow you to instruct CluedIn to cleanup the mistakes. 

