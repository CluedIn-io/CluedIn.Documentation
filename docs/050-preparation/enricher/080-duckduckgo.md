---
layout: cluedin
nav_order: 8
parent: Enricher
grand_parent: Preparation
permalink: preparation/enricher/duckduckgo
title: DuckDuckGo
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to configure the DuckDuckGo enricher. The purpose of this enricher is to get general information about the organization from the DuckDuckGo search engine. More details can be found in [Properties from DuckDuckGo enricher](#properties-from-duckduckgo-enricher).

The DuckDuckGo enricher supports the following endpoint:

- `https://api.duckduckgo.com`

## Add DuckDuckGo enricher

The enricher uses the organization name and/or the website to search for information in the DuckDuckGo engine.

**To add the DuckDuckGo enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **DuckDuckGo**, and then select **Next**.

    ![duck-duck-go-enricher-1.png](../../assets/images/preparation/enricher/duck-duck-go-enricher-1.png)

1. On the **Configure** tab, provide the following details:

    - **Accepted Business Domain** – enter the business domain to define which golden records will be enriched.

    - **Organization Name Vocabulary Key** – enter the vocabulary key that contains the names of companies that will be used for searching the DuckDuckGo engine.

    - **Website Vocabulary Key** – enter the vocabulary key that contains the websites of companies that will be used for searching the DuckDuckGo engine.

        ![duck-duck-go-enricher-2.png](../../assets/images/preparation/enricher/duck-duck-go-enricher-2.png)

1. Select **Test Connection** to make sure the enricher is properly configured, and then select **Add**.

    The DuckDuckGo enricher is added and has an active status. This means that it will enrich golden records based on the configuration details during processing or when you trigger external enrichment.

After the DuckDuckGo enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

- **Authentication** – modify the details you provided while configuring the enricher.

## Properties from DuckDuckGo enricher

You can find the properties added to golden records from the DuckDuckGo enricher on the **Properties** page.

![duck-duck-go-enricher-4.png](../../assets/images/preparation/enricher/duck-duck-go-enricher-4.png)

For a more detailed information about the changes made to a golden record by the DuckDuckGo enricher, check the corresponding data part on the **History** page.

![duck-duck-go-enricher-5.png](../../assets/images/preparation/enricher/duck-duck-go-enricher-5.png)

The following table lists the properties that can be added to golden records by the DuckDuckGo enricher.

| Display name | Vocabulary key |
|--|--|
| Abstract | duckDuckGo.organization.abstract  |
| Abstract Source | duckDuckGo.organization.abstractSource  |
| Abstract Text | duckDuckGo.organization.abstractText |
| Abstract Url | duckDuckGo.organization.abstractURL |
| Answer | duckDuckGo.organization.answer |
| Answer Type | duckDuckGo.organization.answerType |
| Definition | duckDuckGo.organization.definition |
| Definition Source | duckDuckGo.organization.definitionSource |
| Definition Url | duckDuckGo.organization.definitionURL |
| Employees | duckDuckGo.organization.employees |
| Entity | duckDuckGo.organization.entity |
| Facebook Profile | duckDuckGo.organization.facebookProfile |
| Founded | duckDuckGo.organization.founded |
| Git Hub Profile | duckDuckGo.organization.gitHubProfile |
| Heading | duckDuckGo.organization.heading |
| Image | duckDuckGo.organization.image |
| Image Height | duckDuckGo.organization.imageHeight |
| Image Is Logo | duckDuckGo.organization.imageIsLogo |
| Image Width | duckDuckGo.organization.imageWidth |
| Industry | duckDuckGo.organization.industry |
| Instagram Profile | duckDuckGo.organization.instagramProfile |
| Redirect | duckDuckGo.organization.redirect |
| Revenue | duckDuckGo.organization.revenue |
| Score | duckDuckGo.organization.score |
| Twitter Profile | duckDuckGo.organization.twitterProfile |
| Type | duckDuckGo.organization.type |
| Websites | duckDuckGo.organization.websites |
| Youtube Channel | duckDuckGo.organization.youtubeChannel |

Additionaly, the DuckDuckGo enricher can add various infobox properties (for example, Formerly Called, Founders, Products, and so on) and related topic properties (brief description with a link to the source). These properties depend on the information that the enricher can find.