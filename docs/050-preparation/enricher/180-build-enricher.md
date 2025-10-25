---
layout: cluedin
nav_order: 18
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/build-custom-enricher
title: Build custom enricher

---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In CluedIn, an enricher allows you to take input from data flowing through the processing pipeline and then lookup services (typically external APIs) as to enrich just a single particular entity.

In our [HelloWorld example](https://github.com/CluedIn-io/CluedIn.Enricher.HelloWorld), we will obtain `Person` data from an external source called [JSON Placeholder](https://jsonplaceholder.typicode.com).

**Prerequesites**

CluedIn is a .NET platform. So you will need:

- .NET installed
- Visual Studio installed
- Docker

## Create initial template

To avoid cumbersome boilerplating, CluedIn provides you a script to generate a working Visual Studio solution.

## Install the generation tool

You will need to install node, npm, yeoman, and the generator itself.

1. Install Yeoman and `generator-cluedin-externalsearch` using npm (we assume you have pre-installed node.js).

1.  Create a new folder to store the new project. From the command prompt, run the following code to install the generator.

    ```shell
    npm install -g yo
    npm install -g generator-cluedin-externalsearch
    ```

1. Run the generator, providing `Name` and `Business Domain` (for example, Person or Company).

    ```shell
    yo cluedin-externalsearch
    ```

    For more information on how the CluedIn Server finds and loads type from integration assemblies, see `Naming Integrations` in the [Build Integration](./build-integration) documentation.

## Add models

First, we will setup a `User` class to receive the data. See [User.cs](https://github.com/CluedIn-io/CluedIn.Enricher.HelloWorld/blob/master/src/Models/User.cs).

```csharp
    public class User
	{
		public int id { get; set; }
		public string name { get; set; }
		public string username { get; set; }
		public string email { get; set; }
	}
```

## Add client

Next, we will add a client class and associated interface to fetch data from the external source. See [HelloWorldClient.cs](https://github.com/CluedIn-io/CluedIn.Enricher.HelloWorld/blob/master/src/Client/HelloWorldClient.cs) and [IHelloWorldClient.cs](https://github.com/CluedIn-io/CluedIn.Enricher.HelloWorld/blob/master/src/Client/IHelloWorldClient.cs).

```csharp
	public class HelloWorldClient : IHelloWorldClient
	{
		private const string BaseUri = "https://jsonplaceholder.typicode.com";

		private readonly IRestClient _client;

		public HelloWorldClient(IRestClient client)
		{
			_client = client ?? throw new ArgumentNullException(nameof(client));

			client.BaseUrl = new Uri(BaseUri);
		}

		public async Task<User> GetUser(string id) => await GetAsync<User>($"users/{id}");

		private async Task<T> GetAsync<T>(string url)
		{
			var request = new RestRequest(url, Method.GET);

			var response = await _client.ExecuteTaskAsync(request);

			if (response.StatusCode != HttpStatusCode.OK)
			{
				var diagnosticMessage = $"Request to {_client.BaseUrl}{url} failed, response {response.ErrorMessage} ({response.StatusCode})";

				throw new InvalidOperationException($"Communication to jsonplaceholder unavailable. {diagnosticMessage}");
			}

			var data = JsonConvert.DeserializeObject<T>(response.Content);

			return data;
		}

	}

	public interface IHelloWorldClient
	{
		Task<User> GetUser(string id);
	}
```

## Add vocabulary

Then we will define our vocabulary classes. See [HelloWorldVocabulary.cs](https://github.com/CluedIn-io/CluedIn.Enricher.HelloWorld/blob/master/src/Vocabularies/HelloWorldVocabulary.cs) and [HelloWorldVocabularies.cs](https://github.com/CluedIn-io/CluedIn.Enricher.HelloWorld/blob/master/src/Vocabularies/HelloWorldVocabularies.cs).

```csharp

	public class HelloWorldVocabulary : SimpleVocabulary
	{
		public HelloWorldVocabulary()
		{
			VocabularyName = "HelloWorld User";
			KeyPrefix = "helloworld.user";
			KeySeparator = ".";
			Grouping = EntityType.Unknown;

			AddGroup("HelloWorld Details", group =>
			{
				Id = group.Add(new VocabularyKey("Id", VocabularyKeyDataType.Integer, VocabularyKeyVisibility.Visible));
				Name = group.Add(new VocabularyKey("Name", VocabularyKeyDataType.PersonName, VocabularyKeyVisibility.Visible));
				Username = group.Add(new VocabularyKey("Username", VocabularyKeyDataType.PersonName, VocabularyKeyVisibility.Visible));
				Email = group.Add(new VocabularyKey("Email", VocabularyKeyDataType.Email, VocabularyKeyVisibility.Hidden));
			});

		}

		public VocabularyKey Id { get; private set; }
		public VocabularyKey Name { get; private set; }
		public VocabularyKey Username { get; private set; }
		public VocabularyKey Email { get; private set; }
	}

	public static class HelloWorldVocabularies
	{
		public static HelloWorldVocabulary User { get; } = new HelloWorldVocabulary();
	}

```

## Add provider

Lastly, we will add the provider class. See [HelloWorldExternalSearchProvider.cs](https://github.com/CluedIn-io/CluedIn.Enricher.HelloWorld/blob/master/src/HelloWorldExternalSearchProvider.cs).

```csharp
	public class HelloWorldExternalSearchProvider : ExternalSearchProviderBase
    {
	    private static readonly Guid ProviderId = Guid.Parse("2261b8f8-00b7-45bb-8112-5cc897fb16d8"); // TODO replace with new guid

        private readonly IHelloWorldClient _client;

        public HelloWorldExternalSearchProvider(IHelloWorldClient client)
            : base(ProviderId, EntityType.Person)
        {
	        _client = client;
        }

        public override IEnumerable<IExternalSearchQuery> BuildQueries(ExecutionContext context, IExternalSearchRequest request)
        {
			if (!Accepts(request.EntityMetaData.EntityType))
				yield break;

			var entityType = request.EntityMetaData.EntityType;

			var id = request.QueryParameters.GetValue(HelloWorldVocabularies.User.Id, new HashSet<string>());

			var person = new Dictionary<string, string>
			{
				{ "id",           id.FirstOrDefault() }
			};

			if (person.Any())
				yield return new ExternalSearchQuery(this, entityType, person);
        }

		public override IEnumerable<IExternalSearchQueryResult> ExecuteSearch(ExecutionContext context, IExternalSearchQuery query)
        {
            var id = query.QueryParameters["id"].FirstOrDefault();

            if (string.IsNullOrEmpty(id))
                yield break;

            var user = _client.GetUser(id).Result;
			if (user != null)
				yield return new ExternalSearchQueryResult<User>(query, user);
        }

		public override IEnumerable<Clue> BuildClues(ExecutionContext context, IExternalSearchQuery query, IExternalSearchQueryResult result, IExternalSearchRequest request)
		{
			var resultItem = result.As<User>();

			var code = GetOriginEntityCode(resultItem);

			var clue = new Clue(code, context.Organization);

			PopulateMetadata(clue.Data.EntityData, resultItem);

			return new[] {clue};
		}

		public override IEntityMetadata GetPrimaryEntityMetadata(ExecutionContext context, IExternalSearchQueryResult result, IExternalSearchRequest request)
        {
            var resultItem = result.As<User>();
            return CreateMetadata(resultItem);
        }

        public override IPreviewImage GetPrimaryEntityPreviewImage(ExecutionContext context, IExternalSearchQueryResult result, IExternalSearchRequest request)
        {
            return null;
        }

        private IEntityMetadata CreateMetadata(IExternalSearchQueryResult<User> resultItem)
        {
            var metadata = new EntityMetadataPart();

            PopulateMetadata(metadata, resultItem);

            return metadata;
        }

        private EntityCode GetOriginEntityCode(IExternalSearchQueryResult<User> resultItem)
        {
	        return new EntityCode(EntityType.Person, CodeOrigin.CluedIn.CreateSpecific("helloworld"), resultItem.Data.id);
        }

        private void PopulateMetadata(IEntityMetadata metadata, IExternalSearchQueryResult<User> resultItem)
        {
            var code = GetOriginEntityCode(resultItem);

            metadata.EntityType       = EntityType.Person;
            metadata.Name             = resultItem.Data.name;
            metadata.OriginEntityCode = code;

            metadata.Codes.Add(code);
			metadata.Properties[HelloWorldVocabularies.User.Email] = resultItem.Data.email;
		}
    }
```