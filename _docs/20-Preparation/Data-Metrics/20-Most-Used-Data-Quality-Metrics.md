---
category: Preparation
title: Most Used Data Quality Metrics
---

In this article, we describe the most used data quality metrics. You can pick the ones that you want to see on your data or implement your metrics.

- [Accountability](#data-accountability)
- [Accuracy](#data-accuracy)
- [Completeness](#data-completeness)
- [Complexity](#data-complexity)
- [Connectivity](#data-connectivity)
- [Dark Data](#dark-data)
- [Flexibility](#data-flexibility)
- [Interpretability](#data-interpretability)
- [Noise](#data-noise)
- [Orderliness](#data-orderliness)
- [Relevance](#data-relevance)
- [Reliability](#data-reliability)
- [Sparsity](#data-sparsity)
- [Staleness](#data-staleness)
- [Stewardship](#data-stewardship)
- [Timeliness](#data-timeliness)
- [Uniformity](#data-uniformity)
- [Usability](#data-usability)

## Data Accountability
#### Description:
The Data Accountability metric helps to keep track of ownership of the data. The more people are responsible for a record, the higher the accountability.

#### How to improve this metric:
To improve Data Accountability, assign a product owner to every integration configuration. The more integration configurations have set product owners, the higher Data Accountability.

## Data Accuracy
#### Description:
The Accuracy is scored by the number of different data sources that are eluding to the same value of data for the same property. This does not mean that the values have to be the same but are eluding to the same value. For example, +45 53 53 53 53 might be an accurate phone number for a person, but so is 53 53 53 53. They are physically different values, but essentially, both are accurate.

#### How to improve this metric:
Use CluedIn Mesh to change the values in the source. Use CluedIn Clean to reconcile the data in CluedIn databases.

## Data Completeness
#### Description:
The Completeness is scored on whether a value is present or not. A value in our world is one that is not an empty string or Null. We treat values like Unknown, N/A, 0 as values.

#### How to improve this metric:
Add data that matches more or all properties of your Vocabulary.

## Data Complexity
#### Description:
The Complexity signals how many properties and edges does an entity have.

#### How to improve this metric:
The more properties and edges an entity has, the higher its Complexity. For some data, it’s expected to be complex. If you start to ingest data with fewer properties or edges, the Complexity will eventually go down.


## Data Connectivity
#### Description:
It is unique to CluedIn because, as part of its data layer, one of the constructs of your data that you get is a Graph. This Graph is a native graph, not just a triplet store. This means that we have a fully connected network of your data. Very similar to Google, Twitter, Facebook, and LinkedIn, the more “dense” your record is, the more “important” it is. This is not always the case, and in some cases, we are more interested in incoming connections than outgoing connections. More data that is directly or indirectly connected to a record will gain a higher connectivity score.

#### How to improve this metric:
Add more connections between your data records.

## Dark Data
#### Description:
This measures how many Shadow Entities you have. Shadow Entities are pointers to records that don’t exist yet, e.g., You are referring to a Movie, and you have the ID, but you don’t have the actual movie in your system. A high Dark Data indicates that you have to find more datasets to ingest because you are missing obvious data that exists in your business.

#### How to improve this metric:
For this metric, the less is better.
Add data that necessary to reduce the number of shadow entities. For example, if you have orders with customer IDs, but you didn’t ingest the customers with such IDs, add them to CluedIn, and the Dark Data eventually will go down.


## Data Flexibility
#### Description:
Given a record, how versatile is it in being used many times for many different reasons, i.e., how many streams involve this record where the TYPE of stream Export Target is different, e.g., Power BI is BI, Azure ML is ML. Raise flexibility by having streams go to different Export Targets.

#### How to improve this metric:
Stream your data to more platforms like PowerBI, Azure ML, SQL Server, etc.


## Data Interpretability
#### Description:
How perfect is your data at aligning to a core or non-provider-specific Vocabulary.? As soon as you see a record in CluedIn that has provider-specific Vocab, this gives the impression that records are harder to understand and indicates that you are bringing in data that you probably will not use because it is not part of a common semantic. Raise your Interpretability by adding more CORE Vocabularies to map your input data

The metric shows how many ingested properties match the core vocabulary versus the properties that don’t match. Interpretability is similar to the [Complexity](#data-complexity).

#### How to improve this metric:
Map more properties to the core vocabularies.

## Data Noise
#### Description:
This is calculated by External Data (from Enrichment Services) that are also Shadow Entities. This means that you are doing a lot of fuzzy lookups on records that have no Entity Codes to map back to your records, or your fuzzy merging is not doing a good enough job, or the data merging is not obvious. 

#### How to improve this metric:
To fix this, open the Shadow Entity Studio and start to map records together manually.


## Data Orderliness
#### Description:
This is about how pedantic you are with every data part having a matching CluedIn Clean part. This would indicate that your team essentially does a manual check and clean on every record that comes through the platform, not just the Golden Record.

#### How to improve this metric:
To fix this, you need to basically clean every data part that has ever come through.

## Data Relevance
#### Description:
Calculating Data Relevance can be tricky. Not to you and me, but for technology. First, we need to pin Relevance on something. Mostly, it will be pinned on YOU, but in this case, we are pinning it on the company, i.e., what is relevant for the company. Why? Because this is not only your data in the data hub. Sure, when you search through the data in CluedIn, it will show more relevant results to you, but that is a different use case. We score Relevance on how many hops a record is away from the business, e.g., if you are an employee of a company, you are directly connected. If you are a contact of an employee of a company, then you are two hops away. However, this is not enough. We have also coupled this with the Relevance of the actual metadata you have on those records. For example, how relevant today is it that you have the Fax number of a business? I would argue, it is not. Having their annual revenue, employee count, and website is much more relevant. We have also decided that anything that is five or more hops away from the business has a very low relevance.

The Relevance is like the [Interpretability](#data-interpretability), but the Relevance does not decrease if you ingest properties that are not mapped to the core vocabularies.

#### How to improve this metric:
Increase the number of properties matched to core vocabularies.

## Data Reliability
#### Description:
It comes down to trust. Trust comes in many ways. First, it can come from a product owner being able to influence reliability. So, the first influence to reliability is a static score of how reliable the source is. For example, it is typically mandated that HR systems keep very high-quality data. Because of this, when adding integration to CluedIn, you can set the expected reliability of the source. This is a “gut feeling,” but this also helps us give an impression of how far off your gut feeling is.

#### How to improve this metric:
Increase the source quality for your integrations.

## Data Sparsity
#### Description:
Do your records come together from a lot of places? Don’t get us wrong, high sparsity is good! It means that CluedIn is doing its job and bring records together. A Low sparsity means that your records might not be joining well.

#### How to improve this metric:
Ingest data from more sources.

## Data Staleness
#### Description:
Essentially scored based on the rate of updates in records in respect to the accuracy. A good example would be the phone number or an email. An email on a person today may be stale tomorrow. We are scoring on how long your data hub has the wrong value for a property.

#### How to improve this metric:
There’s no good or bad value for the Staleness. The more times you have updated your data in the last 30 days, the lower is Staleness.

## Data Stewardship
#### Description:
The Data Stewardship metric is scored based on how much manual cleaning, labeling, and curation has been done on a record.
The Stewardship is very similar to the [Orderliness](#data-orderliness). While the Orderliness ensures that for each non CluedIn Clean historical record, there is one from CluedIn Clean, the Stewardship calculates the ratio between the records that are coming from CluedIn Clean versus the ones that don’t come from CluedIn Clean.

#### How to improve this metric:
The more times you cleaning and editing your data, the higher the metric.

## Data Timeliness
#### Description:
Timeliness is scored on time to value and delivery. The more real-time that data is synced to the CluedIn hub and the consumers of the data, the better the Timeliness. Sometimes, you might think that you are not in control of this, and yes, there are many cases when you are not. However, one way is to increase the Timeliness is to run syncs of data more often. Yes, this will require more infrastructure, but there is a reality in real-time data that the more mature you need the data, the less real time you can get your insights.

It shows the time between ingesting a record and outputting it to a stream.

#### How to improve this metric:
The more data is used in streams, the higher the metric. The metric will eventually go down and become zero if no data was streamed in the last 30 days.


## Data Uniformity
#### Description:
Measured very similar to [Accuracy](#data-accuracy) but is much stricter. Uniformity is scored on how many different sources are eluding to the same value in the same format. The closer the format, the higher the Uniformity. For example, if one record was telling me that the industry of a company was “Software” and another record was telling me “software”, then this is very close Uniformity, but not 100%. The more divergence in values, the lower in Uniformity.

It is similar to [Accuracy](#data-accuracy), but the Uniformity is harsher and takes data types and string casing into account. This is why the Uniformity will always be lower than Accuracy.

#### How to improve this metric:
Use CluedIn Mesh to change the values in the source. Use CluedIn Clean to reconcile the data in CluedIn databases.

## Data Usability
#### Description:
Usability is scored based on the number of consumers. If you have data that many consumers constantly use, it helps speak to the data’s usability.

Of all the streams that were created, how many involve this record.

#### How to improve this metric:
Stream you data to more streams.