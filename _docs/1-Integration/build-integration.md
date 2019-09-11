---
category: Integration
title: Build Integration
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

### Install the generation tool

You will need to install node, npm, yeoman and the generator itself.

First, install Yeoman and generator-cluedin-crawler using npm (we assume you have pre-installed node.js).

```shell
> npm install -g yo generator-cluedin-crawler
```

### Execute the generation tool

All you need to do is mount the target folder where you would like the generator to create the files, and run the container. So for example if you want to crate the solution under `c:\projects\CluedinCrawler` you would run:

```shell
docker run --rm -ti -v c:/projects/CluedinCrawler:/generated cluedin/generator-crawler-template
```

If you are already in the target location you could just use the variable ${PWD}:

```shell
docker run --rm -ti -v ${PWD}:/generated cluedin/generator-crawler-template
```

To execute the script, simply go to the folder where you want to create the solution and invoke:

```shell
> yo cluedin-crawler.
```

Your visual studio solution is now created.

For more advanced installation, please refer to our generation tooling documentation.

### Adding a Model

There are several steps needed to create a crawler that fetches data, creates Clues and passes them back to CluedIn for processing. Please refer to our [Hello World](https://github.com/CluedIn-io/CluedIn.Crawling.HelloWorld) sample repository for a working example. This is based on a simple external [JSON service ](https://jsonplaceholder.typicode.com/users)

Using the steps above to generate project called Crawling.HelloWorld, the following is the minimal steps required:

Steps:

1. Create model classes. See [User.cs](https://github.com/CluedIn-io/CluedIn.Crawling.HelloWorld/blob/master/src/HelloWorld.Core/Models/User.cs)

```csharp
    public class User
    {
        public int id { get; set; }
        public string name { get; set; }
        public string username { get; set; }
        public string  email { get; set; }
    }
```

2. Create class to fetch remote data. See [HelloworldClient.cs](https://github.com/CluedIn-io/CluedIn.Crawling.HelloWorld/blob/master/src/HelloWorld.Infrastructure/HelloWorldClient.cs)

```csharp
    public class HelloWorldClient
    {
        private const string BaseUri = "https://jsonplaceholder.typicode.com";

        private readonly ILogger _log; 
        private readonly IRestClient _client;

        public HelloWorldClient(ILogger log, HelloWorldCrawlJobData helloWorldCrawlJobData, IRestClient client) // TODO: pass on any extra dependencies
        {
            if (helloWorldCrawlJobData == null) throw new ArgumentNullException(nameof(helloWorldCrawlJobData));

            this._log = log ?? throw new ArgumentNullException(nameof(log));
            this._client = client ??  throw new ArgumentNullException(nameof(client));

            client.BaseUrl = new Uri(BaseUri);
        }

        public async Task<IList<User>> GetUsers() => await this.GetAsync<IList<User>>("users");

        private async Task<T> GetAsync<T>(string url)
        {
            var request = new RestRequest(url, Method.GET);

            var response = await this._client.ExecuteTaskAsync(request);

            if (response.StatusCode != HttpStatusCode.OK)
            {
                var diagnosticMessage = $"Request to {this._client.BaseUrl}{url} failed, response {response.ErrorMessage} ({response.StatusCode})";

                this._log.Error(() => diagnosticMessage);

                throw new InvalidOperationException($"Communication to jsonplaceholder unavailable. {diagnosticMessage}");
            }

            var data = JsonConvert.DeserializeObject<T>(response.Content);

            return data;
        }


        public AccountInformation GetAccountInformation()
        {
            return new AccountInformation("", ""); //TODO
        }
    }
```

3. Create vocabulary. See [UserVocabulary.cs](https://github.com/CluedIn-io/CluedIn.Crawling.HelloWorld/blob/master/src/HelloWorld.Crawling/Vocabularies/UserVocabulary.cs)

```csharp
    public class UserVocabulary : SimpleVocabulary
    {
        public UserVocabulary()
        {
            this.VocabularyName = "HelloWorld User";
            this.KeyPrefix = "helloworld.user";
            this.KeySeparator = ".";
            this.Grouping = EntityType.Unknown;

            this.AddGroup("HelloWorld Details", group =>
              {
                  this.Id = group.Add(new VocabularyKey("Id", VocabularyKeyDataType.Integer, VocabularyKeyVisiblity.Visible));
                  this.Name = group.Add(new VocabularyKey("Name", VocabularyKeyDataType.PersonName, VocabularyKeyVisiblity.Visible));
                  this.Username = group.Add(new VocabularyKey("Username", VocabularyKeyDataType.PersonName, VocabularyKeyVisiblity.Visible));
                  this.Email = group.Add(new VocabularyKey("Email", VocabularyKeyDataType.Email, VocabularyKeyVisiblity.Hidden));
              });

        }

        public VocabularyKey Id { get; private set; }
        public VocabularyKey Name { get; private set; }
        public VocabularyKey Username { get; private set; }
        public VocabularyKey Email { get; private set; }
    }
```

4. Create Clue Producer. See [](https://github.com/CluedIn-io/CluedIn.Crawling.HelloWorld/blob/master/src/HelloWorld.Crawling/ClueProducers/UserClueProducer.cs)

```csharp
    public class UserClueProducer : BaseClueProducer<User>
    {
        private readonly IClueFactory _factory;

        public UserClueProducer(IClueFactory factory)
        {
            this._factory = factory ?? throw new ArgumentNullException(nameof(factory));
        }

        protected override Clue MakeClueImpl(User input, Guid accountId)
        {
            if (input == null) throw new ArgumentNullException(nameof(input));

            // TODO: Create clue specifying the type of entity it is and ID
            var clue = this._factory.Create(EntityType.Person, input.id.ToString(), accountId);

            // TODO: Populate clue data
            var data = clue.Data.EntityData;

            var vocab = new UserVocabulary();
            data.Properties[vocab.Id] = input.id.PrintIfAvailable();

            data.Name = input.name.PrintIfAvailable();
            data.Properties[vocab.Name] = input.name.PrintIfAvailable();

            data.Properties[vocab.Email] = input.email;
            data.Properties[vocab.Username] = input.username;

            clue.ValidationRuleSuppressions.AddRange(new[]
            {
                RuleConstants.DATA_001_File_MustBeIndexed,
                RuleConstants.METADATA_002_Uri_MustBeSet,
                RuleConstants.METADATA_003_Author_Name_MustBeSet,
                RuleConstants.PROPERTIES_002_Unknown_VocabularyKey_Used
            });

            return clue;
        }
    }
```

5. Create Crawler class. See [HelloWorldCrawler.cs](https://github.com/CluedIn-io/CluedIn.Crawling.HelloWorld/blob/master/src/HelloWorld.Crawling/HelloWorldCrawler.cs)



```csharp
    public class HelloWorldCrawler : ICrawlerDataGenerator
    {
        private readonly IHelloWorldClientFactory _clientFactory;
        public HelloWorldCrawler(IHelloWorldClientFactory clientFactory)
        {
            this._clientFactory = clientFactory;
        }

        public IEnumerable<object> GetData(CrawlJobData jobData)
        {
            if (!(jobData is HelloWorldCrawlJobData helloworldcrawlJobData))
            {
                yield break;
            }

            var client = this._clientFactory.CreateNew(helloworldcrawlJobData);

            //crawl data from provider and yield objects

            foreach( var user in client.GetUsers().Result)
            {
                yield return user;
            }
        }       
    }
```

### Deploying the crawler locally

TODO

### Testing the crawler

Please refer to [install an integration](/docs/1-Integration/install-integration.html)
