---
category: Integration
title: Install Integration
---
### Installing integrations in Kubernetes

#### Via the helm chart

In a production environment, using Kubernetes, you can add the components you want to install through the [`values.yml`](/docs/00-gettingStarted/kubernetes.html#installation) file.
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
> In this example the `nuget` feed is used without authentication, while the `custom`  feed uses credentials


Credentials can also be passed to the helm install/upgrade command when invoked.