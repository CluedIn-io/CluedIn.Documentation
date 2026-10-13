---
title: Sign in with Keycloak through Microsoft Entra
url: https://documentation.cluedin.net/operate/identity-providers/keycloak-entra-sso
content_type: how-to
section: Deploy & operate > External identity providers
---

# Sign in with Keycloak through Microsoft Entra

> how-to: Steps to accomplish one task.

Use a Keycloak realm as the upstream SAML provider. Review the [shared Entra prerequisites and SAML values](https://documentation.cluedin.net/operate/identity-providers/external-idp-entra-sso.md). Console labels can vary by Keycloak version.

## Configure Keycloak

1. In the intended realm, create a client with type **SAML**.
2. Set its **Client ID** to the shared Entra audience.
3. Register the shared ACS under **Valid Redirect URIs**, using the exact URL.
4. Under **Fine Grain SAML Endpoint Configuration**, set **Assertion Consumer Service POST Binding URL** to the shared ACS.
5. Set **Name ID Format** to **persistent** and **Force POST Binding** to on. Confirm the emitted NameID matches Entra's requirements.
6. Enable **Sign Assertions** and use a supported SHA-256 signing configuration.
7. Add a **User Property** SAML mapper for `email`; set its SAML attribute name to the shared email claim and its name format to URI.
8. Obtain the realm's SAML IdP descriptor, issuer, SSO endpoint, and signing certificate.

Do not configure Entra under Keycloak's **Identity Providers** for this direction of federation. Entra is the service provider represented by the SAML client.

Prefer the explicit ACS POST endpoint over treating a shared Master SAML Processing URL as a complete logout configuration. Test logout separately.

## Connect Entra and CluedIn

Complete [Entra federation, guest onboarding, and CluedIn role assignment](https://documentation.cluedin.net/operate/identity-providers/external-idp-entra-sso.md#configure-entra). Use the resource tenant associated with your CluedIn SSO connection.

Start the pilot sign-in from CluedIn, verify the correct user and role, then test role changes and logout. Provider roles or groups require an explicit authorization design; forwarding them in SAML does not automatically assign CluedIn roles.

> **Important:** Validate this pattern in your deployment before rollout. The provider application authenticates to Entra; its ACS points to Entra rather than CluedIn.

## Troubleshooting

Check that the client ID exactly matches Entra's audience, including the trailing slash. Inspect realm events and the email mapper. Ensure the public HTTPS hostname in metadata is reachable and consistent with the deployed reverse-proxy configuration.

## References

- [Keycloak Server Administration Guide](https://www.keycloak.org/docs/latest/server_admin/index.html)

Up: [External identity providers](https://documentation.cluedin.net/operate/identity-providers.md)
