---
layout: default
title: Installation
nav_order: 20
has_children: true
permalink: /deployment
---

{: .fs-6 .fw-300 }

CluedIn is designed with the [Microservices Architecture](https://microservices.io/index.html) in mind. That means that CluedIn, as an application, is a set of interconnected services: a web application, GraphQL API, databases, message queue, and so on.

Each CluedIn service runs in a separate [container](https://www.docker.com/get-started), allowing us to test, scale, and monitor each service effectively.

While CluedIn is a [cloud-native](https://docs.microsoft.com/en-us/dotnet/architecture/cloud-native/definition) application, you can also run it on your local machine.

[Docker Compose](https://docs.docker.com/compose/) is the technology that allows us to run a group of containers on our local computer easily. You just run a few commands, and a new CluedIn instance is up and running on your laptop or desktop computer. You can use it for testing and development. Please, follow the [Local Deployment](./docker-compose) section for more details.

When it comes to production, [Kubernetes](https://kubernetes.io/) runs CluedIn services in the cloud and ensures that the containers are healthy and scale as they should.

While all modern cloud providers support Kubernetes, we recommend running CluedIn on Microsoft Azure with the help of [Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/). Read more about it in the [Azure](./azure) section of our documentation. 
