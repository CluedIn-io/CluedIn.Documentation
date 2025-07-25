---
layout: cluedin
nav_order: 6
parent: Playbooks
permalink: /playbooks/data-ingestion-playbook
has_children: true
title: Data ingestion playbook
---

| Audience | Time to read |
|--|--|
| Business User, Data Project Lead, Data Steward, Data Analyst, Data Architect, Data Engineer | 2 min |

**You are here in the data journey**

![data-ingestion-you-are-here.png]({{ "/assets/images/playbooks/data-ingestion-you-are-here.png" | relative_url }})

Data ingestion is the first step of your MDM project. In this playbook, you will learn how to organize your MDM project and communicate its complexities and associated risks to your managers and business stakeholders. By understanding these elements, you’ll be better equipped to:

- **Deliver value** by improving critical data and **demonstrate project progress** to stakeholders. Delivering value does not mean using all CluedIn features; it means having **one end-to-end data flow** running in CluedIn that has improved value.

- **Mitigate potential issues** and ensure project success.

The data ingestion process consists of several steps: data impact workshop, picking the right tool, ingesting, mapping, and processing.

![data-ingestion-process.png]({{ "/assets/images/playbooks/data-ingestion-process.png" | relative_url }})

Before diving into the process of ingesting data into CluedIn, we recommend that you get acquainted with the foundational principles outlined in this playbook. In our experience, we’ve observed that many data teams tend to jump directly into the implementation phase without fully understanding the specificity of CluedIn. Additionally, they often overlook the critical step of defining which data will have the most significant impact on their objectives. If you have a small data team (one or two people), you may opt for a lighter approach. However, we still recommend following the guidelines from this playbook to better structure your MDM project.

**Main data ingestion principle for your first use case**

If you have the opportunity, **focus on the critical data you have access to and start with a simple implementation**. Once completed, organize a demo for your stakeholders and then release it to your production environment.

**Why should you apply this principle?**

![data-ingestion-benefits.png]({{ "/assets/images/playbooks/data-ingestion-benefits.png" | relative_url }})

1.  **Improved data** – you have one end-to-end data flow that improves a portion of your critical data.

2.  **Available in production** – you went through your IT processes to deploy the production environment according to your organization policies. It means that from now on, it will only get easier.

3.  **Full cycle of data journey** – by delivering a fairly simple use case into production, you’ve completed one full cycle of your MDM project, which you’ll need to repeat every time.

**Where to start with data ingestion?** The first step of data ingestion is the data impact workshop. It is a collaborative session designed to help you identify your business domains, determine the data sources to ingest, and assess their criticality to your operations. Learn more in [Data impact workshop](/playbooks/data-ingestion-playbook/data-impact-workshop).
