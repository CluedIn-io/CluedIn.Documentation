---
layout: cluedin
nav_order: 3
parent: Access control
grand_parent: Management
permalink: /management/access-control/access-control-reference
title: Access control reference
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will find reference information about the structure of an access control policy and the actions available in the access control policy rule.

## Access control policy structure

Access control policy is a mechanism that allows you to precisely define access to golden records and their properties. The access control policy consists of several building blocks.

![access-control-policy-structure.png]({{ "/assets/images/management/access-control/access-control-policy-structure.png" | relative_url }})

- **Filters** – conditions to define which golden records the access control policy applies to.

- **Policy rule** – an object that grants specific users and/or roles a particular type of access to golden records that match the rule's filters and conditions. The policy rule contains the following settings:

    - **Conditions** – additional criteria on top of the filters to define which golden records are affected by the specific policy rule.

    - **Action** – operation to allow a specific type of access to golden records that match the rule's filters and conditions.

    - **Members** – users and/or roles to whom the policy rule's action is applied.

    - **All Vocabulary Keys** – a checkbox that, if selected, means that the policy rule's action is applied to all vocabulary keys in golden records that match the rule's filters and conditions.

    - **Vocabulary Keys** – a field where you can select specific vocabulary keys to which the policy rule's action will be applied.

    - **Vocabularies** – a field where you can select specific vocabularies to which the policy rule's action will be applied.

        You need to select specific vocabulary keys or vocabularies to which the policy rule will be applied. If no vocabulary keys or vocabularies are selected, the members of the policy rule won't be able to view golden records at all.

## Access control policy rule actions

Access control policy rule actions define the type of access to the properties in golden records that match the rule's filters and conditions.

![access-control-policy-rule-actions.png]({{ "/assets/images/management/access-control/access-control-policy-rule-actions.png" | relative_url }})

### View

This action gives access to view the values of specific vocabulary keys in golden records that match the rule's filters and conditions. This action does not give access to edit the existing properties of a golden record or add new properties. That is why the members of the policy rule with the view action will see the icon indicating that the value cannot be edited.

![access-control-policy-rule-actions-view.png]({{ "/assets/images/management/access-control/access-control-policy-rule-actions-view.png" | relative_url }})

If the users are not granted access to specific vocabularies or vocabulary keys that are used in golden records, they will see the **No value** text on the search page for certain properties. This means that either the property does not exist in a specific golden record or that the users do not have access to the property according to access control.

![access-control-policy-rule-actions-no-value.png]({{ "/assets/images/management/access-control/access-control-policy-rule-actions-no-value.png" | relative_url }})

If you want to indicate that a golden record has a specific property without displaying this property to users, create a policy rule with the mask action.

### Mask

This action hides the values of specific vocabulary keys in golden records that match the rule's filters and conditions. The members of the policy rule with the mask action will see the icon indicating that the value is masked due to access control policy. Masked value cannot be retrieved in any way, and it cannot be edited.

![access-control-policy-rule-actions-mask.png]({{ "/assets/images/management/access-control/access-control-policy-rule-actions-mask.png" | relative_url }})

{:.important}
The [mask value action](/management/rules/rules-reference) in data part and golden record rules will be deprecated in future releases. Therefore, use the mask action in access control policy rules.


### Add/edit

This action allows the members of the policy rule to add new properties to the golden record and/or edit the existing properties in the golden record. The properties that the members can add/edit depend on the vocabularies and/or vocabulary keys selected in the policy rule:

- If the policy rule is applied to all vocabulary keys, then the members can add or edit all vocabulary keys that are used in golden records that match the rule's filters and conditions.

- If policy rule is applied to specific vocabulary keys, then the members can add or edit only the selected vocabulary keys that are used in golden records that match the rule's filters and conditions.

- If the policy rule is applied to specific vocabularies, then the members can add or edit any vocabulary keys belonging to the specified vocabularies that are used in golden records that match the rule's filters and conditions.

{:.important}
The add/edit action takes precedence over the view action. If a user is a member of both a policy rule with the view action and a policy rule with the add/edit action, and both rules apply to the same vocabulary keys, it means that the user will be able to add or edit those vocabulary keys. 

**Add/edit action and RACI permissions**

When adding a property to the golden record, you might want to create a new value. This is possible only if you have the needed RACI permissions: either you are the owner of the vocabulary or you have the Consulted access to the management.datacatalog claim.

When you are trying to add or edit a property in a golden record, CluedIn first checks if you have the required RACI permissions and then it checks if you are allowed to make changes to that specific golden record according to the access control policy. If your access level is less than Consulted, you will not be able to add or edit the property in a golden record.