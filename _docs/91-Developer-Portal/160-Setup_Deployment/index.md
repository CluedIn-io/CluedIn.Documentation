# Setup and Deployment

## Getting Started

The quickest way to get started with CluedIn would be to use our `Simple-Docker-Deployment` Docker scripts.

### What is Docker?

[Docker](https://www.docker.com/) is a tool designed to make it easier to create, deploy, and run applications by using containers and CluedIn is all about containers

The reason CluedIn embraces containers are the following:

- Faster Application Deployment and Portability
- Developer Productivity
- Agility to Scale to Demand
- Efficient Compute Resources Usage
- Better Security and Governance, External to the Containers


### Requirements

CluedIn has some a basic set of requirements.

We are consistently trying to keep the requirements as small as possible in order to get you up and running switfly.

Requirement List:

- Windows

  Currently CluedIn still needs windows to run the Simple-Docker-Deployment.

  NOTE: The product team is actively working on having CluedIn working in both environments seamlessly (Linux and Windows containers).

- A github account

  CluedIn uses github to share public code with the community. If you want to have access to the code, you will need a github account.

- GIT installed locally

  When working with CluedIn, you will need from time to time to pull some of our public repositories, if you are not familiar with GIT, you can use the [github desktop application](https://desktop.github.com/) to ease the process.

- Latest Docker installed

  [Download and install Docker](https://store.docker.com/editions/community/docker-ce-desktop-windows)


- Access to private CluedIn Docker organization.

  If you are a certified CluedIn developers, you should have read access to the CluedIn Docker hub. If it is not the case, please contact your account manager.

  To verify if you have access, [visit our docker organization](https://hub.docker.com/u/cluedin/) and check if you have access to [cluedin-server](https://hub.docker.com/r/cluedin/cluedin-server/) image. If you see a 404, you do not have access, if you see the image, all good.

### Install CluedIn

1. Clone the Simpler Docker Deployment

> git clone https://github.com/CluedIn-io/Simple-Docker-Deployment.git

2. Open a Windows PowerShell script as administrator

3. Execute create in the root folder of the freshly cloned repository

> ./create.ps1

4. Visit http://app.cluedin.test


### Remove CluedIn

1. Open a Windows PowerShell script as administrator

2. Execute remove in the root folder of the freshly cloned repository

> ./remove.ps1

### Any troubles?

Visit the [public repository](https://github.com/CluedIn-io/Simple-Docker-Deployment) for more information.

### Next

[Deploying CluedIn in your own environment](./hosted.md).