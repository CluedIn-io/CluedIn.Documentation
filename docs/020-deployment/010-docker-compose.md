---
layout: default
title: Local
parent: Installation
nav_order: 2
permalink: /deployment/local
has_children: true
tags: ["deployment", "docker", "docker-compose", "local-deployment"]
last_modified: 2023-06-30
---

Learn how to run CluedIn locally and prepare to stream data to Microsoft SQL Server databases.

<div style='padding:58.42% 0 0 0;position:relative;'>
<iframe src="https://player.vimeo.com/video/842179773?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="AMA_installation_overview_video_upd"></iframe>
</div>

CluedIn is being developed with a cloud-centric approach, which means that running CluedIn locally can pose some challenges. The local installation of CluedIn does not provide all the features available in cloud environment, such as auto-scaling, auto-restart, logging, monitoring, and more. However, you may still consider installing CluedIn locally for the following reasons:

- **Cost efficiency**. Running CluedIn in Azure incurs expenses, and for the purpose of simple testing, you may prefer to avoid these costs.

- **Writing CluedIn extensions**. CluedIn is very flexible and can be extended through custom code. If you want to extend CluedIn by writing code, you can test your extensions locally within CluedIn, making the testing process easier.

- **No need to be Administrator in Azure**. Running CluedIn in Azure requires elevated permissions within the Azure platform, which you might not have. Thus, having the ability to run CluedIn locally provides you with the advantage of evaluating, customizing, and developing with CluedIn without the need to deal with permissions in Azure.

This section provides you with instructions on how to **run CluedIn locally with the SQL Server Connector extension**.