Data Policies

Data Policies will allow you to generate Rules and Restrictions. Using the CluedIn Rules engine, you will be able to listen to certain data flowing through CluedIn or already persisted into the CluedIn Datastores and then react based off that. 

Rules are in place to flag when there are matches and then add an optional operation on the data associated with the match. This includes actions such as: 

 - Masking Data
 - Replacing the value with another value

 Restrictions are in place to stop the processing of data if it matches the respective business rules. For example, if you had a business rule was that you did not want to send a persons Gender to any system or make it available for the business to query, then a restriction will not only not persist this data to CluedIn, but will also not allow this data to continue process and hence in turn will not be made available in data streams or data available via the CluedIn Graph API.