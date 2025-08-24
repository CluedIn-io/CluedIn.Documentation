---
layout: cluedin
title: Connect FiveTran to CluedIn
parent: Knowledge base
permalink: /kb/connect-to-fivetran
nav_order: 2
---

# Connecting Fivetran to CluedIn: A Complete Guide

This guide explains how to integrate **Fivetran** with **CluedIn** so that the data pipelines and transformations managed in Fivetran flow directly into CluedIn’s **data quality** and **master data management (MDM)** framework.

---

## Why Connect Fivetran to CluedIn?

- **Seamless Ingestion**: Automatically land data from SaaS, databases, and applications into CluedIn via your warehouse.  
- **Data Quality Monitoring**: Allow CluedIn to validate and score the data streamed by Fivetran.  
- **Master Data Governance**: Feed harmonized data into CluedIn golden records for entity resolution and survivorship rules.  
- **Operational Efficiency**: Use CluedIn’s alerts (Slack/Teams/Email) to monitor Fivetran pipelines and resulting data quality.

---

## Integration Architecture


- Fivetran extracts and loads data into a supported warehouse.  
- CluedIn connects to the same warehouse (via JDBC/ODBC) or consumes Fivetran outputs.  
- CluedIn applies enrichment, data quality rules, and master data processing.

---

## Prerequisites

- **Fivetran**: Active account with connectors configured to land data in your warehouse.  
- **CluedIn**: Access to ingestion pipelines and entity mappings.  
- **Warehouse**: Supported target (Snowflake, BigQuery, Redshift, Azure Synapse, SQL Server, etc.).  
- **Credentials**: Database/service accounts with read access for CluedIn.  

---

## Step 1 — Set Up Fivetran Connector

1. Log in to Fivetran dashboard.  
2. Choose a **source connector** (e.g., Salesforce, HubSpot, MySQL).  
3. Configure destination schema (e.g., `fivetran_salesforce`, `fivetran_hubspot`).  
4. Verify sync is active and data is landing in the warehouse.

---

## Step 2 — Prepare Data for CluedIn

- Align schema names and tables with business domains (e.g., `customer_raw`, `product_raw`).  
- Optionally use **Fivetran Transformations** (dbt integrated) to clean data before CluedIn ingestion.  
- Ensure consistent primary keys (`id`, `email`, `sku`) for CluedIn entity resolution.

---

## Step 3 — Connect CluedIn to the Warehouse

1. In CluedIn, go to **Data Sources → Add Connector**.  
2. Select your warehouse type (Snowflake, BigQuery, SQL Server, etc.).  
3. Enter JDBC/ODBC connection details:  
   - Host, Port, Database  
   - User & Password / Key  
   - Schema (e.g., `fivetran_salesforce`)  
4. Test the connection and save.

---

## Step 4 — Map Fivetran Tables to CluedIn Entities

- Example mapping:  
  - `fivetran_salesforce.accounts` → **Customer** entity  
  - `fivetran_hubspot.contacts` → **Lead/Customer** entity  
  - `fivetran_erp.products` → **Product** entity  

- Define **attributes** (columns) and link them to CluedIn’s schema.  
- Enable deduplication and survivorship rules.

---

## Step 5 — Automate Data Quality Monitoring

1. Create **CluedIn Data Quality rules**:  
   - Completeness (e.g., Customer Email required).  
   - Validity (e.g., VAT number format).  
   - Consistency (e.g., SKU in ERP matches SKU in CRM).  
2. Apply rules to ingested Fivetran tables.  
3. Enable **alerts** (Slack, Teams, Email) to monitor DQ scores in real time.

---

## Step 6 — Enable Master Data Workflows

- As Fivetran loads new/updated data, CluedIn:  
  - Merges records into golden entities.  
  - Resolves duplicates across systems.  
  - Applies survivorship rules (e.g., “email from CRM overrides ERP”).  
- Configure **downstream syncs** to push golden records back to target systems if needed.

---

## Step 7 — Automate via Scheduling

- **Fivetran** handles incremental syncs automatically.  
- **CluedIn** ingestion jobs can be scheduled to run after each Fivetran sync.  
- Optionally integrate via webhook/trigger: when Fivetran finishes sync, it triggers CluedIn ingestion.

---

## Best Practices

- **Schema Naming**: Keep Fivetran schemas clear (`fivetran_<source>`).  
- **Entity Alignment**: Decide early how sources map to CluedIn entities (Customer, Product, Supplier).  
- **Transform Before or After?**  
  - Use dbt/Fivetran transformations for light cleaning.  
  - Use CluedIn for entity resolution, survivorship, and golden records.  
- **Monitoring**: Configure Slack alerts for pipeline failures in Fivetran and DQ failures in CluedIn.  
- **Security**: Use vaults/secret stores for credentials, never hardcode them.  

---

## Troubleshooting

- **No data in CluedIn**: Check schema permissions and ensure warehouse sync is complete.  
- **Duplicate records**: Verify unique keys are consistent across Fivetran sources.  
- **DQ rules failing unexpectedly**: Inspect dbt/Fivetran transformations vs. CluedIn expectations.  
- **Slow ingestion**: Partition large tables or enable incremental loading.  

---

## Summary

By connecting **Fivetran** to **CluedIn**, you can:  
- Ingest data from hundreds of SaaS apps and databases.  
- Monitor and improve **data quality** across sources.  
- Build and maintain **golden records** through entity resolution and MDM.  
- Keep teams informed with real-time alerts when data quality or pipeline issues arise.  

This integration turns your Fivetran pipelines into a **governed, quality-assured data supply chain** managed inside CluedIn.
