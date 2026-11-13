---
layout: cluedin
title: Export targets
parent: Publish & consume
nav_order: 30
has_children: true
permalink: /publish/export-targets
content_type: landing
summary: An export target is the destination a stream writes to.
redirect_from: ["/consume/export-targets"]
source_path: docs/150-consume/040-export-targets.md
tags: ["consume","export-targets"]
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Export targets are used for connecting with an integration point (also referred to as target), enabling CluedIn to send records to it using a [stream](/publish/streams). Examples of integration points include the following:

- Business intelligence tools

- Data warehouse dimension tables

- Machine learning platforms

- Custom applications

- Databases

Here are two examples of how to build a new Export Target:

- [SQL Server](https://github.com/CluedIn-io/CluedIn.Connector.SqlServer)

- [Snowflake](https://github.com/CluedIn-io/CluedIn.Connector.Snowflake)

See the full list of public implementations of CluedIn Export Targets [here](https://github.com/CluedIn-io?q=connector).

In this article, you will learn how to configure and manage an export target that can receive records sent from CluedIn.

## Configure an export target

You can configure a predefined export target provided with CluedIn (such as SQL Server Connector or Azure Event Hub Connector). You can also write a custom connector using the CluedIn NuGet package; however, it requires C# knowledge and the actual external service.

**To configure an export target**

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

    The **Add Export Target** pane opens, where you can select and configure the needed export target.

1. On the **Choose Target** tab, select the external system you want to establish a connection with. Then, select **Next**.

1. On the **Configure** tab, enter the connection details. The list of fields that you need to complete depends on the selected export target. For example, for the Microsoft SQL Server export target, you need to provide the **Name**, **Host**, **Database Name**, **Username**, and **Password**.

1. Test the connection to make sure it works, and then select **Add**.

    If the test fails, select **Run diagnostics** instead of (or after) **Test Connection** to see which part of the connection is the problem. See [Diagnose a connection problem](#diagnose-a-connection-problem).

    ![Animation: selecting Add Export Target, choosing a target on the Choose Target tab, entering connection details on the Configure tab, testing the connection, and adding it]({{ "/assets/images/consume/export-targets/export-target-configuration.gif" | relative_url }})

    You configured the export target. Now, it can be attached to the stream. The user who added the export target is the owner of the export target.

## Diagnose a connection problem

When **Test Connection** fails, it only tells you that something is wrong, not what. Select **Run Diagnostics**, next to **Test Connection**, to break the connection attempt down into individual checks and see exactly which one failed. This is available wherever CluedIn connects to an external service - export targets, [enrichers](/govern/enrichment/add-enricher), and [AI platforms, deployments and endpoints](/govern/ai-agents/prerequisites-to-using-ai-agents) - and the checks are the same wherever it appears:

- **Gateway** – the diagnostics request reached the CluedIn server.
- **Outbound IP** – the public IP address(es) this CluedIn instance's own requests to the target come from, so you know what to add to the target's firewall allowlist. Shown when an administrator has configured it under **Administration** > **Network**; otherwise this check is skipped.
- **DNS** – the configured host name resolves.
- **Network** – the configured port is reachable.
- **TLS** – the certificate the target presents is trusted (only checked when the target negotiates TLS directly on its port).
- **Authentication** – the credentials are accepted.
- **Authorization** – the account has the permissions the connection needs (for example, to create and write to a table). Currently available for SQL Server-based export targets.
- **Sample read/write** – a minimal operation against the target succeeds: for a SQL Server-based export target, a read and write; for an AI deployment or endpoint, a real sample request sent through it.

Each check shows as succeeded, failed, or skipped. A check is skipped, rather than run, when an earlier check it depends on already failed — for example, if DNS resolution fails, the network, authentication, authorization, and sample read/write checks all show as skipped, because none of them can meaningfully run without a resolvable host. A skipped check tells you which earlier check blocked it, so you always know which one to fix first.

Not every check applies everywhere. TLS is skipped as not applicable when the target does not negotiate TLS directly on its port. Authorization and sample read/write currently run their full checks only for SQL Server-based export targets and for AI deployments and endpoints (as a real sample request); everything else still gets the network and authentication checks, with authorization and sample read/write reported as not applicable.

![Connectivity diagnostics dialog for a SQL Server export target, with Gateway, DNS, Network, Authentication, Authorization, and Sample read/write all succeeded, and TLS skipped as not applicable]({{ "/assets/images/consume/export-targets/connectivity-diagnostics.png" | relative_url }})

## Manage an export target

On the export target details page, you can do the following:

- Test the connection to the export target, or select **Run diagnostics** to see which part of the connection is failing. See [Diagnose a connection problem](#diagnose-a-connection-problem).

    ![Export target details page with Test connection, the Active toggle, and the Synchronized and Healthy status labels]({{ "/assets/images/consume/export-targets/export-targets-1.png" | relative_url }})

- View the streaming modes supported by the export target:

    - **Synchronized** – the records in the export target mirror the records in CluedIn.

    - **Event** – the records in the export target are written as events (for example, Create, Insert, Update, Delete) each time an action occurs in CluedIn.

- Activate and deactivate the export target. When activating or deactivating the export target, you can view the streams linked to it as well as start, pause, or stop the needed streams.

    ![Deactivate Export Target dialog listing linked streams with start, pause and stop controls, and the Deactivate button]({{ "/assets/images/consume/export-targets/export-targets-2.png" | relative_url }})

- Review the export target health checks.

    Health checks for the export target run every 60 seconds. If, for example, somebody has changed the password for the user connecting to the export target, the health check status would change to **Unhealthy**, letting you know that you need to check on the export target. After the issue is fixed, the status will go back to **Healthy** again. The **Partially Healthy** status indicates that some pods are reporting healthy and others are reporting unhealthy (for example, if there is a network issue where one pod is struggling to connect but the other pods can still connect).

    If the export target is **Unhealthy**, you cannot select it in the export target configuration for a stream. Additionally, if you have already configured the stream and the export target becomes **Unhealthy**, you cannot start such stream.

- Edit the connection details.
