---
layout: cluedin
title: Fuzzy-match a record before creating it
parent: Develop & APIs
nav_order: 50
permalink: /develop/fuzzy-matching
content_type: how-to
tags: ["api", "rest api", "search"]
---

If your application lets a user create a record that should map to a CluedIn golden record — for example, a CRM form that creates a contact or account — call the Search API first to check whether a matching golden record already exists. The v1 search endpoint matches on name, display name, and description with a one-character fuzzy tolerance, so a near-miss spelling ("Acme Corp" vs. "Acme Corportion") still finds the existing record instead of creating a duplicate.

Use this for a quick, real-time check against a single typed value as the user types or submits a form. It is not a substitute for [deduplication](/master/deduplication), which resolves duplicates across your whole data set on an ongoing basis and merges them into a single golden record — use that when you need an ongoing solution rather than a one-off check at the point of entry.

## Prerequisites

- An API token with access to Search. See [Get started with the REST API](/api/get-started) for how to authenticate and the base URL to use.

## Inputs

| Field | Required | Accepts | Example |
|---|---|---|---|
| `q` | Yes | The text to match — typically the name the user just typed. | `Acme Corportion` |
| `page` | Yes | The page number to return, starting at `1`. | `1` |
| `take` | Yes | The maximum number of results to return. | `5` |

## Check whether a similar record already exists

1. Call the v1 search endpoint with the value from your form:

   ```
   GET /api/v1/search?q={value}&page=1&take=5
   ```

   For example, searching for a misspelled company name:

   ```
   GET /api/v1/search?q=Acme%20Corportion&page=1&take=5
   ```

1. Read the `Total` field in the response.

   - `Total` is `0` — no similar record was found. It is safe to let the user create a new record.
   - `Total` is `1` or more — a similar record already exists. `Hits` contains the matching entities; show them to the user so they can confirm one is a match instead of creating a duplicate.

## Verify the result

A response with `Total` greater than `0` and at least one entry in `Hits` confirms the fuzzy match worked. The request only reads data — nothing in CluedIn changes, so you can call it as often as you need, on every keystroke or only on submit.

## What this changes

Nothing. This is a read-only search — it does not create, update, or merge any record. Creating the new record afterwards (if the user confirms there is no match) is a separate call, such as the [Entities](/api/entities) API.

## If something goes wrong

- **The request returns a 500 with an empty query** — `q` is required and cannot be empty; validate it client-side before calling the endpoint.
- **You get matches you did not expect** — the one-character fuzzy tolerance also matches unrelated short words that happen to be one character apart. Prefer longer, more specific values (a full company name rather than a single word) to keep matches relevant.
- **You need to match on a field other than name, display name, or description** — the v1 endpoint's fuzzy tolerance only applies to those three fields. For matching on other properties, use the general [Search](/api/search) endpoint's filters, which match exactly rather than fuzzily.
