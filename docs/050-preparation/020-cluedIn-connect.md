---
layout: default
title: CluedIn Connect
parent: Preparation
nav_order: 20
has_children: false
permalink: /preparation/cluedin-connect
tags: ["preparation","cluedin-connect"]
---

Whereas your crawlers are responsible for fetching data from datasources and creating edges. It is not the responsiblity of the crawlers to determine what type of relationship that linkage is. This is due to the nature that determining this is usually not static in nature and can sometimes take complex calculations to determine. Hence it is alwasy best practice to specify simple edge types in crawlers and then rules can be set in CluedIn Connect to run the smarts.

This is also due to the fact that you might need to query other data from other systems to properly be able to determine what type of relationship exists between two records. 

The simple edge types include:

 - Parent
 - PartOf

 CluedIn connect will help you build rules that determine what strongly typed relationship should be constructed. A simple example would be an edge type that has a temporal factor to it e.g. past, present, future. If we statically were to create a relationship of type /WorksFor from a Person to an Organization then chances are this data might not be current and hence the relationship could actually be /WorkedFor or /SoonWorkFor. The good thing is that other metadata available might be able to help us dynamically determine these edge types. For example, you might connect your HR system to CluedIn in which it will have the start date and end date of employment. Using the rules engine in CluedIn Connect you could determine that if the employment date is within this time frame then you could also determin the relationship type beteen these two records. 

 CluedIn Connect also specifies the ability to have complex processors that can use more than just simple rules to determing edge types. You might find that you will want to use Natural Language Processing to determine the edge type between two records.