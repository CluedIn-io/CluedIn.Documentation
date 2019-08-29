---
category: Get Started
title: CluedIn with Docker
---

### Introduction

As CluedIn is a complex platform, CluedIn is providing you a template on how to run CluedIn using docker locally on your machine.

#### Requirements

- Docker for Windows
- Access to the private repositories inside the CluedIn DockerHub organization. You will require a Docker Hub account and request access from CluedIn; then use this account to do a docker login.

NOTE: **Only CluedIn certified developers** has access to the CluedIn DockerHub.

#### 1. Clone the Simple-Docker-Deployment

```
git clone https://github.com/CluedIn-io/Simple-Docker-Deployment
```

#### 2. Pull latest image

```
> docker pull cluedin/cluedin-server
```

```
> docker pull cluedin/app
```


#### 3. Start CluedIn

As administrator, run create.ps1.

#### 4. CluedIn is now running.

The app should be available under http://app.cluedin.test.

Data is persisted.

![First screen](first-screen-app.PNG)

#### 5. Stopping

You can then stop and start the stack, using the `start.ps1` and `stop.ps1` scripts.

#### 6. Removing

You can remove all traces of CluedIn, including all the data, invoking the `remove.ps1` script.
