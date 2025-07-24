---
layout: cluedin
title: Build Integration
parent: Crawlers
grand_parent: Ingestion
nav_order: 080
has_children: false
permalink: {{ site.baseurl }}/integration/build-integration
tags: ["integration"]
---
### Introduction

CluedIn official integrations are one size fits all integrations. They will generally try to ingest as much data as they can.

If you want to ingest data in a precise fashion or want to ingest data from an in-house tool, an old tool, from some custom APIs, you will need to create your own integration.

### Pre-requesite

CluedIn is a .NET platform. So you will need:

- .NET installed
- Visual Studio installed
- Docker


### Creating initial template

To avoid cumbersome boilerplating, CluedIn provides you a script to generate a working Visual studio solution.

1. Create a folder for your provider
    ```shell
    mkdir my-first-integration
    cd my-first-integration
    ```

1. Run the generator
    ```shell
    docker run --rm -ti -v ${PWD}:/generated cluedin/generator-crawler-template
    ```
    The generator will ask some questions and then generate all your solution files:

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


1. Initialize a git repo
    ```shell
    git init
    git add .
    git commit -m "Initial commit"
    ```


1. Open the solution in Visual Studio and build it or alternatively you should also build it from the command line using the dotnet cli: `dotnet build` 


### Adding a Model

