---
layout: cluedin
nav_order: 3
parent: Configuration
grand_parent: PaaS operations
permalink: /deployment/infra-how-tos/auth0-entra-sso
title: Sign in with Auth0 through Microsoft Entra
tags: ["authentication", "sso", "entra", "auth0"]
last_modified: 2026-10-01
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

You can use Auth0 credentials to sign in to CluedIn through Microsoft Entra federation. CluedIn continues to use its Entra SSO integration; Auth0 authenticates the user upstream.

This guide describes SAML federation into an **Entra workforce tenant**, with users represented as B2B guests. It builds on [Configure SSO](/deployment/infra-how-tos/configure-sso).

{:.important}
This is a federation configuration guide, not a guarantee of compatibility with every CluedIn deployment. Validate guest sign-in, identity mapping, and role assignment in your instance before rollout. For SaaS, contact [CluedIn support](mailto:support@cluedin.com) if SSO configuration changes are required.

## How sign-in works

1. The user starts from the CluedIn sign-in page and selects the configured SSO option.
2. CluedIn sends the user to Microsoft Entra.
3. Entra routes authentication to Auth0.
4. Auth0 authenticates the user and returns a SAML assertion to Entra.
5. Entra completes sign-in and returns an Entra-issued token to CluedIn.
6. CluedIn identifies the user and applies its configured role-management mode.

The SAML exchange is between Auth0 and Entra. The existing CluedIn-to-Entra connection remains the application-facing SSO connection.

## Prerequisites

Before configuring federation, prepare:

- Working [Entra SSO for CluedIn](/deployment/infra-how-tos/configure-sso).
- An Auth0 administrator and an Entra administrator authorized to manage external identity providers and guest invitations.
- One test user in Auth0, with a stable identifier and an accurate email address.
- Access to the CluedIn Enterprise application and its user or role assignments.
- A test environment or an agreed pilot in which to check guest access.

Confirm which Entra tenant issues tokens to CluedIn. Configure federation and guest access in that resource tenant. For multi-tenant SaaS, use the customer tenant associated with the CluedIn Enterprise application and follow the [multi-tenant SaaS role guide](/administration/roles/mt-saas-sso-roles).

## Configure Auth0

Create a dedicated application for the Entra federation connection.

1. In Auth0, open **Applications > Applications** and create or select the application.
2. Enable the intended user connection for this application.
3. Under **Addons**, enable **SAML2 Web App**.
4. Set its callback URL to Entra's ACS endpoint.
5. Configure the audience, email mapping, and persistent NameID.
6. From the addon's **Usage** view, obtain the issuer, login endpoint, signing certificate, and metadata.

Use these values for an Entra workforce tenant in the Microsoft public cloud:

