---
layout: default
nav_order: 1
parent: Kubernetes
grand_parent: Deployment
permalink: /deployment/kubernetes/deployment
title: Deployment
tags: ["deployment", "kubernetes"]
---


# Kubernetes
{: .no_toc }
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

---
### Introduction

CluedIn provides a *helm chart* to install CluedIn quickly in a Kubernetes cluster. [*Helm*](https://helm.sh/) is a package manager which simplifies the installation and management of complex applications in a Kubernetes environment. Charts are stored in a repository and they are invoked using the `helm-cli` tool from a terminal that has access to a Kubernetes cluster.

The purpose of the chart is to install the CluedIn application, this includes the actual CluedIn server, website, and other [services required](../../getting-started) (storage, queues, etc.)

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
- [Enabling Single Sign On](../../administration/authentication)
- [Install a crawler/custom component](../../integration/install-integrations)

Optionally, you can also adjust other settings to cater for more complex scenarios:
- [Persistence/Using Managed Disks](./persistence)
- [Azure SQL Server](./sql)
- [Scaling](./scaling)
- [Monitoring and logging](./monitoring)