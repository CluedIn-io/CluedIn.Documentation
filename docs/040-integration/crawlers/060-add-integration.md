---
layout: cluedin
title: Add an integration
parent: Crawlers
grand_parent: Ingestion
nav_order: 060
has_children: false
permalink: /integration/add-integration
tags: ["integration"]
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

An integration in CluedIn should not be tied to a specific user. When installed, an integration typically accepts parameters so it can be added multiple times for different users or contexts. Examples include:

- Slack accounts from multiple organizations.

- Multiple shared email inboxes from the same Exchange server.

- Multiple Office 365 accounts.

For details, see [Build an integration](./build-integration).

When installing an integration:

- To allow read-only access, add the integration with a user account that has read-only permissions to all relevant data.

- To allow push-back (write access), add the integration with an administrator account.

## Types of integration

Integrations fall under the following types:

- Cloud integrations

- On-premise integrations

### Cloud integrations

Cloud integrations connect CluedIn to existing SaaS products such as HubSpot, Slack, or Dropbox.

To authenticate a cloud integration, CluedIn supports three methods (the method varies by product):

- OAuth authentication – You are redirected to the integration’s website, where you grant CluedIn permission to access your data.

- API token – You provide a valid API token so CluedIn can access the data.

- Form fields – Some integrations require multiple fields (for example, URL, username). Make sure you have the correct details before configuring them.

{:.important}
If you are running CluedIn on-premises, you must set up the OAuth process with the product you want to add. Refer to the provider’s documentation for setup steps.

### On-premise integration

On-premise integrations are installed on your own servers. A common example is the File System provider, which scans files located on a physical hard drive.

## Add an integration

1. Sign in to CluedIn.

1. Go to the **Integration** section.

1. Select **Available integrations**.

     ![available-integration]({{ "/assets/images/integration/integration-add-1.png" | relative_url }})

1. Select **Add configuration**.

    ![available-integration]({{ "/assets/images/integration/integration-add-2.png" | relative_url }})

1. Follow the authentication process.

    ![available-integration]({{ "/assets/images/integration/integration-add-3.png" | relative_url }})

6. Configure your integration and add it.

    You have added the integration.

    ![available-integration]({{ "/assets/images/integration/integration-add-4.png" | relative_url }})

## Data coming in

Once an integration is added, CluedIn will ingest the data. When the ingestion is complete, you will receive a notification.

## Product Owner

You can set the Product Owner when you add an integration:

- Multiple Product Owners can be assigned.

- The Product Owner role can change throughout the lifetime of the integration.

Setting a Product Owner defines certain actions and responsibilities, including:

 - Accepting or rejecting Mesh Commands.

 - Receiving notifications when a Subject Request Access contains data for this integration point.

 - Taking responsibility for CluedIn [clean projects](/preparation/clean) that use data from this integration.

 - Being notified if their system is involved in a data breach.

 - Accepting or rejecting data involved in a retention setup. 

 - Setting the Consent for properties in their integration.

 - Resolving duplicates in their integration point. 

 - Managing provider-specific vocabularies and mappings to core vocabulary keys.
 
## Integration access

![Diagram]({{ "/assets/images/integration/setting-access-at-integration-level.png" | relative_url }})

