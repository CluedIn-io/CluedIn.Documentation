---
category: Get Started
title: CluedIn with Docker
---

## Introduction

As CluedIn is a complex platform, CluedIn is providing you a template on how to run CluedIn using docker locally on your machine.

### Requirements

- Windows version **1903** or greater
- Latest version of [Docker for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows) (> 19.03.4)
- Docker [experimental features](https://docs.docker.com/docker-for-windows/#daemon) turned on 
- Docker set up to run [Windows containers](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers)
- Access to the private repositories inside the [cluedin](https://hub.docker.com/u/cluedin/) DockerHub organization. You will require a Docker Hub account and request access from CluedIn; then use this account to do a ```docker login```.
    NOTE: **Only CluedIn certified developers** have access to the CluedIn DockerHub.

You can verify if you satisfy these requirements and you can run simultaneously Windows and Linux containers by opening a `Powershell` console and running:
```powershell
docker info | sls 'Storage Driver'
```

The returned value should be:
```
 Storage Driver: windowsfilter (windows) lcow (linux)
```

### Running CluedIn

#### First time preparation

1. Clone the Simple-Docker-Deployment
    ```shell
    git clone https://github.com/CluedIn-io/Simple-Docker-Deployment
    ```

1. Pull latest images
    ```shell
    docker-compose pull
    ```

1. Open an **administrator `Powershell`** console, run ```./pki/Create-Certificates.ps1 -Trust```.


#### Starting the application

The application is run doing a via docker-compose You can then bring the application up doing:

```shell
docker-compose up -d
```

You can check if the the different services are created running:
```shell
docker-compose ps
```

The CluedIn server component takes a while to boot up. You can verify it is starting correctly:
```shell
docker-compose logs -f server
```

The server will be ready when you see the message `Server Started`. Open your browser and CluedIn should be available under [https://app.127.0.0.1.xip.io](https://app.127.0.0.1.xip.io).

![First screen](first-screen-app.PNG)


In order to use CluedIn you need to create an *organization*. There are two ways to do this

- Using a script. In a `Powershell` console run `bootstrap/Create-Organization.ps1`. This will create an organization with the following parameters:

    |          |        |   
    |----------|--------|
    | name     | foobar |
    | url      | [https://foobar.127.0.0.1.xip.io](https://foobar.127.0.0.1.xip.io) |
    | admin    | admin@foobar.com |
    | password | foobar23 |

    *These values can be overridden by passing parameters to the Powershell script*

- Using the UI
    1. Navigate to the [https://app.127.0.0.1.xip.io/signup](https://app.127.0.0.1.xip.io/signup) page.
    1. Fill in an email address (it can be fictitious)
    1. Check the `/emails` folder. You should be able to open the file with the standard Mail application from Windows by double clicking on it.
    1. Click on the *Setup my organization link* in the email
    1. Fill in the information and click in *Sign up*
    1. You will be redirected to the login screen. Simply add the information created in the step above.

#### Stopping the application

You can then stop and start the stack, using the usual docker-compose commands

```shell
docker-compose down # containers are removed, data is kept 
docker-compose down -v # containers are removed and data is lost
```

If you need to remove the certificates you can run

```powershell
./pki/Remove-Certificates.ps1
```

### Adding extra components

You can add extra providers or enrichers in two different ways:

1. Via Nuget packages
    1. Add a a file named `Packages.txt` in the `./components` folder with the names of the nuget packages for the components you want to install.
    1. If the Nuget packages are not available publicly add a `nuget.config` file in the `./components` folder. Either pass the password token to the `nuget.config` or create a `KEY` environment variable with it.
1. Copy the relevant DLLs for the components in the `./components` folder.
