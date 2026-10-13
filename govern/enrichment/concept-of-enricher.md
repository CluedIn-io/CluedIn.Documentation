---
title: Concept of enricher
url: https://documentation.cluedin.net/govern/enrichment/concept-of-enricher
content_type: concept
section: Govern & improve > Enrichment
---

# Concept of enricher

> concept: Explains how something works.

In this article, you will explore the concept of an enricher through an example and understand its place in the data life cycle in CluedIn.

## Enricher example

Imagine you have a golden record—_CluedIn_—that contains several properties. How can you enrich this golden record with additional information available on the internet?

To begin with, you need to add the web enricher and specify the vocabulary key. The value of this vocabulary key will be used to retrieve information from external services. In this case, the vocabulary key is _organization.website_. The enricher then retrieves all available information it can find based on the specified website address. Finally, this new information is added to the initial golden record.

![Animation: the Web enricher reads organization.website from the CluedIn golden record and adds a Web source with website title and description properties](https://documentation.cluedin.net/assets/images/preparation/enricher/enricher-example.gif)

In the next section, you'll find out how the data from the enricher is incorporated into the corresponding golden record.

## Enricher in data life cycle

The following diagram illustrates the place of enricher within the data life cycle in CluedIn.

![Diagram: a golden record passes the vocabulary key organization.website to the Web enricher, which queries external services and produces a clue; processing the clue updates the golden record](https://documentation.cluedin.net/assets/images/preparation/enricher/enricher-life-cycle.gif)

**From golden record to enricher**

To begin the process of enriching a golden record with additional information, you need to designate a vocabulary key. This vocabulary key serves as the basis for retrieving additional information about that particular golden record from the internet. If you don't provide a vocabulary key, the enricher won't be able to look for additional information. For more details about prerequisites for an enricher, see [Connectors](https://documentation.cluedin.net/get-started/core-concepts/connectors.md).

**From enricher to clue**

When the enricher receives the vocabulary key value, it calls an external internet service, typically an API, to retrieve additional information associated with the specified vocabulary key. Then, the information obtained from the external service appears in CluedIn as a clue. For more information about the clue structure, see [Clue reference](https://documentation.cluedin.net/get-started/core-concepts/clue-reference.md). Now, how do we link a new clue to the golden record?

**From clue to golden record**

When a new clue appears in CluedIn from the enricher, it goes into the processing pipeline. It is important to note that such clue has the same primary identifier as the golden record. During processing, CluedIn transforms the clue into a data part and executes merging by identifiers to ensure that the new information seamlessly integrates with the existing golden record. To learn more about what happens to the clue during processing, see [Data life cycle](https://documentation.cluedin.net/get-started/core-concepts/data-life-cycle.md).

> **Important:** The processing of a clue from an enricher follows the same steps as any other clue within the system.

Up: [Enrichment](https://documentation.cluedin.net/govern/enrichment.md)
