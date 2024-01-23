---
layout: cluedin
title: Roles
parent: Administration
permalink: /administration/roles
nav_order: 20
has_children: true
tags: ["administration", "roles"]
---

In this article, you will learn about claims and access levels, which are the main concepts that define roles.

**_This article is intended for users with the OrganizationAdmin role or users with the following claim access level._**

| Section | Claim | Access level |
|--|--|--|
| Admin | Roles | At least Consulted |

Roles are used to grant permissions to users to perform specific actions in CluedIn. These permissions are only granted to the modules within the platform, not to the data. For information on how to restrict access to data, see [Permissions](/administration/permissions).

All roles are listed in **Administration** > **Roles**. The following table provides a list of the CluedIn application roles.

| Role name | Description |
|--|--|
| DataArchitect | Responsible for designing an organization's enterprise data strategy. |
| DataCompliance | Responsible for daily operations around data compliance. |
| DataComplianceAdministrator | Responsible for approving changes made by users with the DataCompliance role. |
| DataGovernance | Responsible for monitoring and maintaining data quality. |
| DataGovernanceAdministrator | Responsible for approving changes made by the users with the DataGovernance role. |
| DataSteward | Responsible for cleaning data using the Clean and Prepare modules. |
| DataStewardAdministrator | Responsible for approving changes made by the users with the DataSteward role. |
| DeduplicationAdministrator | Responsible for creating and maintaining deduplication projects and merging the results back into the system. |
| DeduplicationReviewer | Responsible for reviewing deduplication project results and approving groupings. |
| Guest | User with minimal, read-only permissions. |
| OrganizationAdmin | Administrator within the organization. |
| OrganizationUser | User within the organization who can view all modules as read-only. |
| ReportManager | User who can generate reports for compliance matters such as breach, subject request, and retention. |
| User | User who can view all modules as read-only. |

A role is a container for claims and access levels. A claim is the name of a specific feature or operation that can be performed in CluedIn. Most of the time, the name of the claim is the same as the name of the module in CluedIn. An access level indicates the type of activity that can be performed with the claim. 

To view the role's claims and access levels, select the role. In the first column, you can find the name of the section in CluedIn (a) and claims within that section (b). In the second column, you can find access levels (c) to each claim.

![roles-1.png](../../assets/images/administration/roles/roles-1.png)

Each role contains the same list of claims, but different access levels. We recommend that you familiarize yourself with the default CluedIn roles, so that you know which role to assign to users in your organization. If the default configuration is not suitable for you, you can change the access levels in the default roles or create your own roles.

In CluedIn, the following access levels are used:

- **None** – no access to the claim.
- **Informed** – read-only access to the claim. The user will be able to view all information within the claim, but will not be able to add, edit, or delete items within the claim.
- **Consulted** – read and write access to the claim. The user will be able to add, edit, or delete items within the claim.
- **Responsible** – read, write, and submit approval requests.
- **Accountable** – read, write, submit approval requests, and approve requests.

Each subsequent access level includes all permissions from the previous access level.

{:.important}
In CluedIn, the most commonly used access levels are Informed and Consulted. We are working on making the access levels consistent within the platform. Currently, for some modules, the activity represented by the Responsible and Accountable access levels is the same.

All authorized users have a list of claims and access levels applied to them. If a user has multiple roles with different claim access levels, then the higher access level will be applied to the user.