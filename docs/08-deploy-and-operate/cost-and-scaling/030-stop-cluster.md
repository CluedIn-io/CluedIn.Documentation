---
layout: cluedin
title: Stop AKS cluster to reduce cost
parent: Cost and scaling
grand_parent: Deploy & operate
nav_order: 30
permalink: /operate/cost-and-scaling/stop-cluster
content_type: how-to
redirect_from: ["/kb/stop-cluster"]
source_path: docs/200-kb/kb0012-stop-aks-cluster.md
tags: ["AKS", "cost saving"]
published: false
---

Stopping the AKS cluster reduces costs, but you will still pay for other resources such as storage, networking, and so on. However, the overall cost will be significantly reduced.

If you want to stop your Kubernetes cluster (AKS) from running, follow the steps outlined in this article.

**To stop AKS cluster**

1. Navigate to https://portal.azure
1. Search for the Managed Resource Group (MRG) that houses your CluedIn instance.
1. Select the Kubernetes service resource. It usually starts with `aks-` followed by a unique string.
1. At the top, select **Stop**, which should then begin to power down your instance.

If you require any further assistance, reach out to CluedIn support.