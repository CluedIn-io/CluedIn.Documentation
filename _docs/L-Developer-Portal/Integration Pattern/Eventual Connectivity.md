Eventual Connectivity

The CluedIn Eventual Connectivity pattern is at the heart of CluedIn. This pattern of integration makes it simple to blend data from many different systems into a unified and connected dataset. 

You will need to understand some of the core concepts behind the pattern:

 - Entity Codes
 - Aliases
 - Vocabularies
 - Edges
 - GraphStore
 - Shadow Entities

 The aim of CluedIn is to build a unified and connected dataset where the model of that data is generated from the data itself. This means that you don't have control over the modelling within CluedIn. As you work more with CluedIn, you will realise that if we would like to do purpose fit modelling, then we will stream data our of CluedIn and make it available in other systems where purpose-fit modelling will apply. 

 The Eventual Connectivity pattern is here to simplify the integration of data and to forgo long and tedious architecture meetings to discuss how different systems will connect with each other. The Eventual Connectivity pattern will do the blending of data for you, as long as you can instruct it and guide it using the concepts mentioned above. 

 The major project advantage of this pattern is that we can take one system, actually you can even take one object in a system at a time, mark up that object and let the pattern take care of finding how it will blend. 

 With this in mind, we start by taking one system, going through an object at a time and determining what (if any) Entity Codes, Aliases and Edges exist on that object type. 

 It is also important to remember that with Edges, we do not want or expect you to know where this reference is pointing to - rather we would ask you to instruct us that a particular field or column should point to an Entity Code of another record. This record could be in the current system, or it could be in another system all together. 