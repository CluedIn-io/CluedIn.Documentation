---
layout: default
title: Local Deployment
parent: Deployment
nav_order: 010
permalink: /deployment/docker-compose
tags: ["deployment", "docker", "docker-compose", "local-deployment"]
last_modified: 2021-10-19
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
# Create a new environment targeting the latest version
.\cluedin.ps1 env latest -Tag latest
# Check default ports are available
.\cluedin.ps1 check latest
# Start CluedIn
.\cluedin.ps1 up latest
# Create an organization
.\cluedin.ps1 createorg latest -Name example -Pass Example123!

# this will provide the login details you need e.g
# ...
# Email: admin@example.com
# Password: Example123!

# Open the login page
.\cluedin.ps1 open latest -Org example
```

After running the above commands, you should be able to access the CluedIn UI at: <a href="http://app.127.0.0.1.nip.io:9080/" target="_blank">http://app.127.0.0.1.nip.io:9080/</a>.

For more details, please check our the Home repository <a href="https://cluedin-io.github.io/Home/" target="_blank">documentation</a>.