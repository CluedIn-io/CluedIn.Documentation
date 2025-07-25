---
layout: cluedin
nav_order: 1
parent: Configuration
grand_parent: PaaS operations
permalink: deployment/infra-how-tos/connect-to-cluedin
title: Connect to CluedIn cluster
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
headerIcon: "paas"
---

[Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview) provides an effective environment and the tools you need to interact with your AKS cluster without significant configuration or effort.

**To connect to your CluedIn cluster in Azure Cloud Shell**

1. In the Azure portal, navigate to your AKS resource.

1. On the menu bar, select **Connect**.

    ![connect-to-cluedin-1.png]({{ "/assets/images/ama/howtos/connect-to-cluedin-1.png" | relative_url }})

    In the right pane, you'll see the connection details and instructions that you can use to connect to your CluedIn cluster.

    ![connect-to-cluedin-2.png]({{ "/assets/images/ama/howtos/connect-to-cluedin-2.png" | relative_url }})

For additional details, please refer to [Microsoft Documentation](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal?tabs=azure-cli#connect-to-the-cluster).