| Setting | Value |
|---|---|
| Callback / ACS | `https://login.microsoftonline.com/login.srf` |
| Audience | `https://login.microsoftonline.com/<ENTRA-TENANT-ID>/` |
| NameID format | `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent` |
| Email attribute | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` |

The Auth0 callback above belongs to Entra. Keep CluedIn's own redirect URI on its Entra application registration.

The following illustrates the SAML2 Web App settings. Replace the tenant placeholder and verify the resulting assertion:

```json
{
  "audience": "https://login.microsoftonline.com/<ENTRA-TENANT-ID>/",
  "recipient": "https://login.microsoftonline.com/login.srf",
  "destination": "https://login.microsoftonline.com/login.srf",
  "mappings": {
    "user_id": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier",
    "email": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
  },
  "nameIdentifierFormat": "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
  "nameIdentifierProbes": [
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier"
  ],
  "signatureAlgorithm": "rsa-sha256",
  "digestAlgorithm": "sha256",
  "passthroughClaimsWithNoMapping": false,
  "mapIdentities": false
}
```

Use a stable NameID rather than an identifier that changes with the user's email. Review any Auth0 Actions that override SAML settings. See [Customize SAML assertions](https://auth0.com/docs/authenticate/protocols/saml/saml-configuration/customize-saml-assertions) for the available parameters.

## Configure Entra federation

In the resource tenant, open **External Identities > All identity providers > Custom > Add new > SAML/WS-Fed**. Select **SAML** and import Auth0 metadata or enter its issuer, HTTPS login endpoint, and signing certificate.

For domain-based federation, associate the users' email domain. If the Auth0 login endpoint uses a different domain, follow Microsoft's DNS TXT verification instructions. For domains already verified in Entra, review B2B invitation redemption order to prioritize SAML federation where appropriate.

For users across unrelated email domains, Microsoft's **domainless federation** option supports issuer-based routing. Follow its invitation `domain_hint` instructions; only one wildcard provider is supported per tenant.

Use [Microsoft's federation guide](https://learn.microsoft.com/en-us/entra/external-id/direct-federation) for current portal steps, domainless routing, cloud-specific endpoints, and certificate renewal.

## Invite the test user and assign access

Invite the Auth0 test user as a B2B guest in the resource tenant, then redeem the invitation using Auth0. Confirm the redeemed guest identity is associated with the intended provider before testing CluedIn.

An existing guest may already be associated with another authentication method. Review the guest's redemption state before reusing it; a newly invited pilot user makes the initial test easier to interpret.

Assign the guest to the CluedIn Enterprise application as required by your access policy.

Choose one of the existing CluedIn role-management modes:

- **Local role management:** assign the appropriate CluedIn role in the UI after initial sign-in.
- **Entra-managed roles:** assign the guest or an appropriate group to the required application role and enable **Automatic Role Synchronization** in CluedIn.

Auth0 roles do not automatically become CluedIn roles. Entra must issue the role claims expected by CluedIn. Use the role values documented in [Configure SSO](/deployment/infra-how-tos/configure-sso#map-microsoft-entra-application-roles-to-cluedin-roles), or the [multi-tenant SaaS role guide](/administration/roles/mt-saas-sso-roles) for that deployment type.

B2B guest access does not inherently require changing a single-tenant application into a multi-tenant application. Check the configured authority, account types, and guest handling for your deployment before changing the application registration.

## Verify the complete flow

Use a private browser window and start at CluedIn:

1. Select SSO and confirm authentication reaches Auth0.
2. Sign in with the pilot account and complete any required Entra access checks.
3. Confirm the browser returns to CluedIn.
4. Verify the expected user identity and organization membership.
5. Check that the assigned role permits the intended actions.
6. Change a role assignment, sign out, and sign in again to verify synchronization.
7. Test an unassigned user against your application's access policy.
8. Test logout and subsequent sign-in to understand which sessions remain active.

Record the Auth0 application, Entra tenant, guest object, role assignments, and test results. Avoid sharing tokens, assertions, or credentials in diagnostic reports.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Entra uses another sign-in method | Federation routing, invitation redemption order, and the guest's existing provider association. |
| Auth0 reports a callback error | The SAML addon's callback points to Entra's ACS endpoint. |
| Entra rejects the assertion | Audience, issuer, signature, certificate, NameID, and email mapping. |
| Email-domain mismatch | Domain-based federation configuration, or domainless routing if appropriate. |
| Entra succeeds but CluedIn rejects sign-in | Resource tenant, configured authority, guest identity claims, and application assignment. |
| Sign-in works but permissions are missing | Entra app-role assignment, exact role value, and Automatic Role Synchronization. |
| Logout immediately signs the user in again | Remaining Auth0 or Entra browser sessions; test the complete logout behavior. |

Check both Auth0 authentication logs and Entra sign-in logs to identify which stage failed.

## Alternative: Entra External ID customer tenant

Entra External ID customer tenants support custom OIDC providers, offering another way to federate Auth0. That route uses an external tenant application registration and sign-in user flow.

Treat it as a separate architecture choice. Confirm CluedIn compatibility with the external tenant's endpoints, issuer, claims, and role model before adopting it. An existing workforce-tenant integration alone does not establish that compatibility.

See [Add a custom OIDC provider](https://learn.microsoft.com/en-us/entra/external-id/customers/how-to-custom-oidc-federation-customers).

## References

- [Configure Auth0 as a SAML identity provider](https://auth0.com/docs/authenticate/single-sign-on/outbound-single-sign-on/configure-auth0-saml-identity-provider)
- [Customize Auth0 SAML assertions](https://auth0.com/docs/authenticate/protocols/saml/saml-configuration/customize-saml-assertions)
- [Configure Entra SAML/WS-Fed federation](https://learn.microsoft.com/en-us/entra/external-id/direct-federation)
