---
layout: cluedin
title: Run a writeback job
parent: Writeback
grand_parent: Publish & consume
nav_order: 30
permalink: /publish/writeback/run-a-writeback-job
content_type: how-to
tags: ["consume", "data export", "writeback"]
last_modified: 2026-10-24
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Run a writeback job when you want to push the golden records matching its entity type and selection criteria to the target system right now. Each run is recorded in the job's run history, so you can check back on the outcome—and on any errors—after it finishes.

## Prerequisites

- The **Writeback** claim. See [Claims](/administer/users-and-roles/claims#consume).
- A writeback job already [created](/publish/writeback/create-a-writeback-job), with a verified connection and at least one field mapping.

## Run a writeback job

**To run a writeback job:**

1. On the navigation pane, go to **Consume** > **Writeback**.

1. Select the writeback job you want to run.

1. In the upper-right corner, select **Run now**.

    The run is queued, and a new row appears at the top of the **Run history** table.

## Verify the result

The **Run history** table on the job's details page lists every run, newest first, with its status, when it was queued, how many records were **Attempted**, **Succeeded**, and **Failed**, and who triggered it.

A run moves through the following statuses:

- **Queued** – the run is waiting to start.
- **Running** – the run is pushing records.
- **Succeeded** – every attempted record was pushed successfully.
- **Partially succeeded** – some records were pushed successfully and some failed.
- **Failed** – no records were pushed successfully.

![The run history table for a writeback job, showing a completed run with a Succeeded status]({{ "/assets/images/consume/writeback/writeback-run-history.png" | relative_url }})

If a run has any failed records, its **Failed** count is a link. Select it to open a panel listing each failed record—which entity it was, and the error message the target system returned.

## What this changes

- **Running a job** pushes the records matching the job's entity type and selection criteria at the moment the run starts. Records added or changed after the run starts are not included in that run.
- **Writeback does not delete records.** A failed push does not remove anything from CluedIn or from the target system.
- **A run does not retry failed records automatically.** To retry, run the job again; it re-evaluates the selection criteria and pushes every matching record again.

## If something goes wrong

- **A run stays Queued.** The run has not been picked up yet. Give it a moment and check again; if it stays Queued for longer than other runs normally take, contact your administrator.
- **A run shows Failed or Partially succeeded.** Select the **Failed** count to see the error for each record. A common cause is a field mapping pointing at a target field the target system does not have, or a value the target system rejects (for example, an invalid email format).
- **Attempted is 0.** No golden records matched the job's entity type and selection criteria at the time of the run. Check the job's **CluedIn entity type** and **Selection criteria** on its configuration.
