---
layout: cluedin
title: Concept of workflows
parent: Workflow
permalink: /workflow/concept-of-approvals
nav_order: 1
has_children: false
---

{:.important}
To use the **Workflow** module in CluedIn, you need to configure [Power Automate integration](/microsoft-integration/power-automate).

Let's explore the concept of Power Automate workflows in CluedIn using an example of rule modification. If you want to automate the approval process for rule changes, you can create a dedicated Power Automate workflow that will send approval requests to the appropriate users whenever a rule is modified.

![concept-of-approvals.gif]({{ "/assets/images/workflow/concept-of-approvals.gif" | relative_url }})

A user with at least Consulted access level to the Rule Builder claim can modify any rule. However, to ensure transparency and accuracy, the changes are not applied right away. Instead, an approval request is sent to the appropriate users. When one of the appropriate users approves changes, a notification in CluedIn is sent to the user who made the changes, and the changes are applied to the rule.

**Who are the users in charge of approval?**

- In case of **modifying an existing element**, the users in charge of approval are the owners listed on the **Owners** tab of the element. Since both users and roles can be the owners, all users with the corresponding roles are also considered approvers.

**Is there a connection between external approvals and internal CluedIn change requests?**

When you modify an element in CluedIn, both an internal change request and an external approval request are sent to the owners. The request that is processed first determines the outcome for the element. For example, if an owner approves the internal change request in CluedIn, the element is updated accordingly. However, if another owner rejects the external approval request in Outlook, this rejection is ignored because the element has already been updated. Essentially, the first processed request is applied to the element, and any subsequent request is ignored.