---
category: Integration
title: Install Integration
---

### Using Docker

If you are running CluedIn using Docker, for testing and evaluation purposes, you can follow the [adding extra components](/docs/00-gettingStarted/docker-local.html#adding-extra-components) instructions.


### Installing integrations in Kubernetes 

#### Via the helm chart

In a production environment, using Kubernetes, you can add the components you want to install through the [`values.yml`](/docs/00-gettingStarted/kubernetes.html#installation) file. You can also specify different nuget sources for those packages:

```yaml
cluedin:
    components:
        packages:
        - nuget.package1
        - nuget.package2
        sources: # optionally add nuget sources
            mynugetfeed: # any name you want to give to this feed
                url: url-to-my-nuget-feed
```

If those sources require authentication, you can create a secret with a variable `KEY` with the PAT credentials:

```shell
kubectl create secret generic --from-literal=KEY=<token-to-access-nuget> my-nuget-secret
```
Then you can add the name of the secret to the `values.yml` file.
```yaml
cluedin:
    secrets:
    - my-nuget-secret
```

---
#### Via custom image

Alternatively you could build your own Docker image, using the CluedIn one as a base, copying the files for the components. This has the advantage that the container can start up quicker, as it does not have to download nuget packages, plus also it does not require communication to the nuget feed. 

You can add:

1. DLLs you want to install

    ```Dockerfile
    FROM cluedin/cluedin-server:ltsc2019-latest

    COPY <your-dlls> /app/ServerComponent
    ```

1. a list of nuget packages and a `nuget.config`:
    ```Dockerfile
    # escape=`

    FROM cluedin/cluedin-server:ltsc2019-develop

    COPY nuget.config Packages.txt /nuget/

    RUN /Install-Packages.ps1 -PackageListFile \nuget\Packages.txt -nugetConfig \nuget\nuget.config; `
        mv \packages\*.dll \app\ServerComponent\; `
        rm \nuget -Recurse -Force
    ```

2. nuget packages from a private repo that requires authentication:
    ```Dockerfile
    # escape=`

    FROM cluedin/cluedin-server:ltsc2019-develop

    ARG KEY

    COPY nuget.config Packages.txt /nuget/

    RUN /Install-Packages.ps1 -Key=$KEY -FeedNames @('private-feed-1','private-feed-2') -PackageListFile \nuget\Packages.txt -nugetConfig \nuget\nuget.config; `
        mv \packages\*.dll \app\ServerComponent\; `
        rm \nuget -Recurse -Force
    ```
    You would then pass the key as a build argument: e.g. `docker build . --build-arg=KEY=<my-nuget-key> -t my-custom-cluedin-server-image`

