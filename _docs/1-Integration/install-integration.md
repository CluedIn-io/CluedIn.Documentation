---
category: Integration
title: Install Integration
---

### Introduction

To install an integration, you will need it being packaged using Nuget.

### Official CluedIn integrations

Visit our [list of all official CluedIn integration](./someURL.html).


### Pre-requesite

- Docker

### How to run

Please close our template repository:

```
> git clone https://github.com/CluedIn-io/CluedIn.Template.Crawling.Server
```

### Add the nuget package you want to install

In the Packages.txt, add all the Nuget package you want to install.

If you have build a custom crawler, it would generally looks like:

```
CluedIn.Crawling.MyCrawler
CluedIn.Crawling.MyCrawler.Core
CluedIn.Crawling.MyCrawler.Infrastructure
CluedIn.Provider.MyCrawler
```
