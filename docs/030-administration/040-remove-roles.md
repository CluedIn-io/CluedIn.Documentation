---
layout: cluedin
nav_order: 1
parent: Roles
grand_parent: Administration
permalink: /administration/roles/remove-roles
title: Remove roles
tags: ["administration", "roles"]
---

In this article, you will learn how to remove roles from users so that they are restricted from performing certain operations in CluedIn.

**_This article is intended for users with the OrganizationAdmin role or users with the following claim access levels._**

| Section | Claim | Access level |
|--|--|--|
| Admin | Users | At least Consulted |
| Admin | Roles | At least Consulted |

The following diagram shows the flow of removing roles from users.

![remove-role-diagram.png](../../assets/images/administration/roles/remove-role-diagram.png)

**To remove roles from a user**

1. On the navigation pane, go to **Administration** > **Roles**. Then, select the needed role.

    Alternatively, you can go to **Administration** > **User Management** > **Users**. Select a user, go to the **Roles** tab, and then select the role that you want to remove from the user.

1. Go to the **Users** tab.

1. Select the checkbox next to the user whom you want to remove from the role.

1. Select **Remove from role**, and then confirm your choice.

    ![remove-role-1.png](../../assets/images/administration/roles/remove-role-1.png)

    The role is removed from the user. The user will receive an email about the role changes. For the changes to take the effect, the users have to sign out and sign in again.