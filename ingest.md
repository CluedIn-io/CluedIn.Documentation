---
title: Ingest
url: https://documentation.cluedin.net/ingest
content_type: landing
---

# Ingest

How do I get data into CluedIn?
  Data engineers and anyone connecting a source system.

Everything that brings records into CluedIn lives here: connecting a source, describing what you want to ingest, mapping source columns onto the model, and processing the result into golden records.

The usual order is **Data sources -> Mapping -> Processing**. Use [Troubleshoot ingestion](https://documentation.cluedin.net/ingest/troubleshooting.md) when records do not arrive or land in quarantine.

## In this section

- [Tutorial: ingest data](https://documentation.cluedin.net/ingest/tutorial-ingest-data.md) (tutorial): Ingesting data to CluedIn involves three basic steps: importing, mapping, and processing data.
- [Data sources](https://documentation.cluedin.net/ingest/data-sources.md): A data source is where records come from.
- [Mapping](https://documentation.cluedin.net/ingest/mapping.md): Mapping decides which source column becomes which vocabulary key, which value identifies the record, and what business domain it belongs to.
- [Processing](https://documentation.cluedin.net/ingest/processing.md): Processing turns mapped records into data parts and golden records.
- [Troubleshoot ingestion](https://documentation.cluedin.net/ingest/troubleshooting.md): When records do not arrive, or arrive wrong, these are the three places to look: the quarantine holds records that failed validation, the logs say what the source did, and monitoring shows whether processing is keeping up.
- [Manual data entry](https://documentation.cluedin.net/ingest/manual-data-entry.md): Some data has no source system - it lives in someone's head or a spreadsheet.
- [Connectors](https://documentation.cluedin.net/ingest/connectors.md): A connector crawls an external system and turns what it finds into clues.
- [Ingestion patterns](https://documentation.cluedin.net/ingest/patterns.md): Worked patterns for feeding CluedIn from common parts of a modern data stack, and for the case where you have many systems rather than a few.
