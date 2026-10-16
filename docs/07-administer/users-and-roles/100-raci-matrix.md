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
- The business domain you want to record a responsibility for must already be configured. See [Business domains](/model/business-domains).

## Set up responsibilities

**To add one or more responsibilities**

1. In the navigation pane, go to **Management** > **RACI Matrix**.

1. Under **Who**, select one or more roles or users.

1. Under **Functions**, select one or more CluedIn functions. The list is grouped by category—Management, Preparation, Integration, and so on—and covers every function a role can hold a claim for, such as Duplicates, Clean, or Streams.

1. Under **Business domains**, search for one or more business domains. This searches the business domains you have already configured, so you always pick a domain that actually exists rather than typing a name that might not match anything. If the domain you need isn't listed, [create it](/model/business-domains/manage-business-domains) first, then come back here.

1. Check the summary above the button—it states exactly how many responsibilities this creates (every combination of who, function and business domain you picked) and, when you want to double-check before committing, **Show the combinations** expands the full list.

1. Select **Add**.

    ![The RACI matrix rule builder with DataSteward selected as Who, Duplicates selected as a function, and Account selected as the business domain, above a summary stating this will create 1 responsibility]({{ "/assets/images/administration/raci-matrix/raci-matrix-rule-builder.png" | relative_url }})

Because Who, Functions and Business domains can each hold more than one selection, one **Add** can set up many responsibilities at once—for example, two roles across three functions and one business domain creates six responsibilities in a single action. This is the fastest way to set up several similar roles or users together; see [Make changes directly in the matrix](#make-changes-directly-in-the-matrix) for one-off additions afterward.

## Verify the result

After you select **Add**, a confirmation message appears and the matrix below updates immediately:

- A row appears for each function and business domain combination you just created, grouped by the function's category.
- Each role or user you selected shows a checkmark in that row.

If you selected a function and/or a business domain in the rule builder without saving yet, a summary line above the matrix already tells you who is responsible for that combination—or, if no one is, says so directly so you can spot the gap before you close the page.

## Roles and users with broad access

Some roles and users already have broad access in CluedIn—the same [claim-based exception](/administer/users-and-roles/data-access) that lets them bypass access control everywhere else. The matrix marks their column with a distinct icon and a tinted background so you can tell at a glance which columns are "everything, because of their claims" rather than responsibilities you set up one by one. Use the toggle above the matrix to hide these columns when you want to focus on the responsibilities that differ from person to person.

## Make changes directly in the matrix

Beyond the rule builder, the matrix itself can be edited directly—useful for a one-off change, or for extending something you already set up:

- **Add a single responsibility.** Select the **+** in any empty cell to add just that one role-or-user/function/business-domain combination, without reopening the rule builder.
- **Assign a row to more roles or users at once.** Point at a row's function/business domain label and select the **+** that appears next to it. This opens a list of every role or user who doesn't already have that responsibility—select one to assign it immediately, and repeat for anyone else you want to add to that same row.
- **Copy a role or user's responsibilities to another.** Select the **⋮** menu on a column header and choose **Copy to**, then the role or user to copy to. Every responsibility the source role or user has is duplicated onto the target, skipping anything the target already has. This is the fastest way to set up a role or user that should mostly match an existing one.

## Remove a responsibility

**To remove a responsibility**

1. In the matrix, find the checkmark for the responsibility you want to remove.

1. Select the checkmark.

1. In the confirmation dialog, select **Confirm**.

The responsibility is removed immediately and cannot be undone. If a row no longer has any responsibility assigned to it, the row disappears from the matrix.
