---
category: Get Started
title: CluedIn with Docker
---

## Introduction

This will show you how to install CluedIn on your local machine by running it inside Docker. CluedIn is an application with many services, so you will need to ensure you have adequate resources on the machine you intend to run it on.

### Requirements

- At least 16Gb of free memory dedicated to docker (It is preferable to run on a machine with 32Gb of RAM)
- Latest version of [Docker](https://docs.docker.com/get-docker/) for your operating system  (Engine: > 19.03)
- [Powershell 7](https://github.com/PowerShell/PowerShell) for your operating system - This is to run helper scripts
- Access to the private repositories inside the [cluedin](https://hub.docker.com/u/cluedin/) DockerHub organization. You will require a Docker Hub account and request access from CluedIn; then use this account to do a ```docker login```.
    NOTE: **Only CluedIn certified developers** have access to the CluedIn DockerHub. Please contact us on our [website](https://www.cluedin.com/) if you would like access.

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
This will start up the various containers in Docker and begin initializing CluedIn for the first time.

#### Checking application status

Depending on the speed of the machine it is being installed onto CluedIn can take a moment to start up.

You can check the status of this by using:
```shell
./cluedin.ps1 status
```

CluedIn is ready when all the status checks are green.

Open your browser and CluedIn will be available under [http://app.127.0.0.1.nip.io:9080](http://app.127.0.0.1.nip.io:9080).

![First screen](first-screen-app.png)

#### Creating an organization

In order to use CluedIn you need to create an *organization*.
You can use the following command to create an account from the command line

```shell
./cluedin.ps1 createorg -name foobar -pass Foobar23!
```

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

### Adding extra components (such as crawlers, providers, enrichers, connectors)

#### Add CluedIn NuGet feed

In order to satisify the dependances of any additional components to add to CluedIn will require adding the Public CluedIn NuGet feed:

```shell
./cluedin.ps1 packages -addfeed cluedin -uri  https://pkgs.dev.azure.com/CluedIn-io/Public/_packaging/Public/nuget/v3/index.json
```

This results in the following folder tree being created:

```shell
env/default
env/default/.env
env/default/packages
env/default/packages/nuget.config
env/default/packages/local
env/default/packages/packages.txt
```
NOTE: you can inspect `nuget.config` and `packages.txt` for troubleshooting purposes.

#### Adding SqlServer Connector example

1. Download respective .nupkg files from [https://github.com/CluedIn-io/CluedIn.Connector.SqlServer/releases/](https://github.com/CluedIn-io/CluedIn.Connector.SqlServer/releases/) and save/copy into `env/default/packages/local`

1. Add the package:

    ```shell
    ./cluedin.ps1 packages -add CluedIn.Connector.SqlServer
    ```

1. Restore the package to ensure all dependencies are present:

    ```shell
    ./cluedin.ps1 packages -restore
    ```

1. Trash/remove the `cluedin_default_server_1` container using Docker Desktop or `docker rm` command, then run `./cluedin.ps1 up` to force this container to be recreated as shown below:

    ```shell
    ./cluedin.ps1 up
    +-----------------------------+
    | CluedIn - Environment => up |
    +-----------------------------+
    ...
    Creating cluedin_default_server_1 ... done
    ...
    ```

**Sql Server Connector is now available to use as an Export Target, setup in the UI.**

#### Deep clean extra components

In the event you need to remove all packages, it can be useful as part of troubleshooting to "deep clean" the components.

1. Delete the folders:

    ```shell
    env/default/components
    env/default/packages
    ```

1. Use `./cluedin.ps1 down` or trash/remove the `cluedin_default_server_1` container using Docker Desktop or `docker rm` command.

1. Use `./cluedin.ps1 up` to setup the cluster again.

NOTE: Remember to "Add CluedIn NuGet feed" after deleting the `packages` folder and re-add any components you require.

### Developing extra components

#### Increasing the log output

The environment is configured for `Production` level logging by default.
You can increase the amount of information produced by switching to `Development` before using `up` to start CluedIn.

The following will update the environment for `Development` level logging.  It will persist for all future runs of CluedIn:
```shell
./cluedin.ps1 env -set CLUEDIN_ENVIRONMENT=Development
```
### Adding extra components

You can add extra providers or enrichers in two different ways:

1. Via Nuget packages
    1. Add a a file named `Packages.txt` in the `./components` folder with the names of the nuget packages for the components you want to install.
    2. If the Nuget packages are not available publicly add a `nuget.config` file in the `./components` folder. Either pass the password token to the `nuget.config` or create a `KEY` environment variable with it.
2. Copy the relevant DLLs for the components in the `./components/ServerComponent` folder. 

You will also need to load in the deps.json files that are compiled in your C# projects.

If you are wanting to debug your additions locally then you will also want to copy in the .PDB files.

