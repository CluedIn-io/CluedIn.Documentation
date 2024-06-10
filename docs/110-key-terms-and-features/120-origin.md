---
layout: cluedin
title: Origin
parent: Key terms and features
nav_order: 12
has_children: false
permalink: /key-terms-and-features/origin
tags: ["development","clues"]
---

The Origin of a Clue determines the lineage of source. Dependent upon the use case, you might find that sometimes your Origin will differ based off different fields. For example, imagine you are pulling data in from Microsoft Dynamics, but you are aware that one of the fields on a Lead object in Microsoft Dynamics actually comes from a particular Oracle database. It is fine to be able to set the Origin of this Clue to a hybrid of Oracle and Microsoft Dynamics.  This will also help CluedIn reconstruct the full data lineage path of where data comes from and where it flows. You can solve this in two ways, but there is a preferred way. We would rather receive two clues - one that contains all the Dynamic sourced data and the Oracle data, the other that ONLY contains the Oracle data. In this way, we can show that the data has come from both systems and exists in both systems.

An Origin can be any value, but typically it will be the name of the source system where you are pulling data from e.g. HubSpot, Microsoft Dynamics, Oracle, Workday. 