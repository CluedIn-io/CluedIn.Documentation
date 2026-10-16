---
layout: cluedin
title: RACI matrix
parent: Users and roles
grand_parent: Administer
nav_order: 100
permalink: /administer/users-and-roles/raci-matrix
redirect_from: ["/administer/access-control/raci-matrix"]
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The RACI matrix lets you record who is responsible for which CluedIn function—deduplication, cleaning, enrichment, and so on—on which business domain, and see everything you have set up in one place. Use it when you need a clear, shared answer to "if there is a data quality problem with Customer records, who owns fixing it?" without digging through role assignments one at a time.

{:.important}
The RACI matrix is a planning and documentation tool. Adding a responsibility here does not change what a role or user can actually do in CluedIn—it does not grant claims or create access control policies. To change what someone can access, assign [roles](/administer/users-and-roles/roles) and [claims](/administer/users-and-roles/claims), or configure [access control](/administer/access-control).

## Prerequisites

- The same claim as the [Access Control](/administer/access-control) module, at Informed access or higher. See [Claims](/administer/users-and-roles/claims).
- The role or user you want to record a responsibility for must already exist. See [Roles](/administer/users-and-roles/roles) and [User management](/administer/users-and-roles/user-management).

## Set up a responsibility

**To add a responsibility**

1. In the navigation pane, go to **Management** > **RACI Matrix**.

1. Under **1. Who**, select the role or user you want to assign a responsibility to.

1. Under **2. What function**, select one or more CluedIn functions. The list is grouped by category—Management, Preparation, Integration, and so on—and covers every function a role can hold a claim for, such as Duplicates, Clean, or Streams.

1. Under **3. What data**, select one or more business domains. Start typing to search domains you have already used, or create a new one.

1. Select **Add responsibility**.

    ![The RACI matrix rule builder with DataSteward selected as Who, Duplicates and Clean selected as functions, and Customer selected as the business domain]({{ "/assets/images/administration/raci-matrix/raci-matrix-rule-builder.png" | relative_url }})

CluedIn creates one responsibility for every function and business domain combination you selected. For example, selecting two functions and one business domain creates two responsibilities for the role or user you chose.

## Verify the result

After you select **Add responsibility**, a confirmation message appears and the matrix below updates immediately:

- A row appears for each function and business domain combination you just created, grouped by the function's category.
- The role or user you selected shows a checkmark in that row.

If you selected a function and/or a business domain in the rule builder without saving yet, a summary line above the matrix already tells you who is responsible for that combination—or, if no one is, says so directly so you can spot the gap before you close the page.

## Roles and users with broad access

Some roles and users already have broad access in CluedIn—the same [claim-based exception](/administer/users-and-roles/data-access) that lets them bypass access control everywhere else. The matrix marks their column with a distinct icon and a tinted background so you can tell at a glance which columns are "everything, because of their claims" rather than responsibilities you set up one by one. Use the toggle above the matrix to hide these columns when you want to focus on the responsibilities that differ from person to person.

## Remove a responsibility

**To remove a responsibility**

1. In the matrix, find the checkmark for the responsibility you want to remove.

1. Select the checkmark.

1. In the confirmation dialog, select **Confirm**.

The responsibility is removed immediately and cannot be undone. If a row no longer has any responsibility assigned to it, the row disappears from the matrix.
