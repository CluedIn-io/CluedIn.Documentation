---
layout: cluedin
title: How to build an organizational hierarchy
parent: Knowledge base
permalink: kb/how-to-build-an-organizational-hierarchy
nav_order: 4
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

_The terminology and user interface described in this article might be slightly different depending on your version of CluedIn, but the overall logic remains the same._

In this article, you will learn how to build an organizational hierarchy to reflect the relations of entities within an organization. We are going to build a hierarchy of the following entities:

- **Business Group** – the highest-level organizational unit, typically representing a major line of business or a holding structure. It may consist of multiple companies that operate under a shared strategic direction but may have separate operations, finances, and compliance structures.

- **Company** – a legal and financial entity that operates under the business group. It typically has its own set of books for accounting and is responsible for reporting taxes, profits, and losses.

- **Legal Entity** – an organization that has legal standing in the eyes of the law—it can enter contracts, own assets, and be held liable. In many contexts, it is synonymous with a company, but some companies may contain multiple legal entities for operational, tax, or regulatory reasons.

- **Purchasing Organization** – responsible for procurement activities—purchasing goods and services, negotiating terms with vendors, and managing supplier relationships.

- **Sales Organization** – responsible for the sale and distribution of products or services. It defines the selling structure within a company or legal entity, including sales regions, channels, and responsibilities.

- **Warehouse (or plant)** – a warehouse is a specific location, dedicated to the storage and handling of goods; a warehouse is a specific location, often within or attached to a plant, dedicated to the storage and handling of goods.

After completing all steps described in this article, you will get a hierarchy similar to the following.

![hierarchy-warehouse.png]({{ "/assets/images/kb/how-to/hierarchy-warehouse.png" | relative_url }})

## Preparation

You need to have separate data sets representing specific entities in the organizational hierarchy. This means that you need to have 6 data sets: Business Group, Company, Legal Entity, Purchasing Organization, Sales Organization, and Warehouse. If you want to practice building organizational hierarchy, you can use the following files for training:

- <a href="../../../assets/other/business-group.json" download>business-group.json</a>

- <a href="../../../assets/other/company.json" download>company.json</a>

- <a href="../../../assets/other/legal-entity.json" download>legal-entity.json</a>

- <a href="../../../assets/other/purchasing-organization.json" download>purchasing-organization.json</a>

- <a href="../../../assets/other/sales-organization.json" download>sales-organization.json</a>

- <a href="../../../assets/other/warehouse.json" download>warehouse.json</a>

### Business Group data set

The Business Group data set consists of 2 columns: `business_group_id` and `business_group_name`. We mapped this data set to the Business Group business domain and the Training Business Group vocabulary.

![business-group-mapping.png]({{ "/assets/images/kb/how-to/business-group-mapping.png" | relative_url }})

After processing the data set, we have 1 golden record of the Business Group business domain.

![business-group-gr.png]({{ "/assets/images/kb/how-to/business-group-gr.png" | relative_url }})

### Company data set

The Company data set consists of 3 columns: `company_id`, `company_name`, and `business_group_id`. We mapped this data set to the Company business domain and the Training Company vocabulary. The `business_group_id` column is used to establish a relationship between a company and its corresponding business group. Therefore, we need to create an edge relation between the Company and Business Group golden records to represent this connection in the organizational hierarchy. For this purpose, we can use the `/CompanyOf` edge type.

![company-mapping.png]({{ "/assets/images/kb/how-to/company-mapping.png" | relative_url }})

After processing the data set, we have 2 golden records of the Company business domain.

![company-gr.png]({{ "/assets/images/kb/how-to/company-gr.png" | relative_url }})

### Legal Entity data set

The Legal Entity data set consists of 3 columns: `legal_entity_id`, `legal_entity_name`, and `company_id`. We mapped this data set to the Legal Entity business domain and the Training Legal Entity vocabulary. The `company_id` column is used to establish a relationship between a legal entity and its corresponding company. Therefore, we need to create an edge relation between the Legal Entity and Company golden records to represent this connection in the organizational hierarchy. For this purpose, we can use the `/LegalEntityOf` edge type.

![legal-entity-mapping.png]({{ "/assets/images/kb/how-to/legal-entity-mapping.png" | relative_url }})

After processing the data set, we have 2 golden records of the Legal Entity business domain.

![legal-entity-gr.png]({{ "/assets/images/kb/how-to/legal-entity-gr.png" | relative_url }})

### Purchasing Organization data set

The Purchasing Organization data set consists of 3 columns: `purchasing_organization_id`, `purchasing_organization_name`, and `legal_entity_id`. We mapped this data set to the Purchasing Organization business domain and the Training Purchasing Org vocabulary. The `legal_entity_id` column is used to establish a relationship between a purchasing organization and its corresponding legal entity. Therefore, we need to create an edge relation between the Purchasing Organization and Legal Entity golden records to represent this connection in the organizational hierarchy. For this purpose, we can use the `/PurchasingOrgOf` edge type.

![purchasing-org-mapping.png]({{ "/assets/images/kb/how-to/purchasing-org-mapping.png" | relative_url }})

After processing the data set, we have 2 golden records of the Purchasing Organization business domain.

![purchasing-org-gr.png]({{ "/assets/images/kb/how-to/purchasing-org-gr.png" | relative_url }})

### Sales Organization data set

The Sales Organization data set consists of 3 columns: `sales_organization_id`, `sales_organization_name`, and `legal_entity_id`. We mapped this data set to the Sales Organization business domain and the Training Sales Org vocabulary. The `legal_entity_id` column is used to establish a relationship between a sales organization and its corresponding legal entity. Therefore, we need to create an edge relation between the Sales Organization and Legal Entity golden records to represent this connection in the organizational hierarchy. For this purpose, we can use the `/SalesOrgOf` edge type.

