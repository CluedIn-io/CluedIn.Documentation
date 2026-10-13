---
title: Access control
url: https://documentation.cluedin.net/administer/access-control
content_type: landing
section: Administer
---

# Access control

Access control gives you a fine-grained control over who can view and modify specific golden records. Together with source control, access control helps you configure reliable and secure access to golden records in CluedIn. For more information about the combination of source control and access control, see [Data access](https://documentation.cluedin.net/administer/users-and-roles/data-access.md).

**Limitations of access control**

Access control policies are not applied to the data in deduplication projects, clean projects, hierarchy projects, and manual merges. The reason is that the users who are processing groups of duplicates, cleaning data, creating hierarchies, or doing manual merges must be able to view all values to adequately execute their tasks.

> **Important:** When you enable access control for the first time, all users in your organization lose access to golden records. To restore their access, you must create access control policies and ensure users have permissions to the sources of the golden records. 

This section covers the following topics:

- [Create access control policy](https://documentation.cluedin.net/administer/access-control/create-access-control-policy.md) – learn how to create and configure an access control policy.

- [Manage access control policies](https://documentation.cluedin.net/administer/access-control/manage-access-control-policies.md) – learn how to edit, deactivate, and delete an access control policy, as well how these actions affect user access to data.

- [Access control reference](https://documentation.cluedin.net/administer/access-control/access-control-reference.md) – learn about the structure of an access control policy and the available actions in the policy rule.

## In this section

- [Create access control policy](https://documentation.cluedin.net/administer/access-control/create-access-control-policy.md) (how-to): In this article, you will learn how to create an access control policy to configure reliable and secure access to data in CluedIn.
- [Manage access control policies](https://documentation.cluedin.net/administer/access-control/manage-access-control-policies.md) (how-to): In this article, you will learn how to manage an access control policy and modify it when changes are required.
- [Access control reference](https://documentation.cluedin.net/administer/access-control/access-control-reference.md) (reference): In this article, you will find reference information about the structure of an access control policy and the actions available in the access control policy rule.

Up: [Administer](https://documentation.cluedin.net/administer.md)
