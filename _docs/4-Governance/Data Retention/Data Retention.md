Data Retention

Data Retention allows us to set temporal based limits on how long we can retain certain data. Rules on retention will change per industry, country and use case. Becasue of this, CluedIn supports a generic retention framework that allows a user to specify some rules, which will then in turn either archive, purge (or other) data from CluedIn. If you have chosen to implement the Mesh API queries for these mutation commands, then these will also be triggered. This means that CluedIn can support Retention policies in integrated systems as well. 

There are two ways to setup retention periods in CluedIn. The first is to set a Rule / Graph QL query that matches the data you would like to periodically action. You will also set a retention period. 

When those periods are set to run, it will instruct CluedIn to queue all operations needed to complete the process and will ask the approriate owners to do the work. 

The other way is for setting retention on an individual record.