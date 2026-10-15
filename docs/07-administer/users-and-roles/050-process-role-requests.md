---
layout: cluedin
title: Process role requests
parent: Users and roles
grand_parent: Administer
nav_order: 50
permalink: /administer/users-and-roles/process-role-requests
content_type: how-to
redirect_from: ["/administration/roles/process-role-requests"]
source_path: docs/030-administration/050-process-role-requests.md
tags: ["administration", "roles"]
---

In this article, you will learn how to process the role requests you receive from users to grant them the access they need.

When users are browsing CluedIn and find that they do not have access to certain sections or modules, they can send a request to get access. When this happens, you'll receive a new role request notification.

![New Role request notification saying someone requested consume.streams, with a View Request link]({{ "/assets/images/administration/roles/role-request-2.png" | relative_url }})

The following diagram shows the flow of processing role requests.

![Flow: an authorized user sends an access request; the CluedIn administrator receives it, chooses a role and grants access; the user receives an approval notification, then signs out and in to get the new role]({{ "/assets/images/administration/roles/role-request-diagram.gif" | relative_url }})

**To process a role request**

1. In the upper-right corner, select the ellipsis button, and then select **My Tasks**.

1. Select **Role Requests**, and then find the needed request.

1. In the **Actions** column, select **Grant Access**.

    The dialog opens where you can view the details of the access request.

1. In the **Granting Access To** dialog box, do the following:

    1. Review the access level and select another level if necessary.

        The information message below the selected access level helps you understand the permissions that will be granted to the user.

    1. Select a role to assign to the user.

        ![Granting Access To consume.streams dialog with (a) the access level Consulted and (b) the role DataArchitect selected, and the Grant Access button]({{ "/assets/images/administration/roles/role-request-1.png" | relative_url }})

    1. In the lower-right corner, select **Grant Access**.

    The user will receive a notification about the role changes. For the changes to take effect, the user has to sign out and sign in again.