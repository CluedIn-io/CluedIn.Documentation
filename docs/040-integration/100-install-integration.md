---
layout: default
title: Install Integrations
parent: Integration
nav_order: 100
has_children: false
permalink: /integration/install-integrations
tags: ["integration"]
---


### Installing integrations in Kubernetes

#### Via the helm chart

In a production environment, using Kubernetes, you can add the components you want to install through the [`values.yml`](../deployment/kubernetes/deployment) file.
You can specify your own packages and the versions to be installed.  You can also provide your own package feeds, authentication, and even an alternative installer image.

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

##### Configuring Packages

Packages should be listed using their full package id and an optional version.
When supplying the version, you may use [floating versions](https://docs.microsoft.com/en-us/nuget/concepts/dependency-resolution#floating-versions) to allow the version to be resolved at startup time.

```yaml
cluedin:
    components:
      packages:
      - name: CluedIn.Crawling.HubSpot
      - name: CluedIn.Provider.HubSpot
        version: 3.0.0-*
```
> In this example the latest version of `CluedIn.Crawling.HubSpot` will be installed, while the latest 3.0.0 pre-release, or full-release version of `CluedIn.Provider.HubSpot` will be installed.

##### Configuring Sources

The packages to install may be resolved from one or more nuget feeds.
Each feed can be configured under `sources` with optional authentication details

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

---
#### Via Custom Image

You can build your own docker image to contain the integration packages.  This has the advantage that the packages and assets are already contained in the init container and do not need to be downloaded.

1. Create a `packages.txt` file with the integrations to be installed. Versions can be specified after the package name
    ```txt
    CluedIn.Crawling.HubSpot
    CluedIn.Provider.HubSpot 3.0.0-*
    ```
1. Create a `nuget.config` with the feeds to be used.  This is a standard [nuget.config](https://docs.microsoft.com/en-us/nuget/reference/nuget-config-file).
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <configuration>
        <packageSources>
            <add key="custom" value="https://myorg.myget.org/F/customfeed/api/v3/index.json" />
        </packageSources>
    </configuration>
    ```
    > The public nuget.org feed is already included by  default
1. Use the following Dockerfile to build your image
    ```Dockerfile
    FROM cluedin/nuget-installer as base

    # If your feed requires passing credentials
    ARG CUSTOMCRED
    ENV NUGETCRED_CUSTOM=$CUSTOMCRED

    COPY . ./packages

    RUN ./Install-Packages.ps1

    FROM alpine as final
    COPY --from=base ./components ./tmp/components
    ENTRYPOINT ["sh", "-c", "false | cp $(ls -d /tmp/components/*/) -ir ./components 2>/dev/null"]
    ```
    > If one or more feeds requires credentials, you'll need to expose an `ARG`
    and an `ENV` named `NUGETCRED_<feedname>` to allow passing to the install script.

4. Validate your custom image
    ```sh
    # Build the image
    > docker build -t my/cluedin-installer .

    # OR build the image with creds - pass aregument as pipe delimited user|password
    > docker build -t my/cluedin-installer --build-arg CUSTOMCRED='user|pass' .

    # Mount components folder which is where the integration components would be placed
    > docker run --rm -it -v '.:/components' my/cluedin-installer
    ```
5. In the `values.yal` configure your custome image for the components install
    ```yaml
    cluedin:
      components:
          image: 'my/cluedin-installer'
    ```