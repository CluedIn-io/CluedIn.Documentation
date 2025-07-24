---
layout: cluedin
nav_order: 8
parent: Configuration
grand_parent: PaaS operations
permalink: deployment/infra-how-tos/configure-dns
title: DNS
tags: ["deployment", "ama", "marketplace", "azure", "dns", "domain name system"]
last_modified: 2024-05-09
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

As part of the CluedIn configuration, a base URL is used to make the application easily accessible by your browser. For proper configuration of CluedIn, you need to update the DNS settings. Specifically, you need to ensure that the A-records are configured to point either to your public IP address or a private IP address.

{:.important}
Changing your DNS settings could have an impact on your TLS/SSL configuration. If you are also using specific TLS ingress hosts, they will also need to be changed to reflect your new DNS.

## DNS entries

In this article, we'll use `cluedin` as the example organization name that was entered during the [installation of CluedIn](/deployment/azure-marketplace/step-3#complete-the-instance-setup-tab) and `yourdomain.com` as the example main domain.

CluedIn requires the following 3 DNS entries which can be **A-records**:

```
cluedin.yourdomain.com
app.yourdomain.com
clean.yourdomain.com
```

At CluedIn, we recommend the following environments:

- **Development** – for partners and developers to customize CluedIn.
- **Test** – for business users to validate the work implemented by development teams (with non-production data).
- **Production** – for business users to operate CluedIn using real-world data.

We recommend that you set up these environments (development, test, and production) using one the following naming conventions:

**Split by subdomain**

```
cluedin.dev.yourdomain.com
app.dev.yourdomain.com
clean.dev.yourdomain.com

cluedin.test.yourdomain.com
app.test.yourdomain.com
clean.test.yourdomain.com

cluedin.prod.yourdomain.com
app.prod.yourdomain.com
clean.prod.yourdomain.com
```

**Distinct subdomains**
```
cluedin.yourdomain.com
app.yourdomain.com
clean.yourdomain.com

cluedin-dev.yourdomain.com
app-dev.yourdomain.com
clean-dev.yourdomain.com

cluedin-test.yourdomain.com
app-test.yourdomain.com
clean-test.yourdomain.com
```

## Update DNS configuration for CluedIn

After you have decided what kind of DNS setup works for your business, the next steps are to add the needed DNS entries and update your DNS configuration for CluedIn.

**Prerequisites**

- You should be comfortable working in either PowerShell or bash terminal via Azure Cloud Shell.
- You should be connected to your AKS cluster.

    See [Connect to CluedIn cluster](/deployment/infra-how-tos/connect-to-cluedin) for detailed instructions.

- Your Helm repository is set up.

If you have any questions about DNS configuration, you can request CluedIn support by sending an email to <a href="mailto:support@cluedin.com">support@cluedin.com</a> (or reach out to your delivery manager if you have a committed deal).

<hr>

**To update the DNS configuration for CluedIn**

1. Download the current cluster configuration file by running the following command:  
    `helm get values cluedin-platform -n cluedin -o yaml > Cluster-Current-values.yaml`
1. Open the file in a text editor of your choice
1. In the file, find the block of code similar to what is shown below. Look for the entry named **dns**. It is the configuration that controls the DNS address used by CluedIn.  
    ```yaml
    global:
      dns:
        hostname: 1.2.3.4.sslip.io
        # subdomains:
          # openrefine: clean
          # application: app
        
        # If you want to deviate away from the standard 'app' and 'clean' subdomains, you need to add the
        # `subdomains` block of code and ensure that they match in the global.ingress.tls.hosts section as well.
    ```
    {:.important}
    For environments sharing a second-level domain such as `yourdomain.com`, it's important to plan the domains in advance to avoid issues during the onboarding process. 
1. Edit the value of `hostname` to reflect your desired domain for the given environment.
1. Find the **TLS hosts** section. The example of the section is shown below.

    ```yaml
    global:
      ingress:
        tls:
          hosts:
          - cluedin.1.2.3.4.sslip.io
          - app.1.2.3.4.sslip.io
          - clean.1.2.3.4.sslip.io
          - '*.1.2.3.4.sslip.io'
    ```
1. Replace the hosts section as shown below.

    ```yaml
    global:
      ingress:
        tls:
          hosts:
          - cluedin.yourdomain.com
          - app.yourdomain.com
          - clean.yourdomain.com
          - '*.yourdomain.com'
    ```

1. Save the file and apply changes from the local file to the CluedIn cluster by running the following command:  
    `helm upgrade -i cluedin-platform cluedin/cluedin-platform -n cluedin --values Cluster-Current-values.yaml`

After a short time, you'll see the confirmation of your update in the console. CluedIn is now configured to use your new DNS address.

{:.important}
This will use the LetsEncrypt service in the cluster to do an HTTP request to validate the certificate. If you would like to use a self-provided certificate, please review the [Configure TLS Certificates](/deployment/infra-how-tos/configure-certificates) page.