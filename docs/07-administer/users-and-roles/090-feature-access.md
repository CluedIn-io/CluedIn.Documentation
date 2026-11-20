---
layout: cluedin
title: Feature access
parent: Users and roles
grand_parent: Administer
nav_order: 90
permalink: /administer/users-and-roles/feature-access
content_type: how-to
redirect_from: ["/administration/user-access/feature-access"]
source_path: docs/030-administration/user-access/020-feature-access.md
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about the main settings that define access to CluedIn features: roles and item access.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1009084345?h=9c95eebafe&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Roles and ownership"></iframe>
</div>

{:.important}
Feature access does not affect access to data in CluedIn. For example, if you have access to the glossary, you still won't be able to view golden records from a glossary term without specific data access. For more information, see [Data access](/administer/users-and-roles/data-access).

Feature access means permissions that allow you to interact with CluedIn modules: Integrations, Governance, Preparation, Engine Room, Management, Consume, and Administration. Every module contains features that enable you to perform specific tasks. For example, in the Preparation module, you can create clean projects and add enrichers for enhancing golden records. Access to those features is managed by CluedIn roles and by item access.

## Roles

The main parameter that determines whether the user can access CluedIn features is roles. For more information about roles, see a dedicated [article](/administer/users-and-roles/roles).

{:.important}
If you use Microsoft Entra ID and you enable automatic role synchronization, then you don’t need to manage access to features via roles in CluedIn. You can do that using Microsoft Entra ID application roles.

If you notice that you don't have access to a specific feature, you can submit a role request to an Administrator. For a detailed instruction on how to get access to features, see [Request access](/get-started/getting-access#request-access). As an Administrator, you can process such role requests and choose a suitable claim access level and a role for a user. For more information about roles requests, see [Process role requests](/administer/users-and-roles/process-role-requests). The user can have multiple roles with different claim access levels. In this case, the higher claim access level will be applied to the user.

The claim access levels within roles define the possible actions a user can perform on an element within the feature. To illustrate this statement, let's take a look at the example of rules. The access to rules is governed by the Rule Builder claim. Depending on the access level for the Rule Builder claim, you can do different actions with the rules:

- If your access level for the Rule Builder claim is None, you don't have access to the rules at all.

- If your access level for the Rule Builder claim is View, you can view all rules.

- If your access level for the Rule Builder claim is Edit, you can create and manage your own rules. Also, you can make changes to the rules created by other users and submit such changes for approval to the users and roles with Manage access to the rule.

- If your access level for the Rule Builder claim is Manage, you can create and manage your own rules as well as manage all rules created by other users. In other words, this claim access level gives you administrator control over all rules.

## Item access

Item access gives users and roles access to one element, on top of their role's access level. It replaces the **Owners** tab of earlier versions.

Elements with an **Access** tab include clean projects, enrichers, access control policies, vocabularies, deduplication projects, rules, glossary terms, hierarchies, streams, data sources, manual data entry projects and export targets.

Each entry on the tab has one of these levels:

- **View** – the user or role is listed with read access. It doesn't let them open the element if their role has no access to the feature.
- **Edit** – changes they make to the element apply without approval.
- **Manage** – they can also change who has access to the element, and they approve or reject change requests submitted by others.

The user who creates an element gets **Manage** access automatically, and is marked with a **Creator** tag. An element always keeps at least one entry with Manage access, so the last one can't be removed or lowered.

![The Access tab of a rule: a note about item access, the Add user or role and Access level fields, the list of users and roles with their access level and a Creator tag, and the Who does the work list below]({{ "/assets/images/administration/user-access/item-access-tab.png" | relative_url }})

**To give a user or role access to an element**

1. Open the element, and then go to the **Access** tab.

1. In **Add user or role**, select a user or role.

1. In **Access level**, select **View**, **Edit** or **Manage**. The default is **Edit**.

1. Select **Add**.

To change an entry's level, select a new level in its row. To remove an entry, select the delete icon in its row. Changing levels needs Manage access to the element, or the Manage access level for the feature. If you don't have Manage access to the element, adding or removing an entry is submitted for approval.

Below the list, **Who does the work** shows the [responsibilities](/administer/users-and-roles/responsibilities) that cover the element, and whether each one is set on this element or applies to all elements of its kind. Change them on the role's **Responsibilities** tab.

{:.important}
When CluedIn is upgraded, each existing owner becomes an entry with Manage access, and the user who created the element is marked as its creator.

## Combinations of claim access levels and item access

Since both claim access levels and item access regulate the activities that can be performed with an element within a CluedIn feature, it is important to understand how they work together. This section does not include the following combinations:

- None claim access level and item access – the claim access level is not sufficient to open an element, so item access doesn't have any practical application in this combination.

- Manage claim access level and item access – the claim access level gives full control over all elements within a feature, so item access doesn't have any practical application in this combination.

**Edit claim access level with Manage access to the element**

The Edit claim access level gives you access to modify elements with a feature. With Manage access to the element, you can modify the configuration of the element right away as well as receive and process change requests submitted by other users.

![Diagram: a user with Manage access to an element modifies its configuration and changes apply right away; another user with the Edit access level submits changes for approval, and the first user approves or rejects them]({{ "/assets/images/administration/user-access/consulted-owner.gif" | relative_url }})

**View claim access level with access to the element**

The View claim access level gives you access to view all elements within a feature. Even with Manage access to an element, you cannot approve or reject change requests submitted by other users.
