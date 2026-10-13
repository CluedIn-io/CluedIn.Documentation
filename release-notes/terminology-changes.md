---
title: Terminology changes
url: https://documentation.cluedin.net/release-notes/terminology-changes
content_type: reference
section: Release notes
---

# Terminology changes

> reference: Facts, options, APIs.

In the [2025.05 release](https://documentation.cluedin.net/release-notes/2025-05.md) of CluedIn, we have updated some of the terminology used in the platform. The terminology changes simplify CluedIn interface, making it more intuitive and better aligned with common industry concepts.

The terminology changes only affect the terms, the functionality behind the terms remains the same. The following table provides a summary of terminology changes in CluedIn.

| Old term | New term | Definition |
|--|--|--|
| Entity type | Business domain | A well-known business object that provides context for golden records. In CluedIn, all golden records must have a business domain to ensure systematic organization of data management processes. Learn more in [Business domain](https://documentation.cluedin.net/model/business-domains/business-domains-explained.md). |
| Entity origin code | Primary identifier | A mechanism used in CluedIn to define the uniqueness of a golden record. It is configured during the mapping process. The primary identifier consists of a business domain, an origin, and a key that uniquely identifies the record. This combination allows you to achieve absolute uniqueness across all the data sources you interact with. Learn more in [Identifiers](https://documentation.cluedin.net/model/identifiers.md). |
| Entity codes | Identifiers | Additional mechanism to define the uniqueness of a golden record. If a data set contains additional columns that can uniquely represent a record, these columns can also be used to generate identifiers. Learn more in [Identifiers](https://documentation.cluedin.net/model/identifiers.md). |

Up: [Release notes](https://documentation.cluedin.net/release-notes.md)
