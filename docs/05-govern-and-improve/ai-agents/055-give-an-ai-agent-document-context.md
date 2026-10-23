---
layout: cluedin
title: Give an AI agent document context
parent: AI agents
grand_parent: Govern & improve
nav_order: 55
permalink: /govern/ai-agents/give-an-ai-agent-document-context
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to give an AI agent documents to use as context, either by uploading a file directly to the agent or by attaching a document already uploaded to the Ingest area's Unstructured Documents section.

## Prerequisites

- The agent needs an embedding AI endpoint configured, so uploaded documents can be vectorized. For more information, see [Prerequisites to using AI agents](/govern/ai-agents/prerequisites-to-using-ai-agents).
- For image or scanned-PDF content, the agent also needs a Vision endpoint configured for OCR.

## Upload a document directly to an agent

**To upload a document directly to an agent**

1. Open the agent and go to the **Documents** tab.

1. Select **Upload**, then choose a PDF, Word, PNG or JPEG file.

The document appears with a status of **Pending**, and CluedIn extracts, chunks and embeds its text in the background so the agent can retrieve it as context during a run.

## Attach a document already in Unstructured Documents

If a document has already been uploaded to **Ingest** > **Unstructured Documents** - for example because it was also used to [link entities to golden records](/ingest/unstructured-documents/link-extracted-entities-to-golden-records) or [enrich a golden record](/ingest/unstructured-documents/create-or-enrich-records-from-a-document) - you can attach the same document to an agent instead of uploading it again.

**To attach an existing unstructured document**

1. Open the agent and go to the **Documents** tab.

1. Select **Attach Existing Document**.

1. Select **Attach** next to the document you want to add.

CluedIn copies the document onto the agent and processes it the same way as a direct upload.

## Verify the result

A document reaches a status of **Processed** once it has been chunked and embedded; a document the agent can use as context shows a non-zero chunk count. Select the eye icon next to a processed document to view its extracted content.

## If something goes wrong

A document with a status of **Failed** means extraction or embedding could not complete - for example, no embedding endpoint is configured, or an image was uploaded with no Vision endpoint configured. Configure the missing endpoint and upload or attach the document again.
