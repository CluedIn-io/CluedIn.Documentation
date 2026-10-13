---
layout: cluedin
title: 1.1.3. Building a single customer view
parent: CluedIn fundamentals
grand_parent: Learning paths
nav_order: 40
permalink: /learning-paths/fundamentals/building-a-single-customer-view
content_type: tutorial
redirect_from: ["/training/fundamentals/building-a-single-customer-view"]
source_path: docs/220-training/fundamentals/004-building-a-single-customer-view.md
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

## Part 1

**Module:** [1.1. Ingestion](/learning-paths/fundamentals/ingestion)

**Level:** Beginner

In this session, we’ll focus on building a single customer view by identifying and merging duplicate records. We’ll explore the concept of primary identifiers in CluedIn and how to use them to proactively unify duplicate data into a single, accurate customer view.

**Presented by:** Jocelyn Ramirez, your Customer Success Manager, and Matthew Carter, your CluedIn AI Trainer

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1088432455?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="CluedIn Fundamentals Merging by identifiers"></iframe></div>

**Presentation:** <a href="/assets/other/training-ppt/merging-by-identifiers.pptx" download>Download PPT</a>

**Useful resources:**

- [Identifiers](/model/identifiers)

- [Origin](/get-started/core-concepts/origin)

- [Business domain](/model/business-domains/business-domains-explained)

## Part 2

**Module:** [1.1. Ingestion](/learning-paths/fundamentals/ingestion)

**Level:** Beginner

In this session, we’ll explore an alternative approach to identifying and merging duplicate records as part of building a single, unified customer view—a deduplication project. You’ll learn how to set up and work with a deduplication project, understand when this method is most effective, and see how it compares to other deduplication strategies, such as merging by identifiers.

**Presented by:** Jocelyn Ramirez, your Customer Success Manager, and Matthew Carter, your CluedIn AI Trainer

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1088808167?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="CluedIn Fundamentals: Deduplication project"></iframe></div>

**Presentation:** <a href="/assets/other/training-ppt/deduplication-project.pptx" download>Download PPT</a>

**Useful resources:**

- [Deduplication](/master/deduplication)

## Part 3

**Module:** [1.1. Ingestion](/learning-paths/fundamentals/ingestion)

**Level:** Beginner

In this session, we'll explore strategies for defining the uniqueness of records—particularly in situations where the property used to generate a primary or additional identifier is missing or empty. In CluedIn, when two or more records share the same identifier—whether it’s primary or additional—they will be merged into a single golden record. That’s why it’s important to always use valid, unique identifiers.

**Presented by:** Jocelyn Ramirez, your Customer Success Manager, and Matthew Carter, your CluedIn AI Trainer

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1090434884?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="CluedIn Fundamentals Defining record uniqueness"></iframe></div>

**Presentation:** <a href="/assets/other/training-ppt/defining-record-uniqueness.pptx" download>Download PPT</a>

**Useful resources:**

- [Identifiers](/model/identifiers)

## Part 4

**Module:** [1.1. Ingestion](/learning-paths/fundamentals/ingestion)

**Level:** Beginner

In this session, we'll learn how to identify and resolve data quality issues using CluedIn’s edit mode and validations. This helps fix invalid or incomplete identifiers before processing, ensuring more accurate matching and preventing unintended merges across your data.

**Presented by:** Jocelyn Ramirez, your Customer Success Manager, and Matthew Carter, your CluedIn AI Trainer

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1091237527?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="CluedIn Fundamentals Edit mode and validations"></iframe></div>

**Presentation:** <a href="/assets/other/training-ppt/edit-mode-and-validations.pptx" download>Download PPT</a>

**Useful resources:**

- [Identifiers](/model/identifiers)

- [Modify source records](/ingest/processing/preview#modify-source-records)

- [Validations](/ingest/processing/validations)