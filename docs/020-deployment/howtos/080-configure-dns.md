---
layout: default
nav_order: 1
parent: How tos
grand_parent: Deployment
permalink: /deployment/infra-how-tos/configure-dns
title: Configure DNS
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
---


As part of the CluedIn configuration, a base URL is used to make the application easily accessible by your browser. For proper configuration of CluedIn, you need to update the DNS settings. Specifically, you need to ensure that the A-records are configured to point either to your public IP address or a private IP address.

**Important!** Changing your DNS settings could have an impact on your TLS/SSL configuration. If you are also using specific TLS ingress hosts, they will also need to be changed to reflect your new DNS.

# DNS entries

In this article, we'll use `deparmentX` as an example of the organization name that was entered during the [installation of CluedIn](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1188/Step-3-Install-on-AMA?anchor=initial-setup-tab) and `mycompany.com` as an example of the main domain.

You need to have the **A-records** for the following DNS entries:

```
deparmentX.mycompany.com
app.mycompany.com
alertmanager.mycompany.com
clean.mycompany.com
grafana.mycompany.com
prometheus.mycompany.com
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
alertmanager.dev.mycompany.com
clean.dev.mycompany.com
grafana.dev.mycompany.com
prometheus.dev.mycompany.com

deparmentX.test.mycompany.com
app.test.mycompany.com
alertmanager.test.mycompany.com
clean.test.mycompany.com
grafana.test.mycompany.com
prometheus.test.mycompany.com

deparmentX.prod.mycompany.com
app.prod.mycompany.com
alertmanager.prod.mycompany.com
clean.prod.mycompany.com
grafana.prod.mycompany.com
prometheus.prod.mycompany.com
```


# Update DNS configuration for CluedIn

After you add the needed DNS entries, update your DNS configuration for CluedIn.

**Prerequisites**

- You should be comfortable working in either PowerShell or bash terminal via Azure Cloud Shell.
- You should be connected to your AKS cluster.
See [Connect to CluedIn cluster](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1226/Connect-to-CluedIn-cluster) for detailed instructions.
- Your Helm repository is set up.
See [Helm](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1220/Helm) for detailed instructions on how to set up the repository.

If you have any questions about DNS configuration, you can request CluedIn support by sending an email to support@cluedin.com (or reach out to your delivery manager if you have a committed deal).

<hr>

**To update the DNS configuration for CluedIn**

1. Download the current cluster configuration file by running the following command:
`helm get values cluedin-platform -n cluedin -o yaml > Cluster-Current-values.yaml`
2. Open the file in nano editor by running the following command:
`nano Cluster-Current-values.yaml`
3. In the file, find a line that looks similar to the one shown below. Look for the entry named **dns**. It is the configuration that controls the DNS address used by CluedIn.
![configure-dns-1.png](../../assets/images/ama/howtos/configure-dns-1.png)
4. Edit the value of the host name to reflect your main domain. If you have 3 environments (development, test, and production), update the value of the host name for each environment (`dev.mycompany.com`, `test.mycompany.com`, `prod.mycompany.com.`).
5. Find the **TLS hosts** section. The example of the section is shown below.
```
    tls:
      hosts:
      - departmentX.20.0.189.11.sslip.io
      - app.20.0.189.11.sslip.io
      - clean.20.0.189.11.sslip.io
      - grafana.20.0.189.11.sslip.io
      - prometheus.20.0.189.11.sslip.io
      - alertmanager.20.0.189.11.sslip.io
      - '*.20.0.189.11.sslip.io'
```
6. Replace all instances of `20.0.189.11.sslip.io` to `mycopmany.com`. The example of the updated section is shown below.
```
    tls:
      hosts:
      - deparmentX.mycopmany.com
      - app.mycopmany.com
      - clean.mycopmany.com
      - grafana.mycopmany.com
      - prometheus.mycopmany.com
      - alertmanager.mycopmany.com
      - '*.mycopmany.com
```
7. If you are using multiple environments (development, test, and production), update the TLS hosts section for each environment:
   - Development – replace all instances of `20.0.189.11.sslip.io` to `dev.mycompany.com`
   - Test – replace all instances of `20.0.189.12.sslip.io` to `test.mycompany.com`
   - Production – replace all instances of `20.0.189.13.sslip.io` to `prod.mycompany.com`
8. Save the file.
9. Apply changes from the local file to the CluedIn cluster by running the following command:
```
helm upgrade -i cluedin-platform cluedin/cluedin-platform  -n cluedin --create-namespace  --values Cluster-Current-values.yaml --set application.system.runDatabaseJobsOnUpgrade=false 
```

After a short time, you'll see the confirmation of your update in the console. CluedIn is now configured to use your new DNS address.
![configure-dns-2.png](../../assets/images/ama/howtos/configure-dns-2.png)