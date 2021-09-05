---
layout: default
title: All Properties
parent: User Interface
nav_order: 20
permalink: /user-interface/all-properties
tags: ["ui"]
---

This view will show you all meta data properties from all the source systems that have composed this record (entity). You can filter this list by the source system, the vocabulary groupings or the name of the property itself. 

By clicking on the "Clock" you can view the list of historical values for a particular property. For example, you could imagine that you might have the website for a company from multiple sources. Clicking on the clock icon will give you the list of all of those permutations of that value that have been mapped into the website Vocabulary. You can also see your data quality metrics that run at a property level in this view. This allows you to see the overall quality level of an individual property (such as the website) and you can even see the individual quality scores of each value.

If the Pencil icon is enabled, this means that you can edit this value from CluedIn and once submitted, this will generate the subsequent mesh api commands that will need to run against the source systems to proliferate this value into all systems where this value was retrieved in the first place. 

The Mask icon will allow you to anonymise the values in a particular property and will also generate the underlying Mesh commands that will be needed to anonymise these values in the source system as well.