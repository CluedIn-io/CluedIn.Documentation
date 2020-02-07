Removing specific data from CluedIn

On occasion you might find that you need to delete data from an account that came from a particular data source. You have many options to take in this situation. 

1: You can retain the data, but set the read access to false for all users in the system for this particular integration point. (Cons: if this data merged with any records from other sources then those records will remain with read access)

2: You can run a REST API command to remove this data. You will need to provide the ProviderDefinitionId. This command may take some time to finish due to the nature of it needing to split entities that envolve Clues from that source, remove those Clues and then reprocess. You can run a HTTP DELETE against {{url}}/api/v1/organization/providers/clear?id=<Provider Definition Id>