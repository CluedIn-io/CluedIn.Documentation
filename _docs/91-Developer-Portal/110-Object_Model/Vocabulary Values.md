---
category: Developer
title: Vocabulary Values
---

A user can set an allowed and not allowed list of terms for Vocabulary Keys. Anything that is not in the allowed list will by default be processed as normal. Any record that has a term that is in the not allowed list will be placed into the quarantine section as to resolve manually, using rules or in CluedIn Clean.

A cleaning rule could be as simple as "If I see the value GB. then change it to GB".

The allowed list is useful in times where you know the exhaustive list of values that you are allowed to have, such as country codes, dial codes and more. Most Vocabulary Keys will only need to map a not allowed list, due to the nature of not being able to guess what all the possible permutations of values are.

These lists can be managed in the Data Catalog where you can see the distribution of all values currently in the system. Using the + or - buttons, you can add these to the allowed or not allowed list. If you leave catalog values without being on a list, by default CluedIn will process them as normal. If source systems are sending data through with values that exist on the allowed list, this will add to the overall integrity quality metric of that source system. If it is the opposite and the values continue to come through on the not-allowed list, this will not affect the integrity quality metric as it is quite normal that source systems handle data differenetly.

In the profile section of the user interface, you will be able to see your data in a tabular view and the heuristics and histograms of values per "field" that don't comply to an allowed list or are on the not allowed list. This can help give an indication of the quality of data.

Allowed and not allowed values can be statically entered. You can specify these as ranges, individual values or simple rules e.g. "cannot be larger than 15" or "must be hubspot.dealAmount x 12".

The Profile section is run in realtime and hence as soon as a value is detected as not allowed, it will populate this in the quarantine and that particular record will be queued separately for resolution. It can also be configured that only the property that has the non-allowed value will be queued, the rest of the record will be processed. When the resolution has been made in the quarantine section, it will show the lineage that the record came from the source AND that it was then resolved in the quarantine section.

For more complex rules such as relationship requirements or exceptions e.g. "Person cannot be connected to Contact Directly" then please see the developer section on how to implement IQuarantineRule.

Main features:

1: Allows you to set auto tranform/correct rules on values seen in the past.

2: Allows CluedIn to pre-load our core Vocabularies with allowed values for anomaloy detection.

3: Allows profiling and analytics to be run on the distribtuion of quality on a Vocabulary level.

4: Allows our MDM component to select a better display value.

5: Allows CluedIn Clean to indicate what you should normalise too. Also, it can use the Regex to determine patterns for known things like Post Codes etc. Maybe it could say "This looks like a British Post Code"

6: Allows you to set rules like "This must be uppercase"

7: If I am projecting out MONEY, I need to know denomination .

8: We can list Edges per Entity Type i.e. the relationships that exist.

9: Marking allowed terms will train CluedIn to detect bad values in the future.