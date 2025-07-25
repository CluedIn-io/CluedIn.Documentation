---
layout: cluedin
title: Ingestion
nav_order: 60
has_children: true
permalink: integration
---

{: .fs-6 .fw-300 }

In the **Ingestion** module, you can upload your data into CluedIn, map it to standard fields, and process is to turn your data into golden records.

<div class="card-line">
  <div class="card" href="/integration/data sources">
    <div class="icon"><img src='{{ "/assets/icons/data-sources.svg" | relative_url }}' alt="data sources"/></div>
    <div class="title">Data sources</div>
    <div class="content">Get your data from external sources into CluedIn</div>
  </div>
   <div class="card" href="/integration/additional-operations-on-records">
    <div class="icon"><img src='{{ "/assets/icons/additional-operations.svg" | relative_url }}' alt="additional operations"/></div>
    <div class="title">Operations</div>
    <div class="content">Improve the quality of incoming data</div>
  </div>
   <div class="card" href="/integration/crawlers-and-enrichers">
    <div class="icon"><img src='{{ "/assets/icons/crawlers.svg" | relative_url }}' alt="crawlers"/></div>
    <div class="title">Crawlers</div>
    <div class="content">Build robust integrations and crawlers</div>
  </div>
</div>

When you open the **Ingestion** module, the first thing you see is the dashboard that can simplify and streamline your work with data sources and source records.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1071070771?h=4777b31837&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Ingestion dashboard in CluedIn"></iframe>
</div>

The dashboard is a place where you can start the process of uploading the data into CluedIn as well as find general statistics about your data sources. It consists of three main sections.

**Source actions**

At the top of the dashboard, you can find the actions to upload the data into CluedIn from a [file](/integration/file), an [ingestion endpoint](/integration/endpoint), and a [database](/integration/database). Additionally, you can add a [manual data entry](/integration/manual-data-entry) project and navigate to the list of installed crawlers. Each action card contains a number that indicates the count of data sources of a particular type that are currently in CluedIn. Selecting the number in the file, ingestion endpoint, or database action card will take you to the **Sources** page with data sources filtered by a specific type. To view the list of manual data entry projects, select the number in the corresponding action card.

**Data set records pending review**

This table allows you to track the number of records per data set that are in [quarantine](/integration/additional-operations-on-records/quarantine) or [require approval](/integration/additional-operations-on-records/approval). The table includes up to 20 latest sources, regardless of the owner. However, even if the table displays less than 20 sources, there might be additional sources requiring review. This is because after approving a specific source, only sources that were added later than the approved source will appear in the table.

To view the records that are currently in quarantine, select the corresponding number in the **Quarantine** column. Similarly, to view the records that require approval, select the corresponding number in the **Requires approval** column. If you are not the owner of the data source, you cannot approve or reject the records on the **Quarantine** or **Approval** tabs of the data set.

If you want to track records in data sources where you are the owner, go to **Home** > **My tasks**. You will see a similar table with the number of records per data set that are in quarantine or require approval. Each item in the table comes from a data source where you are the owner, so you can go ahead and review the records.

**Manual data entry project records pending review**

This table allows you to track the number of records per manual data entry project that [require approval](/integration/additional-operations-on-records/approval). The table includes up to 20 latest projects, regardless of the owner. However, even if the table displays less than 20 projects, there might be additional projects requiring review. This is because after approving records from a specific manual data entry project, only projects that were added later than the approved project will appear in the table.

To view the records that require approval, select the corresponding number in the **Requires approval** column. If you are not the owner of the manual data entry project, you cannot approve or reject the records on the **Approval** tabs of the project.

If you want to track records in manual data entry projects where you are the owner, go to **Home** > **My tasks**. You will see a similar table with the number of records per manual data entry project that require approval. Since you are the owner of each project in the table, you can go ahead and review the records.