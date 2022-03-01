---
layout: default
nav_order: 2
parent: Kubernetes
grand_parent: Deployment
permalink: /deployment/kubernetes/kubernetes-sample-prerequisites
title: Example pre-requisite configuration
tags: ["deployment", "kubernetes", "prerequisites"]
---
### Example pre-requisite configuration

Creating the Kubernetes cluster is outside the scope of this guide. 

Refer to: [Microsoft Azure AKS documentation](https://docs.microsoft.com/en-us/azure/aks/windows-container-cli).
*The ability of creating AKS clusters with Windows support is currently in Preview. If you have multiple accounts in Azure then you will need to use the `az account set -s <AccountName>` so that you can set the right context for the deployment.*

You must have:
- a local install of [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl) configured to talk to the cluster
- a local install of the CLI for [helm](https://helm.sh/).

1. Create a service account. If you are using RBAC in your Kubernetes cluster you will need to grant permissions to *Tiller* for it to be able to create resources in the cluster. Check [Helm's documentation](https://helm.sh/docs/using_helm/#rbac). In test environments, you may consider just granting Tiller cluster admin permissions:

    - Create a file with the following content

        ```yaml
        apiVersion: v1
        kind: ServiceAccount
        metadata:
            name: tiller
            namespace: kube-system
        ---
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRoleBinding
        metadata:
            name: tiller
        roleRef:
            apiGroup: rbac.authorization.k8s.io
            kind: ClusterRole
            name: cluster-admin
        subjects:
        -   kind: ServiceAccount
            name: tiller
            namespace: kube-system
        ```
        _In production scenarios you will have to be more restrictive with the permissions. See [Helm's documentation](https://helm.sh/docs/using_helm/#securing-your-helm-installation) for advice on security for production environments_
    
    - Run `kubectl apply -f <path-of-file>` to create the role binding
    
    
    If not using RBAC, you will need to run the following
    
    ```powershell
    kubectl create serviceaccount --namespace kube-system tiller
    
    kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
    
    kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}
    ```


1. If using RBAC, execute `helm init --service-account tiller`. This will install *Tiller* in the cluster, so you can install helm charts directly. If not using RBAC, do not use the service account parameter.

1. Install the ingress controller:
    ```powershell
    helm install stable/nginx-ingress \
        --namespace ingress \
        --name ingress  \
        --set rbac.create="true" \
    ```

    After a while the ingress controller will have a public IP that can be used to access the cluster. If you don't want a public IP (because you have something else, like an application gateway in front of it), you can modify the installation of the ingress controller in the step above - see Helm chart [documentation](https://docs.nginx.com/nginx-ingress-controller/installation/installation-with-helm/) (controller.service.loadBalancerIP).

1. To retrieve the public IP:

    ```powershell
    kubectl get svc -n ingress -o wide -l 'component=controller'
    ```
    In your own DNS, configure that IP to whatever host you want to use for CluedIn. You could map it to a wildcard record; alternatively you can use [more specific entries](./ssl).

1. Create a secret with your docker hub login credentials:

    ```powershell
    kubectl create secret docker-registry  docker-registry-key \
        --docker-server='<repository-url>' \
        --docker-username='<your username>' \
        --docker-password='<your password>' \
        --docker-email='<your email>'
    ```
    For Docker Hub, the *repository-url* is ```docker.io```.
    You should request access to the CluedIn Docker Hub repo for those credentials so you can pull the private Docker images with the application.

1. Register the CluedIn helm chart

    ```powershell
    helm repo add cluedin https://cluedin-io.github.io/CluedIn.Helm
    helm repo update
    ```

NOTE: You can also place secrets into a Vault or Key Vault from your cloud provider of choice.

![Diagram](../../assets/images/deployment/azure-aks.png)

### CluedIn Custom Resources for Kubernetes

> **Note**: Only available in CluedIn v3.2.4 onwards

Custom resources are a set of versioned business objects that extend the Kubernetes API. The goal of these objects is to simply performing certain administrative tasks within CluedIn that would normally be quite complex.

CluedIn Custom Resources are monitored and actioned by the `CluedIn Controller` service.

Currently, two actions are supported:
1) Creating/Deleting a CluedIn organization
2) Enabling/Disabling SSO

> **Note**: These guides assume you have access to the cluster via `kubectl` 

#### Creating an organization

> **Note**: This action would happen *instead* of the bootstrap mentioned above.

We will create a new organization called `foobar` by creating a Custom Resource (CR) and installing it into the Kubernetes cluster.

1) Create a secret to hold the administrator email and administrator password for the organization. We create a secret as this is sensitive data we wish to protect.
  
  ```bash
  kubectl create secret generic "foobar-admin" -n cluedin --from-literal=username="admin@foobar.com" --from-literal=password="Foobar23!"
  ```
  
  .. this will create a resource that would look like:
  
  ```yaml
  apiVersion: v1
  kind: Secret
  metadata:
    name: foobar-admin
  data:
    username: YWRtaW5AZm9vYmFyLmNvbQ==
    password: Rm9vYmFyMjMh
  ```

2) Create a custom resource for the new `foobar` organization. You can see we reference the secret name in the `adminUserSecret` property.

  ```yaml
  # File: foobar-org.yaml
  apiVersion: "api.cluedin.com/v1"
  kind: Organization
  metadata:
    name: foobar-organization
  spec:
    name: "foobar"
    adminUserSecret: "foobar-admin"
  ```
  .. you can apply the resource to the Kubernetes cluster to begin the creation process using :
  ```bash
  kubectl apply -n cluedin -f foobar-org.yaml
  ```
  .. this will create a new organization in CluedIn and also create an administrator account with the email and password defined in the secret.
  

