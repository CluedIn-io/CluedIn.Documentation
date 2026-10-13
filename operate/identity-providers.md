---
title: External identity providers
url: https://documentation.cluedin.net/operate/identity-providers
content_type: landing
section: Deploy & operate
---

# External identity providers

CluedIn's single sign-on is wired to Microsoft Entra ID; setting that up is covered in [SSO](https://documentation.cluedin.net/operate/configuration/configure-sso.md). When your users authenticate with a different provider, Entra acts as the broker: the provider signs the user in, and Entra issues the token CluedIn consumes.

Start with [Federate identity providers through Microsoft Entra](https://documentation.cluedin.net/operate/identity-providers/external-idp-entra-sso.md), which covers the steps common to every provider, then follow the page for yours. Which CluedIn role a signed-in user gets is configured separately, in [Users and roles](https://documentation.cluedin.net/administer/users-and-roles.md).

## In this section

- [Federate identity providers through Microsoft Entra](https://documentation.cluedin.net/operate/identity-providers/external-idp-entra-sso.md) (how-to): Use Microsoft Entra as an identity broker to let external users authenticate with their existing provider and access CluedIn through its Entra SSO integration.
- [Sign in with Auth0 through Microsoft Entra](https://documentation.cluedin.net/operate/identity-providers/auth0-entra-sso.md) (how-to): You can use Auth0 credentials to sign in to CluedIn through Microsoft Entra federation.
- [Sign in with Okta through Microsoft Entra](https://documentation.cluedin.net/operate/identity-providers/okta-entra-sso.md) (how-to): Use Okta as the upstream SAML provider and Entra as the token issuer for CluedIn.
- [Sign in with PingOne through Microsoft Entra](https://documentation.cluedin.net/operate/identity-providers/pingone-entra-sso.md) (how-to): This guide covers PingOne as the upstream SAML provider.
- [Sign in with OneLogin through Microsoft Entra](https://documentation.cluedin.net/operate/identity-providers/onelogin-entra-sso.md) (how-to): Use the OneLogin SAML Custom Connector (Advanced) to authenticate users upstream of Entra.
- [Sign in with Google Workspace through Microsoft Entra](https://documentation.cluedin.net/operate/identity-providers/google-workspace-entra-sso.md) (how-to): Use a Google Workspace custom SAML app to authenticate managed Workspace users through Entra.
- [Sign in with Keycloak through Microsoft Entra](https://documentation.cluedin.net/operate/identity-providers/keycloak-entra-sso.md) (how-to): Use a Keycloak realm as the upstream SAML provider.

Up: [Deploy & operate](https://documentation.cluedin.net/operate.md)
