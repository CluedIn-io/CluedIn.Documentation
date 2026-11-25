---
layout: cluedin
title: Upload and extract unstructured documents
parent: Unstructured documents
grand_parent: Ingest
nav_order: 10
permalink: /ingest/unstructured-documents/upload-and-extract-unstructured-documents
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to upload PDF, Word, PowerPoint, Excel and image documents to CluedIn, organize them into folders, and what happens to them after upload: text extraction, OCR for scanned content, and AI-based classification.

## Prerequisites

- You need access to the **Ingest** area.
- For AI classification and the features covered in the following articles (entity linking, record creation and enrichment), your organization needs at least one AI **Chat** endpoint configured. For OCR of scanned documents, it also needs a **Vision** endpoint. For more information, see [Prerequisites to using AI agents](/govern/ai-agents/prerequisites-to-using-ai-agents), which covers how AI endpoints are configured for your organization.

## Upload unstructured documents

**To upload unstructured documents**

1. On the navigation pane, go to **Ingest** > **Unstructured Documents**.

1. In the folder list on the left, select the folder to upload into, or leave **Unfiled** selected to upload without a folder. For more information, see [Organize documents into folders](#organize-documents-into-folders).

1. Do one of the following:

   - Drag one or more files onto the upload area.
   - Drag a folder onto the upload area. Every supported file inside the folder is uploaded; files of an unsupported type are skipped.
   - Select **Browse Files** and choose one or more files.

   Supported file types are PDF, Word (`.docx`), PowerPoint (`.pptx`), Excel (`.xlsx`), and images (`.png`, `.jpg`, `.jpeg`). Any other file type is reported back as skipped, with the reason, instead of stopping the rest of the upload.

1. The uploaded documents appear in the table with a status of **Pending**, and CluedIn starts processing them in the background.

## Organize documents into folders

Folders let you group uploaded documents - for example, by source, project or document type. A document belongs to at most one folder.

**To create, rename or delete a folder**

1. On the navigation pane, go to **Ingest** > **Unstructured Documents**.
1. In the folder list on the left, select **New Folder**, enter a name, and select **Create**.
1. To rename or delete an existing folder, select its **…** menu and choose **Rename** or **Delete**.

   A folder can only be deleted while it is empty. Move or delete its documents first.

**To move a document into a folder**

1. In the document table, select the **…** menu for the document and choose **Move to folder**.
1. Select the destination folder, or **Unfiled** to remove it from its current folder.

Select **All Documents**, **Unfiled**, or a specific folder in the left-hand list to filter the table to that scope.

## How processing works

Each document moves through the following statuses:

| Status | Meaning |
|---|---|
| Pending | Uploaded, waiting to be processed. |
| Extracting | CluedIn is extracting the document's text. |
| Classifying | Text extracted; CluedIn is classifying the document and looking for named entities (see [Link extracted entities to golden records](/ingest/unstructured-documents/link-extracted-entities-to-golden-records)). |
| Processed | Finished. The extracted text (and classification, if available) is ready to view. |
| Failed | Processing could not complete. Select the status badge to see the reason. |

For PDF, Word, PowerPoint and Excel files, text is extracted using the text layer already embedded in the file. If a PDF has little or no embedded text - typically a scanned document - and your organization has a Vision AI endpoint configured, CluedIn automatically falls back to OCR on the document's images instead of failing. PNG and JPEG images have no embedded text layer, so they always go through OCR and require a Vision AI endpoint to be configured; without one, image uploads fail extraction.

If a Chat AI endpoint is configured, CluedIn also classifies the document (for example, as a Contract, Invoice, Report or Resume) once its text has been extracted. Classification is skipped, and the document still reaches **Processed**, if no Chat endpoint is configured.

## Verify the result

Select the eye icon next to a processed document to open it. The **Extracted Content** tab shows the text CluedIn extracted, and the classification, if any, appears as a label at the top of the panel.

## Run a custom prompt against a document

Extraction, classification, entity linking and record creation cover the built-in ways CluedIn uses a document's content. For anything else - summarizing it, pulling out a specific value, checking it against a rule you describe in words - the **Custom Processing** tab runs a prompt of your own choosing against the document instead.

**To run a custom prompt against a document**

1. Open a processed document and go to the **Custom Processing** tab.
1. Enter a **Prompt** describing what you want from the document, and select **Run**.

   CluedIn sends the prompt together with the document's extracted text to the configured Chat AI endpoint and returns its free-text response.

1. Review the result. Running a new prompt replaces the previously stored result for this document.

### Verify the result

The AI's response appears below the prompt, with the date and time it was last run. The result is stored on the document - reopening the document later still shows the last prompt and its result.

### What this changes

Running a custom prompt only reads the document's extracted text and stores the AI's response on the document itself; it does not change any golden record. To update a golden record from a document, see [Create or enrich records from a document](/ingest/unstructured-documents/create-or-enrich-records-from-a-document).

## If something goes wrong

A document with a status of **Failed** shows the reason in a tooltip on its status badge - for example, a scanned PDF with no Vision endpoint configured, or a corrupted file. Fix the underlying cause (for example, configure a Vision endpoint) and upload the document again.
