---
layout: cluedin
title: Entity type
parent: Key terms and features
nav_order: 9
has_children: false
permalink: /key-terms-and-features/entity-type
tags: ["development","entities","entity-types"]
---

An entity type indicates a specific business domain for data. It can represent physical objects, individuals, locations, and so on. An entity type should be global, timeless, and not bound to a specific data source (for example, Person, Organization, Car).

A golden record can have only one entity type. You can use built-in entity types or can create your own custom entity types.

An entity type is assigned to a clue when the mapping is created. It is an important element of codes (entity origin code and entity codes).

**Entity type and codes**

An entity type is a foundational element used in the generation of codes. It always appears as the first part of any code.

**Entity type format**

An entity type always starts with a slash (/). CluedIn has a nested hierarchy of entity types that are separated by slashes. For example, “/Sales/Deal” indicates that the “Deal” entity type is a child of the “Sale” entity type.