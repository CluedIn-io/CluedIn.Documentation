---
category: Administration
title: Removing data
---

# Removing Data for an existing account

You might need to reset your account for many reasons. You could either reset your entire CluedIn instance, create a new account, or reset a particular account. 

A reset of an account will remove all data except the initial 2 records of a User and Account that are created when creating a new CluedIn account. 

You will need to use our REST API, and be an Administrator to be able to run this particular REST command. You will need to supply the OrganizationId of the account that you would like to reset. You can run a `HTTP DELETE` against the `{{url}}/api/Account/client?clientId=<Name of Account>` which will achieve this for you.

Note: On developer machines, it may be easiest to use the Docker option to simply reset your volumes to a default installation of CluedIn. 

# Removing specific data from CluedIn

On occasion you might find that you need to delete data from an account that came from a particular data source. You have many options to take in this situation. 

1. You can retain the data, but set the read access to false for all users in the system for this particular integration point. Beware though that if this data merged with any records from other sources then those records will remain with read access.

1. You can run a REST API command to remove this data. You will need to provide the `ProviderDefinitionId`. This command may take some time to finish because it needs to split entities that involve Clues from that source, remove those Clues and then reprocess. You can run a `HTTP DELETE` against `{{url}}/api/v1/organization/providers/clear?id=<Provider Definition Id>`