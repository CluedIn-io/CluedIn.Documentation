---
layout: default
title: Additional operations on records
parent: Data sources
grand_parent: Integration
nav_order: 060
has_children: true
permalink: /integration/additional-operations-on-records
tags: ["integration"]
last_modified: 2023-11-07
---

Although normalizing, transforming, and improving the quality of records before processing is optional, we recommend that you do it for several reasons:

- Ensure alignment with your data normalization polices.

- Get better matches in deduplication projects.

- Reduce the number of records to clean.

- Optimize the streaming of records.

In this section, you will learn how to normalize and transform property values using property rules and improve the overall quality of records with pre-process rules. Both property and pre-process rules are applied to the records during processing, with property rules taking precedence.

![addional-operations-1.png](../../assets/images/integration/additional-operations/addional-operations-1.png)

You will also learn how to handle anomalous records in the quarantine area and how to interpret logs and monitoring statistics to get insight into what is going on with your records.