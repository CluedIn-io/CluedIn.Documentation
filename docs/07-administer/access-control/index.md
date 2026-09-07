---
layout: cluedin
title: Access control
parent: Administer
nav_order: 30
has_children: true
permalink: /administer/access-control
content_type: landing
summary: Access control policies decide which golden records and which properties a role can see.
list_children: false
redirect_from: ["/management/access-control"]
source_path: docs/080-management/050-access.control.md
---

Access control gives you a fine-grained control over who can view and modify specific golden records. Together with source control, access control helps you configure reliable and secure access to golden records in CluedIn. For more information about the combination of source control and access control, see [Data access](/administer/users-and-roles/data-access).

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1069492038?h=2867233786&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Actions in access control policy rules"></iframe>
</div>

**Limitations of access control**

Access control policies are not applied to the data in deduplication projects, clean projects, hierarchy projects, and manual merges. The reason is that the users who are processing groups of duplicates, cleaning data, creating hierarchies, or doing manual merges must be able to view all values to adequately execute their tasks.

{:.important}
When you enable access control for the first time, all users in your organization lose access to golden records. To restore their access, you must create access control policies and ensure users have permissions to the sources of the golden records. 

This section covers the following topics:

- [Create access control policy](/administer/access-control/create-access-control-policy) – learn how to create and configure an access control policy.

- [Manage access control policies](/administer/access-control/manage-access-control-policies) – learn how to edit, deactivate, and delete an access control policy, as well how these actions affect user access to data.

- [Access control reference](/administer/access-control/access-control-reference) – learn about the structure of an access control policy and the available actions in the policy rule.
