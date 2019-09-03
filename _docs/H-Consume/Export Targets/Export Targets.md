Export Targets

Export Targets are used to authenticate with an integration point with the intention that CluedIn will make data available to this consumer. Good examples include: 

 - Business Intelligence Tools
 - Data Warehouse Dimension Tables
 - Machine Learning Platforms
 - Custom Applications
 - Databases

An Export Target is composed of the authentication piece involved in CluedIn and the target being able to converse, a Transform, a Target and a Matcher. 

The Transform is responsible for taking the data in CluedIn and projecting it out into a format that matches what the consumer is expecting. 

A Target is responsible for detailing the location of the data that CluedIn will send over to the consumer. 

A Matcher is responsible for determining what data will be sent over from CluedIn. 

Similar to Integrations, an Export Target may talk to a Sql Database, a Rest API, a Stream, a SOAP endpoint or more. 