---
layout: cluedin
title: Access control
parent: Management
nav_order: 060
has_children: true
permalink: /management/access-control
---

Access control gives you a fine-grained control over who can view specific golden records and vocabulary keys. Together with source control, access control helps you configure reliable and secure access to data in CluedIn. For more information about the combination of source control and access control, see [Data access](/administration/user-access/data-access).

**Limitations of access control**

Access control policies are not applied to the data in deduplication projects, clean projects, hierarchy projects, and manual merges. The reason is that the users who are processing groups of duplicates, cleaning data, creating hierarchies, or doing manual merges must be able to view all values to adequately execute their tasks.

{:.important}
When you enable access control for the first time, all users in your organization lose access to golden records. To restore their access, you must create access control policies and ensure users have permissions to the sources of the golden records. 

This section covers the following topics:

- [Create access control policy](/management/access-control/create-access-control-policy) – learn how to create and configure an access control policy.

- [Manage access control policies](/Documentation/Management/Access-control/Manage-access-control-policies) – learn how to edit, deactivate, and delete an access control policy, as well how these actions affect user access to data.
