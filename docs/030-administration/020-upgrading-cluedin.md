---
layout: default
nav_order: 2
parent: Administration
permalink: /administration/upgrading-cluedin
title: Upgrading CluedIn
tags: ["administration", "upgrade"]
---

To upgrade CluedIn, you will need to take many things into consideration. 

CluedIn deploys new versions of its software, crawlers and other products to the CluedIn Private Docker Repository. We deploy Stable, Beta and Alpha versions so that our customers can try out different parts of the platform at their discretion.

It is always recommended to first check the release notes of the version you are upgrading to. You might find that if you are jumping a large number of versions, that the upgrade path is harder than smaller increments. If you have adhered to the best practices of CluedIn, then upgrading should be very straight forward. In essence, we offer ways for Developers to inject changes to CluedIn but very much do not recommend changing default CluedIn behaviour. If you have adhered to this then it will make your upgrade paths easier. 

It is also a recommended practice that you also don't directly connect to the CluedIn data stores, but rather use our APIs to interact with the underlying data stores. If you have stuck to this principal, then changes to the underlying data stores can be automated during the upgrade process. 

You may find that certain updates will require you to reprocess the data within your account. The release notes will detail if you will need to run this process or other processes to make data updates if necessary. 

If you have chosen the Docker path of deploying CluedIn then you will need to use your Docker-Compose.yml file to change to the version you would like to upgrade to. We do not suggest changing the dependency versions of other CluedIn dependencies unless it has been specifically sanctioned and supported by CluedIn. For example, changing the version of one of the data stores could result in issues and will not be covered in the support models we provide. Each version of CluedIn will specifically detail which versions of dependencies that it supports.

If you are using Kubernetes to deploy CluedIn, you have built-in support for rolling back a deployment if it fails. This means that you can upgrade or attempt to upgrade your CluedIn instance with full confidence that if it fails, you should not break anything.

# Downgrading CluedIn

Although downgrading is not typically something that is done, there may be times where you need to rollback a deployment. 

If you have installed [CluedIn in Kubernetes](../deployment/kubernetes) you can easily downgrade/rollback. If you have used the _Helm chart_ you can then use the native Helm commands to rollback. Alternatively, if you have just used the Helm chart to create the definition files, those will be committed in a repository with source control, so you can just checkout a different branch or commit and apply the changes to Kubernetes.