#### Checking Organization status

The `STATUS` field of an organization displays its current progress. You can list the `Organization` resources in a namespace by using : 

```bash
kubectl get organizations -n cluedin
```

If the `STATUS` is `Organization [foobar] activated` then we know the `foobar` organization has been created successfully. 
A successfully created organization will also display an `Organization ID`.
Any error messages from the process will be stored in the `STATUS` field and the`Controller` will re-try periodically.

#### Deleting an Organization

  You can remove entirely remove an organization by deleting the custom `Organization` resource that was created previously.
  
  It can be deleted by using the file it was created with ..

  ```bash
  kubectl delete -n cluedin -f foobar-org.yaml
  ```

.. or by using its name (e.g. `foobar-organization`) directly ..

```bash
kubectl delete organization -n cluedin foobar-organization
```

> **Warning**: This action will also remove all data for the organization. Including SQL Server blob data, Neo4J indexes and ElasticSearch indexes.
 
#### Creating a resource for an existing Organization

If you need to create a reference `Organization` resource for an already existing organization (that was, for example, created by the bootstrap process), you just need to retrieve the Organization ID.

This can be found by running a query against the CluedIn databases.

```sql
SELECT [Id] FROM [DataStore.Db.Authentication].[dbo].[OrganizationAccount]
```

.. you can then create a new resource using that ID ..

 ```yaml
  # File: foobar-ref.yaml
  apiVersion: "api.cluedin.com/v1"
  kind: Organization
  metadata:
    name: foobar-organization
  spec:
    name: "foobar"
    id: "d437b952-8bac-4194-ac51-8d23dd219e58"
    adminUserSecret: "foobar-admin"
  ```

.. The `Controller` will not create anything new but will allow deletion of the organization and enable reference by other CluedIn custom resources such as enabling SSO (see below).

#### Enable SSO

> **Note**: This action requires an `Organization` custom resource to exist.

CluedIn currently only support `Azure Active Directory` for SSO.

You will need two bits of information from the `Azure` portal:
1) `Client ID` (also can be displayed as `Application ID`)
2) `Client Secret`

First, we need to create a secret to hold the sensitive `clientSecret` value.

```bash
kubectl create secret generic "foobar-sso" -n cluedin --from-literal=clientSecret="1234-5678-9ABC"
```

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: foobar-sso
data:
  clientSecret: c3RvcCBsb29raW5nIGF0IG15IHNlY3JldAo=
```

Next, we need to create the custom `Feature` resource ..

```yaml
# File: foobar-sso.yaml
apiVersion: api.cluedin.com/v1
kind: Feature
metadata:
  name: foobar-enablesso
spec:
  enableSso:
    clientId: "5f9c3386-c9e3-4232-918b-ea9c303bf10e"
    organizationName: "foobar"
    clientSecretName: "foobar-sso"
    clientSecretKey: "clientSecret"
```

```bash
kubectl apply -n cluedin -f foobar-sso.yaml
```

> **Note**: This action will cause Cluedin Server / CluedIn Processing / CluedIn Crawler to restart their pods.
> The `RollingUpdate` strategy should prevent any disruption but please only execute in a known maintenance window.

`organizationName` is the name of an existing organization (it will search the `Organization` resources for one with a `spec.name` field that matches.)

`clientSecretName` is the name of the secret we created in the previous step.

This process will update two SQL tables with this information and restart the pods of 

#### Check SSO status

The `STATUS` field of a `Feature` displays its current progress. You can list the `Feature` resources in a namespace by using :

```bash
kubectl get features -n cluedin
```

If the `STATUS` is `EnableSSO Feature [...] active.` then we know SSO has been enabled.
Any error messages from the process will be stored in the `STATUS` field and the`Controller` will re-try periodically.

#### Disable SSO

You can disable SSO by deleting the custom `Feature` resource that was created previously.

It can be deleted by using the file it was created with ..

  ```bash
  kubectl delete -n cluedin -f foobar-sso.yaml
  ```

.. or by using its name (e.g. `foobar-enablesso`) directly ..

```bash
kubectl delete feature -n cluedin foobar-enablesso
```

> **Note**: This action will cause Cluedin Server / CluedIn Processing / CluedIn Crawler to restart their pods.
> The `RollingUpdate` strategy should prevent any disruption but please only execute in a known maintenance window.