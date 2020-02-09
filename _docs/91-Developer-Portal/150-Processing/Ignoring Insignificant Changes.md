---
category: Developer
title: Ignoring Insignificant Changes
---

When CluedIn processes Clues, it will generate a Hash value that will take certain values on the Clue and create a unique value that represents a hash of those values. 

By default, all changes and properties in a Clue are treated as something that will play a role in the hashing process. Developers can instruct Vocabularies to "Ignore Hashing", which means that even if these values change on subsequent crawls, it won't play a role in telling CluedIn that the data has changed. Only properties that have changed or been added that are not marked with "Ignore Hashing" will instruct CluedIn that things have changed. 

For example, many tools will change a timestamp value when the record has been viewed - not modified, but simply opened or viewed. You might find that this is important to change the clue, but in many occasions you will find that this change is insignificant and you will want to use your Vocabulary mappings to instruct CluedIn to ignore this change and throw away the Clue from processing. This is typically to help increase the performance and lack of load placed onto the CluedIn processing servers. 