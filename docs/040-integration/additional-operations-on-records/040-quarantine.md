---
layout: cluedin
nav_order: 4
parent: Additional operations
grand_parent: Ingestion
permalink: {{ site.baseurl }}/integration/additional-operations-on-records/quarantine
title: Quarantine
tags: ["integration", "quarantine"]
last_modified: 2024-10-31
---

Quarantine is an area in CluedIn where records that do not meet certain conditions are sent during processing. These conditions are usually set in [pre-process rules](/integration/additional-operations-on-records/preprocess-rules) or [property rules](/integration/additional-operations-on-records/property-rules). In this article, you will learn how to manage quarantined records.

**Why is the record in quarantine?** To find out why the record is in quarantine, select the **View details** icon in the **Details** column. The **Reason** pane will display the rule that led to the record's quarantine. The value that led to the record's quarantine is marked with the information icon.

![quarantine-1.png](../../assets/images/integration/additional-operations/quarantine-1.png)

**What happens to the record after it has been fixed and processed?** The record disappears from the quarantine table. On the **Process** tab of the data set, you will find a new entry including the number of records and the processing status. However, keep in mind that the record remains in its original state on the **Preview** tab of the data set.

**What happens to the record if you reject it?** The record disappears from the quarantine table. However, the record is not lost, it remains in its original state on the **Preview** tab of the data set. If you re-process the data set without changing the previous rules, the record will appear in the quarantine table again.

**To manage quarantined records**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set.

1. Go to the **Quarantine** tab.

    All records are displayed in the table with editable cells.

1. Find values that need to be fixed, and then make changes directly in the cells.

1. When you are satisfied with changes, process the records in one of the following ways:

    - To process the records one by one, select the check mark in the **Actions** column.

    - To process specific records, select checkboxes in the first column for the needed records. You can also process all records by selecting the checkbox in the first column header. Then, in the upper right corner of the table, open the three-dot menu, and select **Process**.

        ![quarantine-3.gif](../../assets/images/integration/additional-operations/quarantine-3.gif)

1. If you do not want to send the records from quarantine to CluedIn, reject them in one of the following ways:

    - To reject the records one by one, select the cross mark in the **Actions** column.

    - To reject specific records, select checkboxes in the first column for the needed records. You can also reject all records by selecting the checkbox in the first column header. Then, in the upper-right corner of the table, open the three-dot menu, and select **Reject**.

    Rejected records are removed from quarantine.