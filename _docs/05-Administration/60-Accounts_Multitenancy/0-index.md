---
category: Administration
title: Multitenancy
---

## Multiple accounts

CluedIn has multi-tenant support natively. This means that you can run multiple different CluedIn accounts, all from the same CluedIn instance. The data is isolated from each other, there is no way to bridge data from different CluedIn accounts, even within the same CluedIn instance. 

Multi-tenant solutions are appropriate when you need to isolate data into respective groups. It is required that each account has its own unique name and mapped to a unique subdomain. It is also required that each user is unique, even across accounts i.e. a user can only exist in one account. 

Data isolation is implemented differently at each store level. In the _Search Store_ a separate index is created per account, but remains within the same cluster. Data in all the other stores, _Graph_, _Relational_, _Blob_ and _Redis_, exists within the same database but is isolated at an application level. 

There are some restricted names on what you can call your CluedIn account. These are controlled via the configuration setting `ReservedOrganizationIds` in your `container.config` (or via the `values.yaml` file if using Kubernetes for deployment).

Check the [installation instructions](/docs/00-gettingStarted/create-organization.html) to create new accounts.

## FAQ
#### Can you bridge data from two accounts into one?

There are special administrator end points that allow you to do this. You might find that you want to start out ingesting data from different sources into different accounts and only merge them when you are happy with the results. 

#### Why would I want to use multi-tenancy?

If you have one installation of CluedIn, but you have very different use cases and data sources that must be isolated with no blending of data across data sources, then this would be a good reason to support multitenancy. Your CluedIn license has no restrictions on how many accounts you can have - so it is more about organization of data more than anything.

#### Can I host all my customers on one CluedIn instance, but have different accounts for each?

If you are a partner of CluedIn, you will know that you cannot use the same license across customers unless agreed with your CluedIn account manager.

#### Can I have multi-tenant support, but each customer gets their own database instances?

Yes, you technically can but you have to be aware of the cost overheads of running it like this. It will most likely be more advantageous to simply run different instances. 

#### Can I run CluedIn without an organisation account?

No. CluedIn is intended to be an application that runs on a server, not on your local developer machine and hence everything is setup in a way that is secure by default. This shows itself in many ways including the fact that you cannot run CluedIn without HTTPS and SSL. 