---
layout: cluedin
title: Job monitoring
parent: Monitoring
grand_parent: Deploy & operate
nav_order: 40
permalink: /operate/monitoring/job-monitoring
content_type: how-to
redirect_from: ["/management/job-monitoring"]
tags: ["management", "monitoring", "jobs", "operations"]
last_modified: 2026-11-20
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Active jobs** and **History** tabs of the **Jobs** page provide a central view of jobs running across your CluedIn environment.

Use it to track the **status, progress, and outcome** of background work, including both recurring scheduled jobs and jobs started by other CluedIn features.

They sit next to the **Manage jobs** tab on the same [Jobs](/administer/jobs) page:

- **Manage jobs** is where you define and schedule recurring work.
- **Active jobs** and **History** are where you observe job executions across the environment.

Job monitoring therefore includes more than user-created schedules. Depending on activity in your environment, you can see system jobs, scheduled jobs, deduplication processing, record operations, and other background work.

## Open job monitoring

On the navigation pane, go to **Management** > **Jobs**, then select one of these tabs:

- **Active jobs** – work that is currently running.
- **History** – completed and previous job executions.

Older links to the standalone Monitoring page still work.

Together, these views let you understand both what CluedIn is doing now and what has happened previously.

## Active jobs

Use the **Active jobs** tab to monitor work that is currently executing.

This view is useful when you want to:

- Confirm that a requested operation has started.
- Track long-running background work.
- See which jobs are currently consuming processing time.
- Investigate work that appears to be taking longer than expected.
- Identify who or what initiated an active operation.

The information shown for a job can depend on the type of operation being executed.

When a job finishes, its execution becomes available in **History**.

## Job history

The **History** tab provides an audit-style view of previous job executions.

For each execution, the list can show:

- **Job** – the name of the operation that ran.
- **Kind** – the category of job, such as a system-scheduled job or a deduplication project.
- **Initiated by** – the user or system process that started the job.
- **Status** – the outcome or current terminal state of the execution.
- **Started** – when execution began.
- **Finished** – when execution ended.
- **Duration** – how long the execution took.

Where available, the job name can link back to the originating object, such as a scheduled job, rule, or project, so that you can inspect its configuration. Jobs that relate to another object, such as a rule processing job, also offer a **view job details** callout. It shows the job's own name, state, progress and, for a failed job, the failure reason.

This makes History useful both for day-to-day operations and for troubleshooting questions such as:

- Did this job actually run?
- When did it start and finish?
- Did it complete successfully?
- Was it initiated by a user or by the system?
- Which project or scheduled job caused this execution?
- How long did it take?

## Job status

The **Status** column provides a quick indication of the execution state.

For example, a completed operation can be shown as **Done**.

Active jobs can display an in-progress state while work is still executing. A job that is being cancelled shows a stopping state until cancellation finishes.

A job that a user stopped is shown as **Cancelled**. **Failed** means the job stopped because of an error. Hover over the **Failed** badge to see the failure reason, so you can often diagnose the problem without contacting support.

Use the status together with the start and finish times to understand whether a job completed normally or still requires investigation.

## Filter monitored jobs

History can contain a large number of executions, particularly in environments with frequent scheduled or system activity.

Use the filters at the top of the page to narrow the list.

### Status

Use **All statuses** to filter jobs by their execution state.

This is useful when you want to focus only on failed, completed, running, or other relevant states.

### Initiated by

Use **Initiated by** to distinguish work started by:

- A particular user.
- The CluedIn system.
- Other available initiators.

This is useful for separating manually initiated work from automated background processing.

### Kind

Use **All kinds** to filter by the type of job.

Examples can include:

- System scheduled jobs.
- User-scheduled jobs.
- Deduplication project jobs.
- Record processing or modification jobs.
- Other background operations exposed through the CluedIn job framework.

The job kinds available depend on the operations that have run in your environment.

### Started date

Use the **Started at** and date controls to restrict history to jobs that began during a particular period.

This is particularly useful when investigating an incident or checking activity during a known deployment, import, or processing window.

## Understand system jobs

Some entries in **Active jobs** and **History** are created by CluedIn itself.

These jobs are typically marked as being initiated by **System** and can include recurring maintenance or metric-processing operations.

For example, the environment can run system jobs that:

- Recompute metrics.
- Archive older metric values.
- Trim high-time-resolution metric data.
- Perform other recurring internal maintenance.

System jobs are visible so administrators can understand what background work is taking place and verify that recurring platform operations are completing successfully.

## Monitor scheduled jobs

Jobs created in [Management > Jobs](/administer/jobs) appear in **Active jobs** and **History** when they execute.

The **Manage jobs** tab tells you how the recurring job is configured, including its schedule and next run.

**Active jobs** and **History** tell you what happened during each actual execution.

For example:

1. A rule reprocessing job is configured to run every night.
2. The **Manage jobs** tab shows the schedule and next expected run.
3. When the schedule triggers, the execution appears under **Active jobs**.
4. After it finishes, the run remains available in **History** with its status, start time, finish time, and initiator.

This separation makes it possible to manage schedules without losing visibility into individual runs.

## Monitor jobs started by CluedIn features

Not every monitored job originates from the Jobs scheduler.

Other features can start background jobs as part of their normal operation.

For example, a deduplication project can create jobs to:

- Find potential duplicate records.
- Generate deduplication results.
- Merge approved duplicate groups.

These executions can appear in **Active jobs** and **History** with the relevant project as the job kind or source.

This provides a single operational view instead of requiring administrators to visit every module independently to understand what work has run.

## Use job monitoring for troubleshooting

When an operation does not appear to have completed as expected, the **Active jobs** and **History** tabs are a useful first place to investigate.

A typical troubleshooting workflow is:

1. Open **Management** > **Jobs**.
2. Check **Active jobs** to see whether the operation is still running.
3. If it is no longer active, open **History**.
4. Filter by status, initiator, kind, or start date.
5. Find the execution and review its start time, finish time, duration, and status.
6. Follow the job link, where available, to inspect the originating scheduled job or project.

This helps distinguish between an operation that never started, one that is still running, and one that already completed.

## Jobs page tabs

The three tabs of the Jobs page are complementary.

| Tab | Purpose |
|--|--|
| **Management > Jobs > Manage jobs** | Create recurring work, define schedules, and manage scheduled or on-demand job definitions. |
| **Management > Jobs > Active jobs** | See background work currently running across the environment. |
| **Management > Jobs > History** | Review previous executions, outcomes, initiators, and timings. |

For information about defining scheduled rule reprocessing and batch GraphQL actions, see [Jobs](/administer/jobs).
