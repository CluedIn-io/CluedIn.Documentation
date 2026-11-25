---
layout: cluedin
title: Manage the processing pipeline
parent: Monitoring
grand_parent: Deploy & operate
nav_order: 25
permalink: /operate/monitoring/manage-processing-pipeline
content_type: how-to
tags: ["monitoring", "engine-room", "queues", "operations"]
last_modified: 2026-11-25
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Processing pipeline** page in **Engine room** shows every queue that data passes through, from ingestion to the outgoing streams, with numbers that update every 2 seconds. Use it to find items that are failing or backlogged, retry failed messages, purge queues, export what you see, and review who did what in the audit log. For how the pipeline works and what affects its speed, see [Processing pipeline]({{ "/operate/monitoring/processing-pipeline" | relative_url }}).

## Prerequisites

- To open the page and export from it, you need at least the **Informed** level of the `engine.processing` claim.
- To retry, purge, or look at the messages waiting on a queue, you need the **Admin** or **Organization Admin** role. Without it, those actions are shown but disabled, and their tooltip says which role is needed.
- Streams are listed only for users who can view streams.

## Read the page

Go to **Engine room** > **Processing pipeline**. The page has two tabs, **Pipeline** and **Audit log**, and fills the whole window.

![The Processing pipeline page in the Grid view: the Live indicator, "Updated N s ago" and Pause at the top right, six KPI cards, a red banner listing one failing and one backlogged item, the toolbar, and the stages stacked with their cards]({{ "/assets/images/operate/processing-pipeline/grid.png" | relative_url }})

- **Live**, **Updated N s ago** and **Pause** (top right, Pipeline tab only). The numbers refresh every 2 seconds. Select **Pause** to stop refreshing while you read; select **Resume** to start again. Refreshing never closes an open menu, dialog or side panel, and never moves your scroll position.
- **KPI cards**: messages in the pipeline, combined incoming and outgoing rates, estimated time remaining, the number of items that need attention, and the number of failed messages.
- **Banner**: lists the items that are failing or backlogged. Select **Show only these** to apply the **Needs attention** filter.

Each card is one queue (or stream) and shows its status as a coloured dot and text, with a matching coloured stroke on its left edge:

| Status | Meaning |
|---|---|
| **Failed** | A dead letter queue holding failed messages, or a queue whose numbers could not be read. |
| **Backlogged** | Messages are waiting, but none are being processed right now. |
| **Running** | Messages are coming in or going out. |
| **Idle** | Nothing is waiting. |

Failed and backlogged items **need attention**; running items are **active**. The steps in **Processing Sub-steps** have no queue of their own and show the numbers of the **Processing** stage, so they are left out of both filters and of the KPI totals.

## Find items

Use the toolbar above the stages:

- **Search** filters the cards by name.
- The dropdown on the right shows **All**, **Active** or **Needs attention**, each with the number of items it would show.
- **Grid**, **Flow** and **Classic** switch the layout. The page remembers the last layout you chose, per user.

**Grid** (the default) stacks the stages from top to bottom. Each stage header shows a select-all checkbox, the stage name, the number of items, the stage's totals and a button to collapse it, and stays pinned to the top while you scroll through its cards. Problem items come first. A stage shows two rows of cards; select **Show all** to see the rest.

**Flow** shows the stages as columns from left to right, joined by arrows. Each column fills the height of the page and scrolls on its own. Drag the background to pan, use the zoom control at the top left to zoom in or out or type a percentage, and select **Fit to screen** at the top right to fit every column. Flow always opens at 100%.

![The Flow view: stages as columns joined by arrows, the zoom control at the top left showing 100%, and Fit to screen at the top right]({{ "/assets/images/operate/processing-pipeline/flow.png" | relative_url }})

**Classic** is the original diagram, stretched to the full width of the page, with all text wrapped inside its boxes.

![The Classic view: data sets on the left, the CluedIn box with clue, edge, parent and metrics processing in the middle, commands and enrichers underneath, and outgoing streams on the right]({{ "/assets/images/operate/processing-pipeline/classic.png" | relative_url }})

