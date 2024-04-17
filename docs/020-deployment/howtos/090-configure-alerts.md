---
layout: cluedin
nav_order: 10
parent: How-to guides for PaaS
grand_parent: Installation
permalink: /deployment/infra-how-tos/configure-alerts
title: Configure alerts
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-23
headerIcon: "paas"
---

By default, CluedIn contains built-in alerts that are sent to our support team.

![Alerts.png](../../assets/images/ama/howtos/configure-alerts-1.png)

If you need to set up additional alerts or modify the existing configuration of alerts, you can do it your CluedIn AKS cluster.

**To configure additional alerts**

1. In the Azure portal, navigate to the needed AKS cluster.

1. In the left pane, under **Monitoring**, select **Alerts**.

    ![alerts.png](../../assets/images/ama/howtos/configure-alerts-2.png)

    You will see the alerts for your CluedIn AKS cluster.
    
1. To configure additional alerts, create a new alert rule and set the actions for the alerts rule as described in [Microsoft documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-new-alert-rule?tabs=metric).