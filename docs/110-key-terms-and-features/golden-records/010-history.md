---
layout: cluedin
nav_order: 1
parent: Golden records
grand_parent: Key terms and features
permalink: /key-terms-and-features/golden-records/history
title: History
tags: ["golden record history"]
last_modified: 2024-01-15
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

History is an important aspect of a golden record because it shows which [data parts](/key-terms-and-features/data-life-cycle) make up a golden record, what values each data part has, and what changes were made to those data parts. In this article, you will learn how the history of a golden record works and how to interpret changes made to golden records.

**Note:** Changes made by golden record rules, data part rules, and survivorship rules are not included in the golden record history.

Depending on which aspect of the history you want to look at, you can switch between the two:

- [Golden record history](#golden-record-history) – here, you can view detailed information about all data parts that make up a golden record.

- [Relations history](#relations-history) – here, you can view detailed information about all outgoing relations (also referred to as _edges_) of a golden record.

    ![history_switch.png](../../assets/images/golden-records/history_switch.png)

## Golden record history

A golden record is made up of many data parts. These data parts can appear from clean projects, deduplication projects, files, crawlers, or manual modifications. For example, if you create a clean project and it affects a golden record property, then a new data part is added to the golden record history, showing the affected property along with other metadata properties. Similarly, if you manually edit a golden record property, then a new data part is added to the golden record history, showing the new property value.

Every time a data part appears in the history, a _branch_ is created. Branches help organize data parts by sources and easily retrieve data parts that were created from one source. For example, data parts that appeared from one clean project belong to one branch, and data parts from a different clean project belong to a different branch.

Each branch has a _head_ that contains values from the data parts belonging to that branch. The same golden record property can have different values in each head. By default, the latest value coming to CluedIn or the latest manually modified value is used in the golden record. If you want to determine which value should be used in a golden record property, create a [survivorship rule](/management/rules). The following diagram illustrates the process of establishing a golden record.

![history-diagram.png](../../assets/images/key-terms-and-features/history-diagram.png)

By default, the **History** page displays the data parts arranged by the sort date (this is the date when CluedIn received the data part). You can explore the data parts using the following views:

- [Data part view](#data-part-view)

- [Golden record view](#golden-record-view)

### Data part view

The data part view is the default view that shows all data parts that make up a golden record.

![history-1.png](../../assets/images/key-terms-and-features/history-1.png)

Each data part has the following attributes:

- A **color circle** that represents a branch. A branch contains the data part versions that appeared from the same source. For example, if you have a crawler that changes some properties of the data part, these changes will be added to the branch as separate data part versions. By selecting the color circle, you can view the branch (1) and its versions (2, 3).

    ![history-2.png](../../assets/images/key-terms-and-features/history-2.png)

- An **icon** that represents a source. A source is a place where the data part is coming from. A source can be a clean project, a deduplication project, a manual data entry project, a file, a crawler, and so on.

- A **title** of the data part that consists of the source name and additional details. For example, if the source is the clean project, then the title also includes the clean project name. You can view the source by selecting the title.

- A **data part ID** (also referred to as record ID). You can view the data part properties (vocabulary keys) by selecting the ID number. These data part properties are used to produce a head, which is then processed by survivorship rules to determine the operational values for the golden record.

- Data part **details**, such as the user who created the data part and dates associated with the data part. For more information about what each date means, see [Filters](#filters).

- Data part **status** that indicates the type of change made on the data part level. For more information about each status, see [Dat part statuses](#data-part-statuses).

By expanding the data part, you can view a table with the metadata properties and vocabulary keys associated with the data part. Each property is marked with the change type label, which indicates whether the property is newly added or changed from one data part version to another.

Each data part is an individual entity, and it is not linked to other data parts in any way, except if these data parts belong to one branch. Because each data part is individual, the first data part in the branch is marked with the **Added** status and does not contain previous values. If the subsequent data part within the branch contain some changes compared to the first data part in the branch, then such data parts are marked with the **Changed** status.

### Golden record view

The golden record view appears when you select any metadata properties or vocabulary keys on the filters pane on the left side of the **History** page. This view shows all records (1) where the selected property or vocabulary key is used, along with the value (2) that is used in the golden record (this is the value that is shown on the **Property** tab of the golden record details page). By looking at the sort date, you can track the historical changes in the property value across all data parts.

![history-3.png](../../assets/images/key-terms-and-features/history-3.png)

{:.important}
**Part ID** from the golden record view and **Record ID** from the data part view are the same.

### Filters

The **History** page contains various filters to help you navigate through the data parts:

- **Data source filter** – you can filter the data parts by the data source that indicates a place where a data part was produced. By default, the data parts from all data sources are displayed on the **History** page.

    ![data-source-filter.png](../../assets/images/golden-records/data-source-filter.png)

- **Date filter** – you can filter the data parts by one of the following dates:

    - **Sort date** – this date is determined by selecting the first available date among modified, created, and discovery dates. In most cases, this is the date when CluedIn received the data.

    - **Modified date** – the date when the data part was last modified in the source system.

    - **Created date** – the date when the data part was originally created in the source system.

    - **Discovery date** – the date when the data part was created in CluedIn.

        ![date-filter.png](../../assets/images/golden-records/date-filter.png)

- **Metadata filter** – you can select any metadata property and see the data parts where it is used.

    ![metadata-filter.png](../../assets/images/golden-records/metadata-filter.png)

- **Vocabulary key filter** – you can select any vocabulary key and see the data parts where it is used, as well as the value chosen for the golden record. The medal icon next to the vocabulary key signifies that this vocabulary key is used in the golden record.

    ![vocab-key-filter.png](../../assets/images/golden-records/vocab-key-filter.png)

## Data part statuses

You can view the data part statuses when you're on the data part view of the **History** page.

| Status | Description |
|--|--|
| Discovered | A data part has been added for the first time in CluedIn. Such data parts do not have the **Created Date** value. The **Previous Value** column in such data part is always empty because this is the first data part in the history.|
| Added | A new data part has been added, creating a new branch. Such data part has the **Created Date** value. The **Previous Value** column is always empty because this is the first data part in a branch. |
| Changed | A new data part has been added within the existing branch. The **Previous Value** column contains the value from the previous data part in the branch. |

## Relations history

The relations history page contains detailed information about all outgoing relations (edges) of a golden record. While outgoing edges are included in the golden record history page, viewing them on the relations history page is more convenient.

Each relation is presented as a separate table entry that contains the source, ID, type, and properties. To view the relation properties, simply expand the dropdown in the **Properties** column.

![history_relations_properties.png](../../assets/images/golden-records/history_relations_properties.png)

You can filter relations by two criteria:

- **Edge Type** – the type of outgoing relation that a golden record has.

- **Properties** – the properties that an outgoing relation of a golden record has.

If you added an outgoing relation by mistake or if you no longer need an outgoing relation, you can delete it. To do this, select the part ID in the table, and then select **Delete**.