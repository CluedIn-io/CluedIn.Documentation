---
layout: cluedin
nav_order: 1
parent: Access control
grand_parent: Management
permalink: /management/access-control/create-access-control-policy
title: Create access control policy
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to create an access control policy to configure reliable and secure access to data in CluedIn.

## Create an access control policy

Since access control is not enabled by default, first you need to enable it:

1. In the navigation pane, go to **Administration** > **Settings**.

1. In the **Data Access** section, turn on the toggle for **Access Control** setting.

    ![access-control-enabled.png]({{ "/assets/images/management/access-control/access-control-enabled.png" | relative_url }})

1. Save your changes.

Now that the access control feature is enabled, you can create access control policies.

**To create an access control policy**

1. In the navigation pane, go to **Management** > **Access Control**.

1. Select **Create Policy**.

1. Enter the name of the policy, and then select **Create Policy**.

1. In the **Filters** section, set up a filter to define the golden records to which the policy will apply.

1. In the **Rules** section, select **Add Policy Rule**, and then define the policy rule:

    1. Enter the name of the policy rule.

    1. (Optional) In **Conditions**, set up additional criteria on top of the filters to define which golden records will be affected by the specific policy rule.

    1. In **Action**, select the type of access to golden record properties: view, mask, or add/edit. Learn more in [Access control reference](/management/access-control/access-control-reference).

    1. In **Members**, select the users or roles to which the policy rule will apply.

    1. If you want to allow access to all vocabulary keys in the golden records affected by the access control policy, select the **All Vocabulary Keys** checkbox.

    1. If you want to allow access only to specific vocabularies or vocabulary keys in the golden records affected by the access control policy, select the needed vocabulary keys or vocabularies.

        ![add-policy-rule.png]({{ "/assets/images/management/access-control/add-policy-rule.png" | relative_url }})

    1. Select **Add Policy Rule**.

    You can add multiple policy rules.

1. Save your changes and then turn on the status toggle to activate the policy.

    It might take up to 1 minute to apply the policy across the system.

    {:.important}
    If the source control is enabled, make sure the users from the **Members** section of the policy rule have permissions to the source of golden records. If the users don't have such permissions, they can't view golden records from that source at all. For more information about source control, see [Data access](/administration/user-access/data-access).

## Impact of access control on system features

Access control policies are applied to golden records and vocabulary keys throughout the system. If you don't have access to specific golden records, then you won't be able to view them at all. If you have access to golden records but lack access to some vocabulary keys associated with them, you will see a **Limited details** label on the golden record page. This label indicates that not all properties of the golden record are visible to you. 

![limited-details-label.png]({{ "/assets/images/management/access-control/limited-details-label.png" | relative_url }})

The information on all tabs of the golden record is displayed in accordance with access control policies. For example, on the **History** tab, you can only view only those records that generated vocabulary keys you have access to. 

**Access control and data catalog**

You can view only those vocabularies and vocabulary keys that you have access to according to the source control policies. Also, if an access control policy is applied to a vocabulary key that is mapped to another vocabulary key, then the policy is also applied to the mapped key.

**Access control and streams**

In the stream, you can view only those golden records and vocabulary keys that you have access to according to the source control policies. However, when you start the stream, all data matching the stream configuration will be exported regardless of your access.

**Access policy and rules**

Rules are applied throughout the system regardless of your access to the affected golden records and vocabulary keys. So, you can set up rules for the records that you don't have access to.