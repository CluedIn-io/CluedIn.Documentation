---
layout: cluedin
title: Global Audit Log
parent: Administer
nav_order: 65
permalink: /administer/global-audit-log
content_type: how-to
tags: ["administration", "audit log", "revert", "governance"]
last_modified: 2026-10-24
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Global Audit Log** records administrative and user actions across CluedIn - who did what, to what, and when - and lets you **revert** a reversible action back to its prior state, either one entry at a time or everything since a chosen point in time.

## Prerequisites

Viewing and reverting entries requires the `admin.tenantmanagement` claim.

## Open the Global Audit Log

Go to **Administration > Global Audit Logs**.

Each entry shows:

- **Name/target** - the object the action was about (for example a glossary term, a custom job, or an entity), linking to it where applicable.
- **Action** - what kind of change was made (for example "Added user to owners" or "Revert action").
- **Changes** - the before/after values for each affected property.
- **Modified by** - the person who made the change, shown by display name only. The audit log never shows a raw login or email address here.
- **Modified at** - when the action happened.

Filter the list by date range or object type, and export the current filter to CSV.

![The Global Audit Log list, with the Modified by column showing a display name rather than an email address, and a bulk-select banner above it]({{ "/assets/images/administration/global-audit-log/global-audit-log-overview.png" | relative_url }})

## Retention: 2 days

Audit log entries, and the ability to revert them, are kept for **48 hours**. After that window, the entry stays visible in the log for reference, but its revert action is disabled. A background job permanently deletes audit log data older than the retention window on a recurring schedule, so entries past the window cannot be recovered.

## Revert a single entry

Entries that can be undone show an active **Revert** button in the Actions column; entries that can't - either because that kind of change doesn't support reverting, or because it's past the 48-hour window - show it disabled, with the reason on hover.

Select **Revert** to undo just that entry. This applies the inverse of the recorded change (for example, removing an owner that an "Add Owner" entry added) and records the outcome as a new "Revert action" entry of its own.

Reversible actions include, among others:

- Adding or removing an owner.
- Deleting an entity - restores the entity and its data as it was at delete time.
- Deduplication merges, clean project changes, custom job updates, and AI agent changes.

## Revert everything since a point in time

To undo every reversible change made since a specific moment - for example, after discovering a bad bulk operation - filter the log to a **From** date and select **Revert everything since this date**. Confirm by typing `REVERT`.

![The point-in-time revert confirmation dialog, asking to type REVERT to confirm reverting every change since a chosen date]({{ "/assets/images/administration/global-audit-log/point-in-time-revert-confirm.png" | relative_url }})

Only entries within the last 48 hours, and of the object types you can edit, are checked - up to the newest 200 matching entries per request. If more entries matched than were checked, narrow the date or object type filter and repeat.

## Verify the result

A point-in-time revert reverts matching entries newest first and reports the outcome of each one individually as a toast notification: a success count, and a specific message for every entry that could not be reverted. The list refreshes once the revert finishes, so you can confirm the reverted entries' "Revert action" entries and check that the affected records are back to their earlier state.

![Toast notifications after a point-in-time revert, showing a success count and individual reasons for entries that could not be reverted]({{ "/assets/images/administration/global-audit-log/point-in-time-revert-results.png" | relative_url }})

A single-entry revert reports success or failure the same way, and either outcome is also visible as a new entry at the top of the log.

## What this changes

Reverting an entry changes live data immediately - it is not a preview or a simulation. It restores the recorded property values; it does not replay any downstream processing (such as rules or enrichment) that ran as a result of the original action, so you may need to re-run that processing separately if it depended on the reverted change.

## If something goes wrong

If an entry's **Revert** button is disabled, hover over it for the reason - typically that the entry is past the 48-hour retention window, that the underlying object no longer exists, or that this kind of change doesn't support reverting.

Nothing is skipped silently: if a point-in-time revert can't undo a specific entry, its toast names the entry and the reason. Narrow your filters and retry for entries that were outside the newest 200 checked.
