---
layout: cluedin
title: Additional operations
parent: Integration
nav_order: 020
has_children: true
permalink: /integration/additional-operations-on-records
tags: ["integration"]
last_modified: 2024-01-15
---

In this section, you will learn how to improve the quality of your data in the **Data Sources** module in CluedIn.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/896923320?h=e1e5c408c7&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" title="Additional operations — rules, quarantine, and monitoring"></iframe>
</div>

Although normalizing, transforming, and improving the quality of records before processing is optional, we recommend that you do it for several reasons:

- Ensure alignment with your data normalization polices.

- Get better matches in deduplication projects.

- Reduce the number of records to clean.

- Optimize the streaming of records.

CluedIn provides the following tools that you can use to enhance the quality of your data before processing:

- [Preview](/integration/additional-operations-on-records/preview) – analyze the uploaded records and improve their quality before processing.

- [Validations](/integration/additional-operations-on-records/validations) – check the records for errors, inconsistencies, and missing values and fix these issues to improve the quality of the records.

- [Property rules](/integration/additional-operations-on-records/property-rules) – normalize and transform property values of mapped records.

- [Pre-process rules](/integration/additional-operations-on-records/preprocess-rules) – improve the overall quality of mapped records.

- [Advanced mapping code](/integration/additional-operations-on-records/advanced-mapping-code) – modify clues programmatically by applying complex conditions.

- [Quarantine](/integration/additional-operations-on-records/quarantine) – handle records that do not meet certain conditions set in property rules, pre-process rules, or advanced mapping.

- [Approval](/integration/additional-operations-on-records/approval) – approve or reject specific records to ensure that only verified records are sent for processing.

You will learn how to interpret [logs](/integration/additional-operations-on-records/logs) and [monitoring](/integration/additional-operations-on-records/monitoring) statistics to get an insight into what is going on with your records. Additionally, you will learn about the [removal of records](/integration/additional-operations-on-records/remove-records) that were created from a specific data source.