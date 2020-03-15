---
category: Manipulation
title: Splitting Records
---

Over time you will realise that there are certain situations where the fuzzy merging engine will merge incorrectly or you have an EntityCode that you thought was unique, but isn’t. In this case you will need to split entities. One can use the CluedIn API to be able to split an Entity out into a tree of Clues and then choose the particular Clue objects that caused the bad merge to occur. After this split, CluedIn will then process the split Clues (minus the removed Clues) back into the Entity. The bad entity code will then be kept in a curated datastore so that future recrawls will not cause this issue to occur again. 

You can split an entity by making a call to the REST API via a POST to

{{url}}/api/admin/commands/split/entity?organizationId=02712a2b-b36a-4f11-95ba-d1850a311419&id=1c436fa6-f2a9-5564-aa1b-3fc61e4fd576&removeClues=2c436fa6-f2a9-5564-aa1b-3fc61e4fd576,3c436fa6-f2a9-5564-aa1b-3fc61e4fd576&executeImediately=true

This command will split the Entity record with the Id of 1c436fa6-f2a9-5564-aa1b-3fc61e4fd576 into as many clues that it was made from and then remove the two Clues with an Id of 2c436fa6-f2a9-5564-aa1b-3fc61e4fd576 and 3c436fa6-f2a9-5564-aa1b-3fc61e4fd576 and then will immediately reprocess all clues except for the 2 in the removeClues parameter. You will then (in most situations) end up with 3 records and dependent upon the data, it might be 3 entities, or a combination of 1 entity and shadow entities. 
