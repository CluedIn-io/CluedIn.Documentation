Core Vocabularies

Core Vocabularies are where are lot of the “smarts” in CluedIn exist. If you map your custom integration sources into Core Vocabularies, there is a high likelihood that something will be done on the data to your advantage. For example, if you map a phone number into the Core Vocabulary Phone Number then CluedIn will, amongst other things: 

Create new normalised representations of the phone number in industry standards e.g. E164. 
Will see if we can confidentially identify or merge records based off this phone number.

Important Core Vocabularies

EditUrl
PreviewUrl
Body

The role of Core Vocabularies is to merge records from different systems based off knowing that these Clues will have a different Origin. 

More often than not, you might find that you will need to introduce new Vocabularies that help you map data between different systems. It is however that you will not introduce your own Core Vocabularies. Core Vocabularies are what CluedIn produce and if you need to introduce your own Vocabulary mappings then you will build your own keys. Each key that you will introduce will need you to introduce a Processor in the processing pipeline that instructs CluedIn how to process data in those keys. It could be something as simple as it "Lowercases" the values or it could be as complex as "It runs fuzzt string manipulation over the values".
