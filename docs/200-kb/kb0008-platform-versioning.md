---
layout: cluedin
title: "Versioning and release schedule"
parent: Knowledge base
description: "Information on how CluedIn is versioning"
permalink: /kb/platform-versioning
tags: ["versioning", "platform"]
last_modified: 2022-05-09
nav_order: 8
published: false
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The CluedIn platform consists of multiple services and databases that when deployed into Kubernetes enable powerful eventual-connectivity and data fabric features to its users. To support prompt delivery of patches, security fixes, and features, we are migrating to a versioning scheme that will allow us to deliver changes as they are available rather than waiting for a full platform release.

## Date versioning

From June 30, 2022, we started using a date-based pattern for versioning. By using dates, we can better communicate to our customers how up to date their instance of CluedIn is, as well as set expectations over when the next release will be made available.

Our date-based version is broken into three parts: `Year`, `Month`, and `Update`.

- The `Year` is always represented as a four-digit year (e.g. `2022`).
- The `Month` is always represented as a two-digit month (e.g. `06` for June).
- The `Update` is always represented as at least a two-digit number (e.g. `01` or `10`).

The parts of the version are then separated by `.` to supply the final version:

- `2022.06.00` – this would be the first release in June 2022.
- `2022.06.01` – this would be the first `update` to the June 2022 release.
- `2022.06.14` – this would be the fourteenth `update` to the June 2022 release.

## Tools and integrations

While the CluedIn platform is easier to package and ship with date-based versioning, tools and integrations (e.g., Home, Helm, Crawlers etc) will continue to use [semantic versioning](https://semver.org/). Each tool or integration is its own product and will release changes and updates as they are available.

## Platform historic versioning

Prior to date-based versioning, the CluedIn platform uses a [semantic versioning](https://semver.org/) scheme. This is an industry standard approach to versioning that we will keep for each of the services and tools that the platform is built on. However, using semantic versioning for the platform itself means versioning all the services as the same version. This proves difficult when a fix is needed in only one service as the version must cascade to all other services, requiring increased build and test time.

