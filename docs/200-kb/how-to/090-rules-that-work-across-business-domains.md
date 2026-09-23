---
layout: cluedin
title: How to write rules that check conditions across different business domains
parent: Knowledge base
permalink: /kb/how-to-write-rules-cross-domain
nav_order: 2
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

CluedIn Rules don’t just operate within a single entity. In many use cases, you’ll need to **span across business domains** — for example, applying a Customer rule that depends on their Orders, or a Supplier rule that looks at related Products. This is similar to performing a **join** in a traditional database.

CluedIn provides functions and entity graph navigation features that allow rules to traverse relationships between entities and operate on connected data.

---

## Key Functions and Concepts

1. `LoadByEntityCode`
    - Loads another entity into context using its unique `EntityCode`.
    - Useful when you already have the identifier of a related entity and want to access its data directly.
    - Example:
        ```powerfx
        LoadByEntityCode("Customer", CustomerEntityCode)
        ```

2. `LoadIncomingRelationships`
    - Retrieves relationships that point to the entity currently being evaluated.
    - Useful when a rule needs to evaluate entities that have a relationship to the current entity.

    For example, suppose a rule is evaluated against a Student record and related Address records point to that Student. The following formula checks whether at least one related Address has a specific vocabulary value:

    ```powerfx
    Not(
        IsEmpty(
            Filter(
                ForAll(
                    LoadIncomingRelationships(Entity),
                    LoadEntityByEntityCode(EntityCode)
                ),
                GetVocabularyKeyValue(ThisRecord, "address.country") = "UK"
            )
        )
    )
    ```

    The formula works as follows:

    1. `LoadIncomingRelationships(Entity)` retrieves incoming relationships for the current entity.
    2. `ForAll(..., LoadEntityByEntityCode(EntityCode))` loads the entity associated with each relationship.
    3. `Filter(...)` evaluates the loaded entities and keeps those that satisfy the required condition.
    4. `Not(IsEmpty(...))` returns `true` when at least one related entity meets the condition.

    Replace `address.country` and `UK` with the vocabulary key and value required by your rule.

    You can also filter relationships by edge type when only a specific relationship should be evaluated:

    ```powerfx
    Filter(
        LoadIncomingRelationships(Entity),
        EdgeType = "/AddressOf"
    )
    ```

3. `LoadOutgoingRelationships`
    - Retrieves relationships going from the entity currently being evaluated to other entities.
    - Useful when the current entity owns the relationship to the related entity.

    For example:

    ```powerfx
    ForAll(
        LoadOutgoingRelationships(Entity),
        LoadEntityByEntityCode(EntityCode)
    )
    ```

    This retrieves the outgoing relationships and loads the entity associated with each relationship.

    When an entity has multiple relationship types, filter the relationships by `EdgeType` before applying further logic.

---

## Traversing multiple relationships

Relationship functions can be nested when a rule needs to evaluate entities more than one relationship away.

For example, a rule can:

1. Load incoming relationships for the current entity.
2. Load the related entity.
3. Load that entity's outgoing relationships.
4. Continue evaluating related entities as required.

Use the simplest traversal that satisfies the rule. Loading related entities and traversing multiple relationship levels increases the amount of work performed by the rule, particularly where entities have many relationships.
