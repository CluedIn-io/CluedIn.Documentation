---
category: Get Started
title: CluedIn with Docker
---

## Introduction

This will show you how to install CluedIn on your local machine by running it inside Docker. CluedIn is a complex application, with many moving parts, so you will need to ensure you have adequate resources on the machine you intend to run it on.

### Requirements

- At least 16Gb of free memory (It is preferable to run on a machine with 32Gb of RAM)
- Latest version of [Docker](https://docs.docker.com/get-docker/) for your operating system  (Engine: > 19.03)
- [Powershell 7](https://github.com/PowerShell/PowerShell) for your operating system - This is to run helper scripts
- Access to the private repositories inside the [cluedin](https://hub.docker.com/u/cluedin/) DockerHub organization. You will require a Docker Hub account and request access from CluedIn; then use this account to do a ```docker login```.
    NOTE: **Only CluedIn certified developers** have access to the CluedIn DockerHub.

### Running CluedIn

#### First time preparation

CluedIn provides a helper script to streamline the process of getting started.

1. Clone the helper script from the CluedIn Home repo
    ```shell
    git clone https://github.com/CluedIn-io/Home
    ```

1. Open a powershell console on Windows - ( or `pwsh` on Mac & Linux ) and run:
    ```shell
    ./cluedin.ps1 check
    ```
    This will check a few things:
    * That you have the needed software installed
    * That you have the ports needed to run CluedIn available
    * That you have logged into docker hub

    If all these checks are green you are ready to proceed. If ports are in use then you may need to stop any programs locally that may be using them and re-run `check` again.

1. Pull the latest cluedin images to your local machine
    ```shell
    ./cluedin.ps1 pull
    ```
    You can use this command to refresh/update any images at a later date.

#### Starting the application

To start up the application use: 

```shell
./cluedin.ps1 up
```
This will start up the various containers in Docker and begin initilializing CluedIn for the first time.

#### Checking application status

Depending on the speed of the machine it is being installed onto CluedIn can take a moment to start up. 

You can check the status of this by using:
```shell
./cluedin.ps1 status
```

CluedIn is ready when all the status checks are green.

Open your browser and CluedIn will be available under [http://app.127.0.0.1.xip.io](http://app.127.0.0.1.xip.io).

![First screen](first-screen-app.PNG)

#### Creating an organization

In order to use CluedIn you need to create an *organization*. There are two ways to do this

- Using a script. In a `Powershell` console run `bootstrap/Create-Organization.ps1`. This will create an organization with the following parameters:

    |          |        |   
    |----------|--------|
    | name     | foobar |
    | url      | [https://foobar.127.0.0.1.xip.io](https://foobar.127.0.0.1.xip.io) |
    | admin    | admin@foobar.com |
    | password | foobar23 |

    *These values can be overridden by passing parameters to the Powershell script*

#### Stopping the application

There are **two** ways to stop the application:

#### Stopping (without deletion of data)

To stop CluedIn but to preserve the data you created while running, use:

```shell
./cluedin.ps1 stop
```

To start CluedIn back up again, you can simply use `up` or :

```shell
./cluedin.ps1 start
```

#### Stopping (with removal/reset of data)

To completely remove CluedIn and all of the associated data use:

```shell
./cluedin.ps1 down
```

This is a destructive action but it is useful for resetting data in CluedIn.

### Adding extra components

You can add extra providers or enrichers in two different ways:

1. Via Nuget packages
    1. Add a a file named `Packages.txt` in the `./components` folder with the names of the nuget packages for the components you want to install.
    1. If the Nuget packages are not available publicly add a `nuget.config` file in the `./components` folder. Either pass the password token to the `nuget.config` or create a `KEY` environment variable with it.
1. Copy the relevant DLLs for the components in the `./components` folder.
