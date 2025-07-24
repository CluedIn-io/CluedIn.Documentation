---
layout: cluedin
title: Suggested Searches
parent: User Interface
nav_order: 090
permalink: user-interface/suggested-searches
tags: ["ui","search"]
last_modified: 2021-10-27
published: false
---

## What are Suggested Searches?
Suggested searches are a way for developers to bring in related data into the single unified view of a record in the user interface of CluedIn. For example, for a company page, you might want to show the employees or you might want to show a list of all documents that are connected to this company directly or indirectly. 

For this, you can add your own custom suggested searches.

Here is a minimal example for implementing custom suggested searches.

See [CodeExample-SuggestedSearches](https://github.com/CluedIn-io/CodeExample-SuggestedSearches) as a reference point.

## Setup Test Data

1. Load in some sample data into your CluedIn instance.
2. When mapping the data, ensure that you have an Edge Type that is /RudiDoes (use the Advance Options)
3. Browse to your Neo4j instance (if local docker and org is foobar then try [http://foobar.127.0.0.1.nip.io:7474/](http://foobar.127.0.0.1.nip.io:7474/)
4. ![image](../assets/images/user-interface/neo4j-example-rudidoes.png)

## Code

Create new folder for this project:
```
% mkdir RudiDoesRelatedEntities
% cd RudiDoesRelatedEntities
```
Generate new files for this integration project:
```
% docker run --rm -ti -v ${PWD}:/generated cluedin/generator-crawler-template
? Name of this integration? RudiDoes
? Will it support webhooks? No
? Does it require OAuth? No
? The company name for this integration (used in dll metadata). CluedIn
? The product name for this integration (used in dll metadata). RudiDoes
```

(highly recommended but optional) Initialize a git repo (since it will allow us to deep clean our repo and commit at proper stages before the build artifacts are created):
```
git init
git add .
git commit -m "Initial commit"
```

Confirm environment and template is fine:
```
% dotnet build
…
Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:01:17.15

% dotnet pack
…
    Successfully created package '/Users/rudiharris/src/CluedIn-io/RudiDoesRelatedEntities/src/RudiDoes.Crawling/bin/Debug/RudiDoes.Crawling.RudiDoes.1.0.0.nupkg'.
    Successfully created package '/Users/rudiharris/src/CluedIn-io/RudiDoesRelatedEntities/src/RudiDoes.Provider/bin/Debug/RudiDoes.Provider.RudiDoes.1.0.0.nupkg'.
```

Check if nupkg files created:
```
% find . -name "*RudiDoes*.nupkg"
./src/RudiDoes.Crawling/bin/Debug/RudiDoes.Crawling.RudiDoes.1.0.0.nupkg
./src/RudiDoes.Infrastructure/bin/Debug/RudiDoes.Crawling.RudiDoes.Infrastructure.1.0.0.nupkg
./src/RudiDoes.Provider/bin/Debug/RudiDoes.Provider.RudiDoes.1.0.0.nupkg
./src/RudiDoes.Core/bin/Debug/RudiDoes.Crawling.RudiDoes.Core.1.0.0.nupkg
```

### New and Customized Files From Template

```csharp
src\RudiDoes.Provider\Installers\RelatedEntitiesInstaller.cs
	
using System.Linq;
using Castle.MicroKernel.Registration;
using Castle.MicroKernel.SubSystems.Configuration;
using Castle.Windsor;
using CluedIn.Core.Installers;
using CluedIn.RelatedEntities;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;
namespace CluedIn.RudiDoes.RelatedEntities.Installers
{
    public class RelatedEntitiesInstaller : IWindsorInstaller
    {
        private ILogger Log;
        public RelatedEntitiesInstaller(ILogger log)
        {
            Log = log;
        }
        public RelatedEntitiesInstaller()
        {
            Log = NullLogger.Instance;
        }
        public void Install(IWindsorContainer container, IConfigurationStore store)
        {
            //////////////////////////////////////////////////////////////////////////////////////////////////////////
            /// CODE ADDED

            Log.LogInformation("[RudiDoes] Begin CluedIn.RudiDoes.RelatedEntities.Installers.Install()");
            // RelatedEntitiesUtility.CypherFluentQueriesCount() requires RelatedEntitiesQueries to be registered
            container.Register(Component.For<RelatedEntitiesQueries>().Instance(new RelatedEntitiesQueries()));
            {
                // log all the classes that implement IRelatedEntitiesProvider
                // (that is the intent of our registration below
                // unfortunately castle windsor doesn't offer debug options around a IRegistration object)
                var classes = System.AppDomain.CurrentDomain.GetAssemblies()
                            .SelectMany(assembly => assembly.GetTypes())
                    .Where(type => type.GetInterfaces().Contains(typeof(IRelatedEntitiesProvider)))
                    .Where(type => type.AssemblyQualifiedName.Contains("RudiDoes"));
                foreach (var classRegistered in classes)
                {
                    Log.LogInformation($"[RudiDoes] Registering {classRegistered}");
                }
            }
            // register all the IRelatedEntitiesProvider classes
            container.Register(CluedInTypes.FromCluedInAssembliesWithServiceFromInterface<IRelatedEntitiesProvider>());
            Log.LogInformation("[RudiDoes] End CluedIn.RudiDoes.RelatedEntities.Installers.Install()");

            //////////////////////////////////////////////////////////////////////////////////////////////////////////
        }
    }
}
```

```csharp
src\RudiDoes.Provider\RudiDoesProviderComponent.cs
	
using Castle.MicroKernel.Registration;
using CluedIn.Core;
using CluedIn.Core.Providers;
// 
using CluedIn.Crawling.RudiDoes.Core;
using CluedIn.Crawling.RudiDoes.Infrastructure.Installers;
// 
using ComponentHost;
using CluedIn.Core.Server;
using CluedIn.RelatedEntities;
using CluedIn.RudiDoes.RelatedEntities.Installers;
using Microsoft.Extensions.Logging;
namespace CluedIn.Provider.RudiDoes
{
    [Component(RudiDoesConstants.ProviderName, "Providers", ComponentType.Service, ServerComponents.ProviderWebApi, Components.Server, Components.DataStores, Isolation = ComponentIsolation.NotIsolated)]
    public sealed class RudiDoesProviderComponent : ServiceApplicationComponent<IBusServer>
    {
        public RudiDoesProviderComponent(ComponentInfo componentInfo)
            : base(componentInfo)
        {
            // Dev. Note: Potential for compiler warning here ... CA2214: Do not call overridable methods in constructors
            //   this class has been sealed to prevent the CA2214 waring being raised by the compiler
            Container.Register(Component.For<RudiDoesProviderComponent>().Instance(this));
        }
        public override void Start()
        {
            //////////////////////////////////////////////////////////////////////////////////////////////////////////
            /// CODE ADDED

            Container.Install(new InstallComponents());
            var asm = System.Reflection.Assembly.GetExecutingAssembly();
            Container.Register(Types.FromAssembly(asm).BasedOn<IProvider>().WithServiceFromInterface().If(t => !t.IsAbstract).LifestyleSingleton());
            Container.Register(Types.FromAssembly(asm).BasedOn<IEntityActionBuilder>().WithServiceFromInterface().If(t => !t.IsAbstract).LifestyleSingleton());
            Container.Register(Types.FromAssembly(asm).BasedOn<IRelatedEntitiesProvider>().WithServiceFromInterface().If(t => !t.IsAbstract).LifestyleSingleton());
            Log.LogInformation("[RudiDoes] Begin CluedIn.Provider.RudiDoes.Start()");
            Container.Install(new RelatedEntitiesInstaller(Log));
            State = ServiceState.Started;
            Log.LogInformation("[RudiDoes] End CluedIn.Provider.RudiDoes.Start()");

            //////////////////////////////////////////////////////////////////////////////////////////////////////////
        }
        public override void Stop()
        {
            if (State == ServiceState.Stopped)
                return;
            State = ServiceState.Stopped;
        }
    }
}
```
	
```csharp
src\RudiDoes.Provider\RudiDoesRelatedEntitiesProvider.cs

using System.Collections.Generic;
using CluedIn.Core;
using CluedIn.Core.Data;
using CluedIn.DataStore.Document.Models;
using CluedIn.RelatedEntities;
using Microsoft.Extensions.Logging;
namespace CluedIn.Provider.RudiDoes
{
    public class RudiDoesRelatedEntitiesProvider : IRelatedEntitiesProvider
    {
        public IEnumerable<SuggestedSearch> GetRelatedEntitiesSearches(ExecutionContext context, Entity entity)
        {
            //////////////////////////////////////////////////////////////////////////////////////////////////////////
            /// CODE ADDED

            // use the provided Log object
            var Log = context.Log;
            Log.LogInformation($"[RudiDoes] RudiDoesRelatedEntitiesProvider.GetRelatedEntitiesSearches({context}, {entity})");
            if (entity.Type != EntityType.Organization)
            {
                Log.LogInformation("[RudiDoes] Entity is not an Organization - nothing to suggest");
                return new SuggestedSearch[0];
            }
            var searches = new List<SuggestedSearch>();
            if (RelatedEntitiesUtility.CypherFluentQueriesCount("{{RELATIONSHIP}} for {{ENTITY}}", string.Format("{0},{1}", "/RudiDoes", entity.Id.ToString()), context) > 0)
            {
                Log.LogInformation("[RudiDoes] CypherFluentQueries matches - adding suggested search");
                searches.Add(new SuggestedSearch {
                DisplayName = "RudiDoes",
                SearchQuery = "{{RELATIONSHIP}} for {{ENTITY}}",
                Tokens = string.Format("{0},{1}", "/RudiDoes", entity.Id.ToString()),
                Type = "List"
                });
            }
            else
            {
                Log.LogInformation("[RudiDoes] CypherFluentQueries does not match - nothing to suggest");
            }
            return searches;

            //////////////////////////////////////////////////////////////////////////////////////////////////////////
        }
    }
}
```
