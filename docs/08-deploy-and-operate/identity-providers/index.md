---
layout: cluedin
title: External identity providers
parent: Deploy & operate
nav_order: 65
has_children: true
permalink: /operate/identity-providers
content_type: landing
summary: CluedIn signs people in through Microsoft Entra, and Entra can federate other identity providers such as Okta, Auth0 or Google Workspace, so people keep using the account they already have.
---

CluedIn's single sign-on is wired to Microsoft Entra ID; setting that up is covered in [SSO](/operate/configuration/configure-sso). When your users authenticate with a different provider, Entra acts as the broker: the provider signs the user in, and Entra issues the token CluedIn consumes.

Start with [Federate identity providers through Microsoft Entra](/operate/identity-providers/external-idp-entra-sso), which covers the steps common to every provider, then follow the page for yours. Which CluedIn role a signed-in user gets is configured separately, in [Users and roles](/administer/users-and-roles).
