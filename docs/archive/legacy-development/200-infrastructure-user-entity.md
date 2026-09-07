---
layout: cluedin
title: Infrastructure User Entity Type
parent: Legacy development documentation
grand_parent: Archive
nav_order: 200
permalink: /archive/legacy-development/infrastructure-user-entity
content_type: reference
redirect_from: ["/development/infrastructure-user-entity"]
source_path: docs/090-development/230-infrastructure-user-entity.md
tags: ["development","entities","entity-types"]
published: false
---

The Infrastructure User Entity Type is for a Clue where it is ambiguous what the Entity Type of a record is. It is mainly reserved for the following types of Entity Types where you cannot statically set a type:

 - Contact
 - Person
 - Group

You should use this Entity Type when you are not guaranteed that the data your are pulling, represents a Person and you would like CluedIn to do some extra processing to determine it for you. Examples could include:

 - If you have mapped a Birthday of a record into the Core Person Vocabulary and it has a valid Birthday, then CluedIn will change this into a Person from an Infrastructure User. 
 - If you have a valid First Name and Last Name then this will be changed into a Person.
 - If a Gender is set then this will change into a Person. 
 - If an age is set then this will change into a Person. 