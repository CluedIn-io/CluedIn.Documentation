---
layout: cluedin
title: Network
parent: Administer
nav_order: 90
permalink: /administer/network
content_type: reference
tags: ["administration", "network", "connectivity", "ip addresses"]
last_modified: 2026-11-07
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

**Network & connectivity** (available from the administration menu as **Network**) shows read-only information about your CluedIn cluster's network, and lets you test whether the cluster can reach a specific destination. A summary row at the top of the page shows the cluster, region, network range (CIDR) and outbound IPs at a glance; the cards below give the full detail.

## Cluster details

The **Cluster details** card shows your CluedIn cluster's region, network range (CIDR), and inbound and outbound IP address(es). The region is shown as a friendly name with its underlying Azure region key alongside it, for example **Australia East (australiaeast)** — the same format is used everywhere the region appears on the page, including the **Cluster location** map, which plots the region's approximate location. Outbound IP addresses are useful when a customer's export target needs to allowlist CluedIn's traffic — see, for example, the [Snowflake connector](/publish/export-targets/snowflake-connector) documentation. Inbound IP addresses are useful when an external system needs to allowlist traffic it receives from CluedIn, such as a webhook callback.

![The Network & connectivity page, showing the summary tiles, the Cluster details card with the region map, and the Test outbound connectivity card]({{ "/assets/images/administration/network/network-page.png" | relative_url }})

### Test outbound connectivity

The **Test outbound connectivity** card lets you check, directly from CluedIn, whether the cluster can reach a specific destination host and port — without having to cross-reference the outbound IP addresses above against a customer's firewall rules yourself, or open a support ticket to confirm.

Enter a destination **host or IP address** and a **port**, then select **Test connection**. CluedIn's server resolves the host via DNS, then attempts a TCP connection to the destination on the given port, and reports the result as a notification:

- **Success** shows the resolved IP address and the connection latency in milliseconds.
- **Failure** shows the reason, such as a timeout or a refused connection.

The test only checks DNS resolution and the TCP connection — it does not perform a TLS handshake or send any application-level data, and it never changes a firewall rule or allowlist.

The destination must resolve to a publicly routable address. A destination that resolves to a loopback, private-network, link-local, or cloud metadata address (for example `169.254.169.254`) is rejected before CluedIn attempts a connection, so the test cannot be used to probe the cluster's own internal network. The test is also rate-limited per organization to prevent it being used to scan ports on other systems; if you hit the limit, wait a minute and try again.
