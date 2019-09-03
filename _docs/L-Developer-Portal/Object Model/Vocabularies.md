Vocabularies

Vocabularies are you way to be able to describe properties that are coming in from datasources. Each Vocabulary has the following properties to set:

 - Key Name
 - Display Name
 - Data Type (of value)
 - Description
 - Visibilty
 - Editable
 - Removable
 - Personally Identifying

 To maintain proper data lineage, it is recommended that the Key Name is set to the exact same value of the property name coming in from the source system. 

 For example, if you are integrating data from a CRM system and one of the properties is named "Column_12", then even though it is tempting to change the Key Name, we would recommend that you maintain that as the Key Name and that you can set the Display Name as something different for aesthetic reasons. 

 The goal of a Vocabulary is to map into a Core Vocaulary if possible. 

 If you find that you have multiple properties from the source systems that map into the same Vocabulary Key, then it is recommend to only map one and keep the others as non-mapped Vocabulary Keys to Core Vocabularies. An example would be if you have 3 properties called Address1, Address2, Address3 then only one of these should map into the Core Vocabulary for a Company Address. You can concatenate all Address Columns into one and set it as the Core Vocabulary Key, but you might need to make a decision on what is the best way to implement this piece. 