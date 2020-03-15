---
category: Developer
title: Content Extractors
---

Content Extractors will allow you to extract raw content from files. This is typically used for extracting content from Presentations, Spreadsheets, Images, Video, Audio and other file types.

Although CluedIn supports over 350 different file types out of the box, there is often the need to support new file types. 

To implement a new Content Extractor, you will need to create a new C# class and inherit from the IContentExtractor interface. Once you have implemented the Content Extractor, simply compiling the project and adding this *.dll file to the ServerComponent folder will enable you to now extract content from those files types. 

Here is a simple example of how to implement a custom content extractor that extracts MarkDown from *.md files.

You will need to add references to the:

 - CluedIn.Core nuget package

```csharp
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Threading;

using CluedIn.Core;
using CluedIn.Core.Data.Parts;
using CluedIn.Core.FileTypes;

namespace Custom.Crawling.ContentExtraction
{
    /// <summary>
    /// The mark down content extractor.
    /// </summary>
    public class MarkDownContentExtractor : IContentExtractor
    {
        private readonly ApplicationContext context;

        private HtmlContentExtractor _htmlExtractor { get; set; }

        public MarkDownContentExtractor(ApplicationContext context)
        {
            this.context = context;
            _htmlExtractor = new HtmlContentExtractor(context);
        }

        //Friendly Name
        public string Name { get { return "Markdown"; } }

        //A score from 1 to 10 on whether this is a more important content extractor that another provider that could also extract this content.
        public int Priority { get { return 10; } }

        public StreamContent Extract(Stream stream, FileInfo fileInfo, CancellationToken cancellationToken)
        {
            var m = new MarkdownSharp.Markdown();

            var streamContent = new StreamContent();

            var documentParts = new List<IDocumentPart> { };

            using (var file = new System.IO.StreamReader(stream, Encoding.UTF8, true, 1024, true))
            {
                var raw = m.Transform(file.ReadToEnd());

                documentParts.Add(_htmlExtractor.Extract(raw));

                streamContent.DocumentParts = documentParts;

                streamContent.MetadataParts = new List<IMetadataPart>();

                return streamContent;
            }
        }

        public bool Accept(MimeType mimeType)
        {
            return mimeType.Equals(MimeType.Md);
        }

        [CanBeNull]
        public IEnumerable<EntityEdgeMap> ExtractEdges(string origin, FileInfo fileInfo)
        {
            return null;
        }
    }
}
```