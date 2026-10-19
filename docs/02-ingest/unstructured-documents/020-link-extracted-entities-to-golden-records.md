---
layout: cluedin
title: Link extracted entities to golden records
parent: Unstructured documents
grand_parent: Ingest
nav_order: 20
permalink: /ingest/unstructured-documents/link-extracted-entities-to-golden-records
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how CluedIn identifies people, organizations and other named entities mentioned in an unstructured document, proposes them as candidate links to existing golden records, and how to review those proposals.

## Prerequisites

- The document must have reached the **Processed** status. For more information, see [Upload and extract unstructured documents](/ingest/unstructured-documents/upload-and-extract-unstructured-documents).
- Your organization needs an AI Chat endpoint configured; entity detection is skipped for documents processed without one.

## Review proposed entity links

While a document is processed, CluedIn asks AI to identify the named entities explicitly mentioned in its text, then searches your existing golden records for the best match for each one.

**To review proposed entity links**

1. Open a processed document and go to the **Entity Links** tab.

1. For each entity, review:

   - **Entity** and **Type** - the name and kind of entity (such as Person, Organization or Product) found in the document.
   - **Matching Golden Record** and **Confidence** - the closest existing golden record CluedIn found for that entity, if any, and how confident the match is. Select the golden record's name to open it in a new context and inspect its current properties before deciding. An entity with no match shown has no suggested golden record to link to.

1. Select **Accept** to create a link between the document and the matched golden record, or **Reject** to dismiss the proposal. Only entities with a matching golden record can be accepted.

## Verify the result

An accepted link changes the entity's status to **Accepted** and creates an edge in the graph from the document to the matched golden record, so the relationship is visible from the golden record's own edges. A rejected link changes status to **Rejected** and is not applied.

## What this changes

Accepting a link only adds an edge between the document and the matched golden record - it does not change any properties on the golden record. To update a golden record's properties from a document instead, see [Create or enrich records from a document](/ingest/unstructured-documents/create-or-enrich-records-from-a-document).
