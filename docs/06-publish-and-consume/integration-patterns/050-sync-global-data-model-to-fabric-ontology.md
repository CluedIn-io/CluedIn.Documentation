---
layout: cluedin
title: Sync the Global Data Model to a Microsoft Fabric Ontology
parent: Integration patterns
grand_parent: Publish & consume
nav_order: 50
permalink: /publish/integration-patterns/sync-global-data-model-to-fabric-ontology
content_type: how-to
tags: ["fabric", "ontology", "global data model", "governance"]
last_modified: 2026-11-17
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Sync your [Global Data Model](/model/global-data-model) to Microsoft Fabric as an **Ontology** item, so the business domains, fields and relationships CluedIn has mastered are available to the rest of your Fabric estate. Once set up, the Ontology keeps itself up to date automatically every 15 minutes.

## Prerequisites

- A Microsoft Fabric connection, with permission to create items in at least one workspace. Create one from **Data Sources** > **Connections** > **Microsoft Fabric** if you don't already have one.
- The **Governance > Global Data Model** claim (Consultant level or above), to use the button described below.

## Sync the Global Data Model

1. Go to **Governance** > **Global Data Model**.
2. Select **Sync with Microsoft Fabric Ontology**.
3. Choose the Microsoft Fabric connection and workspace to sync to, then select **Sync now**.

CluedIn creates an Ontology named **CluedIn Global Data Model Ontology** in the selected workspace the first time you do this. Each business domain becomes an Ontology entity type, each of its visible vocabulary keys becomes one of that entity type's properties, and each relationship between two modelled business domains becomes an Ontology relationship type.

Selecting **Sync now** again - whether for the same workspace or a different one - never creates a second Ontology or a second schedule: CluedIn looks for an existing Ontology with that name first, and updating the recurring schedule reuses the same job rather than adding another one.

## Verify the result

The status shown under the button reflects the most recent sync attempt:

- A success state shows when the Global Data Model was last synced, and confirms the sync re-runs automatically every 15 minutes.
- A failure state shows the error from the most recent attempt - for example, an authentication problem with the Microsoft Fabric connection, or a workspace that no longer exists.

Open the Ontology item in the Fabric portal to confirm its entity types, properties and relationships match what you expect from your Global Data Model.

## What this changes

- Syncing does not change anything in CluedIn - it only reads the current Global Data Model.
- A 15-minute recurring job is created the first time you sync, which keeps the Fabric Ontology in sync with the Global Data Model automatically from then on, with no further action needed.
- Each automatic re-sync replaces the Ontology's definition with the Global Data Model's current state, so changes you make in CluedIn (a renamed business domain, a new relationship, and so on) are reflected in Fabric within 15 minutes of the next scheduled run.

## If something goes wrong

If the status shows a failure, check the error message shown with it first:

- An authentication error usually means the Microsoft Fabric connection's credentials are no longer valid - update the connection and sync again.
- A workspace-not-found error means the selected workspace was deleted or the connection no longer has access to it - choose a different workspace and sync again.

For connection-level problems, see [Connect CluedIn to Microsoft Fabric](/solutions/fabric/connect-cluedin-to-fabric).
