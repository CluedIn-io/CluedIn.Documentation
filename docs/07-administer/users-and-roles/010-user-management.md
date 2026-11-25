---
layout: cluedin
title: User management
parent: Users and roles
grand_parent: Administer
nav_order: 10
permalink: /administer/users-and-roles/user-management
content_type: how-to
redirect_from: ["/administration/user-management"]
source_path: docs/030-administration/010-user-management.md
tags: ["administration", "users"]
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to add and deactivate users in your CluedIn organization.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/936290630?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture;" title="How to add a user"></iframe>
</div>

**_This article is intended for users with the OrganizationAdmin role or users with the following claim access level._**

| Section | Claim | Access level |
|--|--|--|
| Admin | Users | At least Consulted |

A user is someone who can sign in to CluedIn. The user's access to CluedIn modules and features is defined by the user's roles. For more information, see [Roles](/administer/users-and-roles/roles).

You can perform the following actions to manage users:

- [Add user](#add-user-by-email-address)
- [Deactivate user](#deactivate-user)
- [Generate a password for a service account](#generate-a-password-for-a-service-account)

## Add user

Users can be added to CluedIn in one of the following ways:

- [By the user's email address](#add-user-by-email-address)
- [Via Azure Active Directory single sign-on (SSO)](#add-user-via-sso)

### Add user by email address

If you don't have Azure Active Directory SSO enabled for CluedIn, you can add users to the platform by their email addresses.

The following diagram shows the flow of adding users to CluedIn.

![Diagram: a user with the required access level adds a user by email; the new user receives an activation email, creates a password and signs up, then signs in and starts using CluedIn]({{ "/assets/images/administration/user-management/add-user-diagram.gif" | relative_url }})

**To add a user by email address**

1. On the navigation pane, go to **Administration** > **User Management**.

1. On the actions pane, select **Users**. Then, select **Invite User**.

1. On the **Invite User** pane, enter the user's email address. Then, in the lower-right corner, select **Invite**.

    The user will receive an email with a link to activate their account. After the user follows the link and creates a password, you will see the user on the **All users** page.

    ![The All users page showing the invited user john.smith@foobar.com with the OrganizationUser role and an Active status toggle]({{ "/assets/images/administration/user-management/invite-user-email-2.png" | relative_url }})

    By default, the user's role is OrganizationUser. It means that the user can view all sections and modules in a read-only mode. To give the user access to more features within the platform, [add another role to the user](/administer/users-and-roles/assign-roles).

### Add user via SSO

If you have Azure Active Directory SSO enabled for CluedIn, the users will be able to sign in using SSO. For more information, see [Configure SSO](/operate/configuration/configure-sso).

{:.important}
Because the users are part of your SSO domain, they do not need an invite. They can log in directly using their organization credentials. Use invites only for CluedIn non-SSO users.

## Deactivate user

If you want to prevent the user from signing in to CluedIn, deactivate the user.

For SSO users, you can revoke user access in Azure Active Directory. For users added to CluedIn by their email address, you can deactivate them in CluedIn.

The following diagram shows the flow of deactivating a user in CluedIn.

![Diagram: a user with the required access level deactivates a user, after which that user cannot sign in to CluedIn]({{ "/assets/images/administration/user-management/deactivate-user-diagram.gif" | relative_url }})

**To deactivate a user in CluedIn**

1. On the navigation pane, go to **Administration** > **User Management**.

1. On the actions pane, select **Users**. 

1. On the **All users** page, find the user whom you want to deactivate.

1. In the **Active** column, turn off the status toggle.

    Alternatively, you can deactivate the user from the user details page. To do that, select the user and on the **Settings** tab, turn off the status toggle.

    The status of the user is changed to **Blocked**.

    ![The All users page with the status toggle for john.smith@foobar.com turned off and the status shown as Blocked]({{ "/assets/images/administration/user-management/deactivate-user-1.png" | relative_url }})

    The user won't be able to sign in to CluedIn.

## Generate a password for a service account

A user who signs in to CluedIn via SSO has no local password, because their identity provider authenticates them instead. Some automation tools, such as a Product Deployment Toolkit, need a username and password to authenticate with CluedIn directly. To give such a tool its own credentials, mark the SSO user it runs as a **service account**, then generate a local password for it.

{:.important}
This action requires a higher access level than the rest of this article: at least **Accountable** on the **Admin** > **Users** claim, not just Consulted.

**To generate a password for a service account**

1. On the navigation pane, go to **Administration** > **User Management**.

1. On the **All users** page, select the SSO user you want to use as a service account.

1. On the user's details page, select the **Settings** tab.

1. Turn on the **Service Account** toggle.

    ![The user Settings tab with the Service Account toggle turned on and the Generate Password button enabled]({{ "/assets/images/administration/user-management/service-account-toggle.png" | relative_url }})

1. Select **Generate Password**.

1. In the confirmation dialog, select **Generate Password** again to confirm.

    The new password is shown once, with a button to copy it to your clipboard. Copy it now: once you close the dialog, CluedIn does not show the password again, and there is no way to retrieve it later.

1. Select **Continue** to close the dialog.

### Verify the result

The service account can sign in with its username and the copied password, in addition to signing in via SSO unless SSO is otherwise disabled for that user.

### What this changes

Generating a password replaces any local password the user already had. Anything that was using the previous password — including a password generated earlier for the same service account — stops working immediately. Turning the **Service Account** toggle off again does not remove the local password; it only changes whether **Generate Password** is available for that user.

### If something goes wrong

**Generate Password is disabled.** The user is not marked as a service account yet. Turn on the **Service Account** toggle first.

## User management reference

Whenever a new user is added to CluedIn or changes are made to the user details page, they are recorded and can be found on the **Audit Log** tab. These actions include the following:

- Create a user
- Add a user to a role
- Remove a user from a role
- Activate a user
- Deactivate a user
- Delete user invite
- Complete registration
- Mark user as service account
- Unmark user as service account
- Generate password for user