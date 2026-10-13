---
title: Golden record relations
url: https://documentation.cluedin.net/master/golden-records/golden-record-relations
content_type: how-to
section: Master > Golden records
---

# Golden record relations

> how-to: Steps to accomplish one task.

Relations connect golden records by linking a source record to a target record through a specific edge type (for example, _/WorksFor_ or _/FinancedBy_). These relations can be created either before or after data is [processed](https://documentation.cluedin.net/ingest/processing/process-data.md).

In this article, you will learn how to view and manage relations between golden records.

## Manage relations between golden records

Golden Record relations capture real-world connections – for example, between customers and companies, products and vendors, or employees and organizations. In CluedIn, you can create these relations to link one golden record to another. This enriches the context of each record and makes it easier to navigate and analyze your data.

If a connection is no longer valid, you can delete the relation from CluedIn.

### Add relations between golden records

You can add relations in CluedIn in several ways:

- When ingesting data into CluedIn. This method is useful when adding relations for multiple records at once. For details, see [Add relations between records](https://documentation.cluedin.net/model/relationships/tutorial-add-relations.md).

- From the golden record page. This method is useful when adding relations for the same record.

**To add relations from the golden record page**

1. Locate the golden record for which you want to add relations. Then, go to the **Relations** tab of the record.

1. On the left side of the page, at the top of the settings panel, select **Add Relation**.

    ![Relations tab of golden record PO-4100 with the Add relation button highlighted above the settings panel, and the relations graph on the right](https://documentation.cluedin.net/assets/images/golden-records/relations/add-relations/Images/add_relation_btn.png)

   The **Add Edge** panel opens on the right side of the page.

1. On the **Root Record** tab, select whether the relation you want to add is incoming to the current record or outgoing from it. Then, at the bottom of the tab, select **Next**.

    ![Add relation panel on the Relation type step: relation type /LocatedIn, direction Outgoing, with source record PO-4100 shown below](https://documentation.cluedin.net/assets/images/golden-records/relations/add-relations/Images/add_edge_tab.png)

1. On the **Target Record** tab, do the following:

    1. Specify the **edge type** to define the nature of relation between the current record and the record you want to link to it. You can select an existing edge type or create a new one. To create a new edge type, enter a slash (/) followed by a name.

    1. Select the **business domain** of the record that you want to link to the current one.

    1. Select the **record** that you want to link to the current one.

    1. At the bottom of the tab, select **Next**.

    ![Add relation panel on the Target record step: business domain Address and target record Zeppelinstrasse 44 selected](https://documentation.cluedin.net/assets/images/golden-records/relations/add-relations/Images/target_record_tab.png)

1. (Optional) On the **Add Properties** tab, add properties that define edge relations between the two records. Then, at the bottom of the tab, select **Next**.

    ![Add relation panel on the Properties step with an Add property button and the message No edge properties](https://documentation.cluedin.net/assets/images/golden-records/relations/add-relations/Images/add_properties_tab.png)

1. On the **Preview Edge** tab, review the details of the relation that you are adding. Then, at the bottom of the tab, select **Add Edge**.

    ![Add relation panel on the Preview step showing source PO-4100, target Zeppelinstrasse 44, relation type /LocatedIn and direction Outgoing, with the Add relation button](https://documentation.cluedin.net/assets/images/golden-records/relations/add-relations/Images/preview_edge_tab.png)

1. Confirm that you want to add the relation.

    The relation is added and appears in the graph.

    ![Relations graph of the Marketing department record with the newly added /WorksFor relation from Chris Young highlighted](https://documentation.cluedin.net/assets/images/golden-records/relations/add-relations/Images/relation_added.png)

### Delete relations between golden records

You can delete any direct relation of a golden record.

**To delete relation from a golden record**

1. Locate the golden record that contains the relation you want to remove. Then, go to the **Relations** tab of the record.

1. On the left side of the page, at the top of the settings panel, select **Delete Relation**.

    ![Relations tab of golden record PO-4100 with the Delete relations button highlighted next to Add relation](https://documentation.cluedin.net/assets/images/golden-records/relations/delete-relations/Images/delete_relation_btn.png)

    The **Delete Edge** panel opens on the right side of the page.

1. On the **Select Edge** tab, select the relation that you want to delete. Then, select **Next**.

    ![Delete Edge panel on the Select Edge step, listing outgoing and incoming edges with /DeliversTo Industriestrasse 23 selected](https://documentation.cluedin.net/assets/images/golden-records/relations/delete-relations/Images/delete_edge_panel_select_relation.png)

1. On the **Preview Edge** tab, select **Delete Edge**.

    ![Delete Edge panel on the Preview Edge step: root record PO-4100, target Industriestrasse 23, edge type /DeliversTo, with the Delete Edge button](https://documentation.cluedin.net/assets/images/golden-records/relations/delete-relations/Images/delete_edge_panel_preview_tab.png)

1. Confirm the deletion.

## View relations between golden records

Once a golden record is processed, you can view its relations with other golden records. As new records are linked, those relationships are automatically displayed in CluedIn.

**To view the relations of a golden record**

1. Locate the golden record whose relations you want to view. Then, go to the **Relations** tab of the record.

    ![Default Relations tab of DB Schenker AG: settings panel with filters, levels and counts on the left, the relations graph in the centre](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/relations_tab_default_view.png)

   Here, you can view all the relations that the record has. As relations are added or removed, the information on the tab is updated accordingly.

1. Use levels to define how deeply you want to go in your graph.

    ![Relations tab with the Levels slider set to depth 3, showing more records and 22 relationships in the graph](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/select_graph_level_sp.png)

    Consider this example: parent company – child company – department. When viewing the relations for the department record, levels work as follows:

    - Level 1 – shows the relation between the department and the child company.

    - Level 2 – expands further to show the relations between the department, the child company, and the parent company.

1. Use filters to narrow down the information displayed in the graph:

    - **Direction** – choose whether to display incoming, outgoing, or both types of relations.

        ![Relations tab with the Direction filter set to Outgoing, showing 17 outgoing relations and no incoming relations](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/select_directions_sp.png)

    - Select which **Business Domains** and **Relationship Types** to include in the graph.

        ![Business domains and Relationship types filter lists with some items cleared, so the graph shows only the selected domains and relation types](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/select_domains_and_relation_types_sp.png)

1. Configure **Graph Display Settings**:

    - **Include all directions** – when this option is enabled, the graph will expand all direct relations of the neighbouring records.

    - **Include Shadow Records** – when this option is enabled, the graph will also show all [shadow records](https://documentation.cluedin.net/get-started/core-concepts/eventual-connectivity.md) associated with the golden records in it. This option may be useful when debugging relations between golden records.

        In the following example, the author of the **Horizon Campaign Brief** is a shadow record (**Grace Patterson**), and not a regular golden record.

        ![Graph with Include Shadow Records enabled, showing the Horizon Campaign Brief linked by /Action/CreatedBy to a shadow record whose detail panel shows Record Type Shadow Record](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/include_shadow_records_sp.png)

        Shadow records are records that exist in CluedIn but are flagged as hidden. This typically happens when a record does not have enough values to be promoted to a golden record and contains only [identifiers](https://documentation.cluedin.net/model/identifiers.md).

    - **Include Temporal Relations** – when this option is enabled, the graph will also show time-based connections between golden records. Temporal relations highlight how records are linked through events or periods in time: for example, showing that a person worked for a company, but only between 2015 and 2020. This option is useful when you need to understand not just how the records are related, but also when those relations existed.

        In the following example, the **Marketing** department record was added to CluedIn on September 10, 2025. On the same date, several more relations were created.

        ![Graph of PO-4100 with Include temporal relations enabled, showing the date node 2026-05-19 linked to the record](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/include_temporal_relations_sp.png)

   - **Include Enricher Data** – when this option is enabled, the graph will also show records that consist only of data provided by [enrichers](https://documentation.cluedin.net/govern/enrichment.md).

1. Find and highlight specific nodes in the graph:

    - To find records by their display name, on the settings panel on the left side of the page, enter the needed search keyword. In the graph, matching records become highlighted in yellow.

        ![Search box with Schenker entered, reporting 3 matching golden records that are highlighted in yellow in the graph](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/search_records_by_name_sp.png)

    - To find records that have a specific value (vocabulary key value or relation property value), at the top of the settings panel, select **Advanced Filters**.

        ![Relations tab settings panel with the Advanced filters link highlighted next to Reset filters](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/select_advanced_filters_sp.png)

        Then, in the **Advanced Filters** section, select the values of interest. In the graph, matching records become highlighted in yellow.

        ![Advanced filters with vocabulary key cp.invoice.amount and value 37000 selected, one matching record, and the matching invoice node highlighted in the graph](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/find_specific_values_sp.png)

1. Review the information about the relations and nodes that appear in the graph:

    - To view basic information about a relation or a node in the graph, hover over that element. The corresponding information appears in the details panel on the right of the page.

        ![Hovering over the DB Schenker AG node shows a details panel with its business domain, total relationships, direct edge types and direct neighbours by business domain](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/view_node_basic_information_sp.png)

    - To view detailed information about a relation or a node, click that element in the graph.

         Example of detailed information for a relation:

        ![Relation detail pane for /IsRoleOf showing relation type, From and To records, an Edit button, and no edge properties](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/view_relation_further_information_sp.png)

        Example of detailed information for a node:

        ![Golden record detail pane for DB Schenker AG with Vocabulary keys, Properties, Neighbours and Direct relations tabs, listing vocabulary key values and sources](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/view_node_further_information_sp.png)

    - To expand a node and view all of its direct relations, double-click that node in the graph.

        As an example, pay attention to the **Project Phoenix** node before being expanded.

        ![Relations graph with the collapsed Via Roma 12 node highlighted before it is expanded](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/node_before_double_click_sp.png)

        After being expanded, the node reveals three additional relations.

        ![Relations graph after double-clicking Via Roma 12: its additional relations are shown, and Expanded records lists Via Roma 12 with a Reset expansion link](https://documentation.cluedin.net/assets/images/golden-records/relations/view-relations/Images/node_after_double_click_sp.png)

Up: [Golden records](https://documentation.cluedin.net/master/golden-records.md)
