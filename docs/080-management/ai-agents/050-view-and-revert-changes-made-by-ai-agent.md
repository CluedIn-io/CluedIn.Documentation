---
layout: cluedin
title: View and revert changes made by AI agent
parent: AI agents
grand_parent: Management
nav_order: 050
permalink: /management/ai-agents/view-and-revert-changes-made-by-ai-agent
tags: ["management", "ai agents", "review ai agent results"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

All changes that an AI agent makes to golden records are recorded for further review. You can revert any of the changes whenever needed.

## View changes made by an AI agent

You can view the list of all golden records that an AI agent modified, as well as the changes made to a specific golden record.

**To view the changes made by an AI agent**

1. On the navigation pane, go to **AI agents** (or, alternatively, **Management** > **AI Agents**).

1. Select the needed agent in the list. Then, select the needed job.

1. On the job page, go to the **Affected Records** tab. You can now view the list of all golden records that the agent modified.

    ![view_affected_records_sp.png]({{ "/assets/images/management/ai-agents/view-changes-made-by-ai-agents/view_affected_records_sp.png" | relative_url }})

1. To view the changes made to a specific record, select that record in the list.

1. On the golden record page, do one of the following:

    - Go to the **History** tab. Then, locate the record named **AI Agent Job Source** - _Agent name_ - _Job name_. For example, **AI Agent Job Source - Client Data Steward - Fix data quality issues**.

        ![view_affected_records_history_tab.png]({{ "/assets/images/management/ai-agents/view-changes-made-by-ai-agents/view_affected_records_history_tab.png" | relative_url }})

        Expand the record to view the list of changes made.

        ![view_affected_records_history_tab_expanded.png]({{ "/assets/images/management/ai-agents/view-changes-made-by-ai-agents/view_affected_records_history_tab_expanded.png" | relative_url }})

    - Go to the **Topology** tab. Then, locate the node that indicates the changes made by the AI agent. Such nodes are marked with the AI agent icon.

        ![view_affected_records_topology_tab.png]({{ "/assets/images/management/ai-agents/view-changes-made-by-ai-agents/view_affected_records_topology_tab.png" | relative_url }})

        Click the node to view the list of changes made.

        ![view_affected_records_topology_tab_node_panel.png]({{ "/assets/images/management/ai-agents/view-changes-made-by-ai-agents/view_affected_records_topology_tab_node_panel.png" | relative_url }})

        {:.important}
        In the **Value** column, you can view the new property value that the record received after the AI agent made the changes. If you want to view the values both before and after the changes, use the **History** tab.

## Revert changes made by an AI agent

You can revert the following changes made by an AI agent:

- All changes made as part of a specific job.

- All changes made to a specific golden record.

**To revert all changes that an AI agent made**

1. On the navigation pane, go to **AI agents** (or, alternatively, **Management** > **AI Agents**).

1. Select the needed agent in the list. Then, select the needed job.

1. On the job page, go to the **Affected Records** tab.

1. In the upper-right corner of the **Affected Records** tab, select **Revert changes**.

    ![view_affected_records_delete_btn.png]({{ "/assets/images/management/ai-agents/revert-changes-made-by-ai-agents/view_affected_records_delete_btn.png" | relative_url }})

1. Confirm that you want to revert the changes.

**To revert changes that an AI agent made to a specific golden record**

1. Locate and open the needed golden record. You can do this as follows:

    - Using [search](/key-terms-and-features/search).

    - From the AI agent page. To do this, on the navigation pane, go to **AI agents**. Select the needed AI agent and AI agent job, and then go to the **Affected Records** tab.

1. To revert the changes, do one of the following:

    - Go to the **History** tab. Then, locate the record named **AI Agent Job Source** - _Agent name_ - _Job name_. For example, **AI Agent Job Source - Client Data Steward - Fix data quality issues**.

        ![view_affected_records_history_tab.png]({{ "/assets/images/management/ai-agents/view-changes-made-by-ai-agents/view_affected_records_history_tab.png" | relative_url }})

        Open the three-dot menu and select **Delete**.

        ![delete_data_part_from_history_sp.png]({{ "/assets/images/management/ai-agents/revert-changes-made-by-ai-agents/delete_data_part_from_history_sp.png" | relative_url }})

        Then, confirm that you want to revert the changes.

    - Go to the **Topology** tab. Then, locate and open the node that corresponds to the needed change.

        ![view_affected_records_topology_tab.png]({{ "/assets/images/management/ai-agents/view-changes-made-by-ai-agents/view_affected_records_topology_tab.png" | relative_url }})

        In the upper-right corner of the node pane, select **Delete**.
        
        ![delete_data_part_from_topology.png]({{ "/assets/images/management/ai-agents/revert-changes-made-by-ai-agents/delete_data_part_from_topology.png" | relative_url }})

        Then, confirm that you want to revert the changes.