---
layout: cluedin
title: Concept of writeback
parent: Writeback
grand_parent: Publish & consume
nav_order: 10
permalink: /publish/writeback/concept-of-writeback
content_type: concept
tags: ["consume", "data export", "writeback"]
last_modified: 2026-10-24
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Writeback pushes curated golden records from CluedIn to an operational system—HubSpot, Salesforce, or any REST API you connect generically—so the teams working in that system see the cleaned-up data without needing to go through CluedIn themselves.

## How a writeback job is put together

A writeback job has three parts, configured together when you [create the job](/publish/writeback/create-a-writeback-job):

- **A connection** to the target system: which system (HubSpot, Salesforce, or Generic REST), and the credentials used to authenticate to it. Credentials are stored encrypted and are never shown again after you save them. A connection can be reused by more than one writeback job.
- **A source selection**: the CluedIn entity type to push (for example `/Person`), and an optional selection criteria—a CluedIn search query—that narrows it further. Without a selection criteria, every golden record of that entity type is a candidate.
- **A field mapping**: which CluedIn vocabulary key fills which field on the target object (for example, `person.email` to HubSpot's `email` contact property).

## How a run works

A writeback job does not run on its own. You [trigger a run manually](/publish/writeback/run-a-writeback-job), and that run:

1. Finds every golden record that matches the job's entity type and selection criteria, at the moment the run starts.
1. Pushes each one to the target system, using the job's field mapping.
1. Records the outcome once it finishes: how many records were attempted, how many succeeded, and—for each one that failed—what the target system returned.

Each run is kept in the job's run history, so you can see what happened on a previous run even after a later one completes.

## How writeback differs from a stream

[Streams](/publish/streams) and writeback both send CluedIn data to an external system, but they solve different problems:

| | Streams | Writeback |
|--|--|--|
| When it sends data | Continuously, as golden records change | On demand, when you trigger a run |
| What it sends | Any export target your organization has connected | HubSpot, Salesforce, or any REST API you connect generically |
| What selects the records | Filter rules and actions | An entity type and a search query |
| Where the result appears | The stream's log, as records are sent | The run's record counts, once the run finishes |

If you need an operational system to stay continuously in sync with CluedIn, use a stream. If you need to push a specific, curated set of records on demand—for example, after a clean project finishes—use writeback.
