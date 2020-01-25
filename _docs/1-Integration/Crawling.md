Crawling

Crawling servers are stateful but are transactional in nature i.e. if a complete crawl does not finish, then it will never have a state of “complete”. This also means that if you were to cancel a crawler half way through a job, that you will need to start the crawl from the start again or potentially from the data that had changed state in the source system since the last successful crawl time. Crawlers are responsible for fetching data from a source system. Crawlers are self hosted and when they are run, the CluedIn server is responsible for giving it everything that is necessary to successfully connect and pull the right data from a source system. 

It is not recommended to run a Crawling server and a Processing Server in this same CluedIn host, due to the change in nature of stateless and stateful environments. 

There are many crawlers that are provided for you in CluedIn, but if you are building your own, it is important to remember that the crawlers should not contain business logic and should not attempt to fix the data from the source. 

Crawling data can be complex and error-prone and many things can go wrong such as:

 - Time outs when calling sources
 - Network errors when calling sources
 - The source changes structure mid crawl
 - Authentication can change mid crawl
 - Source systems don't have an obvious way to filter the data

 Your crawlers will need to cater for all of the complexities mentioned above and more. You have full control over the granularity of error handling that you would like in your crawlers and hence e.g. managing how often to retry or how many times can be controlled in the crawler template framework.