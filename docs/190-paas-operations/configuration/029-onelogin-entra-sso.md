---
layout: cluedin
nav_order: 7
parent: Configuration
grand_parent: PaaS operations
permalink: /deployment/infra-how-tos/onelogin-entra-sso
title: Sign in with OneLogin through Microsoft Entra
tags: ["authentication", "sso", "entra", "onelogin"]
last_modified: 2026-10-01
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Use the OneLogin **SAML Custom Connector (Advanced)** to authenticate users upstream of Entra. Begin with the [shared prerequisites and SAML values](/deployment/infra-how-tos/external-idp-entra-sso).

## Configure OneLogin

1. Add **SAML Custom Connector (Advanced)** in the administrator portal.
2. Under **Configuration**, set **Audience (EntityID)** to the shared audience. Set **Recipient** and **ACS (Consumer) URL** to the shared ACS.
3. Set **ACS (Consumer) URL Validator** to the exact anchored expression below.
4. Set **SAML initiator** to **Service Provider** and **SAML nameID format** to **Persistent**. Select assertion signing.
5. Under **Parameters**, add the shared email claim, map it to Email, and include it in the SAML assertion.
6. Grant the pilot user application access and obtain issuer, SAML endpoint, certificate, and metadata from the SSO settings.

For the Microsoft public-cloud workforce ACS, the validator is:

```text
^https:\/\/login\.microsoftonline\.com\/login\.srf$
```

Verify the persistent subject in the emitted assertion. Avoid permissive ACS wildcard expressions.

## Connect Entra and CluedIn

Complete [Entra federation, guest onboarding, and CluedIn role assignment](/deployment/infra-how-tos/external-idp-entra-sso#configure-entra). Use the resource tenant associated with your CluedIn SSO connection.

Start the pilot sign-in from CluedIn, verify the correct user and role, then test role changes and logout. Provider roles or groups require an explicit authorization design; forwarding them in SAML does not automatically assign CluedIn roles.

{:.important}
Validate this pattern in your deployment before rollout. The provider application authenticates to Entra; its ACS points to Entra rather than CluedIn.

## Troubleshooting

If OneLogin rejects the ACS, check the anchored validator and the actual requested URL. If authentication succeeds but Entra rejects the response, confirm the email parameter is included in SAML and that Persistent was selected instead of the default email format.

## References

- [Advanced SAML Custom Connector](https://onelogin.service-now.com/kb?id=kb_article_view&sysparm_article=KB0011004)
- [Configure SAML-enabled applications](https://onelogin.service-now.com/kb?id=kb_article_view&sysparm_article=KB0010398)
