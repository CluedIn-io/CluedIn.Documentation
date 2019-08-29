---
category: Integration
title: Build Integration
---

### Introduction

CluedIn official integrations are one size fits all integrations. They will generally try to ingest as much data as they can.

If you want to ingest data in a precise fashion or want to ingest data from an in-house tool, an old tool, from some custom APIs, you will need to create your own integration.

### Pre-requesite

CluedIn is a .NET platform. So you will need:

- .NET installed
- Visual Studio installed
- Docker


### Creating initial template

To avoid cumbersome boilerplating, CluedIn provides you a script to generate a working Visual studio solution.

### Install the generation tool

You will need to install node, npm, yeoman and the generator itself.

First, install Yeoman and generator-cluedin-crawler using npm (we assume you have pre-installed node.js).

```
> npm install -g yo generator-cluedin-crawler
```

### Execute the generation tool

All you need to do is mount the target folder where you would like the generator to create the files, and run the container. So for example if you want to crate the solution under `c:\projects\CluedinCrawler` you would run:

```
docker run --rm -ti -v c:/projects/CluedinCrawler:/generated cluedin/generator-crawler-template
```

If you are already in the target location you could just use the variable ${PWD}:

```
docker run --rm -ti -v ${PWD}:/generated cluedin/generator-crawler-template
```

To execute the script, simply go to the folder where you want to create the solution and invoke:

```
> yo cluedin-crawler.
```

Your visual studio solution is now created.

For more advanced installation, please refer to our generation tooling documentation.

### Adding a Model

### Pushing data

### Deploying the crawler locally

### Testing the crawler

Please refer to [install an integration](/docs/1-Integration/install-integration.html)
