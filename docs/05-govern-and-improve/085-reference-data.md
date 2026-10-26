---
layout: cluedin
title: Reference data
parent: Govern & improve
nav_order: 85
permalink: /govern/reference-data
content_type: concept
tags: ["governance", "reference data", "vocabulary keys", "data quality"]
last_modified: 2026-10-26
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Reference data is a known-good list of values - such as country codes or currency codes - that you can link to one or more [vocabulary keys](/model/vocabularies) to validate the values golden records actually hold against it. Once a vocabulary key is linked, CluedIn checks the records that use it against the reference list and flags the ones whose value is missing or doesn't match, so you can see and fix data quality issues at a glance.

With the **Reference Data** module, you can do the following:

- [Add a reference data set](#add-a-reference-data-set) from the built-in catalog, by uploading a file, or by generating one with AI.

- [Link a vocabulary key to a reference data set](#link-a-vocabulary-key-to-a-reference-data-set) to validate and monitor its values.

- [Monitor flagged records](#monitor-flagged-records) and review which golden records don't match the reference data.

{:.important}
This is a new module. "From Database" and "From Ingestion Point" are shown as menu options for parity with the design, but connecting a live database or ingestion point as a reference data source is not yet implemented - use **From Catalog** or **From Files** for now. Likewise, the **Fix with AI** button on the Monitoring tab is a placeholder for upcoming AI-assisted remediation.

## Add a reference data set

**To add a reference data set from the catalog**

1. On the navigation pane, go to **Governance** > **Reference Data**.

1. Select **Add Reference Data**, and then select **From Catalog**.

    ![The Reference Data page with the Add Reference Data dropdown open, showing From Files, From Database, From Ingestion Point, and From Catalog]({{ "/assets/images/governance/reference-data/add-reference-data/add-reference-data-menu.png" | relative_url }})

1. On the **Choose reference data** panel, expand a category, select the reference list you want to use, and then select **Use as reference**.

    The catalog's **Location & Geography** category currently ships with five ready-to-use lists: ISO 3166 country codes, ISO 4217 currency codes, IANA time zones, country dialing codes, and ISO 639 language codes. Other categories shown in the catalog (Business & Industry Classifications, Finance, Regulatory & Standards, Healthcare & Pharma, Product & Commerce Standards, Technology & IT Standards) are listed for parity with the design but marked **Coming soon** - their specific contents still need product owner sign-off.

    ![The Choose reference data panel with the Location & Geography category expanded and Country list (ISO 3166 codes) selected]({{ "/assets/images/governance/reference-data/add-reference-data/catalog-picker.png" | relative_url }})

    You are taken to the new reference data set's **Data** tab, which shows its rows (for example, every ISO 3166 country with its alpha-2, alpha-3, and numeric codes).

**To add a reference data set from a file**

1. On the navigation pane, go to **Governance** > **Reference Data**.

1. Select **Add Reference Data**, and then select **From Files**.

1. Enter a name and, optionally, a description, then upload a CSV file. The first row of the file is used as the column headers.

1. Select **Add**.

**To generate reference data with AI**

Use this when you want a real-world reference list - such as world currencies or country codes - but don't already have a file for it. Instead of creating a reference data set directly, this generates the data and loads it into a new [ingestion endpoint](/ingest/data-sources/endpoint) data set, which you then map yourself the normal way; once it's mapped and onboarded, come back and add a reference data set (from the catalog, a file, or the Rule Builder) using the resulting golden records.

1. On the navigation pane, go to **Governance** > **Reference Data**.

1. Select **Add Reference Data Set**.

1. Enter a name - it's used for both the new data set and, if you continue, the reference data set itself.

1. Under **Don't have the data yet?**, describe the reference data you want (for example, "world currencies with their code and symbol"), and then select **Generate with AI**.

    CluedIn asks AI to generate the data (for a well-known, enumerable set such as world currencies, every standard member is generated, up to 300 rows) and loads it into a new ingestion endpoint data set. When it's done, a link to the new data set appears.

1. Select **Open in Ingest** to go to the new data set, then [map it](/ingest/mapping) like any other ingested data.

{:.important}
Generating with AI only loads raw data into Ingest - it does not create a reference data set. After mapping and onboarding the generated data, add a reference data set that uses the resulting golden records as its reference values.

## Link a vocabulary key to a reference data set

Linking a vocabulary key to a reference data set is what turns a static list into an active data quality check: CluedIn starts validating the golden records that use that key against the reference data's values.

**To link a vocabulary key**

1. On a reference data set's page, select **Link Vocabulary Key**.

1. On the **Choose Vocabulary Keys** panel, select the vocabulary keys you want to validate against this reference data, then select **Next**.

    ![The Choose Vocabulary Keys panel with vocabulary keys grouped by entity type and several selected]({{ "/assets/images/governance/reference-data/link-vocabulary-key/choose-keys.png" | relative_url }})

1. Turn tracking on or off for the selected keys. Tracking enables background validation and is what makes the key's results appear on the **Monitoring** tab.

1. Select **Link & Reprocess**.

    CluedIn links the keys and runs an initial validation pass. When it's done, the keys appear on the **Linked vocabulary keys** tab with an **Active** (or **Paused**) tracking status.

    ![The Linked vocabulary keys tab showing linked keys with their source, classification, group, and tracking status]({{ "/assets/images/governance/reference-data/link-vocabulary-key/linked-keys-tab.png" | relative_url }})

## Monitor flagged records

Once a vocabulary key is linked with tracking enabled, the **Monitoring** tab shows how many golden records currently have a value that doesn't match the reference data, and lists those records.

**To review flagged records**

1. On a reference data set's page, go to the **Monitoring** tab.

1. Select the linked vocabulary key you want to review, if more than one is linked.

1. Review the **Number of records tagged** chart. It shows, for the selected date range, how many records were flagged on each day tracking ran.

1. Below the chart, review the list of flagged records - their name, business domain (entity type), and the value that didn't match the reference data.

    ![The Monitoring tab with a line chart of records tagged over time and a table of flagged records below it]({{ "/assets/images/governance/reference-data/monitoring/monitoring-tab.png" | relative_url }})

{:.important}
A validation pass checks up to the first 1,000 most-relevant golden records of the linked key's entity type, and reruns whenever you open the Monitoring tab or link a key - rather than on a recurring schedule against the organization's complete data set. For very large data sets, treat the flagged count as a strong sample, not an exact total.

## Remove a reference data set

**To remove a reference data set**

1. On the navigation pane, go to **Governance** > **Reference Data**.

1. Select the reference data set you want to remove.

1. Select **Remove Data Set**, and then confirm the removal.

    Removing a reference data set also removes its linked vocabulary keys and validation history. It does not change the golden records or vocabulary keys themselves.
