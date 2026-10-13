---
title: How to build an organizational hierarchy
url: https://documentation.cluedin.net/model/hierarchies/how-to-build-an-organizational-hierarchy
content_type: how-to
section: Model > Hierarchies
---

# How to build an organizational hierarchy

> how-to: Steps to accomplish one task.

_The terminology and user interface described in this article might be slightly different depending on your version of CluedIn, but the overall logic remains the same._

In this article, you will learn how to build an organizational hierarchy to reflect the relations of entities within an organization. We are going to build a hierarchy of the following entities:

- **Business Group** – the highest-level organizational unit, typically representing a major line of business or a holding structure. It may consist of multiple companies that operate under a shared strategic direction but may have separate operations, finances, and compliance structures.

- **Company** – a legal and financial entity that operates under the business group. It typically has its own set of books for accounting and is responsible for reporting taxes, profits, and losses.

- **Legal Entity** – an organization that has legal standing in the eyes of the law—it can enter contracts, own assets, and be held liable. In many contexts, it is synonymous with a company, but some companies may contain multiple legal entities for operational, tax, or regulatory reasons.

- **Purchasing Organization** – responsible for procurement activities—purchasing goods and services, negotiating terms with vendors, and managing supplier relationships.

- **Sales Organization** – responsible for the sale and distribution of products or services. It defines the selling structure within a company or legal entity, including sales regions, channels, and responsibilities.

- **Warehouse (or plant)** – a warehouse is a specific location, dedicated to the storage and handling of goods; a warehouse is a specific location, often within or attached to a plant, dedicated to the storage and handling of goods.

After completing all steps described in this article, you will get a hierarchy similar to the following.

