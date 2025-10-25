---
layout: cluedin
title: Roles
parent: Administration
permalink: /administration/roles
nav_order: 20
has_children: true
tags: ["administration", "roles"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about claims and access levels, which are the main concepts that define roles.

Roles are used to grant permissions to users to perform specific actions in CluedIn. These permissions are only granted to the modules within the platform, not to the data. For information on how to restrict access to data, see [Data access](/administration/user-access/data-access).

## Default roles

All roles are listed in **Administration** > **Roles**. The following table provides a list of default CluedIn roles. In the **Access status** column, you can download a file with details of the default role's access to the features in CluedIn. However, you can change the configuration of the role and extend its access to features according to your needs.

| Role name | Description | Access status |
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

- Claims – Specific features or operations that can be performed in CluedIn. Most of the time, the name of the claim is the same as the name of the module in CluedIn. Learn more about claims in a dedicated [article](/administration/roles/claims).

- Access levels – Indicate the type of activity that can be performed with the claim.

{:.important}
To get acquainted with the required claims and access levels for all actions in CluedIn, download this <a href="../../../assets/other/Claims-V1.xlsx" download>file</a>.

## View role details

1. On the navigation pane, go to **Administration** > **Roles**.

2. Select a role to view its claims and access levels.

    You can view the following information:

    - The name of the section in CluedIn (a).

    - Claims within that section (b).

    - Access levels (c) to each claim.

    Each role contains the same list of claims, but different access levels. We recommend that you familiarize yourself with the [default CluedIn roles](#default-roles), so that you know which role to assign to users in your organization. If the default configuration is not suitable for you, you can change the access levels in the default roles or create your own roles.

    ![roles-1.png]({{ "/assets/images/administration/roles/roles-1.png" | relative_url }})

## Supported access levels

In CluedIn, the following access levels are used:

- **None** – No access to the claim.
- **Informed** – Read-only access to the claim. The user will be able to view all information within the claim, but will not be able to add, edit, or delete items within the claim.
- **Consulted** – Read and write access to the claim. The user will be able to add, edit, or delete items within the claim.

{:.important}
The Responsible and Accountable access levels are reserved for upcoming versions. Currently, the activities represented by these access levels are the same as in the Consulted access level.

## Managing overlapping roles

All authorized users have a list of claims and access levels applied to them. If a user has multiple roles with different claim access levels, then the higher access level will be applied to the user.