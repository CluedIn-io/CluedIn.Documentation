---
layout: cluedin
title: Golden records
parent: Key terms and features
permalink: /key-terms-and-features/golden-records
nav_order: 5
has_children: true
tags: ["golden record"]
---

A golden record is an **accurate and consolidated representation of a data subject**, such as an organization or an employee, derived from multiple sources. It provides a 360-degree view of a data subject, facilitating a deeper understanding of its current state and the reasons behind it.

A golden record is created through a process of data integration, enrichment, cleaning, deduplication, and manual data entry. Each step in the process is registered as a separate element called a _data part_. A golden record is usually **made up of multiple data parts**. The purpose of creating a golden record is to provide a single source of truth, ensuring data consistency, improving data quality, and enabling better decision-making. A golden record serves as a reliable reference point that can be used by different systems, departments, or stakeholders within the organization.

Golden records in CluedIn are stored for **performance reasons**, but essentially, they are a **projection** of all the sources and rules that you have created. That is why golden records adapt based on the changes that are applied within CluedIn. This makes golden records very **agile**—you can easily **revert changes** and **re-shape your golden records at any point in time**.

## Concept of golden record

A golden record is a **multi-level graph**. A graph structure consists of nodes (discrete objects) that can be connected by relations. Even though this concept can be a bit hard to comprehend at first, once you understand it, you'll appreciate the great flexibility that it gives you.

Golden records can have 2 types of relations:

