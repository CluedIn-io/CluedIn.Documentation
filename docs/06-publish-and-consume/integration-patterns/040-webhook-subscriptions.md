---
layout: cluedin
title: Send events to your systems with webhook subscriptions
parent: Integration patterns
grand_parent: Publish & consume
nav_order: 40
permalink: /publish/integration-patterns/webhook-subscriptions
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

A webhook subscription registers a URL in your own system to receive a signed HTTP POST whenever a
CluedIn event you choose fires - a data source being added, a stream finishing, a user being added,
and more. Use it to notify your other systems the moment something happens in CluedIn, instead of
polling the API.

## Prerequisites

- Tenant management access (`Informed` to view subscriptions, `Consultant` to create, delete, or
  send a test event) under **Developer features**.
- An HTTPS endpoint in your own system that can receive a POST request and respond quickly - CluedIn
  does not wait for your endpoint to finish processing.

## Inputs

| Field | Required | Accepts | Example |
|---|---|---|---|
| Event | Yes | One event type per webhook. CluedIn sends a message every time that event happens; to listen to more events, add another webhook. | `Data source added` |
| Endpoint URL | Yes | A `https://` address that does not resolve to a loopback, private-network, or link-local address. | `https://hooks.example.com/cluedin/sources` |

## Create a webhook subscription

1. Go to **Developer features > Webhooks**.
2. Select **+ Add webhook**.
3. Choose the event to listen for, and enter the HTTPS endpoint that should receive it.
4. Select **Create webhook**.
5. Copy the signing secret shown and store it with the team that owns the receiving endpoint -
   CluedIn shows it only this once. If it is lost, delete the webhook and create a new one.

## Verify the result

The new webhook appears in the **Webhooks** list with a status of **Active**. Delete it, or wait
for the next matching event, to confirm delivery - the list's **Last delivery** column shows the
outcome and time of the most recent attempt once one has happened.

## Verifying a delivery

Every delivery includes an `X-CluedIn-Signature` header in the form `sha256=<hex>` - an
HMAC-SHA256 of the raw request body, keyed with your webhook's signing secret. Recompute it on
your side and compare before trusting the payload:

```text
signature = hex(HMAC_SHA256(secret, raw_request_body))
expected_header = "sha256=" + signature
```

The payload itself is JSON with this shape:

```json
{
  "eventType": "AddDatasource",
  "eventDate": "2026-10-28T07:51:00Z",
  "sequenceNumber": 12345,
  "data": { }
}
```

Delivery is at-least-once - the same event can arrive more than once. `sequenceNumber` stays the
same across repeats of the same event, so use it to deduplicate on your side.

## What this changes

Creating, deleting, or sending a test event for a webhook only changes the webhook subscription
itself - it does not change any CluedIn data. Deleting a webhook stops deliveries for that event
immediately and removes its delivery history.

## Current limitations

- A webhook cannot be edited after it is created, and its event cannot be changed - delete it and
  create a new one instead.
- A subscription cannot be paused and resumed, and its signing secret cannot be regenerated - both
  need a new webhook.
- A failed delivery is not retried automatically, and only the most recent delivery's result is
  kept - there is no delivery history beyond it.

## If something goes wrong

| Symptom | Cause | Fix |
|---|---|---|
| **Endpoint URL** shows "Use a secure address that starts with https://" | The URL is not `https://`, or it resolves to a private/loopback address | Use a public `https://` endpoint |
| **Last delivery** shows **Failed** | Your endpoint returned a non-2xx status, or could not be reached | Check your endpoint's logs for the matching `sequenceNumber`; CluedIn does not retry a failed delivery |
