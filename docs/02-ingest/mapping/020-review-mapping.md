---
layout: cluedin
title: Review mapping
parent: Mapping
grand_parent: Ingest
nav_order: 20
permalink: /ingest/mapping/review-mapping
content_type: how-to
redirect_from: ["/integration/review-mapping"]
source_path: docs/040-integration/data-sources/180-review-mapping.md
tags: ["integration", "mapping"]
last_modified: 2023-11-07
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

After the mapping is created, review the mapping details to make sure that your records will be produced and merged in the most efficient way. This article will guide you through the essential aspects to check when reviewing your mapping details.

![Infographic: what to check in mapping details - 1 Properties, 2 Identifiers correct for merging, 3 optional Relationships for linking records]({{ "/assets/images/integration/data-sources/review-mapping-1.gif" | relative_url }})

{:.important}
Before the data is processed, your mapping changes won't affect the existing records in CluedIn.

To open the mapping details, on the **Map** tab of the data set, select **Edit mapping**. You'll see three tabs containing all mapping details:

- [Map columns to vocabulary key](#properties) – here you can check which properties will be sent to CluedIn after processing.

- [Map entity](#identifiers) – here you can check the general details of the records that will be created after processing and the identifiers that will uniquely represent the records.

- [Add edge relations](#relationships) – here you can create rules for establishing the relationships between golden records.

### Properties

On the **Map columns to vocabulary key** tab, check how the original fields will be mapped to the vocabulary keys in CluedIn after processing. The following actions are available for you:

- Ignore certain fields if you don't want to have them in CluedIn after the data is processed.

- Map the original field to a different vocabulary key.

- Add [property rules](/ingest/mapping/property-rules) to improve the quality of mapped records by normalizing and transforming property values. 

### Identifiers

On the **Map entity** tab, review the general mapping details and check the identifiers that will uniquely represent the records in CluedIn—**primary identifier** and **identifiers**.

**What are general details?**

- Business domain and vocabulary.

- Entity name – name of the records that is displayed on the search results page and on the record details page.

- Preview image, description, date created, and date modified – record properties that you can find on the search results page and on the record details page. You can select which column should be used for each of these settings.

- Author – the column whose value is added to the **Authors** of each record when the data set is processed, such as a created-by or owner column. Select it in **Author** on the **Meta data** page of the **Mapping** tab. A record where the column is empty gets no author. Like the per-record origin below, the setting is stored as a marked block in the mapping's [advanced mapping code](/ingest/mapping/advanced-mapping-code); change it on the **Meta data** page rather than in the code.

**What is a primary identifier?**

A primary identifier is a unique identifier of the record in CluedIn. If the primary identifiers are identical, the records will be merged. This merging is faster than creating a deduplication project because it is done on the fly and is based on strict equality matching. The deduplication project, on the other hand, is based on fuzzy matching and requires you to define matching criteria, making it a more time-consuming process. Even if you prefer to merge records by running a deduplication project, merging by primary identifiers produces cleaner, "pre-merged" records. As a result, the deduplication project will generate better results and be more performant.

**Options for generating the primary identifier**

Depending on how unique you consider the records to be, you can choose one of the following options for generating the primary identifier:

- **Single key** – CluedIn will generate unique primary identifiers for the records based on the selected property. This is the most commonly used option because data often already contains unique identifiers (for example, GUIDs) from the source systems.

- **Auto-generated key** – CluedIn will generate unique primary identifiers for the records. Choosing this option may lead to an increased number of duplicates in the system, but you can mitigate this by running a deduplication project afterwards.

- **Compound key** – CluedIn will generate unique primary identifiers for the records by combining selected properties. Choose this option if you are confident that the data structure won't change in the future. For example, you can select the following properties to generate a compound key: First Name, Last Name, City, Address Line 1, and Country.

The following diagram will help you in determining which option to use for generating the primary identifier.

![Decision tree: if the source has a unique identifier, use a single key; if not and the data set is stable over time, use a compound key; otherwise use an auto-generated key]({{ "/assets/images/integration/data-sources/review-mapping-2.png" | relative_url }})

**Example**

We ingested a file with 1,000 records personal data containing the following columns: ID, First Name, Last Name, Email, SSN, and Country Code. To create the mapping, we selected the Auto Mapping type, and CluedIn automatically generated the mapping for the data set. Since our data set included the 'ID' column, it was automatically selected as the primary identifier. This is a favorable option because no empty or duplicate values were found during the current data set check. It means that the ID is a reliable value to uniquely represent the record in CluedIn.

![Primary identifier section in mapping details with trainingcontact.id selected and the Status panel showing no empty and no duplicated values]({{ "/assets/images/integration/data-sources/review-mapping-3.png" | relative_url }})

If we select a column that contains duplicate values (for example, country), the status check will immediately inform us of the number of duplicate values in the data set. By selecting  **View more details**, you can view the number of duplicate values in the data set, which values are duplicates, and the number of times the duplicate value occurs in the data set. Referring to the screenshot below, there are 3 duplicate values in the data set: United States, Canada, and Spain. The value United States occurs in 550 records. If we proceed with this as the primary identifier and process the data, all 550 records will be merged into a single golden record. In this case, the country cannot serve as a unique representation for each record, as it is acceptable for records to share the same country.

![Primary Identifier Status pane warning that the primary identifier has duplicated values, listing job_title values with 49 duplicates and their counts]({{ "/assets/images/integration/data-sources/review-mapping-4.png" | relative_url }})

However, if you are confident that the selected property can uniquely represent the record, you can proceed with processing the data. Records with identical primary identifiers will be automatically merged, eliminating the need for a separate deduplication project.

{:.important}
If the primary identifier contains an empty value, it is replaced with a hash. If your data set contains a record that is nearly identical to the one with the hash value, they will not be merged because the hash is a unique value. In such cases, you can initiate a deduplication project as a solution.

**Take the origin from a column**

A primary identifier is made of the business domain, an **origin**, and the value of the selected property, for example `/Customer#crm:C0001`. By default every record of a data set gets the same origin. When the records of one data set come from several systems and the system is a column in the data (for example, a `sourceSystem` column with values such as `crm` or `erp`), you can take the origin from that column instead, so each record's primary identifier says which system it came from.

1. On the **Mapping** tab of the data set, select **Identifiers**, and then select **Edit origin**.

1. Turn on **Take the origin from a column**, and then select the **Column**. Only mapped columns are listed.

1. Select **Save**.

The **Identifiers** page then shows which column the origin is taken from. The setting is kept with the mapping and applies the next time the data set is processed:

- Each record's primary identifier uses the value of the column as its origin. The characters `#` and `:` are removed from the value, because they separate the parts of an identifier.

- A record where the column is empty keeps the origin selected above the toggle, which stays the default.

- Golden records that were already produced keep the primary identifier they were created with, and gain the new identifier when they are processed again. A record created from the new identifier has it as its primary identifier.

The setting is stored as a marked block in the mapping's [advanced mapping code](/ingest/mapping/advanced-mapping-code) (**Code mapping before sending clues**). Change it on the **Identifiers** page rather than in the code.

![Entity Identifiers pane of a golden record whose primary identifier is /Customer#sap:C9999, with sap as the source of its ID identifier, taken from the record's sourceSystem column]({{ "/assets/images/integration/data-sources/origin-from-column-result.png" | relative_url }})

**What are identifiers?**

Identifiers can uniquely represent the record in CluedIn, in addition to the primary identifier. If two identifiers are identical, the records will be merged. CluedIn automatically detects properties that can be used as additional identifiers. For example, if the primary identifier is the ID, then the additional identifier could be the email.

Even if there are no duplicate values according to the primary identifier, but there are some according to additional identifiers, the records will be merged.

The following diagram will help you in determining if you need to add additional identifiers.

![Decision tree: if there is another unique identifier and you trust your data, add identifiers; if you do not trust it, run a dedup project later; if there is none, do not add identifiers]({{ "/assets/images/integration/data-sources/review-mapping-5.png" | relative_url }})

### Relationships

A relationship is a connection or association between two or more golden records that indicates how the records are related or interact with each other.

If you want to connect the records from the current data set to other records in CluedIn, you can add relationships between such records. The procedure for adding relationships between records is described in our "Getting started" guide. For more information, see [Add relationships between records](/model/relationships/tutorial-add-relations).

You can add a relationship before or after you process the records. If you add a relationship after processing, you need to process the records again.

When you start creating a relationship, you have to select a **property** from the current data set that references another property existing in CluedIn. For instance, in the case of SQL tables, this property could be a foreign key that connects two tables. The relationship will be established based on the selected property. Then, you need to choose the **edge mode**:

- **Edge** – CluedIn creates relationships between the records based on the origin.

- **Strict Edge** – CluedIn creates relationships between the records that belong to a specific data set, data source, or data source group.

- **Fuzzy Edge** – CluedIn creates relationships through fuzzy matching based on the Name property of the records.

After you select the edge mode, you need to choose the **edge type** to define the nature of relationships between records (for example, /WorksFor, /RequestedBy,/LocatedIn).

**Example**

We have 2 data sets:

- **Companies** – contains the following columns: Company_ID and Company_Name.

- **Employees** – contains the following columns: EmployeeID, First_Name, Last_Name, and Company_ID. Here, the Company_ID defines the company where an employee works.

To connect employees to companies in CluedIn, we can create a relationship in the mapping details of the **Employees** data set. In this case, the Company_ID will serve as the property upon which the relationship is built. We select the **Strict Edge** mode because we are aware of the data set to which we want to connect the employees. Once the processing is complete, all employees who work for a particular company will be shown on the **Relations** tab of a company record.

![Relations graph centred on the DB Schenker AG company record, linked by edges such as /BilledTo, /IsRoleOf, /HasContract and /ManagedAs to invoices, an address, a contract and other records]({{ "/assets/images/integration/data-sources/review-mapping-7.png" | relative_url }})

### Business domain lineage

Before you process a data set, check what else in CluedIn acts on the business domain you are mapping its records to. On the **Mapping** tab, the **Overview** reads from left to right: the data set's columns, the record they become, and then a **Business domain lineage** column listing, for the mapping's business domain:

- **Rules** – data part, survivorship and golden record rules whose condition names the business domain, active or not.

- **Workflow and approval rules** – approval rules whose condition, or one of whose steps, names the business domain.

- **Streams** – streams whose filter names the business domain, with whether they are started.

- **Deduplication projects** – deduplication projects scoped to the business domain.

- **Enrichers** – enrichers that run on the business domain, decided the same way enrichment decides it (including an enricher's default and parent business domains).

- **AI agents** – AI agents with a job that reads the business domain.

Each card is joined to the record by a line, which is solid and moving when the card lists something and dashed when it's empty. Each item links to its own page. An item matches when its condition names the business domain with the **Equals**, **Contains** or **In** operator, at any level of the condition. A card you don't have permission to view is shown empty. On a narrower screen the overview zooms out to fit the whole width; use the zoom controls above it to zoom back in.

The lineage only reads: it doesn't change the mapping or any of the listed items.

![Mapping Overview of a Customer data set: its columns on the left, the Customer record in the middle, and on the right a Business domain lineage column with two rules, an approval rule and a stream joined to the record by lines, plus empty cards for deduplication projects, enrichers and AI agents]({{ "/assets/images/integration/data-sources/mapping-lineage.png" | relative_url }})
