---
layout: cluedin
title: Administration Operations
parent: Legacy development documentation
grand_parent: Archive
nav_order: 20
permalink: /archive/legacy-development/administration-operations
content_type: reference
redirect_from: ["/development/administration-operations"]
source_path: docs/090-development/020-administration-operations.md
tags: ["development","administration"]
published: false
---

You will need to have a role of "Admin" to be able to run these operations. There is only one way to become an Admin and that is by manually adding a mapping in the Relational Store of CluedIn in the AspnetUserRoles table. 

## Post Processing

There are many times within CluedIn where you need to apply an operation on data that already exists within your datastores. This will typically happen when you need to change the values of data in bulk. The Post Processing Admin Endpoint will allow you to run a Post Processing operation which will load all matching data into a queue called PostProcessing and will run the full post processing operation including all custom and included Post Processors of CluedIn.