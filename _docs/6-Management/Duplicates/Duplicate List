Duplicate List

Your duplicates menu will give you a list of different types of possible duplicate records. 

Clicking on the duplicate entries will allow you to see the list of possible duplicates and then place them into a merge operation as to choose which properties are more likely to be the golden value. 

As a developer, you can also add your own types of duplicate detection as well.

To do this, create a C# class and inherit from the IDuplicateQuery interface and CluedIn will then run the SearchDescriptors to generate the list. Compile your class and drop the DLL into the ServerComponent folder and reboot CluedIn.

Here as an example of a Duplicate Query detection that you could add yourself: 

public class ContractDupicate : IDuplicateQuery	
    {	
        private readonly ExecutionContext executionContext;	

        public QueryContainer Query	
        {	
            get => new QueryDescriptor<ElasticEntity>().Bool(b =>	
b.Must(a =>	
(a.Term("entityType", "/Job"))	
&& a.ConstantScore(cs => cs.Filter(f => ConfigurationManager.AppSettings.GetFlag("Feature.Filters.ShadowEntities", true) ? f.Term("isShadowEntity", "false") : f && f.ApplySecurityFilter(this.executionContext) && (!f.Exists("isExternalData") || f.Term("isExternalData", "false"))))));	
        }	
        public string DisplayName { get => "Job Query"; }	

        public ContractDupicate(ExecutionContext executionContext)	
        {	
            this.executionContext = executionContext;	
        }	
    }