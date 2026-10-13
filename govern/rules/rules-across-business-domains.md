---
title: Write rules across business domains
url: https://documentation.cluedin.net/govern/rules/rules-across-business-domains
content_type: how-to
section: Govern & improve > Rules
---

# Write rules across business domains

> how-to: Steps to accomplish one task.

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

Up: [Rules](https://documentation.cluedin.net/govern/rules.md)
