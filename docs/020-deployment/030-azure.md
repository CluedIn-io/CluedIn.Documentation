---
layout: default
title: Azure
parent: Deployment
permalink: /deployment/azure
nav_order: 30
has_children: true
tags: ["deployment", "kubernetes", "azure", "aks", "microsoft"]
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Microsoft Azure is the recommended platform for running CluedIn production instances.

In this article, we briefly observe what you would need to run CluedIn in Azure. Follow the child articles for more specific topics or check the [Deployment](../deployment) article that gives an overview of possible install options.

So, this is what you need to run CluedIn on Azure:

### AKS

To install CluedIn in any cloud, you need a Kubernetes cluster. In Azure, this cluster is provided by Azure Kubernetes Services (AKS).

Therefore, before installing CluedIn, you need to have a working AKS instance with an external IP address.

### DNS

Next, you may not want to access CluedIn just by IP address, so you will need to choose the domain name that will be a part of the URL when you reach CluedIn.
For example, say your company domain is `foobar.dev`. Then you will need DNS [A-records](https://en.wikipedia.org/wiki/List_of_DNS_record_types) that point the following addresses to your cluster IP:

- `app.foobar.dev`
- `foo.foobar.dev`
- `clean.foobar.dev`

The easiest way is to create a wildcard DNS A-record. If the external cluster IP is `185.199.108.153` (just an example), the A-record will look like: `A *.foobar.dev 185.199.108.153`.
Or even `A *.cluedin.foobar.dev 185.199.108.153`, so CluedIn services will be available by:

- `app.cluedin.foobar.dev`
- `foo.cluedin.foobar.dev`
- `clean.cluedin.foobar.dev`

*NOTE: mind the `foo.*` address - this is the name of your organization account in CluedIn, and of course, you can choose a different name for it. We will discuss this later.*

Or, you can create an A-record per each address:

- `A app.cluedin.foobar.dev 185.199.108.153`
- `A foo.cluedin.foobar.dev 185.199.108.153`
- `A clean.cluedin.foobar.dev 185.199.108.153`

It's entirely up to you whether to use a wildcard A-record or an A-record per address.

### SSL/TLS certificates

When you have an AKS cluster with an external IP address that you can reach, and when you know the domain associated with this address, you may need an SSL/TLS certificate to use the HTTPS protocol when reaching the CluedIn service. You can generate one for free via [Let's Encrypt](https://letsencrypt.org/) or a similar service.

When you have all this, you can go to the next step and fulfill CluedIn prerequisites.

### Persistent storage

If this is not a test instance, you need to preserve your data even if you decide to recreate your AKS cluster. So you will need to create a set of Azure Managed Disks for the storage services in CluedIn.

### Email

Optionally, you may want to get email notifications from your CluedIn instance. In that case, you will need an email address from which these notifications will be sent and a login and password to the email account.

### NuGet Personal Access Token (PAT)

You will need the CluedIn PAT to access the CluedIn NuGet feed. Don't hesitate to contact CluedIn support, and they will provide you with that token.

### Installing CluedIn

CluedIn provides a Helm chart that allows you to deploy a CluedIn application to your AKS easily. What you will need is to provide a few details about your infrastructure and CluedIn instance. See more information here.

You can access the step by step installation process [here](../azure/setup).