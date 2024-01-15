---
layout: default
nav_order: 6
parent: Additional operations
grand_parent: Integration
permalink: /integration/additional-operations-on-records/monitoring
title: Monitoring
tags: ["integration", "monitoring"]
last_modified: 2023-11-07
---

Monitoring provides an overview of your records and helps you quickly identify issues. The **Monitoring** tab consists of two sections:

- **Total** – here you can view general information about the records, including the total number of records, original columns, mapped columns, and records in quarantine. This is a useful tool to compare the number of original columns and mapped columns.

- **Queues** – here you can view messages containing records that are waiting to enter the next stage of their life cycle (loading, mapping, processing).

**Important!**  If the number of messages of any type is greater than 0 while the number of consumers is 0, there may be an issue with your data. The following screenshot illustrates a situation where troubleshooting is needed to fix the processing of records.

![monitoring-1.png](../../assets/images/integration/additional-operations/monitoring-1.png)

To get better visibility into what is happening with your records, in addition to monitoring, use **system healthchecks**. You can find them by selecting ![monitoring-2.png](../../assets/images/integration/additional-operations/monitoring-2.png) in the upper-right corner of CluedIn. If the status of any item is red or orange, it means that something is wrong and some services probably need to be restarted. To fix the problem, contact the person responsible for maintaining CluedIn for your organization (for example, system administrator) who can restart the needed service.

![monitoring-3.png](../../assets/images/integration/additional-operations/monitoring-3.png)

The following table provides descriptions of each message queue and corresponding troubleshooting guidelines. If the number of messages doesn't return to 0 or if the number of consumers remains 0, refer to the **Troubleshooting** column for recommended actions.

| Queue | Description | Troubleshooting |
|--|--|--|
| Submitting Messages | Messages containing JSON objects sent to the mapping service to be converted into records during processing. | Go to the **Process** tab and select **Cancel**. If you are a system administrator, verify the status of the mapping service and restart the pod containing the name "annotation". |
| Processing Messages | Messages containing records sent to the processing pipeline. | If you are a system administrator, restart the pod containing the name "submitter". |
| Quarantine Messages | Messages containing records that were approved on the **Quarantine** tab and sent to the processing pipeline. | If you are a system administrator, restart the pod containing the name "submitter". |
| Loading Failures | Messages containing records from the data set that cannot be fully loaded. | Go to the **Preview** tab and select **Retry**. |
| Error Processing Messages | Messages containing records that could not be processed by the processing pipeline because it does not respond. | Go to the **Process** tab and select **Retry**. If you are a system administrator, verify the status of processing pods. |