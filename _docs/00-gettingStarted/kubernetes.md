---
category: Get Started
title: CluedIn with Kubernetes
---

### Introduction

CluedIn provides a *helm chart* to install CluedIn quickly in a Kubernetes cluster. [*Helm*](https://helm.sh/) is a package manager which simplifies the installation and management of complex applications in a Kubernetes environment. Charts are stored in a repository and they are invoked using the `helm-cli` tool from a terminal that has access to a Kubernetes cluster.

The purpose of the chart is to install the CluedIn application, this includes the actual CluedIn server, website, and other [services required](/docs/00-gettingStarted/0-default.html) (storage, queues, etc.)

#### Pre-requisites

Access to a Kubernetes cluster with both Linux **and Windows** nodes. In addition this cluster should have:
- nginx ingress controller installed (it is possible to use a different ingress controller with extra customization).
- DNS configuration pointing to the public IP of the ingress controller
- a secret with the credentials for accessing the CluedIn images from Docker Hub.
- a secret with the SSL certificates for the CluedIn API.
- Helm's *tiller* installed in the cluster if you want to use Helm to install the chart directly. See the [deployment options](#deployment-options).
- Local install of [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl) configured to talk to the cluster
- Local install of the cli for [helm](https://helm.sh/)


The helm chart repository containing the CluedIn chart must be registered. 

You can see a step-by-step guide in the [example pre-requisite configuration](/docs/00-gettingStarted/kubernetes-sample-prerequisites.html)



### Installation

You can retrieve all the configuration options for this helm chart using 

```powershell
helm inspect values cluedin/cluedin > values.yml
```

This creates a values.yml which you can modify to tailor how CluedIn will be installed.

#### Configuration

As a minimum, there are some settings you will need to adjust in the `values.yml` file.

- [DNS / hostnames](/docs/00-gettingStarted/dns-hostnames.html)
- [SSL configuration](/docs/00-gettingStarted/ssl.html)
- [Email](/docs/00-gettingStarted/email.html)
- [Securing access with OAuth2](/docs/00-gettingStarted/oauth2.html)
- Resources: All deployments in the chart are configured with sensible, but fairly minimal resource requests. You can override those within the `values.yaml` file.
- [Extra components to install in the server](/docs/10-Integration/install-integration.html)

Optionally, you can also adjust other settings to cater for more complex scenarios:
- [Persistence](/docs/00-gettingStarted/persistence.html)
- [SQL Server](/docs/00-gettingStarted/sqlserver.html)
- [Scaling](/docs/00-gettingStarted/scaling.html)

#### Deployment options

Once you have set all the required values for your installation in the `values.yaml` file, there are two approaches to install the application in your cluster.

1. You could use [`helm`](https://helm.sh/docs/helm/#helm-upgrade) directly:

    ```bash
    helm upgrade --install <name-of-your-release> -f <path-to-values.yaml> cluedin/cluedin
    ```

    This also works to make any changes to the release if you have modified the values file again. It has the advantage that you keep a history of all the releases you make, and you can easily rollback to any one of them.

    *Beware that, if you are letting the helm chart autogenerate passwords (for the sqlserver and bootstrapping cluedin server), those secrets will be left behind even if you delete the release doing `helm delete --purge <release-name>`. You can delete them manually doing `kubectl delete secret -l release=<release-name>`.*

1. You could use `helm` purely as a templating engine. Helm would then not install anything in the cluster but purely create the set of YAML files that define all the resources needed in the application. You could then further tweak those files, and use them to create the resources in the cluster by running:
    ```shell
        kubectl apply -f .`
    ```

    This has the advantage that you get total flexibility to modify/tweak everything. I would recommend you commit the files to source control to keep record of any changes, giving you not only history but they ability to roll back to any previous state.

    In order to help create those files you could use the following a powershell function like [`Split.ps1`](https://bit.ly/2m3a1Bj).

    ```powershell
    # get the helm chart content - this will create a cluedin folder
    helm fetch cluedin/cluedin --untar
    # execute the template picking the values in your overriden values file
    helm template -n <name-of-relese> -f <path-to-values-file.yml> | Split.ps1 -Discard 'cluedin/templates/'
    ```

    _You could also use the `--output-dir` option of the `helm template` command - though that creates the  files in separate folders and makes it harder to then execute `kubectl apply`._

    Now that you have generated the manifests for all the resources, you can apply them in bulk running `kubectl apply -f .`

#### Monitoring

Check the [monitoring and logging](/docs/00-gettingStarted/monitoring.html) section to learn how to verify if the application is running successfully. You are able to check the logs, and connect to the interfaces of the different tools CluedIn is using.

### Other things to note

#### RabbitMQ High Memory Watermark
RabbitMQ has a _safety_ feature where it will stop taking new messages if the [memory consumption](https://www.rabbitmq.com/memory.html) goes over 40% of the total available memory in the machine. When running in bare metal, this makes sense, but when running  in a pod, dedicated to just RabbitMQ, this setting is too low. By default the chart sets it to 80%. This can be adjusted:

```yaml
rabbitmq:
    environment:
        RABBITMQ_VM_MEMORY_HIGH_WATERMARK: 80%
```

