---
layout: cluedin
title: Access Control
parent: Unsupported features
grand_parent: Archive
nav_order: 10
permalink: /archive/unsupported-features/access-control
content_type: reference
redirect_from: ["/governance/access-control"]
source_path: docs/070-governance/outdated/010-access-control.md
tags: ["governance","access-control"]
published: false
---

CluedIn can enable or disable Read access at a datasource level. If you require more granular level security control, please talk to your CluedIn Account Manager to discuss the options. 

Access Control in CluedIn dictates if certain data is visible to a particular account/user/group in the CluedIn Data Hub. 

By default, Read access is denied to all users except the user that was the original user to integrate a particular source. CluedIn requires an opt-in policy on read access. 

![Diagram](/assets/images/governance/integration-level-access.png)  

You have two ways to apply access control within CluedIn. The first is by visiting a particular user and setting which data sources that user has access to.  The other is by selecting a particular integration source and setting which users have read access to the integration point. 

Step 1: Navigate to your Integrations page. 

Step 2: Click on the integration you are wanting to change permissions for and you will see an "Access" button.

![Diagram](/assets/images/governance/set-access-for-user.png)  

Step 3: Click on this access button and choose the users or roles that you would like to grant read access too. 

![Diagram](/assets/images/governance/user-level-access.png)  