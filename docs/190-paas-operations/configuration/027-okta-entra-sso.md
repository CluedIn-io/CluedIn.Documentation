---
layout: cluedin
nav_order: 5
parent: Configuration
grand_parent: PaaS operations
permalink: /deployment/infra-how-tos/okta-entra-sso
title: Sign in with Okta through Microsoft Entra
tags: ["authentication", "sso", "entra", "okta"]
last_modified: 2026-10-01
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Use Okta as the upstream SAML provider and Entra as the token issuer for CluedIn. Review the [shared prerequisites and SAML values](/deployment/infra-how-tos/external-idp-entra-sso) first.

## Configure Okta

1. Open **Applications > Applications > Create App Integration** in the Okta Admin Console.
2. Select **SAML 2.0** and give the integration a descriptive name.
3. Use the shared **ACS** as **Single sign-on URL**, and the shared **audience** as **Audience URI (SP Entity ID)**.
4. Choose **Persistent** as the **Name ID format**. Configure an administrator-managed, stable application username; do not rely on a user-editable profile field.
5. Add an attribute statement named `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`, mapped to the user's email.
6. Finish the integration, assign the pilot user or group, and obtain the IdP metadata and signing certificate from its sign-on settings.

Inspect the emitted NameID across repeated sign-ins. Preserve it when email changes. Review any application username update behavior.

## Connect Entra and CluedIn

Complete [Entra federation, guest onboarding, and CluedIn role assignment](/deployment/infra-how-tos/external-idp-entra-sso#configure-entra). Use the resource tenant associated with your CluedIn SSO connection.

Start the pilot sign-in from CluedIn, verify the correct user and role, then test role changes and logout. Provider roles or groups require an explicit authorization design; forwarding them in SAML does not automatically assign CluedIn roles.

{:.important}
Validate this pattern in your deployment before rollout. The provider application authenticates to Entra; its ACS points to Entra rather than CluedIn.

## Troubleshooting

Check Okta application assignment and the System Log when the user cannot reach authentication. If Entra rejects the assertion, inspect the NameID format and email attribute rather than using the wizard's default email NameID settings.

## References

- [Create SAML integrations](https://help.okta.com/en-us/Content/Topics/Apps/apps_app_integration_wizard_saml.htm)
- [SAML field reference](https://help.okta.com/en-us/Content/Topics/Apps/aiw-saml-reference.htm)
