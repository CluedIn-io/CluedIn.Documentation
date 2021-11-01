---
layout: default
title: Local Deployment
parent: Deployment
nav_order: 010
permalink: /deployment/docker-compose
tags: ["deployment", "docker", "docker-compose", "local-deployment"]
last_modified: 2021-11-1
---

To run CluedIn on a local computer, you don't need to set up a Kubernetes cluster. 

We provide tooling to run CluedIn in Docker containers with the help of Docker Compose. Docker Compose is a tool for running multi-container applications.

To start learning CluedIn or develop CluedIn integrations, you need only a few things:

* 16GB of free memory (we recommend 32GB).
* [Docker Desktop](https://www.docker.com/products/docker-desktop).
* [PowerShell 7](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.1) or higher.
* Access to [CluedIn DockerHub](https://hub.docker.com/orgs/cluedin) repositories (to download CluedIn container images).
* [Git](https://git-scm.com/).

It doesn't matter if you run it on Mac, Windows, or Linux.
You can start a new instance from your terminal like this:

```powershell
# Start a new PowerShell session
pwsh

# Clone the repository
git clone https://github.com/CluedIn-io/Home.git

# Move to the checkout directory
cd Home

# Log in to DockerHub
docker login

# Check default ports are available
.\cluedin.ps1 check

# Start CluedIn (pull down the images for the latest version, setup the containers, start the containers)
.\cluedin.ps1 up

# Check if CluedIn is ready (i.e. before you create an organization)
.\cluedin.ps1 status
# keep running this command over and over until you see all green ticks
# note: you can also see the same information by refreshing http://127.0.0.1.nip.io:9000/status in your browser
+------------------------+
| CluedIn - Status Check |
+------------------------+
Can Connect
  [1/1] √ » Is Up : http://127.0.0.1.nip.io:9000/status
DataShards
  [1/6] √ » Blob
  [2/6] √ » Configuration
  [3/6] √ » Data
  [4/6] √ » Search
  [5/6] √ » Graph
  [6/6] √ » Metrics
Components
  [1/6] √ » Api
  [2/6] √ » Authentication
  [3/6] √ » Crawling
  [4/6] √ » Scheduling
  [5/6] √ » ServiceBus
  [6/6] √ » System

# Create an organization
.\cluedin.ps1 createorg -name example -pass Example123!
#
# this will provide the login details you need e.g
# ...
# Email: admin@example.com
# Password: Example123!
#
# note: if you get the error "Create organization was not successful" and the status check is good then you will need to stop/start the solution
# .\cluedin.ps1 stop
# .\cluedin.ps1 start
# poll .\cluedin.ps1 status
# try createorg again

# Open the login page
.\cluedin.ps1 open -org example

# (optional) Create a new environment targeting the latest version
# if you don't create a new environment then default will be used instead and the env name can be omitted
# example commands if you are using a non-default environment
.\cluedin.ps1 env latest -Tag latest
# Check default ports are available
.\cluedin.ps1 check latest
# Start CluedIn
.\cluedin.ps1 up latest
# Create an organization
.\cluedin.ps1 createorg latest -name example -pass Example123!

# (optional) Create a new environment to track a particular release
.\cluedin.ps1 env 324 -Tag 3.2.4
# Check default ports are available
.\cluedin.ps1 check 324
# Start CluedIn
.\cluedin.ps1 up 324
# Create an organization
.\cluedin.ps1 createorg 324 -name example -pass Example123!
```

After running the above commands, you should be able to access the CluedIn UI at: <a href="http://app.127.0.0.1.nip.io:9080/" target="_blank">http://app.127.0.0.1.nip.io:9080/</a>.

For up to the minute details, please check our the Home repository <a href="https://cluedin-io.github.io/Home/" target="_blank">documentation</a>.