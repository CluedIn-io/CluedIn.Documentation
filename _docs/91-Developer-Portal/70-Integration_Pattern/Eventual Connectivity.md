Eventual Connectivity

The CluedIn Eventual Connectivity pattern is at the heart of CluedIn. This pattern of integration makes it simple to blend data from many different systems into a unified and connected dataset. 

You will need to understand some of the core concepts behind the pattern:

 - Entity Codes
 - Aliases
 - Vocabularies
 - Edges
 - GraphStore
 - Shadow Entities

 The aim of CluedIn is to build a unified and connected dataset where the model of that data is generated from the data itself. This means that you don't have control over the modelling within CluedIn up-front (but you will have control later in the process). As you work more with CluedIn, you will realise that if we would like to do purpose fit modelling, then we will stream data out of CluedIn and make it available in other systems where purpose-fit modelling can be applied. 

 The Eventual Connectivity pattern is here to simplify the integration of data and to forgoe long and tedious architecture meetings to discuss how different systems will connect with each other. The Eventual Connectivity pattern will do the blending of data for you, as long as you can instruct it and guide it using the concepts mentioned above. 

 The major project advantage of this pattern is that we can take one system, actually you can even take one object in a system at a time, mark up that object and let the pattern take care of finding how it will blend. 

 With this in mind, we start by taking one system, going through an object at a time and determining what (if any) Entity Codes, Aliases and Edges exist on that object type. 

 It is also important to remember that with Edges, we do not want, or expect, you to know where this reference is pointing to - rather we would ask you to instruct us that a particular field or column should point to an Entity Code of another record. This record could be in the current system, or it could be in another system all together. 

 This becomes slightly more complex when you start working with systems that have custom business rules that dictate Entity Codes. The good thing, is that because you take this process one object or system at a time - you can talk with the product owner and domain expert of their system and ask them to help describe that the different properties entail. For example, imagine you had an identifier which wsa actually a concatenated value of two different identifers from different systems. The question needs to be asked if the concatenated version of that identifier is the Entity Code or if there are 3 Entity Codes e.g. One for each piece of the Identifier and then one to act as a unique reference in the current system. If in doubt of uniqueness, you can always mark these records as Aliases or that you can apply Entity Codes in a post processor. 