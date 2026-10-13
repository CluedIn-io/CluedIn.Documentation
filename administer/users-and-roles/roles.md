---
title: Roles
url: https://documentation.cluedin.net/administer/users-and-roles/roles
content_type: concept
section: Administer > Users and roles
---

# Roles

> concept: Explains how something works.

In this article, you will learn about claims and access levels, which are the main concepts that define roles.

Roles are used to grant permissions to users to perform specific actions in CluedIn. These permissions are only granted to the modules within the platform, not to the data. For information on how to restrict access to data, see [Data access](https://documentation.cluedin.net/administer/users-and-roles/data-access.md).

## Default roles

All roles are listed in **Administration** > **Roles**. The following table provides a list of default CluedIn roles. In the **Access status** column, you can download a file with details of the default role's access to the features in CluedIn. However, you can change the configuration of the role and extend its access to features according to your needs.

| Role name | Description | Access status |
|--|--|--|
| DataArchitect | Responsible for designing an organization's enterprise data strategy. | [Download](https://documentation.cluedin.net/assets/other/claims/DataArchitect.xlsx) |
| DataCompliance | Responsible for daily operations around data compliance. | [Download](https://documentation.cluedin.net/assets/other/claims/DataCompliance.xlsx) |
| DataComplianceAdministrator | Responsible for approving changes made by users with the DataCompliance role. | [Download](https://documentation.cluedin.net/assets/other/claims/DataComplianceAdministrator.xlsx) |
| DataGovernance | Responsible for monitoring and maintaining data quality. | [Download](https://documentation.cluedin.net/assets/other/claims/DataGovernance.xlsx) |
| DataGovernanceAdministrator | Responsible for approving changes made by the users with the DataGovernance role. | [Download](https://documentation.cluedin.net/assets/other/claims/DataGovernanceAdministrator.xlsx) |
| DataSteward | Responsible for cleaning data using the Clean and Prepare modules. | [Download](https://documentation.cluedin.net/assets/other/claims/DataSteward.xlsx) |
| DataStewardAdministrator | Responsible for approving changes made by the users with the DataSteward role. | [Download](https://documentation.cluedin.net/assets/other/claims/DataStewardAdministrator.xlsx) |
| DeduplicationAdministrator | Responsible for creating and maintaining deduplication projects and merging the results back into the system. | [Download](https://documentation.cluedin.net/assets/other/claims/DeduplicationAdministrator.xlsx) |
| DeduplicationReviewer | Responsible for reviewing deduplication project results and approving groupings. | [Download](https://documentation.cluedin.net/assets/other/claims/DeduplicationReviewer.xlsx) |
| Guest | User with minimal, read-only permissions. | [Download](https://documentation.cluedin.net/assets/other/claims/Guest.xlsx) |
| OrganizationAdmin | Administrator within the organization. | [Download](https://documentation.cluedin.net/assets/other/claims/OrganizationAdmin.xlsx) |
| OrganizationUser | User within the organization who can view all modules as read-only. | [Download](https://documentation.cluedin.net/assets/other/claims/OrganizationUser.xlsx) |
| ReportManager | User who can generate reports for compliance matters such as breach, subject request, and retention. | [Download](https://documentation.cluedin.net/assets/other/claims/ReportManager.xlsx) |
| User | User who can view all modules as read-only. | [Download](https://documentation.cluedin.net/assets/other/claims/User.xlsx) |

## Understanding roles, claims, and access levels

A role acts as a container for two key components:

- Claims – Specific features or operations that can be performed in CluedIn. Most of the time, the name of the claim is the same as the name of the module in CluedIn. Learn more about claims in a dedicated [article](https://documentation.cluedin.net/administer/users-and-roles/claims.md).

- Access levels – Indicate the type of activity that can be performed with the claim.

> **Important:** To get acquainted with the required claims and access levels for all actions in CluedIn, download this [file](https://documentation.cluedin.net/assets/other/Claims-V1.xlsx).

## View role details

1. On the navigation pane, go to **Administration** > **Roles**.

2. Select a role to view its claims and access levels.

    You can view the following information:

    - The name of the section in CluedIn (a).

    - Claims within that section (b).

    - Access levels (c) to each claim.

    Each role contains the same list of claims, but different access levels. We recommend that you familiarize yourself with the [default CluedIn roles](#default-roles), so that you know which role to assign to users in your organization. If the default configuration is not suitable for you, you can change the access levels in the default roles or create your own roles.

    ![Role claims for the Preparation section: (a) the section name, (b) claims such as Clean, Mesh Center and Prepare, and (c) the access level for each, set to Accountable](https://documentation.cluedin.net/assets/images/administration/roles/roles-1.png)

## Supported access levels

In CluedIn, the following access levels are used:

- **None** – No access to the claim.
- **Informed** – Read-only access to the claim. The user will be able to view all information within the claim, but will not be able to add, edit, or delete items within the claim.
- **Consulted** – Read and write access to the claim. The user will be able to add, edit, or delete items within the claim.

> **Important:** The Responsible access level is reserved for upcoming versions. Currently, the activities represented by this access level are the same as in the Consulted access level. The Accountable access level gives full control over all elements within a feature, including elements owned by other users, and it is required to create elements directly when an approval workflow is enabled for creating them. For more information, see [Feature access](https://documentation.cluedin.net/administer/users-and-roles/feature-access.md).

## Managing overlapping roles

All authorized users have a list of claims and access levels applied to them. If a user has multiple roles with different claim access levels, then the higher access level will be applied to the user.

Up: [Users and roles](https://documentation.cluedin.net/administer/users-and-roles.md)
