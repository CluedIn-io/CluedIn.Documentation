---
layout: cluedin
title: Global Data Model
parent: Governance
nav_order: 2
permalink: /governance/global-data-model
tags: ["governance", "data model", "ontology", "business domains", "relationships"]
last_modified: 2026-09-24
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Global Data Model** gives you a visual view of the schema represented by the data in CluedIn.

Instead of looking at business domains one at a time, you can use the Global Data Model to understand how the complete graph fits together: which business domains exist, how they are connected, and which edge types define the relationships between them.

This makes the Global Data Model useful as an **ontology view** of your CluedIn graph. It helps data architects, data stewards, governance teams, and other users understand the structure of the mastered data without having to inspect individual records or relationships manually.

## What the Global Data Model shows

The Global Data Model represents your CluedIn graph as a network of business domains and edges.

Each business domain is displayed as a node in the model. The connections between nodes represent graph edges between records belonging to those domains.

Depending on the data in your environment, the model can show:

- **Business domains** – the major types of records represented in CluedIn, such as Company, Product, Material, Plant, Contract, Address, or Supplier Risk.
- **Entity types** – the entity type associated with each business domain.
- **Relationships** – connections between business domains.
- **Edge types** – labels that describe the meaning of a relationship, such as `/WorksFor`, `/Contains`, `/ProducedAt`, or `/References`.
- **Record counts** – the number of records associated with a business domain.
- **Relationship counts** – the number of relationships represented by an edge.

The result is a high-level map of the data model that exists across CluedIn.

## Understand the ontology

One of the main uses of the Global Data Model is to understand the **ontology** represented by your data.

An ontology describes the important concepts in a domain and how those concepts relate to one another. In CluedIn, business domains represent those concepts and graph edges represent their relationships.

For example, a manufacturing-oriented model could show that:

- A **Company** has **Purchase Orders**.
- A **Purchase Order** is associated with a **Plant**.
- A **Plant** produces a **Product**.
- A **Product** has a **BOM**.
- A **BOM** contains **Components**.
- A **Material** is referenced by a **Specification**.
- A **Supplier Risk** record relates to a **Company** or supplier.

Seeing these relationships visually can make the overall model much easier to understand than reviewing vocabularies and edge definitions independently.

The Global Data Model is therefore useful for answering questions such as:

- What are the main business concepts represented in CluedIn?
- Which business domains are connected?
- Which domains are highly connected to the rest of the graph?
- What edge types are being used between domains?
- Are there business domains that are not connected to anything else?
- Does the graph structure reflect the business model that we intended to create?
- Where might relationships or domains be missing?

## Navigate the model

Go to **Governance** > **Global Data Model** to open the model.

The graph canvas displays business domains as cards and edges as connections between those cards.

You can use the graph controls to zoom in and out when working with a large model.

For larger environments, the model can contain many business domains and relationships. Use the filtering and display controls to reduce the amount of information shown at one time.

## Search for business domains

Use the **Search business domains** field to find a specific business domain in the model.

This is useful when the graph is large and you want to quickly locate a particular part of the ontology rather than manually scanning the canvas.

For example, you could search for **Product** to identify the Product business domain and then inspect all the domains connected to it.

## Filter the Global Data Model

The filter panel provides summary information about the graph and allows you to control which parts of the model are displayed.

The summary can include:

- **Business domains** – number of business domains represented in the model.
- **Graph edges** – number of edge definitions represented in the model.
- **Records** – number of records represented by the selected scope.
- **Relationships** – number of relationships represented by the selected scope.

You can also filter the model by:

### Business domains

Use the **Business domains** filter to include or exclude particular business domains from the graph.

This is useful when you want to focus on one area of the enterprise model, such as Customer, Product, Supplier, or Reference Data.

### Sources

Use the **Sources** filter to control which data sources contribute to the displayed model.

This can help you understand how different source systems contribute to the overall graph and can be particularly useful when validating a newly onboarded source.

### Minimum records

Use **Minimum records** to hide very small business domains and focus on domains containing a larger number of records.

This can make a large graph easier to interpret by removing low-volume domains from the current view.

## Control what is displayed

The Global Data Model provides display options that let you control how much information appears on the graph.

### Relationship labels

Enable **Relationship labels** to display the edge type on the connections between business domains.

For example, a relationship can be labelled `/WorksFor`, `/Contains`, or `/HasProperties`.

Relationship labels are especially useful when using the model as an ontology diagram because they show the semantic meaning of each connection.

### Record counts

Enable **Record counts** to display the number of records represented by each business domain.

This gives you an immediate sense of the relative amount of data in different areas of the model.

### Display unconnected business domains

Enable **Display unconnected business domains** if you also want to see business domains that currently have no graph relationships to other domains.

Unconnected domains can be important when reviewing the completeness of a model. They may be intentionally standalone, or they may indicate that expected relationships have not yet been created.

### Size cards by record count

Enable **Size cards by record count** to make the visual size of business-domain cards reflect their record volume.

This helps large, high-volume domains stand out and can make it easier to identify the major hubs in the data model.

## Use the Global Data Model for governance

The Global Data Model is useful for more than visualization. It provides a shared view of the data architecture that can support governance and modelling activities.

### Validate the enterprise data model

Use the graph to compare the model implemented in CluedIn with your intended enterprise or domain data model.

You can review whether:

- Expected business domains are present.
- Expected relationships exist.
- Edge directions and edge types make sense.
- Important domains are unexpectedly disconnected.
- New sources have introduced business concepts or relationships that were not previously part of the model.

### Identify highly connected domains

Highly connected business domains often represent important concepts in the model.

For example, Company, Customer, Product, Material, or Location can become central nodes connected to many other domains.

Identifying these hubs can help when planning:

- Governance ownership.
- Data quality controls.
- Survivorship rules.
- Deduplication strategies.
- Reference-data management.
- Downstream publishing.

### Review the impact of model changes

When new business domains or relationships are introduced, the Global Data Model provides a convenient way to see how the overall graph has changed.

This is useful after:

- Onboarding a new source.
- Adding new edge mappings.
- Introducing a new business domain.
- Changing the way records are connected.
- Expanding an existing use case into additional domains.

### Explain the model to business users

The Global Data Model can also be used as a communication tool.

A graph of business concepts and their relationships is often easier for business users to understand than a list of schemas, tables, vocabulary keys, or edge definitions.

For example, instead of describing a model as a collection of technical mappings, you can show that a **Company** is connected to **Contracts**, **Purchase Orders**, **Products**, **Plants**, and **Locations**, and then explain the meaning of those relationships directly from the graph.

## Global Data Model and the CluedIn graph

CluedIn stores mastered data as a graph of records and relationships.

The Global Data Model is a higher-level representation of that graph. Rather than showing every individual record as a node, it summarizes the graph at the **business-domain and relationship level**.

This gives you two complementary views:

| View | Purpose |
|--|--|
| **Golden record graph** | Understand an individual record and the records connected to it. |
| **Global Data Model** | Understand the overall schema and ontology represented across the entire CluedIn graph. |

Use the individual record view when investigating a specific entity. Use the Global Data Model when you want to understand the structure of the whole data estate.
