---
layout: cluedin
title: Generate API token
parent: Administration
permalink: /administration/api-token
tags: ["api token", "api"]

---


# How to Generate an API Token in CluedIn

API Tokens allow external systems and applications to authenticate and interact with CluedIn programmatically. You can create and manage API tokens directly from the **Administration** section of the CluedIn Portal.

---

## Prerequisites

- You must be logged into the **CluedIn Portal**.  
- You need appropriate **administrative permissions** (only Administrators can generate or revoke API tokens).  

---

## Steps to Generate an API Token

1. **Log in to the CluedIn Portal**  
   Open your CluedIn environment in your browser and log in with an account that has administrative privileges.  

2. **Navigate to Administration**  
   - From the left-hand navigation menu, click on **Administration**.  
   - Select **API Tokens** from the options.  

3. **Create a New Token**  
   - Click the **New Token** or **+ Generate Token** button.  
   - Enter a descriptive name for the token (e.g., `Integration_Snowflake_Export` or `MarketingAutomationSync`).  
   - (Optional) Specify a description to clarify its purpose.  

4. **Set Token Permissions/Scope**  
   - Select the scope or permissions you want the token to have.  
   - Choose the minimum necessary permissions to follow security best practices (e.g., read-only vs full write).  

5. **Set Expiry (Optional)**  
   - If supported in your version, define an expiry date/time for the token.  
   - Tokens without an expiry remain valid until explicitly revoked.  

6. **Generate the Token**  
   - Click **Generate**.  
   - CluedIn will display the newly created token.  

7. **Copy and Store the Token Securely**  
   - Copy the token value immediately and store it in a secure location (e.g., a password vault).  
   - **Important**: You will not be able to see the token value again once you leave the page.  

---

## Managing API Tokens

- **View Active Tokens**: The Administration → API Tokens page lists all currently active tokens.  
- **Revoke a Token**: To disable access, select the token and choose **Revoke/Delete**. Revocation is immediate.  
- **Audit Usage**: Some environments log usage details (last used timestamp, created by). Review periodically to keep tokens up to date.  

---

## Best Practices

- Generate tokens **per integration** (not shared across multiple apps).  
- Store tokens securely and never embed them in plain text or version control.  
- Use **least privilege** when assigning scopes.  
- Revoke tokens when they are no longer needed.  
- Rotate long-lived tokens regularly as part of your security policy.  

---

## Summary

You can generate an API token in CluedIn by navigating to **Administration → API Tokens**, creating a new token with a descriptive name, setting permissions, and securely storing the generated value. API tokens allow safe, authenticated access to CluedIn’s APIs for integrations and automation.
