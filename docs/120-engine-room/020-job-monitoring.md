---
layout: cluedin
title: Job monitoring
parent: Engine Room
nav_order: 2
permalink: /engine-room/job-monitoring
tags: ["engine room", "monitoring", "jobs", "operations"]
last_modified: 2026-09-24
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Monitoring** page in Engine Room provides a central view of jobs running across your CluedIn environment.

Use it to track the **status, progress, and outcome** of background work, including both recurring scheduled jobs and jobs started by other CluedIn features.

This is different from the [Jobs](/management/jobs) page:

- **Management > Jobs** is where you define and schedule recurring work.
- **Engine room > Monitoring** is where you observe job executions across the environment.

Monitoring therefore includes more than user-created schedules. Depending on activity in your environment, you can see system jobs, scheduled jobs, deduplication processing, record operations, and other background work.

## Open Monitoring

On the navigation pane, go to **Engine room** > **Monitoring**.

The page contains two main tabs:

- **Active jobs** – work that is currently running.
- **History** – completed and previous job executions.

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

Where available, the job name can link back to the originating object, such as a scheduled job or project, so that you can inspect its configuration.

This makes Monitoring useful both for day-to-day operations and for troubleshooting questions such as:

- Did this job actually run?
- When did it start and finish?
- Did it complete successfully?
- Was it initiated by a user or by the system?
- Which project or scheduled job caused this execution?
- How long did it take?

## Job status

The **Status** column provides a quick indication of the execution state.

For example, a completed operation can be shown as **Done**.

Active jobs can display an in-progress state while work is still executing.

Use the status together with the start and finish times to understand whether a job completed normally or still requires investigation.

## Filter monitored jobs

Monitoring can contain a large number of executions, particularly in environments with frequent scheduled or system activity.

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

Some entries in Monitoring are created by CluedIn itself.

These jobs are typically marked as being initiated by **System** and can include recurring maintenance or metric-processing operations.

For example, the environment can run system jobs that:

- Recompute metrics.
- Archive older metric values.
- Trim high-time-resolution metric data.
- Perform other recurring internal maintenance.

System jobs are visible so administrators can understand what background work is taking place and verify that recurring platform operations are completing successfully.

## Monitor scheduled jobs

Jobs created in [Management > Jobs](/management/jobs) appear in Monitoring when they execute.

The Management page tells you how the recurring job is configured, including its schedule and next run.

Monitoring tells you what happened during each actual execution.

For example:

1. A rule reprocessing job is configured to run every night.
2. **Management > Jobs** shows the schedule and next expected run.
3. When the schedule triggers, the execution appears under **Engine room > Monitoring**.
4. After it finishes, the run remains available in **History** with its status, start time, finish time, and initiator.

This separation makes it possible to manage schedules without losing visibility into individual runs.

## Monitor jobs started by CluedIn features

Not every monitored job originates from the Jobs scheduler.

Other features can start background jobs as part of their normal operation.

For example, a deduplication project can create jobs to:

- Find potential duplicate records.
- Generate deduplication results.
- Merge approved duplicate groups.

These executions can appear in Monitoring with the relevant project as the job kind or source.

This provides a single operational view instead of requiring administrators to visit every module independently to understand what work has run.

## Use Monitoring for troubleshooting

When an operation does not appear to have completed as expected, Monitoring is a useful first place to investigate.

A typical troubleshooting workflow is:

1. Open **Engine room** > **Monitoring**.
2. Check **Active jobs** to see whether the operation is still running.
3. If it is no longer active, open **History**.
4. Filter by status, initiator, kind, or start date.
5. Find the execution and review its start time, finish time, duration, and status.
6. Follow the job link, where available, to inspect the originating scheduled job or project.

This helps distinguish between an operation that never started, one that is still running, and one that already completed.

## Jobs and Monitoring

The Jobs and Monitoring pages are complementary.

| Page | Purpose |
|--|--|
| **Management > Jobs** | Create recurring work, define schedules, and manage scheduled or on-demand job definitions. |
| **Engine room > Monitoring > Active jobs** | See background work currently running across the environment. |
| **Engine room > Monitoring > History** | Review previous executions, outcomes, initiators, and timings. |

For information about defining scheduled rule reprocessing and batch GraphQL actions, see [Jobs](/management/jobs).
