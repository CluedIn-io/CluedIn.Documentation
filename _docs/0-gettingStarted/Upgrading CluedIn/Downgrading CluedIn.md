Downgrading CluedIn

Although downgrading is no typically something that is done, there may be times where you need to rollback a deployment. 

If you have chosen the Kubernetes and Docker path for installation then this will make the downgrade/rollback much easier. Rollback support is built into the Helm charts that CluedIn deploys with. This means that certain tests and checks will need to pass for a deployment to be deemed successful. CluedIn will automatically rollback if this is not passed. 