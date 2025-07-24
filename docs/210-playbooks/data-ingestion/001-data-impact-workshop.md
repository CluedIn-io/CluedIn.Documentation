---
layout: cluedin
nav_order: 1
parent: Data ingestion playbook
grand_parent: Playbooks
permalink: {{ site.baseurl }}/playbooks/data-ingestion-playbook/data-impact-workshop
title: Data impact workshop
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

| Audience | Time to read |
|--|--|
| Business User, Data Project Lead, Data Steward, Data Analyst, Data Architect, Data Engineer | 8 min |

**You are here in the data journey**

![data-ingestion-you-are-here.png](../../assets/images/playbooks/data-ingestion-you-are-here.png)

This article outlines the importance of the data impact workshop as the first step of your data ingestion process.

![data-impact-workshop-intro.png](../../assets/images/playbooks/data-impact-workshop-intro.png)

The data impact workshop is a collaborative session designed to help you identify your business domains, determine the data sources to ingest, and assess their criticality to your operations.

{:.important}
If you have signed the statement of work (SOW) with CluedIn, the data impact workshop will be conducted by a CluedIn expert. If you haven't signed an SOW with CluedIn, use this playbook to conduct the data impact workshop on your own.

## Data selection principles

Data for an MDM project is typically characterized by ease of access, criticality, and completeness. In this section, we explore how these characteristics influence the data you select for your use cases and provide a recommended approach to demonstrate the value of your MDM project.

**Ease of access vs. Criticality**

We always advise you to strike a balance between the ease of access and the criticality of your data. If you want your MDM project to be successful, you will need it to operate on the data that is the most valuable to you. However, from time to time, the access to this data can be restricted or time-consuming as it requires multiple approval steps and buy-in from the business department before starting.

**Criticality vs. Completeness**

The main [data ingestion principle](/playbooks/data-ingestion-playbook) for your first use case is: "Focus on the critical data you have access to and start with a simple implementation". That is why we believe that is probably more important for you to demonstrate value on a sample of critical data rather than having a full solution on the sources that are deemed "nice to have". So, always favor criticality over completeness.

**Recommended approach**

At the start of your MDM project, use data that will showcase the full value of your MDM solution. Avoid focusing on “nice-to-have” use cases where you may have full access but struggle to gain business buy-in.

For a businessperson, seeing a full solution for 10,000 records is a strong proof of value. You can demonstrate the solution, gather feedback, and start preparing your next use cases. This approach aligns with agile methodology, allowing your team to work on new use cases with business stakeholders based on the feedback received, while simultaneously growing the number of records in the test and production environments.

## Data impact quadrant

The data impact quadrant is a tool that helps you visualize and assess data based on two key criteria: **impact** and **access to data**. The purpose of the data impact quadrant is to help you map your sources of data and your business domains in order to evaluate where you should spend your time first.

![data-impact-quadrant.png](../../assets/images/playbooks/data-impact-quadrant.png)

**What are the goals of your data impact quadrant?**

- **Understand where you can gain value with minimal effort within your organization.**

    While it can be challenging to access critical data, this approach will at least align your team with expectations and keep project stakeholders in the line of business (LOB) informed.

- **Understand what can and cannot be delivered at the start of the project.**

    We’ve often seen data teams face pressure due to misaligned expectations from the start. It’s not uncommon for people in the line of business (LOB) to have unrealistic timelines, especially when the data team hasn’t even received the necessary data to begin with. Therefore, it’s crucial to follow the workshop and **present workshop results to your stakeholders**. By doing so, you can communicate the criticality of your demands and the impact of any delays to your stakeholders.

- **Understand what blockers may arise for each source of data.**

    Create the risk assessment matrix that you can update over time and share with your business stakeholders. Sometimes, a good critical escalation call can unlock the majority of your needs that you were waiting to resolve for months. So, make sure to track the blockers on the source of data. An MDM project requires access to critical data, and you need to be clear that to deliver the value, you will need access to it.

**How can critical escalation lead to better project alignment?**

