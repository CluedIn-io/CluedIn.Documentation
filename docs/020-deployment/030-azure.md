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

### Kubernetes / CluedIn Helm Chart Supported Versions

**As of April 2022:**

(EOL = End of Life)

| **K8s version** | **K8S release** | **AKS preview** | **AKS GA**  | **AKS EOL** | **K8S EOL** | **CluedIn 3.2.5** | **CluedIn 3.3.0**
|------|-----------|----------|----------|---------|--|------------------------------|------------------------------|
| 1.18 | Mar-25-20 | EOL      | EOL      | EOL     | Apr-30-21 | `cluedin` / `3.2.5-update.4` | `N/A`                        |
| 1.19 | Aug-26-20 | EOL      | EOL      | EOL     | Oct-28-21 | `cluedin` / `3.2.5-update.4` | `N/A`                        |
| 1.20 | Dec-08-20 | Jan 2021 | Mar 2021 | 1.23 GA | Feb-28-22 | `cluedin` / `3.2.5-update.4` | `cluedin-platform` / `1.0.2` |
| 1.21 | Apr-08-21 | May 2021 | Jul 2021 | 1.24 GA | Jun-28-22 | `cluedin` / `3.2.5-update.4` | `cluedin-platform` / `1.0.2` |
| 1.22 | Aug-04-21 | Sep 2021 | Dec 2021 | 1.25 GA | Nov-28-22 | `cluedin` / `3.2.5-update.4` | `cluedin-platform` / `1.0.2` |
| 1.23 | Dec 2021  | Jan 2022 | Apr 2022 | 1.26 GA | Feb-28-23 | `cluedin` / `3.2.5-update.4` | `cluedin-platform` / `1.0.2` |

**Notes**
*  We broadly follow the Microsoft AKS release calendar: https://docs.microsoft.com/en-us/azure/aks/supported-kubernetes-versions?tabs=azure-cli#aks-kubernetes-release-calendar
* Kubernetes version history: https://en.wikipedia.org/wiki/Kubernetes#Release_timeline
* CluedIn does not currently use any version-specific features of Kubernetes


**Deprecation warnings**

When installing the chart you may see warnings such as:
```
W0419 14:10:41.891611   47978 warnings.go:70] policy/v1beta1 PodSecurityPolicy is deprecated in v1.21+, unavailable in v1.25+
W0419 14:10:41.897405   47978 warnings.go:70] policy/v1beta1 PodSecurityPolicy is deprecated in v1.21+, unavailable in v1.25+
W0419 14:10:41.905217   47978 warnings.go:70] policy/v1beta1 PodSecurityPolicy is deprecated in v1.21+, unavailable in v1.25+
W0419 14:10:41.913406   47978 warnings.go:70] policy/v1beta1 PodSecurityPolicy is deprecated in v1.21+, unavailable in v1.25+
W0419 14:10:41.918653   47978 warnings.go:70] policy/v1beta1 PodSecurityPolicy is deprecated in v1.21+, unavailable in v1.25+
W0419 14:10:41.923475   47978 warnings.go:70] policy/v1beta1 PodSecurityPolicy is deprecated in v1.21+, unavailable in v1.25+
W0419 14:10:41.929713   47978 warnings.go:70] policy/v1beta1 PodSecurityPolicy is deprecated in v1.21+, unavailable in v1.25+
```

These are nothing to worry about until moving to version v1.25 (which at time of writing has not yet been released). Kubernetes working group has not released the replacement for this resource yet (we just know its going away) - Information available here : https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/. CluedIn will provide an update for this resource type in time for 1.25 migrations.

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

You can access the step by step installation process [here](/deployment/azure/setup).