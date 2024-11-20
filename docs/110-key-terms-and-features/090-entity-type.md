---
layout: cluedin
title: Entity type
parent: Key terms and features
nav_order: 9
has_children: false
permalink: /key-terms-and-features/entity-type
tags: ["development","entities","entity-types"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

An entity type represents a specific business domain for data. It can signify physical objects, individuals, locations, and more. Entity types should be **global**, **timeless**, and **independent of specific data sources** (e.g., Contact, Organization, Car).

Each golden record is associated with exactly one entity type. You can leverage built-in entity types or define your own custom entity types.

An entity type is assigned to a clue during the mapping process, and it plays a critical role in various [codes](/key-terms-and-features/entity-codes), including entity origin codes and entity codes.

## Entity type usage

### Adding semantic context to golden records

The entity type provides **metadata**, such as a display name, icon, and description, adding a semantic layer to golden records. Golden records sharing the same entity type inherently share the same semantic meaning.

When defining entity types, it’s essential to balance specificity and genericness. Use terminology familiar to your line of business (LOB) to help identify records intuitively.

{:.important}
CluedIn is flexible—if you choose an initial entity type that needs adjustment, you can change it. However, changing entity types mid-project can be cumbersome, especially if deduplication projects, rules, or streaming configurations have already been applied.

### Filtering golden records

Entity type acts as the default filter for many operations in CluedIn. Selecting the right entity type allows you to target groups of golden records that logically belong together.

### Producing entity origin code (primary identifier)

Entity type forms part of the primary identifier value. This structure enforces that records can only merge if they share the same entity type.

## Entity type properties and characteristics

### Entity type code

Entity types have a unique code, represented as a simple string prefixed by a slash (/). The code uniquely identifies the entity type. That is why you see a slash (/) in front of an entity type.

To create an entity type code, use concise, meaningful names and avoid non-alphanumeric characters where possible.

### Nested entity types

CluedIn supports nested entity types, allowing hierarchical organization of entity types. While not mandatory, this feature can help group entity types of the same nature.

**Example of nested entity types**

In the following hierarchy, Video is a child of Document.

```
/Document
/Document/XLS
/Document/Video
/Document/Audio
```

**Benefits of nested entity types**

- **Filter grouped entities** – nested entity types allow you to filter or stream entities collectively. For example, using a filter that starts with /Document would include all documents, regardless of their specific sub-entity type.

- **Streamline reporting** – nested types simplify reporting and analysis across related entity types.

## Useful resources

- [Add or modify an entity type](/management/entity-type)