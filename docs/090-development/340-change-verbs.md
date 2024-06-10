---
layout: cluedin
title: Change Verbs
parent: Development
nav_order: 340
has_children: false
permalink: /development/change-verbs
tags: ["development","clues"]
published: false
---

On each Clue, the Change Verb can be used to flag to CluedIn what type of "event" this Clue is referring to. This is typically only necessary when data is being pushed to CluedIn and can be used as a way to indicate to CluedIn on how to process this data. 

Imagine a situation where you have a record deleted in a source system and you would like CluedIn to also reflect this deletion in it and any downstream consumer. This Change Verb can be used to manage this. It might be that you would like to mark this as a deletion in CluedIn but maintain the history, or it might be that you want to actually delete the related record in CluedIn. 

When you are using the prebuilt connectors of CluedIn, it is not expected to set this value, in fact in a lot of cases you don't know that they data you are receiving is an addition or a change (unless that source system gives you that metadata).