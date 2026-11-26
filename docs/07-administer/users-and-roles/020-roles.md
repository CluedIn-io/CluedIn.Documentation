---
layout: cluedin
title: Roles
parent: Users and roles
grand_parent: Administer
nav_order: 20
permalink: /administer/users-and-roles/roles
content_type: concept
redirect_from: ["/administration/roles"]
source_path: docs/030-administration/020-roles.md
tags: ["administration", "roles"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about claims and access levels, which are the main concepts that define roles.

Roles are used to grant permissions to users to perform specific actions in CluedIn. These permissions are only granted to the modules within the platform, not to the data. For information on how to restrict access to data, see [Data access](/administer/users-and-roles/data-access).

## Default roles

All roles are listed in **Administration** > **Roles**. The following table provides a list of default CluedIn roles. In the **Default access** column, you can download a file with details of the default role's access to the features in CluedIn. You can change the configuration of any role to suit your needs.

| Role name | Description | Default access |
|--|--|--|
| DataArchitect | Responsible for designing an organization's enterprise data strategy. | <a href="/assets/other/claims/DataArchitect.xlsx" download>Download</a> |
| DataCompliance | Responsible for daily operations around data compliance. | <a href="/assets/other/claims/DataCompliance.xlsx" download>Download</a> |
| DataComplianceAdministrator | Responsible for approving changes made by users with the DataCompliance role. | <a href="/assets/other/claims/DataComplianceAdministrator.xlsx" download>Download</a> |
| DataGovernance | Responsible for monitoring and maintaining data quality. | <a href="/assets/other/claims/DataGovernance.xlsx" download>Download</a> |
| DataGovernanceAdministrator | Responsible for approving changes made by the users with the DataGovernance role. | <a href="/assets/other/claims/DataGovernanceAdministrator.xlsx" download>Download</a> |
| DataSteward | Responsible for cleaning data using the Clean and Prepare modules. | <a href="/assets/other/claims/DataSteward.xlsx" download>Download</a> |
| DataStewardAdministrator | Responsible for approving changes made by the users with the DataSteward role. | <a href="/assets/other/claims/DataStewardAdministrator.xlsx" download>Download</a> |
| DeduplicationAdministrator | Responsible for creating and maintaining deduplication projects and merging the results back into the system. | <a href="/assets/other/claims/DeduplicationAdministrator.xlsx" download>Download</a> |
| DeduplicationReviewer | Responsible for reviewing deduplication project results and approving groupings. | <a href="/assets/other/claims/DeduplicationReviewer.xlsx" download>Download</a> |
| Guest | User with minimal, read-only permissions. | <a href="/assets/other/claims/Guest.xlsx" download>Download</a> |
| OrganizationAdmin | Administrator within the organization. | <a href="/assets/other/claims/OrganizationAdmin.xlsx" download>Download</a> |
| OrganizationUser | User within the organization who can view all modules as read-only. | <a href="/assets/other/claims/OrganizationUser.xlsx" download>Download</a> |
| ReportManager | User who can generate reports for compliance matters such as breach, subject request, and retention. | <a href="/assets/other/claims/ReportManager.xlsx" download>Download</a> |
| User | User who can view all modules as read-only. | <a href="/assets/other/claims/User.xlsx" download>Download</a> |

## Understanding roles, claims, and access levels

A role acts as a container for two key components:

- Claims – Specific features or operations that can be performed in CluedIn. Most of the time, the name of the claim is the same as the name of the module in CluedIn. Learn more about claims in a dedicated [article](/administer/users-and-roles/claims).

- Access levels – Indicate the type of activity that can be performed with the claim: None, View, Edit or Manage.

A role can also have [responsibilities](/administer/users-and-roles/responsibilities), which say what work the role does, approves, is asked about, or is told about, and decide where Steward Inbox tasks go. Responsibilities don't grant access.

{:.important}
To get acquainted with the required claims and access levels for all actions in CluedIn, download this <a href="/assets/other/Claims-V1.xlsx" download>file</a>.

## View role details

1. On the navigation pane, go to **Administration** > **Roles**.

    The **Roles** tab lists the roles, with how many users and responsibilities each has. The **All responsibilities** tab lists the responsibilities of every role and person; see [Responsibilities](/administer/users-and-roles/responsibilities).

1. Select a role. It opens on the **Configuration** tab.

    The features are grouped by section, such as Integration or Preparation, and each has an access level. Select a feature to see, in the panel on the right, what its current access level lets users with this role do. A **Dependencies required** warning means the feature needs access to another feature to work.

    ![The Configuration tab of the DataSteward role: features grouped by section, each with an access level, and the Access details panel on the right listing what Edit access to Available Integrations allows]({{ "/assets/images/administration/roles/role-configuration-tab.png" | relative_url }})

    Each role contains the same list of features, but different access levels. We recommend that you familiarize yourself with the [default CluedIn roles](#default-roles), so that you know which role to assign to users in your organization. If the default configuration is not suitable for you, you can change the access levels in the default roles or create your own roles.

The other tabs of a role are **Responsibilities**, **Users** and **Audit log**.

## Create a role

1. On the navigation pane, go to **Administration** > **Roles**, and then select **Create role**.

1. Enter a name. It must be unique (letter case doesn't matter) and 100 characters or fewer.

1. Optional: add a description that explains what people with this role do. You can use bold, italic, underline, strikethrough, lists and links. It shows under the role name.

1. Select **Create**.

The role opens on its **Configuration** tab with access level **None** for every feature. Set its access there, then add [responsibilities](/administer/users-and-roles/responsibilities) and users.

## Change access levels

1. Open the role on the **Configuration** tab. To see what each access level means, select the info icon next to the **Access level** column header.

1. Select the access level of a feature. To change several at once, select the checkboxes next to the features, or next to a section to select all its features, pick the level in the bar at the top, and then select **Apply**.

    Before anything changes, a confirmation shows how many features get more or less access, how many people in the role it affects, which responsibilities would no longer have enough access, and each feature's level now and after. Select **Change N features** to apply. Right after applying, you can select **Undo** in the message to put the previous levels back.

1. Select **Save**.

## Supported access levels

In CluedIn, the following access levels are used:

- **None** – No access to the feature.
- **View** – Read-only access. Users can open the feature and see its items, but can't change them.
- **Edit** – Users can view, create, edit and delete items. Changes to items created by others are submitted for approval to the people with **Manage** access to that item.
- **Manage** – Full control over the feature: users can view, create, edit and delete items, including items created by others, and change the feature's settings. It's also required to create items directly when an approval workflow is enabled for creating them.

{:.important}
Earlier versions of CluedIn used the levels Informed, Consulted, Responsible and Accountable. Existing roles were moved to the new levels: Informed became View, Consulted and Responsible became Edit, and Accountable became Manage. Who does which work is now set with [responsibilities](/administer/users-and-roles/responsibilities). For how access levels combine with access to a single item, see [Feature access](/administer/users-and-roles/feature-access).

## Managing overlapping roles

All authorized users have a list of claims and access levels applied to them. If a user has multiple roles with different claim access levels, then the higher access level will be applied to the user.