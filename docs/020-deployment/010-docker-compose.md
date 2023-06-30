---
layout: default
title: Local
parent: Installation
nav_order: 2
permalink: /deployment/docker-compose
tags: ["deployment", "docker", "docker-compose", "local-deployment"]
last_modified: 2023-06-30
---

CluedIn is being developed with a cloud-centric approach, which means that running CluedIn locally can pose some challenges. The local installation of CluedIn does not provide all the features available in cloud environment, such as auto-scaling, auto-restart, logging, monitoring, and more. However, you may still consider installing CluedIn locally for the following reasons:

- **Cost efficiency**. Running CluedIn in Azure incurs expenses, and for the purpose of simple testing, you may prefer to avoid these costs.

- **Writing CluedIn extensions**. CluedIn is very flexible and can be extended by writing code. If you need to write code to extend CluedIn, you will most likely want to test your extensions locally within CluedIn to avoid complex deployment mechanism for testing your code.

- **No need to be Administrator in Azure**. Running CluedIn in Azure requires elevated permissions within the Azure platform, which you might not have. Thus, having the ability to run CluedIn locally provides you with the advantage of evaluating, customizing, and developing with CluedIn without the need to deal with permissions in Azure