---
layout: cluedin
title: Data Part
parent: Development
nav_order: 350
has_children: false
permalink: {{ site.baseurl }}/development/data-part
tags: ["development","data-parts","clues"]
published: false
---

When a Clue becomes or is merged with an Entity, it becomes a "Data Part" of that Entity. This is a more smaller representation of a Clue that holds only the necessary parts for the Entity. 

This is important to know as sometimes you may want to transform data at a "Data Part" level instead of at an Entity Level. 

A good example would be cleaning of data. Imagine a situation where you have an Entity for a person that was composed of many Data Parts where one part said this persons age was 44 and another part said forty four. Even though the Golden Record Evaluator might have chosen 44 as the "best" value - it still means that if you went to clean this data at the Entity Level, you would only have the opportunity to clean the 44 value and not the "forty four". This is an example where instead of cleaning records at the entity level, you will want to do it at the data part level instead. 

You can view all the data parts of a record by viewing the "History" tab on the Entity Page. 