- [Linking similar records together](#linking-similar-records-together).

- [Linking golden records together](#linking-golden-records-together).

### Linking similar records together

In CluedIn, similar records are grouped together under the same banner called **golden record**. Generally, the golden record is composed of records from multiple sources.

For example, suppose we have a golden record that is composed of 2 records from different sources: one record from CRM and the other record from ERP. These distinct nodes are referred to as **data parts**.
 
![golden-record-1.png](../../assets/images/key-terms-and-features/golden-record-1.png)

The more sources you add, the bigger your golden record model becomes.

![golden-record-2.png](../../assets/images/key-terms-and-features/golden-record-2.png)

Since the golden record is a projection of the sources, adding or removing a source is not an issue. This is what gives great flexibility of golden records in CluedIn.

### Linking golden records together

We always say that _a golden record is a graph of a graph_. What it means is that when the golden record is being produced, CluedIn has the ability to link golden records together using **edges**. An edge is simply a relation. You can define an edge using rules or during the mapping. When you define an edge, CluedIn can connect golden records together as shown in the example. 

![golden-record-3.png](../../assets/images/key-terms-and-features/golden-record-3.png)

So, when we say that a golden record is a graph of a graph, it is because at the end, the entire view of the models is as follows.

![golden-record-4.png](../../assets/images/key-terms-and-features/golden-record-4.png)

## Golden record step by step

To make the golden record generation process easier to understand, we'll start with the simplified explanation that does not include various types of rules. We’ll focus on the records and use the concepts of bronze, silver, and golden layers from the medallion architecture for visual assistance.


| Medallion architecture term | CluedIn term | Definition |
|--|--|--|
| Bronze layer | Source record | This is a record in its basic, raw format as it was in the source system. |
| Silver layer | Data part | This is a mapped record with all of the pre-processing rules and changes applied to it. |
| Golden layer | Golden record | This is a record that you can trust, usually formed by aggregating data parts to the existing golden record.  |

Generally, a new record is associated with the bronze layer. This is the record that comes from a specific source—it may come from a file, an Azure Data Factory pipeline, or a database. We call this record a **source record**.

The process of generating a golden record spans from source records, through data parts, to the golden record. Next, we’ll describe each step that the record goes through to become a new golden record or aggregate into the existing golden record.

![golden-record-5.png](../../assets/images/key-terms-and-features/golden-record-5.png)

### Source record (bronze)

A source record is a raw record that has been ingested into CluedIn from a source system. It is generally stored in JSON format. Such record has not been modified in any way. You can see source records on the **Preview** tab of the data set.

### Data part (silver)

When records appear in CluedIn, you need to add a semantic layer to transform them into a format that CluedIn can understand. This process is called [mapping](https://documentation.cluedin.net/playbooks/data-ingestion-playbook/concept-of-mapping). Once all the steps of the mapping process have been performed, you get what we call a **data part**. Essentially, a data part is an aggregation of all changes to the record coming from a single source after it has been mapped.

![golden-record-6.png](../../assets/images/key-terms-and-features/golden-record-6.png)

During the mapping process, the source records can go through multiple steps:

- Changes to the values of mapped records via [property rules](/integration/additional-operations-on-records/property-rules).

- Changes to the mapped records via [pre-process rules](/integration/additional-operations-on-records/preprocess-rules).

- Changes to mapped records via [advanced mapping code](/integration/additional-operations-on-records/advanced-mapping-code).

- Approving or rejecting mapped records in the [quarantine](/integration/additional-operations-on-records/quarantine).

All in all, a data part is a record in a format that CluedIn can understand and that has already gone through multiple processes to ensure it is valid and ready for the production of a golden record.

### Golden record (golden)

When you [process](/integration/process-data) the data set, CluedIn checks if the data part can be associated with the existing golden record.

![golden-record-7.png](../../assets/images/key-terms-and-features/golden-record-7.png)

If the data part can be associated with the existing golden record—they share the same [codes](/key-terms-and-features/entity-codes)—then it is **aggregated to the existing golden record**. In this case, the golden record is re-processed. If the data part cannot be associated with the existing golden record, then a **new golden record is created**.

**What happens when golden record is re-processed?**

When a new data part is added to the existing golden record, CluedIn incorporates all of its properties into the golden record. However, conflicts can arise between new and existing data parts when the values for the same property differ. In such cases, the **latest value** is used in the golden record by default. You can also set up your strategy for defining the winning value using [survivorship rules](/management/rules/rule-types#survivorship-rules).

**How does CluedIn define the latest value?**

CluedIn takes the latest value from the data part with the **most recent sort date**. The sort date is determined by selecting the first available date among modified, created, and discovery dates:

- If there is a modified date, then this date is used as the sort date.

- If there is no modified date, but there is a created date, then this date is used as the sort date.

- If there is no modified or created date, then the discovery date is used as the sort date. The discovery date is always present in the data part as it is the date when the data part was created in CluedIn.

When data parts appear from the same source, they are added to the same **version branch**, where each data part is a separate version with its own sort date and status. The sort date of a version is used to determine which values from the branch are used in the golden record. 

![golden-record-8.png](../../assets/images/key-terms-and-features/golden-record-8.png)

**How can you re-shape a golden record?**

Depending on the projects and processes that are running in CluedIn—[clean projects](/preparation/clean), [deduplication projects](/management/deduplication), [enrichers](/preparation/enricher), manual modifications, data ingestion—the golden record can be changed. For example, if you create a clean project and it affects a golden record, a new data part is added to that golden record. Similarly, if you have an enricher that affects a golden record, a new data parts with the properties from third-party source is added to the golden record.

![golden-record-9.png](../../assets/images/key-terms-and-features/golden-record-9.png)

If you are not satisfied with the changes made to a golden record by a specific data part, you can simply delete such data part.

## Golden record page

In CluedIn, you can find a golden record using [search](/key-terms-and-features/search). The golden record page contains several tabs where you can find all relevant information about a golden record:

- Overview – here you can view general information about a golden record, such as entity properties, vocabularies, sources, and more.

- Properties – here you can view all properties that the golden record has as well as add new properties.

- Relations – here you can view which golden records the current golden record is related to.

- Pending changes

- [History](/key-terms-and-features/golden-records/history) – here you can view all data parts (versions of clues that make up a data part) of a golden record as well as all outgoing relations (edges) of a golden record.

- Explain log – here you can view detailed information about the operations performed on a golden record and its data parts.

- Topology – here you can view the visualization of data parts that form a golden record.

- Hierarchy – here you can view the hierarchy projects that the current golden record is a part of.
