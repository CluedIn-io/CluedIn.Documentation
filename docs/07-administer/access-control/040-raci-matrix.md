---
layout: cluedin
title: RACI matrix
parent: Access control
grand_parent: Administer
nav_order: 40
permalink: /administer/access-control/raci-matrix
content_type: concept
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The RACI matrix gives you a single view of who is responsible for what in CluedIn, based entirely on your current access control policies. Instead of opening each policy to see which roles and users it grants access to, you can see every capability and every role or user that is responsible for it at a glance.

{:.important}
The matrix is a read-only summary of your existing access control policies. To change who is responsible for a capability, [edit the access control policy](/administer/access-control/manage-access-control-policies) that grants it—the matrix updates automatically the next time you open it.

**To open the RACI matrix**

- In the navigation pane, go to **Management** > **RACI Matrix**.

You need the same claim as the Access Control module to see this page. For more information, see [Claims](/administer/users-and-roles/claims).

## How the matrix is built

- **Rows** are capabilities—a combination of an [access control action](/administer/access-control/access-control-reference) (View, Add/edit, Mask, or Delete Record) and the business domain it applies to, such as *View — Customer* or *Add/edit — Product*. Only combinations that an active access control policy actually grants appear as rows; a capability with no policy behind it is not shown.

- **Columns** are the roles in your organization, plus any user who was added directly to a policy rule's members instead of through a role.

- A checkmark in a cell means that role or user is responsible for that capability—an active access control policy grants them the action, scoped to that business domain.

A capability's business domain comes from the policy's filter: if a policy's filter restricts it to a specific business domain (entity type), the capability it grants only applies to that domain. If a policy has no such filter, it applies to every business domain the matrix currently shows.

## Roles and users with full access

Some roles and users do not need an access control policy to see or change data—they already bypass access control, the same way they bypass it everywhere else in CluedIn. This happens when a role or user has one of the claim and access level combinations described in [Data access](/administer/users-and-roles/data-access), such as Informed access or higher to the Data Management claim.

These roles and users show a checkmark across every capability in the matrix, regardless of whether a policy specifically names them, because they are responsible for all business domains.

## Only active policies count

The matrix only reflects **active** access control policies. If you deactivate a policy, the capabilities and responsibilities it granted disappear from the matrix the next time you open it, even though the policy itself still exists. To see a capability in the matrix again, [activate the policy](/administer/access-control/manage-access-control-policies#activate-and-deactivate-a-policy) that grants it.
