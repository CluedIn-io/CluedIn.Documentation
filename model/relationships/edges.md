---
title: Relationships (edges)
url: https://documentation.cluedin.net/model/relationships/edges
content_type: concept
section: Model > Relationships
---

# Relationships (edges)

> concept: Explains how something works.

An edge defines a relation between two records in CluedIn.

- Each edge connects a source and a target (also referred to as "from" and "to").

- Each edge has an edge type that explains the nature of the relation (for example, /WorksFor, /LivesWith).

- Edges can also include properties, such as:

    - Weight – Indicates the strength of the relation between two Golden Records. Used in the processing pipeline to influence decision-making.

    - Property bag – Stores additional metadata about the relation.

## Passing data through an edge

Edges can also be used to propagate data between related records.

- Often, you will denormalize references to other entities but still want user-friendly values for display.

- When creating an edge, you can attach extra properties to either the "from" or "to" reference.

- These properties are propagated to the connected entity and are typically used for passing vocabularies.

Consider this example:

- A company record references a country by an ID.

- Through the edge, the company record can also display friendly country values in the UI.

- If the country record is updated, CluedIn automatically updates all references to that country.

> **Important:** By default, CluedIn copies these properties only to the target reference, and only if that reference exists.

## Edge types

An edge type defines the kind of relation between two records, typically expressed in the structure: Object – Verb – Object. For example: John – works at – Lego

In CluedIn, edge types can also store metadata such as weights and properties, but their primary purpose is to describe and query relationships between nodes.

## Static vs. dynamic edge types

- Static edge types – Defined by fixed rules that do not change.

- Dynamic edge types – More flexible, determined at runtime based on additional conditions.

> **Important:** The best practice it to keep edge types in crawlers as generic as possible. Use processors in the processing server to resolve them dynamically into specific types.

Consider this example:

- A crawler sets a static edge type: _Works At_.

- However, employment is temporal — it may not always be valid.

- A processor can check job start and end dates and dynamically update the edge type to _Worked At_ once the person leaves.

Up: [Relationships](https://documentation.cluedin.net/model/relationships.md)
