---
layout: cluedin
title: History
parent: Golden records
grand_parent: Master
nav_order: 20
permalink: /master/golden-records/history
content_type: concept
redirect_from: ["/key-terms-and-features/golden-records/history", "/user-interface/history"]
source_path: docs/110-key-terms-and-features/golden-records/020-history.md
tags: ["golden record history"]
last_modified: 2026-11-26
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

History is an important aspect of a golden record because it shows which [data parts](/get-started/core-concepts/data-life-cycle) make up a golden record, what values each data part has, and what changes were made to those data parts. In this article, you will learn how the history of a golden record works and how to interpret changes made to golden records.

**Note:** Changes made by golden record rules, data part rules, and survivorship rules are not included in the golden record history.

Depending on which aspect of the history you want to look at, you can switch between the two:

- [Golden record history](#golden-record-history) – here, you can view detailed information about all data parts that make up a golden record.

- [Relations history](#relations-history) – here, you can view detailed information about all outgoing relations (also referred to as _edges_) of a golden record.

    ![The History tab of a golden record with the Golden Record and Relations switch highlighted]({{ "/assets/images/golden-records/history_switch.png" | relative_url }})

## Golden record history

A golden record is made up of many data parts. These data parts can appear from clean projects, deduplication projects, files, crawlers, or manual modifications. For example, if you create a clean project and it affects a golden record property, then a new data part is added to the golden record history, showing the affected property along with other metadata properties. Similarly, if you manually edit a golden record property, then a new data part is added to the golden record history, showing the new property value.

Every time a data part appears in the history, a _branch_ is created. Branches help organize data parts by sources and easily retrieve data parts that were created from one source. For example, data parts that appeared from one clean project belong to one branch, and data parts from a different clean project belong to a different branch.

Each branch has a _head_ that contains values from the data parts belonging to that branch. The same golden record property can have different values in each head. By default, the latest value coming to CluedIn or the latest manually modified value is used in the golden record. If you want to determine which value should be used in a golden record property, create a [survivorship rule](/govern/rules). The following diagram illustrates the process of establishing a golden record.

![Diagram: the heads of the file data source, manually added and clean project branches feed a survivorship rule, which produces the golden record]({{ "/assets/images/key-terms-and-features/history-diagram.png" | relative_url }})

By default, the **History** page displays the data parts arranged by the sort date (this is the date when CluedIn received the data part). You can explore the data parts using the following views:

- [Data part view](#data-part-view)

- [Golden record view](#golden-record-view)

### Data part view

The data part view is the default view that shows all data parts that make up a golden record.

![The data part view listing two data parts, each with a color circle for its branch, source, record ID, author, dates and an Added status]({{ "/assets/images/key-terms-and-features/history-1.png" | relative_url }})

Each data part has the following attributes:

- A **color circle** that represents a branch. A branch contains the data part versions that appeared from the same source. For example, if you have a crawler that changes some properties of the data part, these changes will be added to the branch as separate data part versions. By selecting the color circle, you can view the branch (1) and its versions (2, 3).

    ![The History page filtered to the CluedInManualModification branch, showing its two data parts, one Changed and one Added]({{ "/assets/images/key-terms-and-features/history-2.png" | relative_url }})

- An **icon** that represents a source. A source is a place where the data part is coming from. A source can be a clean project, a deduplication project, a manual data entry project, a file, a crawler, and so on.

- A **title** of the data part that consists of the source name and additional details. For example, if the source is the clean project, then the title also includes the clean project name. You can view the source by selecting the title.

- A **data part ID** (also referred to as record ID). You can view the data part properties (vocabulary keys) by selecting the ID number. These data part properties are used to produce a head, which is then processed by survivorship rules to determine the operational values for the golden record.

- Data part **details**, such as the user who created the data part and dates associated with the data part. For more information about what each date means, see [Filters](#filters).

- Data part **status** that indicates the type of change made on the data part level. For more information about each status, see [Dat part statuses](#data-part-statuses).

By expanding the data part, you can view a table with the metadata properties and vocabulary keys associated with the data part. Each property is marked with the change type label, which indicates whether the property is newly added or changed from one data part version to another.

Each data part is an individual entity, and it is not linked to other data parts in any way, except if these data parts belong to one branch. Because each data part is individual, the first data part in the branch is marked with the **Added** status and does not contain previous values. If the subsequent data part within the branch contain some changes compared to the first data part in the branch, then such data parts are marked with the **Changed** status.

### Golden record view

The golden record view appears when you select any metadata properties or vocabulary keys on the filters pane on the left side of the **History** page. This view shows all records (1) where the selected property or vocabulary key is used, along with the value (2) that is used in the golden record (this is the value that is shown on the **Property** tab of the golden record details page). By looking at the sort date, you can track the historical changes in the property value across all data parts.

![The golden record view for Job Title: the golden record value Senior Accountant above a table of the value from each data part]({{ "/assets/images/key-terms-and-features/history-3.png" | relative_url }})

{:.important}
**Part ID** from the golden record view and **Record ID** from the data part view are the same.

### Filters

The **History** page contains various filters to help you navigate through the data parts:

- **Data source filter** – you can filter the data parts by the data source that indicates a place where a data part was produced. By default, the data parts from all data sources are displayed on the **History** page.

    ![The History page with the data source filter set to All data sources highlighted next to the total count]({{ "/assets/images/golden-records/data-source-filter.png" | relative_url }})

- **Date filter** – you can filter the data parts by one of the following dates:

    - **Sort date** – this date is determined by selecting the first available date among modified, created, and discovery dates. In most cases, this is the date when CluedIn received the data.

    - **Modified date** – the date when the data part was last modified in the source system.

    - **Created date** – the date when the data part was originally created in the source system.

    - **Discovery date** – the date when the data part was created in CluedIn.

        ![The sort date dropdown open with the options Sort Date, Modified Date, Created Date and Discovery Date]({{ "/assets/images/golden-records/date-filter.png" | relative_url }})

- **Metadata filter** – you can select any metadata property and see the data parts where it is used.

    ![The Authors metadata property selected on the filters pane, with the matching data parts and their authors shown on the right]({{ "/assets/images/golden-records/metadata-filter.png" | relative_url }})

- **Vocabulary key filter** – you can select any vocabulary key and see the data parts where it is used, as well as the value chosen for the golden record. The medal icon next to the vocabulary key signifies that this vocabulary key is used in the golden record.

    ![The Vocabulary Keys list on the filters pane with trainingcontact.job Title selected, each key marked with a medal icon]({{ "/assets/images/golden-records/vocab-key-filter.png" | relative_url }})

## Redesigned golden record history

When the **Golden Record History - New Tree View** [feature flag](/administer/feature-flags) is turned on, the **Golden Record** view of the **History** tab uses a redesigned layout. It shows the same versions (data parts) as the views above, but adds filtering, a tree of sources, and a side panel for each version.

![The redesigned golden record history: toolbar, filter chips, Sources and Fields filter pane, and the list of versions grouped by day]({{ "/assets/images/golden-records/history-v2/list-view.png" | relative_url }})

### Toolbar and filters

- **Search values** – finds versions whose old or new values contain the text. Field names are not searched.
- **List** and **Tree** – switch between a list of versions and the same list with a tree of sources beside it.
- **Change type** – shows only the selected types: **Discovered**, **Added**, **Changed**, or **Merged**. You can select several.
- **Date** – limits the versions to **Any time**, or to the last 7, 30, or 90 days.
- **Sort** – **Newest first** or **Oldest first**.
- **Sources** and **Fields** – on the filter pane, select one or more sources or fields to show only their versions. Each source shows its latest date, how many current values it supplies (or **Superseded** if it supplies none), and its number of versions. Fields are grouped: metadata first, then one group per vocabulary. Select **Show all** to clear the selection. To collapse the pane, use the chevron on its edge.

Every active filter appears as a chip above the list. Select the **x** on a chip to remove that filter, or **Clear all** to remove them all. Each filter change updates the list, the counts, and the tree immediately and returns you to the first page.

### Versions list

The first row is always the golden record as it stands now. It shows how many current values it has, how many sources supply them, and when it last changed. Select it to see each source and the share of current values it supplies. From that panel, select **View in Properties** to open the **Properties** tab.

The other rows are versions, grouped by day. Each row shows:

- The source, marked by its color and logo.
- A plain-language title, for example, _SAP ERP updated 2 values_.
- Up to three changes, each showing the field, the old value (struck through), and the new value.
- The time, the user, and the version's position among that source's versions.
- One change type tag.

Select a row to open its version details. Select any field name to open that field's history. The **⋮** menu on a row lets you view details, open the source record, copy a link to the version, or delete the version. Merges can't be deleted; you can undo them instead (see [Version details](#version-details)).

### Tree view

In the tree view, each source has its own column. The logo headers stay visible as you scroll: point to a header to see the source name and its number of versions, or select it to filter by that source. The gold bar with a star at the top joins all sources into the golden record. Merges are drawn as dashed grey lines.

![The tree view: one column per source beside the list, with one source highlighted and a tooltip for the version under the pointer]({{ "/assets/images/golden-records/history-v2/tree-view.png" | relative_url }})

When you point to a node or a row, that source's line, nodes, and rows stay highlighted and the others fade. A tooltip shows the source, change type, version, date, user, and changed fields. Select a node to open that version.

To change the width of the tree, drag its edge, or focus the edge and use the arrow keys. Double-click the edge to reset the width. If the columns get narrow, the logos are replaced by colored dots.

### Version details

The version details panel shows:

- **Versions from source** – that source's versions as numbered steps, with the current one filled in. For more than nine versions, the steps in between are collapsed, and you can use **Jump to version** to open any version. Under the steps, a status line tells you how long after the previous version this one arrived, and whether it still supplies current values or has been superseded.
- **Changes** – a table of each field, its action (**Added**, **Updated**, or **Removed**), and the value before and after. Switch **Previous version** to **Golden record now** to compare this version's values with the current golden record instead.
- **Joined sources** – for merges only, the records that were merged. **Undo merge** opens the deduplication project the merge came from, where you can undo it.
- **Metadata** and **Technical details** – collapsed by default.

![The version details panel: numbered versions from the source, the status line, and the Changes table]({{ "/assets/images/golden-records/history-v2/version-details.png" | relative_url }})

From the panel, select **Copy link to this version** to share a link that opens this version directly, or **Open source record** to see the data part's properties.

### Field history

Select any field name, in the list or in version details, to see the field's current value, the source that supplied it, and every value it has had over time. Select **Back** to return to the previous panel.

![The Field history panel: the current value and its source, then every value the field has had, newest first]({{ "/assets/images/golden-records/history-v2/field-history.png" | relative_url }})

Long values are shortened with an ellipsis. Point to a shortened value, or focus it, to see it in full.

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

![The Relations view of the History page listing outgoing edges with Source, Part Id, Edge Type and Properties columns]({{ "/assets/images/golden-records/history_relations_properties.png" | relative_url }})

You can filter relations by two criteria:

- **Edge Type** – the type of outgoing relation that a golden record has.

- **Properties** – the properties that an outgoing relation of a golden record has.

If you added an outgoing relation by mistake or if you no longer need an outgoing relation, you can delete it. To do this, select the part ID in the table, and then select **Delete**.