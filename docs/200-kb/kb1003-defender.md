---
layout: cluedin
title: 'Microsoft Defender for Cloud recommendations'
permalink: /kb/defender-for-cloud-recommendations
parent: Knowledge base
tags: ["recommendations", "Defender", "Cloud"]
nav_order: 14
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This document covers Microsoft Defender for Cloud advisories that you may face when installing the CluedIn MDM PaaS variant of the product into your environemnt. It will explain what each advisory means and how to potentially resolve the issue.

If the advisory is not listed below, please do reach out to support@cluedin.com who will be able to advise further.

## Recommendations

### Container images should be deployed from trusted registries only

The default security policies that are set on `Microsoft Defender for Cloud` can be quite bare when it comes out of the box. As a result, this particular recommendation gets flagged frequently as a high risk. 

The CluedIn installation installs an Azure Kubernetes Service (AKS) cluster which pulls images from `cluedinprod.azurecr.io` with an authorization token. Because `cluedinprod.azurecr.io` is external to your environment, it gets flagged by this recommendation when using default baseline advisories.

**Solution**

To resolve this issue, please amend the recommendation under remediation steps and add a regex string that can accomodate the CluedIn registry.
An example is: `^cluedinprod\.azurecr\.io.*$`. 

{:.important}
This will affect all AKS clusters. If you have additional AKS clusters which are for internal services or other products, you may want to use a more loosely defined regex string that can accommodate both CluedIn and other third-party registries. 