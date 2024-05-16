---
layout: cluedin
title: "Versioning and release schedule"
parent: Knowledge base
description: "Information on how CluedIn is versioning"
permalink: /kb/platform-versioning
tags: ["versioning", "platform"]
last_modified: 2022-05-09
nav_order: 8
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The CluedIn Platform consists of multiple services and databases that when deployed into
Kubernetes enable powerful eventual-connectivity and data fabric features to its users.

To support prompt delivery of patches, security fixes, and features, we are migrating
to a versioning scheme that will allow us to deliver changes as they are available
rather than waiting for a full platform release.

Date versioning
---------------

From June 30th, 2022, we will begin versioning with a date-based pattern. By using dates, we can better
communicate to our customers how up to date their instance of CluedIn is, as well as set expectations
over when the next release will be made available.

Our date-based version is broken into three parts: `Year`, `Month`, and `Update`.
+ The `Year` is always represented as a four-digit year (e.g. `2022`)
+ The `Month` is always represented as a two-digit month (e.g. `06` for June)
+ The `Update` is always represented as at least a two-digit number (e.g. `01` or `10`)

The parts of the version are then separated by `.` to supply the final version:
+ `2022.06.00` - This would be the first release in June 2022
+ `2022.06.01` - This would be the first `update` to the June 2022 release.
+ `2022.06.14` - This would be the fourteenth `update` to the June 2022 release.

Tools and integrations
----------------------

While the CluedIn Platform is easier to package and ship with date-based versioning, tools and integrations (e.g., Home, Helm, Crawlers etc) will continue to use [semantic versioning].

Each tool or integration is its own product so will release changes and updates as they are available.

Platform schedule
-----------------

As we adopt date-based versioning, we aim to offer a more regular cadence of updates to the platform.

### Breaking change release
A breaking change is a change in the platform that requires the customer to rebuild integrations, or invest a significant amount of time to deploy, due to changes in the platform code base or data stores.

These changes will only occur during a release where the `month` has changed. We will communicate our release schedule on our website, clearly marking when we expect to introduce breaking changes.

### Feature release
A feature release will only occur during a release where the `month` has changed. Feature releases will be communicated before development begins so customers can be made aware of what to expect in the next release.

Feature releases may require some upgrade steps that are unique to the release, but should not be as
impactful as a breaking change release.

### Update release
In the months following a release, issues that may arise from bugs or security patches will be supplied in an `update` release. We aim to deliver at least one update per month until the following feature or breaking change release.

### Hotfixes and early access
Occasionally we may make available releases that are in a stage of testing, or early access. This may
be to better support a high priority request from a customer, or for a customer to help us confirm an issue.

Platform historic versioning
----------------------------

Prior to date based versioning, the CluedIn Platform utilised a [semantic version] based scheme. This is an industry standard approach to versioning that we will keep for each of the services and tools that the platform
is built on. However, using semantic versioning for the platform itself means versioning all the services as the
same version. This proves difficult when a fix is needed in only one service as the version must cascade to all
other services, requiring increased build and test time.

[semantic version]: https://semver.org/
[semantic versioning]: https://semver.org/

