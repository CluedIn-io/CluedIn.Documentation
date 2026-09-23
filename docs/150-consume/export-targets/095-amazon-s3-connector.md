---
layout: cluedin
nav_order: 9.5
parent: Export targets
grand_parent: Consume
permalink: /consume/export-targets/amazon-s3-connector
title: Amazon S3 connector
last_modified: 2026-09-23
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to configure the Amazon S3 connector to publish data from CluedIn to an Amazon Simple Storage Service (Amazon S3) bucket.

## Prerequisites

Before configuring the connector, make sure that you have:

- An Amazon S3 bucket that CluedIn can write to.
- The AWS region where the bucket is hosted.
- An AWS access key ID and secret access key for an IAM identity that has permission to write to the bucket.
- If you want CluedIn to write objects beneath a specific path in the bucket, decide which S3 object key prefix you want to use.

{:.important}
Use credentials with only the permissions needed for the target bucket. Do not use AWS root account credentials.

## Configure Amazon S3 connector

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **Amazon S3**. Then, select **Next**.

1. On the **Configure** tab, enter the connection details:

    1. **Name** – user-friendly name of the export target that will be displayed on the **Export Target** page in CluedIn.

    1. **Access Key** – AWS access key ID for the IAM identity that CluedIn will use to access the S3 bucket.

    1. **Secret Key** – AWS secret access key associated with the access key ID.

    1. **Bucket Name** – name of the Amazon S3 bucket where CluedIn will write the exported data. Enter the bucket name only, not an S3 URL.

    1. **Region** – AWS region where the bucket is hosted, for example, `us-east-1` or `ap-southeast-2`.

    1. (Optional) **Directory (Prefix)** – S3 object key prefix under which CluedIn will store exported objects. For example, entering `master-data/customers` will place exported objects under that logical path in the bucket.

    1. **Enable Stream Cache (Sync mode only)** – enable this option if you want CluedIn to cache records and write accumulated data when using synchronized stream mode. Leave it disabled if you want records to be written without stream caching.


1. Select **Test connection** to verify that CluedIn can connect to the bucket using the supplied credentials.

1. When the connection test succeeds, select **Add**.

The Amazon S3 export target is now available to select when you configure a [stream](/consume/streams).

## AWS permissions

The IAM identity represented by the access key and secret key must have permission to access the target bucket and write exported objects to it.

The exact IAM policy depends on how you use the connector. At a minimum, make sure the identity can write objects to the configured bucket and prefix. If your synchronized stream configuration requires CluedIn to remove or replace previously exported objects, grant the corresponding object-management permissions as well.

Where possible, scope the IAM policy to only the bucket and prefix used by this export target.
