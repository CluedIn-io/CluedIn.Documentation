---
category: Misc
---

# Auth Services

## Auth

- get a new token (user token)
- refresh (user token)

NOTE: Maybe auth should be an internal communication to get a new token and proxy by the APP token in order to avoid exposing too much. If a customer would need more, he would need to create an API token.

## Password

- reset password

## API Token

- Get all API tokens (for a given clientId)
- Create a new API Token
- Revoke existing API Token

## Utils

- getUsernameAvailability

## SSO

- get sso providers (app?)
- get auto fill office 365 (app ?)
- get auto fill google (app?)
- save sso provider (app?)
