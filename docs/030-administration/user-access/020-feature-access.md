---
layout: cluedin
nav_order: 1
parent: User access
grand_parent: Administration
permalink: {{ site.baseurl }}/administration/user-access/feature-access
title: Feature access
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about the main settings that define access to CluedIn features: roles and ownership.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1009084345?h=9c95eebafe&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Roles and ownership"></iframe>
</div>

{:.important}
Feature access does not affect access to data in CluedIn. For example, if you have access to the glossary, you still won't be able to view golden records from a glossary term without specific data access. For more information, see [Data access](/administration/user-access/data-access).

Feature access means permissions that allow you to interact with CluedIn modules: Integrations, Governance, Preparation, Engine Room, Management, Consume, and Administration. Every module contains features that enable you to perform specific tasks. For example, in the Preparation module, you can create clean projects and add enrichers for enhancing golden records. Access to those features is managed by CluedIn roles and ownership permissions.

## Roles

The main parameter that determines whether the user can access CluedIn features is roles. For more information about roles, see a dedicated [article](/administration/roles).

{:.important}
If you use Microsoft Entra ID and you enable automatic role synchronization, then you don’t need to manage access to features via roles in CluedIn. You can do that using Microsoft Entra ID application roles.

If you notice that you don't have access to a specific feature, you can submit a role request to an Administrator. For a detailed instruction on how to get access to features, see [Request access](/getting-access#request-access). As an Administrator, you can process such role requests and choose a suitable claim access level and a role for a user. For more information about roles requests, see [Process role requests](/administration/roles/process-role-requests). The user can have multiple roles with different claim access levels. In this case, the higher claim access level will be applied to the user.

The claim access levels within roles define the possible actions a user can perform on an element within the feature. To illustrate this statement, let's take a look at the example of rules. The access to rules is governed by the Rule Builder claim. Depending on the access level for the Rule Builder claim, you can do different actions with the rules:

- If your access level for the Rule Builder claim is None, you don't have access to the rules at all.

- If your access level for the Rule Builder claim is Informed, you can view all rules.

- If your access level for the Rule Builder claim is Consulted, you can create and manage your own rules. Also, you can make changes to the rules created by other users and submit such changes for approval to the owners of the rule.

- If your access level for the Rule Builder claim is Accountable, you can create and manage your own rules as well as manage all rules created by other users. In other words, this claim access level gives you administrator control over all rules.

## Ownership

Ownership defines the right to approve or reject change requests submitted by non-owner users as well as make direct changes.

Almost every element in CluedIn has the **Owners** tab with a list of users and/or roles who are considered owners. Such elements include clean projects, enrichers, access control policies, vocabularies, deduplication projects, rules, glossary terms, hierarchies, streams, and export targets.

Initially, the user who created the element—for example, a rule—is its owner. However, if you trust other users to process change requests related to the element and to make direct changes to the element, you can add those users to the list of owners. You can also add roles to the list of owners; this way, all users who have that role will get the ownership permissions.

**To add owners**

1. Open the element to which you want to add owners, and then go to the **Owners** tab.

1. Select **Add** > **Add Users** or **Add Roles**.

1. Select the checkboxes next to the users or roles who will be granted ownership.

1. In the lower-right corner, select **Add**.

    ![add-owner-role.gif](../../assets/images/administration/user-access/add-owner-role.gif)

When the users or roles appear on the **Owners** tab of the element, they are granted permission to approve or reject change requests submitted by other users. Also, if their access level for the relevant claim is at least Consulted, they can make changes directly without submitting them for approval.

## Combinations of claim access levels and ownership

Since both claim access levels and ownership permissions regulate the activities that can be performed with an element within a CluedIn feature, it is important to understand how they work together. This section does not include the following combinations:

- None claim access level and ownership – the claim access level is not sufficient to open an element, so the ownership permission doesn't have any practical application in this combination.

- Accountable claim access level and ownership – the claim access level gives full control over all elements within a feature, so the ownership permission doesn't have any practical application in this combination.

**Consulted claim access level with ownership**

The Consulted claim access level gives you access to modify elements with a feature. With the ownership permission, you can modify the configuration of an element right away as well as receive and process change requests submitted by other, non-owner users.

![consulted-owner.gif](../../assets/images/administration/user-access/consulted-owner.gif)

**Informed claim access level with ownership**

The Informed claim access level gives you access to view all elements within a feature. However, even if you have the ownership permission, you cannot approve or reject change requests submitted by other, non-owner users.