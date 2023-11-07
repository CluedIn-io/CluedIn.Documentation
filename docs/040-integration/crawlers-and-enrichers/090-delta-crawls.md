---
layout: default
title: Delta Crawls
parent: Crawlers and enrichers
grand_parent: Integration
nav_order: 090
has_children: false
permalink: /integration/delts-crawls
tags: ["integration","delta-crawls"]
---

### What are delta crawls

By default, when adding a new provider, CluedIn sets up two recurring jobs - one that runs every 4 hours and one that runs every 7 days. These jobs can be customised for different intervals or simply disabled.

The weekly job is supposed to run a full crawl again.

The one that runs every 4 hours is called **delta crawl** - a crawl job designed to bring **only the data that is new and hasn't been ingested into CluedIn yet**.

To setup the crawler to support delta crawls as well as full crawls, you can use the `LastCrawlFinishTime` property of the `JobData` object that is available in the crawlers. Once a crawl job has finished, this property is updated with the corresponding date and time and it is available at runtime in the crawler.

An example of how delta crawls can be implemented while still accepting full crawls can be found below:

In the crawler's JobData, we can add a new configurable property as such:

```csharp
public bool FullCrawl { get; set; } = false;
```

And in the JobData's constructor, we can give the property the value from configuration:

```csharp
if (configuration.ContainsKey("FullCrawl") && !string.IsNullOrEmpty(configuration["FullCrawl"].ToString()))
                FullCrawl = GetValue<bool>(configuration, "FullCrawl");
```

In the Client class we check for the FullCrawl's value - if it's false, we continue with the delta crawl; if it's true, we continue with the full crawl. Below we can find two examples of how this can be implemented for an API and for SQL.

Using Eloqua's Bulk API publicly available filters documentation: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-develop/Developers/BulkAPI/Tutorials/Filtering.htm.

```csharp

var exportDefinitionRequest = new ExportDefinitionRequest
{
    Name = "CluedIn Contact Export",
    Fields = new Dictionary<string, string>
    {
        { "EmailAddress", "Contact.Field(C_EmailAddress)"},
        { "FirstName", "Contact.Field(C_FirstName)"},
        { "LastName", "Contact.Field(C_LastName)"}
    }
};

if (!_jobData.FullCrawl && _jobData.LastCrawlFinishTime > DateTime.MinValue)
{
    exportDefinitionRequest.Filter = "'Contact.Field(C_DateModified)' > '" + $"{_jobData.LastCrawlFinishTime.ToString()}" + "'";
}

var exportDefinitionResponse = await PostAsync<ExportDefinitionResponse>("contacts/exports", exportDefinitionRequest);

return exportDefinitionResponse;
```

Using an imaginary Oracle SQL database example:

```csharp

public IEnumerable<SqlEntity> GetObject()
{
    var offsetInitValue = GetInitialOffset();

    var maxNumberOfRows = GetMaxNumberOfRows(tableName);

    var whereStatement = string.Empty;

    if (!_jobData.FullCrawl && _jobData.LastCrawlFinishTime > DateTime.MinValue)
        whereStatement = $"WHERE ModifiedDateColumn > {_jobData.LastCrawlFinishTime}";

    for (var offset = offsetInitValue; offset < maxNumberOfRows; offset += _jobData.PageSize)
    {
        using (var connection = new OracleConnection(_jobData.ConnectionString))
        using (var command = connection.CreateCommand())
        {
            OracleDataReader reader = null;
            try
            {
                connection.Open();

                reader = ActionExtensions.ExecuteWithRetry(() =>
                {
                    command.CommandText = $@"SELECT f.*
                                                FROM (
                                                    SELECT t.*, rownum r
                                                    FROM (
                                                        SELECT *
                                                        FROM SqlTable
                                                        {whereStatement}
                                                        ORDER BY ModifiedDateColumn) t
                                                    WHERE rownum <= {offset + _jobData.PageSize}) f
                                                WHERE r > {offset}";

                    command.CommandTimeout = 180;

                    return command.ExecuteReader();
                },
                isTransient: ex => ex is OracleException || ex.IsTransient());
            }
            catch (Exception exception)
            {
                _log.LogError(exception.Message, exception);
                yield break;
            }


            while (reader.Read())
            {
                SqlEntity sqlEntity = null;

                try
                {
                    sqlEntity = new SqlEntity(reader);
                }
                catch (Exception exception)
                {
                    _log.LogError(exception.Message, exception);
                    continue;
                }

                if(sqlEntity != null)
                  yield return sqlEntity;
            }

        }
    }
}
```

Please note that the syntax `Contact.Field(<field name>)` should be put in double brackets (as per API's documentation), which have not been included in the code snippet for formatting reasons.


### Stream Delta Crawls

Delta crawls can also be setup as consumers for stream platforms such as Kafka. If a Kafka stream has not been set up yet, make sure Change Data Capture is enabled for the database and CluedIn can implement [Debezium](https://debezium.io/documentation/reference/1.2/#_what_is_it) as a Kafka stream (if the database of choice is supported). After we implemented Debezium, we then integrate the crawlers with the stream. One simple example of how a Client can be implemented with Kafka can be found in our [public Kafka example crawler](https://github.com/CluedIn-io/Crawling.ExampleKafka/blob/master/src/Kafka.Infrastructure/KafkaClient.cs).
