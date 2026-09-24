---
layout: cluedin
title: Jobs
parent: Management
nav_order: 80
permalink: /management/jobs
tags: ["management", "jobs", "scheduling", "rules", "graphql"]
last_modified: 2026-09-24
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Jobs** module lets you schedule recurring work in CluedIn and monitor when that work runs.

Jobs are useful for operations that need to happen repeatedly without a user manually starting them each time. For example, you can create scheduled jobs that:

- Reprocess rules.
- Run batch GraphQL actions against a selected set of records.

The Jobs page also contains system-provided jobs used by CluedIn for recurring platform work.

## Open the Jobs page

To open Jobs, go to **Management** > **Jobs**.

The page gives you an operational overview of scheduled work and recent executions.

At the top of the page, summary cards show information such as:

- **All jobs** – total number of jobs.
- **Scheduled** – jobs configured to run on a schedule.
- **Paused** – scheduled jobs that are currently paused.
- **System provided** – recurring jobs supplied and managed by CluedIn.
- **On demand** – jobs that are not currently running on a recurring schedule.
- **Runs, last 24 hours** – recent successful and failed runs.
- **Runs, last 7 days** – run history for the previous seven days.

The job list shows information such as the job name, schedule, current status, last run, next run, and available actions.

You can search and filter the list to focus on jobs by status, type, creator, or action.

## Create a job

Select **Create job** to create recurring work.

A job combines two main concepts:

1. **Action** – what CluedIn should do.
2. **Schedule** – when CluedIn should do it.

The available action determines the configuration required by the job.

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

For more information about rules, see [Rules](/management/rules).

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

For the available GraphQL bulk actions and query examples, see [GraphQL actions](/consume/graphql/graphql-actions).

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

## Monitor job execution

Use the Jobs page to monitor recurring work.

For each job, you can review:

- **Schedule** – how often the job runs.
- **Job status** – whether the job is idle, running, paused, or in another execution state.
- **Last run** – when the most recent execution occurred.
- **Next run** – when the next scheduled execution is expected.
- **Action** – the operation performed by the job.

The summary cards for the last 24 hours and last 7 days help you quickly identify whether scheduled work is succeeding or failing.

If a job is not behaving as expected, review the job configuration, action, schedule, and recent run information before changing the underlying rule or GraphQL operation.

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
