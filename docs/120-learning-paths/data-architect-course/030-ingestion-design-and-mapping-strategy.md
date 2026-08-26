---
layout: cluedin
title: Build ingestion pipelines and support incremental or CDC ingestion
parent: Data Architect course
grand_parent: Learning paths
nav_order: 30
permalink: /learning-paths/data-architect-course/ingestion-design-and-mapping-strategy
---

## Learning outcome

Design and validate an ingestion pipeline that brings source data into CluedIn reliably for both initial loads and ongoing incremental or CDC-style updates.

## Scenario

A source system must feed CluedIn continuously. A one-time import is not enough: the architecture needs a repeatable ingestion path, a clear update strategy, and evidence that changed source records are reflected correctly in CluedIn.

## Read

- [Ingest data](/getting-started/data-ingestion)
- [Delta crawls](/integration/delts-crawls)

## Exercise

1. Identify the source system, connection method, expected volume, and update frequency.
2. Define the initial-load strategy and the ongoing incremental or CDC strategy.
3. Identify the source field or mechanism used to detect inserts and updates.
4. Configure or document the integration and data source group that will feed the training domain.
5. Ingest a representative initial sample and verify that the expected data sets arrive.
6. Change a source record or use a representative incremental batch, run the incremental path, and verify that CluedIn receives the change without requiring a full reload.
7. Record failure handling, retry expectations, logging, and the evidence used to prove that ingestion is healthy.

## Deliverable

An ingestion design containing source, connection method, initial-load strategy, incremental or CDC strategy, operating frequency, failure handling, and validation evidence.

## Complete when

- The pipeline supports repeatable ingestion rather than a one-off import.
- Initial and incremental behavior are both defined and tested.
- A failed or delayed ingestion can be detected and diagnosed.

## Next

Map the incoming data into the semantic model and establish identity and relationships.
