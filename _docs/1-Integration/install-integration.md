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

In the Packages.txt, add all the Nuget packages you want to install.

If you have build a custom crawler, it would generally looks like:

```
CluedIn.Crawling.MyCrawler
CluedIn.Crawling.MyCrawler.Core
CluedIn.Crawling.MyCrawler.Infrastructure
CluedIn.Provider.MyCrawler
```

### Run CluedIn

```
> docker run xxxxx
```

### CluedIn is running with your Crawler

The app should be available under http://app.cluedin.test.

### Create an organization

TODO

```
> ./createOrganization.ps1
```

### Login to the org

Go to http://acme.cluedin.test

username: admin@acme.com
pass: acme23

### Look at the integration page


URL: https://foobar.release23.cluedin-test.online/admin/integration/applications


More information: [How to add an Integration using the CluedIn UI](./somelink)

### Next steps

[How to add an integration](./somelink)