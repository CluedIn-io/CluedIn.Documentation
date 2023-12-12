---
layout: default
nav_order: 7
parent: How-to guides
grand_parent: Installation
permalink: /deployment/infra-how-tos/configure-dns
title: Configure DNS
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}


As part of the CluedIn configuration, a base URL is used to make the application easily accessible by your browser. For proper configuration of CluedIn, you need to update the DNS settings. Specifically, you need to ensure that the A-records are configured to point either to your public IP address or a private IP address.

**Important!** Changing your DNS settings could have an impact on your TLS/SSL configuration. If you are also using specific TLS ingress hosts, they will also need to be changed to reflect your new DNS.

## DNS entries

In this article, we'll use `deparmentX` as an example of the organization name that was entered during the [installation of CluedIn](/deployment/azure-marketplace/step-3#complete-the-initial-setup-tab) and `mycompany.com` as an example of the main domain.

You need to have the **A-records** for the following DNS entries:

```
deparmentX.mycompany.com
app.mycompany.com
clean.mycompany.com
```

At CluedIn, we use the following environments:

- **Development environment** – for partners and developers to customize CluedIn.
- **Test environment** – for business users to validate the work implemented by development teams (with non-production data).
- **Production environment** – for business users to operate CluedIn using real-world data.

We recommend that you set up those environments (development, test, and production) using the name convention of your choice.

**Example of DNS entries for the CluedIn environments**

```
deparmentX.dev.mycompany.com
app.dev.mycompany.com
clean.dev.mycompany.com

deparmentX.test.mycompany.com
app.test.mycompany.com
clean.test.mycompany.com

deparmentX.prod.mycompany.com
app.prod.mycompany.com
clean.prod.mycompany.com
```

## Update DNS configuration for CluedIn

After you add the needed DNS entries, update your DNS configuration for CluedIn.

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
          # openrefine: cluedin-clean-dev
          # application: cluedin-app-dev
        
        # If you want to deviate away from the standard 'app' and 'clean' subdomains, you need to add the
        # `subdomains` block of code and ensure that they match in the global.ingress.tls.hosts section as well.
    ```
    **Note**: For environments sharing a SLD such as `customer.com`, it's important to plan the domains in advance to avoid issues during the onboarding process. 
1. Edit the value of `hostname` to reflect your desired domain for the given environment.
1. Find the **TLS hosts** section. The example of the section is shown below.

    ```yaml
    global:
      ingress:
        tls:
          hosts:
          - departmentX.20.0.189.11.sslip.io
          - app.20.0.189.11.sslip.io
          - clean.20.0.189.11.sslip.io
          - '*.20.0.189.11.sslip.io'
    ```
1. Replace the hosts section as shown below.

    ```yaml
    global:
      ingress:
        tls:
          hosts:
          - departmentX.mycompany.com
          - app.mycompany.com
          - clean.mycompany.com
          - '*.mycompany.com'
    ```

1. Save the file and apply changes from the local file to the CluedIn cluster by running the following command:  
    `helm upgrade -i cluedin-platform cluedin/cluedin-platform -n cluedin --values Cluster-Current-values.yaml`

After a short time, you'll see the confirmation of your update in the console. CluedIn is now configured to use your new DNS address.  
![configure-dns-2.png](../../assets/images/ama/howtos/configure-dns-2.png)

**Note:** This will use the LetsEncrypt service in the cluster to do an HTTP request to validate the certificate. If you would like to use a self-provided certificate, please review the [`Configure TLS Certificates`](/deployment/infra-how-tos/configure-certificates) page