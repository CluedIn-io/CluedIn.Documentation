---
layout: default
nav_order: 10
parent: PowerApps Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/powerapps/setup-credentials
title: Setup Credentials
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2023-05-17
---

Enter your [Microsoft 365](https://www.microsoft365.com/) Credentials in CluedIn Settings.
1. Visit the CluedIn web application
2. Navigate to Administration => Settings
3. Scroll down to the Organization Settings section where you find the settings for PowerApps.
![Input Microsoft Purview credentials](./images/cluedin-setting.png)
    - Username
    - Password
    - Redirect Uri (default: http://localhost/)
4. You can find the values for this by navigating to either the PowerApps page or the Power Automate page and checking the Developer Resources information.
![Developer Resources 1](./images/developer-resources1.png)
![Developer Resources 2](./images/developer-resources2.png)
    - **Base Url** is the _Web API endpoint_ base URL
    - Environment Id
5. For Client Id, you can generate this by navigating to your Azure Active Directory => App registration. Please refer to this [link](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/walkthrough-register-app-azure-active-directory).
    - Client Id