Early in the process, you may need to escalate critical issues. While this may not be a call you like to have, it is often necessary. We’ve seen data teams work on use cases that provided minimal value from the stakeholders’ perspective, leading to bigger problems down the line and even project cancellations. To avoid this, we encourage you to **raise your voice internally** and **maintain transparency with your stakeholders**. If they’re not on board, you may face negativity and high pressure later, having to change use cases or sources extremely fast due to misalignment between your work and stakeholder expectations.

We recommend providing at least a **monthly demo and status update** to ensure stakeholders in the line of business (LOB) are aware of the current situation, as well as the sources and tasks you’re working on.

## Data impact workshop scenario

Now that you understand the importance of the data impact quadrant, let’s explore how it works.

{:.important}
Follow [this link](https://miro.com/app/board/uXjVLDsv2ww=/?share_link_id=341736119087) to find a ready-to-use Miro board for conducting the data impact quadrant exercise with your team. Alternatively, you can use other tools to conduct exercise.

The following image illustrates the data impact quadrant created during a workshop.

![data-impact-quadrant-example.png](../../assets/images/playbooks/data-impact-quadrant-example.png)

Generally, the data impact workshop consists of 5 steps.

![data-impact-workshop-scenario.png](../../assets/images/playbooks/data-impact-workshop-scenario.png)

### Step 1: Identify critical data sources

The first step is to identify your data sources.

**What is critical data?**

To find out what your critical data is, answer the following questions: 

1.  If I remove this source, can my company operate without interruption?

    - If the answer is yes, this is not critical data.

    - If the answer is no, it may be critical data.

2.  If I remove this source, what monetary impacts would it have?

    - If I remove this source, the entire operation line is down. This would indicate that the source is critical.

    - If I remove this source, our sales team cannot sell any more. This would indicate that the source is critical.

    - If I remove this source, our support team cannot operate. This would indicate that the source might be critical.

We cannot really do this exercise for you, all we can do is to help you ask the right questions. However, if your MDM project does not involve critical data, be aware that you may need to put in extra effort to demonstrate its value to business stakeholders and management. While we cannot determine what your company deems critical, we can assist you in that process.

### Step 2: List data sources

The second step is to list each source with a brief description and assign a priority to each.

| Priority | Source | Description | Value for MDM |
| --|--|--|--|
| 1. | CRM | Hold all the information we have around our customers | Required normalization work as lots of manual work on reporting |
| 2. | ERP | Hold all the business domain important for our production | Disconnected from the CRM detail that should be hold the truth |
| 3. | ... | ... |  |

### Step 3: List business domains

The third step is to add business domains for each source. Keep in mind that there may be overlap.

| Priority | Domain | Source | Value for MDM |
| --|--|--|--|
| 1. | Customer | CRM | Represent who buys our services/products |
| 2. | Prospect | CRM | Represent a potential customer |
| 3. | Deals | CRM | Represent a deal that is signed or sent |
| 4. | Customer | ERP | Represent who will get our products |
| 5. | Product | ERP | Represent the product we are selling |
| 6. | Shipping Info | ERP | Represent the shipping contact for a given customer |

### Step 4: Put sources with domains on the quadrant

The fourth step is to place the sources along with domains on the quadrant. Each of your team members should place the sources along with business domains on the quadrant.

It’s important for your team to discuss and align on what they consider “critical” and what they perceive as hard or easy to access. One team member might have access you weren’t aware of, or you might have different perspectives on what defines critical data. Now is a good time to have those conversations and reach alignment.

### Step 5: Create a list with your priorities

Once you’ve reached an agreement, create a list of data sources, starting from the top right and moving to the bottom left, to establish your priorities. The following image shows the direction in which you should list the data sources.

![data-impact-quadrant-example-order.png](../../assets/images/playbooks/data-impact-quadrant-example-order.png)

The following table is an example of what the result of the exercise might look like.

| Priority | Domain | Source | Value for MDM |
| --|--|--|--|
| 1. | Customer | CRM | Represent who buys our services/products |
| 2. | Customer | ERP | Represent who will get our products |
| 3. | Shipping Info | ERP | Represent the shipping contact for a given customer |
| 4. | Product | ERP | Represent the product we are selling |
| 4. | Deals | CRM | Represent a deal that is signed or sent |
| 5. | Prospect | CRM | Represent a potential customer |

With this result, we know we need to work with _Customers_ and with the _ERP_ and the _CRM_ source first. We already have the start of a plan.