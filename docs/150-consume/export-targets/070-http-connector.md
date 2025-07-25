---
layout: cluedin
nav_order: 7
parent: Export targets
grand_parent: Consume
permalink: consume/export-targets/http-connector
title: HTTP connector
last_modified: 2024-10-28
---

This article outlines how to configure the HTTP connector to publish data from CluedIn to an external HTTP endpoint. We'll use the URL generated on the [Webhook.site](https://webhook.site/) as an example of an external endpoint, but you should use your own API endpoint that can be called from CluedIn.

Note that as a free user of the Webhook.site, your URL will stop accepting new requests after reaching the limit of 100 requests. Once this limit is reached, the status of the HTTP export target in CluedIn will become **Unhealthy**.

**Prerequisites:** Make sure you generate a unique URL for your external HTTP endpoint.

**To configure HTTP connector**

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **Http Connector**. Then, select **Next**.

    ![http-connector-choose-target.png]({{ "/assets/images/consume/export-targets/http-connector-choose-target.png" | relative_url }})

1. On the **Configure** tab, enter the connection details:

    1. **Name** – user-friendly name of the export target that will be displayed on the **Export Target** page in CluedIn.

    1. **Url** – unique URL of the external HTTP endpoint. The following screenshot shows the unique URL from the Webhook.site, which you can use for testing HTTP POST requests. You should provide the URL of your own endpoint.

        ![unique-url.png]({{ "/assets/images/consume/export-targets/unique-url.png" | relative_url }})

    1. **Authorization** – authorization header value. You should provide this value if your endpoint requires it.

1. Test the connection to make sure it works, and then select **Add**.

    ![http-connector-configure.png]({{ "/assets/images/consume/export-targets/http-connector-configure.png" | relative_url }})

    Now, you can select the HTTP connector in a stream and start exporting golden records.