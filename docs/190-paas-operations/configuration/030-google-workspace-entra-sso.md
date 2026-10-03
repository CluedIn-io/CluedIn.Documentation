---
layout: cluedin
nav_order: 8
parent: Configuration
grand_parent: PaaS operations
permalink: /deployment/infra-how-tos/google-workspace-entra-sso
title: Sign in with Google Workspace through Microsoft Entra
tags: ["authentication", "sso", "entra", "google-workspace"]
last_modified: 2026-10-01
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Use a **Google Workspace custom SAML app** to authenticate managed Workspace users through Entra. Microsoft's built-in Google federation is intended for Gmail users; Workspace domains use SAML federation.

Review the [shared prerequisites and SAML values](/deployment/infra-how-tos/external-idp-entra-sso).

## Configure Google Workspace

1. As a super administrator, open **Apps > Web and mobile apps > Add app > Add custom SAML app**.
2. Name the app and download the Google IdP metadata or collect its SSO URL, Entity ID, and certificate.
3. In **Service Provider Details**, set **ACS URL** to the shared ACS and **Entity ID** to the shared audience.
4. Select **PERSISTENT** for the Name ID format and map its value to an administrator-controlled stable user attribute. The default primary email can change; plan identity continuity if using it.
5. Add an attribute mapping from the user's primary email to the shared email claim.
6. Finish and turn on **User access** for the pilot user's organizational unit or access group.

Confirm the assertion's NameID stays consistent and that its email matches the invited guest.

## Connect Entra and CluedIn

Complete [Entra federation, guest onboarding, and CluedIn role assignment](/deployment/infra-how-tos/external-idp-entra-sso#configure-entra). Use the resource tenant associated with your CluedIn SSO connection.

Start the pilot sign-in from CluedIn, verify the correct user and role, then test role changes and logout. Provider roles or groups require an explicit authorization design; forwarding them in SAML does not automatically assign CluedIn roles.

{:.important}
Validate this pattern in your deployment before rollout. The provider application authenticates to Entra; its ACS points to Entra rather than CluedIn.

## Troubleshooting

If Google denies access, check the app's User access setting and allow time for changes to propagate. Test from CluedIn even if Google's **Test SAML login** succeeds: the complete Entra guest flow still needs verification.

Google group attributes do not create Entra group membership automatically.

## References

- [Configure a custom Workspace SAML app](https://knowledge.workspace.google.com/admin/apps/set-up-your-own-custom-saml-app)
- [Microsoft Google federation guidance](https://learn.microsoft.com/en-us/entra/external-id/google-federation)
