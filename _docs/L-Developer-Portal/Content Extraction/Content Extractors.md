Content Extractors

Content Extractors will allow you to extract raw content from files. This is typically used for extracting content from Presentations, Spreadsheets, Images, Video, Audio. 

Although CluedIn supports over 350 diffferent file types out of the box, there is often the need to support new file types. 

To implement a new Content Extractor, you will need to create a new C# class and inherit from the IContentExtractor interface. Once you have implemented the Content Extractor, simply compiling the project and adding this *.dll file to the ServerComponent folder will enable you to now extract content from those files types. 

