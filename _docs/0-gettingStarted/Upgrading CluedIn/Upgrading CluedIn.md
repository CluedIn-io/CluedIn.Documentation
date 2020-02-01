Upgrading CluedIn

To upgrade CluedIn, you will need to take many things into consideration. 

CluedIn deploys new versions of its software, crawlers and other products to the CluedIn Private Docker Repository. We deploy Stable, Beta and Alpha versions so that our customers can try out different parts of the platform at their disgression.

It is always recommended to first check the release notes of the version you are upgrading to. You might find that if you are jumping a large number of versions, that the upgrade path is harder than smaller increments. If you have adhered to the best practices of CluedIn, then upgrading should be very straight forward. In essence, we offer ways for Developers to inject changes to CluedIn but very much do not recommend changing default CluedIn behaviour. If you have adhered to this then it will make your upgrade paths easier. 

It is also a recommended practice that you also don't directly connect to the CluedIn datastores, but rather use our API's to interact with the underlying datastores. If you have stuck to this principal, then changes to the underlying data stores can be automated during the upgrade process. 

You may find that certain updates will require you to reprocess the data within your account. The release notes will detail if you will need to run this process or other processes to make data updates if necessary. 

If you have chosen the Docker path of deploying CluedIn then you will need to use your Docker-Compose.yml file to change to the version you would like to upgrade to. We do not suggest changing the dependency versions of other CluedIn dependencies unless it has been specifically santcioned and supported by CluedIn. For example, changing the version of one of the Datastores could result in issues and will not be covered in the support models we provide. Each version of CluedIn will specifically detail which versions of dependencies that it supports.

If you have chosen the Kubernetes and Docker approach to deploying CluedIn then you will also inherit support for automatic rollback of a deployment if it fails. This means that you can upgrade or attempt to upgrade your CluedIn instance with full confidence that if it fails, you will not break anything.