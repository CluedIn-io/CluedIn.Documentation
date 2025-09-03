---
layout: cluedin
title: Release overview
nav_order: 130
has_children: true
permalink: /release-notes
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will find links to release notes and learn about our release process and product versioning.

## Release notes

This section includes links to release notes for the CluedIn platform as well as links to the releases of additional resources.

### Latest release

| Version | Technical version | Release notes |
|--|--|--|
| 2025.05.02 | 4.5.2 | [View release notes](https://cluedin-io.github.io/Releases/2025.05/2025.05.02) |
| 2025.05.01 | 4.5.1 | [View release notes](https://cluedin-io.github.io/Releases/2025.05/2025.05.01) |
| 2025.05.00 | 4.5.0 | [View release notes](https://cluedin-io.github.io/Releases/2025.05/2025.05.00) |

### Previous releases

| Version | Technical version | Release notes |
|--|--|--|
| 2024.12.02 | 4.4.2 | [View release notes](https://cluedin-io.github.io/Releases/2024.12/2024.12.02) |
| 2024.12.01 | 4.4.1 | [View release notes](https://cluedin-io.github.io/Releases/2024.12/2024.12.01) |
| 2024.12 | 4.4.0 | [View release notes](https://cluedin-io.github.io/Releases/2024.12/2024.12.00) |
| 2024.07 | 4.3 | [View release notes](https://cluedin-io.github.io/Releases/2024.07/2024.07.00) |
| 2024.04 | 4.3.0 | [View release notes](https://cluedin-io.github.io/Releases/2024.04/2024.04.00) |
| 2024.03 | 4.1.0 | [View release notes](https://cluedin-io.github.io/Releases/2024.03/2024.03.00) |
| 2024.01 | 4.0.0 | [View release notes](https://cluedin-io.github.io/Releases/2024.01/2024.01.00) |
| 2023.07 |  | [View release notes](https://cluedin-io.github.io/Releases/2023.07/2023.07.02) |
| 2023.04 |  | [View release notes](https://cluedin-io.github.io/Releases/2023.04/2023.04.01) |
| 2022.10 |  | [View release notes](https://cluedin-io.github.io/Releases/2022.10/2022.10.00) |
| 2022.06 |  | [View release notes](https://cluedin-io.github.io/Releases/2022.06/2022.06.00) |
| 3.3 |  | [View release notes](https://cluedin-io.github.io/Releases/3.3/3.3.2) |
| 3.2 |  | [View release notes](https://cluedin-io.github.io/Releases/3.2/3.2.5) |

### Releases of additional resources

| Resource | Description | Release |
|--|--|--|
| Home repo | Contains resources for the local installation of CluedIn. | [View releases](https://github.com/CluedIn-io/Home/releases) |
| Charts repo | Contains installation scripts to install CluedIn in Kubernetes. | [View releases](https://github.com/CluedIn-io/Charts/releases) |
| Integrations releases | Contains releases of installation packages for enrichers and connectors. | [View releases](https://cluedin-io.github.io/Releases/integrations) |

## Release plan for 2025

The following table outlines the features, updates, and UX improvements we plan to implement between September 2025 and September 2026.

![roadmap-Q3-2025.png]({{ "/assets/images/release/roadmap-Q3-2025.png" | relative_url }})

## Release process

In this section, you will learn about our release process and the versioning of product releases. You'll gain an understanding of the stages that CluedIn features go through before becoming generally available, as well as get to know the versioning scheme that we use to deliver changes.

### Release stages
 
In order to prepare new and requested features, enhancements, and fixes, we follow a 6-stage release process. What is more, we are often in multiple release stages simultaneously across several releases. This approach allows us to efficiently prioritize tasks and ensure that features are released in a timely manner. By overlapping stages, we can quickly adapt to changing requirements and deliver continuous improvements. 

![release-stages-1.png]({{ "/assets/images/release/release-stages-1.png" | relative_url }})

The following table describes each stage of the release process.

| Release stage | Description |
|--|--|
| Pre-Planning | This stage is dedicated to the ongoing grooming exercise to keep our backlog up to date.<br>On conclusion of the Planning stage for a given release, we enter the Pre-Planning stage for the subsequent release. The Pre-Planning stage begins with identification of the new top 20 features and improvements and refinement efforts towards them. |
| Planning | During this stage, we assess our groomed backlog items and upcoming customer deadlines. As a result, we create a release manifest detailing expectations and timelines for a given release. |
| Development | This stage is dedicated to active development. This is where the engineering team brings the customer's ideas to life. It is important for us to stay in communication during this phase to ensure that we are building functionality that brings value to the customer. |
| Beta | This is the first testable version of the release. This is the step where we start regression testing. While this version is available in ACR for customer use, it is not recommended to give access to it without specific relationship management. We recommend using the Beta to demo the functionality and gather feedback.<br>Beta cannot be used in production or with real data. |
| Release Candidate | This is a stable version of the release, with potential for a few outstanding minor issues. We open the Release Candidate for testing by our internal teams and selected customers. If a customer needs specific functionality early, this is the recommended point at which they are upgraded.<br>Even though Release Candidate is a production-ready version of the release, the release assets are not yet ready. |
| Public Availability | This is when our release becomes generally available to customers. The release can be classified as major or minor; this classification affects whether a customer should upgrade. SaaS customers are always on the latest Public Availability release. |

### Product release versioning

To support prompt delivery of patches, security fixes, and features, we use a versioning scheme that allows us to deliver changes as they are available rather than waiting for a full platform release. Starting from June 30, 2022, we started using a date-based pattern for versioning. By using dates, we can better communicate to our customers how up to date their instance of CluedIn is.

Our date-based version is divided into three parts: `Year`, `Month`, and `Update`.

- The `Year` is always represented as a four-digit year (e.g. `2024`).
- The `Month` is always represented as a two-digit month (e.g. `10` for October).
- The `Update` is always represented as at least a two-digit number (e.g. `01` or `10`).

The parts of the version are then separated by `.` to supply the final version:

- `2024.10.00` – this would be the first release in October 2024.
- `2024.10.01` – this would be the first `update` to the October 2024 release.
- `2024.10.14` – this would be the fourteenth `update` to the October 2024 release.

{:.important}
Prior to date-based versioning, the CluedIn platform used a [semantic versioning](https://semver.org/) scheme. This is an industry standard approach to versioning that we will keep for each of the services and tools that the platform is built on (e.g., Home, Helm, Crawlers, and so on). Each tool or service is its own product and will release changes and updates as they become available.
