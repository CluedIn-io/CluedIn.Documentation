---
layout: cluedin
title: Create, configure, and run an AI agent
parent: AI agents
grand_parent: Management
nav_order: 030
permalink: /management/ai-agents/create-configure-and-run-an-ai-agent
tags: ["management", "ai agents", "create an ai agent", "configure an ai agent", "run an ai agent"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to create, configure, and run an AI agent tailored to your specific business needs.

## Create an AI agent

An AI agent is a component that uses artificial intelligence to analyze data, provide suggestions, and perform actions on your golden records. It consists of jobs—operational units within an AI agent that define what the agent should do.

**To create an AI agent**

1. On the navigation pane, go to **AI Agents** (or, **Management** > **AI Agents**).

1. Select **Create Agent**.

1. Enter a user-friendly **Name** of the AI agent.

1. Provide a user-friendly **Description** for the AI agent that helps everyone understand what the purpose of this AI agent is. This text will be displayed in the CluedIn UI.

1. Provide **Instructions** for the AI agent. Think of instructions as a job description that tells your AI agent what you’d like it to do. For example, **Fix incorrect date formats** or **Check for out-of-range transaction amounts**.

    {:.important}
    These instructions will apply to all [jobs](#configure-an-ai-agent-job) that the AI agent performs (this way, you won't have to repeat the instructions in each job).

    ![create_agent_pane.png]({{ "/assets/images/management/ai-agents/create-an-ai-agent/create_agent_pane.png" | relative_url }})

1. Select **Create**.

    After you created an AI agent, proceed to configure it by adding jobs.

## Configure an AI agent job

To enable an AI agent to perform a specific task, you must create and configure one or more **AI agent jobs**. A job defines a specific task assigned to the agent—such as detecting duplicates, identifying and resolving data quality issues, or generating rules—based on a specific set of golden records.

Setting up an AI agent job involves the following steps:

1. [Creating a job](#create-a-job) – add a new job for an AI agent.

1. [Adding a data source](#add-a-data-source) – specify a set of golden records the agent should operate on.
    
1. [Configuring the prompt](#configure-the-prompt) – define the instructions  the agent should follow to complete the task.

1. [Testing the job](#test-the-job) – verify the job’s setup by running a preliminary test on a subset of golden records to ensure the agent performs as expected.

1. [Running the job](#run-the-job) – execute the job on the full set of data according to the provided instructions to produce AI suggestions.

### Create a job

A job is the operational unit within an AI agent. It defines what the agent should do and which golden records it should work on.

**To create a job**

1. On the navigation pane, go to **AI Agents** (or, **Management** > **AI Agents**).

1. Select the AI agent for which you want to add a job.

1. Select **Create Job**.

1. Enter a user-friendly **Name** of the job.

1. Provide the **Description** of the job, focusing on the details about what this job will do, its purpose, or any special instructions.

1. Select the **Endpoint** that the job will use. This is the [API endpoint of a specific deployed AI model](/management/ai-agents/prerequisites-to-using-ai-agents#configure-a-model-endpoint) that your job will call to perform its task. Choosing the correct endpoint ensures the job uses the right AI capabilities.

    ![create_pane.png]({{ "/assets/images/management/ai-agents/create-ai-agent-job/create_pane.png" | relative_url }})

1. Select **Create**.

    Once you added a job, proceed to [add a data source](#add-a-data-source) to specify the set of golden records the job will operate on.

### Add a data source

A data source within a job refers to a specific set of golden records that the job will operate on. The data source defines the input data for the AI agent, ensuring that the job processes the correct records for a specific task.

**To add a data source**

1. On the navigation pane, go to **AI Agents** (or, **Management** > **AI Agents**).

1. Select the AI agent for which you added the job. Then, select the job.

1. On the **Configuration** tab of the job page, in the **Data** section, select **Add data source**.

    ![click_add_data_source_btn.png]({{ "/assets/images/management/ai-agents/add-a-data-source/click_add_data_source_btn.png" | relative_url }})

1. On the **Create Data Source** pane, do the following:

    1. Enter a user-friendly **Name** of the data source.

    1. If you want to limit the number of golden records in the data source, select the **Sampling** checkbox. Then, in **Sampling Size**, enter the desired number of records that you want to use.

    1. **Modified Since Last Run** – [TBD].

    1. In the **Conditions** section, add a [filter](/key-terms-and-features/filters) to define which golden records should be included in the data source.

    1. In the **Vocabulary Keys** section, select one or more vocabulary keys that the job will analyze and process.

    1. Select **Create**.

        ![create_data_source_pane.png]({{ "/assets/images/management/ai-agents/add-a-data-source/create_data_source_pane.png" | relative_url }})

    Once you added the needed data source, proceed to configure the prompt that the job should follow to complete the task.

### Configure a prompt

A prompt in an AI agent job is a set of instructions or natural language input that tells the AI agent what task to perform and how to perform it on the selected data source. It acts as the core logic of the job, guiding the AI agent’s behavior based on your business goals.

**To configure a prompt**

1. On the navigation pane, go to **AI Agents** (or, **Management** > **AI Agents**).

1. Select the AI agent for which you added the job. Then, select the job.

1. On the **Configuration** tab of the job page, in the **Skills** section, select the skill that the agent should use to perform the job.

    ![select_skill.png]({{ "/assets/images/management/ai-agents/configure-a-prompt/select_skill.png" | relative_url }})

1. In the **Instructions** section, enter a prompt instructing the agent what task it must perform.

    Then, select the data source on which the job should run. To do this, drag the needed data source from the **Data** section onto the **Instructions** section.

    ![prompt.png]({{ "/assets/images/management/ai-agents/configure-a-prompt/prompt.png" | relative_url }})

    Once you configured the prompt, test the job configuration to make sure that the results meet your expectations and the task is performed correctly.

### Test the job

Testing a job is an important step because it helps achieve the following:

- Ensure the agent performs accurately on a smaller subset of golden records, helping to catch errors early and prevent costly mistakes before processing the full data source.

- Validate that the job configuration and instructions align with the expected outcomes.

{:.important}
When you test the job, no changes are made to the your golden records. The purpose of testing is solely to provide a preview of the results that will be generated when the job is run.

**To test the job**

1. On the navigation pane, go to **AI Agents** (or, **Management** > **AI Agents**).

1. Select the AI agent for which you added the job. Then, select the job.

1. In the upper-right corner of the job page, select **Test Now**. The testing process may take some time depending on the amount of data to be processed.

    ![click_test_job_btn.png]({{ "/assets/images/management/ai-agents/test-a-job/click_test_job_btn.png" | relative_url }})

1. When testing is completed, review the testing results:

    1. Go to the **Runs** tab. Locate the job run with the **Test** label and the time corresponding to when you did the test run. Wait until the test run status is **Completed**.

        ![locate_the_test_run.png]({{ "/assets/images/management/ai-agents/test-a-job/locate_the_test_run.png" | relative_url }})

    1. Select the test run. You can now review the preliminary suggestions generated during the test run. The values that the AI agent suggested to change are highlighted in green.

        ![test_run_results.png]({{ "/assets/images/management/ai-agents/test-a-job/test_run_results.png" | relative_url }})

        {:.important}
        If the test run returns no results, try adjusting the job settings as described in [Troubleshoot an AI agent job](#troubleshoot-an-ai-agentjob).

    1. To view the AI agent suggestions, locate a cell highlighted in green. Then, hover over the information icon in that cell to view the current golden record value and how the AI agent suggests to change it.

        ![view_suggestion_details.png]({{ "/assets/images/management/ai-agents/test-a-job/view_suggestion_details.png" | relative_url }})

    Once you’re satisfied with the job configuration and preliminary suggestions generated by the AI agent, proceed to run the job.

### Run the job

Running a job is how you put your AI agent configuration into action, allowing you to generate tangible results that you can validate and apply. When you run the job, it processes the entire set of golden records defined in the job’s data source configuration. Depending on the size of the data and the AI model’s performance, the job can take anywhere from a few seconds to several hours to several days to complete.

You can run the job:

- Manually now.

- Automatically on a specific schedule. You can have the job running once every N hours or days.

**To run a job**

1. On the navigation pane, go to **AI Agents** (or, **Management** > **AI Agents**).

1. Select the AI agent for which you added the job. Then, select the job.

1. On the job page, turn on the status toggle to enable the job.

    ![enable_the_job.png]({{ "/assets/images/management/ai-agents/run-a-job/enable_the_job.png" | relative_url }})

1. To run the job now, in the upper-right corner of the job page, select **Run Now**.

    ![run_the_job.png]({{ "/assets/images/management/ai-agents/run-a-job/run_the_job.png" | relative_url }})

1. To run the job on a schedule, do the following:
 
    1. On the job page, go to the **Settings** tab.

    1. In the **Recurring Schedule** section, select **Enable**.

    1.  Specify the schedule for job. You can have the job running once every N hours, days, or minutes.

         ![specify_a_schedule.png]({{ "/assets/images/management/ai-agents/run-a-job/specify_a_schedule.png" | relative_url }})

1. In the upper-right corner of the job page, select **Save**.

     When the job completes, you can proceed to [review the results](/management/ai-agents/review-the-results-returned-by-an-ai-agent) returned by an AI agent.

### Troubleshoot an AI agent job

If, after configuring and testing the prompt, the **Test History** pane doesn't display any suggestions, the AI agent might be using an incorrect endpoint to communicate with the deployed AI model on the platform. You can fix this by selecting another endpoint for the AI agent configuration.

**To troubleshoot an AI agent job**

1. On the navigation pane, go to **AI Agents** (or, **Management** > **AI Agents**).

1. Select the AI agent for which you added the job. Then, select the job.

1. On the job page, go to the **Settings** tab.

1. In the **Endpoint** list, select the endpoint that you want to use for the AI agent.

    ![select_endpoint.png]({{ "/assets/images/management/ai-agents/troubleshoot-a-job/select_endpoint.png" | relative_url }})

1. In the upper-right corner of the job page, select **Save**.

    You can now retest and rerun the job.