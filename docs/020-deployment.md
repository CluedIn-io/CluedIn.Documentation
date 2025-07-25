---
layout: cluedin
title: Installation
nav_order: 20
has_children: true
permalink: deployment
---

<div class="card-line">
  <div class="card" href="/deployment/saas">
    <div class="icon"><img src='{{ "/assets/icons/Saas-purple-icon.svg"" | relative_url }}' alt="CluedIn SaaS"/></div>
    <div class="title">CluedIn SaaS</div>
    <div class="content">Get access to cloud-hosted platform, the easiest way to start with CluedIn</div>
  </div>
   <div class="card" href="/deployment/azure-marketplace">
    <div class="icon"><img src='{{ "/assets/icons/PaaS-blue-icon.svg"" | relative_url }}' alt="Azure Market place"/></div>
    <div class="title">CluedIn PaaS</div>
    <div class="content">Install CluedIn within your company’s Azure infrastructure</div>
  </div> 
  <div class="card" href="deployment/local">
    <div class="icon"><img src='{{ "/assets/icons/Local-icon-orange.svg"" | relative_url }}' alt="Installation"/></div>
    <div class="title">Local</div>
    <div class="content">Install CluedIn locally to test its main features and write custom code</div>
  </div>
</div>

CluedIn is designed with the [Microservices Architecture](https://microservices.io/index.html) in mind. That means that CluedIn, as an application, is a set of interconnected services: a web application, GraphQL API, databases, message queues, and so on. Each CluedIn service runs in a separate [container](https://www.docker.com/get-started), allowing us to test, scale, and monitor each service effectively.

While CluedIn is a [cloud-native](https://docs.microsoft.com/en-us/dotnet/architecture/cloud-native/definition) application, you can also run it on your local machine. [Docker Compose](https://docs.docker.com/compose/) is the technology that allows us to run a group of containers on our local computer easily. You just run a few commands, and a new CluedIn instance is up and running on your laptop or desktop computer. You can use it for testing and development. Please, follow the [Local installation guide](/deployment/local/step-2) for more details.

When it comes to production, [Kubernetes](https://kubernetes.io/) runs CluedIn services in the cloud and ensures that the containers are healthy and scale as they should. While all modern cloud providers support Kubernetes, we recommend running CluedIn on Microsoft Azure with the help of [Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/). Read more about it in the [PaaS installation](/deployment/azure-marketplace) section of our documentation.

The following video explores the features and differences between the SaaS, PaaS, and local options for deploying CluedIn.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/928300363?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture;" title="CluedIn installation options"></iframe>
</div>

**Azure Managed Application**

CluedIn is available as an Azure Managed Application, making deployment and operation effortless for you. Depending on the model you choose—PaaS or SaaS—CluedIn can be deployed within your company’s infrastructure or within our infrastructure. Regardless of the chosen model, this setup allows us to handle almost everything for you, including post-installation, upgrades, backups, and monitoring. This ensures that you do not need to worry about operating and managing a cluster yourself, as long as the CluedIn operations team has full access to your cluster.

![paas-saas-diagram.png]({{ "/assets/images/deployment/paas-saas-diagram.png" | relative_url }})

**SaaS vs. PaaS**

The following diagram illustrates the difference between SaaS and PaaS in terms of who is responsible for managing what.

![saas-paas.png]({{ "/assets/images/deployment/saas-paas.png" | relative_url }})
