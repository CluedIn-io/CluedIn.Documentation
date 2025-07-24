---
layout: cluedin
nav_order: 1
parent: User access
grand_parent: Administration
permalink: {{ site.baseurl }}/administration/user-access/data-access
title: Data access
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about the main settings for configuring secure and reliable access to the data in CluedIn—source control and access control.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1009114269?h=7736f41bbb&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Source and access control"></iframe>
</div>

{:.important}
The operations that users can perform with data depend on the roles assigned to the users. For more information, see [Roles](/administration/roles).

Both source control and access control settings are located in **Administration** > **Settings**. This is the starting point where you specify if you want to restrict access to the data in CluedIn. By restricting access, we mean turning on the toggle under **Source Control** and **Access Control**.

![data-access-section.png](../../assets/images/administration/user-access/data-access-section.png)

**Exception in data access settings**

The table below contains the combination of section-claim-access level that grants users access to data regardless of whether the source control and access control are turned on or not.

| Section | Claim | Minimal access level |
|--|--|--|
| Admin | Data Management | Informed |
| Management | Deduplication Project Management | Informed |
| Management | Deduplication Review | Informed |

The reason for this exception is to allow users working on deduplication, clean, or hierarchy projects to view all data in order to properly perform their tasks. Imagine processing a group of duplicates where you don’t have access to some of the conflicting properties; in this case, you won’t be able to fix conflicts at all.

## Source control

With source control, you can manage access to data from a specific source—a data source, a manual data entry project, an integration, and an enricher.

Every source has the **Permissions** tab with a list of users or roles who have access the records produced from that source. Initially, only the user who created the source has access to the records produced from it. However, you can give permission to the source to other users or roles. If you select a role, then all users who have that role will be granted permission to the source.  

**To give permission to the source**

1. Open the needed source, and then go to the **Permissions** tab.

1. Select **Add** > **Add Users** or **Add Roles**.

1. Select the checkboxes next to the users or roles who will be granted permission to the source.

1. In the upper-right corner, select **Grant Access**.

    ![permissions-add-users.gif](../../assets/images/administration/user-access/permissions-add-users.gif)

When the users or roles appear on the **Permissions** tab of the source, they are granted access to the records produced from that source. However, if the access control is enabled, those users or roles must also be added to the access control policies in order to view the records.

## Access control

With access control, you can manage access to entire golden records or specific vocabulary keys. To do that, you create access control policies consisting of the following:

- A filter that defines the golden records to which the policy will be applied.

- Users or roles who will be granted access to golden records.

- Vocabularies or vocabulary keys to which the users or roles will be granted access.

Learn how to create an access control policy in the dedicated [article](/management/access-control).

## Combinations of source and access control

Since both access control and source control regulate access to data, it is important to understand how they work together.

**Both source control and access control are disabled**

![sc-ac-disabled.gif](../../assets/images/administration/user-access/sc-ac-disabled.gif)

When both source control and access control are disabled, any user with any role can view all data in CluedIn without any restrictions. If you have sensitive data that requires protection, we recommend enabling source control and/or access control to ensure secure access.

**Both source control and access control are enabled**

![sc-ac-enabled.gif](../../assets/images/administration/user-access/sc-ac-enabled.gif)

When both source control and access control are enabled, access to data for all users and roles is restricted according to source permissions and access control policies. To view specific golden records, the user has to meet the following requirements:

- The user or the role assigned to the user should be added to the **Permissions** tab of the source from which golden records were produced.

- The user or the role assigned to the user should be added to the **Members** section of the access control policy rule that regulates access to golden records.

Only when both requirements are met, the user can view specific golden records. If either requirement is not met, or if no requirements are met at all, the user will not be able to view golden records. For example, if the user has permissions to the source of golden records but is not included in the access control policy that regulates access to such golden records, then the user cannot view the golden records.

![sc-ac-enabled-no-policy.gif](../../assets/images/administration/user-access/sc-ac-enabled-no-policy.gif)

Similarly to the previous example, if the user is included in the access control policy that regulates access to golden records but does not have permissions to the source of such golden records, then the user cannot view the golden records.

For reliable and secure access to golden records in CluedIn, you have to configure both source permissions and access control policies.

**One of the data access settings is enabled and the other is disabled**

When one of the data access settings is enabled and the other is disabled, access to data is restricted for all users and/or roles according to the enabled data access setting.

![sc-enabled-ac-disabled.gif](../../assets/images/administration/user-access/sc-enabled-ac-disabled.gif)

For example, when source control is enabled and access control is disabled, access to data for all users and/or roles is restricted according to source permissions. Thus, users and/or roles can view golden records only if they are added to the **Permissions** tab of the source from which such golden records were produced.

On the contrary, when source control is disabled and access control is enabled, access to data for all users and roles is restricted according to access control policies. Thus, users and/or roles can view golden records only if they are added to the access control policies that regulate access to such golden records.