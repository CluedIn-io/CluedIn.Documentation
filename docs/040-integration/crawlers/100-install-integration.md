---
layout: cluedin
title: Install integrations
parent: Crawlers
grand_parent: Ingestion
nav_order: 100
has_children: false
permalink: /integration/install-integrations
tags: ["integration"]
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

## Install integrations in Kubernetes

### Via the helm chart

In a production environment, using Kubernetes, you can configure the components that you want to install through the `values.yml` file. You can specify custom packages and versions, define your own package feeds, set authentication, and even use an alternative installer image.

```yaml
cluedin:
    components:
        image: ''    # name of the container to use as an installer - will default to 'cluedin
                     # nuget-installer'
        packages: [] # list of extra Nuget Packages to install in server in name, or name/version pairs
                     # version should be a supported nuget version format.
        sources: {}  # Nuget sources to use
```

At pod startup time, the packages will be passed from an init container to the CluedIn container.

#### Configure packages

Packages must be listed using their full package ID and an optional version. If you provide a version, you may use [floating versions](https://docs.microsoft.com/en-us/nuget/concepts/dependency-resolution#floating-versions), which are resolved at startup.

In this example, the latest version of `CluedIn.Crawling.HubSpot` will be installed, while for `CluedIn.Provider.HubSpot`, the latest 3.0.0 pre-release or full-release version will be installed.

```yaml
cluedin:
    components:
      packages:
      - name: CluedIn.Crawling.HubSpot
      - name: CluedIn.Provider.HubSpot
        version: 3.0.0-*
```


#### Configure sources

Packages can be resolved from one or more NuGet feeds. Each feed is defined under `sources` and may include optional authentication details.

```yaml
cluedin:
  components:
    sources:
      nuget:
        url: https://api.nuget.org/v3/index.json
      custom:
        url: https://myorg.myget.org/F/customfeed/api/v3/index.json
        user: OrgUser
        pass: OrgPass
```

### Via a custom image

You can build a custom Docker image that contains the integration packages. This approach ensures the packages and assets are already included in the init container and do not need to be downloaded at runtime.

1. Create a `packages.txt` file with the integrations to be installed. You can specify versions after the package name.

    ```txt
    CluedIn.Crawling.HubSpot
    CluedIn.Provider.HubSpot 3.0.0-*
    ```

1. Create a `nuget.config` with the feeds to be used. This is a standard [nuget.config](https://docs.microsoft.com/en-us/nuget/reference/nuget-config-file). The public nuget.org feed is included by  default.
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <configuration>
        <packageSources>
            <add key="custom" value="https://myorg.myget.org/F/customfeed/api/v3/index.json" />
        </packageSources>
    </configuration>
    ```

1. Use the following Docker file to build your image.

    If one or more feeds require credentials, you must expose an `ARG` and an `ENV` named `NUGETCRED_<feedname>` so the credentials can be passed to the install script.

    ```Dockerfile
    FROM cluedin/nuget-installer as base

    # If your feed requires passing credentials
    ARG CUSTOMCRED
    ENV NUGETCRED_CUSTOM=$CUSTOMCRED

    COPY . ./packages

    RUN ./Install-Packages.ps1

    FROM alpine as final
    COPY --from=base ./components ./tmp/components
    ENTRYPOINT ["sh", "-c", "false | cp $(ls -d /tmp/components/*/) -r ./components 2>/dev/null"]
    ```

4. Validate your custom image.

    ```sh
    # Build the image
    > docker build -t my/cluedin-installer .

    # OR build the image with creds - pass aregument as pipe delimited user|password
    > docker build -t my/cluedin-installer --build-arg CUSTOMCRED='user|pass' .

    # Mount components folder which is where the integration components would be placed
    > docker run --rm -it -v '.:/components' my/cluedin-installer
    ```
5. In `values.yal`, configure your custom image for component installation.
    ```yaml
    cluedin:
      components:
          image: 'my/cluedin-installer'
    ```