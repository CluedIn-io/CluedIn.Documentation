---
layout: cluedin
title: Upgrade
parent: PaaS operations
permalink: /paas-operations/upgrade
nav_order: 4
has_children: true
tags: ["deployment", "kubernetes", "azure", "aks", "microsoft", "marketplace", "azure-marketplace"]
headerIcon: "paas"
---

When signing up with CluedIn and taking on the Managed Services agreement, product upgrades will be handled for you by the CluedIn team. The team will reach out and work with your requirements to ensure that upgrades happen when it's most convenient for your business.

{:.important}
CluedIn team performs installation activities on all business days **except Friday**. Deploying on a Friday carries higher risk because issues may not surface immediately and can escalate into weekend incidents with fewer people available to respond. As a best practice, it is recommended to schedule installations earlier in the week (Tuesday–Thursday) to allow time for monitoring, troubleshooting, and stabilization.

For some customers, a more tailored agreement exists whereby the management of the cluster and resources are managed by you, including upgrades. This section contains guides for self-service upgrading of CluedIn.

For release note specifics, please visit [Release Notes](/release-notes).

## Managed Upgrade Process

If you use our Managed Services agreement, the following steps will be followed to ensure a smooth and secure process:

{:.important}
If a cluster has large amounts of data, times may vary during the upgrade process.

1. **Schedule the Upgrade Window**  
   - Determine and schedule an appropriate time for the upgrade to minimize impact on users. Notify relevant stakeholders about the planned downtime.

2. **Snapshot of Data Disks**  
   - Before the upgrade begins, take a snapshot of all data disks. This step ensures that the data is safeguarded and can be restored if needed.

3. **Backup Current Helm Values**  
   - Backup the current Helm values configuration. This allows us to revert to the previous state if the upgrade encounters any issues.

4. **Initiate Helm Upgrade**  
   - Start the Helm upgrade process. The expected downtime during this process is around **20 minutes**. We ensure that all systems are monitored during this step to catch any potential issues early.

5. **Cluster Ready for Use**  
   - Once the upgrade completes and the cluster is back online, send a notification to all relevant teams and stakeholders to inform them that the cluster is ready for use.

  ![Diagram]({{ "/assets/images/upgrade/upgrade-process-diagram.png" | relative_url }})
