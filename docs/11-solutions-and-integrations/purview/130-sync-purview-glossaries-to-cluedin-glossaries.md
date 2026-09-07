---
layout: cluedin
title: Sync Purview glossaries to CluedIn glossaries
parent: Microsoft Purview
grand_parent: Solutions & integrations
nav_order: 130
permalink: /solutions/purview/sync-purview-glossaries-to-cluedin-glossaries
content_type: how-to
redirect_from: ["/microsoft-integration/purview/sync-purview-glossaries-to-cluedin-glossaries"]
source_path: docs/180-microsoft-integration/purview/100-sync-purview-glossaries-to-cluedin-glossaries.md
last_modified: 2025-04-30
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to sync Purview glossaries to CluedIn glossaries.

## Preparation

This section contains the steps required to prepare for syncing glossaries from Purview to CluedIn glossary categories and terms.

### Preparation in Purview

Make sure you have the existing classic type glossaries that contain some terms. In the following screenshot, we have 2 glossaries: CluedIn and Data Synchronization.

![sync-purview-glossary-to-cluedin-glossary-existing.png]({{ "/assets/images/microsoft-integration/purview/sync-purview-glossary-to-cluedin-glossary-existing.png" | relative_url }})

### Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.
    
1. Turn on the toggle in **Sync Purview glossaries to CluedIn glossaries**.

    ![sync-purview-glossaries-to-cluedin-glossaries.png]({{ "/assets/images/microsoft-integration/purview/sync-purview-glossaries-to-cluedin-glossaries.png" | relative_url }})

1. Select **Save**.

## Feature demonstration

Once you enable synchronization of Purview glossaries to CluedIn glossaries, you will receive a notification when the glossary term is created in CluedIn.

![sync-purview-glossary-to-cluedin-glossary-notification.png]({{ "/assets/images/microsoft-integration/purview/sync-purview-glossary-to-cluedin-glossary-notification.png" | relative_url }})

**To find terms in CluedIn**

- On the navigation pane, go to **Management** > **Glossary**.

    On the terms page, you can find the categories (a) and terms (b). The category in CluedIn corresponds to the glossary in Purview.

    ![sync-purview-glossary-to-cluedin-glossary-terms-page.png]({{ "/assets/images/microsoft-integration/purview/sync-purview-glossary-to-cluedin-glossary-terms-page.png" | relative_url }})