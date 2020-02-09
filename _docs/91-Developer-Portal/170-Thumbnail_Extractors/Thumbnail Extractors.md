---
category: Developer
title: Thumbnail Extractors
---

Thumbnail Extractors allow you to extract images from Data. The most common use case would be to set a Preview Image of a Clue. This is common for files such as Presentations, Spreadsheets and Videos to have a sample picture to preview what the file looks like. 

There may be times where you are integrating datasources that are not supported by CluedIn. For this, you can create a new thumbnail extractor by creating a new C# class and inheriting from the IThumbnailExtractor interface. 

As an example, you could implement a new Thumbnail Extractor like so:

```csharp
using System;
using System.IO;
using System.Drawing;
using System.Threading;

using CluedIn.Core;
using CluedIn.Core.FileTypes;
using CluedIn.Core.Logging;
using CluedIn.Crawling.ContentExtraction;

namespace Custom.Images.Extractors
{
    public class ImageThumbnailGenerator : ContentExtractor, IThumbnailGenerator
    {
        private readonly ApplicationContext context;

        public ImageThumbnailGenerator(ApplicationContext context)
        {
            this.context = context;
        }

        public int Priority { get { return 10; } }

        public string Name
        {
            get { return this.GetType().Name; }
        }

        public bool Accept(MimeType type)
        {
            switch (type.Code)
            {
                case "image/jpeg":
                case "image/png":
                case "image/x-png":
                case "image/gif":
                case "image/pjpeg":
                case "image/svg+xml":
                case "image/tiff":
                    return true;
                default:
                    return false;
            }
        }

        public IThumbnail GetThumbnail(Stream stream, FileInfo fileInfo, ILogger logger, CancellationToken cancellationToken)
        {
            using (var image = stream != null ? System.Drawing.Image.FromStream(stream) : System.Drawing.Image.FromFile(fileInfo.FullName))
            {
                var newWidth  = 1600;
                var maxHeight = 1600;

                if (image.Width <= newWidth)
                {
                    newWidth = image.Width;
                }

                int newHeight = image.Height * newWidth / image.Width;
                if (newHeight > maxHeight)
                {
                    // Resize with height instead
                    newWidth = image.Width * maxHeight / image.Height;
                    newHeight = maxHeight;
                }

                Image img;

                if (image.Width != newWidth || image.Height != newHeight)
                    img = image.GetThumbnailImage(newWidth, newHeight, () => false, IntPtr.Zero);
                else
                    img = image;

                return new Thumbnail
                {
                    Data     = ImageToByte(img), 
                    Height   = img.Height,
                    Width    = img.Width,
                    MimeType = MimeType.Jpg
                };
            }
        }
    }
}
```

You will then compile and drop the DLL into the ServerComponent directory and restart CluedIn. Now, when processing certain files, CluedIn will attemp to extract richer information from it and help you generate a Preview Image automatically. 
