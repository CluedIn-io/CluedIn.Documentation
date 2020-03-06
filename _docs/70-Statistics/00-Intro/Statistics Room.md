---
category: Statistics
title: Statistics Room Overview
---

---

It is often required to understand what is happening under the hood of CluedIn. It is not as important for Data Stewards and Business Users to know this, but very much more adminstrators or systems owners that are not necessarily aware of how to operate the sub systems.

A lot of this can be sourced from the many Administrator screens that come with CluedIn for the underlying systems. Due to complex security of infrastructure setups, many times you might find that you don’t have access to these systems, but would still like to see some metrics and progress statistics.

For this, we expose some underlying metrics and statistics around memory, disk and cpu and utilisation where possible. This will help you to understand if it might be necessary to increase the infrastructure of your CluedIn installation or potentially to dedicate more resources to a particular process. All values are read-only. For more advanced exploration, please use the underlying system adminstrator interfaces.

You can begin by having a closer look at our dashboards, overseeing the health and basic statistics of pipelines and the databases that our system uses to process and store your data, or you can query our Statistics API directly.

These are broken down in sections.

# Statistics Sections
1. [Statistics Room Overview](/docs/70-Statistics/00-Intro/Statistics%20Room.html)
2. [Processing Pipelines](/docs/70-Statistics/10-Pipelines/Pipelines.html)
3. [Graph Database](/docs/70-Statistics/20-Graph/Graph.html)
4. [Search Database](/docs/70-Statistics/30-Search/Search.html)
5. [Relational Database](/docs/70-Statistics/40-Relational/Relational.html)
6. [Cache Database](/docs/70-Statistics/50-Cache/Cache.html)
7. [Configuration](/docs/70-Statistics/60-Configuration/Configuration.html)

# Querying API for raw data

All the data points presented as cards, charts, and lists can be requested directly from our REST API. On each section's page you will find a section showing an example JSON API response for the statistics described, and possibly explanations on data structures, if the complexity requires it.

For all requests (we recommend Postman for testing), all you need to have is the "Authorization" header set to "Bearer {access_token}", where {access_token} is the token you get when logging in with your organization account. This will provide access to statistics that relate only to your organization's setup. 