There are several steps needed to create a crawler that fetches data, creates Clues and passes them back to CluedIn for processing. Please refer to our [Hello World](https://github.com/CluedIn-io/CluedIn.Crawling.HelloWorld) sample repository for a working example. This is based on a simple external [JSON service ](https://jsonplaceholder.typicode.com/users)

The following is the minimal steps required to replicate the _Hello World_ example:

1. Create model classes. You can use a subgenerator for this:
    ```shell
    docker run --rm -ti -v ${PWD}:/generated cluedin/generator-crawler-template crawler-template:model
    ```  

1. Answer the questions as follows, to create a User model and vocabulary, similar to the one in the example [User.cs](https://github.com/CluedIn-io/CluedIn.Crawling.HelloWorld/blob/master/src/HelloWorld.Core/Models/User.cs)
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

    This will generate 4 files as shown above. If you try to run the tests you will notice there is a failing one, as we need to complete some work in the ClueProducer.

1. Go to the `src/MyFirstIntegration.Crawling/ClueProducers/UserClueProducer.cs` file, in line 29 uncomment the following code:
    ```csharp
    if(input.Name != null)
        data.Name = input.Name;
    ```
1. Delete all other comments in the `UserClueProducer.cs` file.

1. Open the `src/MyFirstIntegration.Infrastructure/MyFirstIntegrationClient.cs` and modify line 16 with the URL for the endpoint:
    ```csharp
        private const string BaseUri = "https://jsonplaceholder.typicode.com";
    ```

1. Since this is a public endpoint we don't need to pass any tokens. Remove or comment out line 42

    ```csharp
    // client.AddDefaultParameter("api_key", myfirstintegrationCrawlJobData.ApiKey, ParameterType.QueryString);`
    ```
1. Add a method to retrieve users (you will need to import some namespaces too):

    ```csharp
    public async Task<IList<User>> GetUsers() => await GetAsync<IList<User>>("users");
    ```

1. In the `src/MyFirstIntegration.Crawling/MyFirstIntegrationCrawler.cs` you retrieve the data you want to insert in CluedIn. Add the following inside the `GetData` method:
    ```csharp
        //retrieve data from provider and yield objects

        foreach( var user in client.GetUsers().Result)
        {
            yield return user;
        }
    ```

1. In order to test the provider, you can use the Integration test provided. Open the `test/integration/Crawling.MyFirstIntegration.Integration.Test/MyFirstIntegrationDataIngestion.cs` file, and in the `CorrectNumberOfEntityTypes` method add a new annotation to indicate the expectation of receiving 10 Persons (that's what the sample endpoint returns by default):
    ```csharp
    [Theory]
    [InlineData("/Provider/Root", 1)]
    [InlineData("/Person", 10)]
    public void CorrectNumberOfEntityTypes(string entityType, int expectedCount)
    ```

1. Execute the tests - they should all pass.

1. Before adding the integration to CluedIn, open the file `src\MyFirstIntegration.Core\MyFirstIntegrationConstants.cs` and modify the values for the constants before the `TODO` comment. This information will be used in the GUI of CluedIn to show information about the integration. In particular you should set the `CrawlerDescription`, `Integration`, `Uri` (if this integration corresponds to an online tool), and `IconResourceName`. This last property corresponds to the path of an embedded resource in the Provider project.

### Architecture

As you can see in the example - these are the main components:
- A *client* that knows how to retrieve data from your source (e.g. `MyFirstIntegrationClient.cs`). It has methods to produce plain objects with the information.
- The method `GetData` in the main Crawling class `MyFirstIntegrationCrawler.cs` - you can consider this as the entry point for the provider. This method will invoke the correct methods of the *client*, in order to yield plain objects.
- A *Vocabulary* class (e.g. `UserVocabulary.cs`) which is for the most part generated automatically. This class defines the different keys of the data you are processing and how they map to generic terms (email, address, company) also in use in other sources. In addition it can define the relationship with other *Vocabularies* (also known as edges). For example the relationship between a user and a company.
- A *ClueProducer* (e.g. `UserClueProducer.cs`) which essentially translates the plain object (retrieved by the *client*) into a *clue*, which is the object understood by CluedIn. It uses the keys from the *Vocabulary* to map the data from the object to the clue.

In this case the sample API was very open and generic, however in other cases you may need extra information (credentials, data sources, etc.) on how to connect to the source, or what data to retrieve. This can be captured in the *CrawlJobData* (e.g. `MyFirstIntegrationCrawlJobData.cs`). You can enrich it with whatever properties you need. However, you will also need to expand two methods in the *Provider* (e.g. `MyFirstIntegrationProvider.cs`):
- `GetCrawlJobData` which translates the keys from a generic dictionary into the *CrawlJobData* object and
- `GetHelperConfiguration` which performs the opposite translation (from the *CrawlJobData* to a dictionary)


### Deploying the provider locally

If you are running CluedIn locally for testing purposes using Docker, you can follow these instructions to add the integration.

You most likely used the Home GitHub repo to pull your CluedIn environment down and boot it up. You can now use this to inject extra components into CluedIn.

Under the `env` folder you can use the `default` folder or you can create new environments (See Home GitHub Readme). 

Within this folder there is a `components` folder. Create a new folder in here called `ServerComponent`. This is essentially a folder in which you can inject your own DLL files and CluedIn will look in this folder on boot of the CluedIn Server Docker Container and load these assemblies as well. 

In the example of a Crawler, you will need to copy the DLL files produced by your different projects (not including the test DLLs), the .json dependency file, any third party libraries you used in your crawler (e.g. a custom NuGet package for talking to a service) and optionally you will want the PDB files if you would like to debug. 

Copy all of these into your newly created `ServerComponent` folder and restart the CluedIn Server Docker container. Make sure that the version of your CluedIn dependencies are exactly the same as the version you are running of CluedIn. You can check this in your packages.props file.

````xml
<PropertyGroup Label="Dependency Versions">
    <_ComponentHost>2.0.0-alpha-14</_ComponentHost>
    <_AutoFixture>4.11.0</_AutoFixture>
    <_CluedIn>3.2.2</_CluedIn>
  </PropertyGroup>
```

### Testing the provider in your environment

Please refer to [install an integration](./install-integrations)


### Generating Models, Vocabularies and ClueProducers

Please refer to the [FileGenerator GitHub Repository](https://github.com/CluedIn-io/Crawling.FileGenerator). This can be used to generate basic models, vocabularies and clue producers using one of three options: Metadata file; CSV files with data; Microsoft SQL Server. The generators need to be updated depending on each data source - more details can be found in the README section of the repository.
