---
layout: cluedin
title: Connect DBT to CluedIn
parent: Knowledge base
permalink: /kb/dbt-to-cluedin
nav_order: 2
---

# Connecting dbt to CluedIn: A Step-by-Step Guide

This guide explains how to integrate **dbt (Data Build Tool)** with **CluedIn** so that the transformations, tests, and models in dbt flow seamlessly into CluedIn’s **data quality** and **master data management (MDM)** framework.

---

## Why Connect dbt to CluedIn?

- **Centralized Data Quality**: Push dbt test results into CluedIn to trigger alerts, dashboards, and Slack notifications.  
- **Metadata Enrichment**: CluedIn can ingest dbt lineage, schema, and model information for entity resolution and cataloging.  
- **Golden Records Context**: Enrich CluedIn golden records with dbt’s transformed data.  
- **Closed Feedback Loop**: Use CluedIn quality insights to inform dbt models, enabling proactive improvements.

---

## Integration Architecture


- dbt runs in your analytics stack (Snowflake, BigQuery, Redshift, etc.).  
- dbt artifacts (manifest.json, run_results.json, sources.json) are generated.  
- CluedIn ingests these artifacts or results via APIs, Connectors, or scheduled jobs.  

---

## Prerequisites

- **CluedIn**: Access to ingestion pipelines and APIs.  
- **dbt**: Installed and configured with your warehouse.  
- **Warehouse**: Supported by both dbt and CluedIn (e.g., Snowflake, BigQuery, SQL Server).  
- **Credentials**: Service accounts/tokens with read access to dbt artifacts and write access to CluedIn.  

---

## Methods of Integration

### 1. Ingest dbt Models into CluedIn

1. **Configure dbt models** to materialize into a schema that CluedIn can connect to.  
   Example in `dbt_project.yml`:
   ```yaml
   models:
     my_project:
       marts:
         schema: cluedin_ready
