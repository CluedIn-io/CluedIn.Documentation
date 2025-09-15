---
layout: cluedin
title: Tag monitoring
parent: Governance
nav_order: 1
permalink: /governance/tag-monitoring
tags: ["governance", "tag monitoring", "tags"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Tags are an essential mechanism that helps you [flag golden records that have data quality issues](https://documentation.cluedin.net/kb/how-to-tag-records-with-data-quality-issues). With the Tag Monitoring module, you can gain insight into tag usage across CluedIn. In particular, you can monitor the following information:

- List of tags used across CluedIn.

- History of tag usage over time.

- Statistics on the numbers of golden records tagged.

- List of records tagged.

In addition to providing insight, the Tag Monitoring module also allows you to act on the information presented to you. In particular, you can do the following:

- [Create new tags](#add-new-tags).

- [Fix tagged records using AI agents](#fix-tagged-records-with-ai).

- [Create a clean project](#create-a-clean-project-for-tagged-golden-records) for the tagged records.

{:.important}
The tag monitoring functionality is not enabled by default. To use it, you must first [enable](#enable-the-tag-monitoring-functionality) it.

## Enable the Tag Monitoring functionality

The tag monitoring functionality is not enabled by default. To use it, you must first enable it.

**To enable the tag monitoring functionality**

1. On the navigation pane, go to **Administration** > **Feature Flags**.

1. On the **Tag Monitoring** card, set the toggle to **Enabled**.

    ![tag_monitoring_feature_flag.png]({{ "/assets/images/governance/tag-monitoring/enable-tag-monitoring-feature/Images/tag_monitoring_feature_flag.png" | relative_url }})

    You can now proceed to [monitor tag usage](#monitor-tag-usage).

## Monitor tag usage

With the Tag Monitoring module, you can monitor the following information:

- List of most-used tags, based on the number of records flagged with them.

- List of all tags used—including the following: history of tag usage over time, statistics on the number of golden records tagged, and the list of records tagged.

This article explains how to monitor both types of information.
       
**To monitor the most-used tags**

1. On the navigation pane, go to **Home**.

1. Scroll down until you reach the **Golden Records Overview** section.

1. Review the **Top tags by golden record count** chart. It displays up to 5 most-used tags based on the number of records that are currently flagged with them.

    ![top_tags_chart_sp.png]({{ "/assets/images/governance/tag-monitoring/monitor-tag-usage/Image/top_tags_chart_sp.png" | relative_url }})

    {:.important}
    If the chart is not available, this may mean that the Tag Monitoring functionality is not [enabled](#enable-the-tag-monitoring-functionality).

1. Select a tag to view detailed information about it. You are now redirected to the **Tag Monitoring** module, where that tag is already selected in the list for you. For details on how to use the **Tag Monitoring** module, see the following procedure.

    ![top_tags_chart_go_to_tag_monitoring_sp.png]({{ "/assets/images/governance/tag-monitoring/monitor-tag-usage/Image/top_tags_chart_go_to_tag_monitoring_sp.png" | relative_url }})

**To monitor all tags used**

1. On the navigation pane, go to **Governance** > **Tag Monitoring**.

    {:.important}
    If the **Tag Monitoring** module is not available, this may mean that the tag monitoring functionality is not [enabled](#enable-the-tag-monitoring-functionality).

1. By default, the **Tag Monitoring** page shows the data for all [business domains](/key-terms-and-features/Image/entity-type) and for the last month going back from today.

    If needed, select the following:

    1. Business domain of interest.

    1. Period of interest.

    ![select_domain_and_period-2.png]({{ "/assets/images/governance/tag-monitoring/monitor-tag-usage/Image/select_domain_and_period-2.png" | relative_url }})

1. On the tags panel on the left, select the tag of interest.

    ![select_tag_interest.png]({{ "/assets/images/governance/tag-monitoring/monitor-tag-usage/Image/select_tag_interest.png" | relative_url }})

    The tags panel shows the following information about a tag:

    1. The [rule]/management/rules) that was used to apply this tag.

    1. [Rule type](/management/rules/rule-types) (data part rule or golden record rule).

    1. The total number of golden records that are currently flagged with this tag.
    
        This number takes into account the currently selected domain. For example, if there are a total of 100 records flagged, and 20 of them are from the /Client business domain, they you will see the number 20 when you select the /Client domain. Otherwise, you will see the number 100.

    1. The percentage of golden records that are currently flagged with this tag.

        - If you selected a business domain in step 2a, then the percentage refers to the number of tagged records only within that domain.

        - If no domain is selected, the percentage refers to the number of tagged records compared to all records in CluedIn.

    ![tag_card.png]({{ "/assets/images/governance/tag-monitoring/monitor-tag-usage/Image/tag_card.png" | relative_url }})

1. In the **Data quality in business domains** chart on the right, review the information about the tag usage over time. To view the number of records tagged at a specific time, hover over the corresponding data point in the chart.

    ![view_data_point_sp.png]({{ "/assets/images/governance/tag-monitoring/monitor-tag-usage/Image/view_data_point_sp.png" | relative_url }})

    {:.important} 
    By default, the data in the chart refreshes every 15 minutes. Your administrator can change this interval in **Administration** > **Settings** > **High Time Resolution Metric interval in minutes**.

1. At the bottom of the page, review the list of golden records tagged with the selected tag.

    ![view_tagged_records.png]({{ "/assets/images/governance/tag-monitoring/monitor-tag-usage/Image/view_tagged_records.png" | relative_url }})

    If needed, adjust how the list is displayed:

    - Select which properties should appear in the table. To do this, above the table, select **Column Options**. Then, select the needed properties or vocabulary keys. For details on how to work with column options, see [Search](/key-terms-and-features/search#search-results-page).

    - By default, the records in the table are sorted by relevance. To sort the records in a different way, above the table, expand the sorting dropdown menu, and then select the needed sorting option.

1. Act on the tagged golden records. You can perform the following actions:

    - [Fix tagged records with AI](#fix-tagged-records-with-AI).

    - [Create a clean project](#create-a-clean-project-for-tagged-golden-records) for the records tagged.

    - [Add new tags](#add-new-tags) if the current ones are not sufficient.

## Fix tagged records with AI

You can leverage [AI agents](/management/ai-agents) to fix the golden records flagged with a specific tag.

**Pre-requisites**

- The AI agents feature must be enabled. For details, see [Prerequisites to using AI agents](/management/ai-agents/prerequisites-to-using-ai-agents).

**To fix tagged records with AI**

1. On the navigation pane, go to **Governance** > **Tag Monitoring**.

    {:.important}
    If the **Tag Monitoring** module is not available, this may mean that the tag monitoring functionality is not [enabled](#enable-the-tag-monitoring-functionality).

1. On the tags panel on the left, select the tag of interest.

    ![select_tag.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/select_tag.png" | relative_url }})

1. In the upper-right corner of the page, select **Fix Data Quality Issues with AI**.

    ![fix_with_ai_btn.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/fix_with_ai_btn.png" | relative_url }})

    {:.important}
    If the **Fix Data Quality Issues with AI** button is unavailable, this may mean that the AI agents feature is not [enabled](/management/ai-agents/prerequisites-to-using-ai-agents).

    The **Fix Data Quality Issues with AI** panel opens on the right of the page.

1. On the **Fix Data Quality Issues with AI** panel, do the following:

    1. Select an **AI Agent** and an **Endpoint** that are most suitable to fix the tagged records.

    1. Use the **Active** toggle to set whether the job should be enabled by default. You can update this setting later on the job page.

    1. Select **Create AI Job**.

    ![fix_with_ai_panel.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/fix_with_ai_panel.png" | relative_url }})

    An [AI agent job](/management/ai-agents/create-configure-and-run-an-ai-agent#create-a-job) is created to handle the selected tagged records. A corresponding label appears in the upper-right corner of the page.

    ![ai_agent_job_creted.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/ai_agent_job_creted.png" | relative_url }})

    At this point, the AI agent did not analyze or change the records in any way.

1. Configure, test, and run the AI agent job:

    1. In the upper-right corner of the page, select **View Results**.

        ![view_results_btn.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/view_results_btn.png" | relative_url }})

        You are redirected to the AI agent job page.

    1. Go to the **Configuration** tab of the job. Note that the **Data** and **Skills** sections are filled out for you.

        {:.important}
        The **Data** section defines the subset of data the AI agent should work on. When you create an AI agent job, CluedIn automatically includes all records flagged with the selected tag (in this example, **invalid-validation-phone**). This selection applies across all business domains, even if you have a domain selected on the **Tag Monitoring** page.

        ![ai_agent_job_data_and_skills.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/ai_agent_job_data_and_skills.png" | relative_url }})

      1. Review the provided **Instructions**. If needed, provide any additional ones.

         ![edit_instructions.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/edit_instructions.png" | relative_url }})

      1. [Test the job](/management/ai-agents/create-configure-and-run-an-ai-agent#test-the-job) to verify that it fixes the records as expected.

         ![test_job_btn.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/test_job_btn.png" | relative_url }})

      1. [Run the job](create-configure-and-run-an-ai-agent#run-the-job) and [review its results](/management/ai-agents/review-the-results-returned-by-an-ai-agent) to have the records fixed.

         ![run_job_btn.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/run_job_btn.png" | relative_url }})

1. When done, go back to **Governance** > **Tag Monitoring** to verify that there is a decrease in the number of records flagged with the selected tag.

    ![verify_records_are_fixed_sp.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/verify_records_are_fixed_sp.png" | relative_url }})

    {:.important}
    By default, the data in the chart refreshes every 15 minutes. Your administrator can change this interval in **Administration** > **Settings** > **High Time Resolution Metric interval in minutes**.

## Create a Clean project for tagged records

After you [use](#monitor-tag-usage) the **Tag Monitoring** page to display the list of golden records flagged with a specific tag, you can create a [clean project](/preparation/clean) for these golden records.

{:.important}
Clean projects are intended to fix the records manually. You can also leverage the AI agents to [fix the records automatically and at scale](#fix-tagged-records-with-ai).

**To create a clean project for tagged golden records**

1. On the navigation pane, go to **Governance** > **Tag Monitoring**.

    {:.important}
    If the **Tag Monitoring** module is not available, this may mean that the tag monitoring functionality is not [enabled](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/4280/Enable-the-tag-monitoring-functionality).

1. On the tags panel on the left, select the tag of interest.

    ![select_tag.png]({{ "/assets/images/governance/tag-monitoring/create-clean-project/Images/select_tag.png" | relative_url }})

1. Above the list of tagged golden records, open the three-dot menu, and then select **Clean**.

    ![three_dot_menu_clean_btn_sp.png]({{ "/assets/images/governance/tag-monitoring/create-clean-project/Images/three_dot_menu_clean_btn_sp.png" | relative_url }})

    The **Create Clean Project** pane opens for you to configure the clean project. Note that the **Filters** section is already filled in so that the project is targeted at records with the selected tag.

1. On the **Configure** tab, do the following:

    1. Enter the name of the clean project.

    1. If needed, add more **Filters** to narrow down the scope of data targeted by the clean project.

        ![create_project_pane_configure_tab.png]({{ "/assets/images/governance/tag-monitoring/create-clean-project/Images/create_project_pane_configure_tab.png" | relative_url }})

    1. Select **Next**.

1. On the **Choose Vocabulary Keys** tab, do the following:

    1. Review the list of properties and vocabulary keys pre-selected for this clean project. If needed, remove any of the properties or keys.

        ![remove_property_btn.png]({{ "/assets/images/governance/tag-monitoring/create-clean-project/Images/remove_property_btn.png" | relative_url }})

    1. If you want to load more properties or vocabulary keys into the project, select **Add Property**. Then choose what type of property—record property or vocabulary property—you want to load to the clean project.

        ![add_property_dropdown.png]({{ "/assets/images/governance/tag-monitoring/create-clean-project/Images/add_property_dropdown.png" | relative_url }})

        Depending on the type of property that you chose, select the record properties or find and select the vocabulary keys that you want to load to the clean project. Then, select **Save Selection**.

    1. Select **Create**.

    You created the clean project from the Tag Monitoring module. The next step is to [generate results](/preparation/clean/manage-clean-project#generate-results) of the clean project.

## Add new tags

The **Tag Monitoring** page lists all tags that are currently used in CluedIn. If this list is not sufficient, and you need new tags in place, you can create these tags directly from the **Tag Monitoring** page.

{:.important}
You can also use the [Rule Builder module](/management/rules) to create new tags. For a step-by-step walkthrough, see [Identifying and labelling incorrect data](/training/fundamentals/identifying-and-labelling-incorrect-data).

**To add tags from the Tag Monitoring page**

1. On the navigation pane, go to **Governance** > **Tag Monitoring**.

    {:.important}
    If the **Tag Monitoring** module is not available, this may mean that the tag monitoring functionality is not [enabled](#enable-the-tag-monitoring-functionality).

1. In the upper-left corner of the page, select **Add Tag**.

    ![add_tag_btn.png]({{ "/assets/images/governance/tag-monitoring/add-new-tags/Images/add_tag_btn.png" | relative_url }})

    The **Add Tag** panel opens on the right of the page.

1. Enter a user-friendly **Tag Name**.

1. Select the **Type** of rule that will be created to apply the tag – data part rule or golden record rule. For details about these rules types, see:

    - [Data part rules](/management/rules/rule-types#data-parts-rules)

    - [Golden record rules](/management/rules/rule-types#golden-record-rules)

1. Use **Filters** to specify the subset or records to which the tag will apply.

    ![add_tag_panel.png]({{ "/assets/images/governance/tag-monitoring/add-new-tags/Images/add_tag_panel.png" | relative_url }})

1. Select **Create**.

    The tag, and the corresponding rule, are created. You can find the rule in the **Rule Builder** module:

    - The rule is active and will automatically apply the tag to new matching records.

    - If you want the rule to apply to existing records as well, on the **Add Tag** panel, select **Reprocess existing records**. Then, wait until the processing is completed.

        ![reprocess_golden_records.png]({{ "/assets/images/governance/tag-monitoring/add-new-tags/Images/reprocess_golden_records.png" | relative_url }})
