---
category: Enricher
title: Install Enricher
---

### Introduction

To install an Enricher, you will need it being packaged using Nuget.

### Official CluedIn Enrichers

Visit our [list of all official CluedIn Enrichers](https://cluedin-marketplace.herokuapp.com/search?type=enricher).


### Pre-requesite

- Docker

### How to run

Please clone our template repository:

```shell
> git clone https://github.com/CluedIn-io/CluedIn.Template.Crawling.Server
```

### Add the nuget package you want to install

In the Packages.txt, add all the Nuget packages you want to install.

If you have build a custom Enricher, it would generally looks like:

```
CluedIn.ExternalSearch.Providers.HelloWorld
```

### Run CluedIn

```shell
> docker run xxxxx
```

### CluedIn is running with your Enricher

The app should be available under http://app.cluedin.test.