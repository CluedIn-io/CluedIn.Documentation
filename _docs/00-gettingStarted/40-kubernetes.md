---
category: Get Started
title: CluedIn with Kubernetes
---

### Introduction

CluedIn provides a *helm chart* to install CluedIn quickly in a Kubernetes cluster. [*Helm*](https://helm.sh/) is a package manager which simplifies the installation and management of complex applications in a Kubernetes environment. Charts are stored in a repository and they are invoked using the `helm-cli` tool from a terminal that has access to a Kubernetes cluster.

The purpose of the chart is to install the CluedIn application, this includes the actual CluedIn server, website, and other [services required](/docs/00-gettingStarted/1-default.html) (storage, queues, etc.)

### Pre-requisites
- Local install of [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl) configured to talk to the cluster
   - Cluster's kubeconfig can be fetched using the following commands:
```powershell
az login
az aks get-credentials `
  --name <clusterName> `
  --resource-group <clusterResourceGroup> `
  --subscription <subscriptionId>
```
- Local install of the cli for [Helm](https://helm.sh/)



### Kubernetes Cluster
*A Kubernetes cluster and kubeconfig access to it is required*.

Recommended nodepool sizing for an AKS cluster can be found below:

| Node Pool         | VM SKU Type         | Amount        | Purpose  | 
|-------------------|:-------------       |:-------------:| :----    |
| Core Pool         | `Standard_DS2_v2`   | 1             | Kubernetes agent internal processes |
| Data Pool         | `Standard_A8_v2`    | 2             | Memory Optimized pool for Databases |
| Processing Pool   | `Standard_F16s_v2`  | 1             | CPU Optimized for Processing workloads |
| General Pool      | `Standard_F4s_v2`   | 2             | General Purpose nodepool to house CluedIn Microservices |

_Additionally, Memory Optimized and CPU Optimized pools can be tainted to only allow Database or Processing workloads._

The same size boxes with the amount of RAM and CPU can also be used for deploying into other cloud providers such as Amazon Web Services of Google Cloud.

### Networking / SSL / DNS
In addition this cluster should have:
- HAProxy ingress controller installed (it is possible to use a different ingress controller (like NGINX) with extra customization).

You can use the following commands to install HAProxy using Helm:
```powershell
kubectl create namespace cluedin
helm repo add haproxy-ingress https://haproxy-ingress.github.io/charts
helm install haproxy-ingress haproxy-ingress/haproxy-ingress --namespace=cluedin
```
- DNS configuration pointing to the public IP of the ingress controller for the following routes:
  - `app.<hostname>` (i.e. https://app.cluedin.com/)
  - `<accountName>.<hostname>` (i.e. https://cluedin.cluedin.com/)
    - _External ingress controller's IP can be found by using `kubectl get services -n cluedin`_


- Secret with the SSL certificates for the following routes:
  - `app.<hostname>` (i.e. https://app.cluedin.com/)
  - `<accountName>.<hostname>` (i.e. https://cluedin.cluedin.com/)
    - _Secret can be created using the following command: `kubectl create secret tls <secret-name>--key <private-key-path> --cert <public-certificate-path>`_

__*There is an option to run without SSL, although not recommended*__
Set the following flag in values.yml to disable HTTPS connection:
```yaml
tls:
    forceHttps: false
```

### Installing CluedIn Platform
CluedIn Platform can be installed as a whole with the help of Helm.

### Preparation

* The helm chart repository containing the CluedIn chart must be registered. 
```powershell
helm repo add cluedin https://cluedin-io.github.io/Charts/
helm repo update
```

* Secret with the credentials for accessing the CluedIn images from Docker Hub.
_Secret can be created using the following command:_
```powershell
kubectl create secret docker-registry docker-registry-key `
  --namespace cluedin `
  --docker-server='docker.io' `
  --docker-username='<your Dockerhub username>' `
  --docker-password='<your Dockerhub password>' `
  --docker-email='<your Dockerhub email>'
```

* Fetch values.yml configuration file to configure CluedIn Installation
```powershell
helm inspect values cluedin/cluedin > values.yml
```
### Installation

Fill out the values.yaml file, specifically the following objects:
```yaml
bootstrap: 
  organization: 
    name: # Organization Account Name
    email: # Admin account's Email
    username: # Admin account's username (should be the same as above) 
    prefix: # Organization prefix used to access the platform (also use in DNS configuration step above)
    password: # Admin account's password
    emailDomain: # Admin account's Email domain
```

*Be aware that you cannot use an organization prefix with a hyphen or period in it.

```yaml
tls: 
  ingressCertSecret: # Name of the secret created in SSL certificate step
```

This creates a values.yml which you can modify to tailor how CluedIn will be installed.

Once values.yml file has been populated and settings are adjusted to your liking, you can install CluedIn Platform with the following Helm command:
```powershell
helm upgrade <release-name (i.e. cluedin-dev, cluedin-prod)> cluedin/cluedin `
  -n cluedin `
  --install `
  --values <path-to-values.yml>
```

Upon running the `helm upgrade` command, Helm will begin installation of CluedIn platform into your Kubernetes cluster. At the end of the installation process, you will be prompted with configuration of your install, URLs you can use to access your freshly installed platform. 

All the workloads may take up to 10 minutes to spin up. You can check your status by running `kubectl get pods -n cluedin`, in a healthy installation scenario all the pods should be in a `Ready` state.

Additionally, you can check the health of the platform by going to `https://app.<hostname>/api/status` healthcheck API.

You will be able to login to the platform by going to `https://app.<hostname>/` (or `http://app.<hostname>/` if not using SSL). 

#### Next Steps

After logging in to the platform, you can proceed with enabling single sign on for your users to access the platform, as well as start loading data in via Data Sources or installing some crawlers. 
Below you will find some useful links on achieving the above:
- [Enabling Single Sign On](/docs/05-Administration/30-Authentication/index.html)
- [Install a crawler/custom component](/docs/10-Integration/install-integration.html)

Optionally, you can also adjust other settings to cater for more complex scenarios:
- [Persistence/Using Managed Disks](/docs/00-gettingStarted/persistence.html)
- [Azure SQL Server](/docs/00-gettingStarted/sqlserver.html)
- [Scaling](/docs/00-gettingStarted/scaling.html)
- [Monitoring and logging](/docs/00-gettingStarted/monitoring.html)

### CluedIn Custom Resources for Kubernetes

> !!! **Only available in CluedIn v3.2.4 onwards** !!!

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
  .. you can apply the resurce to the Kubernetes cluster to begin the creation process using :
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

  You can remove entirely remove an organization by deleteing the custom `Organization` resource that was created previously.
  
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
