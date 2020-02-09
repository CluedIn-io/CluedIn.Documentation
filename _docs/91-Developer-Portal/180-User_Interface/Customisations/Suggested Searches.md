Suggested Searches

Suggested searches are a way for developers to bring in related data into the single unified view of a record in the user interface of CluedIn. For example, for a company page, you might want to show the employees or you might want to show a list of all documents that are connected to this company directly or indirectly. 

For this, you can add your own custom suggested searches. Here is an example for implementing custom suggested searches.

```csharp
using System.Collections.Generic;

using CluedIn.Core;
using CluedIn.Core.Data;
using CluedIn.DataStore.Document.Models;

namespace Custom.SuggestedSearches.Providers
{
    public class DogRelatedEntitiesProvider : IRelatedEntitiesProvider
    {
        public IEnumerable<SuggestedSearch> GetRelatedEntitiesSearches(ExecutionContext context, Entity entity)
        {
            if (entity.Type != "/Dogs")
                return new SuggestedSearch[0];

            var searches = new List<SuggestedSearch>();
            if (RelatedEntitiesUtility.CypherFluentQueriesCount("Dogs connected to {{SITEID}}", entity.Id.ToString(), context) > 0)
            {
                searches.Add(new SuggestedSearch()
                                 {
                    Id = string.Join("{0}{1}", this.ToString(), "Connected"),
                    DisplayName = "Dogs from this site",
                                     SearchQuery = "Dogs connected to {{SITEID}}",
                                     Tokens = entity.Id.ToString(),
                                     Type = "List"
                                 });
            }
            if (RelatedEntitiesUtility.CypherFluentQueriesCount("Dogs connected to {{PERSONID}}", entity.Id.ToString(), context) > 0)
            {
                searches.Add(new SuggestedSearch()
                                 {
                    Id = string.Join("{0}{1}", this.ToString(), "Owns"),
                    DisplayName = "Dog Owners",
                                     SearchQuery = "Dogs connected to {{PERSONID}}",
                                     Tokens = entity.Id.ToString(),
                                     Type = "List"
                                 });
            }            

            return searches;
        }
    }
}
```

You can then compile and drop this DLL into the ServerComponent folder and reboot CluedIn to see your changes reflected in the User Interface.