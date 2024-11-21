---
layout: cluedin
nav_order: 6
parent: Additional operations
grand_parent: Integration
permalink: /integration/additional-operations-on-records/monitoring
title: Monitoring
tags: ["integration", "monitoring"]
last_modified: 2024-08-15
---

In this article, you will learn about the features on the **Monitoring** tab to gain insight into what is happening with your records and help you quickly identify issues.

## Monitoring for all types of data sources

Regardless of the type of data source, the **Monitoring** tab in the data set includes the following sections:

- **Total** – here you can view general information about the records, including the total number of records, original columns, mapped columns, and records in quarantine. This is a useful tool to compare the number of original columns and mapped columns.

- **Global queues** – here you can view global statistics on ingestion and processing requests from all data sets. This is a useful tool to ensure that the system runs correctly.

- **Queues** – here you can view messages containing records that are waiting to enter the next stage of their life cycle (loading, mapping, processing).

In the data set created using an endpoint, these sections are located in the **Overview** area.

If the number of messages of any type is greater than 0 while the number of consumers is 0, there may be an issue with your data. The following screenshot illustrates a situation where troubleshooting is needed to fix the processing of records.

![monitoring-1.png](../../assets/images/integration/additional-operations/monitoring-1.png)

To get better visibility into what is happening with your records, in addition to monitoring, use **system healthchecks**. You can find them in the upper-right corner of CluedIn.

![monitoring-3.png](../../assets/images/integration/additional-operations/monitoring-3.png)

If the status of any item is red or orange, it means that something is wrong and some services probably need to be restarted. To fix the problem, contact the person responsible for maintaining CluedIn for your organization (for example, system administrator) who can restart the needed service.

The following table provides descriptions of each message queue and corresponding troubleshooting guidelines. If the number of messages doesn't return to 0 or if the number of consumers remains 0, refer to the **Troubleshooting** column for recommended actions.

| Queue | Description | Troubleshooting |
|--|--|--|
| Ingestion data set | Messages representing JSON objects sent to various endpoints. | If you are a system administrator, restart the pod named "datasource-processing". |
| Commit data set | Messages representing requests for data set processing. Messages can be added by selecting the **Process** button on the **Process** tab of the data set or each time the endpoint receives data with the auto-submission enabled. | If you are a system administrator, restart the pod named "datasource-processing". |
| Submitting Messages | Messages containing JSON objects sent to the mapping service to be converted into records during processing. | Go to the **Process** tab and select **Cancel**. If you are a system administrator, verify the status of the mapping service and restart the pod named "annotation". |
| Processing Messages | Messages containing records sent to the processing pipeline. | If you are a system administrator, restart the pod named "submitter". |
| Quarantine Messages | Messages containing records that were approved on the **Quarantine** tab and sent to the processing pipeline. | If you are a system administrator, restart the pod named "submitter". |
| Loading Failures | Messages containing records from the data set that cannot be fully loaded. | Go to the **Preview** tab and select **Retry**. |
| Error Processing Messages | Messages containing records that could not be processed by the processing pipeline because it does not respond. | Go to the **Process** tab and select **Retry**. If you are a system administrator, verify the status of processing pods. |

## Monitoring for endpoints

In the data set created using an endpoint, the **Monitoring** tab includes two areas: **Overview** and **Ingestion reports**. The **Overview** area contains statistics described in the previous section. This section focuses on the **Ingestion reposts** area.

![monitoring-4.png](../../assets/images/integration/additional-operations/monitoring-4.png)

The **Ingestion reposts** area contains a table with detailed reports generated for each request sent to an endpoint. The table contains the following columns:

- **ReceiptID** – unique identifier of a request. Every request you send to an endpoint, whether successful or not, receives a unique receipt ID. This ID allows you to quickly locate the request report in CluedIn. Simply copy the receipt ID from the request response and paste it to the search field above the table.

- **Received** – the number of records received by CluedIn. If the number is 0, it means that the request contained errors and CluedIn rejected it.

- **Loaded** – the number of records loaded into CluedIn. This column contains three categories:

    - **Success** – the number of records that were successfully loaded into CluedIn.

    - **Failed** – the number of records that failed to load into CluedIn.

    - **Retry** – the number of records that attempted to reload into CluedIn.

- **Logs** – the number of logs generated for a specific request. You can view the log details by selecting the content of the cell. Keep in mind that for endpoints, we only log warnings. These logs are the same as those found on the **Logs** tab of the dataset. The difference is that the **Logs** tab contains logs for all requests, while the **Ingestion reports** table provides logs for each specific request. For more information on how to read logs, see the [Logs](/integration/additional-operations-on-records/logs documentation.

- **Processed** – the number of records that were processed in CluedIn.

- **Created at** – the timestamp indicating when the ingestion report was generated. This corresponds to the time when the HTTP request was executed.