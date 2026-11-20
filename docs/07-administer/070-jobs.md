---
layout: cluedin
title: Jobs
parent: Administer
nav_order: 70
permalink: /administer/jobs
content_type: how-to
redirect_from: ["/management/jobs", "/development/one-time-jobs", "/development/recurring-time-jobs", "/development/scheduled-time-jobs"]
tags: ["management", "jobs", "scheduling", "rules", "graphql"]
last_modified: 2026-11-20
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Jobs** module lets you schedule recurring work in CluedIn and follow every job execution across your environment, in one place.

Jobs are useful for operations that need to happen repeatedly without a user manually starting them each time. For example, you can create scheduled jobs that:

- Reprocess rules.
- Run batch GraphQL actions against a selected set of records.
- Purge records that match a filter (**Retention and Purge**).

The Jobs page also contains system-provided jobs used by CluedIn for recurring platform work.

## Open the Jobs page

To open Jobs, go to **Management** > **Jobs**.

The page has three tabs:

- **Manage jobs** – the jobs defined in your environment, their schedules, and their recent run results.
- **Active jobs** – job executions that are running right now, across the whole environment.
- **History** – finished job executions, including ones that failed or were cancelled.

**Active jobs** and **History** cover more than the jobs listed under **Manage jobs**: they also show system jobs and background work started by other CluedIn features, such as deduplication projects. For details, see [Job monitoring](/operate/monitoring/job-monitoring).

![The Jobs page, showing the Manage jobs, Active jobs and History tabs]({{ "/assets/images/administration/jobs/jobs-page.png" | relative_url }})

On the **Manage jobs** tab, summary cards at the top of the page, summary cards show information such as:

- **All jobs** – total number of jobs.
- **Scheduled** – jobs configured to run on a schedule.
- **Paused** – scheduled jobs that are currently paused.
- **System provided** – recurring jobs supplied and managed by CluedIn.
- **On demand** – jobs that are not currently running on a recurring schedule.
- **Runs, last 24 hours** – recent successful and failed runs.
- **Runs, last 7 days** – run history for the previous seven days.

When any runs have failed, the red failed count is a link. Select it to open **History**, filtered to failed runs.

The job list shows information such as the job name, schedule, current status, last run, next run, and available actions.

You can search and filter the list to focus on jobs by status, type, creator, or action.

To run several jobs at once, select them using the checkboxes in the list, then select **Run _N_ jobs**. If your organization requires approval to run jobs, a request is sent for each selected job instead.

## Create a job

Select **Create job** to create recurring work.

A job combines two main concepts:

1. **Action** – what CluedIn should do.
2. **Schedule** – when CluedIn should do it.

The available action determines the configuration required by the job.

### Choose a schedule

Turn on **Enable recurring schedule**, then pick a preset:

- **Every few minutes** – runs every _N_ minutes. Starts at every 15 minutes; choose a different interval if needed.
- **Hourly** and **Daily** – run every _N_ hours or days.
- **Weekly** and **Monthly** – run once a week or once a month.
- **Custom** – edit the cron expression directly.

The panel previews the schedule in plain language and lists the next few run times. Schedules are evaluated in the server's time zone (UTC).

![Creating a job that runs every 5 minutes]({{ "/assets/images/administration/jobs/create-job-every-few-minutes.png" | relative_url }})

{:.important}
Pick an interval that leaves the job enough time to finish before its next run, especially for jobs that touch many records.

## Schedule rule execution

You can create a job that runs or reprocesses a rule on a recurring schedule.

This is useful when a rule should be evaluated periodically rather than only when records naturally pass through processing.

For example, you might schedule a rule to:

- Re-evaluate data quality conditions every night.
- Reapply classifications or tags on a regular basis.
- Reprocess a rule after upstream systems are expected to refresh their data.
- Periodically recalculate values that depend on time-sensitive business logic.

When creating the job, select the appropriate rule action, choose the rule to run, and configure the schedule.

The rule continues to use its existing filters and actions. The job controls **when** the rule is run; it does not replace the rule configuration itself.

For more information about rules, see [Rules](/govern/rules).

## Schedule batch GraphQL actions

Jobs can also schedule **batch GraphQL actions**.

GraphQL actions allow CluedIn to perform bulk operations against records returned by a query or filter. By placing that action inside a job, you can run the bulk operation repeatedly according to a schedule instead of starting it manually.

Examples of GraphQL actions include:

