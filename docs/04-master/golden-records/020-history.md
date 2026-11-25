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
last_modified: 2024-01-15
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

- [List view](#list-view) – the flat, chronological view of every data part.

- [Tree view](#tree-view) – a branch tree that shows, at a glance, which data parts belong to the same branch, where branches were merged, and which data part is the latest on each branch.

- [Timeline view](#timeline-view) – the same branches plotted against a time axis, so you can see how far apart in time the data parts on each branch really are.

Switch between List, Tree and Timeline using the view selector at the top of the **History** page. The data source, date, and vocabulary key filters described in [Filters](#filters) apply to all three views: List hides the data parts that do not match, while Tree and Timeline dim them instead of removing them, so the overall branch structure stays visible.

List, Tree and Timeline share the same left-hand and right-hand panels, and only the middle of the page changes:

- **Left panel** – a **Branches** tab (search branches, show or hide one or all of them, focus a single branch, and see how many data parts and current golden record values each branch supplies) and a **Fields** tab (filter by the fields a version changed).

- **Right panel** – selecting a data part, or the **Golden record now** row, opens the **details panel**, with a plain-language summary of what happened, its place on its branch, who and when, the branches a merge joined, and every field it changed, with the old value, the new value, and whether that value is still the one on the golden record today. Technical details, Open record, Copy link and Delete version are available from here.

- Hovering over a data part (in the Tree and Timeline graphs) shows a tooltip with its title, branch, date and how many fields it added, updated, or removed.

### List view

The list view is the default view that shows all data parts that make up a golden record, one row per data part, ordered by date, with the **Golden record now** row pinned to the top.

![The List view of the History page: the Golden record now row pinned above Merge, Changed and Discovered rows, with the Branches panel on the left and the golden record details on the right]({{ "/assets/images/golden-records/history-list-view.png" | relative_url }})

Each row shows:

- A **title** that consists of the source name and additional details. For example, if the source is a clean project, the title also includes the clean project name.

- The **branch** the data part belongs to, with the same colour and name as on the Topology tab and the Tree and Timeline views. A branch contains the data part versions that appeared from the same source.

- The **record ID**, and the date for whichever [date type](#filters) is currently selected.

- A **Latest on this branch** label on the newest data part of each branch.

- A **status** badge that indicates the type of change made on the data part level. For more information about each status, see [Data part statuses](#data-part-statuses).

- A short summary of how many fields the data part added, updated or removed.

Each data part is an individual entity, and it is not linked to other data parts in any way, except if these data parts belong to one branch. Because each data part is individual, the first data part in the branch is marked with the **Added** status and does not contain previous values. If the subsequent data part within the branch contain some changes compared to the first data part in the branch, then such data parts are marked with the **Changed** status.

Selecting a row opens the details panel described above, where you can see every field the data part changed.

![The List view with a Merge row selected, showing its summary, where it sits on its branch, the branches it joined and every field it changed]({{ "/assets/images/golden-records/history-list-view-details.png" | relative_url }})

### Tree view

The tree view draws the same data parts as a branch tree: one lane per branch, with its data parts placed on the lane in time order. This makes it easy to see, for a golden record built from several sources, which data parts belong together, what the latest data part on each branch is, and where branches were joined.

![The Tree view showing three branch lanes joined by a merge, with the Golden record now row above them and the details panel on the right]({{ "/assets/images/golden-records/history-tree-view.png" | relative_url }})

- A **Golden record now** row sits above all the lanes. It is a summary, not a branch — selecting it shows how many current golden record values there are and how many branches supplied them.

- Each **lane** is named and colored the same way as the matching branch on the Topology tab, and is labeled with the kind of source it is: a data source record, an enricher, a clean project, a deduplication merge, or a manual modification.

- A **merge** (from a deduplication project or a manual merge) is drawn as a hollow data part, with one link to the latest data part of each branch it joined at the time of the merge.

- The **latest data part on each branch** is marked, so you can tell at a glance whether a branch has moved on since the golden record last picked up a value from it.

![The details panel for a merge data part, listing the branches it joined and every field it changed]({{ "/assets/images/golden-records/history-tree-merge-details.png" | relative_url }})

If a golden record has more than 24 branches, the 20 most recently active ones each keep their own lane, and the rest are grouped into one grey **Other branches** column. From the details panel of a data part on a grouped branch, you can give that branch its own lane, or group it back.

### Timeline view

The timeline view plots the same branches on a time axis instead of in a plain sequence, one row per branch, so you can see how far apart in time the data parts on a branch really are. Zoom in to spread out data parts that landed close together, which are otherwise grouped into a single, numbered data part on the timeline. Data parts with no date for the currently selected [date filter](#filters) appear in a separate **Date not set** strip so they do not distort the time axis.

![The Timeline view plotting three branches against a date axis, with zoom controls and the details panel on the right]({{ "/assets/images/golden-records/history-timeline-view.png" | relative_url }})

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

- **Status filter** – you can toggle which [data part statuses](#data-part-statuses) are shown: Discovered, Added, Changed, and Merge. Merge is not a status stored on the data part itself; it is shown whenever a data part joined one or more other branches, such as a deduplication or manual merge.

- **Fields filter** – on the **Fields** tab of the left panel, you can select any metadata property or vocabulary key and see the data parts where it is used. A medal icon next to a vocabulary key signifies that it is used in the golden record.

## Data part statuses

You can view the data part statuses when you're on the list view of the **History** page.

| Status | Description |
|--|--|
| Discovered | A data part has been added for the first time in CluedIn. Such data parts do not have the **Created Date** value. The **Previous Value** column in such data part is always empty because this is the first data part in the history.|
| Added | A new data part has been added, creating a new branch. Such data part has the **Created Date** value. The **Previous Value** column is always empty because this is the first data part in a branch. |
| Changed | A new data part has been added within the existing branch. The **Previous Value** column contains the value from the previous data part in the branch. |
| Merge | Shown in the tree and timeline views (and as a filter) whenever a data part joined one or more other branches, such as a deduplication or manual merge. It is not a status stored on the data part itself. |

## Relations history

The relations history page contains detailed information about all outgoing relations (edges) of a golden record. While outgoing edges are included in the golden record history page, viewing them on the relations history page is more convenient.

Each relation is presented as a separate table entry that contains the source, ID, type, and properties. To view the relation properties, simply expand the dropdown in the **Properties** column.

![The Relations view of the History page listing outgoing edges with Source, Part Id, Edge Type and Properties columns]({{ "/assets/images/golden-records/history_relations_properties.png" | relative_url }})

You can filter relations by two criteria:

- **Edge Type** – the type of outgoing relation that a golden record has.

- **Properties** – the properties that an outgoing relation of a golden record has.

If you added an outgoing relation by mistake or if you no longer need an outgoing relation, you can delete it. To do this, select the part ID in the table, and then select **Delete**.