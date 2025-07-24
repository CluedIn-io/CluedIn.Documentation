---
layout: cluedin
title: Data Retention
parent: Governance
nav_order: 080
has_children: false
permalink: {{ site.baseurl }}/governance/data-retention
tags: ["governance","data-retention"]
published: false
---

Data Retention allows CluedIn to set temporal based limits on how long we can retain certain data. Rules on retention will change per industry, country and use-case. Becasue of this, CluedIn supports a generic retention framework that allows a user to specify some rules, which will then, inturn, either archive, purge (or other) data from CluedIn. If you have chosen to implement the Mesh API queries for these mutation commands, then these will also be triggered. This means that CluedIn can support Retention policies in integrated systems as well. 

![Diagram](../assets/images/governance/intro-retention.png)  

There are two ways to setup retention periods in CluedIn. The first is to set a Rule or Graph QL query that matches the data you would like to periodically action. You will also set a retention period. 

![Diagram](../assets/images/governance/create-new-retention.png)  

When those periods are set to run, it will instruct CluedIn to queue all operations needed to complete the process and will ask the approriate owners to do the work in the Mesh Command Center. If you have not implemented the Mesh API for the source systems, the retention will simply notify you that you have a record in that system that needs to be manually actioned.

![Diagram](../assets/images/governance/retention-form.png)  

The other option is for setting retention on an individual record.