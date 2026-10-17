---
title: Generate an API token
url: https://documentation.cluedin.net/administer/api-token
content_type: how-to
section: Administer
---

# Generate an API token

> how-to: Steps to accomplish one task.

API tokens allow external systems and applications to authenticate and interact with CluedIn programmatically. You can create and manage API tokens directly from the **Administration** section of CluedIn.

## Prerequisites

- You must be signed in to CluedIn Portal.  
- You need appropriate administrative permissions (only administrators can generate or revoke API tokens).  

## Steps to generate an API token

1. **Sign in to CluedIn**.
    - Open your CluedIn environment in your browser and sign in with an account that has administrative privileges.  

2. **Navigate to Administration**.  
   - On the left-hand navigation menu, select **Administration**.  
   - Select **API Tokens** from the options.  

3. **Create a new token**.
   - Select **New Token** or **+ Generate Token**.  
   - Enter a descriptive name for the token (e.g., `Integration_Snowflake_Export` or `MarketingAutomationSync`).  
   - (Optional) Specify a description to clarify its purpose.  

4. **Set token claims**.
   - In the **Claims** section, choose an access level for each claim you want the token to use. The claims and access levels are the same ones used by [role RACI approval controls](https://documentation.cluedin.net/administer/users-and-roles/roles.md#supported-access-levels), grouped by category. See [Claims](https://documentation.cluedin.net/administer/users-and-roles/claims.md) for what each claim governs.  
   - Choose the minimum necessary access level for each claim to follow security best practices (e.g., Informed for read-only access instead of Accountable).  

    A claim left at **None** is not granted to the token. If you don't set any claims, the token can authenticate but won't be able to perform claim-gated actions.

    ![The Claims section of the Create API token panel, with the Duplicates claim set to Responsible and the rest left at None](https://documentation.cluedin.net/assets/images/administration/api-token/claims.png)

5. **(Optional) Set expiry**.
   - If supported in your version, define an expiry date/time for the token.  
   - Tokens without an expiry remain valid until explicitly revoked.  

6. **Generate the token**.
   - Select **Generate**.  
   - CluedIn will display the newly created token.  

7. **Copy and store the token securely**.  
   - Copy the token value immediately and store it in a secure location (e.g., a password vault).

    You will not be able to see the token value again once you leave the page.  

## Manage API tokens

- **View Active Tokens**: The **Administration** > **API Tokens** page lists all currently active tokens.  
- **Revoke a Token**: To disable access, select the token, and then select **Revoke/Delete**. Revocation is immediate.  
- **Audit Usage**: Some environments log usage details (last used timestamp, created by). Review periodically to keep tokens up to date.  

## Best practices

- Generate tokens **per integration** (not shared across multiple apps).  
- Store tokens securely and never embed them in plain text or version control.  
- Use **least privilege** when assigning scopes.  
- Revoke tokens when they are no longer needed.  
- Rotate long-lived tokens regularly as part of your security policy.  

## Summary

You can generate an API token in CluedIn by navigating to **Administration** > **API Tokens**, creating a new token with a descriptive name, setting permissions, and securely storing the generated value. API tokens allow safe, authenticated access to CluedIn’s APIs for integrations and automation.

Up: [Administer](https://documentation.cluedin.net/administer.md)
