---
layout: cluedin
title: Setting a Preview Image for a Clue
parent: Development
nav_order: 540
permalink: /developer/clue-preview-image
tags: ["development", "clues"]
published: false
---

Your data will often contain much more than metadata in the form of textual values. You will find that binary data is often associated as metadata such as pictures, files, videos, audio and more. When it comes to data discovery, you will find that certain visual hints will make it easier to discover the data you are looking for. As a simple example, the Logo of an organization. 

The Clue object has the ability to store a single Preview Image. If you have many Preview Images, you can create multiple Clues for the same record. 

To set the Preview Image on a Clue you will need to download the binary and prepare it into a format that CluedIn would like. 

You can use the inbuilt functions that CluedIn provides to download and store the Preview Image like so:

```csharp
var previewImagePart = _fileFetcher.FetchAsRawDataPart("Your Picture Url", "/RawData/PreviewImage", "preview_{0}".FormatWith(data.Name));
 if (previewImagePart != null)
 {
     clue.Details.RawData.Add(previewImagePart);
     clue.Data.EntityData.PreviewImage = new ImageReferencePart(previewImagePart, 255, 255);
 }
```