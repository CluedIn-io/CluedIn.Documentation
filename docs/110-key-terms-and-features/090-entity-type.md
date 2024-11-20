---
layout: cluedin
title: Entity type (Business Domain)
parent: Key terms and features
nav_order: 9
has_children: false
permalink: /key-terms-and-features/entity-type
tags: ["development","entities","entity-types"]
---

An entity type represents a specific business domain for data. It can signify physical objects, individuals, locations, and more. Entity types should be **global**, **timeless**, and **independent of specific data sources** (e.g., Contact, Organization, Car).

Each golden record is associated with exactly one entity type. You can leverage built-in entity types or define your own custom entity types.

An entity type is assigned to a clue during the mapping process and plays a critical role in various codes, including entity origin codes and entity codes.

## Where Is Entity Type Used?

### Adding Semantic Context to Golden Records

The entity type provides **metadata**, such as a display name, icon, and descriptions, adding a semantic layer to golden records.

Golden records sharing the same entity type inherently share the same "semantic meaning."

When defining entity types, it’s essential to balance specificity and genericness. Use terminology familiar to your line of business (LOB) to help identify records intuitively.

{:.important}
Tip: CluedIn is flexible—if you choose an initial entity type that needs adjustment, you can change it. However, changing entity types mid-project can be cumbersome, especially if deduplication projects, rules or streaming configurations have already been applied.

### Filtering Golden Records

Entity type acts as the default filter for many operations in CluedIn. Selecting the right entity type allows you to target groups of golden records that logically belong together.

### Origin Entity Code (Primary Identifier)

Entity type forms part of the primary identifier value. This structure enforces that records can only merge if they share the same entity type.

## Entity Type Properties and Characteristics

### Why Do I See a Slash (/) in Front of an Entity Type?

Entity types have a unique code, represented as a simple string prefixed by a slash (/).

The code uniquely identifies the entity type.

Use concise, meaningful names for codes, avoiding non-alphanumeric characters where possible.

### Nested Entity Types

CluedIn supports nested entity types, allowing hierarchical organization of entity types. While not mandatory, this feature can help group entity types of the same nature.

Example of Nested Entity Types
```
/Document
/Document/XLS
/Document/Video
/Document/Audio
```

In this hierarchy, Video is a child of Document:

#### Benefits of Nested Entity Types

1. **Grouping Filters**: Nested entity types allow you to filter or stream entities collectively.
For instance, using a filter such as starts with /Document would include all documents, regardless of their specific sub-entity type.

2. **Streamline Reporting**: Nested types simplify reporting and analysis across related entity types.

## Useful Resource for Entity Type

- [Add or modify Entity Type](/management/entity-type)
