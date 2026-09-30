---
layout: cluedin
nav_order: 4
parent: Configuration
grand_parent: PaaS operations
permalink: /deployment/infra-how-tos/external-idp-entra-sso
title: Federate identity providers through Microsoft Entra
tags: ["authentication", "sso", "entra", "external-idp"]
last_modified: 2026-10-01
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Use Microsoft Entra as an identity broker to let external users authenticate with their existing provider and access CluedIn through its Entra SSO integration. These guides cover **SAML federation into an Entra workforce tenant using B2B guests**.

"Proxy through Entra" means identity federation here: Entra receives the provider's authentication result and issues the token consumed by CluedIn.

{:.important}
These are configuration patterns based on vendor documentation. Validate the complete flow against your CluedIn deployment before rollout. They do not establish that every provider, version, or policy combination has been tested with CluedIn.

## Choose a provider

| Provider | Guide |
|---|---|
| Auth0 | [Auth0 through Entra](/deployment/infra-how-tos/auth0-entra-sso) |
| Okta | [Okta through Entra](/deployment/infra-how-tos/okta-entra-sso) |
| Ping Identity (PingOne) | [PingOne through Entra](/deployment/infra-how-tos/pingone-entra-sso) |
| OneLogin | [OneLogin through Entra](/deployment/infra-how-tos/onelogin-entra-sso) |
| Google Workspace | [Google Workspace through Entra](/deployment/infra-how-tos/google-workspace-entra-sso) |
| Keycloak | [Keycloak through Entra](/deployment/infra-how-tos/keycloak-entra-sso) |

## Prerequisites

First configure [CluedIn Entra SSO](/deployment/infra-how-tos/configure-sso). Identify the resource tenant used by that connection and obtain administrator access to manage federation, guests, and application assignments there. Prepare a provider administrator and a pilot user.

For SaaS, contact [CluedIn support](mailto:support@cluedin.com) when CluedIn SSO configuration needs changing. For multi-tenant SaaS, follow the [customer Enterprise application role guide](/administration/roles/mt-saas-sso-roles).

## Configure the provider

Create the provider's SAML application using these public-cloud workforce values:

| Setting | Value |
|---|---|
| ACS / reply URL | `https://login.microsoftonline.com/login.srf` |
| SP entity ID / audience | `https://login.microsoftonline.com/<ENTRA-TENANT-ID>/` |
| NameID format | `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent` |
| Email claim | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` |

Use a stable subject identifier, map email separately, and export the provider's issuer, login endpoint, signing certificate, and metadata. The provider-specific guides explain where these settings belong.

## Configure Entra

Open **External Identities > All identity providers > Custom > Add new > SAML/WS-Fed**, choose SAML, and import the provider metadata.

For domain-based routing, associate the external email domain and follow Microsoft's DNS TXT requirements when the provider endpoint uses another domain. For verified Entra domains, review invitation redemption order. Domainless federation supports issuer-based routing; use Microsoft's invitation `domain_hint` procedure and note the one-wildcard-provider limit.

Follow [Microsoft's federation instructions](https://learn.microsoft.com/en-us/entra/external-id/direct-federation) for current steps and certificate maintenance.

## Onboard users and assign CluedIn roles

Invite the pilot user as a B2B guest in the resource tenant. Redeem the invitation with the intended provider, then assign application access.

Existing guests can retain a previous authentication association. Inspect redemption state before reusing an existing account; start with a new pilot guest when possible.

Choose the appropriate CluedIn role-management mode:

- **Local roles:** assign roles in CluedIn after first sign-in.
- **Entra roles:** assign the guest or an Entra group to the required CluedIn application role and enable **Automatic Role Synchronization**.

Provider groups and roles do not automatically become Entra memberships or CluedIn roles. Follow [SSO role mapping](/deployment/infra-how-tos/configure-sso#map-microsoft-entra-application-roles-to-cluedin-roles) or the [multi-tenant SaaS role guide](/administration/roles/mt-saas-sso-roles).

Guest access alone does not require converting an application registration to multi-tenant. Review the configured authority and guest handling first.

## Test from CluedIn

In a private browser window:

1. Start at CluedIn and select SSO.
2. Confirm Entra routes authentication to the intended provider.
3. Authenticate and complete any additional access checks.
4. Verify the returned CluedIn identity, organization, and role.
5. Change a role assignment, sign out, and sign in again.
6. Check how an unassigned user is handled.
7. Test logout and subsequent sign-in across all three services.

This tests the application-initiated flow. A provider dashboard tile or its built-in SAML test may exercise a different flow.

Record results without exposing tokens or credentials. Check provider authentication logs and Entra sign-in logs when a step fails.

## Diagnose failures

| Failure stage | Check |
|---|---|
| Entra routes to another method | Domain routing, redemption order, and the guest's provider association. |
| Provider rejects the request | SAML application assignment, audience, ACS, and request-signature requirements. |
| Entra rejects the response | Issuer, signing certificate, persistent NameID, and email claim. |
| CluedIn rejects sign-in | Resource tenant, authority, guest identity mapping, and app assignment. |
| CluedIn permissions are missing | Exact app-role value, assignment, and Automatic Role Synchronization. |

Authentication federation does not provide automatic user lifecycle synchronization. Define how guest invitations, role changes, and access removal are managed. Include session behavior in offboarding tests.

## Other tenant types

These pages cover workforce B2B federation. Entra External ID customer tenants offer custom OIDC federation, but require separate validation of CluedIn endpoints, issuer, claims, and authorization behavior. See [custom OIDC federation](https://learn.microsoft.com/en-us/entra/external-id/customers/how-to-custom-oidc-federation-customers).
