---
layout: cluedin
title: Frequently asked questions
parent: Knowledge base
permalink: /kb/faq
tags: ["getting-started", "faq"]
nav_order: 15
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

## What happens if I change the default configuration installed using the Azure Marketplace offering?

Any modifications made to the default configuration, except those explicitly documented as post-install adjustments on the documentation portal, will result in the termination of support. This includes:

- Premium Support.
- Azure Managed Application.
- And any other customer support service.

The reason for this is the high probability that the cluster may not operate correctly. Changes outside the documented scope are considered out of support, and CluedIn will not provide assistance or troubleshooting for configurations that deviate from the originally installed setup.

Allowed changes include the following:

- Adjusting requests and limits on CluedIn operating pods (CPU and memory).
- Setting up and receiving assistance with the CluedIn backup solution.
- Configuring single sign-on (SSO).
- Setting up SMTP details for welcome emails.
- Configuring extended alerts via CluedIn (CluedIn-specific alerts only, not customer-specific).
- Troubleshooting ad-hoc cluster failures, if determined not to be caused by the customer.
- Upgrading environments.
- Installing the product using the default configuration.
- Using Azure Key Vault to provide secrets to the cluster.
- Performing general AKS maintenance on the default configuration.

Any deviation from this list will be considered out of support. Assistance for such issues is not guaranteed and may incur additional charges.

## What is different between CluedIn and other data integration platforms?

Whether you use SAP Data Services, Azure Data Factory, SSIS, Talend, Python, SAS Institute, Informatica PowerCenter, or other ETL-based tools, they all hold something in common: you, as the engineer, architect, or business user, must map different systems together.

At CluedIn, we have found that identifying which IDs need to be connected between systems to unify or connect records is often the hardest part, and sometimes impossible.

CluedIn uses a schema-less based integration pattern that doesn't require you to define how systems connect. Instead, you provide a much simpler and streamlined mapping, and CluedIn automatically detects relationships between the systems, often uncovering connections that you would not see yourself. 

## What happens with low-quality, invalid, or messy ingested data?

CluedIn is an extract-load-transform (ELT) type of integration platform. We ingest data as-is, without cleaning or transformation. 

CluedIn detects and addresses data quality issues through its processing engine:

1. Automated cleaning and normalization into the highest-fidelity format.
1. Support for “blacklisted values”, with the ability to remove or transform invalid data during processing.
1. Rules to define what qualifies as valid or invalid data.

Data that meets standards continues through processing; data that fails is quarantined for review and resolution.

## How does CluedIn handle sensitive and personal data?

For personal data:
1. CluedIn automatically detects personal data and alerts you to its presence.
1. Depending on your requirements, you can then choose to mask, anonymize, or remove the data.

For sensitive data:
- The definition of what is considered sensitive varies across organizations.
- For this reason, CluedIn lets you manually flag records as sensitive, building a custom data model that learns and automatically flags similar data over time.

## Does storing raw data in four databases require a lot of storage?

Not necessarily. You control what data is ingested into CluedIn. For many data types, we extract only what is needed (for example, content and metadata from files), not full copies.

All stored data is compressed, so total storage is often much smaller than the source. For example, customers processing hundreds of terabytes of source data typically use 2–3 TB of storage in CluedIn.

## How can I extract data from CluedIn?

CluedIn is designed to sit between source and target systems, making data extraction simple and reliable.

Two main options are recommended:

1. GraphQL API – Query all data in your CluedIn account, selecting specific properties as needed. Results are returned in JSON format.
1. Data Streams – Send (push) data directly to a target system (SQL database, Apache Spark, Power BI, or Data Warehouse).

{:.important}
Avoid using CSV or file exports in production as they can reintroduce data silos.

## Considering that CluedIn uses off-the-shelf (OTS) databases, can I access data directly from there?

While technically possible, direct database access is recommended only in developer environments.

In production, CluedIn provides GraphQL interfaces to safely query your data without exposing the underlying stores.

Native database access is disabled by default in Kubernetes deployments for security reasons.

## What if my systems are highly customized—can CluedIn still integrate them?

Yes. CluedIn integrations assume that the source model can be customized. You will still need to map your source objects into CluedIn to achieve optimal results.

The integrations handle the connection, scheduling, paging, and data delivery—you simply define the logical mapping to the Clue object. Unlike other platforms, CluedIn does not require you to define every connection. This is handled automatically instead.

## If CluedIn connects my data, won't the data model be messy?

At first, yes—because your data landscape is typically messy. CluedIn’s goal is to reveal the natural connections in your data, not impose an artificial structure.

Once those relationships are discovered, you can project clean, business-specific models for different use cases. The underlying graph engine ensures fast, scalable projections.

## Can I automate CluedIn administration?

Yes. The CluedIn administration UI is built entirely on top of our REST API. Anything you can do in the interface can also be scripted via:

- REST API
- PowerShell
- Other scripting languages

This enables full automation of administrative tasks.

## What to do if I have made a change that requires me to re-process the data?

Re-processing is common and expected. You can choose the scope of re-processing based on your needs:

- Source level

- Record level

- Custom options like business domain level

- Global re-processing

## Does CluedIn index everything?

Yes. However, you can optimize indexing by specifying vocabulary key data types during setup. This improves search performance and efficiency while keeping all data searchable.

## How does CluedIn guarantee data consistency across multiple databases?

CluedIn uses an enterprise service bus (ESB) with an eventual consistency model. Data is ingested into a transactional log, which multiple databases read asynchronously.

This guarantees transactional delivery of data and ensures stability even under heavy processing loads.

## Why is CluedIn written in C#?

CluedIn is built on .NET Core and C# for several reasons:

- Proven scalability and performance in large systems.

- Strong ecosystem support from Microsoft and the open-source community.

- Maintainable architecture with clear separation of concerns.

- High speed compared to most modern languages.

While C# may be slightly less memory-efficient, the trade-off enables faster, more stable delivery.

## I am not a C# developer. Can I still extend CluedIn?

Yes. CluedIn communicates via HTTP (REST), so you can use any language that supports REST APIs (Python, R, Go, and so on).

However:

- You cannot inject custom logic into the same application domain as CluedIn.
- You must host your custom code separately. 
- Crawler templates are available only in C#. 

## What type of data is CluedIn not suited for?

CluedIn may not be ideal for:

- Internet of things (IoT) or signal data that needs near-real-time dashboards without governance or cataloging.
- Simple integrations (for example, connecting Dropbox to a CRM) with clear record relationships.
- Use cases that prohibit data movement, because CluedIn works by copying and processing ingested data.

