---
title: Ingestion patterns
url: https://documentation.cluedin.net/ingest/patterns
content_type: landing
section: Ingest
---

# Ingestion patterns

Worked patterns for feeding CluedIn from common parts of a modern data stack, and for the case where you have many systems rather than a few.

## In this section

- [Connect Fivetran to CluedIn](https://documentation.cluedin.net/ingest/patterns/connect-to-fivetran.md) (how-to): This guide explains how to integrate Fivetran with CluedIn so that the data pipelines and transformations managed in Fivetran flow directly into CluedIn’s data quality and master data management (MDM) framework.
- [Connect DBT to CluedIn](https://documentation.cluedin.net/ingest/patterns/dbt-to-cluedin.md) (how-to): This guide explains how to integrate dbt (Data Build Tool) with CluedIn so that the transformations, tests, and models in dbt flow seamlessly into CluedIn’s data quality and master data management (MDM) framework.
- [Connect SnowFlake to CluedIn](https://documentation.cluedin.net/ingest/patterns/snowflake-to-cluedin.md) (how-to): This guide shows practical patterns for pushing data directly from Snowflake into CluedIn Ingestion Endpoints using either a Snowpark Python stored procedure (batch) or a Snowflake External Function (event/row-oriented).
- [Connect multiple data sources to CluedIn](https://documentation.cluedin.net/ingest/patterns/connect-lots-of-systems.md) (how-to): Integrating 100+ sources isn’t a modeling marathon you finish upfront—it’s an incremental journey you steer with evidence from the data itself.

Up: [Ingest](https://documentation.cluedin.net/ingest.md)
