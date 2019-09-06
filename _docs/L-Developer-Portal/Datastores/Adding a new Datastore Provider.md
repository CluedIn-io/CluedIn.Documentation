Adding a new Datastore Provider

There are many types of database families today. Leveraging these different datastores provides flexiblity when it comes to using this data. 

Due to this, it might be that you are interested in storing your data in another datastore type that is not currently shipped with CluedIn. For example, if we wanted to provide support for your data in a Time Series database, this is where you would need to implement a brand new datastore. 

To implement a new datastore, you will need to do two main steps. 

1: Implementing the IDataStore interface.

2: Injecting your new implementation into the Container of CluedIn. 

You will then want to inherit from the ExecutionContext of CluedIn and inject your new Store as a Static instance of your new type of Datastore. This means that your new store is globally available when an ExecutionContext is available. 