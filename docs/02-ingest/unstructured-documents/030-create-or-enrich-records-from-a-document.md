---
layout: cluedin
title: Create or enrich records from a document
parent: Unstructured documents
grand_parent: Ingest
nav_order: 30
permalink: /ingest/unstructured-documents/create-or-enrich-records-from-a-document
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to turn an unstructured document into a new record, and how to use a document to propose updates to an existing golden record.

## Prerequisites

- The document must have reached the **Processed** status. For more information, see [Upload and extract unstructured documents](/ingest/unstructured-documents/upload-and-extract-unstructured-documents).
- Your organization needs an AI Chat endpoint configured.
- A vocabulary must exist for the entity type you want to create or enrich a record for. For more information, see [Vocabularies](/model/vocabularies).

## Create a record from a document

**To create a record from a document**

1. Open a processed document and go to the **Create Record** tab.

1. Enter the **Entity type** to create a record for, for example `/Organization/Product`.

1. Select **Preview** to see which properties CluedIn would map from the document, and their values, before creating anything.

    CluedIn maps the document's extracted text onto the vocabulary keys of that entity type, using only the fields the document clearly states a value for.

1. Review the previewed properties, then select **Create Record** to submit the record as previewed, or **Back** to change the entity type and preview again.

## Verify the result

Record creation, like all record changes in CluedIn, is processed asynchronously. The new record appears in search and on the golden record pages once processing finishes.

In addition to the mapped properties, the new record is stamped with metadata about its source document - the file name, file type, upload date, classification (if any), and the document's own id - so you can trace the record back to the document it came from even if the entity link between them is later rejected or never reviewed.

## Enrich an existing golden record from a document

**To enrich an existing golden record from a document**

1. Open a processed document and go to the **Enrich Golden Record** tab.

1. Enter the **Golden Record id** of the record you want to enrich, and select **Analyze**.

    CluedIn compares the document's content against that record's current property values and proposes a value for each vocabulary key the document clearly states a value for and that differs from the record's current value.

1. Review the proposed changes, then either:

   - Select **Apply** or **Reject** next to a single property to decide it individually.
   - Select **Apply All** or **Reject All** to decide every pending proposal from this analysis at once.

## Verify the result

An applied proposal submits a property update to the golden record and changes the proposal's status to **Applied**. A rejected proposal changes status to **Rejected** and is not applied. Re-running **Analyze** after applying changes returns no further proposals for properties that now match.

## What this changes

Applying a proposal updates one property on the golden record using the same mechanism as editing it directly on the golden record page - it does not change any other properties, and it does not create a new record. **Apply All** and **Reject All** only affect the pending proposals from the golden record id you analyzed - proposals from analyzing this document against a different golden record are not included.
