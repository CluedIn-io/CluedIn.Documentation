---
layout: default
title: Spliting Records
parent: Manipulation
nav_order: 60
has_children: false
permalink: /manipulation/spliting-records
tags: ["manipulation","splitting-records"]
---

Over time you will realize that there are certain situations where the fuzzy merging engine will merge incorrectly or you have an EntityCode that you thought was unique, but isn’t. In this case you will need to split entities. One can use the CluedIn API to be able to split an Entity out into a tree of Clues and then choose the particular Clue objects that caused the bad merge to occur. After this split, CluedIn will then process the split Clues (minus the removed Clues) back into the Entity. The bad entity code will then be kept in a curated datastore so that future recrawls will not cause this issue to occur again. 

You can split an entity by making a call to the REST API via a POST to

{{url}}/api/admin/commands/split/entity?organizationId=02712a2b-b36a-4f11-95ba-d1850a311419&id=1c436fa6-f2a9-5564-aa1b-3fc61e4fd576&removeClues=2c436fa6-f2a9-5564-aa1b-3fc61e4fd576,3c436fa6-f2a9-5564-aa1b-3fc61e4fd576&executeImediately=true

This command will split the Entity record with the Id of 1c436fa6-f2a9-5564-aa1b-3fc61e4fd576 into as many clues that it was made from and then remove the two Clues with an Id of 2c436fa6-f2a9-5564-aa1b-3fc61e4fd576 and 3c436fa6-f2a9-5564-aa1b-3fc61e4fd576 and then will immediately reprocess all clues except for the 2 in the removeClues parameter. You will then (in most situations) end up with 3 records and dependent upon the data, it might be 3 entities, or a combination of 1 entity and shadow entities. 

When executeImediately is set to false only the analysis is done and the split operation is not performed. This will return a log of groupings of data parts that merges together.

Example output:
```json
{"m_MaxCapacity":2147483647,"Capacity":222080,"m_StringValue":"Id:                3b107fbc-d64a-56e8-8970-fe7fcd0e0f87
OriginEntityCode:  /Infrastructure/User#CustomerOrigin:175000304003611
RSwoosh Groups
	Group: 156
		DataPart: 5716; Name: [EntityName]
		DataPart: 2692311; Name: [EntityName]
		DataPart: 1399417; Name: [EntityName]
		...
	Group: 7438
		DataPart: 413478; Name: [EntityName]
		DataPart: 413215; Name: [EntityName]
		DataPart: 413114; Name: [EntityName]
		DataPart: 7614; Name: [EntityName]
		DataPart: 2879604; Name: [EntityName]
		DataPart: 61680; Name: [EntityName]
		DataPart: 728938; Name: [EntityName]
		DataPart: 1234206; Name: [EntityName]
		DataPart: 1889361; Name: [EntityName]
		DataPart: 32481; Name: [EntityName]
		...
TargetGroup: 7438
	DataPart: 413478; Name: [EntityName]
	DataPart: 413215; Name: [EntityName]
	DataPart: 413114; Name: [EntityName]
	DataPart: 7614; Name: [EntityName]
	DataPart: 2879604; Name: [EntityName]
	DataPart: 61680; Name: [EntityName]
	DataPart: 728938; Name: [EntityName]
	DataPart: 1234206; Name: [EntityName]
	....
	Record Attribute: Codes;
	  [EntityCodes in group]
		/Person#CluedIn(email):[email@address.com];
		/Customer#CustomerOrigin:170000351928273;
		/Infrastructure/User#CustomerOrigin:170000351928273;
		/Person#CluedIn(email):[email@address.com];
		/Customer#CustomerOrigin:196000222419740;
		/Infrastructure/User#CustomerOrigin:196000222419740;
		/Customer#CustomerOrigin:196000222321166;
		/Infrastructure/User#CustomerOrigin:196000222321166;
		/Customer#CustomerOrigin:196000221939939;
		/Infrastructure/User#CustomerOrigin:196000221939939;
    ...
	Record Attribute: Name;
		[Names in group]
		...
	Record Attribute: EntityType;
		/Infrastructure/User;
	Record Attribute: FirstName;
		[First names in group]
		...
	Record Attribute: LastName;
		[Last names in group]
		...
	Record Attribute: Email;
	  [Emails in group]
		[email@address.com];
    ...
	Record Attribute: EmailMask;
		[email@address.dummy];
	Record Attribute: Birthday;
		00000000;
		19901231;
		19710517;
		19411124;
		19340922;
	Record Attribute: Location;
		Denmark;
	Record Attribute: Address;
    [Addresses in group]
    ...
	Record Attribute: AddressCountry;
		DK;
		...
	Record Attribute: Organization;
		...
	Record Attribute: Phone;
		...
	Record Attribute: UserName;
		[email@address.com];
	Record Attribute: MiddleName;
		...
Entity: 3b107fbc-d64a-56e8-8970-fe7fcd0e0f87 - /Infrastructure/User#CustomerOrigin:175000304003611
	Removed Codes: 4;
		/Customer#CustomerOrigin:14700061000005;
		/Customer#CustomerOrigin:1674001800100;
		/Infrastructure/User#CustomerOrigin:14700061000005;
		/Infrastructure/User#CustomerOrigin:1674001800100;
	Added Codes: 0;
	All Codes: 1036;
		/Infrastructure/User#Globase:7985;
		/Infrastructure/User#CustomerOrigin:146000586143288;
		/Customer#CustomerOrigin:146000586143288;
		/Infrastructure/User#CustomerOrigin:157000129430958;
		/Customer#CustomerOrigin:157000129430958;
		/Infrastructure/User#CustomerOrigin:146000586144209;
    ...
Operations: 27
   Save Operations : 1
   Post Commands   : 26
","m_currentThread":0}}
```