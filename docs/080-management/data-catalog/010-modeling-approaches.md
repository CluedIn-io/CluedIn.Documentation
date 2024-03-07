---
layout: cluedin
nav_order: 1
parent: Data catalog
grand_parent: Management
permalink: /management/data-catalog/modeling-approaches
title: Modeling approaches
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about two data modeling approaches in CluedIn: agile data-first approach and traditional model-first approach.

## Data-first approach

The data-first approach focuses on agility, flexibility, and faster time-to-value. It provides the opportunity to ingest your data first and then dynamically create an entity type and vocabulary as needed.

Unlike a predefined schema, the data-first approach uses flexible data structures to adapt to changing requirements. This allows your data models to iteratively evolve based on feedback, data analysis, and the dynamic nature of business needs.

The following video shows an example of creating a shared model using vocabulary key mapping and survivorship rules.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/920523650?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Vocabulary key mapping"></iframe>
<iframe src="https://player.vimeo.com/video/910767689?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" title="Deduplication in practice"></iframe>
</div>

## Model-first approach

Traditional model-first approach involves the creation of a comprehensive data model that defines the structure, relationships, and constraints of master data. This approach requires a thorough understanding of the business domain, data requirements, and anticipated data usage scenarios.

You need to think about all potential scenarios within your data beforehand. When it comes to practice, it may turn out that the model you've built does not align with your requirements, particularly when unforeseen possibilities and cases arise. After preparing the model, it may turn out that certain vocabulary keys are missing or that the model is not ideally suited for your specific dataset. That's why the data-first approach is the preferred one.