---
title: Alerts
url: https://documentation.cluedin.net/operate/configuration/configure-alerts
content_type: how-to
section: Deploy & operate > Configuration
---

# Alerts

> how-to: Steps to accomplish one task.

By default, CluedIn contains built-in alerts that are sent to our support team.

![List of built-in metric alert rules, such as node CPU utilization above 80, container memory usage above 95, and pod in failed state](https://documentation.cluedin.net/assets/images/ama/howtos/configure-alerts-1.png)

If you need to set up additional alerts or modify the existing configuration of alerts, you can do it your CluedIn AKS cluster.

**To configure additional alerts**

1. In the Azure portal, navigate to the needed AKS cluster.

1. In the left pane, under **Monitoring**, select **Alerts**.

    ![Azure portal AKS cluster menu with Alerts highlighted under Monitoring](https://documentation.cluedin.net/assets/images/ama/howtos/configure-alerts-2.png)

    You will see the alerts for your CluedIn AKS cluster.

1. To configure additional alerts, create a new alert rule and set the actions for the alerts rule as described in [Microsoft documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-new-alert-rule?tabs=metric).

Up: [Configuration](https://documentation.cluedin.net/operate/configuration.md)
