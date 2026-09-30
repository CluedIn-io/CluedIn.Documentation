---
layout: cluedin
nav_order: 6
parent: Configuration
grand_parent: PaaS operations
permalink: /deployment/infra-how-tos/pingone-entra-sso
title: Sign in with PingOne through Microsoft Entra
tags: ["authentication", "sso", "entra", "pingone"]
last_modified: 2026-10-01
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

This guide covers **PingOne** as the upstream SAML provider. PingFederate and PingOne for Enterprise have different consoles and connection procedures; do not apply these UI steps unchanged to those products.

Review the [shared Entra prerequisites and SAML values](/deployment/infra-how-tos/external-idp-entra-sso).

## Configure PingOne

1. In the intended environment, add a **SAML application**.
2. Under **Configuration**, set **ACS URLs** to the shared ACS and **Entity ID** to the shared audience.
3. Select **persistent** as **Subject NameID format**.
4. Under **Attribute Mappings**, map the subject to a stable user identifier and add the shared email claim, using the user's email. Inspect the actual assertion to confirm both.
5. Select a signing key and use a supported SHA-256 signing configuration. Sign the assertion.
6. Apply the intended authentication and access policies, enable the application, and allow the pilot user.
7. Obtain the application's IdP metadata, issuer, login endpoint, and signing certificate.

If signed authentication requests are enforced, verify compatibility with Entra's request and configure the verification certificate required by PingOne.

## Connect Entra and CluedIn

Complete [Entra federation, guest onboarding, and CluedIn role assignment](/deployment/infra-how-tos/external-idp-entra-sso#configure-entra). Use the resource tenant associated with your CluedIn SSO connection.

Start the pilot sign-in from CluedIn, verify the correct user and role, then test role changes and logout. Provider roles or groups require an explicit authorization design; forwarding them in SAML does not automatically assign CluedIn roles.

{:.important}
Validate this pattern in your deployment before rollout. The provider application authenticates to Entra; its ACS points to Entra rather than CluedIn.

## Troubleshooting

Check the application's authentication policy and attribute mappings. Confirm the configured ACS matches the request. An unrelated IdP-initiated launch failure does not replace a test starting from CluedIn.

## References

- [Add a PingOne application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html)
- [Configure a PingOne SAML application](https://docs.pingidentity.com/pingone/applications/p1_edit_application_saml.html)
