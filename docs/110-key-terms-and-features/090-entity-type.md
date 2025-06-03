---
layout: cluedin
title: Business domain
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

A business domain represents a specific business object that describes the semantic meaning of golden records. It can signify physical objects, individuals, locations, and more. Business domains should be **global**, **timeless**, and **independent of specific data sources** (e.g., Contact, Organization, Car).

Each golden record is associated with exactly one business domain. You can leverage built-in business domains or define your own custom business domains.

A business domain is assigned to a clue during the mapping process, and it plays a critical role in various [identifiers](/key-terms-and-features/entity-codes), including primary identifiers and additional identifiers.

## Business domain usage

### Adding semantic context to golden records

The business domain provides **metadata**, such as a display name, icon, and description, adding a semantic layer to golden records. Golden records sharing the same business domain inherently share the same semantic meaning.

When defining business domains, it’s essential to balance specificity and genericness. Use terminology familiar to your line of business (LOB) to help identify records intuitively.

{:.important}
CluedIn is flexible—if you choose an initial business domain that needs adjustment, you can change it. However, changing business domains mid-project can be cumbersome, especially if deduplication projects, rules, or streaming configurations have already been applied.

### Filtering golden records

Business domain acts as the default filter for many operations in CluedIn. Selecting the right business domain allows you to target groups of golden records that logically belong together.

### Producing primary identifier

Business domain forms part of the primary identifier value. This structure enforces that records can only merge if they share the same business domain.

## Business domain properties and characteristics

### Business domain code

Business domains have a unique code, represented as a simple string prefixed by a slash (/). The code uniquely identifies the business domain. That is why you see a slash (/) in front of a business domain.

To create a business domain code, use concise, meaningful names and avoid non-alphanumeric characters where possible.

### Nested business domains

CluedIn supports nested business domains, allowing hierarchical organization of business domains. While not mandatory, this feature can help group business domains of the same nature.

**Example of nested business domains**

In the following hierarchy, Video is a child of Document.

```
/Document
/Document/XLS
/Document/Video
/Document/Audio
```

**Benefits of nested business domains**

- **Filter grouped entities** – nested business domains allow you to filter or stream entities collectively. For example, using a filter that starts with /Document would include all documents, regardless of their specific sub-business domain.

- **Streamline reporting** – nested business domains simplify reporting and analysis across related business domains.

## Useful resources

- [Add or modify a business domain](/management/entity-type)