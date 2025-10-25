---
layout: cluedin
title: Delta crawls
parent: Crawlers
grand_parent: Ingestion
nav_order: 090
has_children: false
permalink: /integration/delts-crawls
tags: ["integration","delta-crawls"]
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

## About delta crawls

By default, when adding a new provider, CluedIn sets up two recurring jobs:

- Delta crawl (every 4 hours) – Brings only the new data that hasn’t yet been ingested into CluedIn.

- Full crawl (every 7 days) – Runs a complete crawl of the source again.

These jobs can be customized for different intervals or disabled entirely.

To support both delta crawls and full crawls, crawlers use the `LastCrawlFinishTime` property of the `JobData` object. After a crawl job finishes, this property is updated with the corresponding date and time, making it available for the next run.

## Implementation example

The following example illustrates how to implement delta crawls while still accepting full crawls.

**To implement crawls**

1. In the crawler's `JobData`, add a new configurable property.

    ```csharp
    public bool FullCrawl { get; set; } = false;
    ```

1. In the `JobData` constructor, set the property value from the configuration.
    
    ```csharp
    if (configuration.ContainsKey("FullCrawl") && !string.IsNullOrEmpty(configuration["FullCrawl"].ToString()))
                FullCrawl = GetValue<bool>(configuration, "FullCrawl");
    ```

1. In the `Client` class, check the `FullCrawl` value:

    - If false – continue with the delta crawl.

    - If true – continue with the full crawl.

    Provided below are two examples of how this can be implemented for an API and for SQL. The examples are based on [Eloqua's Bulk API publicly available filter documentation](https://docs.oracle.com/en/cloud/saas/marketing/eloqua-develop/Developers/BulkAPI/Tutorials/Filtering.htm).

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

    An example using an imaginary Oracle SQL database:

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

    {:.important}
   The syntax `Contact.Field(<field name>)` must be wrapped in double brackets (as per API documentation). This is omitted here for formatting clarity.


## Stream delta crawls

Delta crawls can also be implemented as consumers for streaming platforms such as Kafka:

- If Kafka stream is not set up yet, enable Change Data Capture (CDC) on your database.

- CluedIn supports using [Debezium](https://debezium.io/documentation/) as a Kafka stream for supported databases.

- After Debezium is set up, crawlers can be integrated directly with the stream.

For a working reference, see the public [public Kafka example crawler](https://github.com/CluedIn-io/Crawling.ExampleKafka/blob/master/src/Kafka.Infrastructure/KafkaClient.cs) in CluedIn’s GitHub.
