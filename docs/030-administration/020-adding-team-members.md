---
layout: default
nav_order: 2
parent: Administration
permalink: /administration/adding-team-members
title: Adding Team Members
tags: ["administration", "users", "sso", "single-sign-on"]
---

## Adding new users manually
New team members can be added to an existing account via their email address. This new member is by default added as a regular user with no extra permissions. It is the responsibility of an _Administrator_ to change their roles after they have been added to the system. Users must have a matching email domain if using the manual approach of User management. Please see the Access Control part of our documentation to see what rights a regular _User_ has within CluedIn.

1. To invite a new user to CluedIn, navigate to the Users menu option and click on the _Administration_ menu option and click on _Users_. You will see a breakdown of roles and users. In the top right hand corner there is a button _Invite a New Team Member_.

1. You will be prompted with the ability to fill in an email. This can be internal or external users. They will receive an email that will be able to guide them through the process. 

If you click on the _Suggested Users_ tab, CluedIn will suggest people to invite based on the data you have already added to CluedIn. This allows you to discover users you might not have thought about adding. 

Instead of adding users manually to the system, it is generally better to to use an LDAP / Single Sign On Provider for managing users and groups within CluedIn. In this way, Users are provisioned through Active Directory and no sensitive user information is ever stored on the CluedIn side. This also allows you to manage access, users and roles from a central place. 

## Allowing new users to sign up

You can configure CluedIn to allow users with a particular email domain to sign up automatically. Follow the instructions in the [Authentication](./authentication) section.
