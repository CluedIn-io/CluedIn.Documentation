Data Glossary

The Data Glossary allows Data Governance teams to map a proper semantic model over data that typically will come from many different sources. 

The role of the Data Glossary is to map specific business terminolgy to one or many Vocabularies via a rules engine. For example, you might find that your definition of a "Customer" is an Entity of type /Organization where the organization.type = 'Enterprise' and the salesforce.accounting.isPaid = 'true' and the dinero.invoices.paymentDate is less than today. 

Making these mappings will make it easier to query CluedIn, not having to know all the terminolgy that might not relate to your part of the business. 

To create new glossary entries, you simply will need to enter a Name, Description and map this using the rules builder. When querying based off this Glossary, CluedIn will do the underlying mapping to resolve what you actually mean when you ask CluedIn to give you a list of "Customers".

The Glossary also allows you to set a list of allowed or preferred values per Vocabulary. For example, it might be that you would like to give your downstream consumers the ability to query by a company founding date, but the value of that needs to be a 4 digit representative of a year and it can't be less that 1900 and greater than the current year. This will not only allow CluedIn to report to you on records that do not adhere to this, but it will help your Data Engineers using CluedIn Clean to understand how they should clean certain data when they see it. 

The glossary will also help different parts of the business understand what data they are working with. If you find certain terminology hard to understand, the glossary will help describe what the intention behind certain data is. For example, if we wanted to know what the salesforce.accounting.isPaid value describes, we may set a description of "this details that a customer has paid on their end, but the money has not necessarily made it into our accounts yet. To see if the money is in our account, please use dinero.invoice.isPaid and check if it is true or false".

The Data Glossary will be evaluated in the following cases:

 - Using GraphQL
 - Creating Outgoing Streams