![Finished organizational hierarchy: business group ABC Retail Corp over two companies; ABC Fashion Co. over two legal entities; these over purchasing and sales organizations; ABC Retail Stores over three warehouses](https://documentation.cluedin.net/assets/images/kb/how-to/hierarchy-warehouse.png)

## Preparation

You need to have separate data sets representing specific entities in the organizational hierarchy. This means that you need to have 6 data sets: Business Group, Company, Legal Entity, Purchasing Organization, Sales Organization, and Warehouse. If you want to practice building organizational hierarchy, you can use the following files for training:

- [business-group.json](https://documentation.cluedin.net/assets/other/business-group.json)

- [company.json](https://documentation.cluedin.net/assets/other/company.json)

- [legal-entity.json](https://documentation.cluedin.net/assets/other/legal-entity.json)

- [purchasing-organization.json](https://documentation.cluedin.net/assets/other/purchasing-organization.json)

- [sales-organization.json](https://documentation.cluedin.net/assets/other/sales-organization.json)

- [warehouse.json](https://documentation.cluedin.net/assets/other/warehouse.json)

### Business Group data set

The Business Group data set consists of 2 columns: `business_group_id` and `business_group_name`. We mapped this data set to the Business Group business domain and the Training Business Group vocabulary.

![Mapping of business-group.json columns business_group_id and business_group_name to the Business Group business domain and Training Business Group vocabulary keys](https://documentation.cluedin.net/assets/images/kb/how-to/business-group-mapping.png)

After processing the data set, we have 1 golden record of the Business Group business domain.

![One golden record, ABC Retail Corp, of the Business Group business domain](https://documentation.cluedin.net/assets/images/kb/how-to/business-group-gr.png)

### Company data set

The Company data set consists of 3 columns: `company_id`, `company_name`, and `business_group_id`. We mapped this data set to the Company business domain and the Training Company vocabulary. The `business_group_id` column is used to establish a relationship between a company and its corresponding business group. Therefore, we need to create an edge relation between the Company and Business Group golden records to represent this connection in the organizational hierarchy. For this purpose, we can use the `/CompanyOf` edge type.

![Mapping of company.json columns company_id, company_name, and business_group_id to the Group Company business domain, with business_group_id creating 1 edge](https://documentation.cluedin.net/assets/images/kb/how-to/company-mapping.png)

After processing the data set, we have 2 golden records of the Company business domain.

![Two golden records of the Group Company business domain: ABC Fashion Co. and XYZ Home and Tech Co.](https://documentation.cluedin.net/assets/images/kb/how-to/company-gr.png)

### Legal Entity data set

The Legal Entity data set consists of 3 columns: `legal_entity_id`, `legal_entity_name`, and `company_id`. We mapped this data set to the Legal Entity business domain and the Training Legal Entity vocabulary. The `company_id` column is used to establish a relationship between a legal entity and its corresponding company. Therefore, we need to create an edge relation between the Legal Entity and Company golden records to represent this connection in the organizational hierarchy. For this purpose, we can use the `/LegalEntityOf` edge type.

![Mapping of legal-entity.json columns legal_entity_id, legal_entity_name, and company_id to the Legal Entity business domain, with company_id creating 1 edge](https://documentation.cluedin.net/assets/images/kb/how-to/legal-entity-mapping.png)

After processing the data set, we have 2 golden records of the Legal Entity business domain.

![Two golden records of the Legal Entity business domain: Fashion E-Commerce Ltd. and Fashion Retail Ltd.](https://documentation.cluedin.net/assets/images/kb/how-to/legal-entity-gr.png)

### Purchasing Organization data set

The Purchasing Organization data set consists of 3 columns: `purchasing_organization_id`, `purchasing_organization_name`, and `legal_entity_id`. We mapped this data set to the Purchasing Organization business domain and the Training Purchasing Org vocabulary. The `legal_entity_id` column is used to establish a relationship between a purchasing organization and its corresponding legal entity. Therefore, we need to create an edge relation between the Purchasing Organization and Legal Entity golden records to represent this connection in the organizational hierarchy. For this purpose, we can use the `/PurchasingOrgOf` edge type.

![Mapping of purchasing-organization.json columns to the Purchasing Organization business domain, with legal_entity_id creating 1 edge](https://documentation.cluedin.net/assets/images/kb/how-to/purchasing-org-mapping.png)

After processing the data set, we have 2 golden records of the Purchasing Organization business domain.

![Two golden records of the Purchasing Organization business domain: Central Procurement and Fashion Division Procurement](https://documentation.cluedin.net/assets/images/kb/how-to/purchasing-org-gr.png)

### Sales Organization data set

The Sales Organization data set consists of 3 columns: `sales_organization_id`, `sales_organization_name`, and `legal_entity_id`. We mapped this data set to the Sales Organization business domain and the Training Sales Org vocabulary. The `legal_entity_id` column is used to establish a relationship between a sales organization and its corresponding legal entity. Therefore, we need to create an edge relation between the Sales Organization and Legal Entity golden records to represent this connection in the organizational hierarchy. For this purpose, we can use the `/SalesOrgOf` edge type.

![Mapping of sales-organization.json columns to the Sales Organization business domain, with legal_entity_id creating 1 edge](https://documentation.cluedin.net/assets/images/kb/how-to/sales-org-mapping.png)

After processing the data set, we have 2 golden records of the Sales Organization business domain.

![Two golden records of the Sales Organization business domain: ABC Online Sales Division and ABC Retail Stores](https://documentation.cluedin.net/assets/images/kb/how-to/sales-org-gr.png)

### Warehouse data set

The Warehouse data set consists of 3 columns: `warehouse_id`, `warehouse_name`, and `sales_orgnization_id`. We mapped this data set to the Warehouse business domain and the Training Warehouse vocabulary. The `sales_orgnization_id` column is used to establish a relationship between a warehouse and its corresponding sales organization. Therefore, we need to create an edge relation between the Warehouse and Sales Organization golden records to represent this connection in the organizational hierarchy. For this purpose, we can use the `/WarehouseOf` edge type.

![Mapping of warehouse.json columns warehouse_id, warehouse_name, and sales_organization_id to the Warehouse business domain, with sales_organization_id creating 1 edge](https://documentation.cluedin.net/assets/images/kb/how-to/warehouse-mapping.png)

After processing the data set, we have 3 golden records of the Warehouse business domain.

![Three golden records of the Warehouse business domain: Distribution Center West, Apparel Fulfillment Hub, and Distribution Center East](https://documentation.cluedin.net/assets/images/kb/how-to/warehouse-gr.png)

### Preparation results

After preparing the data sets, you can view the relations between golden records—created using edges—on the **Relations** tab of a golden record. For example, the following screenshot shows how a company is related to its business group, as well as to the legal entities that are part of the company.

![Relations tab of the ABC Fashion Co. golden record, linked to its business group ABC Retail Corp and to the legal entities Fashion Retail Ltd. and Fashion E-Commerce Ltd.](https://documentation.cluedin.net/assets/images/kb/how-to/preparation-results.png)

To view all organizational relations in one place, create a hierarchy.

## Hierarchy creation

The process of creating a hierarchy involves configuring a hierarchy project and loading entities of specific relation types.

### Hierarchy project configuration

1. Start by creating a hierarchy project. In the first step, you only need to provide the hierarchy name. You do not need to select the business domain because we will rely on the existing edge relations.

    ![Create Hierarchy dialog on the General step, with Name set to Org Hierarchy and Business domain left empty](https://documentation.cluedin.net/assets/images/kb/how-to/create-hierarchy-general.png)

1. Since the relations between golden records already exist in the system, we can use them as the starting for building the hierarchy. We will build the hierarchy from top to bottom, starting with the relations between Business Group and Company. These relations are represented by the `/CompanyOf` relation type with the **Incoming** direction.

    ![Hierarchy configuration step with From existing relations selected, Relation type /CompanyOf, and Edge direction Incoming](https://documentation.cluedin.net/assets/images/kb/how-to/create-hierarchy-config-1.png)

1. For the top-level hierarchy project configuration, we rely on the existing relations to **Automatically** identify top-level golden records. Regarding the hierarchy type configuration, we choose the **Single hierarchy project** option because there is only one top-level Business Group golden record.

    ![Top level configuration set to Automatically, and Single hierarchy project - multiple top-level golden records selected](https://documentation.cluedin.net/assets/images/kb/how-to/create-hierarchy-config-2.png)

    As a result, the hierarchy project displays the relations between Business Group and its Companies. Next, we will explain how to load other entities of the organizational hierarchy to the project one by one.

    ![Hierarchy showing ABC Retail Corp with its two companies, XYZ Home and Tech Co. and ABC Fashion Co.](https://documentation.cluedin.net/assets/images/kb/how-to/create-hierarchy-result.png)

### Building organizational hierarchy

1. To build organizational hierarchy, we recommend loading entities using the existing relations. Since we already have the relations between Business Group and its Companies, next we need to display the relations between Companies and their Legal Entities. To do this, load entities that have the `/LegalEntityOf` relation type with the **Incoming** direction.

    ![Load Entities pane with Relation type /LegalEntityOf and Edge direction Incoming, previewing Fashion E-Commerce Ltd. and Fashion Retail Ltd.](https://documentation.cluedin.net/assets/images/kb/how-to/load-entities-legal-entity-of.png)

    As a result, the hierarchy is updated with the Legal Entity golden records.

    ![Hierarchy with the two legal entities, Fashion E-Commerce Ltd. and Fashion Retail Ltd., added under ABC Fashion Co.](https://documentation.cluedin.net/assets/images/kb/how-to/hierarchy-legal-entity.png)

1. Next, we need to display the relations between Legal Entities and their Purchasing Organizations. To do this, load entities that have the `/PurchasingOrgOf` relation type with the **Incoming** direction.

    ![Load Entities pane with Relation type /PurchasingOrgOf and Edge direction Incoming, previewing Central Procurement and Fashion Division Procurement](https://documentation.cluedin.net/assets/images/kb/how-to/load-entities-purchasing-org-of.png)

    As a result, the hierarchy is updated with the Purchasing Organization golden records.

    ![Hierarchy with a purchasing organization added under each legal entity: Fashion Division Procurement and Central Procurement](https://documentation.cluedin.net/assets/images/kb/how-to/hierarchy-purchasing-org.png)

1. Next, we need to display the relations between Legal Entities and their Sales Organizations. To do this, load entities that have the `/SalesOrgOf` relation type with the **Incoming** direction.

    ![Load Entities pane with Relation type /SalesOrgOf and Edge direction Incoming, previewing ABC Online Sales Division and ABC Retail Stores](https://documentation.cluedin.net/assets/images/kb/how-to/load-entities-sales-org-of.png)

    As a result, the hierarchy is updated with the Sales Organization golden records.

    ![Hierarchy with the sales organizations ABC Online Sales Division and ABC Retail Stores added under Fashion Retail Ltd.](https://documentation.cluedin.net/assets/images/kb/how-to/hierarchy-sales-org.png)

1. Finally, we need to display the relations between Sales Organizations and their Warehouses. To do this, load entities that have the `/WarehouseOf` relation type with the **Incoming** direction.

    ![Load Entities pane with Relation type /WarehouseOf and Edge direction Incoming, previewing three warehouses](https://documentation.cluedin.net/assets/images/kb/how-to/load-entities-warehouse-of.png)

    As a result, the hierarchy is updated with the Warehouse golden records. This is the last level that we needed to add to the hierarchy, and now our hierarchy displays the relations between Business Group, Companies, Legal Entities, Procurement Organizations, Sales Organizations, and Warehouses.

    ![Complete hierarchy with three warehouses, Distribution Center West, Distribution Center East, and Apparel Fulfillment Hub, under ABC Retail Stores](https://documentation.cluedin.net/assets/images/kb/how-to/hierarchy-warehouse.png)

### Hierarchy creation results

After creating a hierarchy, you need to save and publish it. As a result, you can view the hierarchy project on the **Hierarchies** tab of a golden record that is involved in the hierarchy. Additionally, the hierarchy relations are displayed on the **Relations** tab of a golden record.

To sum up, in this article, we demonstrated how to create an organizational hierarchy using the existing relations between organizational entities within the system. To automate the hierarchy-building process, it is essential to define edge relations during mapping. CluedIn uses these edge relations to efficiently build and manage the organizational hierarchy.

Up: [Hierarchies](https://documentation.cluedin.net/model/hierarchies.md)