Select a card to open its side panel. It shows the item's status, stage and live numbers, the actions you can take on it, and, if you have the Admin role, the first messages waiting on its queue.

![The side panel of the Dead Letter (Recoverable) queue: status Failed, its message counts and rates, the Retry failed messages and Purge buttons, and three waiting messages]({{ "/assets/images/operate/processing-pipeline/panel.png" | relative_url }})

## Retry failed messages

**Retry failed messages** sends the messages waiting on a dead letter queue back to the queues they originally failed on, so they are processed again. It is only offered on a dead letter queue that holds failed messages (**Dead Letter (Recoverable)** or **Dead Letter (Non-Recoverable)**).

1. Open the action in one of three ways:
    - On the card, select the three-dot menu, then **Retry failed messages**.
    - In the card's side panel, select **Retry failed messages**.
    - Select the cards' checkboxes, then select **Retry failed messages** in the bulk actions next to **Export**.
2. In the confirmation dialog, check how many failed messages will be retried, then select **Retry failed messages**.

![A dead letter queue's three-dot menu open on its card, offering View details, Retry failed messages and Purge]({{ "/assets/images/operate/processing-pipeline/attention-menu.png" | relative_url }})

## Purge queues

**Purge** removes every message waiting on a queue. Purged messages can't be recovered; messages already being processed are not affected.

1. Select **Purge** from the card's three-dot menu, from its side panel, or from the bulk actions with several cards selected.
2. In the confirmation dialog, select **Purge**.

## Work with several items at once

Select the checkbox on each card, or the checkbox in a stage header to select the whole stage. While anything is selected, the toolbar shows the number selected and **Retry failed messages**, **Purge**, **Export** and **Clear selection**. Your selection stays when you change the layout, the filter or the search.

## Export the pipeline

1. Select **Export** in the toolbar, or **Export** in the bulk actions to start with your selection.
2. Choose the **Scope**: **All** items, the **Current view** (what the filter and search show now), or the **Selected** items.
3. Choose the **Format**: **CSV** or **Excel**.
4. Select **Export**. The file downloads straight away.

![The Export pipeline dialog with the scope options All, Current view and Selected, and the format options CSV and Excel]({{ "/assets/images/operate/processing-pipeline/export.png" | relative_url }})

The file has one row per item, with its stage, name, status, message counts, rates, failed messages and queue name.

## Review the audit log

The **Audit log** tab lists every retry, purge and export made from the Processing pipeline page, newest first, with **Changed by**, **Changed at**, **Action**, **Item** and **Details**.

- Use **Search** and **Export** on the left to find entries and download them as CSV.
- Use the filters on the right to narrow the list by action, by user and by time.

![The Audit log tab listing purges, exports and a retry, with the action, user and date filters on the right]({{ "/assets/images/operate/processing-pipeline/audit.png" | relative_url }})

## Verify the result

- After a retry, a message tells you how many failed messages were sent back and how many could not be retried. The dead letter queue's count drops as its messages move back to their original queues, which then process them in the background.
- After a purge, a message confirms how many queues were purged, and their counts drop to zero on the next refresh.
- Every retry, purge and export appears on the **Audit log** tab straight away.

## What this changes

- **Retry** puts messages back on the queues they failed on, so the data in them is processed again and can change golden records like any other processed data. A message that fails again goes back to a dead letter queue.
- **Purge** permanently deletes the waiting messages. It can't be undone.
- **Export** only downloads a file; it doesn't change anything.

## If something goes wrong

- **The retry, purge or message preview is disabled.** You need the Admin or Organization Admin role.
- **"Could not retry the failed messages" or "Could not purge the queue".** The message bus could not complete the operation. Try again; if it keeps failing, check the server logs.
- **A retry reports messages that could not be retried.** Those messages could not be sent back to their original queue (for example, because it no longer exists) and stay failed.
