---
layout: cluedin
title: Writeback
parent: Publish & consume
nav_order: 25
has_children: true
permalink: /publish/writeback
content_type: landing
summary: "A writeback job pushes a selection of curated golden records from CluedIn to an operational system such as HubSpot or Salesforce, on demand."
list_children: false
tags: ["consume", "data export", "writeback"]
last_modified: 2026-10-24
---

Once data has been cleaned and merged into golden records in CluedIn, you often need to put it back to work in the operational system your teams use day to day—for example, pushing a verified email address back to the matching contact in HubSpot or Salesforce. Writeback does this directly, without routing the data through an Event Hub or a Power Automate flow.

A writeback job has three parts: a connection to the target system (its credentials, stored securely), the CluedIn entities to send (an entity type and an optional selection criteria), and a field mapping from CluedIn vocabulary keys to fields on the target object. Running the job pushes the matching records and records the outcome—how many records were attempted, how many succeeded, and the error for each one that failed.

Unlike a [stream](/publish/streams), a writeback job does not run continuously. You trigger a run manually, and it pushes whatever matches the job's selection criteria at that moment.

This section covers the following areas:

- [Concept of writeback](/publish/writeback/concept-of-writeback) – learn how a writeback job is put together and how a run works.

- [Create a writeback job](/publish/writeback/create-a-writeback-job) – learn how to connect a target system and configure a writeback job.

- [Run a writeback job](/publish/writeback/run-a-writeback-job) – learn how to trigger a run and read its results.
