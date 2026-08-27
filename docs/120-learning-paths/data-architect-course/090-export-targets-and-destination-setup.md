---
layout: cluedin
title: Configure Export Targets
parent: Data Architect course
grand_parent: Learning paths
nav_order: 90
permalink: /learning-paths/data-architect-course/export-targets-and-destination-setup
---

## Learning outcome

Configure and validate the destination connection that CluedIn will use to publish trusted data to a downstream system.

## Scenario

A downstream consumer is ready to receive data from CluedIn. Before building a stream, you need a working Export Target with a tested connection, understood capabilities, and an identified owner.

## Read

- [Export targets](/consume/export-targets)

## Exercise

1. Choose the downstream system for the training scenario.
2. Select the appropriate Export Target type and document the required connection information.
3. Configure the Export Target in a non-production environment.
4. Test the connection and verify that the target is healthy.
5. Record the streaming modes supported by the target and any connector-specific limitations that affect the downstream contract.
6. Define ownership, credential-management expectations, and what should happen if the destination becomes unhealthy.

## Deliverable

An Export Target configuration record containing destination purpose, connector type, connection validation, supported modes, ownership, and operational dependencies.

## Complete when

- The Export Target connection is healthy and testable.
- Connector capabilities and limitations are understood before stream design begins.
- Ownership and failure handling are explicit.

## Next

Continue to [Configure Streams and downstream contracts](/learning-paths/data-architect-course/streams-and-downstream-contracts).
