---
layout: cluedin
title: Impersonate a user
parent: Users and roles
grand_parent: Administer
nav_order: 95
permalink: /administer/users-and-roles/impersonate-user
content_type: how-to
tags: ["administration", "users"]
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Impersonation lets an OrganizationAdmin temporarily view CluedIn exactly as another user in the organization sees it - to confirm that user's permission and RACI setup, or to reproduce an access issue they reported - without knowing their password, and without logging out of your own account.

**_This article is intended for users with the OrganizationAdmin role._**

| Section | Claim | Access level |
|--|--|--|
| Admin | Users | OrganizationAdmin role required |

## Prerequisites

- You must have the OrganizationAdmin role. Impersonation is not available to any other role, regardless of claim access level. For more information, see [Roles](/administer/users-and-roles/roles).
- The user you want to impersonate must belong to your organization. You cannot impersonate yourself.

## Start impersonating a user

1. On the navigation pane, go to **Administration** > **User Management**.

1. On the **All users** page, find the user you want to impersonate.

1. In the **Impersonate** column, select **Impersonate**.

    ![The All users page with a Name, Roles, Active, and Impersonate column; an Impersonate link appears next to testuser@foobar.com but not next to the signed-in admin's own row]({{ "/assets/images/administration/impersonate-user/all-users-impersonate-link.png" | relative_url }})

CluedIn reloads and signs you in as that user. A banner stays visible at the top of every page for as long as impersonation is active, showing which user you are viewing CluedIn as.

While impersonating, you see exactly the modules, features, and data the impersonated user can see - including anything restricted by their RACI permissions. Admin-only screens, such as **User Management** itself, show **You do not have access** unless the impersonated user also has that access.

![The impersonation banner reading "You are viewing CluedIn as testuser@foobar.com" with a Stop impersonating button, above a page reading "You do not have access, Sorry, you do not have access to this page. To gain access, please contact your administrator."]({{ "/assets/images/administration/impersonate-user/impersonation-banner.png" | relative_url }})

## Stop impersonating

1. In the impersonation banner at the top of the page, select **Stop impersonating**.

CluedIn reloads and returns you to your own account. You do not need to sign in again.

An impersonation session also ends on its own after 1 hour. If it ends while you are still reviewing something, start it again or select **Stop impersonating** and sign back in if prompted.

## What this changes

Impersonation does not change the impersonated user's account - their password, roles, and data stay exactly as they were. It only changes what you, the admin, see while the session is active. Any changes you make while impersonating (for example, editing a record) still happen, and are attributed to the impersonated user, exactly as if they had made the change themselves.

## Audit log reference

Starting and stopping impersonation is recorded on the **Audit Log** tab, including the timestamp, the admin who started or stopped it, and the impersonated user.

## If something goes wrong

- If you don't see the **Impersonate** column or link next to a user, you don't have the OrganizationAdmin role.
- You cannot impersonate yourself - no **Impersonate** link appears on your own row.
- You cannot impersonate a user outside your organization.