- Splitting matching entities.
- Deleting matching entities.
- Running post-processing.
- Recalculating entity metrics.
- Reprocessing edges.
- Running enrichment.

For the available GraphQL bulk actions and query examples, see [GraphQL actions](/publish/graphql/graphql-actions).

{:.important}
GraphQL actions can modify or reprocess large numbers of records. Review the query, filters, and action carefully before scheduling a recurring job.

### Example

Suppose you want to recalculate entity metrics for all Customer records every night.

The GraphQL action can target the required records:

```graphql
{
  search(query: "entityType:/Customer") {
    entries {
      actions {
        processEntityMetrics
      }
    }
  }
}
```

You can configure this as a Job and schedule it to run at the required interval.

This separates the **selection and operation logic** from the **schedule**:

- GraphQL defines which records are targeted and what action is performed.
- Jobs defines when the action runs.

## Purge records with Retention and Purge

A **Retention and Purge** job permanently deletes data from every record that matches the rule you configure. Use it to enforce data retention policies, for example removing records in a business domain once they reach a particular state.

When you create the job, define at least one condition under **Records to purge**. An empty rule would match every record, so the job can't be saved without one.

If a condition can't be evaluated when the job runs (for example, it refers to a value that no longer exists), CluedIn treats it as matching **no** records rather than all of them. In that case nothing is purged.

To see what the job did, open **View details** on the job. For a Retention and Purge job, this shows the configured filter and the latest run's outcome: how many records were purged, and how many failed.

{:.important}
Purged data can't be recovered from CluedIn. Review the filter carefully before saving the job, and consider running it on demand once before giving it a recurring schedule.

## Scheduled and on-demand jobs

Jobs can be used in different execution modes.

### Scheduled jobs

Scheduled jobs run automatically according to the configured recurrence.

The Jobs page displays:

- The schedule description.
- The most recent run.
- The next expected run.
- The current execution status.

This gives administrators a single place to confirm that recurring work is running as expected.

### On-demand jobs

A job can also represent work that is available to run without a recurring schedule.

This is useful when you want the job definition to be reusable but only want to start it when required.

## System-provided jobs

CluedIn also uses the Jobs framework for recurring platform operations.

These jobs are labelled **System** on the Jobs page so that they can be distinguished from jobs created by users.

Examples can include internal maintenance and metrics-processing jobs.

System-provided jobs make recurring platform activity visible in the same operational view as user-created work.

### Jobs that must run in order

Some system jobs depend on another job having run first. For example, **Archive metrics values** should run after **Global metrics** and **High time resolution metrics**, so it archives their finished values rather than a stale snapshot.

When a job has a dependency like this, its detail page shows a note explaining which jobs to run first. Follow that order if you start these jobs manually.

![The Archive metrics values job detail page, showing its ordering note]({{ "/assets/images/administration/jobs/job-ordering-note.png" | relative_url }})

## Monitor job execution

Use the Jobs page to monitor recurring work.

For each job, you can review:

- **Schedule** – how often the job runs.
- **Job status** – whether the job is idle, running, paused, or in another execution state.
- **Last run** – when the most recent execution occurred.
- **Next run** – when the next scheduled execution is expected.
- **Action** – the operation performed by the job.

The summary cards for the last 24 hours and last 7 days help you quickly identify whether scheduled work is succeeding or failing.

A run that you or another user stopped is shown as **Cancelled**, not **Failed**. A run shown as **Failed** stopped because of an error. Hover over its **Failed** badge to see the failure reason.

If a job is not behaving as expected, review the job configuration, action, schedule, and recent run information before changing the underlying rule or GraphQL operation. To follow individual executions, use the **Active jobs** and **History** tabs.

## Pause and resume scheduled work

When recurring work should temporarily stop, pause the job rather than deleting it.

Pausing preserves the job configuration but prevents the schedule from starting new executions.

This is useful during:

- Deployment or maintenance windows.
- Data migrations.
- Investigation of a failing job.
- Temporary suspension of an upstream or downstream process.

Resume the job when scheduled execution should continue.

## Jobs compared with rules and GraphQL

Jobs do not replace rules or GraphQL actions.

They provide a scheduling and operational layer around those capabilities.

| Capability | Purpose |
|--|--|
| **Rule** | Defines the conditions and actions that should be applied to data. |
| **GraphQL action** | Defines a bulk operation to perform against selected records. |
| **Job** | Defines when the rule or batch operation should run and provides execution monitoring. |

This separation allows the same rule or bulk action logic to be managed independently from its execution schedule.
