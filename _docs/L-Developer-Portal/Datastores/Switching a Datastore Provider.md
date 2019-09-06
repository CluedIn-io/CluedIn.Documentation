Switching a Datastore Provider

CluedIn ships with many different datastore implementations. This gives you a choice on what system will host your data. It may be that you would rather use PostGres or MySQL than SQL Server for the Relational Store. It maybe that you would like to use a cloud SQL provider via PAAS. The Datastore abstraction layer allows you to support this change. 

To change your implementation of a particular store requires two pieces:

1: Implementing the IDataStore interface and the specific provider interface you would like to implement e.g. IRelationalDataStore. 

2: Injecting your new implementation into the Container of CluedIn. 