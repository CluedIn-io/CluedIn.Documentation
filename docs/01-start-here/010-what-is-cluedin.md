---
layout: cluedin
title: What is CluedIn?
parent: Get started
nav_order: 10
permalink: /get-started/what-is-cluedin
content_type: concept
---

CluedIn is a master data management platform. It ingests records from every system you connect to it, works out which of those records describe the same real-world thing, and produces one **golden record** per thing - with the full history of where each value came from.

## What the platform does

| Stage | What happens | Where it is documented |
|---|---|---|
| Ingest | Records arrive from files, databases, endpoints and connectors, and are mapped onto your model. | [Ingest](/ingest) |
| Model | Business domains, vocabularies and identifiers describe what the data means. | [Model](/model) |
| Master | Duplicates are found and merged into golden records. | [Master](/master) |
| Govern & improve | Clean projects, rules, enrichers and tags raise and hold data quality. | [Govern & improve](/govern) |
| Publish & consume | Streams, export targets, GraphQL and REST deliver the trusted data onward. | [Publish & consume](/publish) |

The two supporting areas are [Administer](/administer) - managing the product - and [Deploy & operate](/operate) - running the installation.

## What makes it different

CluedIn does not require you to agree on a schema before you load data. Records are ingested as they are, described with vocabularies, and connected through identifiers as evidence arrives. That property is called [eventual connectivity](/get-started/core-concepts/eventual-connectivity), and it is the idea most worth understanding before anything else.

## Next

- New to the product: [Quickstart](/get-started/quickstart)
- Want the vocabulary first: [Core concepts](/get-started/core-concepts) and [Terminology](/get-started/terminology)
- Learning for a specific role: [Learning paths](/learning-paths)
