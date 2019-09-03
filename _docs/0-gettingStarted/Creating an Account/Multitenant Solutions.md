Multitenant Solutions

CluedIn has Multitenant support natively. This means that you can run multiple different CluedIn accounts, all from the same CluedIn instance. The data is isolated from each other, there is no way to bridge data from different CluedIn accounts, even within the same CluedIn instance. 

Multitenant solutions are appropriate where you need to isolate data into respective groups. It is required that each account has its own unique name and mapped to a unique domain. It is also required that each user is unique, even across accounts i.e. a user can only exist in one account. 

Data isolation is implemented differently at each store level. 

Search Store: A seperate index is created per account, but remains within the same cluster. 
Graph Store: All data is included in the same Graph, but is isolated at the application level using Labels to filter by account. 
Relational Store: All data exists within the same Database, but uses application isolation to filter data by account. 
Blob Store: All data exists within the same Database, but uses application isolation to filter data by account. 
Redis Store: All data exists within the same Database, but uses application isolation to filter data by account. 