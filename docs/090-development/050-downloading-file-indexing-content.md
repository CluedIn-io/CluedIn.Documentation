---
layout: cluedin
title: Downloading a File and Indexing the Content
parent: Development
nav_order: 050
has_children: false
permalink: {{ site.baseurl }}/development/downloading-file-indexing-content
tags: ["development","indexing"]
published: false
---

As you may be talking to datasources where the data requires you to download files, CluedIn provides a framework to download and index the content of the files. The good news is that CluedIn provides Content Extractors for the most popular of file types such as PPTX, PDF and more. This will allow you to search within the content of files. 

```csharp
        var download = new RestClient().DownloadData(new RestRequest(input.Url));
        this.Index(download, input.Filename, clue);


        public void Index(byte[] data, string filename, Clue clue)
        {
            if (data == null)
                throw new ArgumentNullException(nameof(data));

            if (clue == null)
                throw new ArgumentNullException(nameof(clue));

            if (!ConfigurationManagerEx.AppSettings.GetFlag("Crawl.InitialCrawl.FileIndexing", true))
                return;

            if (data.Length > Constants.MaxFileIndexingFileSize)
                return;

            using (var tempFile = new TemporaryFile(filename))
            {
                CreatePhysicalFile(data, tempFile);

                FileCrawlingUtility.IndexFile(tempFile, clue.Data, clue, null, _applicationContext);
            }
        }

        protected void CreatePhysicalFile(byte[] data, FileInfo info)
        {
            using (var stream = new MemoryStream(data))
            {
                using (var fs = new FileStream(info.FullName, FileMode.OpenOrCreate, FileAccess.Write))
                {
                    stream.CopyTo(fs);
                }
            }
        }

```