![sales-org-mapping.png]({{ "/assets/images/kb/how-to/sales-org-mapping.png" | relative_url }})

After processing the data set, we have 2 golden records of the Sales Organization business domain.

![sales-org-gr.png]({{ "/assets/images/kb/how-to/sales-org-gr.png" | relative_url }})

### Warehouse data set

The Warehouse data set consists of 3 columns: `warehouse_id`, `warehouse_name`, and `sales_orgnization_id`. We mapped this data set to the Warehouse business domain and the Training Warehouse vocabulary. The `sales_orgnization_id` column is used to establish a relationship between a warehouse and its corresponding sales organization. Therefore, we need to create an edge relation between the Warehouse and Sales Organization golden records to represent this connection in the organizational hierarchy. For this purpose, we can use the `/WarehouseOf` edge type.

![warehouse-mapping.png]({{ "/assets/images/kb/how-to/warehouse-mapping.png" | relative_url }})

After processing the data set, we have 3 golden records of the Warehouse business domain.

![warehouse-gr.png]({{ "/assets/images/kb/how-to/warehouse-gr.png" | relative_url }})

### Preparation results

After preparing the data sets, you can view the relations between golden records—created using edges—on the **Relations** tab of a golden record. For example, the following screenshot shows how a company is related to its business group, as well as to the legal entities that are part of the company.

![preparation-results.png]({{ "/assets/images/kb/how-to/preparation-results.png" | relative_url }})

To view all organizational relations in one place, create a hierarchy.

## Hierarchy creation

The process of creating a hierarchy involves configuring a hierarchy project and loading entities of specific relation types.

### Hierarchy project configuration

Start by creating a hierarchy project. In the first step, you only need to provide the hierarchy name. You do not need to select the business domain because we will rely on the existing edge relations.

![create-hierarchy-general.png]({{ "/assets/images/kb/how-to/create-hierarchy-general.png" | relative_url }})

Since the relations between golden records already exist in the system, we can use them as the starting for building the hierarchy. We will build the hierarchy from top to bottom, starting with the relations between Business Group and Company. These relations are represented by the `/CompanyOf` relation type with the **Incoming** direction.

![create-hierarchy-config-1.png]({{ "/assets/images/kb/how-to/create-hierarchy-config-1.png" | relative_url }})

For the top-level hierarchy project configuration, we rely on the existing relations to **Automatically** identify top-level golden records. Regarding the hierarchy type configuration, we choose the **Single hierarchy project** option because there is only one top-level Business Group golden record.

![create-hierarchy-config-2.png]({{ "/assets/images/kb/how-to/create-hierarchy-config-2.png" | relative_url }})

As a result, the hierarchy project displays the relations between Business Group and its Companies. Next, we will explain how to load other entities of the organizational hierarchy to the project one by one.

![create-hierarchy-result.png]({{ "/assets/images/kb/how-to/create-hierarchy-result.png" | relative_url }})

### Building organizational hierarchy

To build organizational hierarchy, we recommend loading entities using the existing relations. Since we already have the relations between Business Group and its Companies, next we need to display the relations between Companies and their Legal Entities. To do this, load entities that have the `/LegalEntityOf` relation type with the **Incoming** direction.

![load-entities-legal-entity-of.png]({{ "/assets/images/kb/how-to/load-entities-legal-entity-of.png" | relative_url }})

As a result, the hierarchy is updated with the Legal Entity golden records.

![hierarchy-legal-entity.png]({{ "/assets/images/kb/how-to/hierarchy-legal-entity.png" | relative_url }})

Next, we need to display the relations between Legal Entities and their Purchasing Organizations. To do this, load entities that have the `/PurchasingOrgOf` relation type with the **Incoming** direction.

![load-entities-purchasing-org-of.png]({{ "/assets/images/kb/how-to/load-entities-purchasing-org-of.png" | relative_url }})

As a result, the hierarchy is updated with the Purchasing Organization golden records.

![hierarchy-purchasing-org.png]({{ "/assets/images/kb/how-to/hierarchy-purchasing-org.png" | relative_url }})

Next, we need to display the relations between Legal Entities and their Sales Organizations. To do this, load entities that have the `/SalesOrgOf` relation type with the **Incoming** direction.

![load-entities-sales-org-of.png]({{ "/assets/images/kb/how-to/load-entities-sales-org-of.png" | relative_url }})

As a result, the hierarchy is updated with the Sales Organization golden records.

![hierarchy-sales-org.png]({{ "/assets/images/kb/how-to/hierarchy-sales-org.png" | relative_url }})

Finally, we need to display the relations between Sales Organizations and their Warehouses. To do this, load entities that have the `/WarehouseOf` relation type with the **Incoming** direction.

![load-entities-warehouse-of.png]({{ "/assets/images/kb/how-to/load-entities-warehouse-of.png" | relative_url }})

As a result, the hierarchy is updated with the Warehouse golden records. This is the last level that we needed to add to the hierarchy, and now our hierarchy displays the relations between Business Group, Companies, Legal Entities, Procurement Organizations, Sales Organizations, and Warehouses.

![hierarchy-warehouse.png]({{ "/assets/images/kb/how-to/hierarchy-warehouse.png" | relative_url }})

### Hierarchy creation results

After creating a hierarchy, you need to save and publish it. As a result, you can view the hierarchy project on the **Hierarchies** tab of a golden record that is involved in the hierarchy. Additionally, the hierarchy relations are displayed on the **Relations** tab of a golden record.

To sum up, in this article, we demonstrated how to create an organizational hierarchy using the existing relations between organizational entities within the system. To automate the hierarchy-building process, it is essential to define edge relations during mapping. CluedIn uses these edge relations to efficiently build and manage the organizational hierarchy.