---
layout: cluedin
title: Build an integration
parent: Crawlers
grand_parent: Ingestion
nav_order: 080
has_children: false
permalink: /integration/build-integration
tags: ["integration"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

CluedIn’s official integrations are designed as one-size-fits-all solutions. They generally attempt to ingest as much data as possible.

If you need more control—such as ingesting data selectively, connecting to in-house or legacy tools, or working with custom APIs—you will need to create a custom integration.

## Prerequisites

CluedIn is a .NET platform. Therefore, you will need the following:

- .NET installed
- Visual Studio installed
- Docker


## Create the initial template

To save time and avoid cumbersome boilerplate, CluedIn provides a script that generates a working Visual Studio solution for you.

**To create the initial template**

1. Create a folder for your provider.
    ```shell
    mkdir my-first-integration
    cd my-first-integration
    ```

1. Run the generator.
    ```shell
    docker run --rm -ti -v ${PWD}:/generated cluedin/generator-crawler-template
    ```
    The generator will ask some questions and will then generate all your solution files.

    ```shell
         _-----_     ╭──────────────────────────╮
        |       |    │  Welcome to the awesome  │
        |--(o)--|    │    CluedIn integration   │
       `---------´   │        generator!        │
        ( _´U`_ )    ╰──────────────────────────╯
        /___A___\   /
         |  ~  |
       __'.___.'__
     ´   `  |° ´ Y `

    ? Name of this crawler? MyFirstIntegration
    ? Will it support webhooks? No
    ? Does it require OAuth? No
    ```


1. Initialize a Git repository.
    ```shell
    git init
    git add .
    git commit -m "Initial commit"
    ```


1. Open the solution in Visual Studio and build it. Alternatively, build it from the command line using the .NET CLI:
    ```
    dotnet build
    ```


## Add a model

You need to perform several steps to create a crawler that fetches data, creates [clues](/key-terms-and-features/clue-reference), and passes them back to CluedIn for processing. For a working reference, see our [Hello World sample repository](https://github.com/CluedIn-io/CluedIn.Crawling.HelloWorld), which demonstrates the process using a simple external [JSON service ](https://jsonplaceholder.typicode.com/users).

The minimal steps required to replicate the Hello World example are as follows.

**To replicate the Hello World example**

1. Create model classes. You can use a subgenerator for this:
    ```shell
    docker run --rm -ti -v ${PWD}:/generated cluedin/generator-crawler-template crawler-template:model
    ```  

1. Answer the questions as shown in the example. This will create a User model and a vocabulary, matching the example in [User.cs](https://github.com/CluedIn-io/CluedIn.Crawling.HelloWorld/blob/master/src/HelloWorld.Core/Models/User.cs).
    ```shell
         _-----_     ╭──────────────────────────╮
        |       |    │    This sub-generator    │
        |--(o)--|    │   allows to create new   │
       `---------´   │       vocabularies       │
        ( _´U`_ )    ╰──────────────────────────╯
        /___A___\   /
         |  ~  |
       __'.___.'__
     ´   `  |° ´ Y `
    ? What is the model name? User
    ? What is the business domain? Person
    ? Enter a comma separated list of properties to add to the model id,name,username,email
    ? Choose the visibility for key: id(undefined) Visible
    ? Choose the type for key id Integer
    ? Should key id map to a common vocab? None
    ? Choose the visibility for key: name(undefined) Visible
    ? Choose the type for key name Text
    ? Should key name map to a common vocab? None
    ? Choose the visibility for key: username(undefined) Visible
    ? Choose the type for key username Text
    ? Should key username map to a common vocab? None
    ? Choose the visibility for key: email(undefined) Hidden
    ? Choose the type for key email Email
    ? Should key email map to a common vocab? ContactEmail
       create src/MyFirstIntegration.Core/Models/User.cs
       create src/MyFirstIntegration.Crawling/ClueProducers/UserClueProducer.cs
       create src/MyFirstIntegration.Crawling/Vocabularies/UserVocabulary.cs
       create test/MyFirstIntegration.Crawling.Unit.Test/ClueProducers/UserClueProducerTests.cs
    ```

    This will generate four files listed above. If you try to run the tests, one will fail because the ClueProducer still needs to be completed.

1. Go to the `src/MyFirstIntegration.Crawling/ClueProducers/UserClueProducer.cs` file. In line 29, uncomment the following code:
    ```csharp
    if(input.Name != null)
        data.Name = input.Name;
    ```
1. Delete all other comments in the `UserClueProducer.cs` file.

1. Open the `src/MyFirstIntegration.Infrastructure/MyFirstIntegrationClient.cs` file. In line 16, specify the URL for the endpoint:
    ```csharp
        private const string BaseUri = "https://jsonplaceholder.typicode.com";
    ```

1. Because this is a public endpoint, no tokens are required. Remove or comment out line 42.

    ```csharp
    // client.AddDefaultParameter("api_key", myfirstintegrationCrawlJobData.ApiKey, ParameterType.QueryString);`
    ```
1. Add a method to retrieve users. You will also need to import some namespaces.

    ```csharp
    public async Task<IList<User>> GetUsers() => await GetAsync<IList<User>>("users");
    ```

1. In the `src/MyFirstIntegration.Crawling/MyFirstIntegrationCrawler.cs` file, you retrieve the data you want to insert in CluedIn. Add the following code inside the `GetData` method:
    ```csharp
        //retrieve data from provider and yield objects

        foreach( var user in client.GetUsers().Result)
        {
            yield return user;
        }
    ```

1. To test the provider, you can use the provided integration test. Open the `test/integration/Crawling.MyFirstIntegration.Integration.Test/MyFirstIntegrationDataIngestion.cs` file. Then, in the `CorrectNumberOfEntityTypes` method, add a new annotation to indicate the expected result: 10 persons (the default return from the sample endpoint).
    ```csharp
    [Theory]
    [InlineData("/Provider/Root", 1)]
    [InlineData("/Person", 10)]
    public void CorrectNumberOfEntityTypes(string entityType, int expectedCount)
    ```

1. Execute the tests. They should all pass.

1. Before adding the integration to CluedIn, open the `src\MyFirstIntegration.Core\MyFirstIntegrationConstants.cs` file. Then, modify the values for the constants before the `TODO` comment. This information will be used in the CluedIn GUI to show information about the integration.

    In particular, make sure to set the following:

    - `CrawlerDescription` – A short description of the crawler.

    - `Integration` – The name of the integration.

    - `Uri` – The URL of the tool, if this integration corresponds to an online service.

    - `IconResourceName` – The path of an embedded resource in the provider project.

## Architecture

As shown in the example, these are the main components of a CluedIn integration:

- **Client** (for example, `MyFirstIntegrationClient.cs`):

    - Responsible for retrieving data from your source.

    - Contains methods that return plain objects with the required information.

- The `GetData` method in the main crawling class `MyFirstIntegrationCrawler.cs`:

    - Acts as the entry point for the provider.

    - Invokes the client’s methods to retrieve plain objects.

- **Vocabulary class** (for example, `UserVocabulary.cs`):

    - Mostly generated automatically.

    - Defines the data keys you are processing and maps them to generic terms (such as email, address, company) used across CluedIn.

    - Can also define relationships with other vocabularies (known as [edges](/key-terms-and-features/edges)). For example, the relationship between a user and a company.

- **ClueProducer** (for example, `UserClueProducer.cs`):

    - Translates plain objects retrieved by the client into [clues](/key-terms-and-features/clue-reference), the format understood by CluedIn.

    - Uses the keys defined in the vocabulary to map object data to the clue.

In this case, the sample API was open and generic. In other cases, however, you may need additional details—such as credentials, data sources, or connection parameters—to access the source and determine what data to retrieve. This information can be captured in `CrawlJobData` (for example, `MyFirstIntegrationCrawlJobData.cs`), which you can enrich with any properties you need. To support this, you must also extend two methods in the provider (for example, `MyFirstIntegrationProvider.cs`):

- `GetCrawlJobData` – Translates the keys from a generic dictionary into the `CrawlJobData` object.

- `GetHelperConfiguration` – Performs the opposite translation (from `CrawlJobData` to a dictionary).


## Deploy the provider locally

If you are running CluedIn locally for testing purposes using Docker, you can add your integration by following the provided steps.

**To deploy the provider locally**

1. Set up your environment:

    - You most likely used the Home GitHub repository to pull your CluedIn environment down and boot it up.

    - You can now use this repository to inject extra components into CluedIn.

    - Under the `env` folder, you can either use the `default` folder or can create new environments (see the Home GitHub README for details).

1. Inside your chosen environment folder, open the `components` folder.

1. In there, create a new folder called `ServerComponent`. This folder is where you inject your DLL files. On startup, the CluedIn Server Docker container will scan this folder and load the assemblies.

1. For a crawler integration, copy the following files into the `ServerComponent` folder:

    - The DLL files produced by your different projects (excluding test DLLs).

    - The JSON dependency file.

    - Any third-party libraries used in your crawler (for example, a custom NuGet package for accessing a service).

    - (Optional) The PDB files, if you need to debug. 

1. Restart the CluedIn Server Docker container. Make sure that the versions of your CluedIn dependencies match the version of CluedIn you are running. You can check the version in your `packages.props` file.

    ````xml
    <PropertyGroup Label="Dependency Versions">
        <_ComponentHost>2.0.0-alpha-14</_ComponentHost>
        <_AutoFixture>4.11.0</_AutoFixture>
        <_CluedIn>3.2.2</_CluedIn>
     </PropertyGroup>
    ```

## Test the provider in your environment

To test your provider locally, follow the steps in [Install integrations](./install-integrations).


## Generate models, vocabularies, and ClueProducers

You can use the [FileGenerator GitHub repository](https://github.com/CluedIn-io/Crawling.FileGenerator) to generate basic models, vocabularies, and ClueProducers. The generator supports three input options:

- Metadata file

- CSV files with data

- Microsoft SQL Server

The generated code will need to be updated based on the specifics of your data source. More details are available in the repository’s README.
