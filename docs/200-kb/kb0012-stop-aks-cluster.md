---
layout: cluedin
title: Stop AKS cluster to reduce cost
parent: Knowledge base
permalink: /kb/stop-cluster
tags: ["AKS", "cost saving"]
nav_order: 13
---

In the event you would like to stop your Kubernetes cluster (AKS) from running, you can perform this action by doing the following:

1. Navigate to https://portal.azure
1. Search for the Managed Resource Group (MRG) that house your CluedIn instance
1. Click on the Kubernetes service resource. Normally starting `aks-` followed by a unique string
1. Within here, click on Stop at the top which should then begin to power down your instance.

Please note that whilst this does reduce cost, you will still pay for other resources such as storage, networking, etc. but the cost will be greatly reduced.

If you require any further assistance, please reach out to CluedIn support who will assist.