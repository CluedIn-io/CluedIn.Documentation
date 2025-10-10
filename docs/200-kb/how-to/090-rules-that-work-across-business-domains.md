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
